---
title: 'Cloud Throw Down:  Part 1 – Operating Systems & Languages'
date: 2010-11-01 00:07:09 -0700
last_modified_at: 2010-11-09 10:55:55 -0800
permalink: /2010/11/01/cloudthrowdown-part1/
slug: cloudthrowdown-part1
wp_id: 1515
original_url: https://compositecode.blog/2010/11/01/cloudthrowdown-part1/
categories:
- AWS
- Azure
- Tech Throw-down
tags:
- amazon web services
- aws
- azure
- cloud
- cloud computing
- ec2
- virtual
- web role
- windows azure
excerpt: The clouds available from Amazon Web Services, Windows Azure, Rackspace and others have a few things in common. They’re all providing storage, APIs, and other bits around the premise of the cloud. They all also run on virtualized operating systems. This blog entry I’m going to focus on some key features and considerations I’ve run into over the last year or so working with these two cloud stacks. I’ll discuss a specific feature and then will rate it declaring a winner.
---

|  |  |
| --- | --- |
| [Amazon Web Services](http://aws.amazon.com)  *Amazon Web Services* | [Windows Azure](http://www.microsoft.com/windowsazure)  *Windows Azure* |

The clouds available from [Amazon Web Services](http://aws.amazon.com), [Windows Azure](http://www.microsoft.com/windowsazure), Rackspace and others have a few things in common.  They’re all providing storage, APIs, and other bits around the premise of the cloud.  They all also run on virtualized operating systems.  This blog entry I’m going to focus on some key features and considerations I’ve run into over the last year or so working with these two cloud stacks.  I’ll discuss a specific feature and then will rate it declaring a winner.

**Operating System Options**

AWS runs on their AMI OS images, running Linux, Windows, or whatever you may want.  They allow you to execute these images via the EC2 instance feature of the AWS cloud.

Windows Azure runs on Hyper-V with Windows 2008.  Their VM runs Windows 2008.  Windows Azure allows you to run roles which execute .NET code or Java, PHP, or other languages, and allow you to boot up a Windows 2008 OS image on a VM and run whatever that OS might run.

***Rating & Winner: Operating Systems Options** goes to Amazon Web Services*

**Development Languages Supported**

AWS has a .NET, PHP, Ruby on Rails, and other SDK options.  Windows Azure also has .NET, PHP, Ruby on Rails, and other SDK options.  AWS provides 1st class citizen support and development around any of the languages, Windows Azure does not but is changing that for Java.  Overall both platforms support what 99% of developers build applications with, however Windows Azure does have a few limitations on non .NET languages.

***Rating & Winner: Development Languages Supported** is a tie.  AWS & Windows Azure both have support for almost any language you want to use.*

**Operating System Deployment Time**

AWS can deploy one of hundreds of any operating system image with a few clicks within the administration console.  Linux instances take about a minute or two to startup, with Windows instances taking somewhere between 8-30 minutes to startup.  Windows Azure boots up a web, service, or CGI role in about 8-15 minutes.  The Windows Azure VM Role reportedly boots up in about the same amount of time that AWS takes to boot a Windows OS image.

The reality of the matter is that both clouds provide similar boot up times, but the dependent factor is which operating system you are using.  If you’re using Linux you’ll get a boot up time that is almost 10x faster than a Windows boot up time.  Windows Azure doesn’t have Linux so they don’t gain any benefit from this operating system.  So really, even though I’m rating the cloud, this is really a rating about which operating system is faster to boot.

***Rating & Winner: Operating System Deployment Time** goes to AWS.*

[![Amazon Web Services](/images/adronhall.smugmug.com/Software/Software-Development/Technology-Company-Logos/logoaws/1070205742_R9ydp-O.gif "Amazon Web Services")](http://aws.amazon.com)

*Amazon Web Services*

***Today’s winner is hands down AWS.*** Windows Azure, being limited to Windows OS at the core, has some distinct and problematic disadvantages with bootup & operating system support options.  However I must say that both platforms offer excellent language support for development.

To check out more about either cloud service navigate over to:

- [Amazon Web Services](http://aws.amazon.com) or
- [Windows Azure](http://www.microsoft.com/windowsazure)

That’s the competitions for today.  I’ll have another throw down tomorrow when the tide may turn against AWS – so stay tuned!  🙂
