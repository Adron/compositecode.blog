---
title: The Database Deluge…  Who’s Who
date: 2013-01-15 23:19:30 -0800
last_modified_at: 2013-01-18 10:15:26 -0800
permalink: /2013/01/15/the-database-deluge-whos-who/
slug: the-database-deluge-whos-who
wp_id: 7518
original_url: https://compositecode.blog/2013/01/15/the-database-deluge-whos-who/
categories:
- Databases
- Distributed Things
- Reviews
- Riak
tags:
- cassandra
- column database
- couch
- couchdb
- database
- document database
- document store
- graph database
- hbase
- key-value database
- key-value store
- mongo
- mongodb
- neo4j
- nosql
- rdbms
- redis
- redis.io
- relational database
- riak
excerpt: These are the top NoSQL Solutions in the market today that are open source, readily available, with a strong and active community, and actively making forward progress in development and innovations in the technology. I’ve provided them here, in no order, with basic descriptions, links to their main website presence, and with short lists of …
---

These are the top NoSQL Solutions in the market today that are open source, readily available, with a strong and active community, and actively making forward progress in development and innovations in the technology. I’ve provided them here, in no order, with basic descriptions, links to their main website presence, and with short lists of some of their top users of each database. Toward the end I’ve provided a short summary of the database and the respective history of the movement around No SQL and the direction it’s heading today.

## Cassandra

<http://cassandra.apache.org/>

Cassandra is a distributed databases that offers high availability and scalability. Cassandra supports a host of features around replicating data across multiple datacenters, high availability, horizontal scaling for massive linear scaling, fault tolerance and a focus, like many NoSQL solutions around commodity hardware.

Cassandra is a hybrid key-value & row based database, setup on top of a configuration focused architecture. Cassandra is fairly easy to setup on a single machine or a cluster, but is intended for use on a cluster of machines. To insure the availability of features around fault tolerance, scaling, et al you will need to setup a minimal cluster, I’d suggest at least 5 nodes (5 nodes being my personal minimum clustered database setup, this always seems to be a solid and safe minimum).

Cassandra also has a query language called CQL or Cassandra Query Langauge. Cassandra also support Apache Projects Hive, Pig with Hadoop integration for map reduce.

***Who uses Cassandra?***

- IBM
- HP
- Netflix
- *…many others…*

