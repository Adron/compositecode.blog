---
title: Scaling PostgreSQL + Top 12 Curated Posts
date: 2021-05-11 11:57:24 -0700
last_modified_at: 2021-05-11 11:58:01 -0700
permalink: /2021/05/11/scaling-postgresql/
slug: scaling-postgresql
wp_id: 63779
original_url: https://compositecode.blog/2021/05/11/scaling-postgresql/
categories:
- Databases
tags:
- postgres
- scaling
- sql
excerpt: There are two main ways to scale data storage, especially databases, and the resources available to store and process that data.
image: /wp-content/uploads/2020/11/databases.jpg
---

A video introduction into the basics of scaling a relational database like PostgreSQL.

<iframe allowfullscreen="true" class="youtube-player" height="486" loading="lazy" sandbox="allow-scripts allow-same-origin allow-popups allow-presentation allow-popups-to-escape-sandbox" src="https://www.youtube.com/embed/Y19kKj2J6vc?version=3&amp;rel=1&amp;showsearch=0&amp;showinfo=1&amp;iv_load_policy=1&amp;fs=1&amp;hl=en-US&amp;autohide=2&amp;wmode=transparent" style="border:0;" width="863"></iframe>

There are two main ways to scale data storage, especially databases, and the resources available to store and process that data.

> *Horizontal Scaling (scale-out): This is done through adding more individual machines in some way, creating a cluster for the database to operate. Various databases handle this in different ways ranging from a system like a distributed database, which is specifically built to scale horizontally, to relational databases which require different strategies like sharding the data itself.*

> *Vertical Scaling (scale-up): This includes increasing the individual system resources allocated to a database on a single vertically integrated machine, such as the CPU or number of CPUs, memory, and disk or disks.*

For horizontal scaling the approach often requires things like possible sharding of the data across multiple databases and then pooling those resources together via connection pooling, load balancers, and other infrastructure resources to direct the correct requests and traffic at the right sharded database resource.

Sometimes from a purely process-centric horizontal scaling perspective, we just need more query and processing power but the data can be stored on a singular machine. In this case, we might implement a proxy to direct traffic across some bouncers that would then get requests and responses to and from the individual machines.

Vertical scaling often requires new hardware and a migration to the larger machine. Sometimes however it may just require more CPU, RAM, or more drive storage. If it is a singular need it often can be met by adding one of those elements or changing out one. For example, if a databases is continually hitting the peak processing of the CPUs to handle queries, one might be able to just add another processor or change the processor to a faster processor or one with more cores to process with. In the case of memory being overloaded, the same for that, simply increase the maximum memory in the system. Of course, the underlying limitations of vertical scaling always come up when you already have the fastest CPU or the memory is already maxed out. In that situation one might need to think about horizontally scaling as described in the previous described example.

The following is a top X list of blog entries that cover the expansion of the topic in many ways. I’ve found these (along with more than a few others) very useful in my own efforts around scaling Postgres (and other databases).

1. [Vertically Scaling PostgreSQL](https://pgdash.io/blog/scaling-postgres.html)
2. [Vertically Scale Your PostgreSQL Infrastructure w/ pgpool -3- Adding Another Standby](https://blog.dbi-services.com/vertically-scale-your-postgresql-infrastructure-with-pgpool-3-adding-another-standby/)
3. [Vertically scale your PostgreSQL infrastructure with pgpool — 2 — Automatic failover and reconfiguration](https://blog.dbi-services.com/vertically-scale-your-postgresql-infrastructure-with-pgpool-2-automatic-failover-and-reconfiguration/)
4. [How well can PostgreSQL scale horizontally?](https://www.quora.com/How-well-can-PostgreSQL-scale-horizontally?share=1)
5. [How to Horizontally Scale Your Postgres Database Using Citus](https://dzone.com/articles/how-to-horizontally-scale-your-postgres-database-using-citus)
6. [Horizontal scalability with Sharding in PostgreSQL — Where it is going Part 1 of 3](https://www.highgo.ca/2019/08/08/horizontal-scalability-with-sharding-in-postgresql-where-it-is-going-part-1-of-3/)
7. [Lessons learned scaling PostgreSQL database to 1.2bn records/month](https://gajus.medium.com/lessons-learned-scaling-postgresql-database-to-1-2bn-records-month-edc5449b3067)
8. [IDEAS FOR SCALING POSTGRESQL TO MULTI-TERABYTE AND BEYOND](https://www.cybertec-postgresql.com/en/ideas-for-scaling-postgresql-to-multi-terabyte-and-beyond/)
9. [Scaling PostgreSQL Using Connection Poolers & Load Balancers](https://severalnines.com/database-blog/scaling-postgresql-using-connection-poolers-load-balancers)
10. [Vertically Scaling PostgreSQL](https://pgdash.io/blog/scaling-postgres.html)
11. [Scaling PostgreSQL for Large Amounts of Data](https://severalnines.com/database-blog/scaling-postgresql-large-amounts-data)
12. [Scaling Postgres](https://www.scalingpostgres.com/)
