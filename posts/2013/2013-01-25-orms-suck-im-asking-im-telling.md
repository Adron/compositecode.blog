---
title: ORMs Suck, I’m Asking & I’m Telling
date: 2013-01-25 13:10:50 -0800
last_modified_at: 2013-01-25 15:01:33 -0800
permalink: /2013/01/25/orms-suck-im-asking-im-telling/
slug: orms-suck-im-asking-im-telling
wp_id: 7575
original_url: https://compositecode.blog/2013/01/25/orms-suck-im-asking-im-telling/
categories:
- Architecture
tags:
- dynamic language
- object relational mapper
- object relationship mapper
- orm
- productivity booster
- technology
excerpt: Here’s a thing that’s come up already. ORMs, or Object Relational Mapper, are a RDBMS based thing for devs that want, in essence a statically typed object to deal with when writing code (yes, I know there’s a ton of other things an ORM can do or be used for, but I’m going with a …
---

Here’s a thing that’s come up already. ORMs, or Object Relational Mapper, are a RDBMS based thing for devs that want, in essence a statically typed object to deal with when writing code (yes, I know there’s a ton of other things an ORM can do or be used for, but I’m going with a simple explanation here, [here’s more info](http://en.wikipedia.org/wiki/Object-relational_mapping)). For some situations, I can see where that’s a productivity booster, but in other situations it is a very broken ideal. Especially when it comes to needs around highly complex query needs, performance and a host of other functionalities when you get into the higher end demands of Enterprise or \*web scale\* type systems.

Two things that has brought up this question in a new light, is:

- **One**: Why would you use an ORM in a dynamic language like JavaScript, that has a simple native format like JSON? It tends to make far less sense to do this. What’s your take? Like the idea? Hate the idea?
- **Two**: In a schemaless database, forcing an ORM on something that is built specifically to not have this featureset (for a number of reasons) seems to break the design ideas of the systems. Whether it is Mongo, Riak, Cassandra or whatever, why would you actually want to or not want to use an ORM? I’ve got my own thoughts but would like to know what people think about this notion.

-Please comment, I’ll be diving into any feedback too.
