---
title: Dammit!  I Broke the Build!
date: 2008-10-30 12:32:00 +0000
last_modified_at: 2008-10-30 12:32:00 +0000
permalink: /2008/10/30/dammit-i-broke-the-build/
slug: dammit-i-broke-the-build
wp_id: 550
original_url: https://compositecode.blog/2008/10/30/dammit-i-broke-the-build/
categories:
- Uncategorized Bits
tags: []
excerpt: I broke the build this morning as I fixed a bug at 1:12am. I didn't just break it though, I broke it in an absolutely stupid, shameful, silly way. I somehow managed to stick a semi-colon on the end of a line of code before checking in, in addition to the semi-colon that was already …
---

I broke the build this morning as I fixed a bug at 1:12am. I didn't just break it though, I broke it in an absolutely stupid, shameful, silly way. I somehow managed to stick a semi-colon on the end of a line of code before checking in, in addition to the semi-colon that was already on the end of the line of code. Woe is me, I'm a little special in the head today.

It does go to show though, technically, with modern tools I should not have been able to make that mistake. This is something I'll have to work with others to assure we implement. Nobody, should be able to actually check in code that would cause a break of the build. I have a little research to do because in VSTS TFS 2008, the currently used tool, I'm not sure how to set this up. Hopefully I can help figure out a way to help implement this to reduce these wasted minutes and hours of each day for the teams.

## In Other News

[WebTrends](http://www.webtrends.com) has been getting some good news releases and other such things recently. Lately there has been a post about our new products and product efforts. [WebTrends](http://www.webtrends.com) declared data independence. Beyond that if we take a look at what has been released we get into some interesting scenarios, especially for sites with serious traffic volumes that need measured! [WebTrends](http://www.webtrends.com) Connect & Data Scheduler will provide multiple avenues for access to data, delivered on various frequencies you can setup and various methods in addition to that. Using Web Services, ODBC, and the associated APIs one can really wire up the data into dashboards and integrate the data into other tools. Imagine being able to actually tie in your analytics data for the executive team and display it beside the ad spot purchasing data, to compare web vs. TV purchased ads and follow through. I personally find it very gratifying to see an actual click through to purchase line versus and artificial "guesstimate" for TV ad purchases.

But just imagine, by connecting those systems it isn't unfeasible to imagine even that data becoming available in some manner. I'll leave that exercise (at least for now) up to the reader.

## Open ID Rocks!

I mentioned a few days ago that [Microsoft finally got on the band wagon, well Google has also decided last week that it will also provide Open ID Provider Services](http://www.cmswire.com/cms/web-20/microsoft-google-shake-hands-over-openid-003430.php?utm_source=internal&utm_medium=web_recent-articles&utm_campaign=Internal_Recent-Articles) which I had not realized. But between both of them getting on board, that is awesome news.

## …and more Broken Builds

As the day has moved on there have been other build breakages, not particularly me. However the onus has been put on me a few times. It makes me ponder what VSTS TFS is doing. I've used it in the past, mostly with VSTS TFS 2005, and have had tons of issues. I'm usually pretty observant of what source control systems do with my code, but TFS is super tricky. It ghosts things in and out, mixes up versioning and puts some files with other check ins, then reports a breakage on a CI build that has nothing to do with a particular check out.

Now last time I checked, that level of inaccuracy was unacceptable. I was hoping that these types of issues would have been resolved in 2008, but it looks like my hopes have been dashed. This doesn't even touch on [Ayende's](http://ayende.com/) Issues that he's [mentioned in the past](http://ayende.com/Blog/archive/2008/10/27/visual-studio-2010.aspx), and [more](http://ayende.com/Blog/archive/2007/04/29/Passonaite-at-Team-System-Depending-on-which-direction.aspx), and I'm sure more. He just flat out states it flat out " It means that it cannot be trusted". Which honestly, I can't disagree with. After using Subversion with TeamCity and other tools, TFS just does not have that same level of quality or trust. Once again I'll state, I sure hope to see this fixed and changed in 2010, even though I'm not holding my breath this time, I still have a bruise from passing out for the 2008 version.
