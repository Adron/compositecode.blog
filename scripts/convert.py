"""Convert posts/_raw/posts.json into Markdown files with YAML front matter.

Writes posts/YYYY/YYYY-MM-DD-slug.md and posts/_raw/media.json, the list of images to download
(consumed by download_media.py). Image references are rewritten to site-root paths:
  compositecode.blog uploads  -> /wp-content/uploads/...   (same URL as on WordPress)
  author-owned image hosts    -> /images/<host>/...
  everything else             -> original URL with the WordPress.com Photon proxy removed
"""
import html
import json
import re
from datetime import datetime
from pathlib import Path
from urllib.parse import unquote, urlsplit

import yaml
from bs4 import BeautifulSoup, NavigableString
from markdownify import MarkdownConverter

ROOT = Path(__file__).resolve().parent.parent
POSTS = ROOT / "posts"
RAW = POSTS / "_raw"

PHOTON = re.compile(r"^https?://i[0-3]\.wp\.com/")
BLOG_HOSTS = {"compositecode.blog", "www.compositecode.blog", "compositecode.com", "www.compositecode.com",
              "compositecode.files.wordpress.com", "compositecode.wordpress.com"}
OWNED_IMAGE_HOSTS = {"adronhall.smugmug.com", "photos.adron.me", "photos.smugmug.com", "adron.github.io"}
OLD_BLOG_HOSTS = BLOG_HOSTS | {"adronbhall.com", "www.adronbhall.com", "blog.adron.me"}
IMAGE_EXT = re.compile(r"\.(png|jpe?g|gif|webp|svg|bmp)$", re.I)
# [sourcecode lang="x"]...[/sourcecode] blocks, optionally wrapped in <pre> or <p>
SHORTCODE = re.compile(r"(?:<pre[^>]*>\s*)?(?:<p>)?\[(sourcecode|code|source)\b([^\]]*)\](.*?)\[/\1\]"
                       r"(?:\s*</p>)?(?:\s*</pre>)?", re.S)
# WordPress's wptexturize ran over shortcode bodies; undo its substitutions inside code
UNTEXTURIZE = str.maketrans({"\u201c": '"', "\u201d": '"', "\u2033": '"', "\u2018": "'", "\u2019": "'",
                             "\u2032": "'", "\u2013": "--", "\u2014": "---", "\u2026": "...", "\u00d7": "x"})
EXT_LANG = {"js": "javascript", "ts": "typescript", "py": "python", "rb": "ruby", "go": "go", "cs": "csharp",
            "java": "java", "sh": "bash", "json": "json", "yml": "yaml", "yaml": "yaml", "sql": "sql",
            "html": "html", "xml": "xml", "css": "css", "md": "markdown", "rs": "rust", "tf": "hcl"}

media = {}  # local path -> list of source URLs to try, in order
# images that 404 everywhere (written by download_media.py); keep their original URL instead of a dead local path
failed_media = set(json.loads((RAW / "media_failures.json").read_text())) if (RAW / "media_failures.json").exists() else set()
known_permalinks = set()


def unwrap_photon(url):
    """https://i0.wp.com/host/path?resize=.. -> https://host/path"""
    url = html.unescape(url).strip()
    if PHOTON.match(url):
        url = "https://" + PHOTON.sub("", url).split("?", 1)[0]
    return url


def local_image(url):
    """Map an image URL to its local site path (registering it for download), or return the cleaned remote URL."""
    origin = unwrap_photon(url)
    parts = urlsplit(origin)
    host, path = parts.netloc.lower(), unquote(parts.path)
    if not IMAGE_EXT.search(path):
        return origin
    if host in BLOG_HOSTS:
        m = re.search(r"/(?:wp-content/uploads/|(?=\d{4}/\d{2}/))(.+)$", path)
        if not m:
            return origin
        rel = m.group(1)
        local = "/wp-content/uploads/" + rel
        encoded = re.search(r"(?:/uploads/|/)(\d{4}/\d{2}/.+)$", parts.path).group(1)
        sources = [f"https://compositecode.blog/wp-content/uploads/{encoded}",
                   f"https://i0.wp.com/compositecode.blog/wp-content/uploads/{encoded}"]
    elif host in OWNED_IMAGE_HOSTS:
        safe = re.sub(r"[^A-Za-z0-9._/-]+", "-", path).strip("/")
        local = f"/images/{host}/{safe}"
        # Photon keeps copies of images that have since vanished from SmugMug; cap width to keep the repo small.
        sources = [f"https://i0.wp.com/{host}{parts.path}?w=1600", f"https://{host}{parts.path}"]
    else:
        return origin
    if local in failed_media:
        return origin
    media.setdefault(local, sources)
    return local


