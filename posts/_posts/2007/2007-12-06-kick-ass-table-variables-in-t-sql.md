---
title: Kick Ass Table Variables in T-SQL
date: 2007-12-06 10:07:52 -0800
last_modified_at: 2007-12-06 10:07:52 -0800
permalink: /2007/12/06/kick-ass-table-variables-in-t-sql/
slug: kick-ass-table-variables-in-t-sql
wp_id: 376
original_url: https://compositecode.blog/2007/12/06/kick-ass-table-variables-in-t-sql/
categories:
- Uncategorized Bits
tags: []
excerpt: Table variables are another “tool belt” item that one must have when really digging into various SQL tasks. Oracle and other real databases also have this capability, but I’m going to, as usual, discuss the Microsoft SQL variant of the table variable for a minute. One scenario that I was faced with was how to …
---

Table variables are another “tool belt” item that one must have when really digging into various SQL tasks.  Oracle and other real databases also have this capability, but I’m going to, as usual, discuss the Microsoft SQL variant of the table variable for a minute.

One scenario that I was faced with was how to match data that existed in a database with data that had been put together in a text file type format.  I’ll call this scenario the Groupie Scenario.

**Groupie Scenario**

In the Groupie Scenario I needed to use a table variable to stored all of the statically created data in the flat file I received.  There are a ton of ways to load this data into physical or even temp tables using SSIS and other methods, but I just grabbed the text file and did a quick find and replace on the beginning and ending of the data.  What I ended up with was a really nice set of INSERT statements ready to go.  All I needed then was to create a table variable to insert into and I was set.

Basically this worked out to look something like this:

> DECLARE @UriCompareList TABLE
> (
>   UriDescription nvarchar(50),
>   UriPath nvarchar(100)
> )
> INSERT INTO @UriCompareList VALUES (‘Argentina’,’/argentina/socios/’)
> INSERT INTO @UriCompareList VALUES (‘Austria’,’/austria/partner/’)
> INSERT INTO @UriCompareList VALUES (‘Belgium’,’/partner/belux/’)
> INSERT INTO @UriCompareList VALUES (‘Bolivia’,’/bolivia/socios/’)
> INSERT INTO @UriCompareList VALUES (‘Brazil’,’/brasil/parceiros/’)
> INSERT INTO @UriCompareList VALUES (‘Bulgaria’,’/bulgaria/partners/’)

After I built that, I simply added the query segment to utilize the table variable.

> SELECT
> DISTINCT (DIR.[dirurl]), COUNT(DISTINCT(DIR.[ID])) as TotalCountedItems
> FROM @UriCompareList AS UCL LEFT OUTER JOIN [dbo].[dirdir] AS DIR
>     ON [DIR].[dirurl] = [UCL].[UriPath]
> WHERE dirTime < @EndDate AND dirTime > @StartDate
> GROUP BY [dirurl]
> ORDER BY [dirurl]

Technorati Tags: [T-SQL](http://technorati.com/tags/T-SQL),[SQL](http://technorati.com/tags/SQL),[SQL Server](http://technorati.com/tags/SQL%20Server),[Table Variable](http://technorati.com/tags/Table%20Variable)

del.icio.us Tags: [T-SQL](http://del.icio.us/popular/T-SQL),[SQL](http://del.icio.us/popular/SQL),[SQL Server](http://del.icio.us/popular/SQL%20Server),[Table Variable](http://del.icio.us/popular/Table%20Variable)
