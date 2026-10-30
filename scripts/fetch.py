"""Download raw post, page, category, tag, and user JSON from the public WordPress REST API into posts/_raw/.

Requests go through curl: WordPress.com serves a JavaScript bot challenge to Python's urllib
but not to curl.
"""
import json
import re
import subprocess
import time
from pathlib import Path

API = "https://compositecode.blog/wp-json/wp/v2"
RAW = Path(__file__).resolve().parent.parent / "posts" / "_raw"


def get(url, tries=4):
    for attempt in range(tries):
        res = subprocess.run(
            ["curl", "-sS", "--fail", "-D", "-", "--max-time", "120", url],
            capture_output=True, text=True,
        )
        if res.returncode == 0:
            headers, _, body = res.stdout.partition("\n\n")
            pages = re.search(r"(?im)^x-wp-totalpages:\s*(\d+)", headers)
            return json.loads(body), int(pages.group(1)) if pages else 1
        if attempt == tries - 1:
            raise RuntimeError(f"{url}: {res.stderr.strip()}")
        print(f"  retry {url}: {res.stderr.strip()}")
        time.sleep(2 ** attempt)


def fetch_all(endpoint):
    items, page, pages = [], 1, 1
    while page <= pages:
        batch, pages = get(f"{API}/{endpoint}?per_page=100&page={page}&orderby=id&order=asc")
        items.extend(batch)
        print(f"{endpoint}: page {page}/{pages} ({len(items)} items)")
        page += 1
    return items


def main():
    RAW.mkdir(parents=True, exist_ok=True)
    for endpoint in ("categories", "tags", "posts", "pages", "users"):
        items = fetch_all(endpoint)
        (RAW / f"{endpoint}.json").write_text(json.dumps(items, ensure_ascii=False, indent=1))


if __name__ == "__main__":
    main()
