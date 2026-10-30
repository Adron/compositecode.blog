---
title: I Can Talk About It Finally! => Tier 3 Web Fabric Platform as a Service (PaaS)
date: 2012-05-08 20:15:33 -0700
last_modified_at: 2012-05-08 20:15:33 -0700
permalink: /2012/05/08/i-can-talk-about-it-finally-tier-3-web-fabric-platform-as-a-service-paas/
slug: i-can-talk-about-it-finally-tier-3-web-fabric-platform-as-a-service-paas
wp_id: 5541
original_url: https://compositecode.blog/2012/05/08/i-can-talk-about-it-finally-tier-3-web-fabric-platform-as-a-service-paas/
categories:
- Cloud Foundry
- Cloud Speak
- Iron Foundry
- Platform (as a Service)
tags:
- iaas
- paas
- tier 3 web fabric
- tier3
- web fabric
excerpt: 'A couple months ago I shifted gears and started working for Tier 3 on a number of projects. I made this decision for a few reasons: 1. I’m a huge advocate of PaaS (Platform as a Service) technologies. I like what PaaS enables and what it eliminates. Matter of fact I’d say I’m a bull …'
---

[![](/images/adronhall.smugmug.com/Software/Software-Development/The-CloudFoundry-Story/i-JbNSqtG/0/S/Tier3LogoOnWhite-S.jpg)](http://www.tier3.com)A couple months ago I shifted gears and started working for [Tier 3](http://www.tier3.com) on a number of projects. I made this decision for a few reasons:

[![](/images/adronhall.smugmug.com/Software/Software-Development/The-CloudFoundry-Story/i-zM8zbZR/0/S/cloudfoundry-S.png)](http://www.cloudfoundry.org)**1.** I’m a huge advocate of PaaS (Platform as a Service) technologies. I like what PaaS enables and what it eliminates. Matter of fact I’d say I’m a bull on the technology. I like to learn about, create and build the architectures within platforms. I also love the rather complex back end problems that come up when building a truly powerful, scalable, high end, highly available PaaS. You say, “*Adron, Tier 3 doesn’t have any PaaS stuff, it’s an IaaS Provider, this doesn’t explain anything?*” Aha! Read on (unless of course you’ve caught the news today… then you already know the answer)

![](/images/adronhall.smugmug.com/Software/Software-Development/The-CloudFoundry-Story/i-DfwBtVq/0/O/IronFoundry.png)**2.** I’m a polyglot dev. .NET kind of burned me out a few years back and I dedicated to learning as many other frameworks, languages, and tech stacks that I could. I’ve never been happier with the variety these days. I’ll admit though I still love to use all those years of experience I have with .NET. Indeed, I have a little soft spot in my heart for C#. Tier 3, along with the Iron Foundry Project, has given me the opportunity to work across languages and stacks including Node.js, Ruby, Objective-C and more.

![](/images/adronhall.smugmug.com/Software/Software-Development/The-CloudFoundry-Story/i-xRK3QGV/0/O/1336450737WebCoding.png)**3.** I like to build things, advocate for those things and what they can do for you, for dev teams, and in the end what we developers can build with them. Sometimes this might mean I do it myself, sometimes it means coordinating and leading a team (or as I often say of leads, “*serving*” the team). Right now I’m getting to do a little bit of both and it is indeed fun and really exciting! This brings me to the answer.

**The Answer:**  *[Tier 3](http://www.tier3.com) now has one of the, if not the most advanced [PaaS Environment available today](http://www.tier3.com/blog/web-data-fabric).*  Yeah, you can quote me on that. I’m not saying it because I work at [Tier 3](http://www.tier3.com), I’m saying it because I decided to come work at [Tier 3](http://www.tier3.com) to help build it. Those of you that know me, know why and where I do things. I have intent behind these decisions.  😉

The Tier 3 PaaS environment officially has more support for frameworks than any other PaaS Provider out there today. Congratulations to the team for getting this out the door! Needless to say, ***I’m proud to be a part of this team of bad ass devs! Cheers!***

## What is the Tier 3 Web Fabric?

Here’s a short tour I put together…

#

What exactly makes up a Web Fabric? We’ve taken Coud Foundry as a core, adding Iron Foundry for full support of all major Enterprise Frameworks and added a fabric over these services to provide an automated seem-less creation of a complete PaaS Environment.

*How would you use a PaaS like this?*

In an enterprise software and application development shop there is often a break out between development, testing, maybe a UAT (User Acceptance Testing) and finally production. One way to utilize such capabilities is to built a Web Fabric for each of these environments. Once each environment is built, these can then be scaled up or down as needed. Once the environment is done simply delete it. For an environment like UAT or Test, this is one of the most ideal situations to create an environment from scratch, ensuring that outliers don’t affect the testing criteria. How do you build a Tier 3 Web Fabric PaaS? This is the fun part. This process involves a little information and a few clicks, which then will build an entire PaaS environment.

**Step 1:** In the Tier 3 Control Panel click on the tab titled “*Fabrics*“. Inside that view, click on “*Create Web Fabric*“.

![Tier 3 Control Panel](/images/adronhall.smugmug.com/Software/Software-Development/Tier-3-Fabric/i-3rfJMbd/0/S/Screen-Shot-2012-05-08-at-S.png "Tier 3 Control Panel")

*Tier 3 Control Panel*

**Step 2:** Fill out the information requested on the screen. The user that you’re creating will be your Tier 3 Web Fabric Administrator. The name becomes part of your URI to access the PaaS API from, and the friendly name below that displays as a description in the control panel. The last piece of information is public or private, the private option limiting access to only VPN users of your Tier 3 Account.

![Creating a New Web Fabric](/images/adronhall.smugmug.com/Software/Software-Development/Tier-3-Fabric/i-9Qz8r9K/0/S/Screen-Shot-2012-05-08-at-S.png "Creating a New Web Fabric")

*Creating a New Web Fabric*

**Step 3:** Now give it some time. Remember this is not merely a simple virtualized instance of an operating system. What is now happening is a [Cloud Foundry](http://www.cloudfoundry.org) environment is being built, Iron Foundry is also added & other enhancements are being applied and built. This then creates an entire Tier 3 Web Fabric that can be used with any of the following tools, languages, and databases.

***A few of the languages and frameworks…***

- Ruby on Rails or Sinatra
- ASP.NET w/ whichever .NET Language, it could be C#, VB.NET, or [.NET COBOL](http://www.netcobol.com/cobol-compiler-for-net/) if you so felt inclined to build a web application with it.
- Java w/ Spring and other options.
- Node.js Nuff’ Said
- Python

***Of course the database services too…***

- MongoDB
- MS SQL Server
- vmWare PostGreSQL
- Redis

These are just a few that are and will be supported in the coming days. The [Cloud Foundry](http://www.cloudfoundry.org) base provides a massively powerful core to build off of and extend services and frameworks.

***For pushing applications to the Tier 3 Web Fabric, here are some tools to help with that…***

[**vmc-IronFoundry**](http://rubygems.org/gems/vmc-IronFoundry) :: This is the same thing as the vmc CLI that is part of the Cloud Foundry Project except that it adds support for .NET pushes from the command line too.

[**vmc**](http://rubygems.org/gems/vmc) :: this is the default way used by most people working with Cloud Foundry based PaaS Environments.

**[Eclipse & STS for Java](http://docs.cloudfoundry.com/tools/STS/configuring-STS.html)** :: this is the extension that integrates into Eclipse.

[**Cloud Foundry Explorer**](http://www.ironfoundry.org/download) :: this can be used to view and push .NET applications to the Tier 3 Web Fabric (or any Iron Foundry enabled Cloud Foundry Environment)

## Open Source Software, Iron Foundry and More…

In the coming days, weeks, and months I’ll be working with the team here at Tier 3 to drive more capabilities and features. In addition I’ll also be driving the Iron Foundry Open Source effort, pushing to extend what we’ve provided already with the .NET support extension on Cloud Foundry and also more. We here at Tier 3 love the open source community, and we love being part of the community. So with this announcement I wanted to add a big, huge, awesome ***THANKS*** to everyone out there passionately involved in and building software that is open source. You all ***ROCK***!

Stay tuned, this is merely the beginning.