def internal_link(url):
    """Turn links to this blog (current or old domains) into site-root paths."""
    u = html.unescape(url).strip()
    parts = urlsplit(u)
    if parts.netloc.lower() not in OLD_BLOG_HOSTS:
        return url
    path = parts.path if parts.path.endswith("/") or "." in parts.path.rsplit("/", 1)[-1] else parts.path + "/"
    if parts.netloc.lower() in ("compositecode.blog", "www.compositecode.blog") or path in known_permalinks:
        if IMAGE_EXT.search(parts.path):
            return local_image(u)
        if "/wp-content/uploads/" in parts.path:  # PDFs and other attachments
            local = unquote(parts.path)
            if local in failed_media:
                return u
            media.setdefault(local, [f"https://compositecode.blog{parts.path}"])
            return local
        return path + (f"?{parts.query}" if parts.query else "") + (f"#{parts.fragment}" if parts.fragment else "")
    return url


def code_block(soup, text, lang=None):
    pre = soup.new_tag("pre")
    text = text.replace("\xa0", " ").replace("\r\n", "\n").strip("\n")
    if lang:
        pre["data-lang"] = lang.lower()
    pre.append(NavigableString(text))
    return pre


def pre_text(el):
    for br in el.find_all("br"):
        br.replace_with("\n")
    lines = el.select(".cm-line")
    if lines:
        return "\n".join(line.get_text() for line in lines)
    return el.get_text()


def pre_lang(el):
    if el.get("data-lang"):
        return el["data-lang"]
    classes = " ".join(el.get("class", []) + [c for d in el.find_all(True) for c in d.get("class", [])])
    for pat in (r"brush:\s*([\w+#-]+)", r"language-([\w+#-]+)", r"\bhighlight\s+([\w+#-]+)", r"lang-([\w+#-]+)"):
        m = re.search(pat, classes)
        if m and m.group(1) not in ("plaintext", "text", "plain"):
            return m.group(1)
    parent = el.parent
    if parent is not None:
        m = re.search(r"highlight-(?:source-)?([\w+#-]+)", " ".join(parent.get("class", [])))
        if m:
            return m.group(1)
    return None


def shortcode_to_pre(m):
    attrs = html.unescape(m.group(2))
    body = re.sub(r"<br\s*/?>\n?", "\n", m.group(3))
    body = re.sub(r"</p>\s*<p>", "\n\n", body)
    body = html.unescape(re.sub(r"<[^>]+>", "", body)).translate(UNTEXTURIZE).strip("\n")
    found = re.findall(r"=[\"'\u201c\u201d\u2033]?([\w+#-]+)", attrs)  # last value wins on malformed attrs
    lang = f' data-lang="{found[-1].lower()}"' if found else ""
    return f"<pre{lang}>{html.escape(body, quote=False)}</pre>"


def preprocess(content):
    soup = BeautifulSoup(SHORTCODE.sub(shortcode_to_pre, content), "html.parser")

    # Live Writer / CopySourceAsHtml: one <pre> per line inside div.csharpcode
    for div in soup.select("div.csharpcode"):
        if div.select_one("pre[data-lang]"):
            div.unwrap()
            continue
        lines = [pre_text(p) for p in div.find_all("pre")]
        div.replace_with(code_block(soup, "\n".join(lines)))

    # Pasted GitHub gist markup: rebuild as a code block plus a link to the gist
    for div in soup.select("div.gist"):
        rows = div.select("td.blob-code")
        meta = div.select_one(".gist-meta a[href]")
        name = div.select_one(".gist-meta a:nth-of-type(2)")
        ext = name.get_text().rsplit(".", 1)[-1].lower() if name and "." in name.get_text() else ""
        block = code_block(soup, "\n".join(r.get_text() for r in rows), EXT_LANG.get(ext))
        div.replace_with(block)
        if meta:
            p = soup.new_tag("p")
            a = soup.new_tag("a", href=meta["href"].replace("/raw/", "/").split("/raw")[0])
            a.string = "View the gist on GitHub"
            p.append(a)
            block.insert_after(p)

    for pre in soup.find_all("pre"):
        pre.replace_with(code_block(soup, pre_text(pre), pre_lang(pre)))

    # Jetpack tiled galleries -> plain images
    for gallery in soup.select("div.tiled-gallery"):
        wrapper = soup.new_tag("div")
        for img in gallery.find_all("img"):
            p = soup.new_tag("p")
            p.append(soup.new_tag("img", src=img.get("data-orig-file") or img.get("src", ""),
                                  alt=img.get("alt") or img.get("data-image-title", "")))
            wrapper.append(p)
        gallery.replace_with(wrapper)

    for img in soup.find_all("img"):
        src = img.get("data-orig-file") or img.get("src")
        if not src:
            img.decompose()
            continue
        keep = {"alt": img.get("alt", ""), "title": img.get("title")}
        img.attrs = {"src": local_image(src), **{k: v for k, v in keep.items() if v}}

    for a in soup.find_all("a", href=True):
        href = a["href"]
        a["href"] = local_image(href) if IMAGE_EXT.search(urlsplit(unwrap_photon(href)).path) else internal_link(href)

    for iframe in soup.find_all("iframe"):
        iframe["src"] = html.unescape(iframe.get("src", "")).replace("http://", "https://", 1)

    return soup


