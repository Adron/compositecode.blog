---
title: Business Intelligence Observations
date: 2007-10-24 17:28:00 +0000
last_modified_at: 2007-10-24 17:28:00 +0000
permalink: /2007/10/24/business-intelligence-observations/
slug: business-intelligence-observations
wp_id: 410
original_url: https://compositecode.blog/2007/10/24/business-intelligence-observations/
categories:
- Uncategorized Bits
tags: []
excerpt: As I sit through the second day of training I can’t help but think back upon my previous experiences with OLAP and BI. My thoughts run back to some other times doing the same things, but it just wasn’t initially called BI or OLAP, simply reports for executives and business decision making. I find it …
---

As I sit through the second day of training I can’t help but think back upon my previous experiences with OLAP and BI.  My thoughts run back to some other times doing the same things, but it just wasn’t initially called BI or OLAP, simply reports for executives and business decision making.  I find it interesting that there are specific labels for all of these efforts.

BI for the most part is just views, stored procedures, and other data getters that coordinates and correlates data into “information”.  The difference now is that there are tools and other applications that assist   This has been done for ages and ages.  There have been autonomous database servers setup just for this purpose before.  They where not called OLAP or BI servers, just simply report servers.

One of the solutions that I worked with in the past previous to dedicated OLAP and BI solutions was back at SCP Pool Corp.  We had a database that was used for OLTP work and another database that stored denormalized reporting data.  In addition to that we had break downs of data into views and other assorted organizations to provide extensive reports.

This solution was nothing more than what the BI and OLAP Cubes provide today.  The data was similar, the speed was similar, and the capabilities where similar.

I will admit though, that even with similar capabilities, what is simplified and assured with SSAS & SSIS in comparison to the manually created and manually coded solutions of yesteryear are vastly better.  I just like to draw the correlation that it isn’t particularly NEW, it is just DIFFERENT.  The decrease in time it takes to put together report cubes, process them because of simplified structures, and the ongoing enhancements to the underlying engines themselves make BI and OLAP work worth the investment.

Once again, just like *interurban passenger cars* are now *light rail vehicles* and *horseless carriages* are now *cars*, *reporting databases* are now *OLAP/BI Cubes*.
