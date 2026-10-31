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
- [x] Final re-sync right before DNS cutover: nothing new since 2026-10-09 (checked 2026-10-30)
- [ ] Upload the 4 large slide decks to the `attachments` GitHub Release (files are outside the repo; links already point at the release)
- [x] Download all VideoPress originals (7 embedded + 5 unattached, 582 MB) to `~/Desktop/compositecode-videos/` with `INDEX.md` mapping each to its post (2026-10-30)
- [ ] Rehost the 7 embedded videos (YouTube or similar) and update those posts' embeds before cancelling WordPress; the VideoPress players stop working when the plan ends
  - `/2010/06/10/first-post-code-kata-alpha-counter/`, `/2010/08/09/aws-5-minute-quick-start/`, `/2010/12/07/windows-azure-sdk-1-3-broken-deployments/`, `/2011/03/29/aws-linux-ec2-wordpress-free/`, `/2011/04/03/deploying-asp-net-mvc-3-razor-web-app-to-appharbor-4-minutes/`, `/2018/09/17/strata-ninjas-distributed-data-day-and-graph-day-trip-recap/`, `/2024/05/02/software-development-getting-started-by-getting-organized/`
- [ ] Decide on the 7 unattached video attachment pages in the WP video sitemap (`/hashiconf-trip-day-1-mp4/` etc.): rehost and add pages, or let them 404
- [ ] Export the 1,219 comments (needs a WXR export from wp-admin) if you want them archived. The WordPress admin is reachable again at https://compositecode.wpcomstaging.com/wp-admin/ (WordPress moved the site there when the domain left)
- [x] Export the Jetpack email subscriber list: `~/Desktop/compositecode-subscribers-2026-10-30.csv`, 551 rows via Jetpack Cloud (61 Subscribed, 89 Emails paused, 222 Not confirmed, 149 Not subscribed, 29 Bounced, 1 Not sending). Not committed to the repo (personal data)
- [ ] Optional: check for drafts or private posts (not visible to the public API; WXR export from https://compositecode.wpcomstaging.com/wp-admin/)
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
- [ ] Decide on "Follow via Email": Jetpack's form can't work off WordPress; pick a newsletter service (Buttondown, Substack, etc.), import the active subscribers from the exported CSV (61 "Subscribed"; decide on the 89 "Emails paused"), and add its form to `_includes/sidebar.html`
- [ ] Dropped on purpose: "My Upcoming Events" widget (was empty), EU cookie banner (only needed for WordPress.com's cookies), Jetpack likes/sharing buttons, comments feed link
- [ ] Optional: add a favicon (WordPress was serving its generic default icon)

## GitHub hosting

- [x] Jekyll 4 site using the Colinear theme, built by GitHub Actions
- [x] Deploy workflow (`.github/workflows/pages.yml`), with a daily rebuild for scheduled posts
- [x] Enable GitHub Pages (Source: GitHub Actions) and confirm the first deploy (2026-10-30)
- [x] Review the preview at https://adron.github.io/compositecode.blog/ (deployed and smoke-tested 2026-10-30; it now redirects to https://compositecode.blog/)
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
- [x] Wait at least 48 hours (the registry's delegation TTL is 24 hours) with WordPress untouched; the site keeps being served by WordPress throughout. (Cut over early at your request; see stage 3.) Earliest stage 3: 2026-11-01 15:10 PT
- [x] Confirm public resolvers return Route 53's answers (`dig compositecode.blog NS @1.1.1.1` / `@8.8.8.8`)

### Stage 3: Point at GitHub Pages

- [x] GitHub → Settings → Pages → Add a domain → `compositecode.blog`; `_github-pages-challenge-Adron` TXT added to Route 53; verified 2026-10-30 (keep the record permanently)
- [x] Final content re-sync from WordPress: nothing new since 2026-10-09 (checked 2026-10-30)
- [x] Repo → Settings → Pages → Custom domain: `compositecode.blog` (set 2026-10-30, ahead of the 48h wait at your request; resolvers still caching WordPress's nameservers keep serving the WordPress copy until they expire)
- [x] Apply `dns/route53-stage2-github-pages.json` (GitHub A/AAAA, `www` → `adron.github.io`, removes the wildcard): applied 2026-10-30 16:21 PT
  - Browsers that cached WordPress's HSTS header see certificate errors until GitHub issues the certificate (usually minutes, up to about an hour)
- [x] When the certificate is issued, tick **Enforce HTTPS**: certificate approved and served 16:33 PT (after re-attaching the custom domain to trigger GitHub's DNS check), HTTPS enforced; expires 2027-01-28, auto-renewed by GitHub
- [x] Confirm `http://` → `https://` and `www` → apex redirects; spot-check old URLs, `/feed/`, and `/?p=75418` (300 random URLs from the live WordPress sitemap all 200 on 2026-10-30)
- [x] Confirm canonical URLs read `https://compositecode.blog/...` and pages no longer carry `noindex`
- [x] Within ~24h of 2026-10-30 15:06 PT, resolvers still caching WordPress's nameservers (Quad9 and OpenDNS were) expire and also reach GitHub; the scheduled check on 2026-11-01 confirms (Cloudflare, Google, Quad9 and OpenDNS all reach GitHub as of 2026-10-31 10:00 PT)
- [x] Note: HTTPS visitors on already-switched resolvers saw a certificate warning for about 11 minutes (16:22–16:33 PT) while the certificate was issued
- [x] ~~Rollback if needed: re-apply `dns/route53-stage1-mirror-wordpress.json`~~ No longer possible: since the transfer, WordPress.com no longer serves compositecode.blog (it answers "Active domain connection for this domain not found")

### Stage 4: Transfer the registration to Vercel

Vercel only becomes the registrar. DNS stays in Route 53 and the site stays on GitHub Pages.
Start this only after stages 2 and 3 are done and stable, and while the WordPress.com plan is still active.

- [x] Before starting, check: Vercel quotes $25 transfer (adds a year) and $25/yr renewal; Vercel-registered domains can use up to four custom nameservers
- [x] Confirm the domain is eligible (Vercel confirmed it's transferable; WordPress.com auto-renew isn't until 2028-03-17)
- [x] Make sure the registrant email at WordPress.com is one you can read (transfer approval mail goes there)
- [x] WordPress.com → Domains → compositecode.blog → Transfer: unlocked (registry status `ok`) and authorization code obtained, 2026-10-30
- [x] `vercel domains transfer-in compositecode.blog --scope adron-halls-projects`: submitted and paid ($25) 2026-10-30; owned by the "Adron Hall's projects" scope
- [x] Vercel warned it switches transferred domains to Vercel DNS, so the full record set was imported into Vercel DNS ahead of time (`dns/compositecode.blog.zone`) and verified identical on ns1/ns2.vercel-dns.com; the site resolves the same whichever nameservers are active
- [x] Approve the transfer (expedited via WordPress.com's email): completed 2026-10-31 00:14 PT. Registry now shows registrar Name.com (Vercel's registrar), expiry 2029-04-17, and the usual 60-day post-transfer lock
- [x] After it completes, check which nameservers the registry lists: still the four Route 53 servers (Vercel didn't switch them); site, HTTPS and redirects verified
- [x] Decide where DNS lives: **keep Route 53** (decided 2026-10-31). Vercel DNS keeps an identical copy as a standby
- [x] Vercel finished its side of the transfer and, as warned, switched the registry to `ns1/ns2.vercel-dns.com` (2026-10-31 01:37 PT); the standby copy kept the site up
- [x] Set the four Route 53 servers back as the domain's nameservers via Vercel's registrar API (`PATCH /v1/registrar/domains/compositecode.blog/nameservers`); registry back on Route 53 at 2026-10-31 10:01 PT
- [ ] After 2026-11-02 (48h after the switch back, so no resolver still uses Vercel's nameservers), optionally delete the standby records in Vercel DNS. Until then, any record change must be made in both Route 53 and Vercel DNS
- [x] Confirm the site still resolves and serves
- [x] Turn on auto-renew in Vercel (2026-10-31)
- [ ] Confirm WHOIS privacy is on in the Vercel dashboard (Domains → compositecode.blog)
- [x] Note: do not add the domain to a Vercel project: the site is served by GitHub Pages, and adding it would ask you to point DNS at Vercel

## WordPress.com wind-down (only after the new site is live and verified)

- [x] Final content re-sync and comparison
- [ ] Rehost VideoPress videos (above)
- [x] Export subscribers (above)
- [ ] Export comments, if wanted (above)
- [x] Domain transfer to Vercel complete (stage 4), so nothing domain-related depends on WordPress.com
- [ ] Cancel the WordPress.com hosting plan (and the old domain subscription there, if it's still listed after the transfer)
- [ ] Optional, after WordPress is gone: drop `include:_spf.wpcloud.com` from the SPF record (it only authorized WordPress.com to send mail as the domain)
