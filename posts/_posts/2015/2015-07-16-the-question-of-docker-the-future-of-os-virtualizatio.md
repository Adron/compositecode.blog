---
title: The Question of Docker, The Future of OS Virtualization
date: 2015-07-16 22:07:22 -0700
last_modified_at: 2015-07-22 15:31:16 -0700
permalink: /2015/07/16/the-question-of-docker-the-future-of-os-virtualizatio/
slug: the-question-of-docker-the-future-of-os-virtualizatio
wp_id: 11380
original_url: https://compositecode.blog/2015/07/16/the-question-of-docker-the-future-of-os-virtualizatio/
categories:
- Architecture
- Containers
tags:
- analysis
- docker
- os level virtualization
- virtualization
excerpt: In this article I’m going to take a look at Docker and OS Virtualization autonomously of each other. There’s a reason, which will unfold as I dig through some data and provide this look into what is and isn’t happening in the virtualization space. It’s important to also note what methods were used to attain …
image: /wp-content/uploads/2015/07/docker-delete.png
---

In this article I’m going to take a look at Docker and OS Virtualization autonomously of each other. There’s a reason, which will unfold as I dig through some data and provide this look into what is and isn’t happening in the virtualization space.

It’s important to also note what methods were used to attain the information provided in this article. I have obtained information through speaking with Docker employees and key executives including Ben Golub and founder Solomon Hykes over the years since the founding of Docker (and it’s previous incarnation dotCloud, before the pivot and name change to Docker).

Beyond communicating directly with the Docker team and gaining insight from them I have also done a number of interviews over the course of 4 days. These interviews have followed a fairly standard set of questions and conversation about the Docker technology, including but not limited to the following questions.

- What is your current use of Docker visualization technologies?
- What is your future intended use of Docker technologies?
- What is the general current configuration and setup of your development team(s) and tooling that they use (i.e. stack: .NET, java, python, node.js, etc)
- Do you find it helps you to move forward faster than without?

## **The History of OS-Level Virtualization**

First, let’s take a look at where virtualization has been, then I’ll dive into where it is now, and then I’ll take a look at where it appears to be going in the future and derive some information from the interviews and discussions that I’ve had with various teams over the last 4 days.

**The Short of It**

OS-level virtualization is a virtualization application that allows the installation of software in a complete file system, just like a hypervisor based virtualization server, but dramatically faster installation and prospectively speed overall by using the host OS for OS-level virtualization. This cuts down on excess redundancies
within the core system and the respective virtual clients on the host.

Virtualization in concept has been around since the 1960s, with IBM being heavily involved at the Cambridge Scientific Center. Over time developments continued, but the real breakthrough in pushing virtualization into the market was VMware in 1999 with their virtual platform. This, hypervisor level virtualization great into a huge industry with the help of VMware.

However OS-level virtualization, which is what Docker is based on, didn’t take off immediately when introduced. There were many product options that came out over time around OS-level virtualization, but nothing made a huge splash in the industry similar to what Docker has. Fast forward to today and Docker was released in 2013 to an ever increasing developer demand and usage.