class Converter(MarkdownConverter):
    def _raw(self, el):
        return "\n\n" + str(el) + "\n\n"

    def convert_iframe(self, el, text, parent_tags):
        return self._raw(el)

    convert_video = convert_audio = convert_object = convert_embed = convert_script = convert_iframe

    def convert_blockquote(self, el, text, parent_tags):
        if "twitter-tweet" in el.get("class", []) or "instagram-media" in el.get("class", []):
            return self._raw(el)
        return super().convert_blockquote(el, text, parent_tags)

    def convert_figcaption(self, el, text, parent_tags):
        return "\n\n*" + text.strip() + "*\n\n" if text.strip() else ""


def to_markdown(content):
    soup = preprocess(content)
    md = Converter(heading_style="ATX", bullets="-", code_language_callback=lambda el: el.get("data-lang"),
                   escape_misc=False).convert_soup(soup)
    md = re.sub(r"[ \t]+\n", "\n", md)
    return re.sub(r"\n{3,}", "\n\n", md).strip() + "\n"


def plain(text):
    text = BeautifulSoup(html.unescape(text or ""), "html.parser").get_text(" ")
    text = re.sub(r"\[/?(?:sourcecode|code|source)\b[^\]]*\]", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return re.sub(r"\s*(Continue reading.*|\[…\]|\[\.\.\.\])$", "", text).strip()


def offset(local, gmt):
    delta = datetime.fromisoformat(local) - datetime.fromisoformat(gmt)
    minutes = round(delta.total_seconds() / 60)
    sign = "+" if minutes >= 0 else "-"
    return f"{sign}{abs(minutes) // 60:02d}{abs(minutes) % 60:02d}"


def main():
    posts = json.loads((RAW / "posts.json").read_text())
    cats = {c["id"]: html.unescape(c["name"]) for c in json.loads((RAW / "categories.json").read_text())}
    tags = {t["id"]: html.unescape(t["name"]) for t in json.loads((RAW / "tags.json").read_text())}
    known_permalinks.update(urlsplit(p["link"]).path for p in posts)

    for p in posts:
        permalink = urlsplit(p["link"]).path
        date = p["date"]
        front = {
            "title": html.unescape(p["title"]["rendered"]),
            "date": f"{date.replace('T', ' ')} {offset(date, p['date_gmt'])}",
            "last_modified_at": f"{p['modified'].replace('T', ' ')} {offset(p['modified'], p['modified_gmt'])}",
            "permalink": permalink,
            "slug": unquote(p["slug"]),
            "wp_id": p["id"],
            "original_url": p["link"],
            "categories": [cats[c] for c in p["categories"] if c in cats],
            "tags": [tags[t] for t in p["tags"] if t in tags],
        }
        excerpt = plain(p["excerpt"]["rendered"])
        if excerpt:
            front["excerpt"] = excerpt
        if p.get("jetpack_featured_media_url"):
            front["image"] = local_image(p["jetpack_featured_media_url"])
        if p.get("format") and p["format"] != "standard":
            front["format"] = p["format"]

        body = to_markdown(p["content"]["rendered"])
        out = POSTS / date[:4] / f"{date[:10]}-{unquote(p['slug'])}.md"
        out.parent.mkdir(parents=True, exist_ok=True)
        fm = yaml.safe_dump(front, allow_unicode=True, sort_keys=False, width=10_000)
        out.write_text(f"---\n{fm}---\n\n{body}")

    (RAW / "media.json").write_text(json.dumps(media, indent=1))
    print(f"wrote {len(posts)} posts, {len(media)} images to download")


if __name__ == "__main__":
    main()
