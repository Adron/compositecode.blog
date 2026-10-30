"""Download the images listed in posts/_raw/media.json into the site root, trying each source URL in order.

Already-downloaded files are skipped, so the script can be re-run. Failures go to posts/_raw/media_failures.json.
"""
import json
import subprocess
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RAW = ROOT / "posts" / "_raw"


def fetch(local, sources):
    dest = ROOT / local.lstrip("/")
    if dest.exists() and dest.stat().st_size > 0:
        return local, "exists"
    dest.parent.mkdir(parents=True, exist_ok=True)
    tmp = dest.with_name(dest.name + ".part")
    for url in sources:
        res = subprocess.run(
            ["curl", "-sSL", "--fail", "--max-time", "120", "-o", str(tmp), "-w", "%{content_type}", url],
            capture_output=True, text=True,
        )
        if res.returncode == 0 and not res.stdout.startswith("text/html"):
            tmp.rename(dest)
            return local, "ok"
        tmp.unlink(missing_ok=True)
    return local, "failed"


def main():
    media = json.loads((RAW / "media.json").read_text())
    for hosted_elsewhere in json.loads((RAW / "release_assets.json").read_text()):
        media.pop(hosted_elsewhere, None)
    failures_file = RAW / "media_failures.json"
    failures = json.loads(failures_file.read_text()) if failures_file.exists() else {}
    counts = {}
    with ThreadPoolExecutor(max_workers=8) as pool:
        for i, (local, status) in enumerate(pool.map(lambda kv: fetch(*kv), media.items()), 1):
            counts[status] = counts.get(status, 0) + 1
            if status == "failed":
                failures[local] = media[local]
            else:
                failures.pop(local, None)
            if i % 200 == 0:
                print(f"{i}/{len(media)} {counts}")
    failures_file.write_text(json.dumps(failures, indent=1))
    print(f"done: {counts}")


if __name__ == "__main__":
    main()
