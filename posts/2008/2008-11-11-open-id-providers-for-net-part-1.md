---
title: Open ID Providers for .NET Part 1
date: 2008-11-11 02:12:29 +0000
last_modified_at: 2008-11-11 02:12:29 +0000
permalink: /2008/11/11/open-id-providers-for-net-part-1/
slug: open-id-providers-for-net-part-1
wp_id: 560
original_url: https://compositecode.blog/2008/11/11/open-id-providers-for-net-part-1/
categories:
- Uncategorized Bits
tags: []
excerpt: OpenID is sweeping the web. With announcements by Microsoft and Google recently to support the OpenID Framework, things have effectively gotten huge! One of the things I’ve been wondering about is WCF Security and how one could integrate with OpenID. Here’s what I’ve been able to dig up and implement so far. First off, it …
---

[OpenID](http://openid.net/) is sweeping the web. With announcements by Microsoft and Google recently to support the [OpenID](http://openid.net/) Framework, things have effectively gotten huge! One of the things I’ve been wondering about is WCF Security and how one could integrate with [OpenID](http://openid.net/). Here’s what I’ve been able to dig up and implement so far.

First off, it is a good idea to review what [OpenID](http://openid.net/) is. Check it out at [openid.net](http://openid.net/) for a starting point. A good read is available at the [what page](http://openid.net/what/) for [OpenID](http://openid.net/). However, if you want to get into the nitty gritty internal workings of [OpenID](http://openid.net/), it is a little trickier. The [developer page](http://openid.net/developers/) is a good place to start, but it is somewhat minimal. Once jumping out from that page the information gets more useful. Plaxo has an interesting [recipe for OpenID](http://www.plaxo.com/api/openid_recipe) and also [OpenID for non-Super Users](http://www.intertwingly.net/blog/2007/01/03/OpenID-for-non-SuperUsers) are great. Both get into the grit more.

But skipping past a ton of the existing specifications and documentation might be a better idea once I realized that there truly were some .NET libraries for [Open ID](http://openid.net/).

- [DotNet OpenId](http://code.google.com/p/dotnetopenid/)
- [ExtremeSwank](http://extremeswank.com/aspnet_openid.html) which is hosted at [ExtremeSwank Google Code](http://code.google.com/p/extremeswankopenid/).

Out of these two examples [ExtremeSwank](http://extremeswank.com) definitely has the [best documentation](http://extremeswank.com/OpenIDDoc/Index.html) out. Easy to [read code examples](http://code.google.com/p/extremeswankopenid/wiki/UsageExamples) are even available. I started to just go with [ExtremeSwank](http://extremeswank.com/), but after looking up integration notes on [OpenID](http://openid.net/) support in [BlogEngine.NET](http://dotnetblogengine.net/) I decided to download both.

For my pending [BlogEngine.NET](http://dotnetblogengine.net/) Integration I found the following articles:

- [jmpinline "How to add OpenID support to BlogEngine.NET"](http://blog.nerdbank.net/2008/01/how-to-add-openid-support-to.html)
- [Chris Blankenship’s Ramblings "OpenID for BlogEngine.Net"](http://www.dscoduc.com/post/2008/01/30/OpenID-for-BlogEngineNet.aspx)

I’ll have the follow up to my discoveries soon, so stay tuned!

…and if you do want to read the [specifications](http://openid.net/developers/specs/), feel free.
