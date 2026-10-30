---
title: Let’s Talk Top 7 Options for Database Gumbo
date: 2019-01-04 12:01:56 -0800
last_modified_at: 2019-01-09 18:20:30 -0800
permalink: /2019/01/04/lets-talk-top-7-options-for-database-gumbo/
slug: lets-talk-top-7-options-for-database-gumbo
wp_id: 15155
original_url: https://compositecode.blog/2019/01/04/lets-talk-top-7-options-for-database-gumbo/
categories:
- Databases
- Distributed Things
- The Future
tags:
- apache cassandra
- cassandra
- database gumbo
- databases
- datastax enterprise
- dse
- dynamodb
- elastic
- elasticsearch
- oracle
- postgres
- postgresql
- redis
- sql server
- sqlite
excerpt: When one starts to dig into databases things get really complex really fast. There’s not only a whole plethora of database companies and projects, but database types, storage engines, and other options and functionality to choose from. One place to get a start is just to take a look at the crazy long list of …
---

When one starts to dig into databases things get really complex really fast. There’s not only a whole plethora of database companies and projects, but database types, storage engines, and other options and functionality to choose from. One place to get a start is just to take a look at the [crazy long list of databases on db-engines](https://db-engines.com/en/ranking). In this post I’m going to take a look at a few of the top database engines to create a starting point – which I’ll reference – for future [video streaming coding sessions (follow me @ twitch.tv/adronhall)](https://www.twitch.tv/adronhall).

## My Options for Database Gumbo

1. Apache Cassandra / DataStax Enterprise
2. Postgresql
3. SQL Server
4. Elasticsearch
5. Redis
6. SQLite
7. Dynamo DB

## The Reasons

Ok, so the list is as such, and as stated it’s my list. There are a lot of databases, and of course some are still more used such as Oracle. However here’s some of the logic and reasoning behind my choices above.

**Oracle**

First off I feel like I need to broach the Oracle topic. Mostly because of their general use in industry. I’m not doing anything with Oracle now, nor have I for years for a long, long, ***LONG*** list of reasons. Using their software tends to be buried in bureaucratic, oddly broken and unnecessary usage today anyway. They use predatory market tactics, completely dishonorable approach to sales and services, as well as threatening and suing people for doing benchmarks, and a host of other practices. In face to face experiences, Oracle tends to give off experiences, that Lawrence from Office Space would say, “*naw man, I think you’d get your ass kicked for that!*” and I agree. Oracle’s practices are too often disgusting. But even from the purely technical point of view, the Oracle Database and ecosystem itself really isn’t better than other options out there. It is indeed a better, more intelligently strategic and tactical option to use a number of alternatives.

<iframe allowfullscreen="true" class="youtube-player" height="486" loading="lazy" sandbox="allow-scripts allow-same-origin allow-popups allow-presentation allow-popups-to-escape-sandbox" src="https://www.youtube.com/embed/WDgq-K2oYLo?version=3&amp;rel=1&amp;showsearch=0&amp;showinfo=1&amp;iv_load_policy=1&amp;fs=1&amp;hl=en-US&amp;autohide=2&amp;wmode=transparent" style="border:0;" width="863"></iframe>

**Apache Cassandra / DataStax Enterprise**

This combo has multiple reasons and logic to be on the list. First and foremost, much of my work today is using DataStax Enterprise (DSE) and Apache Cassandra since I work for DataStax. But it’s important to know I didn’t just go to DataStax because I needed a job, but because I chose them (and obviously they chose me by hiring me) because of the team and technology. Yes, they pay me, but it’s very much a two way street, I advocate Cassandra and DSE because I personally know the tech is top tier and solid.

On the fact that Apache Cassandra is top tier and solid, it is simply the remaining truly masterless distributed database that provides a linear path of scalability on the market that you can use, buy support for, and is actually actively and knowingly maintained not just by DataStax but by members of the community. One could make an argument for MongoDB but I’ll maybe elaborate on that in the future.

In addition to being a solid distributed database there are capabilities inherent in Apache Cassandra because of the data types and respective the CQL (Cassandra Query Language) that make it a great database to use too. DataStax Enterprise extends that to provide spatial (re: GIS/Geo Data/Queries), graph data, analytics engine, and more built on other components like SOLR and related technology. Overall a great database and great prospective combinations with the database.

**Postgresql**

Postgres is a relational database that has been around for a long time. It’s got some really awesome features like native JSON support, which I’m a big fan of. But I digress, there’s tons of other material that lays out thoroughly why to use Postgres which I very much agree with.

- [How I Approach Software Development and Why I Prefer Postgresql to mysql](https://www.goetas.com/blog/how-i-approached-software-development-and-why-i-prefer-postgresql-to-mysql/)
- [Why Postgres 5 Years Later](http://www.craigkerstiens.com/2017/04/30/why-postgres-five-years-later/) is a great list of reasons!

Just from the perspective of the extensive and rich data types Postgres is enough to be put on this list, but considering there are a lot of reasons around multi-tenancy, scalability, and related characteristics that are mostly unique to Postgres it’s held a solid position.

**SQL Server**

This one is on my list for a few reasons that have nothing to do with features or capabilities. This is the first database I was responsible for in its entirety. Administration, queries, query tuning, setup, and developer against with the application tier. I think of all my experience, this database I’ve spent the most time with, with Apache Cassandra being a close second, then Postgres and finally Riak.

*Kind of a pattern there eh? Relational, distributed, relational, distributed!*

The other thing about SQL Server however is the integrations, tooling, and related development ecosystem around SQL Server is above and beyond most options out there. Maybe, with a big maybe, Oracle’s ecosystem might be comparable but the pricing is insanely different. In that SQL Server basically can carry the whole workload, reporting, ETL, and other feature capabilities that the Oracle ecosystem has traditionally done. Combine SQL Server with SSIS (SQL Server Integration Services), SSRS (SQL Server Reporting Services), and other online systems like Azure’s SQL Database and the support, tooling, and ecosystem is just massive. Even though I’ve had my ins and outs with Microsoft over the years, I’ve always found myself enjoying working on SQL Server and it’s respective tooling options and such. It’s a feature rich, complete, solidly, and generally well performing relational database, full stop.

**Elasticsearch**

Ok, this is kind of a distributed database of sorts but focused more exclusively (not totally since it’s kind of expanded its roles) search engine. Overall I’ve had good experiences with Elasticsearch and it’s respective ELK (or Elastic ecosystem) of tooling and such, with some frustrating flakiness here and there over the years. Most of my experience has come from an operational point of view with Elasticsearch. I’ve however done a fair bit of work over the years in supporting teams that are doing actual software development against the system. I probably won’t write a huge amount about Elasticsearch in the coming months, but I’ll definitely bring it up at certain times.

**Redis / SQLite / DynamoDB**

These I’ll be covering in the coming months. For Redis and DynamoDB I have wanted to dig in for some comparison analysis from the perspective of implementing data tiers against these databases, where they are a good option, and determining where they’re just an outright bad option.

For SQLite I’ve used it on and off for many years, but have wanted to sit down and just learn it and try out some of its features a bit more.
