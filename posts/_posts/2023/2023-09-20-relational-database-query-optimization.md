---
title: Relational Database Query Optimization
date: 2023-09-20 13:20:09 -0700
last_modified_at: 2024-04-12 20:09:43 -0700
permalink: /2023/09/20/relational-database-query-optimization/
slug: relational-database-query-optimization
wp_id: 66755
original_url: https://compositecode.blog/2023/09/20/relational-database-query-optimization/
categories:
- Databases
tags:
- database
- mariadb
- mysql
- oracle
- postgresql
- query optimization
- relational database
- relational database management system
- sql server
excerpt: We’re discussing query optimization techniques for relational databases, covering both common and uncommon strategies across various database management systems. These techniques range from basic practices like indexing to advanced methods like bitmap indexing and adaptive cursor sharing.
image: /wp-content/uploads/2023/08/alphabet-letters-and-icons-with-the-word-database-2023-08-19-06-29-49-utc.jpg
---

This is a continuation of my posts on relational databases, started [here](/2023/08/22/designing-a-relational-database-data-modeling/). Previous posts on this theme, “[Data Modeling](/2023/08/22/designing-a-relational-database-data-modeling/)“, “[Let’s Talk About Database Schema](/2023/08/29/lets-talk-about-database-schema/)“, “[The Exasperating Topic of Database Indexes](/2023/09/06/the-exasperating-topic-of-database-indexes/)“, and “[The Keys & Relationships of Relational Databases](/2023/09/18/the-keys-relationships-of-relational-databases/)“.

Query optimization refers to the process of selecting the most efficient way to execute a SQL query. The goal is to retrieve the requested data as quickly and efficiently as possible, making the best use of system resources. Given that there can be multiple strategies to retrieve the same set of data, the optimizer’s role is to choose the best one based on factors like data distribution, statistics, and available resources.

## Query Optimizers

Here’s a brief overview:

### 1. SQL Server

**Query Execution Plans**: SQL Server provides graphical execution plans which allow you to see how the query optimizer plans to execute your query. There are mainly three types of execution plans:

- **Estimated Execution Plan**: Provides an estimated plan without running the query.
- **Actual Execution Plan**: Provides the plan after the query has been executed.
- **Text Execution Plan**: Provides a textual representation of the execution plan.

**How to Get Them**:

- **Graphical Execution Plan (Management Studio)**:
  - **Actual Execution Plan**: You can view the actual execution plan that was used by SQL Server by running the query in SQL Server Management Studio (SSMS) with the “Include Actual Execution Plan” option enabled (shortcut: Ctrl + M). This shows the plan after the query execution, including runtime metrics such as actual row counts and actual execution times.
  - **Estimated Execution Plan**: Before running your query, you can also obtain an estimated execution plan by selecting “Display Estimated Execution Plan” (shortcut: Ctrl + L) in SSMS. This provides a plan based on statistics, without actually running the query.
- **Text and XML Plans**:
  - **SET SHOWPLAN\_TEXT**: By setting `SET SHOWPLAN_TEXT ON`, SQL Server returns the execution plan in a textual format instead of executing it. This provides a detailed, readable plan.
  - **SET SHOWPLAN\_XML**: Similar to `SET SHOWPLAN_TEXT`, but it returns the plan in an XML format when set to ON. This XML can then be viewed graphically in SSMS by clicking on the XML result.
  - **SET SHOWPLAN\_ALL**: This setting provides detailed information in a tabular format, including both the estimated and actual execution plan details if available.
- **Dynamic Management Views (DMVs)**:
  - SQL Server provides several DMVs that can help you retrieve historical execution plans. For instance, `sys.dm_exec_query_stats` combined with `sys.dm_exec_query_plan` and `sys.dm_exec_sql_text` can help you find execution plans for previously executed queries.
- **SQL Server Profiler and Extended Events**:
  - These tools allow you to capture execution plans for queries as they occur. You can set up an event session to capture the `Showplan XML` event, which gives you the execution plan in XML format for each query.
- **Query Store**:
  - If enabled, Query Store captures a history of execution plans along with their performance data. You can review these plans through various reports available in SSMS, which help in identifying performance regression and plan changes over time.

