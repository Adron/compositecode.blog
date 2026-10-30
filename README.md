# Composite Code

The source for [compositecode.blog](https://compositecode.blog): 20 years of posts, exported from WordPress.com and served as a Jekyll site from GitHub Pages. Migration status lives in [punch-list.md](punch-list.md).

## Layout

| Path | What it is |
| --- | --- |
| `posts/_posts/YYYY/` | Posts, one Markdown file each (`YYYY-MM-DD-slug.md`) |
| `pages/` | Standalone pages (About, Projects, etc.), each with a `permalink` |
| `wp-content/uploads/`, `images/` | Images and attachments, at the same URLs they had on WordPress |
| `_data/terms.json` | Category/tag name → WordPress slug, so `/category/<slug>/` and `/tag/<slug>/` URLs stay put |
| `_data/redirects.yml` | Old paths that forward to current ones |
| `_plugins/wordpress_compat.rb` | Category, tag and date archives, redirect pages, `/?p=123` lookup, preview base-path rewriting |
| `posts/_raw/` | Raw WordPress API JSON and the media manifests (not published) |
| `scripts/` | The export pipeline |

## Writing a new post

Add `posts/_posts/<year>/YYYY-MM-DD-your-slug.md`:

```markdown
---
title: "Your Title"
date: 2026-11-02 09:00:00 -0800
categories: [Some Category]
tags: [some tag, another tag]
---

Post body in Markdown.
```

It publishes at `/2026/11/02/your-slug/`, the same URL shape WordPress used. To use a different slug than the filename, set `slug:`. Posts dated in the future go live on the first daily rebuild after their date. New categories and tags get archive pages automatically.

Images go in `wp-content/uploads/YYYY/MM/` (or anywhere else in the repo). Reference them with a root path, such as `/wp-content/uploads/2026/11/diagram.png`.

## Running locally

```sh
bundle install
bundle exec jekyll serve      # http://127.0.0.1:4000
```

## Deploying

Pushing to `main` runs `.github/workflows/pages.yml`, which builds the site and deploys it to GitHub Pages. It also rebuilds daily so scheduled posts publish.

## Re-running the WordPress export

Only needed while WordPress is still live. This overwrites the exported posts and pages, so don't run it after editing them here.

```sh
python3 -m venv .venv && .venv/bin/pip install markdownify pyyaml
.venv/bin/python scripts/fetch.py           # API -> posts/_raw/*.json
.venv/bin/python scripts/convert.py         # JSON -> posts/_posts, pages, _data/terms.json
.venv/bin/python scripts/download_media.py  # new images/attachments
.venv/bin/python scripts/convert.py         # again, so links to images that failed to download point at their original URLs
```
