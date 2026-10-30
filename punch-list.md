# WordPress → GitHub Pages migration punch list

Running checklist for moving compositecode.blog off WordPress.com. Check items off as they land.

## Content export

- [x] Export all 1,479 published posts to Markdown with front matter (`posts/_posts/`)
- [x] Export all 131 published pages (`pages/`)
- [x] Download images and attachments, keeping `/wp-content/uploads/...` paths (2,120 files)
- [x] Rehost your own SmugMug / `adron.github.io` images locally under `/images/`
- [x] Convert all six legacy code-block formats to fenced code blocks with languages
- [x] Strip Jetpack contact/subscribe forms, which can't work on a static site
- [x] Resize oversized stock JPEGs (over 2 MB) to 2400 px, saving 124 MB
- [x] Re-sync check on 2026-10-30: no new posts since 2026-10-09
- [ ] Final re-sync right before DNS cutover (see README, "Re-running the WordPress export")
- [ ] Upload the 4 large slide decks to the `attachments` GitHub Release (files are outside the repo; links already point at the release)
- [ ] Rehost the 7 VideoPress embeds (YouTube or similar) before cancelling WordPress; they stop working when the plan ends
  - `/2010/06/10/first-post-code-kata-alpha-counter/`, `/2010/08/09/aws-5-minute-quick-start/`, `/2010/12/07/windows-azure-sdk-1-3-broken-deployments/`, `/2011/03/29/aws-linux-ec2-wordpress-free/`, `/2011/04/03/deploying-asp-net-mvc-3-razor-web-app-to-appharbor-4-minutes/`, `/2018/09/17/strata-ninjas-distributed-data-day-and-graph-day-trip-recap/`, `/2024/05/02/software-development-getting-started-by-getting-organized/`
- [ ] Decide on the 7 unattached video attachment pages in the WP video sitemap (`/hashiconf-trip-day-1-mp4/` etc.): rehost and add pages, or let them 404
- [ ] Export the 1,219 comments (needs a WXR export from wp-admin) if you want them archived
- [ ] Export the Jetpack email subscriber list before cancelling (can't be moved automatically)
- [ ] Optional: check for drafts or private posts (not visible to the public API; WXR export from wp-admin)
- [ ] Optional: the 2013-12-08 restify post has an unclosed `[sourcecode]` block (already broken on WordPress)

## URL / SEO preservation

- [x] Every post keeps its exact WordPress URL (`/YYYY/MM/DD/slug/`), pinned in front matter
- [x] New posts get the same URL shape automatically (`permalink: /:year/:month/:day/:title/`)
- [x] Pages keep their exact URLs, including nested ones (`/projects/hasura-short-bits/`)
- [x] Category and tag archives at WordPress slugs (`/category/<slug>/`, `/tag/<slug>/`)
- [x] Year, month and day archives (`/2026/`, `/2026/10/`, `/2026/10/09/`)
- [x] Home pagination at `/page/N/`
- [x] Feed at `/feed/` (Atom) plus `/feed.xml`
- [x] `sitemap.xml` and `robots.txt`
- [x] `/?p=123` and `/?page_id=45` links forward to the right post (`/wp-ids.json` lookup)
- [x] Redirect pages for old page paths WordPress was forwarding (`_data/redirects.yml`, 14 entries)
- [x] Canonical URLs, Open Graph and Twitter cards via jekyll-seo-tag, all on `https://compositecode.blog`
- [x] Preview at github.io is `noindex` so it can't compete with the real domain
- [x] Verified: 3,832 of 3,839 URLs from the live sitemap and API exist in the build; the 7 gaps are the video attachment pages above
- [ ] Not preserved (low value, noted for completeness): `/category/x/page/2/` paginated term archives, `/author/adron/`, `/comments/feed/`, per-post `/feed/`, and `wp.me` short links
- [ ] After cutover: submit `https://compositecode.blog/sitemap.xml` in Google Search Console and Bing Webmaster Tools
- [ ] After cutover: watch Search Console "Not found (404)" for a few weeks; add stragglers to `_data/redirects.yml`

## GitHub hosting

- [x] Jekyll 4 site with custom layouts (light/dark), built by GitHub Actions
- [x] Deploy workflow (`.github/workflows/pages.yml`), with a daily rebuild for scheduled posts
- [ ] Enable GitHub Pages (Source: GitHub Actions) and confirm the first deploy
- [ ] Review the preview at https://adron.github.io/compositecode.blog/
- [ ] Optional: site search (e.g. Pagefind in the build step)
- [ ] Optional: comments for new posts (e.g. giscus)

## Domain / DNS cutover

Current state (checked 2026-10-30): registered with Automattic (WordPress.com) until 2028-04-17, nameservers `ns1–3.wordpress.com`, A records `192.0.78.133` / `192.0.78.253`, WordPress sends HSTS with `max-age=31536000`.

- [ ] Verify `compositecode.blog` for GitHub Pages in your GitHub account settings (adds a `_github-pages-challenge-Adron` TXT record) to block domain takeovers
- [ ] A day before: lower the DNS TTL on the apex and `www` records
- [ ] Set the custom domain to `compositecode.blog` in the repo's Pages settings
- [ ] Replace the apex A records with GitHub's:
  - A: `185.199.108.153`, `185.199.109.153`, `185.199.110.153`, `185.199.111.153`
  - AAAA: `2606:50c0:8000::153`, `2606:50c0:8001::153`, `2606:50c0:8002::153`, `2606:50c0:8003::153`
- [ ] `www` CNAME → `adron.github.io` (GitHub then redirects `www` to the apex)
- [ ] Keep the existing TXT records (SPF `include:_spf.wpcloud.com`, `openai-domain-verification`)
- [ ] Wait for GitHub to issue the Let's Encrypt certificate, then tick **Enforce HTTPS**
  - Do this at a quiet time: browsers that cached WordPress's HSTS header will show certificate errors until the certificate is issued (usually minutes, up to about an hour)
- [ ] Confirm `http://` → `https://` and `www` → apex redirects; spot-check old URLs, `/feed/`, and `/?p=75418`
- [ ] Optional: move DNS (and later the registration) away from WordPress.com, e.g. to Cloudflare or another registrar; keep paying for the registration either way

## WordPress.com wind-down (only after the new site is live and verified)

- [ ] Final content re-sync and comparison
- [ ] Rehost VideoPress videos (above)
- [ ] Export subscribers and comments (above)
- [ ] Cancel the WordPress.com hosting plan, keeping the domain registration if DNS stays there
