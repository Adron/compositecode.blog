---
title: Architectural PaaS Cracks or Crack PaaS
date: 2013-07-27 10:30:09 -0700
last_modified_at: 2013-08-08 12:46:03 -0700
permalink: /2013/07/27/architectural-paas-cracks-or-crack-paas/
slug: architectural-paas-cracks-or-crack-paas
wp_id: 8538
original_url: https://compositecode.blog/2013/07/27/architectural-paas-cracks-or-crack-paas/
categories:
- Cloud Foundry
- Cloud Speak
- Iron Foundry
- OpenShift
- Platform (as a Service)
tags:
- cartridge
- cassandra
- data
- database
- databases
- paas
- polyglot
- riak
- service
excerpt: Over the last couple years there have been two prominent open source PaaS Solutions come onto the market. Cloud Foundry & OpenShift. There’s been a lot of talk about these plays and the talk has slowly but steadily turned into traction. Large enterprises are picking these up and giving their developers and operations staff a …
---

![](/images/adronhall.smugmug.com/Software/Misc-Images/Logo/i-Z4XmSP4/1/O/PAAS-Rocker-Logo.jpg)Over the last couple years there have been two prominent open source PaaS Solutions come onto the market. **[Cloud Foundry](http://www.cloudfoundry.com/)** & **[OpenShift](https://www.openshift.com/)**. There’s been a lot of talk about these plays and the talk has slowly but steadily turned into traction. Large enterprises are picking these up and giving their developers and operations staff a real chance to make changes. Sometimes disruptive in a very good way.

However, with all the grandeur I’m going to hit on the negatives. These are the missing parts, the serious pain points beyond just some little deployment nuisance. Then a last note on why, even amidst the pain points, you still need to make real movement with PaaS tooling and technologies.

## Negative: The Data Story is Lacking

Both Cloud Foundry and OpenShift have a way to plug into databases easily.

Cloud Foundry provides ways to build a [**Cloud Foundry Service**](http://docs.cloudfoundry.com/docs/using/services/) that becomes the bound and hooked in SQL Server, MySQL, Postgresql, Redis or whatever data storage service you need. For more details on [building a service](http://docs.cloudfoundry.com/docs/running/architecture/services/), check out the [echo example on the vcap sample github project](https://github.com/cloudfoundry/vcap-services-sample-release).

OpenShift has what are called [**Cartridges**](https://www.openshift.com//developers/cartridge-authors-guide) which provide the ability to add databases and other services into the system. For more information about the cartridges check out [Red Hat’s OpenShift Documentation](https://www.openshift.com/developers/documentation) and also the [forums](https://www.openshift.com/community).

Cloud Foundry and OpenShift however have distinctive weak spots when it comes to services that go beyond a mere single instance database. In the case of a true distributed database such as Cassandra, HBase or Riak, it is inordinately difficult to integrate a system that any PaaS inter-operates with well. In some cases it’s irrelevant to even try.

The key problem being that both of the PaaS systems assume the mantle of master while subjugating the distributed database a lower tier of coordination. The way to resolve this at the moment is to do an autonomous installation of Riak, Cassandra, Neo4j or other database that may be distributed, stored hot swappable, or otherwise spread across multiple machine or instance points. Then create a bound connection between it and the PaaS Application that is hosted. *This is the big negative in PaaS systems and tooling right now, the data story just doesn’t expand well to the latest in data and database technologies.* I’ll elaborate more about this below.

## Negative: Deployment is Sometimes Easy, Maintenance is Sometimes Hard

Cloud Foundry is extremely rough to deploy, unless you use Bosh to deploy to either VMware Virtualized instances or AWS. Now, you could if resources were available get Bosh to deploy your Cloud Foundry environment anywhere you wanted. However, that’s not easy to do. Bosh is still a bit of a black box. I myself along with others in the community are working to document Bosh, but it is slow going.

OpenShift is dramatically easier to deploy, but is missing a few key pieces once deployed that draw some additional operational overhead. One of those is that OpenShift requires more networking management to handle routing between various parts of the PaaS Ecosystem.

Overall, this boils down to what you need between the two PaaS tool chains. If you want Cloud Foundry’s automatic routing and management between nodes. This is a viable route, but if your team wants to manage the networking tier more autonomous from the PaaS environment then maybe OpenShift is the way to go. In the end, it’s *negative bumpy territory to determine which you may or may not want based on that.*

## Negative: Full Spectrum Polyglot, Missing Some

Cloud Foundry has a wider selection of languages and frameworks with community involvement around those with groups like [Iron Foundry](http://ironfoundry.org/). OpenShift I’m sure will be getting to parity in the coming months. I have no doubt between both of these PaaS Ecosystems that they’ll expand to new languages and frameworks over time. Being polyglot after all is a no brainer these days!

## Why PaaS Is, IMHO, Still Vitally Important

First toss out the idea that huge, web scale, Facebooks and Googles need to be built. Think about what the majority of developers out there in the world work on. Tons and tons and tons of legacy or greenfield enterprise applications. Sometimes the developer is lucky enough to work on a full vertical mix of things for a small business, but generally, the standard developer in the world is working on an enterprise app.

PaaS tooling takes the vast majority of that enterprise app maintenance from an operational side and tosses it out. Instead of managing a bunch of servers with a bunch of different apps the operations team manages an ecosystem that has a bunch of apps. This, for the enterprises that have enough foresight and have managed their IT assets well enough to be able to implement and use PaaS tooling, is ***HUGE***!

For companies working to stay relevant in the enterprise, for companies looking to make inroads into the enterprise and especially for enterprises that are looking to maintain, grow or struggling to keep ahead of the curve – PaaS tooling is something that is a must have.

Just ask a dev, do they want to spend a few hours configuring and testing a server?  Do they want to deploy their application and focus on building more value into that application?

…being I’ve spent a few years being the developer, I’ll hedge on the side of adding value.

## What’s Next?

So what’s next? Two major things in my opinion.

**1. Fill the data gap.** Most of the PaaS tooling needs to bridge the gap with the data story. I’m working my part with testing, development and efforts to get real options built into these environments, but this often leads back to the data story of PaaS being weak. What’s the solution here? I’m in talks, ongoing, planning sessions ongoing, and we’ll eventually get a solid solution around the data side.

**2. Fix deployments & deployment management.** Bosh isn’t straight forward or obvious in what it does, Cloud Foundry is easily the hardest thing to deploy with many dependencies. OpenShift is easier to deploy and neither of them actually have a solid management story over time. Bosh does some impressive updates of Cloud Foundry, and OpenShift has some upgrade methods, but still over time and during day to day operations there hasn’t been any clear cut wins with viewing, monitoring and managing nodes and data within these environments.

[![](/images/adronhall.smugmug.com/Software/Misc-Images/Logo/i-5zk96td/0/O/AH---Logo-32x32.png)](http://adron.me)
