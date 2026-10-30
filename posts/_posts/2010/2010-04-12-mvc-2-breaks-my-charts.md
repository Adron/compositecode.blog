---
title: MVC 2 Breaks my Charts?
date: 2010-04-12 18:15:04 -0700
last_modified_at: 2010-10-04 11:20:20 -0700
permalink: /2010/04/12/mvc-2-breaks-my-charts/
slug: mvc-2-breaks-my-charts
wp_id: 720
original_url: https://compositecode.blog/2010/04/12/mvc-2-breaks-my-charts/
categories:
- Rants
tags: []
excerpt: I wonder if anyone has had issues with running MSCharts with MVC 2? I have tried a couple of different issues, but still have not got them to render correctly. In the end I always end up with broken image links. Has anyone seen this? I have no errors displaying in my MVC 2 Application …
---

I wonder if anyone has had issues with running MSCharts with MVC 2?  I have tried a couple of different issues, but still have not got them to render correctly.  In the end I always end up with broken image links.  Has anyone seen this?

![](/images/adronhall.smugmug.com/Software/Misc-Images/Misc-Screen-Shots/MVC-2-Breaks-my-Charts-01/835355709_3WFLZ-M.png)

I have no errors displaying in my MVC 2 Application build or anything, nothing specific that leads me to any explanation.  If anyone has any ideas, please leave a comment or shoot me an e-mail; adronhall at gmail dot com.  I would greatly appreciate any insight you MSChart Elite may have.  : )

ADDITIONAL NOTE:  The links look like this:

<http://localhost:1799/Scorecard/ChartImg.axd?i=chart_6d740211d16b41bd9cc2662b602c4045_0.png&g=8840cdffa191495caafa73150dc0de7d>
Which I assume is what they should look like, since the ChartImg.axd is supposed to be handling the requests for the chart images.  Maybe the handler is broken/messed up?
