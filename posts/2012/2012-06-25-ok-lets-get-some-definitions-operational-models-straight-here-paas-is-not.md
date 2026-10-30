---
title: Ok, Let’s Get Some Definitions & Operational Models Straight Here! PaaS is NOT…
date: 2012-06-25 10:11:55 -0700
last_modified_at: 2012-06-25 10:11:55 -0700
permalink: /2012/06/25/ok-lets-get-some-definitions-operational-models-straight-here-paas-is-not/
slug: ok-lets-get-some-definitions-operational-models-straight-here-paas-is-not
wp_id: 5870
original_url: https://compositecode.blog/2012/06/25/ok-lets-get-some-definitions-operational-models-straight-here-paas-is-not/
categories:
- Cloud Speak
- Conferences
tags:
- cloud
- cloud computing
- cloud connect
- cloud foundry
- cloudfoundry
- open shift
- paas
- platform as a service
- red hat
- rhel
- ubuntu
excerpt: I just got signed up for Cloud Connect Chicago and started checking out some of the talks. One talk jumped out, being that it is about PaaS Technology. After reading it though I immediately felt the need to straighten out some things that looked misleading. Maybe the presenter (JP Morgenthal) will lay these things out …
---

I just got signed up for [Cloud Connect Chicago](http://www.cloudconnectevent.com/chicago/) and started checking out some of the talks. One talk jumped out, being that it is about PaaS Technology. After reading it though I immediately felt the need to straighten out some things that looked misleading. Maybe the presenter ([JP Morgenthal](https://twitter.com/#!/jpmorgenthal)) will lay these things out well for the attendees, but at this point I don’t know that. I’m making a point to see this session while I’m at Cloud Connect. I’m curious to see how he lays out the content. Here’s the description for the “[Navigating PasS: Your Road Map for Application Development](http://www.cloudconnectevent.com/chicago/cloud-computing-workshops/navigating-pass-your-road-map-for-application-development.php)“. Hopefully I’ll see you there!

> Platform-as-a-Service (PaaS) has most simply been described as the set of tools above the infrastructure (hypervisor) and contains the applications being served out of the cloud. However, this description covers a large body of resources. Navigating the use of PaaS for application development and delivery requires a very wide understanding of the computing environment and doesn’t fully relieve the user from understanding the infrastructure that is used to operate the PaaS.

## Hypervisor + PaaS, You’re Doing it Wrong

First off, the thing that really caught my attention about this session is that it sounds like someone from a very specific company trying to sell a very specific thing wrote this initial description. A PaaS, or Platform as a Service does NOT have to run on an infrastructure hypervisor. It has ZERO association to a hypervisor. All a PaaS should do, ought to be, and generally is regardless who it is made by or who is running it, is a set of software that automates deployment, application distribution to systems serving the application, and generally simplifies the deployment of an application and to some degree databases or data repositories. There is, and should NOT be, any type of coupling, especially any tight coupling, to some hypervisor.

In summary, a PaaS should have zero to do with a hypervisor. It should rely on a simple operating system that has minimal resource overhead and minimal requirements. Take Cloud Foundry or Open Shift. They rely on some of the most capable operating systems, Red Hat Linux (RHEL) and Ubunut LTE to run the PaaS Systems. These are by far some of the best choices in the industry to determine the core of where a PaaS should run. Based on this, it is an operating system, at the core that enables these systems. NOT a hypervisor. If you’re looking to base your PaaS System off of a hypervisor, I’m afraid you’ll have made a severe mistake right off the bat.

Now if you put your [Red Hat](http://www.redhat.com/) or [Ubuntu OS](http://www.ubuntu.com/) on a hypervisor, or straight on the metal, you’re fine. Just don’t cross the seperations of concern from the operating system to travel from PaaS to hypervisor. That’d just be…

***wrong.***

## What I Agree With, You Better Understand IaaS

One thing I agree with in the above description and I’m betting JP will put some emphasis on this part of the discussion, is that you absolutely need to have an understanding of your infrastructure that runs underneath your PaaS. There are a multitude of reasons to keep in mind what the infrastructure is doing underneath and how it handles what you’re deploying to your PaaS. Here’s two hugely important topics of concern when you deploy a PaaS into any environment.

- When an application deploys to multiple instances. What does that mean in your PaaS? Is it on several separate instances? Is it in different geographical areas? Does it go under a different load balancer? How is my database deployed? If you’ve deployed a NoSQL solution, that needs multiple nodes for data integrity, do you know how many nodes are deployed?
- If I deploy a site to my PaaS, how will it and can it talk to itself or outside via networking? Do I have loop back protection on for security? Will it disallow certain port traffic? What is happening to port traffic and traffic in general?

It looks like the session will cover a lot of these topics. So if you’re looking to attend, I highly suggest checking out JP’s session. I’ll be looking forward to his approach to many of the other topics (check out the site description) such as those I just mentioned along with security, deployment concerns, deploying a single language PaaS (like Apprenda, Cloudbees, etc) and other solutions. In addition to that, I’ll likely be bringing an arsenal of questions, see you all and JP at Cloud Connect!
