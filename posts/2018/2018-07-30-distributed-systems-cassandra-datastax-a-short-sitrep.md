---
title: 'Distributed Systems: Cassandra, DataStax, a Short SITREP'
date: 2018-07-30 17:33:38 -0700
last_modified_at: 2018-08-01 12:43:27 -0700
permalink: /2018/07/30/distributed-systems-cassandra-datastax-a-short-sitrep/
slug: distributed-systems-cassandra-datastax-a-short-sitrep
wp_id: 14307
original_url: https://compositecode.blog/2018/07/30/distributed-systems-cassandra-datastax-a-short-sitrep/
categories:
- cassandra
- datastax enterprise
- Unknown Code Ramblings
tags:
- cassandra
- cloud
- columnar
- cql
- datastax
- hybrid-cloud
- multi-cloud
- read repair
- spark
- sql
excerpt: SITREP = Situation Report. It’s military speak. 💂🏻‍♂️ Apache Cassandra is one of the most popular databases in use today. It has many characteristics and distinctive architectural details. In this post I’ll provide a description and some details for a number of these features and characteristics, divided as such. Then, after that (i.e. toward the end, …
---

SITREP = Situation Report. It’s military speak. 💂🏻‍♂️

[Apache Cassandra](http://cassandra.apache.org/) is one of the most popular databases in use today. It has many *characteristics* and distinctive *architectural* details. In this post I’ll provide a description and some details for a number of these *features* and *characteristics*, divided as such. Then, after that (*i.e. toward the end, so skip there if you just want to the differences*) I’m doing to summarize key differences with the latest release of the [DataStax Enterprise 6](https://www.datastax.com/products/datastax-enterprise) version of the database.

## Cassandra Characteristics

Cassandra is a linearly scalable, highly available, fault tolerant, distributed database. That is, just to name a few of the most important characteristics. The Cassandra database is also cross-platform (runs on any operating systems), multi-cloud (runs on and across multiple clouds), and can survive regional data center outages or even in multi-cloud scenarios entire cloud provider outages!

Columnar Store, Column Based, or Column Family? What? Ok, so you might have read a number of things about what Cassandra actually is. Let’s break this down. First off, a columnar or column store or column oriented database guarantees data location for a single column in a node on disk. The column may span a bunch of or all of the rows that depend on where or how you specify partitions. However, this isn’t what the Cassandra Database uses. Cassandra is a column-family database.

A column-family storage architecture makes sure the data is stored based on locality of the data at the partition level, not the column level. Cassandra partitions group rows and columns split by a partition key, then clustered together by a specified clustering column or columns. To query Cassandra, because of this, you must know the partition key in order to avoid full data scans!

Cassandra has these partitions that guarantee to be on the same node and sort strings table (referred to most commonly as an SSTable \*) in the same location within that file. Even though, depending on the compaction strategy, this can change things and the partition can be split across multiple files on a disk. So really, data locality isn’t guaranteed.

Column-family stores are great for high throughput writes and the ability to linearly scale horizontally (*ya know, getting lots and lots of nodes in the cloud!*). Reads using the partition key are extremely fast since this key points to exactly where the data resides. However, this often – at least last I know of – leads to a full scan of the data for any type of ad-hoc query.

A sort of historically trivial but important point is the column-family term comes from the storage engine originally used based on a key value store. The value was a set of column value tuples, which where often referenced as *family*, and later this *family* was abstracted into *partitions*, and then the storage engine was matched to that abstraction. Whew, ok, so that’s a lot of knowledge being coagulated into a solid eh!  [scuse’ my odd artful language use if you visualized that!]

With all of this described, a that little history sprinkled in, when reading the description of Cassandra in the [README.asc](https://github.com/apache/cassandra) file of the actual [Cassandra Github Repo](https://github.com/apache/cassandra) things make just a little more sense. In the file it starts off with a description,

> Apache Cassandra is a highly-scalable partitioned row store. Rows are organized into tables with a required primary key.
>
> Partitioning means that Cassandra can distribute your data across multiple machines in an application-transparent matter. Cassandra will automatically repartition as machines are added and removed from the cluster.
>
> Row store means that like relational databases, Cassandra organizes data by rows and columns. The Cassandra Query Language (CQL) is a close relative of SQL.

Now that I’ve covered the 101 level of what Cassandra is I’ll give a look at DataStax and their respective offering.

## DataStax

DataStax Enterprise at first glance might be a bit confusing since immediate questions pop up like, “Doesn’t DataStax make Cassandra?”, “Isn’t DataStax just selling support for Cassandra?”, or “Eh, wha, who is DataStax and what does this have to do with Cassandra?”. Well, I’m gonna tell ya all about where we are today regarding all of these things fit.

### Performance

DataStax provides a whole selection of amenities around a database, which is derived from the Cassandra Distributed Database System. The core product and these amenities are built into what we refer to as the “*[DataStax Enterprise 6](https://www.datastax.com/products/datastax-enterprise-6)*“. Some of specific differences are that the database engine itself has been modified out of band and now delivers 2x the performance of the standard Cassandra implemented database engine. I was somewhat dubious when I joined but after the third party benchmarks where completed that showed the difference I grew more confident. My confidence in this speed increase grew as I’ve gotten to work with the latest version I can tell in more than a few situations that it’s faster.

### Read Repair & NodeSync

If you already use Cassandra, read repair works a certain way and that still works just fine in DataStax Enterprise 6. But one also has the option of using NodeSync which can help eliminate scripting, manual intervention, and other repair operations.

### Spark SQL Connectivity

There’s also an always on SQL Engine for automated uptime for apps using DataStax Enterprise Analytics. This provides a better level of analytics requests and end -user analytics. Sort of on this related note, DataStax Studio also has notebook support for Spark SQL now. Writing one’s Spark SQL gets a little easier with this option.

### Multi-Cloud / Hybrid-Cloud

Another huge advantage of DataStax Enterprise is going multi-cloud or hybrid-cloud with DataStax Enterprise Cassandra. Between the Lifecycle Manager (LCM), OpsCenter, and related tooling getting up and running with a cluster across a varying range of data-centers wherever they may be is quick and easy.

## Summary

I’ll be providing deeper dives into the particular technology, the specific differences, and more in the future. For now I’ll wrap up this post as I’ve got a few others coming distinctively related to distributed database systems themselves ranging from specific principles (like CAP Theorem) to operational (how to and best ways to manage) and development (patterns and practices of developing against) related topics.

Overall the solutions that DataStax offers are solid advantages if you’re stepping into any large scale data (big data or whatever one would call their plethora of data) needs. Over the coming months I’ve got a lot of material – from architectural research and guidance to tactical coding implementation work – that I’ll be blogging about and providing. I’m really looking forward to exploring these capabilities, being the developer advocate to DataStax for the community of users, and learning a thing or three million.
