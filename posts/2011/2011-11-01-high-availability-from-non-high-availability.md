---
title: 'High Availability From Non-High Availability: OpenStack, Dell, Crowbar, Private Clouds, and Moving the Enterprise Forward…'
date: 2011-11-01 10:57:59 -0700
last_modified_at: 2011-11-01 10:30:39 -0700
permalink: /2011/11/01/high-availability-from-non-high-availability/
slug: high-availability-from-non-high-availability
wp_id: 4161
original_url: https://compositecode.blog/2011/11/01/high-availability-from-non-high-availability/
categories:
- Architecture
- AWS
- Azure
- Cloud Speak
tags: []
excerpt: The Environment Recently a conversation came up about high availability in a traditional Enterprise Environment. Let me paint the picture for this environment; “This environment has several hundred servers, and several hundred applications. These application range in simple client server applications to n-tier applications strung across multiple services and machines. Some are resilient, some are not so resilient. These applications have administration that ranges from needing rebooted on a daily basis to not being touched for months at a time. Needless to say the range of applications is vast. In addition to all these applications the data center had a mix of hardware concerns that directly effected how applications were built.” With that basic idea, one can imagine that planning for high availability is by no means a simple thing. However there are opportunities now available, that Enterprises have never had previously. In the past an Enterprise would usually have some big heavy hitter come in, such as EMC. The Enterprise would then pay them hundreds of thousands or even millions of dollars to do an analysis. Then the Enterprise would probably fork over another couple hundred grand here and there. This would happen time and time again, until some level of high availability would be achieved. …read more by clicking through…
---

## The Environment

Recently a conversation came up about high availability in a traditional Enterprise Environment. Let me paint the picture for this environment;

> “This environment has several hundred servers, and several hundred applications. These application range in simple client server applications to n-tier applications strung across multiple services and machines. Some are resilient, some are not so resilient. These applications have administration that ranges from needing rebooted on a daily basis to not being touched for months at a time. Needless to say the range of applications is vast.
>
> In addition to all these applications the data center had a mix of hardware concerns that directly effected how applications were built.”

With that basic idea, one can imagine that planning for high availability is by no means a simple thing. However there are opportunities now available, that Enterprises have never had previously. In the past an Enterprise would usually have some big heavy hitter come in, such as EMC. The Enterprise would then pay them hundreds of thousands or even millions of dollars to do an analysis. Then the Enterprise would probably fork over another couple hundred grand here and there. This would happen time and time again, until some level of high availability would be achieved.

Well, to put it simply, a lot of that effort is unneeded today. The effort that is needed, with the right team, is in the hands of the Enterprise itself. Some people who know me, would immediately think I’m about to say “just setup an account at AWS and build to the cloud…” which is obviously the easiest, secure, and most progressive route to go. But no, I’m going to step in with some other solutions, that can be provided on-premise. I’ll elaborate at a later time the reasons behind this.

I’m going to now step through some key technologies available today. These can be used to provide high availability from the software architecture points of view. In your enterprise, if you have off-shored, outsourced, or otherwise attained your Enterprise Software, these functionalities and capabilities will be up to the creating provider. You’ll have to go to them for further information on how to change or adapt the architecture.

## Software Architecture

For in house software here are some APIs, SDKs, and tools to help attain the much sought after high availability (Always aiming for that mythical five 9’s).

### Dell’s Cloud Solutions

So without significant research time, the Dell Solutions can be thoroughly confusing at first glance. They don’t offer anything related to actual “cloud services” such as AWS, Windows Azure, or Rackspace. What they’re simply offering is hardware to build out resilient data centers and contributing actively to open source software solutions.

