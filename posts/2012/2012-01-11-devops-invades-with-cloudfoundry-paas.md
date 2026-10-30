---
title: Devops Invades with PaaS & CloudFoundry
date: 2012-01-11 12:40:14 -0800
last_modified_at: 2012-01-12 23:22:07 -0800
permalink: /2012/01/11/devops-invades-with-cloudfoundry-paas/
slug: devops-invades-with-cloudfoundry-paas
wp_id: 4748
original_url: https://compositecode.blog/2012/01/11/devops-invades-with-cloudfoundry-paas/
categories:
- .NET Bits
- Architecture
- Cloud Speak
- My Updates
- Platform (as a Service)
tags:
- appfog
- cloudfoundry
- ironfoundry
- new relic
- paas
- tier 3
- tier3
excerpt: 'I have jumped head first into CloudFoundry over the last few weeks. In doing so I’ve started working with AppFog, IronFoundry, VMware and other devops tools. There are several avenues I’m taking to get more familiar with CloudFoundry based PaaS technology. Here’s a short review: Writing I started writing a series which is being published by New Relic around “Removing the Operating System Barrier with Platform as a Service”. Part 1 is live NOW – so go give it a read! 🙂 Working Currently I’ve been working up some Enterprise Prototypes using the IronFoundry Technology. The idea is to provide a seamless deployment option for Enterprises that may have a very mixed environment of public and private computing options, virtual and non-virtualized environments, and any array of other capabilities. I’ve also been toying around with Windows 2008 Server Core, which I’ll have more about shortly. …click through for more…'
---

I have jumped head first into [CloudFoundry](http://www.cloudfoundry.org) over the last few weeks. In doing so I’ve started working with [AppFog](http://www.appfog.com), [IronFoundry](http://www.ironfoundry.org/), [VMware](http://www.vmware.com/products/fusion/overview.html) and other devops tools.  There are several avenues I’m taking to get more familiar with CloudFoundry based PaaS technology. Here’s a short review:

## Writing

I started writing a series which is being published by [New Relic](http://newrelic.com/) around “***[Removing the Operating System Barrier with Platform as a Service](http://blog.newrelic.com/2012/01/11/removing-the-operating-system-barrier-with-platform-as-a-service-paas-a-guest-post-from-adron-hall/)***“.  [Part 1](http://#) is live NOW – so go give it a read!  🙂

## Working

Currently I’ve been working up some Enterprise Prototypes using the [IronFoundry](http://www.ironfoundry.org/) Technology. The idea is to provide a seamless deployment option for Enterprises that may have a very mixed environment of public and private computing options, virtual and non-virtualized environments, and any array of other capabilities. I’ve also been toying around with Windows 2008 Server Core, which I’ll have more about shortly.

**Public Cloud [AppFog](http://www.appfog.com)**

[AppFog](http://www.appfog.com) provides a public facing PaaS supporting PHP, Ruby on Rails, Java, MongoDB and a lot of other packages. They’re currently in beta right now, which I was fortunate enough to snag access to, but I’m sure the covers will come off soon enough! The underlying technology is built on CloudFoundry, providing a robust, scalable, and capable infrastructure connection to provide PaaS on.

In addition to AppFog there is the CloudFoundry.com offering, which I’ve tested out a little bit, but mostly focused on AppFog and on building out…

**Private Cloud Capabilities w/ Public Cloud Style Infrastructure**

I’ve built out some images to test out how CloudFoundry and IronFoundry works. I did pull down the provided virtual machines but I’m also building out my own to understand it better. The Ruby + C# that I’ve seen from the VMware crew & Tier 3 team has been great so far (I always dig reading some solid code).

- [Github CloudFoundry Code](https://github.com/cloudfoundry)
- [Github IronFoundry Code](https://github.com/IronFoundry) fork for .NET

That’s it for this short review, more to come, and let me know what you think of my entry “[Removing the Operating System Barrier with Platform as a Service](http://bit.ly/yOHu8M)” over on [New Relic’s Blog](http://blog.newrelic.com/).