**Database Engine Tuning Advisor**: This is a separate tool that can analyze a workload and provide recommendations for indexes, indexed views, and partitioning.

### 2. Oracle

**Explain Plan**: The EXPLAIN PLAN statement displays the execution path chosen by the Oracle optimizer for a SQL statement. The plan is generated without executing the query.

**How to Get Them**:

- **EXPLAIN PLAN Command**: This is one of the most straightforward methods to obtain the execution plan. You use the `EXPLAIN PLAN FOR` command followed by your SQL query. For example:sqlCopy code`EXPLAIN PLAN FOR SELECT * FROM employees WHERE department_id = 10;` After running this command, you can view the execution plan using a select statement from a plan table (default table is `PLAN_TABLE`):sqlCopy code`SELECT * FROM TABLE(DBMS_XPLAN.DISPLAY());`
- **SQL Developer**: Oracle SQL Developer, the graphical tool for database development, allows you to easily view execution plans by simply running the query with the “Explain Plan” button or using the “Autotrace” feature, which not only shows the plan but also provides statistics about the query execution.
- **DBMS\_XPLAN Package**: This package provides several functions to display formatted information about execution plans stored in the plan table. After running an `EXPLAIN PLAN`, you can display the output with:sqlCopy code`SELECT * FROM TABLE(DBMS_XPLAN.DISPLAY('PLAN_TABLE', null, 'TYPICAL'));` You can also use it to display the actual execution plan for a query that has been executed, by referencing the cursor through `DBMS_XPLAN.DISPLAY_CURSOR` function, which is useful for getting a real-world plan including runtime statistics:sqlCopy code`SELECT * FROM TABLE(DBMS_XPLAN.DISPLAY_CURSOR(null, null, 'ALLSTATS LAST'));`
- **V$SQL\_PLAN View**: Oracle also provides dynamic performance views such as `V$SQL_PLAN`, which contain information about the execution plans for recently executed queries. This view is particularly useful for looking at plans of queries that are still in memory:sqlCopy code`SELECT * FROM V$SQL_PLAN WHERE sql_id = 'your_sql_id_here';`
- **TKPROF Utility**: TKPROF is a tool used to format the contents of the trace files generated by the SQL Trace facility. You can enable SQL Trace for your session, execute your queries, and then use TKPROF to generate a human-readable file that includes execution plans along with timing statistics.
- **Autotrace in SQL\*Plus**: This feature in SQL*Plus and SQLcl can be used to report execution plans and statistics of executed SQL statements automatically. It’s enabled by issuing `SET AUTOTRACE ON` in your SQL*Plus session.

**SQL Tuning Advisor**: This tool provides recommendations to improve the performance of SQL queries.

**How to Launch**:

- It can be accessed from Oracle Enterprise Manager (OEM) or directly from SQL with the `DBMS_SQLTUNE` package.

### 3. MariaDB/MySQL

**EXPLAIN**: This command can be used to obtain a query execution plan, which describes how MySQL intends to execute your query.

**How to Get Them**:

- **EXPLAIN Statement**: This is the most common method used to obtain a query execution plan. You prepend `EXPLAIN` to any SELECT, INSERT, DELETE, REPLACE, or UPDATE statement to get information about how MySQL would execute it. This includes details about table scans, joins, indexes used, and more. The syntax is simple:sqlCopy code`EXPLAIN SELECT * FROM your_table WHERE column = 'value';`
- **EXPLAIN EXTENDED**: This provides additional information beyond what the basic `EXPLAIN` provides. It can reveal details about how MySQL resolves the query, including rewrites performed by the optimizer:sqlCopy code`EXPLAIN EXTENDED SELECT * FROM your_table;`
- **EXPLAIN FORMAT=JSON**: For more detailed insight, especially in MySQL 5.6+ and MariaDB 10.1+, you can use the JSON format for the execution plan. This format provides a more detailed and hierarchical view of the plan, which can be more readable and informative:sqlCopy code`EXPLAIN FORMAT=JSON SELECT * FROM your_table;`
- **SHOW PLAN**: Available in MariaDB, this command is used within the context of the `ANALYZE` statement to provide a real-time execution plan and statistics about a query’s execution. This is useful for capturing execution details during the actual run of a query:sqlCopy code`ANALYZE FORMAT=JSON SELECT * FROM your_table;`
- **Performance Schema**: In MySQL, particularly with newer versions, you can use the Performance Schema to collect and analyze performance data, including comprehensive details about query execution. This approach is more complex and requires setting up performance schema instrumentation but can yield very detailed insights.
- **Optimizer Trace**: In MySQL, the optimizer trace feature gives insights into the optimizer’s decision-making process. It’s a JSON-formatted output that shows how different query execution plans are compared and chosen. This feature is enabled and queried as follows:sqlCopy code`SET optimizer_trace="enabled=on"; SELECT * FROM your_table; SELECT * FROM information_schema.optimizer_trace;`

