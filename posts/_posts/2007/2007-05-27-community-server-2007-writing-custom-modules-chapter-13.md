---
title: Community Server 2007 – Writing Custom Modules – Chapter 13
date: 2007-05-27 07:30:13 -0700
last_modified_at: 2007-05-27 07:30:13 -0700
permalink: /2007/05/27/community-server-2007-writing-custom-modules-chapter-13/
slug: community-server-2007-writing-custom-modules-chapter-13
wp_id: 479
original_url: https://compositecode.blog/2007/05/27/community-server-2007-writing-custom-modules-chapter-13/
categories:
- Uncategorized Bits
tags: []
excerpt: I started last night working some demo modules out of the Professional Community Server book from Wrox written by Wyatt Preul, Keyvan Nayyeri, Jose Lema, and Jim Martin. The book has been a good starting point and for the most part well written, I do however have a few points of contention. While working through …
---

I started last night working some demo modules out of the [Professional Community Server](http://www.wrox.com/WileyCDA/WroxTitle/productCd-0470108282.html) book from [Wrox](http://www.wrox.com) written by [Wyatt Preul](http://wyattpreul.com/default.aspx), [Keyvan Nayyeri](http://nayyeri.net/), [Jose Lema](http://www.tankete.com/core/blogs/jose_lema/default.aspx), and [Jim Martin](http://jamesdmartin.com/default.aspx).  The book has been a good starting point and for the most part well written, I do however have a few points of contention.  While working through the first sample with a fellow techie, he being a network engineer and myself being a software architect we barreled through the sample easily.  The problem however that I must draw is that the sample is unable to be directly (or indirectly tested) because it only sends an e-mail out “if” an exception of CSException occurs.  At the end of the example, compiled, put into the bin, and the config set properly, one then has to force a CSException?  Maybe I missed that chapter, but it seems this is a relatively weak sample.  Great book, but that one sample just irks me.

Otherwise I must say thanks to all who put together the book!  It’s been a great kick start!

To beat a dead horse and return to the problem point I have with that one example, when I get through developing a few other modules and am more familiar with exactly what I am doing, I will follow up with a module or two that provides the points I feel are missing.
