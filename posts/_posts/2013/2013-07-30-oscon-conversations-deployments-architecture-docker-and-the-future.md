---
title: 'OSCON : Conversations, Deployments, Architecture, Docker and the Future?'
date: 2013-07-30 16:43:21 -0700
last_modified_at: 2013-08-08 12:45:40 -0700
permalink: /2013/07/30/oscon-conversations-deployments-architecture-docker-and-the-future/
slug: oscon-conversations-deployments-architecture-docker-and-the-future
wp_id: 8647
original_url: https://compositecode.blog/2013/07/30/oscon-conversations-deployments-architecture-docker-and-the-future/
categories:
- .NET Bits
- Architecture
- Basho
- Conferences
tags:
- container
- container technology
- docker
- open source
- oscon
excerpt: 'I wrote about my first day of OSCON “OSCON : Day 1, Windows Just Doesn’t Do Cloud Foundry… but, there’s a fix for that…“. The rest of the week was most excellent. I caught up with friends and past coworkers. I heard about people working on some amazing new projects. Some things I will try …'
---

![](https://photos.adron.me/Software/Misc-Images/Just-Icons-and-Bits/i-sqjsXrf/0/Th/oscon_logo_twitter-Th.jpg)I wrote about my first day of OSCON “[OSCON : Day 1, Windows Just Doesn’t Do Cloud Foundry… but, there’s a fix for that…](/2013/07/25/oscon-day-1-windows-just-doesnt-do-cloud-foundry-but-theres-a-fix-for-that/)“. The rest of the week was most excellent. I caught up with friends and past coworkers. I heard about people working on some amazing new projects. Some things I will try to write up in the coming days, as I’m sure some of it will be making the tech news (if not the regular people news too).

## Conversations

Had some great conversations about the direction of enterprise and paas uptake. It’s great to hear that there is some movement in that space finally. As one would expect however, there is still a lot of distance for the enterprise to catch up on, but they’ll get there – or fall apart in the meantime.

There were also tons of conversation about the [Indiegogo Ubuntu Edge](http://www.indiegogo.com/projects/ubuntu-edge) mobile device. This device is a great looking and sounds like a solid idea. The questions arise in the fact that they’re working to make this a purely crowd funded project. This wouldn’t be a concern if they were trying to just get a few million in capital, but they’re aiming for $32 million! Overall though, with 128 GB, Dual LTE Antennas for Europe and the US, a top tier screen in quality and design, a metal body and also multiple other features that put this phone ahead of anything out there. I hope it’s successful, but I must admit my own hesitance. What’s your take on the device?

## Deployments

Over the course of the conference I talked to and worked with a number of other individuals playing around with Cloud Foundry and also OpenShift. The primary aspect that we worked on was strategies around deployment of these PaaS Technologies.

We also worked with Iron Foundry to extend Cloud Foundry to support .NET. If you love .NET or hate .NET, wherever in that spectrum, it has an absolutely huge user base still. Primarily because .NET spent the last decade and a few years going head to head against Java in the Enterprise, and we all know the enterprise is slow to shift anything. So for now and the foreseeable future .NET is an extremely large part of the development world. Having it work in your PaaS is fundamental to gaining significant enterprise share. Cloud Foundry is the only open source, internally usable PaaS on the market today. There are closed source options available, but that obviously doens’t come up at OSCON.

While at OSCON, I also got to discuss architecture and deployment of [Riak](http://basho.com/riak/) with a number of people. The usage of Riak continues to grow and the environments, use cases and tooling that people are using Riak with and for is always an interesting space for me. I also got to discuss deployment of Cassandra and even some [Neo4j](http://www.neo4j.org/), [Redis](http://redis.io/) and Riak side by side deployments. People have used an interesting mix of NoSQL solutions out there to pull their respective data together for their needs.

Among all these deployments, conversations regularly returned to a known topic of mine. Cloud computing and who is capable of what, where and when. [AWS](http://aws.amazon.com/) is still an easy leader in cloud computing, not just in customers but in technology. This also brought up the [concerns and apathy that some have around OpenStack](http://diversity.net.nz/on-openstack-and-the-aws-api-internal-divisions-surface/2013/07/24/) ([hat tip to Ben Kepes for the write up](http://diversity.net.nz/on-openstack-and-the-aws-api-internal-divisions-surface/2013/07/24/)) working more homogeneously with AWS. Whatever the case might be, the path for OpenStack needs to be clarified regularly. I imagine the next movement is going to be away from being too concerned with infrastructure and increased concern with portability of applications and development of applications.

![](/images/adronhall.smugmug.com/Software/Misc-Images/Bad-Resume/i-Nw9QXMC/0/S/microsoft-communism-S.jpg)Another growing topic of discussion was around building applications for, on and with [Windows Azure](http://www.windowsazure.com/). Microsoft has actually become dramatically more involved in open source in an honest and more integrity based way. I’m honestly amazed at how far they’ve come from the declaration years ago that “[open source is a cancer](http://www.slate.com/articles/technology/technology/2005/11/red_herring.html)” and the all too famous, “[linux is communism](http://www.theregister.co.uk/2000/07/31/ms_ballmer_linux_is_communism/)“. Whatever that was supposed to mean, they didn’t seem to get it back then. Now however, they regularly contribute to open source projects on [codeplex](http://www.codeplex.com/) but also [github](http://www.github.com) and other places. Microsoft has even contributed to the Linux kernal a few months ago.

That leads me to the next topic that came up a number of times…

## Architecture

There’s been a lot of discussion about architecture around PaaS, containers (more on that in a moment), distributed systems in general and distributed databases. As I wrote about recently, “[Architectural PaaS Cracks or Crack PaaS](/2013/07/27/architectural-paas-cracks-or-crack-paas/)” the world of distributed systems and distributed databases has more than a few issues when working together in a PaaS environment. This brought up the discussion about what solutions exist today, solutions I look forward to writing and building in the coming months.

The most immediate solution to scalable data sources is still to run your operational data sources such as Neo4j, Redis, Riak or other database autonomously but residing close to your PaaS System. The current public PaaS Providers do exactly this and in some cases extend that to offer the databases and data sources as services through add-ons. These are currently great solutions, but require time, effort and custom development work when setting up internally.

This leads me to the last topic…

## The Story of a Container – Docker

Well, not just [Docker](http://www.docker.io/), but containers in general and Docker specifically. First some context about what a container is.

**Container** – In this particular context I’m writing about a container, or more specifically a runtime-container, that isolates resources for applications or services. Containers are common in PaaS technologies to help isolate the specific services or applications when they’re on a single physical machine or instance. For each of the respective PaaS systems that came up at OSCON we have dotCloud from the same team that created Docker, Cloud Foundry has Warden and OpenShift has gears and Red Hat Enterprise Linux OS specific containers.

I’ve studied Warden a little in the past while I was working with [AppFog](https://www.appfog.com/) and [Tier 3](http://www.tier3.com/) around Cloud Foundry. Warden is a great piece of technology. However the star at OSCON was clearly Docker. I jumped into a number of conversations around Docker. This conversation would then take the direction to containers becoming the key to PaaS tooling and systems growth and increasing capabilities. That leads me back to my previous blog entry “[Architectural PaaS Cracks or Crack PaaS](/2013/07/27/architectural-paas-cracks-or-crack-paas/)” and one of the key solutions to the data tier issue.

### Containers, A Solution for Scaling the Data Tier

One of the issues that comes up when trying to scale any distributed database in a PaaS Environment is how to provide multi-tenancy without spooling up new instances for each and every single installation of a node within that distributed database. Here’s an example diagram of the requirements behind a scalable distributed database.

![Masterless, Distributed Cluster of Nodes](/images/adronhall.smugmug.com/Software/Course-Materials/Distributed-Databases/i-fgPBHqx/0/S/Masterless-Cluster-2--S.png)

*Masterless, Distributed Cluster of Nodes*

In a default configuration you’d want each node to be running on a physical machine or dedicated virtual instance. This is for performance reasons as well as reasons for load balancing, security, data integrity and a host of others. This is the natural beginning state of a highly available distributed database or distributed system.

Trying to deploy something like this into a PaaS environment is tricky. Take into account that there is no such thing in application or service speak as an instance, and especially not anything such as a physical server. The real division between process and resources are containers. These containers are what actually needs to run the distributed system node. This becomes possible, if a distributed system node can be deployed to and executed from within a container.

### Enter Docker

[![](/images/adronhall.smugmug.com/Software/Misc-Images/Just-Icons-and-Bits/i-CjZhXch/0/S/homepage-docker-logo-S.png)](http://www.docker.io)After reviewing Docker, the capabilities around it and the requirements of a distributed database, it looks like an ideal marriage of the two technologies. Already Docker has Redis and other database technologies running on it. The Container technology around Docker looks like an ideal fit to extend distributed systems to run autonomously of a single physical machine or single instance per node. This would enable nodes to be deployed as resources are available to provide a more seamless and PaaS style deployment for systems like Cassandra, Riak and related distributed systems. Could this be the next evolution of affordable distributed systems, containers to the rescue?

I’ll be reporting back on my progress, this could be cool!

Stay tuned for a write up on [Docker](http://www.docker.io/) in the near future. For more information now check out [http://www.docker.io](http://www.docker.io/).

[![](/images/adronhall.smugmug.com/Software/Misc-Images/Logo/i-5zk96td/0/O/AH---Logo-32x32.png)](http://adron.me)
