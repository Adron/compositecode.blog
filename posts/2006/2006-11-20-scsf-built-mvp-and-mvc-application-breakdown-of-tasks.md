---
title: SCSF built MVP and MVC Application Breakdown of Tasks
date: 2006-11-20 05:31:00 +0000
last_modified_at: 2006-11-20 05:31:00 +0000
permalink: /2006/11/20/scsf-built-mvp-and-mvc-application-breakdown-of-tasks/
slug: scsf-built-mvp-and-mvc-application-breakdown-of-tasks
wp_id: 528
original_url: https://compositecode.blog/2006/11/20/scsf-built-mvp-and-mvc-application-breakdown-of-tasks/
categories:
- Uncategorized Bits
tags: []
excerpt: In an MVC or MVP Project the obvious usage reason is to break down tasks among the various aspects of the architect. In either model view controller or model view presenter there are three specific areas in which tasks need performed. Depending on team size the breakdowns can occur in various ways. The example below …
---

In an MVC or MVP Project the obvious usage reason is to break down tasks among the various aspects of the architect.  In either model view controller or model view presenter there are three specific areas in which tasks need performed.  Depending on team size the breakdowns can occur in various ways.  The example below is one way to break down the tasks.  I hopefully will dredge up some time and list out other scenarios that can be met with this architecture.  This however is the most straight forward and obvious development method usage of MVP and MVC.

**Task**:  There is a need for a new screen that will contain interfacing to data within the database.  The screen has at least 2-3 buttons and a good number of text boxes, drop downs, and or any other development elements needed.  This screen needs put in place ASAP with validation, logging, and all the plumbing of the pattern that is in use (MVC or MVP).

**Team Staff (Medium Size)**:  Business Analyst, Senior Developer (Patterns Guru), Intermediate or New Developer, and a Database Developer.

- Model – BA & Senior Developer should work on this element.- View – Inter/New Developer.  The view gives the basic overview of business logic and also give a good starting point working with MVC & MVP because any developer knows how to develop a screen.- Controller / Presenter – Database Developer should work on this element.  If a database developer works with the dev team in a scenario like this, he inherently should work on the aspects of development that he is most familiar with, thus the aspects that are closest to the data.

**Team Staff (Large Size)**:  Senior Developer (Patterns Guru), 5 Intermediate Developers ranging from straight out of college to 1-2 years of experience.  These silos that each dev group works in after a short period will make this a very fast method to develop new features with.  Only breaking out developers in such a way and allowing actual specialization of labor to occur can one really get the full benifit of this architecture.  So break the groups up, allow some cross training, but primarily focus on specialization if you need speed of development.

- Model – Senior Developer & 2 Intermediate Developer- View – 1 Intermediate Developer- Controller / Presenter – 2 Intermediate Developers.

**Team Staff (Small Size)**:  Senior Developer (Patterns Guru), 1 Intermediate Developer.  One could say, “We’ll meet in the middle!”

- Model – Senior Developer- View – Intermediate Developer- Controller / Presenter – Senior Developer & Intermediate Developer

[![kick it on DotNetKicks.com](http://www.dotnetkicks.com/Services/Images/KickItImageGenerator.ashx?url=http://adronbhall.com/blogs/technology__software_development/archive/2006/11/20/1439.aspx)](http://www.dotnetkicks.com/kick/?url=http://adronbhall.com/blogs/technology__software_development/archive/2006/11/20/1439.aspx)
