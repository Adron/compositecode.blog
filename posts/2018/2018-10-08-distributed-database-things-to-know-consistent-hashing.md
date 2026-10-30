---
title: Consistent Hashing
date: 2018-10-08 09:30:15 -0700
last_modified_at: 2018-10-29 09:42:02 -0700
permalink: /2018/10/08/distributed-database-things-to-know-consistent-hashing/
slug: distributed-database-things-to-know-consistent-hashing
wp_id: 14168
original_url: https://compositecode.blog/2018/10/08/distributed-database-things-to-know-consistent-hashing/
categories:
- Distributed Things
tags:
- consistent hashing
- distributed databases
- distributed systems
excerpt: I wrote about consistent hashing in 2013 when I worked at Basho, when I had started a series called “Learning About Distributed Databases” and today I’m kicking that back off after a few years (ok, after 5 or so years!) with this post on consistent hashing. As with Riak…
image: /wp-content/uploads/2018/10/fixed1.png
format: aside
---

I wrote about consistent hashing in 2013 when I worked at Basho, when I had started a series called “[Learning About Distributed Databases](/2013/05/25/consistent-hashing-learning-about-distributed-databases-issue-002/)” and today I’m kicking that back off after a few years (ok, after 5 or so years!) with this post on consistent hashing.

As with Riak, which I wrote about in 2013, Cassandra remains one of the core active distributed database projects alive today that provides an effective and reliable consistent hash ring for the clustered distributed database system. This hash function, is an algorithm that maps data to variable length to data that’s fixed. This consistent hash is a kind of hashing that provides this pattern for mapping keys to particular nodes around the ring in Cassandra. One can think of this as a kind of [Dewey Decimal Classification](https://en.wikipedia.org/wiki/Dewey_Decimal_Classification) system where the cluster nodes are the various bookshelves in the library.

Ok, so maybe the Dewey Decimal system isn’t the best analogy. Does anybody even learn about that any more? If you don’t know what it is, please read up and [support your local library](https://bookriot.com/2017/02/06/7-ways-to-support-your-local-library-right-now/).

Consistent hashing allows data distributed across a cluster to minimize reorganization when nodes are added or removed. These partitions are based on a particular partition key. The partition key shouldn’t be confused with a primary key either, it’s more like a unique identifier controlled by the system that would make up part of a primary key of a primary key that is made up of multiple [candidate keys](https://en.wikipedia.org/wiki/Candidate_key) in a [composite key](https://en.wikipedia.org/wiki/Compound_key).

For an example, let’s take a look at sample data from the DataStax docs on consistent hashing.

> For example, if you have the following data:
>
> | name | age | car | gender |
> | --- | --- | --- | --- |
> | jim | 36 | camaro | M |
> | carol | 37 | 345s | F |
> | johnny | 12 | supra | M |
> | suzy | 10 | mustang | F |
>
> The database assigns a hash value to each partition key:
>
> | Partition key | Murmur3 hash value |
> | --- | --- |
> | jim | -2245462676723223822 |
> | carol | 7723358927203680754 |
> | johnny | -6723372854036780875 |
> | suzy | 1168604627387940318 |
>
> Each node in the cluster is responsible for a range of data based on the hash value.
>
> *Hash values in a four node cluster*
>
> ![](https://docs.datastax.com/en/dse/6.0/dse-arch/datastax_enterprise/images/arc_hashValueRange.png)
>
> DataStax Enterprise places the data on each node according to the value of the partition key and the range that the node is responsible for. For example, in a four node cluster, the data in this example is distributed as follows:
>
> | Node | Start range | End range | Partition key | Hash value |
> | --- | --- | --- | --- | --- |
> | 1 | -9223372036854775808 | -4611686018427387904 | johnny | -6723372854036780875 |
> | 2 | -4611686018427387903 | -1 | jim | -2245462676723223822 |
> | 3 | 0 | 4611686018427387903 | suzy | 1168604627387940318 |
> | 4 | 4611686018427387904 | 9223372036854775807 | carol | 7723358927203680754 |

So there ya go, that’s consistent hashing and how it works in a distributed database like [Apache Cassandra](http://cassandra.apache.org/), the derived distributed database [*DataStax Enterprise*](https://www.datastax.com/products/datastax-enterprise), or the mostly defunct RIP Riak. If you’d like to dig in further, I’ve also found [Distributed Hash Tables](https://en.wikipedia.org/wiki/Distributed_hash_table) interesting and also a host of other articles that delve into coding up a consistent has table, respective ring, and the whole enchilada. Check out these articles for more information and details:

- - [Simple Magic Consistent](https://dzone.com/articles/simple-magic-consistent) by Mathias Meyer [@roidrage](https://twitter.com/roidrage) CTO of [Travis CI](https://travis-ci.org/). Mathias’s post is well written and drives home some good points.
  - [Consistent Hashing: Algorithmic Tradeoffs](https://medium.com/@dgryski/consistent-hashing-algorithmic-tradeoffs-ef6b8e2fcae8) by Damien Gryski [@dgryski](https://twitter.com/dgryski). This post from Damien is pretty intense, and if you want code, he’s got code for ya.
  - How Ably Efficiently Implemented Consistent Hashing by [Srushtika Neelakantam](https://www.linkedin.com/in/srushtika/). Srushtika does a great job not only of describing what consistent hashing is but also has drawn up diagrams, charts, and more to visualize what is going on. But that isn’t all, she also wrote up some code to show nodes coming and going. A really great post.

For more on distributed database things to know subscribe to the blog, of course the ole’ RSS feed works great too, and follow [@CompositeCode](https://twitter.com/CompositeCode) on Twitter for blog updates.

> ## Distributed Database Things to Know Series
>
> 1. Consistent Hashing (this post)
> 2. [Apache Cassandra Datacenter & Racks](/2018/10/29/cassandra-datacenter-racks/)
