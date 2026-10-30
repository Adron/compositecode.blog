---
title: Seattle Code Camp – A Summary
date: 2012-06-17 10:13:29 -0700
last_modified_at: 2012-06-17 10:13:29 -0700
permalink: /2012/06/17/seattle-code-camp-a-summary/
slug: seattle-code-camp-a-summary
wp_id: 5828
original_url: https://compositecode.blog/2012/06/17/seattle-code-camp-a-summary/
categories:
- Conferences
- Presentations and Speaking
tags:
- aws
- big data
- chaos monkey
- code camp
- netflix
- paas
- platform as a service
- rackspace
- seattle
- seattle code camp
- tier 3
excerpt: Wow… that was great. I had three presentations. Well, honestly it was more like two presentations and a brainstorming session with about 3 dozen really smart people! First there was the “Node.js Rulz! JavaScript takes over the full stack“. This session went pretty well, and I hope I got a lot of developers riled up …
---

Wow… that was great.

I had three presentations. Well, honestly it was more like two presentations and a brainstorming session with about 3 dozen really smart people!

First there was the “***[Node.js Rulz! JavaScript takes over the full stack](https://seattle.codecamp.us/Sessions/Details/301)***“. This session went pretty well, and I hope I got a lot of developers riled up to give Node.js a try. I discussed the various testing, framework, and other libraries needed to get going with development. I also did a test deployment against [Tier 3’s Web Fabric PaaS](http://www.tier3.com/) ([Cloud Foundry](http://www.cloudfoundry.org) powered AWESOME). If you want to try out this deployment model, a sand box is available for free over at the [Iron Foundry Project](http://ironfoundry.org/) (.NET extensions for [Cloud Foundry](http://www.cloudfoundry.org)). Just sign up and we’ll get you added ASAP.

In summary, I went end to end with Node.js. Overall, it’s a beautiful thing that I highly suggest people give a thorough look at.

The next session I did was “***[Removing the Operating System Barrier with Platform as a Service](https://seattle.codecamp.us/Sessions/Details/283)***“. This session covers my primary live of wrok and advocacy these days. It involves a key facet of software development that I’ve dubbed the “Beer Factor”. More on the “Beer Factor” later.  🙂

In this session I covered the history, reasons for, and overall impetus of PaaS (Platform as a Service) and why it matters to software developers. The general gist is, it is changing the very way we can and will be doing software development. The change, is absolutely for the better. Developers, consider yourself empowered. Also, more on this in the near future.

The last sessions, which was more of a large scale brain storming session, was “[Putting it all together, letting apps lead the cycle, TDD in the cloud](https://seattle.codecamp.us/Sessions/Details/284)“. This session really kicked off a lot of different thoughts around the MAJOR gaps in cloud computing development. So I’m going to break out some of those key points below:

- There is no logical, easy, or well defined way to test deployments to the cloud. If you’re AWS, Rackspace, Windows Azure, Tier 3, AppFog or any other company – deployment is not simple. A big impetus is to test production, something that absolutely has to be done. The gateways or checks in deploying software; for the underlying infrastructure, the platform, or anything that is geographically dispersed, multi-instance, or similar is very difficult. For software developers, devops, and the like, we want this to be better. We all brainstormed a bit around this and the resounding sentiment was, “damn, this is hard, yet so powerful and enabling that we have to figure out better ways to test and do deployments into cloud environments”
- Chaos Monkey must bet let loose on the WORLD!!  See below:

  [![clive boulton](https://twimg0-a.akamaihd.net/profile_images/1960400193/cb_212x212_normal.png)**clive boulton** ‏~~@~~**iC**](https://twitter.com/#!/iC)

  [~~@~~**adrianco**](https://twitter.com/#!/adrianco) chances of open sourcing Chaos Monkey? Room full of Cloud Devs want, egged on by [~~@~~**adron**](https://twitter.com/#!/adron)[~~#~~**seattlecodecamp**](https://twitter.com/#!/search/%23seattlecodecamp "#seattlecodecamp")

  [![adrian cockcroft](https://twimg0-a.akamaihd.net/profile_images/2166370139/da6048b3_unicorn-fish_normal.jpg)**adrian cockcroft** ‏~~@~~**adrianco**](https://twitter.com/#!/adrianco)

  [~~@~~**iC**](https://twitter.com/#!/iC)[~~@~~**adron**](https://twitter.com/#!/adron) it’s on the way, actively being cleaned up for github

  Adrian Cockroft RULZ! Thx Adrian, we’ll all keep an eye out for that! 🙂
- One of the other things that was brought up was the endless options, and thus complexity, around the data story these days. This translates to, how do we simplify deployment of relational, document, object, key value or other types of databases? Each needs a particular type of default deployment. How do we as developers create a better model to get our data repositories of choice up and live. With Cloud Foundry the data deployments are a single node, which isn’t really useful for things like Riak, Mongo, Couch or databases that need to start with three or more nodes. It’s ok for relational databases, but it is very common to need that hot swappable database running somewhere. These are all questions that need answered to make the data story of PaaS technologies more palatable.
- Monitoring and intelligent systems. Some suggestions around monitoring, which came from the question of how to test a deployed system before and after deployment, where pretty solid. Nodes need to be intelligent enough to be able to identify they’re live, active, and doing X, Y or Z. Controllers need to understand and know how to interact with these nodes. The back and forth is somewhat complex, but I can imagine just like with Cloud Foundry, they’re is a viable and simple solution among all of this with the appropriate abstractions and build out of systems.

That’s my summary. I had a blast, got to see a lot of people I know and meet a lot of new people I didn’t know. I always love being able to catch up and really expand on what our efforts are individually and collectively as a development community. Great fun, until next time, cheers!
