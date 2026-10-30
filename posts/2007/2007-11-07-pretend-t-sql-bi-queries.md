---
title: Pretend T-SQL BI Queries
date: 2007-11-07 08:37:00 +0000
last_modified_at: 2007-11-07 08:37:00 +0000
permalink: /2007/11/07/pretend-t-sql-bi-queries/
slug: pretend-t-sql-bi-queries
wp_id: 403
original_url: https://compositecode.blog/2007/11/07/pretend-t-sql-bi-queries/
categories:
- Uncategorized Bits
tags: []
excerpt: Often times there is no cube, no OLAP, no BI plan but someone wants reports that provide rollup data, data slices, sums, and even dimensional representations that are oriented toward the BI world. Of course building these in SQL is possible, even easy sometimes, but it slams the processing of an RDBMS. When working through …
---

Often times there is no cube, no OLAP, no BI plan but someone wants reports that provide rollup data, data slices, sums, and even dimensional representations that are oriented toward the BI world.  Of course building these in SQL is possible, even easy sometimes, but it slams the processing of an RDBMS.  When working through these various SQL Queries it becomes a little more obvious, especially when the data rows number in the hundreds of thousands, exactly why OLAP and BI exist.

The following are the literal operators that provide cube like functionality within T-SQL.  However there are many issues with attempting to use T-SQL to get Cube sliced data and definitely issues with performance.  If the database is OLTP and has transactions occurring it is probably best to not even attempt queries with these operators.  It would be kind of like database server suicide.

**ROLLUP** – Rollup Is an aggregate function that creates an additional column of output with a value of 1 when the row is added by either the CUBE or ROLLUP operator, or 0 when the row is not the result of CUBE or ROLLUP.

Grouping is allowed only in the select list associated with a GROUP BY clause that contains either the CUBE or ROLLUP operator.

**CUBE** – The CUBE operator generates a result set that is a multidimensional cube. A multidimensional cube is an expansion of fact data, or data that records individual events. The expansion is based on columns that the user wants to analyze. These columns are called dimensions. The cube is a result set that contains a cross tabulation of all the possible combinations of the dimensions.

The CUBE operator is specified in the GROUP BY clause of a SELECT statement. The select list contains the dimension columns and aggregate function expressions. The GROUP BY specifies the dimension columns and the keywords WITH CUBE. The result set contains all possible combinations of the values in the dimension columns, together with the aggregate values from the underlying rows that match that combination of dimension values.

**SUM** – Returns the sum of all the values, or only the DISTINCT values, in the expression. SUM can be used with numeric columns only. Null values are ignored. May be followed by the OVER clause.

**COUNT** – Returns the number of items in a group. COUNT works like the COUNT\_BIG function. The only difference between the two functions is their return values. COUNT always returns an *int* data type value. COUNT\_BIG always returns a *bigint* data type value. May be followed by the OVER clause.

…and my favorite, for complexity reasons.

**COMPUTE** – Generates totals that appear as additional summary columns at the end of the result set. When used with BY, the COMPUTE clause generates control-breaks and subtotals in the result set. You can specify COMPUTE BY and COMPUTE in the same query.

One of the twisted things about the COMPUTE statement is dealing with it as part of the result set, because simply put, it isn’t.  It comes back as a secondary result set which needs to be handled as such.

So when in need of some preparatory T-SQL data “munging” to see how things might be in a cube, check out BOL (SQL Server Book Online, comes with the server installation) for any of these operator keywords and you’ll get multiple examples.

So that is my quick summary of “*wannabe*” OLAP type T-SQL queries.  If you want real reporting on slices and dices of data though, you have to drop these and get with the real OLAP/BI solution world.
