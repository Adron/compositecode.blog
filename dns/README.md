# DNS for compositecode.blog

DNS is hosted in **AWS Route 53** (account `196936048600`, hosted zone `Z01473392OJPXBMNA7D22`).
The domain is **registered with Vercel** (registrar of record: Name.com) until 2029-04-17. It was transferred from
WordPress.com (Automattic) on 2026-10-31; Route 53 can't register or transfer `.blog`. Vercel is only the registrar:
the nameservers point at Route 53 and the site is served by GitHub Pages. See stage 4 in `punch-list.md`.

**Any record change must currently be made in both Route 53 and Vercel DNS** (`compositecode.blog.zone`), until the
Route 53 servers are pinned as custom nameservers in Vercel (see the punch list). Vercel DNS is a standby copy.

Route 53 nameservers for the zone:

```
ns-425.awsdns-53.com
ns-800.awsdns-36.net
ns-1487.awsdns-57.org
ns-1649.awsdns-14.co.uk
```

## Stages

1. **Mirror WordPress** (`route53-stage1-mirror-wordpress.json`, applied 2026-10-30). The Route 53 zone answers
   exactly what WordPress.com's nameservers answer, so changing nameservers has no visible effect.
2. **Switch nameservers** at WordPress.com to the four above (done 2026-10-30; registry switched 15:06 PT). The `.blog` registry caches delegation for 24 hours,
   so leave WordPress.com DNS and the WordPress site untouched for at least 48 hours afterwards.
3. **Point at GitHub Pages** (`route53-stage2-github-pages.json`, applied 2026-10-30 16:21 PT; HTTPS certificate issued 16:33 PT). First verify the domain with GitHub (adds a
   `_github-pages-challenge-Adron` TXT record) and set the custom domain in the repo's Pages settings.
   Stage 2 also deletes the wildcard `*` record: GitHub warns that wildcard records invite subdomain takeover.
   The GitHub verification TXT record (`route53-github-verification.json`) was added and verified on 2026-10-30
   and must stay in place permanently.
4. **Transfer the registration to Vercel** (started 2026-10-30, scope `adron-halls-projects`). Vercel moves
   transferred domains onto Vercel DNS (`ns1/ns2.vercel-dns.com`), so `compositecode.blog.zone` was imported into
   Vercel DNS beforehand and checked identical to Route 53. After the transfer, either keep Vercel DNS or set the
   four Route 53 servers as custom nameservers in Vercel; keep the two zones identical while switching.
   Vercel DNS also adds default CAA records (letsencrypt.org, pki.goog, sectigo.com) and a wildcard pointing at
   Vercel; both are harmless for GitHub Pages.

Apply a stage with:

```sh
aws route53 change-resource-record-sets --hosted-zone-id Z01473392OJPXBMNA7D22 \
  --change-batch file://dns/route53-stage2-github-pages.json
```

## Checking

```sh
# Route 53 directly
dig +short @ns-425.awsdns-53.com compositecode.blog A
# What the registry currently delegates to (24h cache)
dig +short NS compositecode.blog @a.ns.nic.blog
# Public resolvers
dig +short compositecode.blog A @1.1.1.1 ; dig +short compositecode.blog A @8.8.8.8
```
