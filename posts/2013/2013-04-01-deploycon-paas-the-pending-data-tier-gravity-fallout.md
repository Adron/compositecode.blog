---
title: Deploycon, PaaS & the pending data tier gravity fallout…
date: 2013-04-01 15:52:30 -0700
last_modified_at: 2013-04-01 15:55:37 -0700
permalink: /2013/04/01/deploycon-paas-the-pending-data-tier-gravity-fallout/
slug: deploycon-paas-the-pending-data-tier-gravity-fallout
wp_id: 7986
original_url: https://compositecode.blog/2013/04/01/deploycon-paas-the-pending-data-tier-gravity-fallout/
categories:
- Architecture
- Cloud Foundry
- Cloud Speak
- OpenShift
- Platform (as a Service)
tags:
- app
- applications
- bosh
- cluster
- data
- data integrity
- data tier
- database
- deploycon
- deployment
- distributed database
- paas
- platform services
- software
- web app
excerpt: 'For a quick recap of last years Deploycon & related talks, check out my “Day #3 => DeployCon && Enterprise && Data Gravity” entry from last year. PaaS Systems aren’t always effectively distributed. Heroku has fallen over every time east-1 has gone down at AWS. Not that I’m saying they’ve done bad, just pointing that …'
---

For a quick recap of last years Deploycon & related talks, check out my “[Day #3 => DeployCon && Enterprise && Data Gravity](/2012/06/15/day-3-deploycon-wheres-enterprise-data-gravity/)” entry from last year.

[![](/images/adronhall.smugmug.com/Software/Meetups-N-Conferences/Deploycon-2013/i-5fMvzd3/0/O/deploycon-logo.png)](http://deploycon.com/)PaaS Systems aren’t always effectively distributed. Heroku has fallen over every time east-1 has gone down at AWS. Not that I’m saying they’ve done bad, just pointing that out. With Cloud Foundry, there’s several key SPOFs (Single Points of Failure), and with all PaaS Systems the data tier is often the neglected pairing of the system. I’ve been wanting to write about this for a few months now and Deploycon has lit a fire for me to do just that.

## Deploycon – “*Platform Services and Developer Expectations” \*\**

I’m on a panel at Deploycon titled “*Platform Services and Developer Expectations”* and this leads right back around to that. This SPOF issue is concerning to me as PaaS Providers talk up the offerings more and more with little light actually shone on this issue. In some ways each is moving away form their respective SPOFs, but overall they’re all pretty prevalent throughout. For security, each has a non-distributed database, which technically needs backed up still – no clear replication or other mechanisms setup to ensure data integrity in a failure situation. Of course, the huge saving grace with a PaaS, is that if the overall system goes down or a SPOF blows up, all the existing deployed applications will generally continue to run. Unless of course the routing and networking are also SPOF. This is the largest glaring concern with PaaS Systems that I see today.

One of the other things about PaaS that has always led to a ton of questions is “what about my PostGresql/mysql/Riak/mongodb/database thing and how do I do X, Y, Z with it to ensure scalability in my PaaS.” In almost every case it ends with a simple and unfortunate answer, “…when it comes to data, a PaaS doesn’t really do a damn thing for ya…” This is obviously not very helpful. The entire reason to put a PaaS into place is to simplify life, the sad fact that it barely does a thing for the data tier isn’t very helpful.

Now, hold on a second before you start screaming at me about “but a PaaS does X, Y and Z and isn’t even supposed to touch that aspect of things…” let me elaborate a bit more. The panel at Deploycon states “…Developer Expectations” and when things are getting simplified in the way a PaaS does, developers assume that if it does all this fancy magic for an application it ought to simplify the data side of things too! Right? Well no, and it isn’t going to for the foreseeable future. But no matter what, it doesn’t change the fact that developers often have that expectation.

Now, I could write at length about all the reasons that PaaS doesn’t really do anything for the data tier. I could wax poetic about how a distributed database (re: Riak, Cassandra, etc) just doesn’t lend itself to a cookie cutter approach to deployment under a PaaS or an RDBMS has umpteen different configurations for stability, scaling, hot swappable services, and other such complexities around the data tier. But instead I’m going to skip all, maybe cover some of those things another day, and jump right into some of the things that are actually moving forward to fill this gap.

## BOSH, Cloud Foundry, OpenShift & fixing the data tier…

The most obvious reason there isn’t a simple turn key solution to the data side of things with a PaaS ecosystem is that data is complex and extremely diverse. There’s distributed key/value stores (Riak, Cassandra), there’s sort of kind of distributed databases (Mongo), graph databases (Neo4j), the age old RDBMS (DB2, SQL Server, Oracle’s Stuff, etc) and the million solutions around that, there’s key/value in memory styled databases that are insanely fast, like Redis. Expanding just slightly you have software that works around these systems such as Hadoop & Riak CS & the list goes on. All of it focused on the data tier and maintaining one, two or some form of the three points around CAP Theorem (<http://en.wikipedia.org/wiki/CAP_theorem>), atomicity and other key capbilities.

All of the PaaS Systems, including public and private often have some sort of plug-in style architectures for data. Whether it is [Apprenda](http://apprenda.com/) which is closed to community and closed source or an ongoing open to community PaaS like OpenShift or Cloud Foundry, things still fall almost entirely to the developers or database team to build an architecture around the data. When looking at solutions to simplify data in PaaS Systems the closed source solutions we have no idea what they’re up to in this regard. The one’s that are open source or in large part public and involved in the community PaaSes, like EngineYard, Heroku, Cloudbees and others we can really see the directions and efforts around creating real PaaS style solutions to the data tier problem.

***BOSH, Vagrant, etc…***One of the best solutions I’ve seen so far is the ability of Bosh, which was created by the Cloud Foundry team while at VMware, to spool up an environment that includes such things as a Riak Cluster (or other cluster). Currently Brian McClain & Dr Nic have worked to put together such Bosh + Vagrant scripts & get things rolling. I myself will be spending some considerable time on just that. But beyond that this is a good start in enabling data tier back ends.

How to close the gap, between absurdly simple application deployment and still arduous and difficult data tier deployment? For the next several years I think we’ll have cumbersome deployment practices around the data tier. There won’t be anything as elegantly simple as Cloud Foundry’s single line deployment or AppFog’s one click deployment of a web application. The best we can do at this time, is to streamline around pieces and architectures, and at least get them into a kind of simple 3 step deployment.

Please drop a comment or two on how you think we might simplify the data side of the PaaS toolchain. Also drop a few tweets in the twitterverse too, I’m sure that’ll be exploding as usual. I’m @adron, ping me.

Cheers, happy data architecting.

\*\* the [Deploycon](http://deploycon.com/agenda/)[panel will be at 4:30pm in Santa Clara on April 2nd](http://deploycon.com/agenda/). Come [check it out](http://deploycon.com/).
