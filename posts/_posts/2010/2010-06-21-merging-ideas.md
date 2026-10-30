---
title: 'Merging Ideas : Transit and Tech'
date: 2010-06-21 04:02:18 -0700
last_modified_at: 2010-06-21 04:45:05 -0700
permalink: /2010/06/21/merging-ideas/
slug: merging-ideas
wp_id: 52
original_url: https://compositecode.blog/2010/06/21/merging-ideas/
categories:
- Ideas
tags:
- transit
excerpt: So I got up on a Saturday, pondering what routes and buses would need to be taken to go from Belltown to Fremont here in the Seattle area. Because I live here and have a transit oriented mind (I do write Transit Sleuth also…) I know which buses come where that would make a trip to Fremont real easy. Fortunately there is a site called onebusaway.org here in Seattle that helps one that likes to effectively use transit. The core Metro, Pierce County, Sound Transit, and other sites are of minimal use in comparison. They can give you basic routing but other than that there isn’t a lot of other information for the hard core transit user. So this Saturday morning I stumbled into an idea that wouldn’t be too expensive to implement within the cloud (either Azure or AWS). Here’s my initial idea without any research done except to know that somewhere, somehow, Metro, Sound Transit, and the other authorities in the Seattle area offer some type of data and GPS location feeds.
---

So I got up on a Saturday, pondering what routes and buses would need to be taken to go from Belltown to Fremont here in the Seattle area.  Because I live here and have a transit oriented mind (I do write [Transit Sleuth](http://transitsleuth.com) also…) I know which buses come where that would make a trip to Fremont real easy.  Fortunately there is a site called onebusaway.org here in Seattle that helps one that likes to effectively use transit.  The core [Metro](http://metro.kingcounty.gov/), Pierce County, [Sound Transit](http://www.soundtransit.org), and other sites are of minimal use in comparison.  They can give you basic routing but other than that there isn’t a lot of other information for the hard core transit user.

So this Saturday morning I stumbled into an idea that wouldn’t be too expensive to implement within the cloud (either [Azure](http://www.microsoft.com/windowsazure) or [AWS](http://aws.amazon.com)).  Here’s my initial idea without any research done except to know that somewhere, somehow, [Metro](http://metro.kingcounty.gov/), [Sound Transit](http://www.soundtransit.org), and the other authorities in the Seattle area offer some type of data and GPS location feeds.

[![Transit & Logistics Cloud Idea](https://compositecode.blog/wp-content/uploads/2010/06/logistics-idea.jpg "Transit & Logistics Cloud Idea")](https://compositecode.blog/wp-content/uploads/2010/06/logistics-idea.jpg)

*Transit & Logistics Cloud Idea*

The connectivity shown in the diagram above is nice and all, but what exactly do I want for a front end?  That’s the next point, what is needed is a truly flexible dashboard.  One needs to be able to actually query against locations and find multiple options to the various places they’re trying to travel to.  For instance, the trip from Belltown to Fremont isn’t just one bus.  I could easily get the 17, 30, 26, or 28.  But there isn’t an easy way to identify and track all of the nearby bus stop locations that those buses travel by on their route.  That’s where a dashboard of statuses and location information would come into play.

The idea would be able to track multiple bus stops in a particular location for various buses going in all directions.  This seems like a feasible idea.  The extension of that would be to get the stops within X distance from a particular location, possibly derived from an iPhone or some such.  I’d like to use this on an RIA for the Windows 7 Series, Blackberry, and iPhone – which I assume would be a boon for anyone that uses the Metro, Sound Transit, or surrounding services.

I have collected the following information for this *prospective* project.

The [onebusaway.org](http://onebusaway.org/) [Open Source Project](http://code.google.com/p/onebusaway/) that currently does bus tracking and other transit related information has some great research done already, which may be useful.

King County Metro has a page of [Q & A for developers](http://www.kingcounty.gov/transportation/kcdot/MetroTransit/Developers/QandA.aspx).  The [GTFS Data for Metro is available](http://metro.kingcounty.gov/GTFS/) too.

A really good discovery I found was the [UW Research](http://www.its.washington.edu/its_ws.html).  This site has all sorts of web services information related to traffic and transit.  In addition there is specific .NET examples and such.  Always nice to see the examples in the code or tech stack that I intend to use.
