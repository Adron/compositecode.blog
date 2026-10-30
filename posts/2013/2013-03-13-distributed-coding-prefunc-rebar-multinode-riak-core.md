---
title: 'Distributed Coding Prefunc: Rebar Multinode Riak Core'
date: 2013-03-13 15:32:52 -0700
last_modified_at: 2013-03-13 17:25:09 -0700
permalink: /2013/03/13/distributed-coding-prefunc-rebar-multinode-riak-core/
slug: distributed-coding-prefunc-rebar-multinode-riak-core
wp_id: 7881
original_url: https://compositecode.blog/2013/03/13/distributed-coding-prefunc-rebar-multinode-riak-core/
categories:
- Basho
- Databases
- Distributed Things
- Erlang
- How-to
- Riak
tags: []
excerpt: Before diving into this entry, you might want to check out some of my other getting Erlang installed with appropriate testing frameworks entries. Moving on… At Basho we’re are always trying to make it easier to do big things. A short time ago we pushed forward on Rebar, Riak Core and getting things put together …
---

[![](/images/adronhall.smugmug.com/Software/Misc-Images/Just-Icons-and-Bits/i-rnNZZNH/0/O/Erlang_logo.png)](http://www.erlang.org/)Before diving into this entry, you might want to check out some of my other [getting Erlang installed with appropriate testing frameworks entries](/2013/02/11/prefunc-data-types/). Moving on…

![](/images/adronhall.smugmug.com/Software/Misc-Images/Just-Icons-and-Bits/i-thvBzTp/0/O/riak-transparent-larger.png)At Basho we’re are always trying to make it easier to do big things. A short time ago we pushed forward on Rebar, Riak Core and getting things put together to make it simpler to get kick started working on distributed systems like the Riak Database & distributed system itself. There’s way more that is possible, which I’ll get into in just a minute. Before diving into some of those things, here’s a few quick links & context of what exactly Rebar and Riak Core are.

**Riak Core**
**Github:** <https://github.com/basho/riak_core>

Riak Core has been available for quite some time. We’ve also been hustling for a while getting together a robust array of material around Riak Core. One excellent place to get started on learning about Riak Core is the “[Introducing Riak Core](http://basho.com/introducing-riak-core/)” blog article published on the Basho blog a while back. To describe [Riak Core](https://github.com/basho/riak_core), or [riak\_core](https://github.com/basho/riak_core), it is the underpinnings of what [Riak](https://github.com/basho/riak) is built on. It provides many features to get you started building distributed systems. A few of the key features are being able to track and manage the nodes, clusters and related pieces of the distributed architecture within a system.

**Rebar**
**Github:** <https://github.com/basho/rebar>
**Wiki:** <https://github.com/basho/rebar/wiki>

Rebar is an Erlang build tool that helps you in putting together projects based on Riak Core.

**Rebar Riak Core**
**Github:** <https://github.com/basho/rebar_riak_core>

The Rebar Riak Core project repository template helps you start writing things like the Riak Database itself. It’s based on setting up Riak Core via template scripting an N Node Cluster devrel, vnodes, etc. Once you’re up and running it can be used to help develop distributed, scalable and fault tolerant applications.

For more on the Rebar Riak Core check out the README.md in the github repository. There are some great examples of how to get a multinode devrel running in a few steps.

**Rebar Riak Core Quick Start**

The quickest way to get started using the Riak Core and Rebar scripts is to get the prebuilt binaries or you can just clone and install the Rebar scripts if you’d like all the things. To get the binaries and executables you can download and have them ready by wget (or use your preferred method to download).

```bash
wget http://cloud.github.com/downloads/basho/rebar/rebar && chmod u+x rebar
```

To get the cloned repository and ready for use.

```bash
$ git clone git://github.com/rebar/rebar.git
$ cd rebar
$ ./bootstrap
```

Now the easiest way possible is to use the Riak Core Templates with a quick git clone. After cloning the repo, copy them to the rebar templates directory (note that you’ll need to create this initially) and then create a working directory to put the project in and navigate into that directory.

```bash
git clone git://github.com/rzezeski/rebar_riak_core.git
mkdir -p ~/.rebar/templates
cp rebar_riak_core/* ~/.rebar/templates
mkdir projectNameHere
cd projectNameHere
```

Now that a template is available, run the following command to create the Erlang Project.

```bash
rebar create template=riak_core_multinode appid=rabbits nodeid=rabbits
```

You’re now ready to go to work using Rebar and the template you’ve created. I followed the try-try-try example repo in the example above to get started, check it out for a great walk through that dives in deeper to Riak Core, each small element of the project and files created, and a multi-node project as the sample.

***So what to do now?***

This is where it is time to throw around some creativity to get real solutions to real problems. Building distributed systems is becoming more and more paramount to effective usage of infrastructure and systems. Using Riak Core to get started building out your distributed system is an ideal place to start. These are a few ideas that the team was brainstorming on. Over the coming weeks we’ll be putting together material to outline ways to not only get started, but to implement systems like this.

**Distributed Web Caching Tier**

Caching tiers often come up in conversations, whether related to distributed systems or not, and often end up on the distributed topic. The question resounds, “how do I create a caching tier that can be distributed and provide real session, state management, cached elements, live data and other needs?” Well Riak Core is a great place to start developing a custom distributed caching tier that could even extend to use Riak KV (the Riak Database implemented on Riak Core), Redis, Rabbit MQ or many other solutions by pulling them together to provide appropriate cache at the appropriate tiers of an application architecture.

**In House Cluster Monitoring & Smart Resolver**

One of the things that the Riak Core would be used to great effect for is a multi-node, clustered and geographically dispersed monitoring system for any multi-data center application. This could be built out and used for almost any actual environment, with custom specifics or a completely generic situation of pizza box servers. Because fo the distributed concepts behind Riak Core it would provide an ideal basis for monitoring – and re-launching or otherwise dealing with systems that need high uptime and recovered as fast as possible if they go down.

**Logging, Web, Server, and Business Analytics**

In any situation where analytics are collected there are often dozens if not thousands of servers, various systems and even numerous devices that may be emitting data via services or other mediums. Riak Core is a great place to lay the groundwork for a distributed system that could maintain a massive store of managed data for fast searching of analytics. This could be the groundwork for biotech research analytics, analysis of market data or a dozen other things that need highly available systems storing vast data with map reduction or other search capabilities. Think Business Intelligence (BI) with serious technological power.

**Multi-node Project**

Of course, as the example I used to create the first sample above, dive into the try-try-try tutorial for some great multi-node how to. If you have any questions please jump in ping me on twitter [@adron](http://twitter.com/adron) or ping [@basho](http://twitter.com/basho), join the [mailing list](http://lists.basho.com/mailman/listinfo/riak-users_lists.basho.com), the IRC #riak channel on freenode.
