---
title: Sorry Database Nerds, Nobody Actually Gives a Shit…
date: 2013-11-03 09:11:09 -0800
last_modified_at: 2013-11-25 15:11:48 -0800
permalink: /2013/11/03/sorry-database-nerds-nobody-actually-gives-a-shit/
slug: sorry-database-nerds-nobody-actually-gives-a-shit
wp_id: 9046
original_url: https://compositecode.blog/2013/11/03/sorry-database-nerds-nobody-actually-gives-a-shit/
categories:
- Databases
- Ideas
tags:
- aaS
- database
- distributed database
- geo
- graph
- graph theory
- key value
- managed database
- managed services
- mongo
- mongo lab
- mongodb
- mongolab
- nosql
- orchestrate.io
- orchestrateio
- paas
- relational database
- sql
- time series
excerpt: So I’ve been in more than a few conversations about data structures, various academic conversations and other notions about where and how data should be stored. I’ve been on projects and managed projects that involve teams of people determining how to manage data so that other people can just not manage data. They want to …
---

So I’ve been in more than a few conversations about data structures, various academic conversations and other notions about where and how data should be stored. I’ve been on projects and managed projects that involve teams of people determining how to manage data so that other people can just not manage data. They want to focus on business use and not the data mechanisms underneath. The root of everything around databases really boils down to a single thing – how can we store X and retrieve X – nobody actually trying to get business done or change the world is going to dig into the data storage mechanisms if they don’t have to. To summarize,

> ***nobody actually gives a shit…***

![](https://photos.adron.me/Software/Course-Materials/Distributed-Databases/i-XW6sRQJ/0/S/node%20down-S.jpg)At least nobody does until the database breaks, or somebody has to be hired to manage or tune queries or something or some other problem comes up. In the ideal world we could just put data into the ether and have it come back when we ask for it. Unfortunately we have to keep caring for where the data is, how it’s stored, the schema (even in schema-less, you still need to know the schema of the data at some point, it’s just another abstraction to push off dealing with the database), how to backup, recover, [data gravity](http://blog.mccrory.me/2010/12/07/data-gravity-in-the-clouds/), proximity and a host of other concerns. Wouldn’t it be cool if we could just work on our app or business? Wouldn’t it be nice to just, well, focus on things we actually give a shit about?

## Managed Data Systems!

The whole \*aaS and PaaS World has been pushing to simplify operations to the point that the primary, if not the only concern, is the business itself. This is a pretty big step in many ways, but holds a lot of hope and promise around fixing the data gravity, proximity, management and related concerns. One provider of services that has an interesting start around the NoSQL realm is Orchestrate.io. I’ll have more about them in the future, as I’ll actually be working on hacking on some code against their platform. They’re currently solving a number of the mentioned issues. Which is great, a solid starting point that takes us past the draconian nature of the old approach to NoSQL and Relational Databases in general.

There has been some others, such as Mongo Labs or such, that have created a sort of DBaaS. This however doesn’t fill the gap that Orchestrate.io is filling. So far almost every \*aaS database or other solution has merely been a single type of database that a developer can just throw data at in a single kind of way. Not really flexible, and really only abstracting some manual work, but not providing much additional value add around using the actual data. Orchestrate.io is bridging these together with search, replication and other features to provide a platform on which multiple options are available via the API. Key value, geo, time series and others are all coming together for them nicely. Having all the options actually creates a real value add, versus just provide one single way to do one thing.

## Intelligent Data Systems?

After checking out and [interviewing Orchestrate.io](/2013/10/22/orchestrate-io-to-the-death-of-database-infrastructure/) recently I’ve stumbled into a few other ideas. It would be perfect for them to implement or for the open source community to take a stab at. What would happen if the systems storing the data knew where to put things? What would be the case for providing an intelligent indexing policy or architecture at the schema design decision layer, the area where a person usually must intervene? Could it be done?

A decision tier that scans and makes decisions on the data to revamp the way it is stored against a key value, geo, time series or other method. Could it be done in real time? Would it have to go through some type of processing system? The options around implementing something like this are numerous, but this just leaves a lot of space for providing value add around the data to reduce the complexity of this decision making.

Imagine you have key value data, that needs to be associative based on graph principles, that you must store in a highly available system with pertinent real-time data provided based on those graph relations. A decision layer, to create an intelligent data system, could monitor the data and determine the frequent query paths against the data. If the data is growing old it could move data from real-time to archival via the key value. Other decisions could be made to push up data segments into a cache tier or some other mechanism to provide realtime graph connections to client queries. These are all decisions that would need to be made by somebody working on the data, but could be put into a set of rules to allow for re-allocation of the data via automated mechanisms into better storage options. Why keep old data that isn’t queried in the active in memory graph store, push it to the distributed key store. Why keep the graph data on drive when it can be in memory with correlated keys in a key value in memory store, backed by an on drive key value? All valid decisions, all becoming better understood day by day. It’s about time some of this decision process started to be automated.

What are your thoughts? Pro-intelligent data systems or anti-intelligent data systems? Think it’ll work or is it the wrong approach? Maybe the system should approach some other zenith or axiom point to become truly abstracted and transparent?
