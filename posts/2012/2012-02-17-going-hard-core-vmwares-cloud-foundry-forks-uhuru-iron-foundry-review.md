---
title: 'Going Hard Core: Vmware’s Cloud Foundry Forks Uhuru & Iron Foundry Review'
date: 2012-02-17 16:24:49 -0800
last_modified_at: 2012-05-01 10:25:25 -0700
permalink: /2012/02/17/going-hard-core-vmwares-cloud-foundry-forks-uhuru-iron-foundry-review/
slug: going-hard-core-vmwares-cloud-foundry-forks-uhuru-iron-foundry-review
wp_id: 5081
original_url: https://compositecode.blog/2012/02/17/going-hard-core-vmwares-cloud-foundry-forks-uhuru-iron-foundry-review/
categories:
- .NET Bits
- Architecture
- Cloud Speak
- Infrastructure
- Platform (as a Service)
tags:
- .NET
- asp.net
- asp.net mvc
- cloud
- cloud computing
- cloudfoundry
- dotnet
- iron foundry
- mvc
- paas
- services
- uhuru software
- vcap
excerpt: 'Back in December Uhuru Software and Tier 3 released two different forks of Cloud Foundry that enabled .NET Support. I wasn’t sure which I wanted to use, since I had some serious Cloud Foundry work I was about to dive into, so I’ve picked them apart to determine how each works. This is what I’ve found so far. Uhuru Source Code Public Site: http://www.uhurusoftware.com/ Community / Support Site Community LinkedIn Site (Mostly “biz” oriented) What Uhuru Software is… Micro Cloud VM/Installers (requires registration) Iron Foundry Source Code Public Site: http://www.ironfoundry.org/ Community / Support Site Iron Foundry Blog VM Download (For Micro Cloud Foundry) That covers the basic links to the downloads, community, and other points of presence, now it is time to dig into some of the differences I’ve found. First though, I got a good environment setup to test each of the forks, from within the same Cloud Foundry Environment! So this is how I’ve set this up…'
---

Back in December Uhuru Software and Tier 3 released two different forks of Cloud Foundry that enabled .NET Support. I wasn’t sure which I wanted to use, since I had some serious Cloud Foundry work I was about to dive into, so I’ve picked them apart to determine how each works. This is what I’ve found so far.

**[![](/images/adronhall.smugmug.com/Software/Software-Development/The-CloudFoundry-Story/i-8Cv4dN4/0/O/UhuruSoftware.png)](http://www.uhurusoftware.com/)[Uhuru](http://www.uhurusoftware.com/)**

- [Source Code](https://github.com/UhuruSoftware)
- [Public Site: http://www.uhurusoftware.com/](http://www.uhurusoftware.com/)
- [Community / Support Site](https://uhurusoftware.zendesk.com/home)
- [Community LinkedIn Site](http://www.linkedin.com/groups?home=&gid=4206663) (Mostly “biz” oriented)
- [What Uhuru Software is…](http://www.uhurusoftware.com/pub/dotnetfaq.aspx)
- [Micro Cloud VM/Installers (requires registration)](http://www.uhurusoftware.com/microcloud.aspx)

**[![](/images/adronhall.smugmug.com/Software/Software-Development/The-CloudFoundry-Story/i-DfwBtVq/0/O/IronFoundry.png)](http://www.ironfoundry.org/)[Iron Foundry](http://www.ironfoundry.org/)**

- [Source Code](https://github.com/ironfoundry)
- [Public Site:  http://www.ironfoundry.org/](http://www.ironfoundry.org/)
- [Community / Support Site](http://help.ironfoundry.org/home)
- [Iron Foundry Blog](http://blog.ironfoundry.org/)
- [VM Download (For Micro Cloud Foundry)](http://www.ironfoundry.org/download)

That covers the basic links to the downloads, community, and other points of presence, now it is time to dig into some of the differences I’ve found. First though, I got a good environment setup to test each of the forks, from within the same Cloud Foundry Environment! So this is how I’ve set this up… [![](/images/adronhall.smugmug.com/Software/Software-Development/The-CloudFoundry-Story/i-dDM6JXV/0/S/Migration-580x580-S.jpg)](http://www.vmware.com/products/fusion/overview.html)Setting up the Virtual Machines w/ VMware Fusion I suspect, you could tangibly do this with some other virtualization software, but VMware is probably the easiest to use and setup on OS-X & Windows. I haven’t tried this on Linux so there’s another space I’d have to give it a go. Using ESX I also suspect this would also be extremely easy to setup. It’s up to you, but I’m doing all of this with VMware Fusion. The environment I’m using for this comparison consists of the following virtual images:

### Micro Cloud Foundry Instances

These instances were easy, I just downloaded them from the Cloud Foundry Site on the [Micro Cloud Foundry Download Page](https://my.cloudfoundry.com/micro/dns). The simple configuration is outlined in “[Micro Cloud Foundry Installation & Setup](http://support.cloudfoundry.com/entries/20316811-micro-cloud-foundry-installation-setup)“.

### Iron Foundry Instances

For this, I downloaded the available VM on the [Iron Foundry Site here](http://www.ironfoundry.org/download).

### Uhuru Instances

I setup the Uhuru Instances using the instructions available from [Uhuru Software here](http://www.uhurusoftware.com/media/6069/uhurupaasinstallguide.pdf).

### Setting up Some Controllers

So the first thing I did was dive into setting up a controller, or actually two, because I wanted to have an Iron Foundry Environment and a Uhuru Software Environment. After that I’d then try to mix and match them and figure out differences or conflicts. The instructions listed under the “[Uhuru Instances](http://www.uhurusoftware.com/media/6069/uhurupaasinstallguide.pdf)” has information regarding setup of a controller for the Uhuru Software Environment, which is what I followed. It is also a good idea to get setup with Putty or ready with SSH for usage of Cloud Foundry, Uhuru Software, and Iron Foundry.
