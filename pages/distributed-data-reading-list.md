---
layout: page
title: Distributed Data Reading List
date: 2018-06-13 09:33:46 -0700
last_modified_at: 2018-06-13 09:33:46 -0700
permalink: /distributed-data-reading-list/
slug: distributed-data-reading-list
wp_id: 14155
original_url: https://compositecode.blog/distributed-data-reading-list/
---

I’ve started this page on Wednesday, June 13th 2018. It is a a page dedicated to links of good reads on distributed systems, different methods of data storage, graph databases, and all the different related topics.  These topics are helpful to understanding how to effectively store data in the way you need the data to be used.

- [About Deletes and Tombstones in Cassandra](http://thelastpickle.com/blog/2016/07/27/about-deletes-and-tombstones.html) – The process of Tombstones is writing a record, because data is largely immutable in a distributed database like Cassandra, to mark that it is “deleted”. This article goes into more depth about the process, why it is done this way, and ways to streamline this process.
- [Cleaning Up Tombstones in DataStax Enterprise and Apache Cassandra](https://academy.datastax.com/support-blog/cleaning-tombstones-datastax-dse-and-apache-cassandra) – The process of marking records with a tombstone can take up storage, sometimes significantly so and a need to clean up this process arises. This article is a look at some of the ways to clean up this process for your distributed Cassandra/DataStax Systems.
