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
- [x] Home pagination at `/page/N/`, 5 posts per page as on WordPress (296 pages, same posts on each page number; spot-checked against live)
- [x] Paginated category, tag and date archives at `<archive>/page/N/`, page counts verified against live
- [x] Author archive at `/author/adron/` (paginated)
- [x] Feed at `/feed/` (Atom) plus `/feed.xml`
- [x] `sitemap.xml` and `robots.txt`
- [x] `/?p=123` and `/?page_id=45` links forward to the right post (`/wp-ids.json` lookup)
- [x] Redirect pages for old page paths WordPress was forwarding (`_data/redirects.yml`, 14 entries)
- [x] Canonical URLs, Open Graph and Twitter cards via jekyll-seo-tag, all on `https://compositecode.blog`
- [x] Preview at github.io is `noindex` so it can't compete with the real domain
- [x] Verified: 3,832 of 3,839 URLs from the live sitemap and API exist in the build; the 7 gaps are the video attachment pages above
- [ ] Not preserved (low value, noted for completeness): `/comments/feed/`, per-post `/feed/`, and `wp.me` short links
- [ ] After cutover: submit `https://compositecode.blog/sitemap.xml` in Google Search Console and Bing Webmaster Tools
- [ ] After cutover: watch Search Console "Not found (404)" for a few weeks; add stragglers to `_data/redirects.yml`

## Theme (Colinear)

