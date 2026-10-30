---
layout: page
title: 'SACON Proposal: Relational to Distributed Database Migration & Data Modeling'
date: 2019-01-28 15:24:24 -0800
last_modified_at: 2019-01-28 16:15:16 -0800
permalink: /sacon-proposal-relational-to-distributed-database-migration-data-modeling/
slug: sacon-proposal-relational-to-distributed-database-migration-data-modeling
wp_id: 15277
original_url: https://compositecode.blog/sacon-proposal-relational-to-distributed-database-migration-data-modeling/
---

**Title:** Relational to Distributed Database Migration & Data Modeling

**Description:** Migration of databases and the concerns around data-schema and modeling.

**Abstract:** With data growing every day, it’s routine to exceed the capabilities of standard relational databases and find yourself needing to migrate to a linearly scalable distributed database (like Apache Cassandra, TiDB, FoundationDB, CosmosDB, Dynamo DB, or other distributed database). In this talk I’ll present many of the steps that need to be taken to migrate a relational model to a distributed database model, with some focus around a columnar store. Once several of the various migration concerns are detailed, I’ll step through various ways to mitigate risk and initiate such a migration from one database type to another.

**Who is this presentation for:** Database Administrator (DBA), Architect, Data Architect, Data Scientist

**Prereqs:**

1. A basic level of SQL Databases and some basics around relational modeling in databases.
2. A basic understanding of scaling a vertical systems (i.e. via hardware CPU, RAM, Drive, etc) vs. horizontal scaling (i.e. add new machine, repeat).
