---
title: Pragmatic Database Schema Naming Conventions, Practices, and Patterns
date: 2020-11-29 09:41:57 -0800
last_modified_at: 2020-11-29 09:44:36 -0800
permalink: /2020/11/29/database-naming-schema/
slug: database-naming-schema
wp_id: 40122
original_url: https://compositecode.blog/2020/11/29/database-naming-schema/
categories:
- Databases
tags:
- data design
- data modeling
- database
- database conventions
- database modeling
- database schema
- naming
- naming conventions
excerpt: In this post I’ve put together some of the naming conventions, rules, and ideas that I tend to follow when creating database schemas to work with. This also applies to schema-less databases, distributed systems databases, graph, time series, or whatever else I am working with. It’s always good to have some good conventions to work with, and the descriptions and ideas in this post are a solid starting point.
image: /wp-content/uploads/2020/11/databases.jpg
---

In this post I’ve put together some of the naming conventions, rules, and ideas that I tend to follow when creating database schemas to work with. This also applies to schema-less databases, distributed systems databases, graph, time series, or whatever else I am working with. It’s always good to have some good conventions to work with, and the descriptions and ideas in this post are a solid starting point.

## What We’re Working With, Some of The Database Rules

Let’s start with a SQL Server rule. Table names must be less than 128 characters. To force SQL Server to use non-standard table names one can use brackets. Then in scripts these names have to be single quoted.

There are many other rules about naming things in SQL Server. But let’s talk about some other database specific rules for other databases.

Postgres names fold to lowercase versus uppercase, which is different then many other databases. Throw in some double quotes however and you can use names like MyTable, MYTABLE, and mytable. These would all be the same without double qutoes, add the double quotes around those names and “MYTABLE” becomes different than “MyTable” and different than “mytable”.

SQL identifiers in Postgres and key words must begin with letters (a-z), which include diacritical marks and non-Latin letters. After the first letter and identifier can have letters, underscores, digits, or dollar signs. If an identifier is double quoted, you can also yse keywords, albeit I would very strongly reccommend against this practice.

As these examples provide, there are a number of ways that the rules are just different enough from one database to another that it is often very helpful to use a naming convention that would work across databases. I’m often working with a variety of databases so this post will cover naming convention ideas and respective patterns and practices around them that would work with every conceivable database I know to exist!

## Table, Column, Tuple, or Related Naming Conventions