[![](/images/adronhall.smugmug.com/Software/Misc-Images/Just-Icons-and-Bits/i-6JPqzLV/0/O/hbase_logo.png)](http://hbase.apache.org/)HBase

<http://hbase.apache.org/>

In the book, [Seven Databases in Seven Weeks](http://www.amazon.com/Seven-Databases-Weeks-Modern-Movement/dp/1934356921), the Apache HBase Project is described as a nail gun. You would not use HBase to catalog your sales list just like you wouldn’t use a nail gun to build a dollhouse. This is an apt description of HBase.

HBase is a column-oriented database. It’s very good at scaling out. The origins of HBase are rooted in [BigTable by Google](http://research.google.com/archive/bigtable.html). The proprietary database is described in in the 2006 white paper, “Bigtable: A Distributed Storage System for Structured Data.”

HBase stores data in buckets called tables, the tables contain cells that are at the intersection of rows and columns. Because of this HBase has a lot of similar characteristics to a relational database. However the similarities are only in name.

HBase also has several features that aren’t available in other databases, such as; versioning, compression, garbage collection and in memory tables. One other feature that is usually only available in relational databases is strong consistency guarantees.

The place where HBase really shines however is in queries against enormous datasets.

HBase is designed architecturally to be fault tolerate. It does this through write-ahead logging and distributed configuration. At the core of the architecture HBase is built on Hadoop. Hadoop is a sturdy, scalable computing platform that provides a distribute file system and mapreduce capabilities.

***Who is using it?***

- Facebook uses HBase for its messaging infrastructure.
- Stumpleupon uses it for real-time data storage and analytics.
- Twitter uses HBase for data generation around people search & storing logging & monitoring data.
- Meetup uses it for site data.
- There are many others including Yahoo!, eBay, etc.

## Mongo

<http://www.mongodb.org/>

MongoDB is built and maintained by a company called 10gen. MongoDB was released in 2009 and has been rising in popularity quickly and steadily since then. The name, contrary to the word mongo, comes from the word humongous. The key goals behind MongoDB are performance and easy data access.

The architecture of MongoDB is around document database principles. The data can be queried in an ad-hoc way, with the data persisted in a nested way. This database also, like most NoSQL databases enforces no schema, however can have specific document fields that can be queried off of.

***Who is using it?***

- Foursquare
- bit.ly
- CERN for collecting data from the large Hadron Collider
- …others…

## Redis

<http://redis.io/>

Redis stands for Remote Dictionary Service. The most common capability Redis is known for, is blindingly fast speed. This speed comes from trading durability. At a base level Redis is a key-value store, however sometimes classifying it isn’t straight forward.

Redis is a key-value store, and often referred to as a data structure server with keys that can be string, hashes, lists, sets and sorted sets. Redis is also, stepping away from only being a key-value store, into the realm of being a publish-subscribe and queue stack. This makes Redis one very flexible tool in the tool chest.

***Who is using it?***

- Blizzard (You know, that World of Warcraft game maker)  😉
- Craigslist
- flickr
- …others…

## Couch

<http://couchdb.apache.org/>

Another Apache Project, CouchDB is the idealized JSON and REST document database. It works as a document database full of key-value pairs with the values a set number of types including nested with other key-value objects.

The primary mode of querying CouchDB is to use incremental mapreduce to produce indexed views.

One other interesting characteristic about CouchDB is that it’s built with the idea of a multitude of deployment scenarios. CouchDB might be deployed to some big servers or may be a mere service running on your Android Phone or Mac OS-X Desktop.

Like many NoSQL options CouchDB is RESTful in operation and uses JSON to send data to and from clients.

The Node.js Community also has an affinity for Couch since NPM and a lot of the capabilities of Couch seem like they’re just native to JavaScript. From the server aspect of the database to the JSON format usage to other capabilities.

***Who uses it?***

- NPM – Node Package Manager site and NPM uses CouchDB for storing and providing the packages for Node.js.

## Couchbase (UPDATED January 18th)

Ok, I realized I’d neglected to add [Couchbase](http://www.couchbase.com/) (thus the Jan 18th update), which is an open source and interesting solution built off of Membase and Couch. Membase isn’t particularly a distributed database, or database, but between it and couch joining to form Couchbase they’ve turned it into a distributed database like couch except with some specific feature set differences.

A lot of the core architecture features of Couch are available, but the combination now adds auto-sharding clusters, live/hot swappable upgrades and changes, memchaced APIs, and built in data caching.

***Who uses it?***

- Linkedin
- Orbitz
- Concur
- …and others…

## Neo4j

<http://www.neo4j.org/>

Neo4j steps away from many of the existing NoSQL databases with its use of a graph database model. It stored data as a graph, mathematically speaking, that relates to the other data in the database. This database, of all the databases among the NoSQL and SQL world, is very whiteboard friendly.

Neo4j also has a varied deployment model, being able to deploy to a small or large device or system. It has the ability to store dozens of billions of edges and nodes.

***Who is using it?***

- Accenture
- Adobe
- Lufthansa
- Mozilla
- …others…

## Riak

Riak is a key-value, distributed, fault tolerant, resilient database written in Erlang.  It uses the Riak Core project as a codebase for the distributed core of the system. I further explained Riak, since yes, I work for Basho who are the makers of Riak, in a separate blog entry “[Riak is… A Big List of Things](/2013/01/11/riak-is-a-whole-big-list-of-things/)“. So for a description of the features around Riak check that out.

***Who is using Riak?***

- Best Buy
- Github
- Voxer
- Yammer
- Comcast
- […many others…](http://basho.com/company/production-users/)

## In Summary

One of the things you’ll notice with a lot of these databases and the NoSQL movement in general is that it originated from companies needing to go “web scale” and RDBMSs just couldn’t handle or didn’t meet the specific requirements these companies had for the data. NoSQL is in no way a replacement to relational or SQL databases except in these specific cases where need is outside of the capability or scope of SQL & Relational Databases and RDBMSs.

Almost every NoSQL database has origins that go pretty far back, but the real impetus and push forward with the technology came about with key efforts at Google and Amazon Web Services. At Google it was with [***BigTable Paper***](/wp-content/uploads/2013/01/bigtable-osdi06.pdf) and at Amazon Web Services it was with the [***Dynamo Paper***](/wp-content/uploads/2012/12/amazon-dynamo-sosp2007.pdf). As time moved forward with the open source community taking over as the main innovator and development model around big data and the NoSQL database movement. Today the Apache Project has many of the projects under its guidance along with other companies like Basho and 10gen.

In the last few years, many of the larger mainstays of the existing database industry have leapt onto the bandwagon. Companies like *Microsoft, Dell, HP* and *Oracle* have made many strategic and tactical moves to stay relevant with this move toward big data and nosql databases solutions. However, the leadership is still outside of these stalwarts and in the hands of the open source community. The related companies and organizations that are focused on that community such as 10gen, Basho and the Apache Organization still hold much of the future of this technology in the strategic and tactical actions that they take since they’re born from and significant parts of the community itself.

For an even larger list of almost every known NoSQL Database in existence check out [NoSQL Database .org](http://nosql-database.org/).
