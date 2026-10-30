---
title: Riak Developer Guidance
date: 2013-08-21 13:09:45 -0700
last_modified_at: 2013-08-21 15:59:28 -0700
permalink: /2013/08/21/riak-development-guidance-the-client-round-robin-anti-pattern/
slug: riak-development-guidance-the-client-round-robin-anti-pattern
wp_id: 8825
original_url: https://compositecode.blog/2013/08/21/riak-development-guidance-the-client-round-robin-anti-pattern/
categories:
- Architecture
- Distributed Things
- Riak
tags:
- architecture
- architecture guidance
- cluster
- code guidance
- database
- database cluster
- design guidance
- distributed databases
- distributed systems
- enterprise architecture
- node
- nodes
- riak
- riak client
- round robin
- software architecture
excerpt: The “Client Round Robin Anti-Pattern” One of the features that is often available in Riak Client software (including the CorrguatedIron .NET Client, the riak-js client and others) is the ability to send requests to the Riak Cluster through a round robin style approach. What this means is each IP, of each node within the Riak …
---

## The “Client Round Robin Anti-Pattern”

![](https://photos.adron.me/Software/Misc-Images/Just-Icons-and-Bits/i-GDsdPNb/0/S/1298948512_batch_process-S.png)One of the features that is often available in Riak Client software (including the **[CorrguatedIron](https://github.com/DistributedNonsense/CorrugatedIron/)** .NET Client, the **[riak-js](https://github.com/mostlyserious/riak-js)** client and others) is the ability to send requests to the Riak Cluster through a round robin style approach. What this means is each IP, of each node within the Riak Cluster is entered into a config file for the client. The client then goes through that list to send off requests to read, write or delete data in the database.

The client being responsible and knowledgeable about the data tier of the application in an architecture is an immediate red flag! The concept around SoC ([Separation of Concerns](http://en.wikipedia.org/wiki/Separation_of_concerns)) dictates that

> “SoC is a *principle for separating a computer program into distinct sections, such that each section addresses a separate concern.*“

Having the client provide a network tier layer to round robin communication with the database leaves us in a scenario that should be separated into individual concerns. Below is some basic guidance on eliminating this SoC issue.

- Client ONLY sends and receives communication: The client, especially in the situation with a distributed system like Riak should only be dealing with sending and receiving information from the cluster or a facade that provides an interface for that cluster.
- Another layer should deal with the network communication and division of nodes and node communication. Ideally, in the case or Riak, and most distributed systems this should be dealt with at the network device layer (router).
- The network device (router) layer would ideally be able to have (through software likely) a way to automate the failure, inclusion or exclusion of nodes with the cluster system. If a node goes down, the network device should handle the immediate cessation of communication with that node from all clients, routing the communication accordingly to an active node.
- The node itself needs to maintain a continual information state available to the network. Ideally the network state would identify any addition or removal of a node and if possible the immediate failure of a node. Of course it isn’t always possible to be informed of a failure, but the first line of defense should start within the cluster itself among the nodes.

**The Anti-Pattern**

Having the client handle all of these parts of the functional architecture leads to a number of problems, not merely that the guidance of the SoC concept is broken. With the client attempting to track and be aware of the individual nodes in the cluster, it sets the client with a huge responsibility.

![](https://photos.adron.me/Software/Misc-Images/Bad-Resume/i-rsGrq2B/0/Th/bush_doing_it_wrong-Th.jpg)Take for instance the riak-js client. If a node goes down the client will need to be aware of which node has gone down. For a few seconds (yes, you have to wait entire seconds at this level) the node will be gone and the client won’t know it is down. The client would just have to reasonably wait. When the communication times out, the client would then have to have the responsibility of marking that particular node as down. At this point the client must track which node it is in some type of data repository local to the client. The client must also set a time or some way to identify when the node comes back up. Several questions start to come up such as;

- Does the client do an arbitrary test to determine when the node comes back up?
- When the node comes back up is it considered alive or damaged?
- How would the client manage the IP (or identifier) of the node that has gone down?
- How long would the client store that the node is down?

The list of questions can get long pretty quick, thus the bad karma of not following a good practice around separating your concerns appropriately! One has to be careful, a god class might be right around the corner otherwise! That’s it for this quick journey into some distributed database usage guidelines. Until next, happy data sciencing.  😉
