---
title: News, Keeping Up, and Work Bits
date: 2008-10-30 02:01:05 +0000
last_modified_at: 2008-10-30 02:01:05 +0000
permalink: /2008/10/30/news-keeping-up-and-work-bits/
slug: news-keeping-up-and-work-bits
wp_id: 549
original_url: https://compositecode.blog/2008/10/30/news-keeping-up-and-work-bits/
categories:
- Uncategorized Bits
tags: []
excerpt: I finally listened to the keynote from PDC 2008. It was pretty good, nothing that I wasn’t really prepared for, but I’m sure a decent amount of cool things introduced for the Microsoft Developer out and about in the wild. I was glad to finally see the cloud computer official, etc. Overall I’m chomping at …
---

I finally listened to the keynote from PDC 2008. It was pretty good, nothing that I wasn’t really prepared for, but I’m sure a decent amount of cool things introduced for the Microsoft Developer out and about in the wild. I was glad to finally see the cloud computer official, etc. Overall I’m chomping at really getting into some of the other sessions related to the specific pieces of technology. Especially WCF, WF, and the whole middle tier pieces. I’m also keen to see what is done with the ASP.NET MVC Framework, and especially looking for to a real release finally.

Anyway, nothing I haven’t really blabbered on about before. In other efforts to keep up with technology and the architectural demands of the industry I often bounce over to [InfoQ](http://www.infoq.com). One good listen recently was by Dan Pritchett of eBay. I’ll correct his title for him, “[Designing for Latency](http://www.infoq.com/presentations/Architecting-Latency-Dan-Pritchett)“. Even though he’s one of those evil “architecting is a verb” people, he’s a good solid guy, and has some decent information to listen to and think through if you are building anything that might have latency involved. In other words, EVERYBODY!

In other news, [Moore’s Law Has Changed](http://www.infoq.com/news/2008/06/scala-vs-erlang), instead now we get cores instead of clock speed increases. While I’d still love some clock speed increases, it is nice to basically have a multi-core proc in every box these days.

## PDC 2008 Kewl Bits

Check out this [video](http://channel9.msdn.com/pdc2008/TL47/). VSTS is going to rock a lot more. There are a few issues still that concern me, but the work flows and bug tracking are looking pretty good and improved!

At 28.00 minutes in they hit on how to prevent checking in a local change set that might break the build. Not like the “no you can’t check this in cuz you broke it” type of limitations, but it actually gives you information back on why it didn’t build correctly.

Other parts are the testing now automatically sends a video along with the bug, also a whole event log is sent along with the bug, and a whole bunch of other information pertinent to getting a bug fixed.

At 32.29, the “Layer Diagram” is shown. This is a new diagram and let me tell ya, that sucker will save some time in drawing out the dependencies! For debugging and presentation of an architecture. I’m digging this, all built into the TFS Toolset.

36.10 the Architecture Explorer is looking wicked too. This just brings home the idea that we developers are finally getting those promised 4th Generation Languages. Albeit they’re 5+ years behind, but they are arriving! The diagrams too, especially this layer diagram, is a beautiful thing to have that easily accessible. For a real kicker, check out the sequence diagram generated from code at 42:20.

For a real cool unit test bit, check out 46:10. That’s all I’m going to say about that…

## Today’s Closing…

…That’s about it for today. I’m hoping tomorrow to have my Part 2 for the WCF known types & other bits finished and written up.
