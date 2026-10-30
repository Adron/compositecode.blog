---
title: TFS Fight and Some TDD
date: 2009-03-10 14:11:00 +0000
last_modified_at: 2009-03-10 14:11:00 +0000
permalink: /2009/03/10/tfs-fight-and-some-tdd/
slug: tfs-fight-and-some-tdd
wp_id: 603
original_url: https://compositecode.blog/2009/03/10/tfs-fight-and-some-tdd/
categories:
- Uncategorized Bits
tags: []
excerpt: I started working on a new project a few days ago that has been dubbed Cockatoo, which we have hosted on Codeplex, by the team I'm working with. For those that are curious who these 3L173 d3\/3L0P3r$ are I'll run through the names; Jason Mauer, Josh Wisely, Erik Mork, Monica Mork, Kelly White, and… we …
---

I started working on a new project a few days ago that has been dubbed [Cockatoo](http://www.codeplex.com/Cockatoo), which we have hosted on [Codeplex](http://www.codeplex.com), by the team I'm working with.  For those that are curious who these [3L173 d3\/3L0P3r$](http://www.brenz.net/l337Maker.asp) are I'll run through the names;  [Jason Mauer](http://www.jasonmauer.com), Josh Wisely, [Erik Mork](http://www.sparklingclient.com/), [Monica Mork](http://www.sparklingclient.com/), [Kelly White](http://whitepdx.com/blogs/kelly/default.aspx), and…  we might have more.  Want to join the team?  Send me a message at *adronhall at symbol gmail [.] com*…

Anyway, I'll jump into some of the first steps I've taken to get rolling.  My task is to create an assembly that will wrap the Twitter API so that the methods are abstracted into simple object method calls instead of instantiating and working through all the various HTTP communications.  As always, I try to stick with the TDD style and thus jumped right into the test code.