- Table, column, and related object names should contain only letters, numbers as characters in the body of the name and not as the preface characters, underscores and absolutely no spaces or special characters. In summary, use a case scheme like [Camel or Pascal Case](/2020/11/27/name-casing-conventions/) but do not use [Snake or Kebab Case](/2020/11/27/name-casing-conventions/).
- Use meaningful names from the business or organizational domain being modeled. Such as “BankingUsers”, “Transactions”, “railroads”, or “railroad\_Systems”.
- Use singular word names if at all possible, only moving to compound word naming if absolutely necessary. Ideally names would be single words like “User”, “Transactions”, “railroad”, or “system” and exclude compound names like “railroadSystem” until it is needed to prevent confusion or naming collisions.
- Columns that are primary or foreign keys should be prefaced with PK\_ and FK\_ respectively, and in my moderately humble opinion, stick to just PK or FK using Camel or Pascal Case. For other metadata, indexes, and related names use a respective preface or postfix conventions.
- It’s also a good idea to choose plural or singular for table names. However, be sure to choose one or the other so that frameworks, [Object Relationship/Relational Mappers/Mapping (ORM)](https://en.wikipedia.org/wiki/Object%E2%80%93relational_mapping), and other tools can effectively name things when used. For example, when table names are singular, many ORM frameworks when generating code would take a singular table name like `Customer` and make it `Customers` and have objects of `Customer`.

## Schema/Domain Naming Conventions

In many databases there are additional organizational and related structures that help us to setup tables, functions, stored procedures, compiled SQL/queries, and other objects in groupings. Naming these objects accordingly is easiest by following the same convention as the table naming convention.

For example, if the table naming convention is following Camel Case then continue that;

Table Names for Returns in an E-commerce Domain:

- Purchase
- Return
- Shipped

Table Names for Pricing in an E-commerce Domain:

- Price
- Cost

Table Names for Core Tables, for multiple schemas, within the E-commerce Domain:

- Item

This could be split out to three schemas;

- Core
- Prices
- Returns

The names would then look like this:

Core.Item
Prices.Purchase
Prices.Return
Prices.Shipped
Returns.Purchase
Returns.Return
Returns.ShippedItem

## An Example

Here’s an example I put together with some naming conventions I’ve found useful, reduces confusion, and manages to tell a reasonable amount of information about the domain space and schema of the database without conflicts.

[![](/wp-content/uploads/2020/11/0kv162hdpfkhylj8bxsp.png)](/wp-content/uploads/2020/11/0kv162hdpfkhylj8bxsp.png)

*The Database Schema*

Throughout this schema I’ve used Camel Casing, with most single word column and single word table names. Keeping it simple, such as `Id` and `Stamp` are some of the recurring columsn that are useful for retrieval, relationships, and determining origins of data over time. In production settings there are default columns that are often needed and one can rest assured, a time stamp is most likely one of those that is needed everywhere for audits!

For my foriegn key columns, one can determine the relationship by the name of the column itself. For example, in the Connection table the are two foreign keys, one to the Action table and one to the Source table, to the respective Id columns in each of those tables. The one exception is NoteJot, which I named because `Note` tends to conflict in certain systems. In that table I’ve added a relationship, for recursive data, back to itself with the use of the NoteId foreign key back to the table’s primary key `Id`.

The diagram above, without any further details can be used to create the schema, with SQL code that would look like the following.

```
CREATE TABLE "Source" (
  "Id" uuid PRIMARY KEY,
  "Stamp" timestamp,
  "Name" text,
  "Uri" text,
  "Details" text
);

CREATE TABLE "SourceNotes" (
  "SourceId" uuid,
  "NotesId" uuid,
  "Details" text,
  "Stamp" timestamp
);

CREATE TABLE "NoteJot" (
  "Id" uuid PRIMARY KEY,
  "Stamp" timestamp,
  "NoteId" uuid,
  "Details" text
);

CREATE TABLE "Action" (
  "Id" uuid PRIMARY KEY,
  "Stamp" timestamp,
  "Action" json
);

CREATE TABLE "Connection" (
  "Id" uuid PRIMARY KEY,
  "Stamp" timestamp,
  "ActionId" uuid,
  "SourceId" uuid
);

CREATE TABLE "Formatter" (
  "Id" uuid PRIMARY KEY,
  "Stamp" timestamp,
  "ConnectionId" uuid,
  "FormatterMap" json
);

CREATE TABLE "Schema" (
  "Id" uuid PRIMARY KEY,
  "Stamp" timestamp,
  "ConnectionId" uuid,
  "SchemaMap" json
);

ALTER TABLE "SourceNotes" ADD FOREIGN KEY ("SourceId") REFERENCES "Source" ("Id");

ALTER TABLE "SourceNotes" ADD FOREIGN KEY ("NotesId") REFERENCES "NoteJot" ("Id");

ALTER TABLE "NoteJot" ADD FOREIGN KEY ("NoteId") REFERENCES "NoteJot" ("Id");

ALTER TABLE "Connection" ADD FOREIGN KEY ("ActionId") REFERENCES "Action" ("Id");

ALTER TABLE "Connection" ADD FOREIGN KEY ("SourceId") REFERENCES "Source" ("Id");

ALTER TABLE "Formatter" ADD FOREIGN KEY ("ConnectionId") REFERENCES "Connection" ("Id");

ALTER TABLE "Schema" ADD FOREIGN KEY ("ConnectionId") REFERENCES "Connection" ("Id");
```

We have the tables and keys, all following the [Camel Case](/2020/11/27/name-casing-conventions/) standard. Much of this however could be – if you preferred – to Pascal Case however switching them to [Snake or Kebab Case](/2020/11/27/name-casing-conventions/) would cause a number of issues depending on the database.

## Do NOT Use These

Unless you want to spend tons of time with errors, debugging, and related issues skip these practices.

- Generally throughout databases it is best to skip [Snake or Kebab Case](/2020/11/27/name-casing-conventions/). Various situations they’re fine, but overall they’re likely to run into conflicts, naming limitations, or other concerns. It’s best to just skip them and remove the concern.
- When you’re using data that has variance in how it is represented, do not use multitudes of formats. For dates, location, geographic, or related data it is best to stick to a particular format that is repeated throughout the database. Using mixed representations, for example with dates a MMDDYYYY format and then a DD-MM-YYYY format, methods, functions, or other elements that consume or process this data will need to account for this. Creating more time consuming and error prone code.
- Once you pick a naming scheme for any particular database object type, stick to the naming scheme. For example, if you go with Camel Casing for your tables, use Camel Casing for *all of the tables* and don’t switch to Pascal for some of them. Specifically, however with this guidance, is if you switch object types, for example you name the tables Pascal Cased but switch to Camel Case for indexes, that’s perfect. Then if ever reviewing a list of objects irrespective of kinds of objects, one can differentiate merely by the conventions used.

## Summary & Caveat

Working up a set of patterns, practices, rules, and generally conventions to work with on the database side of things is immensely useful. It helps the Database Administrators, Data Scientists, Software Developers, others that need to utilize the database, and to communicate with each other in reference to the database and data.

---

That’s it for the database schema topic for now. However, if you’re interested in joining me for more database and data oriented things, language stack setup, software development, patterns, practices, and more in addition to writing some JavaScript, Go, Python, Terraform, and infrastructure, web dev, and all sorts of coding I stream regularly on Twitch at <https://twitch.tv/thrashingcode>, post the VOD’s to YouTube along with entirely new tech and *metal* content at <https://youtube.com/ThrashingCode>. Feel free to check out a coding session, ask questions, interject, or just come and enjoy the tunes!
