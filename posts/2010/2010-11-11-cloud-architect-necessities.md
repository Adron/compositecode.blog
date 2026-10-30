---
title: Cloud Software Architect Necessities
date: 2010-11-11 04:45:00 -0800
last_modified_at: 2010-11-11 16:46:16 -0800
permalink: /2010/11/11/cloud-architect-necessities/
slug: cloud-architect-necessities
wp_id: 1020
original_url: https://compositecode.blog/2010/11/11/cloud-architect-necessities/
categories:
- Architecture
- AWS
- Azure
- Cloud Speak
tags:
- amazon web services
- aws
- cloud
- software architecture
- windows azure
excerpt: Cloud Architecture is becoming more and more relevant in the software industry today. A lot of efforts are becoming less about software and more about cloud software. The whole gamut of cloud technology; platform, service, infrastructure, or platforms on platforms are growing rapidly in number. The days you didn’t need to know what the cloud was are rapidly coming to an end. As I move further along in my efforts with cloud development, both at application level and services levels, I’ve come to a few conclusions about what I do and do not need. The following points are what I have recently drawn conclusions about, that cause frustration or are drawn from the beauty of cloud architecture.
---

Cloud Architecture is becoming more and more relevant in the software industry today.  A lot of efforts are becoming less about *software* and more about *cloud software*.  The whole gamut of cloud technology; platform, service, infrastructure, or platforms on platforms are growing rapidly in number.  The days you didn’t need to know what the cloud was are rapidly coming to an end.

As I move further along in my efforts with cloud development, both at application level and services levels, I’ve come to a few conclusions about what I do and do not need.  The following points are what I have recently drawn conclusions about, that cause frustration or are drawn from the beauty of cloud architecture.

**REST is King, Period**

When I use REST in this context, I don’t just mean a nice clean URI or “*not SOAP*”.  I’m talking about the whole entire enchilada of REST Architecture Principles.  A good place to start learning about REST is the [Wikipedia Article](http://en.wikipedia.org/wiki/Representational_State_Transfer).  Other key resources to check out include;  [Roy T. Fielding’s Dissertation](http://www.ics.uci.edu/~fielding/pubs/dissertation/top.htm), specifically [chapter 5](http://www.ics.uci.edu/~fielding/pubs/dissertation/rest_arch_style.htm), [Principled Design of the Modern Web Architecture](http://www.ics.uci.edu/~taylor/documents/2002-REST-TOIT.pdf), and the O’Reilly Book [RESTful Web Services](http://oreilly.com/catalog/9780596529260).

REST Architecture is fundamental to the web and the fact that the web is continuous in uptime.  The web, or Internet, doesn’t go down, doesn’t crash, and is always available in some way.  REST Architecture and the principles around it are what enables the web to be this way.  The cloud seeks to have the same abilities, functionality, and basically be always on, thus REST Architecture is key to that underpinning.

**Core Development**

Currently I do most of my development with C# using the .NET Framework.  This is great for developing in cloud environments in Windows Azure and Amazon Web Services.  The .NET Framework has a lot of libraries that work around, with, and attempt to provide good RESTful Architecture.  However, there are also a lot of issues, such as the fact that WCF and ASP.NET at their core aren’t built with good intent against RESTful Architecture.  ASP.NET MVC and some of the latest WCF Releases (the out of band stuff) are extensively cleaning this up and I hear that this may be sooner than later.  I look forward to have cleaner, bare bones, fast implementations to use for RESTful development in Azure or AWS.

The current standing ASP.NET (Web Forms) Architecture is built well above the level it should be to utilize REST Architecture well.  Thus it creates a lot of overhead and unnecessary hardware utilization, especially for big sites that want to follow good RESTful Practice.

WCF on the other hand had some great ideas behind it, but as REST increased in popularity and demanded better use of the core principles the web is founded on, the WCF model has had to bend and give way some of its functional context in order to meet basic REST Architecture.

Anyway, that’s enough for my ramblings right now.  Just wanted to get some clear initial thoughts written down around Cloud Architecture needs for the software developer.
