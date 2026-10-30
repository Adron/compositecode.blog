---
title: Linux Containers, LXC, FreeBSD Jails, VServer…
date: 2013-11-18 02:23:56 -0800
last_modified_at: 2014-01-23 17:40:49 -0800
permalink: /2013/11/18/linux-containers-windows-containers-lxc-freebsd-jails-vserver/
slug: linux-containers-windows-containers-lxc-freebsd-jails-vserver
wp_id: 9146
original_url: https://compositecode.blog/2013/11/18/linux-containers-windows-containers-lxc-freebsd-jails-vserver/
categories:
- Containers
tags:
- docker
- linux
- linux containers
- lxc
excerpt: These days containerization of work, applications and storage on systems has become a hot topic. Not to say it wasn’t before, but it’s got a boost from the cloud computing segment of the industry. With that I felt the need to write up what I’ve discovered of the history in this industry so far. I’d …
image: /wp-content/uploads/2013/11/lxc.png
---

These days containerization of work, applications and storage on systems has become a hot topic. Not to say it wasn’t before, but it’s got a boost from the cloud computing segment of the industry. With that I felt the need to write up what I’ve discovered of the history in this industry so far. I’d love feedback and corrections if I’ve got anything out of order here or if – heaven forbid – I’ve got something wrong.

## What are Containers?

Before I get into what a container is, it is best to define what [operating system-level virtualization](http://en.wikipedia.org/wiki/Operating_system-level_virtualization) is. Sometimes this is referred to as jailed services or apps running in a jail.

This level of virtualization often provides extremely similar functionality as a VMware, Virtual Box or Hyper-V virtual server would provide. The difference however is primarily around the idea that the operating system-level virtualization actually runs as a service, usually protected, that runs apps as if it were an operating system itself.

So what’s a container?

> Linux Contains is a feature that allows Linux to run a single or more isolated virtual systems that each have their own network interfaces, computer process threads and namespaces, user namespaces and states.

![](https://photos.adron.me/Software/Software-Development/Docker-Virtual-Machines/i-gntfzfB/0/S/lxc-S.png)One of the common abbreviations for Linux Containers you’ll see is LxC. There are however many distinct operating system-level virtualization solutions.

- [**Open VZ**](http://en.wikipedia.org/wiki/OpenVZ) – this technology uses a single patched Linux kernel, providing the ability to use the architecture and kernel version of the system that is executing the container.
- [**Linux V-Server**](http://en.wikipedia.org/wiki/Linux-VServer) – this technology is a virtual private server implementation that was created by adding operating system-level virtualization to the Linux kerne. The project was started by Jacques Gélinas. It is now maintained by Herbert Pötzl of Austria and is not related to the Linux Virtual Server project. The server breaks things into partitions called security contexts, within that is the virtual private server.
- **[![](https://photos.adron.me/Software/Software-Development/Docker-Virtual-Machines/i-sj97cvz/0/S/freebsd-jail-S.jpg)FreeBSD Jail](http://en.wikipedia.org/wiki/FreeBSD_jail)** – This container technology breaks apps and services into jails.
- [**Workload Partitions**](http://en.wikipedia.org/wiki/Workload_Partitions) – This is a technology built for AIX, introduced in AIX 6.1. Workload Partitions breaks things into WPARs. These are software partitions that are created from the resources of a single AIX OS instance. WPARs can be created on any **[system p](http://en.wikipedia.org/wiki/System_p)**(the new old thing, was the RS/6000 tech) hardware that supports AIX 6.1 or higher versions. There are two kinds of WPARs, System WPARs and Application WPARs.
- **[![](https://photos.adron.me/Software/Software-Development/Docker-Virtual-Machines/i-Xgn8g64/0/S/sol10logo-S.png)Solaris Containers](http://en.wikipedia.org/wiki/Solaris_Containers)** – is a container tech for x86 and SPARC systems. It was first released in February 04′ for Solaris 10. It is also available in OpenSolaris, SmartOS and others as well os Oracle Solaris 11. The Solaris container combines resource controls in seperations referred to as zones. These zones act as completely isolated virtual servers within a OS.

## What is so great about a container?

Ok, so I’ve covered what a container is. You’re probably asking, “*so what do I do with these containers?*” There are a number of things, for starters speed is a huge advantage with containers. You can spool up entire functional application or service systems, like an API facade or something, in seconds. Often times a container will spool up and be ready in less than a second. This provides a huge amount of power to build out flexible, resilient, self-healing distributed systems that otherwise are just impossible to build with slow loading traditional virtual machine technology.

*Soft memory* is another capability that most containers have. This is the capability of being allocated, or being allocated and running, in memory. As one may already know, if you run something purely out of memory it is extremely fast, often 2-10x faster than running something that has to swap on a physical drive.

*Managing* crashing services or damaged ecosystem elements. If the containers are running, but one gets hit with an overloaded compute ask, software crashes on it, or one of the many receive some type of blocking state like a DDOS of sorts, just reboot it. Another option is just to kill it and spool up and entirely new instance of the app or service in a container. This ability really is amplified in any cloud environment like AWS where a server instance may crash with some containers on it, but having another instance running with multiple containers on it is easy, and restarting those containers on running instances is easy and extremely fast.

*Security* is another element that can be assisted with container technology. As I alluded to in the previous point above, if a container gets taken over or otherwise compromised, it’s very easy to just kill it and resume one that is not compromised. Often buying more time to resolve the security concern. Also, by having each container secured against each other container, controlling a container does not result in a compromised physical machine and operating system. This is a huge saving grace when security is breached.

## Container Summary

Containers are a hot ticket topic, for good reason. They provide increase management of apps and services, can utilize soft memory, increase security and they’re *blazing fast*. The technology, albeit having been around for a good decade, is starting to grow in new ways. Containers are starting to also become a mainstay of cloud technology, almost a requirement for effective management of distributed environments.

*Next up*, I’ll hit on Docker tech from DotCloud and Salomon Hykes [@solomonstre](https://twitter.com/solomonstre).

For now, anybody got some additions or corrections for this short history and definitions of containers?  🙂
