---
title: Riak is… A Whole Big List of Things
date: 2013-01-11 11:59:42 -0800
last_modified_at: 2013-01-17 08:03:49 -0800
permalink: /2013/01/11/riak-is-a-whole-big-list-of-things/
slug: riak-is-a-whole-big-list-of-things
wp_id: 7366
original_url: https://compositecode.blog/2013/01/11/riak-is-a-whole-big-list-of-things/
categories:
- Cloud Speak
- Distributed Things
- Riak
tags:
- basho
- distributed compute
- distributed computing
- distributed database
- distributed systems
- enterprise scale
- fault-tolerant
- high availability
- highly available
- horizontal scale
- horizontal scaling
- key value
- master-less
- multi-tenancy
- multi-tenant
- open source
- open source software
- oss
- riak
- scalable
- scale
- scaling
- single point of failure
- web scale
excerpt: 'What is Riak? Who builds it? Who maintains it? Can I download it? How does it work? What are the features? Here’s the start of answers to these questions and more. First, the basic high level description: “Riak is an open source, highly scalable, fault-tolerant distributed database.” That’s the first line you’ll read when checking …'
---

What is Riak? Who builds it? Who maintains it? Can I download it? How does it work? What are the features?

Here’s the start of answers to these questions and more.

##

First, the basic high level description:

*“[Riak](http://basho.com/products/riak-overview/) is an open source, highly scalable, fault-tolerant distributed database.”*

That’s the first line you’ll read when checking out the product via the Basho product link. It provides good information, but here I’m going to add more to the definition without the need to dig around yourself. Maybe I can save you some time & provide some links directly to solid information in the docs. Kind of a “[Cliff Notes](http://www.cliffsnotes.com/)” of Riak. Let’s take this feature by feature which will in turn get us to a definitive definition of what exactly Riak is.

### Riak is Open Source.

Riak is built and contributed to by the community, **with Basho being the steward and an active member that extends, builds and provides support for additional products**. The avenues to reach the Riak Open Source Community members is pretty straight forward, following known avenues of communication. Hit us up on the **[email list](http://lists.basho.com/mailman/listinfo/riak-users_lists.basho.com)**, especially feel free to contribute & ask questions via the **[Github Basho organization](https://github.com/basho/)**, there is the **[Basho Riak Blog](http://basho.com/blog/)**, the **[weekly recap](http://recap.basho.com/)** and jump into the IRC chat room **[#riak](http://irc.lc/freenode/riak/irctc@@@)** on [freenode](http://freenode.net/). Oh, and there’s a twitter feed **[@basho](https://twitter.com/basho)**.

So what exactly does this get you, when you become a user or contributor of Riak? The entire community is behind you, will help you get started using Riak and provide help whenever you run into problems. If you want SLAs or 24 hour support Basho can provide this for you. But for bugs, issues, queries, searching and all sorts of other related development questions there is the community. An open source community like this is passionate, which means you’ll have support like no closed source company will ever provide you, and absolutely no closed source product’s community will provide you. We’re talking about a different level of interest, passion and levels of personal involvement.

### Riak is a key value based database store.

Riak is a key value store. What exactly is a key value store? It’s pretty simple and you’re probably already familiar with what a key value store is. A key value is made up of two pieces of data, the first is the identifier for the second element within the data structure. This gives a system or developer using key value storage a schema-less way of working with data.

### Riak is designed for highly distributed environments.

This type of distributed isn’t the “we put one database over here and one database over here and you gotta figure out how they work together” type of distribution. So this isn’t some of that oddball pretend stuff Oracle keeps hoisting on people. This is the honest to goodness distribution of the sort, when one node goes down you don’t blink, you don’t stop eating dinner, you don’t sweat it. You just continue onward with life knowing full well that you’ll just spool up another node when you need to.

### Riak is master-less, with no single point of failure.

This is one of self explanatory features. But what does a master-less system provide us? One thing is no single point of failure. Being that all nodes can act autonomously to work around the loss of one or more nodes it also helps add to the high availability of the system.

### Riak is fault tolerant, like a disk drive you wish was real.

Ever have a backup disk drive? What? You don’t have one of those? Ugh. Ok, so imagine you had a backup disk drive that had an unfortunately high failure rate. Well, why, because you know, they have an oddly high failure rate. If you do backups like good practices dictate, eventually you’ll end up with some dead drives.

RAID, both software and hardware, are built specifically to deal with this type of failure. With a distributed system like Riak, it bumps the level of abstraction above software or hardware RAID, enabling another level of even greater fault tolerance. Not to remove the relevance of RAID capabilities, but with a multi-node system like Riak, you can easily remove nodes and swap them out as needed, keeping costs down by using simple drives in simple machines. If you want to, you could indeed get higher I/O machines and faster drives, but it isn’t necessary to insure fault tolerance in a Riak Database System.

### Riak scales, with hot swappable nodes enabling zero downtime.

The ability to commit hot swappable changes while in the midst of operating starts at a very low level for Riak. The language used to build Riak, Erlang has the ability to change pieces of an application system in realtime built into the precepts of the language. This provides, at the core, the inherent capability to change out systems, and by proxy of architectural design, the ability for nodes in Riak to be changed out simply by removing them from a cluster ring. Once that is done it is just as simple to add another node or nodes back into the cluster ring, enabling a number of additional practices around upgrades, hot swaps for failures, or even version changes.

### Riak can be used as a building block for distributed (aka cloud) infrastructure.

The concepts and contractual components that Riak Database is built on are available for use via the [Riak Core Project](https://github.com/basho/riak_core). If you’re looking into starting a project around distributed systems this is a great place to get start. Also be sure to do a general web engine (re: google) search for “riak core” and you’ll find lots of material around the project, and projects people have started with the project as a base. I’m currently in the process of putting together one of these projects myself.

### Riak is eventually consistent.

The term eventually consistent is becoming more and more common place. Riak is one of the many systems, that inherently often apply to distributed systems, that use the concepts of eventual consistency. The idea, is that even though all nodes may not immediately receive a new piece of data, or updated piece of data, they eventually will receive that update and by synchronized with the cluster ring of nodes. This goes back to the equality of nodes and removal of the master-less concepts, providing the availability and other capabilities, with some trade off in the synchronization of data through eventual consistency.

**In Summary**

That’s round one for the many features of Riak. I’ll be adding more in the future, but for now this is a good starting point in knowing about and knowing what Riak is, what it can be used for, and how it might help you extend, maintain or invent the next great piece of technology.
