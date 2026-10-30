---
title: .NET Assemblies for Webtrends DX Web Services
date: 2009-11-22 12:47:35 +0000
last_modified_at: 2009-11-22 12:47:35 +0000
permalink: /2009/11/22/net-assemblies-for-webtrends-dx-web-services/
slug: net-assemblies-for-webtrends-dx-web-services
wp_id: 672
original_url: https://compositecode.blog/2009/11/22/net-assemblies-for-webtrends-dx-web-services/
categories:
- Uncategorized Bits
tags: []
excerpt: One of the easiest ways to develop against the Webtrends DX Web Services is to use the Webtrends.SDK Assembly. The Webtrends SDK handles all of the retrieval of profile & report listings, report objects, mappings into DataTable, Object, or other formats, and authentication. The SDK cuts down on about 50-80% of the code one needs …
---

One of the easiest ways to develop against the Webtrends [DX](http://developer.webtrends.com/community/dx/) Web Services is to use the Webtrends.SDK Assembly.  The Webtrends SDK handles all of the retrieval of profile & report listings, report objects, mappings into DataTable, Object, or other formats, and authentication.  The SDK cuts down on about 50-80% of the code one needs to write to retrieve and process the returned report data.  Development is always moving forward to add functionality, processing, more mappings, and other features to the SDK to simplify and speed development.  Here are some samples of the current key parts of the SDK Library.

**The Business Objects**

The business objects provided in the Webtrends SDK are used to map the retrieved data into.  These object include the following key classes (not all are included, it is a pretty long list):
