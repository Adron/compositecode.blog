---
title: .NET Subversion Tips
date: 2008-06-03 01:34:04 -0700
last_modified_at: 2008-06-03 01:34:04 -0700
permalink: /2008/06/03/net-subversion-tips/
slug: net-subversion-tips
wp_id: 293
original_url: https://compositecode.blog/2008/06/03/net-subversion-tips/
categories:
- Uncategorized Bits
tags: []
excerpt: I’ve never been the “repository guy” or “build manager” or anything of that nature, but have had a decent amount of experience working with the tools. So a few simple tips… Exclude Directories The second you create a project in .NET, if it is one of the projects that have a obj and bin directory, …
---

I’ve never been the “repository guy” or “build manager” or anything of that nature, but have had a decent amount of experience working with the tools.

So a few simple tips…

**Exclude Directories**

The second you create a project in .NET, if it is one of the projects that have a ***obj*** and ***bin*** directory, set both to be excluded from commits.  There is no reason to include these directories.  Every time a project is built these will be recreated, which will cause file changes and a required commit, and if excluded they’ll just build without interrupting the flow of commits, updates, and adds.

While we’re on the topic.  If you use [ReSharper](http://www.jetbrains.com/resharper/index.html), make SURE to exclude the [ReSharper](http://www.jetbrains.com/resharper/index.html) cache directory.  This sucker can get HUGE and bloat up the source repository.  If you don’t use [ReSharper](http://www.jetbrains.com/resharper/index.html), GET IT!  Then exclude the cache directory.

Technorati Tags: [ReSharper](http://technorati.com/tags/ReSharper),[Subversion](http://technorati.com/tags/Subversion)

del.icio.us Tags: [ReSharper](http://del.icio.us/popular/ReSharper),[Subversion](http://del.icio.us/popular/Subversion)
