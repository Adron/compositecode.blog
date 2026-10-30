---
title: BI Applications?
date: 2007-12-26 06:00:05 -0800
last_modified_at: 2007-12-26 06:00:05 -0800
permalink: /2007/12/26/bi-applications/
slug: bi-applications
wp_id: 361
original_url: https://compositecode.blog/2007/12/26/bi-applications/
categories:
- Uncategorized Bits
tags: []
excerpt: It seems that everywhere one looks in the ETL/OLAP/BI Industry Space there are no real canned applications. When I say canned application I’m talking about an application that from the ground up is all inclusive, managing the database, the ETL, the warehouse and any possible staging, and finally the Cube itself and reporting that sits …
---

It seems that everywhere one looks in the ETL/OLAP/BI Industry Space there are no real *canned applications*.  When I say canned application I’m talking about an application that from the ground up is all inclusive, managing the database, the ETL, the warehouse and any possible staging, and finally the Cube itself and reporting that sits on top of it.  Let me break that down real quick:

- Database- Staging- Warehouse- Cube- Reporting

…and of course, one can’t forget…

- ETL – **E**xtraction, **T**ransform, and **L**oading

I have as of yet seen something, able to be delivered with a single MSI, or even something that is easily installed in one or two steps.  Of course, I saw all this, and would love for someone to comment on a product that is easily installed that utilizes all of these things in one install package.  Especially if it uses Microsoft’s Technology Stack.

In addition to not having seen this yet, I keep reading about the prospective gain in market share of *applications* that are supposedly just like this.  To that I ask, “How does one scale a canned application”.  The amount of logic and decision branching the application would have to make during the course of the application scaling is practically impossible to do well.  Sure, one can put in some basic checks, but beyond that I would suspect a kind of diminishing return.  The simple fact is, that business intelligence still needs a significant presence of skilled ETL, Report, and Database Developers.

I’m not really complaining, just sort of stating the obvious.  As I dig more into this industry, I can really see how difficult it is to find people that are skilled in the full technology stack or even theory of the entire technology ideology behind business intelligence.

So with the end of the year coming up, I think what I’ll do is just set a new years resolution to get something built with a business intelligence engine as the basis.  Personally or work related doesn’t matter, I just need to create something in this space that brings together these points.
