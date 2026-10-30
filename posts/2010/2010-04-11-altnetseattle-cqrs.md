---
title: '#altnetseattle – CQRS'
date: 2010-04-11 09:16:57 +0000
last_modified_at: 2010-10-04 11:19:30 -0700
permalink: /2010/04/11/altnetseattle-cqrs/
slug: altnetseattle-cqrs
wp_id: 713
original_url: https://compositecode.blog/2010/04/11/altnetseattle-cqrs/
categories:
- Conferences
tags:
- altnet
excerpt: 'This is a topic I know nothing about, and thus, may be supremely disparate notes. Have fun translating. : ) . . .and coolness that the session is well past capacity. Separates things form the UI and everything that needs populated is done through commands. The domain and reports have separate storage. Events populate these …'
---

This is a topic I know nothing about, and thus, may be supremely disparate notes.  Have fun translating.  : )   . . .and coolness that the session is well past capacity.

- Separates things form the UI and everything that needs populated is done through commands.  The domain and reports have separate storage.
- Events populate these stores of data, such as “sold event”.
- What it looks like, is that the domain controls the requests by event, which would be a product order or something similar.
- Event sourcing is a key element of the logic.
- DDD (Domain Driven Design) is part of the core basis for this methodology/structure.
- The architecture/methodology/structure is perfect for blade style plugin hardware as needed.
- Good blog entry [DDDD: Why I love CQRS](http://jonathan-oliver.blogspot.com/2009/10/dddd-why-i-love-cqrs.html) and another [Command and Query Responsibility Segregation (CQRS)](http://blog.fossmo.net/post/Command-and-Query-Responsibility-Segregation-(CQRS).aspx), [more](http://abdullin.com/cqrs), [CQRS ? la Greg Young](http://elegantcode.com/2009/11/11/cqrs-la-greg-young/), a bit by [Udi Dahan](http://www.udidahan.com/2009/12/09/clarified-cqrs/) and there are more.  Google, Bing, etc are there for a reason.

It appears the core underpinning architectural element of this is the break out of unique identifiable actions, or I suppose better described as events.  Those events then act upon specific pipelines such as read requests, write requests, etc.  I will be doing more research on this topic and will have something written up shortly.  At this time it seems like nothing new, just a large architectural break out of identifiable needs of the entire enterprise system.  The reporting is in one segment of the architecture, the domain is in another, hydration broken out to interfaces, and events are executed to incur events on the Reports, or what appears by the description to be events on the domain.

Anyway, more to come on this later.
