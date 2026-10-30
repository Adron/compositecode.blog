# DNS for compositecode.blog

DNS is hosted in **AWS Route 53** (account `196936048600`, hosted zone `Z01473392OJPXBMNA7D22`).
The domain is **registered at WordPress.com (Automattic)** until 2028-04-17 and is being **transferred to Vercel**
(Route 53 can't register or transfer `.blog`). Vercel will only be the registrar: the nameservers keep pointing at
Route 53 and the site stays on GitHub Pages. See stage 4 in `punch-list.md`.

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
3. **Point at GitHub Pages** (`route53-stage2-github-pages.json`). First verify the domain with GitHub (adds a
   `_github-pages-challenge-Adron` TXT record) and set the custom domain in the repo's Pages settings.
   Stage 2 also deletes the wildcard `*` record: GitHub warns that wildcard records invite subdomain takeover.
   The GitHub verification TXT record (`route53-github-verification.json`) was added and verified on 2026-10-30
   and must stay in place permanently.
4. **Transfer the registration to Vercel** once the above is stable. The transfer doesn't change DNS; afterwards,
   check the registry still delegates to the four Route 53 nameservers.

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
