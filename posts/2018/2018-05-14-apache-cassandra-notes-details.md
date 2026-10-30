---
title: 'Cassandra: Quick Installation & Download Notes & Details'
date: 2018-05-14 14:55:16 -0700
last_modified_at: 2018-05-14 14:56:31 -0700
permalink: /2018/05/14/apache-cassandra-notes-details/
slug: apache-cassandra-notes-details
wp_id: 13886
original_url: https://compositecode.blog/2018/05/14/apache-cassandra-notes-details/
categories:
- Unknown Code Ramblings
tags: []
excerpt: A collection of notes and details. There’s plenty of details and docs out there, which I’ll reference a few below to get started with Cassandra. The goal with these notes is to provide a kind of summarized punch list of items to quickly get started around Cassandra/Datastax Enterprise 6 (DSE6). I’ll have a number of …
image: /wp-content/uploads/2018/05/datastaxandcassandra.jpg
---

A collection of notes and details. There’s plenty of details and docs out there, which I’ll reference a few below to get started with Cassandra. The goal with these notes is to provide a kind of summarized punch list of items to quickly get started around Cassandra/Datastax Enterprise 6 ([*DSE6*](https://www.datastax.com/products/datastax-enterprise-6)). I’ll have a number of additional pieces coming real soon, as I’ve got some geeky experiments and related surprise implementations I’m putting together in the very near future. Let’s just say there will likely be Lego, trains, and many nodes among other fascinating elements coming together to make it happen! *Enjoy the start…*

## The Big Details

- Who – Avinash Lakshman ([@hedvigeng](https://twitter.com/hedvigeng)) and Prashant Malik ([@pmalik](https://twitter.com/pmalik)) originally developed Cassandra at Facebook for inbox search.
- ![2000px-Cassandra_logo.svg](/wp-content/uploads/2018/05/2000px-cassandra_logo-svg.png)What – [Apache Cassandra](http://cassandra.apache.org/) is a highly scalable, high-performance distributed database built with the ability to handle large amounts of structured data decentralized across many servers. In service of that goal Cassandra provides a highly available system without a single point of failure.
- Where – Apache Cassandra can be found on the [Apache Cassandra Site](http://cassandra.apache.org/) and the code in the [Cassandra Github Repo](https://github.com/apache/cassandra).
- When – Cassandra was released as open source by Facebook in 2008, and became an Apache top-level project in February of 2010.
- Why – When you want no fixed schema, massive scale, huge storage capability options, eventually consistent, fault-tolerant, dynamic/elastic scalability, fast linear-scale performance, always on highly available, and related features.

## Distributed Databases

- [According to Wikipedia](https://en.wikipedia.org/wiki/Distributed_database)
- Read a past entry of mine and saw how far current distributed systems have come since [suggestions on how to backup Riak](/2013/05/08/distributed-databases-issue-001/) were commonplace and found a good collection of info and links to information about [consistent hashing](/2013/05/25/consistent-hashing-learning-about-distributed-databases-issue-002/) I did. It’s an old post (circa 2013 so some of the poor ole’ Riak links don’t work, but the [wikipedia](https://en.wikipedia.org/wiki/Consistent_hashing) article is good and the general content is good.)
- Other databases in the distributed systems realm: [Aerospike](https://en.wikipedia.org/wiki/Aerospike_database), [ArangoDB](https://en.wikipedia.org/wiki/ArangoDB), [Couchbase (Sort of derived out of Couch, but not really)](https://en.wikipedia.org/wiki/Couchbase_Server), [FoundationDB](https://en.wikipedia.org/wiki/FoundationDB), [NuoDB](https://en.wikipedia.org/wiki/NuoDB) are some of the others out there, among many. Often support is minimal in comparison however.

## Getting Started, Installing, Configuration, Setup, & Start

- [Cassandra Download and Installation](http://cassandra.apache.org/download/)
- [DataStax Downloads and Installation](https://academy.datastax.com/downloads)

## CQL – Cassandra Query Language

- [DataStax Docs on CQL](https://docs.datastax.com/en/cql/3.1/cql/cql_intro_c.html)
- [Apache Cassandra Docs on CQL](http://cassandra.apache.org/doc/latest/cql/)

## Intro & Architecture of Cassandra References

- [Using Apache Cassandra – A few things before you start](https://hackernoon.com/using-apache-cassandra-a-few-things-before-you-start-ac599926e4b8)
- [A Quick Introduction to Apache Cassandra](https://www.sitepoint.com/a-quick-introduction-to-apache-cassandra/)

This is merely the beginning of the blogging, projects, and notes, if you’d like to bookmark where I’ll be linking ***all*** of my [Datastax + Cassandra notes](/cassandra/), check out my [Cassandra root documentation & links page](/cassandra/).