The Dell Cloud Edge Software is available on [Github](http://www.github.com) at [dellcloudedge](https://github.com/dellcloudedge). The best places to start researching what is available are on two key blogs; [JBGeorge Tech Blog](http://jbgeorge.net/) and [Rob Hirschfeld’s Blog](http://robhirschfeld.com/).

Another key part of the Dell Solution is Crowbar. [Dell open sourced Crowbar at the 2011 OSCON Conference](http://en.community.dell.com/dell-blogs/enterprise/b/inside-enterprise-it/archive/2011/07/27/dell-announces-availability-of-openstack-solution-open-sources-crowbar-software-framework.aspx). Even though most of the sample configurations revolve around Dell Poweredge Servers and Rackspace Cloud Builder Solutions, the software is available for use on system that are completely unrelated from Rackspace or Dell Solutions. Crowbar, simply put, is the software used to get servers up and running. As quoted on the Dell Announcement released during OSCON,

> “Bringing up a cloud can be no mean feat, as a result a couple of our guys began working on a software framework that could be used to quickly (typically before coffee break!) bring up a multi-node OpenStack cloud on bare metal. That framework became Crowbar. What Crowbar does is manage the OpenStack deployment from the initial server boot to the configuration of the primary OpenStack components, allowing users to complete bare metal deployment of multi-node OpenStack clouds in a matter of hours (or even minutes) instead of days.”

That quote now brings up the next piece of software, [OpenStack](http://www.openstack.org/). When building out a data-center it is a solid idea to begin building a platform on which things will operate. [OpenStack](http://www.openstack.org/) enables just that. There are two major elements of [OpenStack](http://www.openstack.org/) that are key; [OpenStack Compute](http://www.openstack.org/projects/compute/) and [OpenStack Storage](http://www.openstack.org/projects/storage/). This is where the architectural paradigm begins to change dramatically for traditional software. This is also where there will  a major sticking point for traditional Enterprise Software that relies primarily on a database on a server, with a web server on a server, and maybe some middleware or a service bus on another server. The massive problem is applications need to focus around horizontal scalability with compute and storage being the two key elements.

In many enterprises this is unfortunate, because a safe estimate would be 95% or more of enterprise applications don’t scale horizontally, or scale at all. If you’re an SOA shop, you’re much farther along than most. Most enterprises simply rely on the traditional vertical stack. This is a major problem. So how do we bridge this gap between the compute plus storage architectural design goal versus traditional architecture? That’s where the follow software comes to the rescue.

## Windows Server AppFabric

[![Windows Azure AppFabric (Click to visit the MS Azure AppFabric Site)](/images/adronhall.smugmug.com/Software/Misc-Images/Just-Icons-and-Bits/i-DvtZ9qS/0/S/WindowsAzureAppFabricjpg-550x0-S.jpg "Windows Azure AppFabric (Click to visit the MS Azure AppFabric Site)")](http://www.microsoft.com/windowsazure/appfabric/)

*Windows Azure AppFabric (Click to visit the MS Azure AppFabric Site)*

***(Not to be confused with the Windows Azure AppFabric, for [differences review this article](http://social.technet.microsoft.com/wiki/contents/articles/1445.aspx#Windows_Server_AppFabric))***

[![Windows Server AppFabric (Click for the MS Site)](/images/adronhall.smugmug.com/Software/Misc-Images/Just-Icons-and-Bits/i-W6MhzcL/0/S/WindowsServerAppFabricjpg-S.jpg "Windows Server AppFabric (Click for the MS Site)")](http://msdn.microsoft.com/en-us/windowsserver/ee695849.aspx)

*Windows Server AppFabric (Click for the MS Site)*

The Windows Server AppFabric has several capabilities that help an enterprise application leap forward into the modern era of horizontal scalability with a more clear way to focus on compute and storage. The feature set of the AppFabric includes these key functions that enable this leap forward (more information available in this [article](http://social.technet.microsoft.com/wiki/contents/articles/422.aspx)):

- Workflow Instance Management
- Scaling Out Distributed Applications

These by no means are the only features of AppFabric. For a thorough description of scenarios and applications around AppFabric check out [Introducing Windows Server AppFabric](http://compositecode.blog/wp-content/uploads/2011/11/introducing_windows_server_appfabric.pdf).

## In Summary

Where Does This Leave Enterprise Environments? The simple answer is, “***A really long way away from achieving the scalability, cost savings, integrity, agaility, and capabilities of public cloud computing***“. You can quote me on that. The effort to acheive data integrity and up time to perform standard business, it’s already here for Enterprises, but to go beyond that and extend hours of operation, acheive 5 9’s of up time, and decrease costs in a dramatic way is generally cost prohibitive in private cloud infrastructure and especially in traditional data center operations. The fact is, things will still go down. Applications have a long way from being resilient, idempotent, or designed with an architecture that allows them with the concept of the public cloud “design for failure” concept.

So what to do about this? The best thing for an Enterprise Application Environment is simply to start building applications with horizontal scalability in mind. Build with the concept of systems being nodes, with idempotent messaging, clear and redundant messaging queues, and thinking – even while limited by traditional data centers and limited visualization technologies – thinking in a resilient architectural style instead of the traditional vertical mindset.

These tools I’ve outlined can help your Enterprise move forward in a traditional data center environment, a private cloud infrastructure environment, and be prepared for public cloud scale and capabilities.