> [Timeline of Virtualization Development](https://en.wikipedia.org/wiki/Timeline_of_virtualization_development)

Docker really brought OS-level virtualization to the developer community at the right time in regards to demands around web development and new ways to implement effective continuous delivery of applications. Docker has been one of the most extensively used OS-level virtualization tools to implement immutable infrastructure, continuous build, integration, and deployment environments, and to use as a general virtual environment to spool up resources as needed for development.

## **Where we Are With Virtualization**

Currently Docker holds a pretty dominant position in the OS-level virtualization market space. Let’s take a quick review of their community statistics and involvement from just a few days ago.

*The Stats: Docker on Github ->*<https://github.com/docker/docker>

Watchers: 2017
Starred: 22941
Forks: 5617

16,472 Commits
3 Branches
102 Releases
983 Contributors

Just from that data we can ascertain that the Docker Community is active. We can also take a deep look into the forks and determine pull requests, acceptance of and related data to find out that the overall codebase is healthy with involvement. This is good to know since at one point there were questions if Docker had the capability to manage the open source legions pushing the product forward while maintaining the integrity, reputation, and quality of the product.

Now let’s take a look at what that position is based on considering the interviews I’ve had in the last 4 days. Out of the 17 people I spoke with all knew what Docker is. That’s a great position to be in compared to just a few years ago.

Out of the 17 people I spoke with, 15 of the individuals are working on teams that have, are implementing or are in some state between having and implementing Docker into their respective environments.

Of the 17, only 13 said they were concerned in some significant way about Docker Security. All of these individuals were working on teams attempting to figure out a way to use Docker in a production way, instead of only in development or related uses.

The list of uses that the 17 want to use or are using Docker for vary as much as the individual work that each is currently working on. There are however some core similarities in what they’re working on where Docker comes into play.

The most common similarity among Docker uses is simply as a platform to build out development testing environments or test servers. This is routinely a database server or simple distributed database like Cassandra or Riak, that can be built immutably, then destroyed and recreated whenever it is needed again for test and development. Some of the build outs are done with Docker specifically to work up a mock distributed database environment for testing. Mind you, I’m probably hearing about and seeing this because of my past work with Basho and other distributed systems programmers, companies, and efforts around this type of technology. It’s still interesting and very telling none the less.

The second most common usage is for Docker to be used somewhere in the continuous delivery chain. The push to move the continuous integration and delivery process to a more immutable, repeatable, and reliable process has been a perfect marriage between Docker and these needs. The ability to spin up entire environments in a matter of seconds and destroy them on whim, creating them again a matter of moments later, as made continuous delivery more powerful and more possible than it has ever been.

Some of the less common, yet still key uses of Docker, that came up during the interviews included; in memory cache servers, network virtualization, and distributed systems.

## Virtualization’s**Future**

**Pathing**

With the history covered, the core uses of Docker discussed, let’s put those on the table with the acquisitions. The acquisitions by Docker have provided some insight into the future direction of the company. The acquisitions so far include: Kitematic, SocketPlane, Koality, and Orchard.

From a high level strategic play, the path Docker is pushing forward into is a future of continued virtualization around, as the hipsters might say “all the things”. With their purchase of Kitematic and SocketPlane. Both of these will help Docker expand past only OS virtualization and push more toward systemic virtualization of network environments with programmatic capabilities and more. These are capabilities that are needed to move past the legacy IT environments of yesteryear which will open up more enterprise possibilities too.

To further their core use that exists today, Docker has purchased Koality. Koality provides parallelizable continuous integration, deployment, and related services. This enables Docker to provide more built out services around this very important.

The other acquisition was Orchard (orchardup.com). This is a startup that provides a Docker host in the cloud, instantly. This is a similar purchase as the Koality one. It bulks up capabilities that Docker had some level of already. It also pushes them forward with two branches of capabilities: SaaS based on the web and prospectively offering something behind the firewall, which the Koality acquisition might have some part to play also.

**Threat Vectors**

Even though the pathways toward the future seem clear for Docker in many ways, in other ways they see dramatically less clear. For one, there are a number of competitive options that are in play now, gaining momentum and on the horizon. One big threat is Google’s lack of interest in Docker has led them to build competing tooling. If they push hard into the OS level virtualization space they could become a substantial threat.

The other threat vector, is the simple unknown of what could become a threat. Something like Mesos might explode in popularity and determine it doesn’t want to use Docker, and focus on another virtualization path. In the same sense, Mesos could commoditize Docker to a point that the value add at that level of virtualization doesn’t retain a business market value that would sustain Docker.

The invisible threat around this area right now is fairly large. There’s no greater way to determine this then to just get into a conversation with some developers about Docker. In one sense they love what it allows them to do, but the laundry list of things they’d like would allow for a disruptor to come in and steal the Docker thunder pretty easily. To put it simply, there isn’t a magical allegiance to Docker, developers will pick what helps them move the ball forward the fastest and easiest.

Another prospective threat is a massive purchase by a legacy software company like Oracle, Microsoft, or someone else. This could effectively destabilize the OSS aspects of the product and slow down development and progress, yet it could increase corporate adoption many times over what it is now. So this possibility is something that shouldn’t be ruled out.

### Summary

Docker has two major threats: the direct competitor and their prospectively being leapfrogged by another level of virtualization. The other prospective threat to part of the company is acquisition of Docker itself, while it could mean a huge increase in enterprise penetration. In the future path the company and technology is moving forward in, there will be continued growth in usage and capabilities. The growth will maintain in the leading technology startups and companies of this kind, while the mid-size and larger corporate environments will continue to adopt and deploy at a slower pace.

### **A Question for You**

I’ve put together what I’ve noticed, and I’d love to see things that you dear reader might notice about the Docker momentum machine. Do you see networking as a strength, other levels of virtualization, deployment of machines, integration or delivery, or some other part of this space as the way forward into the future. Let me know what your thoughts are on Twitter or whatever medium you feel like reaching out on. Of course, I’d also love to know if you think I’m wrong about anything I’ve written here.
