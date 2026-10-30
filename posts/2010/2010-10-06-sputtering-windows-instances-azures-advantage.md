---
title: Sputtering Windows Instances
date: 2010-10-06 05:10:59 -0700
last_modified_at: 2010-10-04 15:38:03 -0700
permalink: /2010/10/06/sputtering-windows-instances-azures-advantage/
slug: sputtering-windows-instances-azures-advantage
wp_id: 1331
original_url: https://compositecode.blog/2010/10/06/sputtering-windows-instances-azures-advantage/
categories:
- AWS
- Azure
- Cloud Speak
tags:
- amazon web services
- ami
- aws
- ec2
- esx
- hyper-v
- linux
- virtualization
- vmware
- windows
- windows azure
excerpt: I had a concern about Windows OS being used for cloud computing. The instances in Windows Azure take a significant amount of time to boot up. In Amazon Web Services the Windows EC2 Instances also take a long time to boot up. Compared to Linux, Windows takes 2-4x longer to spool up in the cloud. Before today, this just seemed like it might be a problem I was experiencing. I tend to believe I’m doing something wrong before I go on the warpath, but today that concern that I’d done something wrong has ended. RightScale posted a blog entry about the difficulties of Windows in EC2. They’re seeing the same issues I was.
---

I had a concern about Windows OS being used for cloud computing.  The instances in Windows Azure take a significant amount of time to boot up.  In Amazon Web Services the Windows EC2 Instances also take a long time to boot up.  Compared to Linux, Windows takes 2-4x longer to spool up in the cloud.  (Compare a boot time of about ~1 minute for Linux in EC2 vs 8-15 minutes for Windows)

Before today, this just seemed like it might be a problem I was experiencing.  I tend to believe I’m doing something wrong before I go on the warpath, but today that concern that I’d done something wrong has ended.  RightScale posted a blog entry about the [difficulties of Windows in EC2](http://blog.rightscale.com/2010/08/17/windows-in-the-cloud-with-rightscale).  They’re seeing the same issues I was.

Another issue that they noticed, which I too noticed, was the issues around the clocks being off.  This is a similar problem to Windows being used with VMWare and setting up images.  The clock just doesn’t ync the first time, or subsequent times.  Usually a few manual attempts need to be made.

In another entry I caught another [list of issues with Windows that Linux just doesn’t have](http://lordsithtech.net/?p=429).  None of these are work stoppage issues, but they are all very annoying and would push one toward using Linux instead if at all possible.

Putting Windows Azure and Amazon Web Services EC2 side by side [Network World has found them to be on a collision course](http://www.networkworld.com/news/2010/062510-microsoft-azure-amazon-ec2.html).

**Boiling it Down, Where Does Windows Stand?**

After some serious analysis by individuals of Windows running in Cloud Environments it appears that Windows just isn’t as suited to running in virtualized environments as Linux.  A number of friends have pointed out to me how much friendlier Linux is in virtualized spaces such as VMWare’s ESX Environment.

Also based on hard analysis of VMWare versus Hyper-V, the later doesn’t appear to be as sophisticated or capable of virtualized hosting.  Is this going to cause a price point issue for Windows Azure versus AWS EC2?  Just from the perspective of requiring more hardware for Hyper-V Virtualization versus VMWare & Amazon’s AMI Virtualization it makes me ponder if this could be a major competitive advantage for Linux based clouds.  Already there is the licensing price points, so how does MS own up to that?

I would be curious to see what others have experienced.  Have you seen virtualized differences that cause issues hosting Linux vs. Windows in VMWare, Hyper-V, or AWS?  Do you foresee any other problems that could become big problems?
