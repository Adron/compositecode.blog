---
title: Aggregated Web Services Pt I
date: 2010-07-28 06:26:53 -0700
last_modified_at: 2010-07-28 08:15:43 -0700
permalink: /2010/07/28/aggregated-web-services-pt-i/
slug: aggregated-web-services-pt-i
wp_id: 808
original_url: https://compositecode.blog/2010/07/28/aggregated-web-services-pt-i/
categories:
- Architecture
tags:
- diagram
- enterprise architecture
- services
- web services
excerpt: I’ve been working through an architecture scenario recently. This is what I have so far. Multiple external web services, some SOAP and some REST, and some data sources in a SQL Server Database, Azure Table Storage, and flat files of some sort. All of these sources need to be accessed by a web site for read-only display. In the diagram below I’ve drawn out the primary three points of reference. The services that are external; Contract, Table Store, Document, Search, and Help Desk Services. The Website Web Services Facade, which would be an aggregated layer that then provides the various services via an internally controlled services layer. On top of that will be the web site, accessing the services from the aggregated layer with jQuery. Basic Three Tiers After creating this to get some basic idea of how these things should fit together, I moved on to elaborate on the web services aggregation layer. What I’ve sketched in this diagram is the correlation to architectural elements and the physical environments they would prospectively be deployed to. Again, broken out by the three tiers as shown above. Website and the respective jQuery, AJAX, and Market/CSS for display. Web Services, which include the actual architecture breakout; Facade Interface, Facade Aggregation Component, Cache & Non-cached DTOs (Data Transfer Objects), Cache Database/Storage, Caching Process, Lower Layer Aggregation Component, and the Poller Process for polling the external services. The cache is intended to use SQL Server, thus the red call out to the physical SQL Server cluster. The last tier, which isn’t being developed, but just providing data is the External Services, primarily shown to provide a full picture of all the layers.
---

I’ve been working through an architecture scenario recently.  This is what I have so far.  Multiple external web services, some SOAP and some REST, and some data sources in a SQL Server Database, Azure Table Storage, and flat files of some sort.  All of these sources need to be accessed by a web site for read-only display.  In the diagram below I’ve drawn out the primary three points of reference.

1. The services that are external; Contract, Table Store, Document, Search, and Help Desk Services.
2. The Website Web Services Facade, which would be an aggregated layer that then provides the various services via an internally controlled services layer.
3. On top of that will be the web site, accessing the services from the aggregated layer with jQuery.

[![base three tiers](/images/adronhall.smugmug.com/Software/Software-Development/aggregatedwebservices/TheAggregatedWebServices/948093751_gM9eX-O.png "base three tiers")](http://adronhall.smugmug.com/Software/Software-Development/aggregatedwebservices/TheAggregatedWebServices/)

*Basic Three Tiers*

After creating this to get some basic idea of how these things should fit together, I moved on to elaborate on the web services aggregation layer.  What I’ve sketched in this diagram is the correlation to architectural elements and the physical environments they would prospectively be deployed to.  Again, broken out by the three tiers as shown above.

1. Website and the respective jQuery, AJAX, and Market/CSS for display.
2. Web Services, which include the actual architecture breakout;  Facade Interface, Facade Aggregation Component, Cache & Non-cached DTOs ([Data Transfer Objects](http://en.wikipedia.org/wiki/Data_transfer_object)), Cache Database/Storage, Caching Process, Lower Layer Aggregation Component, and the Poller Process for polling the external services.
3. The cache is intended to use SQL Server, thus the red call out to the physical SQL Server cluster.
4. The last tier, which isn’t being developed, but just providing data is the External Services, primarily shown to provide a full picture of all the layers.

[![aggregate web services](/images/adronhall.smugmug.com/Software/Software-Development/aggregatedwebservices/TheAggregatedWebServicesFacade/948220226_K9QBg-O.png "aggregate web services")](http://adronhall.smugmug.com/Software/Software-Development/aggregatedwebservices/TheAggregatedWebServicesFacade/)

*Aggregate Web Services*

I primarily drew up these diagrams for discussion of the architecture, poke holes in it, or otherwise. Which speaking of, if any readers have input, question, or are curious please type up a comment and I’ll answer it ASAP.

As the effort continues there are some other great how-to write ups I will be putting together.  Everything from unit testing, mocking (with moq), how to setup test services, test services, and other elements of the project.  I’ll have all this coming, so keep reading & let me know what you think of the design so far, subscribe via e-mail (look to the metadata section below), or grab the RSS for the blog (see below also).

[![kick it on DotNetKicks.com](http://www.dotnetkicks.com/Services/Images/KickItImageGenerator.ashx?url=http%3a%2f%2fcompositecode.com%2f2010%2f07%2f28%2faggregated-web-services-pt-i%2f&bgcolor=3333FF&cfgcolor=CC3300)](http%3A%2F%2Fwww.dotnetkicks.com%2FServices%2FImages%2FKickItImageGenerator.ashx%3Furl%3Dhttp%253a%252f%252fcompositecode.com%252f2010%252f07%252f28%252faggregated-web-services-pt-i%252f%26bgcolor%3D3333FF%26cfgcolor%3DCC3300)

[![Shout it](http://dotnetshoutout.com/image.axd?url=http%3A%2F%2Fcompositecode.com%2F2010%2F07%2F28%2Faggregated-web-services-pt-i%2F)](http://dotnetshoutout.com/Aggregated-Web-Services-Pt-I-Composite-Code)
