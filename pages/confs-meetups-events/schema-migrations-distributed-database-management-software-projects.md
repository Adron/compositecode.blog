---
layout: page
title: Schema Migrations & Distributed Database Management Software Projects
date: 2019-04-25 15:32:04 -0700
last_modified_at: 2019-05-07 14:44:27 -0700
permalink: /confs-meetups-events/schema-migrations-distributed-database-management-software-projects/
slug: schema-migrations-distributed-database-management-software-projects
wp_id: 15755
original_url: https://compositecode.blog/confs-meetups-events/schema-migrations-distributed-database-management-software-projects/
---

***NOTE: Slides & Video will eventually be provided once talk is given.***

**Slides**

<iframe allowfullscreen="true" frameborder="0" height="569" loading="lazy" marginheight="0" marginwidth="0" mozallowfullscreen="true" src="https://docs.google.com/presentation/d/e/2PACX-1vTdEYCUx-V8GktBkoikXrvvg08n3rLgf4KnPfI1iojHurRdYPlS4r_TtiRxjuLs1Dz3S-Avaa0dg9vU/embed?start=false&amp;loop=false&amp;delayms=3000" webkitallowfullscreen="true" width="863"></iframe>

TLDR; Come learn about DataGrip, Goland, and developing with distributed database Apache Cassandra.

I’ve broken this talk out into three parts:

**Distributed Database Apache Cassandra**

In this part of the talk I’ll give a quick overview of Apache Cassandra and what it is, how it works, in a lightning talk style format.

**Schema Migrations**

In this second part of the talk the dive will be much deeper. Covering the reasons for implementation of schema migrations into one’s development practices. Advantages and disadvantages of using this on a day to day basis. What is involved to build out schema migrations, tools to use, and other ecosystem options for a range of databases while focusing on Apache Cassandra.

**DataGrip and IDE’s**

For the second part, and wrapping up, I’ll cover a tour through the features and capabilities of DataGrip and related IDE’s. The core focus around and for getting your CQL, SQL, or related migration code put together for managing your database(s).

**Prerequisites if you’d like to follow along:**

- Get DataGrip, and your preferred JetBrains IDE (IntelliJ, Goland, WebStorm, Pycharm, etc) installed.
- Have Docker installed and ready to use.
- `docker pull` the `postgres` and `cassandra` docker images from docker hub (I’ll cover it, but it’s best if we don’t try to get these large images all at the same time, so please do a docker pull before the session)
