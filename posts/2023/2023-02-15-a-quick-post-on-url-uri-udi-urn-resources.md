---
title: A Quick Post on URL, URI, UDI, URN… Resources
date: 2023-02-15 18:16:13 -0800
last_modified_at: 2023-07-17 10:40:37 -0700
permalink: /2023/02/15/a-quick-post-on-url-uri-udi-urn-resources/
slug: a-quick-post-on-url-uri-udi-urn-resources
wp_id: 65902
original_url: https://compositecode.blog/2023/02/15/a-quick-post-on-url-uri-udi-urn-resources/
categories:
- Unknown Code Ramblings
tags:
- udi
- uri
- url
excerpt: URL, or Uniform Resource Locator, is often used as a blanket term for almost anything on the internet. A URI, or Uniform Resource Identifier, represents a unique resource on a server, located somewhere on the World Wide Web. Other abbreviations that are often confusingly related include UDI for Universal Document Identifier and URN for Universal Resource Name. All together we have the following abbreviations;
image: /wp-content/uploads/2023/02/world-wide-web.webp
---

URL, or Uniform Resource Locator, is often used as a blanket term for almost anything on the internet. A URI, or Uniform Resource Identifier, represents a unique resource on a server, located somewhere on the World Wide Web. Other abbreviations that are often confusingly related include UDI for Universal Document Identifier and URN for Universal Resource Name. All together we have the following abbreviations;

- URL – Uniform Resource Locator
- URI – Uniform Resource Identifier
- UDI – Universal Document Identifier
- URN – Uniform Resource Name

A URI can be either a URL or URN.

![](https://documents.lucid.app/documents/cc0f85a4-ce77-4283-b652-88b96ef1c317/pages/SVqXRFmNeIsj?a=369&x=489&y=255&w=680&h=288&store=1&accept=image%2F*&auth=LCA%20ac4c4de6438faee9ccf031079a9cbf0ad2ec9cc89e251e4f712c897fc02d6aee-ts%3D1676509942)

### URI Syntax

```
scheme:[//authority]path[?query][#fragment]
```

- Scheme – This is a non-empty sequence of characters followed by a colon, followed by any combo of digits, letters, periods, hyphens, or plus characters. The scheme is registered with the Internet Assigned Numbers Authority (IANA).
- Authority – The authority is an optional field preceded by //. It has the following subfields.
  - Userinfo – A subcomponent which could contain username and password, or other user information data.
  - Host – A subcomponent containing either an IP address or a registered host or domain name.
  - Port – An optional subcomponent that is followed by a colon.
- Path – Contains a sequence of segments separated by a slash characters. This could be something like `/resources` or `/trains` or similar.
- Query – An optional component preceded by a question mark. The component contains a query string of non-hierarchical data, each parameter is separated by an ampersand in the query component and parameter values are assigned using an equals operator.
- Fragment – An optional field and is preceded by a hash. The fragment includes a fragment identifier for a secondary resource.

#### Examples

- `mailto:myaddress@thrashingcode.com`
- `telnet://10.20.0.1:23/`
- `ldap://[2020:ba6:9:9]/c=ZAZA?objectClassOfDomain?objectOfDomain`

### The Differentiator

The URI examples above all could be called URLs, however the difference is that a URI is an identifier, where as a URL is an identifier and provides details on how to get to the identified resource.

## URN AKA Uniform Resource Name

URNs are not used often. More specific details can be found in [RFC 2141](https://www.rfc-editor.org/rfc/rfc2141). For this quick post it’s safe to sort of ignore URNs, as the other abbreviations are the ones you will see out and about in the world, and specifically used in detailing REST APIs and the like.
