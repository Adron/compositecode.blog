---
title: Survey of Go Libraries for Database Work
date: 2019-03-27 16:50:33 -0700
last_modified_at: 2019-03-27 16:50:33 -0700
permalink: /2019/03/27/survey-of-go-libraries-for-database-work/
slug: survey-of-go-libraries-for-database-work
wp_id: 15568
original_url: https://compositecode.blog/2019/03/27/survey-of-go-libraries-for-database-work/
categories:
- Architecture
- cassandra
- Databases
- datastax enterprise
- Distributed Things
tags:
- apache
- apache cassandra
- cassandra
- data science
- mysql
- postgresql
- sql server
excerpt: Over the past few months I’ve picked up a number of libraries in the Go ecosystem to help me get work done around database engineering. These libraries are ones that I have used to do a range of work primarily around Apache Cassandra, DataStax Enterprise, PostgreSQL, and to a lesser degree MS SQL Server, MySQL, …
image: /wp-content/uploads/2019/03/devops-days-vancouver-architecture-guidance-venomous-database-reliability-engineering-8.jpg
---

Over the past few months I’ve picked up a number of libraries in the Go ecosystem to help me get work done around database engineering. These libraries are ones that I have used to do a range of work primarily around [Apache Cassandra](http://cassandra.apache.org/), [DataStax Enterprise](https://www.datastax.com/products/datastax-enterprise), [PostgreSQL](https://www.postgresql.org/), and to a lesser degree [MS SQL Server](https://www.microsoft.com/en-us/sql-server/default.aspx), [MySQL](https://www.mysql.com/), and others. The following is a survey of libraries that I’ve found to be pretty solid for getting the job done.

![DevOps Days Vancouver - Architecture Guidance - Venomous Database Reliability Engineering (5)](/wp-content/uploads/2019/03/devops-days-vancouver-architecture-guidance-venomous-database-reliability-engineering-5-1.jpg)

I’ve broken the follow tooling libraries out into the following categories:

- **Observability, Monitoring, & Insight** – I created this section, and added libraries to it based specifically on the specific and peculiarly pedantic nature of observability in light of monitoring that work to provide insight into one’s applications they’re responsible for. For additional information about observability check out the Wikipedia article on the topic [observability](https://en.wikipedia.org/wiki/Observability), it’s a great starting point. For monitoring however it gets more specific with a breakdown of monitoring types: [application performance monitoring](https://en.wikipedia.org/wiki/Application_performance_management), [network monitoring](https://en.wikipedia.org/wiki/Network_monitoring), [system monitoring](https://en.wikipedia.org/wiki/System_monitor), and [business transaction monitoring](https://en.wikipedia.org/wiki/Business_transaction_management). The libraries in this section apply to some or all of the criteria in this definitions.
- **Data Schema Migration** – Managing one’s data schema for a database, even really, truly, honestly if you have a schema-less system you still need to manage the underlying schema at some level.
- **Flow, Pipelines, Extraction, Transformation, and Loading** – This section is mutative in the sense that it includes a lot of various types of libraries that have a very wide range of work to do and they offers a plethora of ways to do this work. Creating pipelines, to flow sequences, to extraction and transformation, to standard bulk loading. These libraries provide ways to get the data where you need it when you need it there in effective and reliable ways.
- **Database Backup Libraries** – There are a zillion different things to maintaining effective and useful database backups; onsite storage, offsite storage, rotation periods, transmission & security control, scheduling, full or differential, and other topics of concern. One of the most important and often overlooked aspect of database backups is actually *restoring* the database from backup! These libraries can be used to get those backups, automate, and implement restoration of data in a more seamless way.
- **Database Drivers** – At the core of any programmable automation of databases, one needs to have some way to connect to and work with the databases they’re automating, that’s where database drivers come into play. For Go, there’s a ton of support on every relatively known database in existence. MS SQL, Apache Cassandra, PostgreSQL, and dozens more!

![DevOps Days Vancouver - Architecture Guidance - Venomous Database Reliability Engineering](/wp-content/uploads/2019/03/devops-days-vancouver-architecture-guidance-venomous-database-reliability-engineering-5.jpg)

[**Veneur**](https://github.com/stripe/veneur) – Largely used by and originating from Stripe. This library works as a distributed, fault tolerant pipeline for data emitted from run time on systems and services throughout your environment. It has server implementations of the [DogStatsD](https://docs.datadoghq.com/developers/dogstatsd/) protocol or [SSF](https://github.com/stripe/veneur/tree/master/ssf) ([Sensor Sensibility Format](https://github.com/stripe/veneur/tree/master/ssf)) for aggregating metrics and sending these metrics for storage or via sinks to various other systems. The system can also works up histograms, sets, and counters as global aggregator.

TLDR;

> Veneur is a convenient sink for various observability primitives with lots of outputs!

**[Honeycomb.io](https://www.honeycomb.io/)** – Honeycomb I did some work for back in February of 2018 and gotta say I loved the team. Charity [@mipsytipsy](https://twitter.com/mipsytipsy), Christine [@cyen](https://twitter.com/cyen), Ben [@maplebed](https://twitter.com/maplebed) and crew are tops! Friendly, wildly smart, and humble thrown in for good measure. With that said, I’m also a fan of the product. It’s a solid high cardinality, query and event intake system for observability. There are libraries for Go as well as others, and it’s pretty easy to use the library to [setup ingest](https://github.com/honeycombio/libhoney-go) for appropriately [instrumented applications](https://github.com/honeycombio/beeline-go).

TLDR;

> Honeycomb.io is a Saas tool with available libraries for Go to provide observability insight and data collection for your applications!

**[OpenCensus](https://opencensus.io/)** – This framework and toolset provides ways to get telemetry out of your services. Currently  there are libraries for a number of languages that allow you to capture, manipulate, and export metrics and distributed traces to your data store of choice. The key idea is that OpenCensus works via tracing through the course of events in an application and that data is logged for awareness, insight, and thus observability of your systems.

TLDR;

> OpenCensus is a library that provides ways to gather telemetry for your services and store it in your choice of a location.

**[RxGo](https://github.com/ReactiveX/RxGo)** – This library is a reactive extensions built for Go. This one is as much a programming concept as it is a way to enhance and specifically focus on observability, so let’s take a look at the intro example they’ve got on the actual repo [README.md](https://github.com/ReactiveX/RxGo/blob/master/README.md) itself.

> [ReactiveX](http://reactivex.io/), or Rx for short, is an API for programming with observable streams. This is a ReactiveX API for the Go language.
>
> *ReactiveX* is a new, alternative way of asynchronous programming to callbacks, promises and deferred. It is about processing streams of events or items, with events being any occurrences or changes within the system.
>
> In Go, it is simpler to think of a observable stream as a channel which can `Subscribe` to a set of handler or callback functions.
>
> The pattern is that you `Subscribe` to an `Observable` using an `Observer`:
>
> ```go
> subscription := observable.Subscribe(observer)
> ```
>
> An `Observer` is a type consists of three `EventHandler` fields, the `NextHandler`, `ErrHandler`, and `DoneHandler`, respectively. These handlers can be evoked with `OnNext`, `OnError`, and `OnDone` methods, respectively.
>
> The `Observer` itself is also an `EventHandler`. This means all types mentioned can be subscribed to an `Observable`.
>
> ```go
> nextHandler := func(item interface{}) interface{} {
>     if num, ok := item.(int); ok {
>         nums = append(nums, num)
>     }
> }
>
> // Only next item will be handled.
> sub := observable.Subscribe(handlers.NextFunc(nextHandler))
> ```

TLDR;

> RxGo are the reactive extensions that make it easier to go full scale and spectrum observability, with significantly greater insight into your applications over time and the events they execute.

![DevOps Days Vancouver - Architecture Guidance - Venomous Database Reliability Engineering (1)](/wp-content/uploads/2019/03/devops-days-vancouver-architecture-guidance-venomous-database-reliability-engineering-1-1.jpg)

[**Go-Migrate**](https://github.com/golang-migrate/migrate) – This library is written in Go and handles data schema migrations for a significant number of databases; PostgreSQL, MySQL, SQLite, RedShift, Neo4j, CockroadDB, and that’s just a few.

*Example:*

```
migrate -source file://path/to/migrations -database postgres://localhost:5432/database up 2
```

TLDR;

> Go-Migrate is an open source library that can be used via CLI or in code to manage all your schema migration needs.

[**Gocqlx Migrate**](https://github.com/scylladb/gocqlx/tree/master/migrate) – This library primarily provides extensions to the Go CQL driver library, and one of those extensions specifically is a data-schema migration functionality.

*Example:*

```
package main

import (
    "context"

    "github.com/scylladb/gocqlx/migrate"
)

const dir = "./cql"

func main() {
    session := CreateSession()
    defer session.Close()

    ctx := context.Background()
    if err := migrate.Migrate(ctx, session, dir); err != nil {
        panic(err)
    }
}
```

TLDR;

> Gocqlx Migrate is a feature of the Gocqlx extensions library that can be used for schema migrations from within code.

![DevOps Days Vancouver - Architecture Guidance - Venomous Database Reliability Engineering (2)](/wp-content/uploads/2019/03/devops-days-vancouver-architecture-guidance-venomous-database-reliability-engineering-2-1.jpg)

[Pachyderm](https://pachyderm.io/) – ([Open Source Repo](https://github.com/pachyderm/pachyderm)) A pachyderm is

> a very large mammal with thick skin, especially an elephant, rhinoceros, or hippopotamus.

So it is kind of a fitting name for this library. The library, the project itself, has found funding and bills itself as “*Scalable, Reproducible Data Science*“. I’ve used it minimally myself, but find it continually popping up on my “*use this tool because you’ll need a ton of the features*” list.

TLDR;

> Pachyderm is an open source library, and paired capital funded company, that does indeed provide scalable, reproducible data science in addition to being a great library for your ETL and related data management needs.

[Reflow](https://github.com/grailbio/reflow) – This library provides incremental data processing in the cloud. Providing this ability gives scientists and engineers the ability to put tools together, packaged in Docker images, using programming constructs. The library then evaluates the programs transparently parallelizing the work and memoizing results – i.e. using go routines and caching data appropriately to speed up tasks. The library was created at [GRAIL](http://grail.com/) to manage our NGS (next generation sequencing) bioinformatics workloads on [AWS](https://aws.amazon.com/), but has also been used for many other applications, including model training and ad-hoc data analyses. Severl of Reflow’s key features include:

- functional, lazy, type-safe **D**omain **S**pecific **L**anguage (DSL) for writing workflow programs.
- the runtime for the DSL evaluates incrementally, coordinating cluster execution, and memoization.
- a cluster scheduler to dynamically provision and tear down resources in the cloud (currently AWS is supported).
- with containers the same processing workloads can also be executed locally.

TLDR;

Reflow provides a way for data scientists, and by proxy database administrators, data programmers, programmers, and anybody that needs to work through ETL or related work to write programs against that data in the cloud or locally.

![DevOps Days Vancouver - Architecture Guidance - Venomous Database Reliability Engineering (3)](/wp-content/uploads/2019/03/devops-days-vancouver-architecture-guidance-venomous-database-reliability-engineering-3-1.jpg)

[Restic](https://restic.net/) ([Github](https://github.com/restic/restic)) – Restic is a backup CLI and Go library that will backup to a number of sources, a few including; local directory, sftp, http REST, S3, Google Cloud Storage, Azure Blob Storage, and others.

Restic follows several objectives:

- The tool aims to be easy, with minimal singular steps to execute a backup.
- The tool aims to be fast, using appropriate mechanisms to ensure speedy backups.
- The tool aims to provide verifiable backups that can easily be restored.
- The tool aims to incorporate cryptographic guarantees of confidentiality to make sure the backups are secure.
- The tool aims to be efficient with additional snapshots only taking the storage of the actual increment and de-duplicated to save space in the storage back end.

![DevOps Days Vancouver - Architecture Guidance - Venomous Database Reliability Engineering (4)](/wp-content/uploads/2019/03/devops-days-vancouver-architecture-guidance-venomous-database-reliability-engineering-4-1.jpg)

For each of these there’s a particular single driver that I use for each. Except in the case of Apache Cassandra and DataStax Enterprise I have also picked up gocqlx to add to my gocql usage.

[PostgreSQL](https://github.com/lib/pq) – Features:

- SSL
- Handles bad connections for database/sql
- Scan time.Time correctly (i.e. timestamp[tz], time[tz], date)
- Scan binary blobs correctly (i.e. bytea)
- Package for hstore support
- COPY FROM support
- pq.ParseURL for converting urls to connection strings for sql.Open.
- Many libpq compatible environment variables
- Unix socket support
- Notifications: LISTEN/NOTIFY
- pgpass support

[Gocql](https://github.com/gocql/gocql) & [Gocqlx](https://github.com/scylladb/gocqlx) –

Gocql Features:

- Modern Cassandra client using the native transport
- Automatic type conversions between Cassandra and Go
  - Support for all common types including sets, lists and maps
  - Custom types can implement a Marshaler and Unmarshaler interface
  - Strict type conversions without any loss of precision
  - Built-In support for UUIDs (version 1 and 4)
- Support for logged, unlogged and counter batches
- Cluster management
  - Automatic reconnect on connection failures with exponential falloff
  - Round robin distribution of queries to different hosts
  - Round robin distribution of queries to different connections on a host
  - Each connection can execute up to n concurrent queries (whereby n is the limit set by the protocol version the client chooses to use)
  - Optional automatic discovery of nodes
  - Policy based connection pool with token aware and round-robin policy implementations
- Support for password authentication
- Iteration over paged results with configurable page size
- Support for TLS/SSL
- Optional frame compression (using snappy)
- Automatic query preparation
- Support for query tracing
- Support for Cassandra 2.1+ binary protocol version 3
  - Support for up to 32768 streams
  - Support for tuple types
  - Support for client side timestamps by default
  - Support for UDTs via a custom marshaller or struct tags
- Support for Cassandra 3.0+ binary protocol version 4
- An API to access the schema metadata of a given keyspace

Gocqlx Features:

- Binding query parameters form struct or map
- Scanning results directly into struct or slice
- CQL query builder (package qb)
- Super simple CRUD operations based on table model (package table)
- Database migrations (package migrate)

[Go-MSSQLDB](https://github.com/denisenkom/go-mssqldb) – Features:

- Can be used with SQL Server 2005 or newer
- Can be used with Microsoft Azure SQL Database
- Can be used on all go supported platforms (e.g. Linux, Mac OS X and Windows)
- Supports new date/time types: date, time, datetime2, datetimeoffset
- Supports string parameters longer than 8000 characters
- Supports encryption using SSL/TLS
- Supports SQL Server and Windows Authentication
- Supports Single-Sign-On on Windows
- Supports connections to AlwaysOn Availability Group listeners, including re-direction to read-only replicas.
- Supports query notifications

So this is just a few of the libraries I use, have worked with, and suggest checking out if you’re delving into database work and especially building systems around databases for reliability and related efforts.

If you’ve got other libraries that you’ve used, or really like, definitely leave a comment and let me know and I’ll update the post to include new libraries for Go. Subscribe to the blog too as I’ve got more posts in the cooker for database work, Go libraries and usage with databases, and a lot more. Happy thrashing code!