**Optimizer Trace**: MySQL also offers an optimizer trace that provides insight into the optimizer’s decision-making process.

### 4. PostgreSQL

**EXPLAIN**: PostgreSQL also uses the EXPLAIN command to see the execution plan of a SQL statement.

**How to Get Them**:

- **EXPLAIN**: The `EXPLAIN` command in PostgreSQL shows the execution plan of a query without actually running it. This command provides details on how the database plans to execute the query, including which algorithms will be used to join tables and how rows will be processed.Basic usage:sqlCopy code`EXPLAIN SELECT * FROM your_table;`
- **EXPLAIN ANALYZE**: This is an extension of the `EXPLAIN` command. `EXPLAIN ANALYZE` actually executes the query, and then reports the execution plan and the actual execution time for each step. This can be more insightful than `EXPLAIN` alone because it shows what really happened during the execution.Example:sqlCopy code`EXPLAIN ANALYZE SELECT * FROM your_table;`
- **EXPLAIN (FORMAT JSON, XML, etc.)**: PostgreSQL allows the execution plan to be output in different formats such as TEXT, XML, JSON, or YAML. This can be useful for further processing or analysis of the plan in tools that can parse these formats.Example using JSON:sqlCopy code`EXPLAIN (FORMAT JSON) SELECT * FROM your_table;`
- **Verbose Output**: Adding the `VERBOSE` keyword to an `EXPLAIN` statement provides additional information, such as the output columns of each node in the plan.Example:sqlCopy code`EXPLAIN (VERBOSE) SELECT * FROM your_table;`
- **Buffers**: Using `BUFFERS` with `EXPLAIN ANALYZE` provides information about buffer usage during the query execution. This is useful for understanding the I/O behavior of your query.Example:sqlCopy code`EXPLAIN (ANALYZE, BUFFERS) SELECT * FROM your_table;`
- **Timing**: The `TIMING` option can be turned on or off in `EXPLAIN ANALYZE` to show or hide the timing information for each operation. By default, timing is on in PostgreSQL 9.2 and above.Example to turn off timing:sqlCopy code`EXPLAIN (ANALYZE, TIMING OFF) SELECT * FROM your_table;`
- **pg\_stat\_statements**: This is an extension that needs to be enabled in your PostgreSQL instance. It provides a means to track execution statistics of all SQL statements executed by a server, not just the plan but also execution frequency, total time spent in the statement, and more.To use it, first ensure it’s enabled and then query its view:sqlCopy code`CREATE EXTENSION IF NOT EXISTS pg_stat_statements; SELECT * FROM pg_stat_statements;`

**pg\_stat\_statements Module**: This is an extension in PostgreSQL that captures execution statistics of SQL statements, giving insights about frequently executed queries, their average execution time, and more.

**How to Launch**:

- First, enable the `pg_stat_statements` in the `postgresql.conf` file or on server start. Once done, you can query the `pg_stat_statements` view to see the statistics.

For all these databases, it’s important to remember that understanding the underlying data model, data distribution, and application requirements is crucial when interpreting the recommendations and execution plans from these tools. Always test the recommendations in a non-production environment before implementing them in production.

## Common Optimizations

1. **“Speedy Searchers” (Indexes)**:
   - Use them: Create the right indexes to supercharge your search queries. Think of it as the fast lane on the database highway!
