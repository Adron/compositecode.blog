---
title: Database Naming Convention Ideas
date: 2021-03-31 10:41:51 -0700
last_modified_at: 2021-03-31 14:49:07 -0700
permalink: /2021/03/31/database-naming-convention-ideas/
slug: database-naming-convention-ideas
wp_id: 63655
original_url: https://compositecode.blog/2021/03/31/database-naming-convention-ideas/
categories:
- Unknown Code Ramblings
tags:
- database conventions
- database naming
- naming
- naming conventions
- naming is hard
- programming
excerpt: A while ago I wrote a post titled “Pragmatic Database Schema Naming Conventions, Practices, and Patterns”. In that post I outlined basic naming convention use in naming the elements of your database and the database itself using general naming conventions like; Camel, Pascal, Kebab, and the like. For a quick lookup, I also wrote a post titled “Name Casing Conventions, The Quick Comparison” just to list out the specific naming conventions.
image: /wp-content/uploads/2020/11/databases.jpg
---

A while ago I wrote a post titled “[Pragmatic Database Schema Naming Conventions, Practices, and Patterns](/2020/11/29/database-naming-schema/)“. In that post I outlined basic naming convention use in naming the elements of your database and the database itself using general naming conventions like; Camel, Pascal, Kebab, and the like. For a quick lookup, I also wrote a post titled “[Name Casing Conventions, The Quick Comparison](/2020/11/27/name-casing-conventions/)” just to list out the specific naming conventions.

Recently **[Jens Dahl Møllerhøj](https://www.linkedin.com/in/mollerhoj3)** wrote to me about a post he wrote on the topic of many to many tables and a convention around how they could be named. I read the post and indeed, very good observation of language and how we ought to name many to many relationship based tables, or junction tables. Give it a read at “[How to Name Your Junction Tables](https://world.hey.com/jdmo/how-to-name-your-junction-tables-3735fdc9)“.

Also in the original post a few comments and notes have been made about database naming conventions. Here is a short list of those:

- Generally, many if not most database administrator’s prefer naming of tables be singular items. Like “user”, “address”, or “item”. Some prefer plural like “users”, “addresses”, or “items”. Pick one, stick to it.
- More than a few tools take singular table names and will pluralize them or the object arrays/entities that are returned, be aware of this and know the effect your naming strategy may have on this feature and practice.
- Most would prefer lower case naming for database objects as it prevents the need for quotes and other syntax in the SQL statements. Making statements much easier to write if one doesn’t need to quote every table, schema(namespace), column, and related items because it has uppercase characters. Yes, this does make picking a convention a bit tricky, but see the next item to simplify things.
- Compound names should largely be avoided for column and table names. This prevents the naming conventions conflicting with the need for lowercase naming.

While developing your schemas and naming conventions, here’s another addendum of [do and do nots for postgres](https://wiki.postgresql.org/wiki/Don%27t_Do_This#Don.27t_use_timestamp_.28without_time_zone.29).

That’s it for now. More comments, ideas, thoughts, complaints, or opinions about naming things in databases or naming objects and such in programming, let me know [@Adron](https://twitter.com/adron) or leave a comment below.
