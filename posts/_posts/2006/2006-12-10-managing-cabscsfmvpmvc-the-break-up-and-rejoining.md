---
title: Managing CAB/SCSF/MVP/MVC, the break up and rejoining.
date: 2006-12-10 13:36:32 -0800
last_modified_at: 2006-12-10 13:36:32 -0800
permalink: /2006/12/10/managing-cabscsfmvpmvc-the-break-up-and-rejoining/
slug: managing-cabscsfmvpmvc-the-break-up-and-rejoining
wp_id: 523
original_url: https://compositecode.blog/2006/12/10/managing-cabscsfmvpmvc-the-break-up-and-rejoining/
categories:
- Uncategorized Bits
tags: []
excerpt: So once again I’m back at putting together management methodology for MVP designs. It seems also pertinent that sometimes, against what would seem logical, it’s also a good idea ot mix MVP and MVC design. With the possiblities for using controllers for business flow when writing the business flow in presenters breaks apart the logic …
---

So once again I’m back at putting together management methodology for MVP designs.  It seems also pertinent that sometimes, against what would seem logical, it’s also a good idea ot mix MVP and MVC design.  With the possiblities for using controllers for business flow when writing the business flow in presenters breaks apart the logic into too many seperate and sometimes disparate locations.

The idea here is a wizard with multiple screens, each being a SmartPart, that is then fed into a TabWorkspace or other multiple smart part container, should utilize a singe controller for the basic business logic flow, while the presenters can or should hold individual screen business logic.  Also of course linked up to any pertinent business rules validation and other such infrastructure.  Often times one or the other is used (I say often times, MVP and MVC aren’t exactly regularly used design patterns) and mixing seems like it might be “against the rules”.

Contrary to that one should utilize such break downs with prudent and thought out design of the controlers and presenters.  With careful design developers can then develop within their particular business or infrastructure scope without infringing upon each other’s efforts.
