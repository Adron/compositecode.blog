---
title: Going Live, Data & Pricing @ Orchestrate
date: 2014-02-04 11:03:17 -0800
last_modified_at: 2014-02-04 11:03:17 -0800
permalink: /2014/02/04/going-live-data-pricing-orchestrate/
slug: going-live-data-pricing-orchestrate
wp_id: 9641
original_url: https://compositecode.blog/2014/02/04/going-live-data-pricing-orchestrate/
categories:
- Databases
- Orchestrate.io
- Reviews
tags:
- database
- graph
- graph store
- key value
- keyvalue
- nosql
- orchestrate
- orchestrate.io
excerpt: Over the last few months while working on the prototype around Deconstructed I’ve been using the Orchestrate service offering exclusively. With their service around key value and graph store easily accessible via API it was a no brainer to get started building ASAP. Today, that service goes full beta! You can get the full lowdown …
---

Over the last few months while working on the prototype around Deconstructed I’ve been using the Orchestrate service offering exclusively. With their service around key value and graph store easily accessible via API it was a no brainer to get started building ASAP. Today, that service goes full beta! You can get the full lowdown at the [Orchestrate site](http://orchestrate.io/).

[![](https://photos.adron.me/Software/Misc-Images/Just-Icons-and-Bits/i-8sGKrTJ/0/S/rings_trans_horiz_new%20%282%29-S.gif)](http://orchestrate.io/)

You might recall that I mentioned [Orchestrate a while back when they lept into the PIE Class a few months ago](/2013/07/23/pies-third-class-you-better-keep-an-eye-on-these-companies/). So here’s a few quick thoughts on the release and what Orchestrate is.

The basic premise is Orchestrate provides full-text search, time ordered events, graph, key value storage and a lot more. All of these capabilities are offered via an API that create a product that’s extremely easy to get started. Think about what you’d need to do to get full-text search against a key value setup. Really think about it. Yeah? That’s a lot of steps. With Orchestrate you just sign up and start using it. Think about setting up a graph store and managing it on production systems. Yeah? Lot’s of work once it gets used. Again, just sign up, it’s all there, the graph to the key value to the event series and more. All the NoSQL juice you need located in a single service so you’re not fighting and maintaining multiple databases, nodes or whatever you’re working with.

Sing up. Use.

I will copy one thing from the press release….

- Ad hoc search queries with Lucene
- Event and time-ordered storage for activity feeds, sensor data
- Create and query graph relationships
- Easy to understand pricing
- Data export at will – no lock-in
- Standards compliant data security protocols
- Daily data backups
- Bulk data loading
- Daily and hourly usage monitoring
- A single, simple interface – JSON data in/out
- Designed to complement existing databases and MBaaS services
- Client libraries for Java, Node.js, and Go. More on the way!

## Using Orchestrate

There are quotes in the press release, but I’ve got a few myself. I’m working to build out a prototype service that I and Aaron Gray will be releasing soon. Our startup is called Deconstructed, but more on that later. Without [Orchestrate](http://orchestrate.io/) my dev cycle would be longer each day, as I battle with maintaining the data sources that I need. Without it I would have spent another 2-3 weeks setting up and staging nosql database technology. All things I didn’t really need to do. I needed to focus on the service, the value that we’ll soon bring to our customers.

It really boils down to this, and don’t get me wrong, I’m a total data nerd. But when it comes to building a product or service, the last thing I want to do is fight with managing the data anymore than I have to. That notion inspired me to write “[Sorry Database Nerds, Nobody Actually Gives a Shit](/2013/11/03/sorry-database-nerds-nobody-actually-gives-a-shit/)” which still holds true. I can’t think of a single business that wants to sit around and grok how an index works in a key value or what the spline of text-search queries is going to be.

## Pricing

Pricing is sweet, for many that want to try it out things are free. Prices go up a bit more from there, but if you fall into the pricing you’re doing some business and ought to be rolling in a few bucks eh!

The interesting thing to me about pricing is that they’ve structured it around MOp, which stands for MegaOps. More specifically that’s one million API calls or one million operations.

## Summary

If you write code, even a little or if you manage data you should do yourself the service and check out what [Orchestrate](http://orchestrate.io/) has built. It’s a solid investment of time. I’ll have a lot more on Orchestrate and how we’re using the service for Deconstructed and more on using the service with JavaScript in the coming months. Keep your eyes peeled and I might even have some Dart and C# magic thrown in there to boot! Check em’ out, until later, happy hacking.
