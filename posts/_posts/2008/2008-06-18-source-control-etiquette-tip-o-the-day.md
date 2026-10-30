---
title: 'Source Control Etiquette :: Tip o'' The Day'
date: 2008-06-18 05:58:58 -0700
last_modified_at: 2008-06-18 05:58:58 -0700
permalink: /2008/06/18/source-control-etiquette-tip-o-the-day/
slug: source-control-etiquette-tip-o-the-day
wp_id: 283
original_url: https://compositecode.blog/2008/06/18/source-control-etiquette-tip-o-the-day/
categories:
- Uncategorized Bits
tags: []
excerpt: 'Some more quick best practices for using source control. Simple Rule: Check in often, build often, and keep updated as frequently as you have code that builds. This prevents merge conflicts, overrides, and other goofy nonsense that no one wants to deal with. I would say it is a good idea to update every time …'
---

Some more quick best practices for using source control.

**Simple Rule**:  Check in often, build often, and keep updated as frequently as you have code that builds.  This prevents merge conflicts, overrides, and other goofy nonsense that no one wants to deal with.

I would say it is a good idea to **update** every time a new successful build occurs on the build server.

**Commit** (check in) every time new working code is completed.  This should be every 30 minutes to an hour.  If not, you’re probably working through tasks that are too big at one time and the tasks need to be broken down further.  This is also a sign that TDD is not being followed closely (or at all).  Even if test after is the process, tasks should be 30 minutes to an hour, and should be **committed** accordingly back to the repository.

Technorati Tags: [Source Control](http://technorati.com/tags/Source%20Control),[Etiquette](http://technorati.com/tags/Etiquette)

del.icio.us Tags: [Source Control](http://del.icio.us/popular/Source%20Control),[Etiquette](http://del.icio.us/popular/Etiquette)
