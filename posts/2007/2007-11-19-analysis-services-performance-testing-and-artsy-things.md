---
title: Analysis Services Performance Testing and Artsy Things
date: 2007-11-19 08:53:00 +0000
last_modified_at: 2007-11-19 08:53:00 +0000
permalink: /2007/11/19/analysis-services-performance-testing-and-artsy-things/
slug: analysis-services-performance-testing-and-artsy-things
wp_id: 391
original_url: https://compositecode.blog/2007/11/19/analysis-services-performance-testing-and-artsy-things/
categories:
- Uncategorized Bits
tags: []
excerpt: I’m on a couple new quests as of this week. One is to find a decent way to performance test SSAS without buying or putting in place large servers similar to what would be used in a production environment. The second is to figure out how to have JavaScript or some code provide the timeline …
---

I’m on a couple new quests as of this week.  One is to find a decent way to performance test SSAS without buying or putting in place large servers similar to what would be used in a production environment.  The second is to figure out how to have JavaScript or some code provide the timeline or time slice of a flash video that could be on my server or some other server embedded in my web page.

With the JavaScript and Flash needs, I’m at ground zero still.  Most of what I’ve looked at just doesn’t seem to work.  [Silverlight](http://silverlight.net/) could totally replace the need, but the request is for Flash.  @#$(^& Flash!!!!  Argh.  Anyone with any ideas, or know any good places to find information of Flash Video functionality, please let me know and post a comment.

For the first quest, to find a way to performance test SSAS Cubes via a tool or some other feature.  Part of this quest is to find a way to get performance numbers that can be reviewed and then calculated easily.  The idea is to get the current numbers and scale them appropriately for the larger machines or environments the SSAS Cube would sit on.  Again if anyone out there has 2 cents to apply, please do!

Just a review of what I’ve found relating to performance tools:

The first thing I stumbled on was [Mark Russo’s SSAS Performance Tools Blog Entry](http://sqlblog.com/blogs/marco_russo/archive/2007/04/28/ssas-performance-tools.aspx).  In his blog entry he mentions the second thing I came upon, the [MDX Script Performance Tool](http://www.codeplex.com/mdxscriptperf) on [Codeplex](http://www.codeplex.com).  This tool written by [Chris Webb](http://cwebbbi.spaces.live.com/default.aspx) is discussed more on his blog entry [MDX Script Performance Analyser](http://cwebbbi.spaces.live.com/Blog/cns!7B84B0F2C239489A!1128.entry).

Another tool [Chris Webb](http://cwebbbi.spaces.live.com/default.aspx) mention [via his blog](http://www.codeplex.com/SQLSrvAnalysisSrvcs) is the [load testing tool](http://www.codeplex.com/SQLSrvAnalysisSrvcs).

There are also the multitude of links for the [Analysis Services 2005 Performance Tuning White Paper](http://www.google.com/url?sa=t&ct=res&cd=1&url=http%3A%2F%2Fdownload.microsoft.com%2Fdownload%2F8%2F5%2Fe%2F85eea4fa-b3bb-4426-97d0-7f7151b2011c%2FSSAS2005PerfGuide.doc&ei=d-BBR4ezGqO4gQP5maymCg&usg=AFQjCNGH-tAdJ5gX3Vc69NYzTN7r--5mWg&sig2=-XqvvOjMmP18COSoFbLkFA), something that might add to what I’m looking for, but not automated for sure.

So far with all these tools I haven’t found a complete “performance estimation tool” that would fulfill the functions that I’m looking for.  I ***suppose*** I’ll have to start building my own.
