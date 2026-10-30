---
title: Learning About Docker
date: 2013-11-20 00:01:21 -0800
last_modified_at: 2013-11-20 08:44:03 -0800
permalink: /2013/11/20/learning-about-docker/
slug: learning-about-docker
wp_id: 9144
original_url: https://compositecode.blog/2013/11/20/learning-about-docker/
categories:
- Architecture
- Containers
- How-to
tags:
- container
- containers
- docker
- history
- linux
- lxc
- paas
- platform as a service
excerpt: Over the next dozen or so few days I’ll be ramping up on Docker, where my gaps are and where the project itself is going. I’ve been using it on and off and will have more technical content, but today I wanted to write a short piece about what, where, who and how Docker came …
---

Over the next dozen or so few days I’ll be ramping up on [Docker](http://docker.io), where my gaps are and where the project itself is going. I’ve been using it on and off and will have more technical content, but today I wanted to write a short piece about what, where, who and how Docker came to be.

As an open source engine Docker automates deployment of lightweight, portable, resilient and self-sufficient containers that run primarily on Linux. Docker containers are used to contain a payload, encapsulate that and consistently run it on a server.

This server can be virtual, on AWS or OpenStack, in clusters, public instances or private, bare-metal servers or wherever one can get an operating system to run. I’d bet it would show up on an Arduino cluster one of these days.  😉

User cases for Docker include taking packaging and deployment of applications and automating it into a simple container bundle. Another is to build PaaS style environments, lightweight that scale up and down extremely fast. Automate testing and continuous integration and deployment, because we all want that. Another big use case is simply building resilient, scalable applications that then can be deployed to Docker containers and scaled up and down rapidly.

## A Little History

The creators of Docker formed a company called dotCloud that provided PaaS Services. On October 29th, 2013 however they changed the name from dotCloud to Docker Inc to emphasize the focus change from the dotCloud PaaS Technology to the core of dotCloud, Docker itself. As Docker became the core of a vibrant ecosystem the founders of dotCloud chose to focus on this exciting new technology to help guide and deliver on an ever more robust core.

[![Docker Ecosystem from the Docker Blog. Hope they don't mind I linked it, it shows the solid lifecycle of the ecosystem. (Click to go view the blog entry that was posted with the image)](https://photos.adron.me/Software/Software-Development/Docker-Virtual-Machines/i-BhpSw9R/0/M/ecosystem2-M.jpg)](http://blog.docker.io/2013/10/dotcloud-is-becoming-docker-inc/)

*Docker Ecosystem from the Docker Blog. Hope they don’t mind I linked it, it shows the solid lifecycle of the ecosystem. (Click to go view the blog entry that was posted with the image)*

The community of docker has been super active with a dramatic number of contributors, well over 220 now, most who don’t work for Docker and they’ve made a significant percentage of the commits to the code base. As far as the repo goes, it has been downloaded over a 100,000 times, yup, over a hundred. thousand. times!!! It’s container tech, I’m still impressed just by this fact! On [Github the repo](https://github.com/dotcloud/docker) has thousands of starred observers and over 15,000 people are using Docker. One other interesting fact is the slice of languages, with a very prominent usage of Go.

![Docker Language Breakout on Github](https://photos.adron.me/Software/Software-Development/Docker-Virtual-Machines/i-f3NRmLC/0/O/dotcloud_docker.png)

*Docker Language Breakout on Github*

Overall the Docker project has exploded in popularity, which I haven’t seen since Node.js set the coder world on fire! It’s continuing to gain steam in how and in which ways people deploy and manage their applications – arguably more effectively in many ways.

[![Portland Docker Meetup. Click image for link to the meetup page.](https://photos.adron.me/Software/Meetups-N-Conferences/Portland-Docker/i-h5Z9b3Z/0/S/Docker-Portland-Banner-S.png "Portland Docker Meetup. Click image for link to the meetup page.")](http://www.meetup.com/Docker-Portland-OR/)

*Portland Docker Meetup. Click image for link to the meetup page.*

The community is growing accordingly too, not just a simple push by Docker/dotCloud itself, but actively by grass roots efforts. One is even sprung up in Portland in the Portland Docker Meetup.

## So Docker, Getting Operational

![The Loading Bay](https://photos.adron.me/Software/Software-Development/Docker-Virtual-Machines/i-WpGSzNM/0/S/lgslings-S.jpg)

*The Loading Bay*

One of the best ways to describe docker (*which the Docker team often uses, hat tip to the analogy!*) and containers in general is to use a physical parallel. One of the best stories that is a great example is that of the shipping and freight industry. Before containers ships, trains,

![Manually Guiding Freight, To Hand Unload Later.](https://photos.adron.me/Software/Software-Development/Docker-Virtual-Machines/i-hGpZnjj/0/Th/history-img5-Th.jpg)

*Manually Guiding Freight, To Hand Unload Later.*

trucks and buggies (ya know, that horses pulled) all were loaded by hand. There wasn’t any standardization around movement of goods except for a few, often frustrating tools like wooden barrels for liquids, bags for grains and other assorted things. They didn’t mix well and often were stored in a way that caused regular damage to good. This era is a good parallel to hosting applications on full hypervisor virtual machines or physical machines with one operating system. The operating system kind of being the holding bay or ship, with all the freight crammed inside haphazardly.

![Shipping Yards, All of a Sudden Organized!](https://photos.adron.me/Software/Software-Development/Docker-Virtual-Machines/i-W8DtrdM/0/Th/history-img2-Th.png)

*Shipping Yards, All of a Sudden Organized!*

When containers were introduced like the shiny blue one shown here, everything began a revolutionary change. The manpower dramatically

![A Flawlessly Rendered Container](https://photos.adron.me/Software/Software-Development/Docker-Virtual-Machines/i-jT3FfMR/0/S/photodune-1719153-container-l-S.jpg)

*A Flawlessly Rendered Container*

dropped, injuries dropped, shipping became more modular and easy to fit the containers together. To put it simply, shipping was revolutionized through this invention. In the meantime we’ve all benefitted in some way from this change. This can be paralleled to the change in container technology shifting the way we deploy and host applications.

***Next post, coming up in just a few hours “Docker, Containers Simplified!”***
