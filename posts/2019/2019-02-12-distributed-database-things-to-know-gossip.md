---
title: 'Distributed Database Things to Know: Gossip'
date: 2019-02-12 11:19:43 -0800
last_modified_at: 2019-02-12 11:19:43 -0800
permalink: /2019/02/12/distributed-database-things-to-know-gossip/
slug: distributed-database-things-to-know-gossip
wp_id: 14172
original_url: https://compositecode.blog/2019/02/12/distributed-database-things-to-know-gossip/
categories:
- Databases
- datastax enterprise
- Distributed Things
tags: []
excerpt: Some of the names used can seem to conflate the actual purpose of a feature’s functionality in distributed databases. However gossip is pretty spot on. Within a group of people gossiping the purpose is to find out each other’s business. What’s going on with Frank, who’s he seeing, and Sally started a business, say what! …
image: /wp-content/uploads/2018/10/fixed1.png
format: aside
---

Some of the names used can seem to conflate the actual purpose of a feature’s functionality in distributed databases. However gossip is pretty spot on. Within a group of people gossiping the purpose is to find out each other’s business. What’s going on with Frank, who’s he seeing, and Sally started a business, say what! In the end, all gossippers get into the business and understand what Frank, Sally, and the whole crew are up to. This is a good analogy for what gossip does in a distributed database, or distributed systems in general.

The way gossip works in node, is on a peer-to-peer basis. It’s a communication protocol with the purpose of minding the other nodes business so the singular node gossiping can go about its business. The process runs every second and exchanges state messages between the nodes, which then can update their respective state and keep all nodes informed.

Preventing over-communication and mixed messages, the list is derived from seed nodes for all nodes in the cluster. When a node boots up it initiates its gossip from this seed node, which we usually have a few of, and then continues with that gossip list. Note, that seed nodes aren’t a single point of failure, as other nodes in the cluster will take their place if need be, they’re just kind of designated as the lead to initiate a gossip list from.

It is important in Apache Cassandra to also designate a single seed node per replication group (i.e. datacenter) for the seed list. This is recommended for fault tolerance, else gossip has to communicate across higher latency to hit each datacenter, which can eat at response time and performance of the gossip. Think of sending a snail mail USPS letter to a friend to get gossip news! That would take months just to find out what’s going on, kind of the same version of that for computer nodes going across datacenters to talk to the seed node.