2. **“Fresh Intel” (Update Statistics)**:
   - Keep your database in-the-know: Regularly update the statistics so the database has fresh intel on your data layout and can make smarter decisions.
3. **“Join the Party Right” (Optimize Joins)**:
   - Don’t let your tables just mash together; ensure that they join on indexed columns and minimize rows with precision, like an elite party guest list.
4. **“Break it to Make it” (Partitioning)**:
   - Too much data? No problem! Break your big tables into manageable pieces. It’s like organizing a messy room into tidy sections.
5. **“Déjà Vu Data” (Caching)**:
   - Remember the results of common queries so you can serve them up instantly next time. It’s like having your favorite dish pre-made and ready to serve.
6. **“Shape Shifter Queries” (Query Rewriting)**:
   - A little twist and turn can change the game. Rewrite your queries for a new perspective and often, faster results.
7. **“Be Picky” (Selective Retrieval)**:
   - Don’t grab everything off the shelf! Only pick up what you need. Use specific column names instead of SELECT \*.
8. **“Slim & Trim” (Limit Data)**:
   - Stay in shape! Use LIMIT, OFFSET, and WHERE to fetch just the right amount of data and keep things lean.
9. **“Design Detective” (Normalization)**:
   - Investigate and restructure: Ensure your database design is optimal. A well-organized schema is half the battle won!
10. **“Peek Under the Hood” (Profiling & EXPLAIN)**:
    - Don’t just run your queries blindly; use profiling tools and the EXPLAIN command to see what’s going on behind the scenes.

## Esoteric Optimizations

While the basic principles of query optimization apply across the board, there are some advanced and often less-commonly applied techniques that can squeeze out more performance, especially in edge cases or specific scenarios. Here are some of the more uncommon ways to optimize queries:

1. **Materialized Query Tables (MQTs)**:
   - Sometimes found in enterprise-level RDBMSs like DB2, MQTs are like views that store results of a query and can be refreshed periodically. They can help optimize complex computations, but require a balance of when to refresh the MQT versus querying it.
2. **Bitmap Indexing**:
   - While B-tree and hash indexes are more common, bitmap indexes can be beneficial for columns with a low cardinality (few unique values). They’re especially useful for data warehousing scenarios where AND/OR operations are frequent.
3. **Index-Organized Tables (IOT)**:
   - Offered by systems like Oracle, IOTs are tables stored in a B-tree structure. This can lead to faster access times for certain types of queries, but with trade-offs in other operations like inserts.
4. **Database In-Memory**:
   - Databases like Oracle offer an in-memory option. While the main data can be on disk, frequently accessed data is stored in-memory in a columnar format, enabling rapid analytics.
5. **Clustered Columnstore Indexes**:
   - Available in systems like SQL Server, these indexes store data in a columnar format, optimizing it for reading large amounts of data, beneficial for analytics.
6. **Query Rewrite**:
   - Some advanced RDBMSs can recognize when a new query is logically equivalent to a previous one and will use cached results or a more optimized path. This often requires a deep understanding of the optimizer’s logic and might involve hints or specific syntax.
7. **Use of Zone Maps**:
   - Zone maps (or storage indexes) keep track of ranges of values for columns stored in specific data blocks or extents. This allows the database to skip over large portions of data that aren’t relevant to a query.
8. **Database Compression**:
   - Some databases offer on-the-fly compression and decompression. This reduces I/O, which often is a major bottleneck. However, there’s CPU overhead for compression operations.
9. **Adaptive Cursor Sharing**:
   - Systems like Oracle can generate multiple execution plans for a single query to adapt to different bind variable values, optimizing performance for varied use cases.
10. **Parallel Query Execution**:
    - For very large datasets, databases like Oracle and SQL Server can split a single query to run in parallel across multiple CPU cores or threads. This requires a fine balance to prevent resource contention.

Many of these uncommon methods require a deep understanding of both the database system in question and the specific workload being optimized. Additionally, many are context-specific: they might offer significant benefits in one scenario while being detrimental in another. As always, thorough testing and monitoring are essential when implementing advanced optimization techniques.
