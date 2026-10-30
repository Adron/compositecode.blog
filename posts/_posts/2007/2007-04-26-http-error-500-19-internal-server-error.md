---
title: HTTP Error 500.19 – Internal Server Error
date: 2007-04-26 16:47:47 -0700
last_modified_at: 2007-04-26 16:47:47 -0700
permalink: /2007/04/26/http-error-500-19-internal-server-error/
slug: http-error-500-19-internal-server-error
wp_id: 493
original_url: https://compositecode.blog/2007/04/26/http-error-500-19-internal-server-error/
categories:
- Uncategorized Bits
tags: []
excerpt: This “HTTP Error 500.19 – Internal Server Error” and “HTTP Error 500.0 – Internal Server Error” have become the bane of my existence lately. I’ve been trying to run two of my projects via the localhost IIS Server. The errors listed have basically rendered the local IIS Server useless. I’ve checked out a lot of …
---

This “HTTP Error 500.19 – Internal Server Error” and “HTTP Error 500.0 – Internal Server Error” have become the bane of my existence lately.  I’ve been trying to run two of my projects via the localhost IIS Server.  The errors listed have basically rendered the local IIS Server useless.

I’ve checked out a lot of entries and other blogs in regards to this error, but none of the “solutions” have done anything for me.  With that in mind I’ve attempted to run the various solutions without the localhost.  So far, the solution is, is to use the virtual dev server.  If you need windows authentication or something you’ll have to set it via the properties of the project.
