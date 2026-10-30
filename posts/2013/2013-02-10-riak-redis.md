---
title: Not So Versus, Riak Versus Redis
date: 2013-02-10 21:38:29 -0800
last_modified_at: 2013-02-10 21:38:29 -0800
permalink: /2013/02/10/riak-redis/
slug: riak-redis
wp_id: 7694
original_url: https://compositecode.blog/2013/02/10/riak-redis/
categories:
- Basho
- Databases
tags:
- basho
- database
- databases
- redis
- riak
excerpt: Recently a friend of mine and fellow coder, harkening back to my Russell Investments Enterprise Developer days posed the discussion of Redis versus Riak. Well, first off, I thought I myself needed to write down a line by line comparison. I’ve worked with both in various ways but I’d never really thought about them lined …
---

Recently a friend of mine and fellow coder, harkening back to my Russell Investments Enterprise Developer days posed the discussion of Redis versus Riak. Well, first off, I thought I myself needed to write down a line by line comparison. I’ve worked with both in various ways but I’d never really thought about them lined up side by side. Often I think of the two pieces of technologies as complementary in various ways. But before I dive into that, let’s take a look at the stats side by side of each.

|  |  |  |
| --- | --- | --- |
| Company/Maintainer/Builder | Basho Technologies **[@basho](https://twitter.com/basho)** | Salvatore Sanfilippo **[@antirez](https://twitter.com/antirez)** w/ **[VMware](http://www.vmware.com/)** |
| Official Product Name | Riak | Redis |
| License | Apache ([link](https://github.com/basho/riak/blob/master/LICENSE)) | BSD ([link](http://redis.io/topics/license)) |
| Storage Type | Key Value | Key Value |
| Protocols | HTTP/RESTful & Custom Binaries | Telnet like / Proprietary |
| Replication/Clustering | Masterless | Master / Slave Replication |
| Language/Framework | Erlang / C | C / C++ |
| Best Use | Dynamo style architecture & concepts. Primarily used for extreme high availability. | Best known and used for extremely fast access to quickly changing data and known size. |
| Key Feature | Fault Tolerant | Crazy Fast |

Redis is primarily something you’re going to use to move data in and out at crazy fast speeds. However, when you need to store data, it isn’t ideal. There are ways, but it tends to work better handing off to something else to store the data. However Riak on the other hand isn’t always the fastest database, but it’ll withstand serious hits and still maintain integrity of data. It is also tunable for writes, reads and other characteristics that enable tuning and also integrity of the data among nodes. The more nodes in Riak you have the higher available iOPs and fault tolerance. The other thing that Riak can do over time, is truly scale from a horizontal and vertical perspective. Grow Riak tall and wide, it’ll give you linear performance and integrity improvements.

The thing I’ve seen over and over, is Riak as a store and Redis as a cache or other temporal specific data store for websites or other high transaction systems. Overall each serves a very specific purpose but work well in conjunction with each other when you’re rolling together an extremely high performance architecture with an extremely highly available back end data store.

If you’re in Seattle and up for lunch this Wednesday, join me for the [Riak Nerd Lunch](http://www.meetup.com/Seattle-Riak/events/103333992/).
