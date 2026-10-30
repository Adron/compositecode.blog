---
title: Cassie Schema Migrator >> CaSMa
date: 2019-06-11 08:57:06 -0700
last_modified_at: 2019-06-11 13:25:02 -0700
permalink: /2019/06/11/cassie-schema-migrator-casma/
slug: cassie-schema-migrator-casma
wp_id: 15883
original_url: https://compositecode.blog/2019/06/11/cassie-schema-migrator-casma/
categories:
- .NET Bits
- c#
tags:
- casma
- cassie schema migrator
- code
- coding
- database
- distributed databases
- multi-model
- open source
- open source software
- programming
- schema migration
- software development
excerpt: 'A few weeks back I started working on a schema migration tool for Apache Cassandra and DataStax Enterprise. Just for context, here are the short definitions of what each of the elements of CaSMa are. Apache Cassandra Definition: Apache Cassandra is a free and open-source, distributed, wide column store, NoSQL database management system designed to …'
image: /wp-content/uploads/2019/03/devops-days-vancouver-architecture-guidance-venomous-database-reliability-engineering-1-1.jpg
---

A few weeks back I started working on a schema migration tool for [Apache Cassandra](http://cassandra.apache.org/) and [DataStax Enterprise](https://www.datastax.com/products/datastax-enterprise). Just for context, here are the short definitions of what each of the elements of CaSMa are.

- [![cstar-icon](/wp-content/uploads/2019/06/cstar-icon.png)Apache Cassandra](https://en.wikipedia.org/wiki/Apache_Cassandra)
  - *Definition*: Apache Cassandra is a free and open-source, distributed, wide column store, NoSQL database management system designed to handle large amounts of data across many commodity servers, providing high availability with no single point of failure.
  - *History*: Avinash Lakshman, one of the authors of Amazon’s Dynamo, and Prashant Malik initially developed Cassandra at Facebook to power the Facebook inbox search feature. Facebook released Cassandra as an open-source project on Google code in July 2008. In March 2009 it became an Apache Incubator project. On February 17, 2010 it graduated to a top-level project. Facebook developers named their database after the Trojan mythological prophet Cassandra, with classical allusions to a curse on an oracle.
- [![dse-logo](/wp-content/uploads/2019/06/dse-logo.png)DataStax Enterprise](https://www.datastax.com/products/datastax-enterprise)
  - *Definition*: DataStax Enterprise, or routinely just referred to as DSE, is an extended version of Apache Cassandra with multi-model capabilities around graph, search, analytics, and other features like security capabilities and a core data engine 2x speed improvement.
  - *History*: DataStax was formed in 2009 by Jonathan Ellis and Matt Pfeil and originally named Riptano. In 2011 Riptano changes names to DataStax. For more history check out the [Wikipedia page](https://en.wikipedia.org/wiki/DataStax) or [company page](https://www.datastax.com/resources/infographic/the-history-of-apache-cassandra) for a timeline of events.
- [![command-tools](/wp-content/uploads/2019/06/command-tools.png)Schema Migration](https://en.wikipedia.org/wiki/Schema_migration)
  - *Definition*:In software engineering, schema migration (also database migration, database change management) refers to the management of incremental, reversible changes to relational database schemas. A schema migration is performed on a database whenever it is necessary to update or revert that database’s schema to some newer or older version. Migrations are generally performed programmatically by using a schema migration tool. When invoked with a specified desired schema version, the tool automates the successive application or reversal of an appropriate sequence of schema changes until it is brought to the desired state.
  - Addition reference and related materials:
    - [Evolutionary Database Design](https://martinfowler.com/articles/evodb.html)
    - [Evolutionary Database Design Wikipedia Page](https://en.wikipedia.org/wiki/Evolutionary_database_design)

[![iconmonstr-twitch-5](/wp-content/uploads/2019/03/iconmonstr-twitch-5.png)](https://www.twitch.tv/datastaxdevs/)Over the next dozen weeks or so as I work on this application via the [DataStax Devs Twitch](https://www.twitch.tv/datastaxdevs/) stream ([next coding session events list](https://www.twitch.tv/events/rCm6x_LkSuOvT5vFWMI0EA)) I’ll also be posting some blog posts in parallel about schema migration and my intent to expand on the notion of schema migration specifically for multi-model databases and larger scale NoSQL systems; namely Apache Cassandra and DataStax Enterprise. Here’s a shortlist for the next three episodes;

- [DataStax’s Apache Cassandra & DSE C# Hour – Ep 11](https://www.twitch.tv/events/rCm6x_LkSuOvT5vFWMI0EA)
- [DataStax’s Apache Cassandra & DSE C# Hour – Ep 12](https://www.twitch.tv/events/ZLziYH-WS4CrpNLUYdU30Q)
- [DataStax’s Apache Cassandra & DSE C# Hour – Ep 13](https://www.twitch.tv/events/0q0doXJXSvOgAq1oR91E5Q)

The other important pieces include the current code base on Github, the continuous integration build, and the tasks and issues.

- Github Repo [CassieSchemaMigrator](https://dev.azure.com/adronhall-datastax/cassie-schema-migrator/_build/)
- CI Build, Tasks, Good First Issues and Issues:
  - [![](https://dev.azure.com/adronhall-datastax/cassie-schema-migrator/_apis/build/status/Adron.CassieSchemaMigrator?branchName=master)](https://dev.azure.com/adronhall-datastax/cassie-schema-migrator/_build/results)
  - [![GitHub issues by-label](https://camo.githubusercontent.com/1f6ea7b6e12af6d30f0a8c738fdd74bf71db1ef5/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f6973737565732d7261772f4164726f6e2f436173736965536368656d614d69677261746f722f676f6f64253230666972737425323069737375652e737667)](https://github.com/Adron/CassieSchemaMigrator/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+issue%22)
  - [![GitHub issues](https://camo.githubusercontent.com/b9a7c97bf38aa76db63c8cc81191aea7d3b24665/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f6973737565732f4164726f6e2f436173736965536368656d614d69677261746f722e737667)](https://github.com/Adron/CassieSchemaMigrator/issues)

Alright, now that all the collateral and context is listed, let’s get into at a high level what this is all about.

## CaSMa’s Mission

Schema migration is a powerful tool to get a project on track and consistently deployed and development working against the core database(s). However, it’s largely entrenched in the relational database realm. This means it’s almost entirely focused on a schema with the notions of primary and foreign keys, the complexities around many to many relationships, indexes, and other errata that needs to be built consistently for a relational database. Many of those things need to be built for a distributed columnar store, key value, graph, time series, or a million other possibilities too. However, in our current data schema world, that tooling isn’t always readily available.

The mission of CaSMa is to first resolve this gap around schema migration, first and foremost for Apache Cassandra and prospectively in turn for DataStax Enterprise and then onward for other database systems. Then the mission will continue around multi-model systems that should, can, and ought to take advantage of schema migration for graph, and related schema modeling. At some point the mission will expand to include other schema, data, and state management focused around software development and data needs within that state

As progress continues I’ll publish additional posts here on the different data model concepts and nature behind various multi-model database options. These modeling options will put us in a position to work consistently, context based, and seamlessly with ongoing development efforts. In addition to all this, there will be the weekly Twitch sessions where I’ll get into coding and reviewing what coding I’ve done off camera too. Check those out on the [DataStax Devs Channel](https://www.twitch.tv/).

If you’d like to get into the project and help out just ping me via Twitter [@Adron](https://twitter.com/Adron) or message me [here](/contact/).