- [x] Identified the live theme: Colinear by Automattic (GPL), with your WordPress.com Custom Colors
- [x] Ported Colinear's stylesheets unmodified (`assets/css/colinear/`), plus the captured Custom Colors CSS
- [x] Self-hosted Genericons (menu icons); Open Sans, Lora and Inconsolata via Google Fonts, as on WordPress
- [x] Layouts rebuilt on Colinear's markup: masthead, primary menu with dropdowns, right sidebar, entry header/footer, author box, post navigation, archive headers
- [x] Primary menu copied from the WordPress "Nav" menu (`_includes/primary-menu.html`)
- [x] Colinear's `navigation.js` ported (dropdown toggles rewritten without jQuery)
- [x] Sidebar: Recent Posts, Blog Feeds, Search (site-restricted Google search), monthly Archive dropdown
- [x] Compared side by side with the live site in a browser (desktop): post, home, category archive, menu dropdowns
- [ ] Check the mobile layout and menu toggle on a phone (couldn't resize the browser during the session)
- [ ] Decide on "Follow via Email": Jetpack's form can't work off WordPress; pick a newsletter service (Buttondown, Substack, etc.), import the 303 subscribers, and add its form to `_includes/sidebar.html`
- [ ] Dropped on purpose: "My Upcoming Events" widget (was empty), EU cookie banner (only needed for WordPress.com's cookies), Jetpack likes/sharing buttons, comments feed link
- [ ] Optional: add a favicon (WordPress was serving its generic default icon)

## GitHub hosting

- [x] Jekyll 4 site using the Colinear theme, built by GitHub Actions
- [x] Deploy workflow (`.github/workflows/pages.yml`), with a daily rebuild for scheduled posts
- [x] Enable GitHub Pages (Source: GitHub Actions) and confirm the first deploy (2026-10-30)
- [ ] Review the preview at https://adron.github.io/compositecode.blog/ (deployed and smoke-tested 2026-10-30)
- [ ] Optional: site search (e.g. Pagefind in the build step)
- [ ] Optional: comments for new posts (e.g. giscus)

## Domain / DNS cutover

DNS moves to Route 53; the registration moves from WordPress.com (Automattic) to Vercel, since Route 53 can't
register or transfer `.blog`. Details and the change files are in [`dns/`](dns/README.md).
Do one change at a time: nameservers, then the GitHub cutover, then the registrar transfer.

### Stage 1: Route 53 zone mirroring WordPress (no visible change)

- [x] Inventory WordPress.com DNS: apex A ×2, apex TXT (SPF, OpenAI verification), `_dmarc` TXT, `www` CNAME, wildcard `*` CNAME; no MX, no CAA
- [x] Confirm DNSSEC is off (no DS record at the `.blog` registry), so there's nothing to unwind first
- [x] Create Route 53 hosted zone `Z01473392OJPXBMNA7D22` in AWS account `196936048600` with an exact copy of those records (TTL 300)
- [x] Verify Route 53 answers match WordPress.com's for every record

### Stage 2: Switch nameservers (WordPress.com dashboard)

- [x] (2026-10-30 15:03 PT) WordPress.com → Upgrades → Domains → compositecode.blog → Name servers: turn off "Use WordPress.com name servers" and enter:
  `ns-425.awsdns-53.com`, `ns-800.awsdns-36.net`, `ns-1487.awsdns-57.org`, `ns-1649.awsdns-14.co.uk`
- [x] Confirm the registry delegates to Route 53 (switched 2026-10-30 15:06 PT): `dig @a.ns.nic.blog compositecode.blog NS +noall +authority`
- [ ] Wait at least 48 hours (the registry's delegation TTL is 24 hours) with WordPress untouched; the site keeps being served by WordPress throughout. Earliest stage 3: 2026-11-01 15:10 PT
- [ ] Confirm public resolvers return Route 53's answers (`dig compositecode.blog NS @1.1.1.1` / `@8.8.8.8`)

### Stage 3: Point at GitHub Pages

- [x] GitHub → Settings → Pages → Add a domain → `compositecode.blog`; `_github-pages-challenge-Adron` TXT added to Route 53; verified 2026-10-30 (keep the record permanently)
- [x] Final content re-sync from WordPress: nothing new since 2026-10-09 (checked 2026-10-30)
- [x] Repo → Settings → Pages → Custom domain: `compositecode.blog` (set 2026-10-30, ahead of the 48h wait at your request; resolvers still caching WordPress's nameservers keep serving the WordPress copy until they expire)
- [ ] Apply `dns/route53-stage2-github-pages.json` (GitHub A/AAAA, `www` → `adron.github.io`, removes the wildcard) at a quiet time
  - Browsers that cached WordPress's HSTS header see certificate errors until GitHub issues the certificate (usually minutes, up to about an hour)
- [ ] When the certificate is issued, tick **Enforce HTTPS**
- [ ] Confirm `http://` → `https://` and `www` → apex redirects; spot-check old URLs, `/feed/`, and `/?p=75418`
- [ ] Confirm canonical URLs read `https://compositecode.blog/...` (on the github.io preview they include `/compositecode.blog/` twice; that's expected while a base path is set)
- [ ] Rollback if needed: re-apply `dns/route53-stage1-mirror-wordpress.json` (WordPress keeps serving as long as the plan is active)

### Stage 4: Transfer the registration to Vercel

Vercel only becomes the registrar. DNS stays in Route 53 and the site stays on GitHub Pages.
Start this only after stages 2 and 3 are done and stable, and while the WordPress.com plan is still active.

- [ ] Before starting, check in the Vercel dashboard: the `.blog` transfer price, and that a Vercel-registered domain can keep custom (Route 53) nameservers. If it can't, stop and pick another registrar (e.g. Porkbun) rather than moving DNS.
- [ ] Confirm the domain is eligible: not registered or transferred in the last 60 days, and not within 45 days of an auto-renewal (a transfer then may not add a year)
- [ ] Make sure the registrant email at WordPress.com is one you can read (transfer approval mail goes there)
- [ ] WordPress.com → Domains → compositecode.blog → Transfer: unlock the domain and get the authorization (EPP) code
- [ ] Vercel → Domains → Transfer in → `compositecode.blog` + the code (or `vercel domains transfer-in compositecode.blog`); pay the transfer fee (adds one year: expiry 2028-04-17 → 2029-04-17)
- [ ] Approve the transfer if WordPress.com sends a confirmation email (otherwise it completes on its own in about 5–7 days)
- [ ] After it completes, confirm nameservers are still Route 53: `dig +short NS compositecode.blog @a.ns.nic.blog` should list the four `awsdns` servers; if Vercel switched them, set custom nameservers back to Route 53 in the Vercel dashboard
- [ ] Confirm the site still resolves and serves (`dig +short compositecode.blog A @1.1.1.1`, load https://compositecode.blog/)
- [ ] Turn on auto-renew and WHOIS privacy in Vercel
- [ ] Do not add the domain to a Vercel project: the site is served by GitHub Pages, and adding it would ask you to point DNS at Vercel

## WordPress.com wind-down (only after the new site is live and verified)

- [ ] Final content re-sync and comparison
- [ ] Rehost VideoPress videos (above)
- [ ] Export subscribers and comments (above)
- [ ] Domain transfer to Vercel complete (stage 4), so nothing domain-related depends on WordPress.com
- [ ] Cancel the WordPress.com hosting plan (and the old domain subscription there, if it's still listed after the transfer)
- [ ] Optional, after WordPress is gone: drop `include:_spf.wpcloud.com` from the SPF record (it only authorized WordPress.com to send mail as the domain)
