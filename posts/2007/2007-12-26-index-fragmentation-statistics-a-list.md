---
title: Index, Fragmentation, Statistics – A List
date: 2007-12-26 06:54:12 +0000
last_modified_at: 2007-12-26 06:54:12 +0000
permalink: /2007/12/26/index-fragmentation-statistics-a-list/
slug: index-fragmentation-statistics-a-list
wp_id: 360
original_url: https://compositecode.blog/2007/12/26/index-fragmentation-statistics-a-list/
categories:
- Uncategorized Bits
tags: []
excerpt: This entry is going to be a collected list of practices for index, fragmentation, statistics, and general VLDB table and view maintenance. First off, a few obvious index practices. If a non-clustered index is not used, toss it. When a table has a record inserted, the duplicate of that is inserted into the non-clustered index. …
---

This entry is going to be a collected list of practices for index, fragmentation, statistics, and general VLDB table and view maintenance.

First off, a few obvious index practices.

1. If a non-clustered index is not used, toss it.  When a table has a record inserted, the duplicate of that is inserted into the non-clustered index.  Each time that record is deleted the same must occur in the index and the same goes for updates.  Most horrendously, if a clustered index is created then the non-clustered index has to be rebuilt.  Major IO hog, if it isn’t used, no point in having it.  For information on how to check if a non-clustered index is being used, check out this blog entry on the [SQL Server Storage Engine](http://blogs.msdn.com/sqlserverstorageengine/archive/2007/04/20/how-can-you-tell-if-an-index-is-being-used.aspx).  At some point I might shrink that into a short entry and post it as a tip o’ the day.  I’ve had to reference it a number of times and would rather just the quick bullet points.- When checking VLDBs, and especially VVVLDBs, for consistency in sizes exceeding hundreds of gigabytes or even multiple terabytes there are a few options that one can follow:
     1. Use the WITH PHYSICAL\_ONLY option for CHECKDB.  It will run similar to DBCC CHECKALLOC and read and audit every allocated page in the database.  It will skip logical errors, inter-page checks, and some other things like the DBCC CHECKCATALOG.- Break up the checks by partition.  The DBCC CHECKFILEGROUP run on a read-only filegroup every week or two works great.  On a read-write filegroup DBCC CHECKFILEGROUP should be run every day or every few days.- Break up the checks into smaller groups by doing DBCC CHECKCATALOG or DBCCCHECKTABLE.  Break them into different groups and then segment the job execution of these checks to different maintenance windows.- Logical fragmentation only affects read-ahead performance, only a rebuild/defrag of indexes will help.- Low page density affects UI throughput and memory usage, which could be a sign of page-splits.  Check this frequently.- If defrag is done instead of rebuild, make sure to update stats.- Be cautious when doing large index maintenance jobs if log shipping or DBM is used, index rebuilds are always full-logged when DBM is present.  (DBM = Database Mirroring)

A few items mentioned by [**Peter Sampson – Technical Director at Centerstance**](http://www.linkedin.com/in/petersamson);  Blogs: [Moving to Mac](http://movingtomac.blogspot.com/) and [SQL Janitor](http://sqljanitor.blogspot.com/), over a recent pint o’ Beer at Bailey’s Taproom.

1. Regardless of OLTP or OLAP almost any table in SQL Server should…
   1. always have a clustered index on the table.- have a clustered index design that either very rarely or never has the clustered index updated.  SQL Server does a DELETE and an UPDATE if you update a column with a clustered index!- use non-clustered indexes in conjunction with the clustered index since they are interleaved.- DBCC DBREINDEX rebuilds the table and indexes depending on the parameters passed.  This is best done on a regular schedule, often by setting a job to execute the task.- FILLFACTOR is a critical parameter for DBREINDEX, make sure it isn’t just set to 100 or some other erroneous value that will cause problems.  FILLFACTOR sets the free space to leave during the rebuild of the Index B-tree structures and is a reverse representation.  100 == no free space, 90 = 10% free, and so on.  For read-only tables do a FILLFACTOR = 95 or perhaps 90.  For other stuff FILLFACTOR = 85 is a good starting point since it gives you some head room for INSERTs and UPDATEs after you run DBREINDEX.- DBCC UPDATE STATS collects new statistics but does not remove fragmentation.  It takes less time than DBREINDEX and can be useful if you’ve done a lot of transactions and don’t quite have time for DBREINDEX.- Peter:  “*Auto-update stats I no longer trust to provide accurate statistics over an extended period of time.  Got burned up with this, leave auto-update stats enabled but supplement with regular DBREINDEX or UPDATE STATS as needed.*“

Someone asked me during a discussion, and it is often forgotten what VLDB stands for.  To alleviate confusion, VLDB stands for very large database.  When it has extra Vs it means it is REALLY frikkin huge!

A last few links for reference material:

> [Best practice when optimizing indexes on SQL Server 2005](http://demiliani.com/blog/archive/2007/02/16/5058.aspx)
>
> [Best SQL Server indexing strategies](http://searchsqlserver.techtarget.com/tip/0,289483,sid87_gci1267870,00.html)
>
> [TOP 10 SQL Server Indexing Tips to Improve Performance](http://searchsqlserver.techtarget.com/generic/0,295582,sid87_gci1239952,00.html)

Hope that’s useful.

Technorati Tags: [FILLFACTOR](http://technorati.com/tags/FILLFACTOR),[DBCC](http://technorati.com/tags/DBCC),[DBREINDEX](http://technorati.com/tags/DBREINDEX),[INSERT](http://technorati.com/tags/INSERT),[UPDATE](http://technorati.com/tags/UPDATE),[DELETE](http://technorati.com/tags/DELETE),[Index](http://technorati.com/tags/Index),[Defrag](http://technorati.com/tags/Defrag),[Index Rebuild](http://technorati.com/tags/Index%20Rebuild),[DBM](http://technorati.com/tags/DBM),[Database Mirroring](http://technorati.com/tags/Database%20Mirroring),[CHECKALLOC](http://technorati.com/tags/CHECKALLOC),[CHECKCATALOG](http://technorati.com/tags/CHECKCATALOG),[CHECKFILEGROUP](http://technorati.com/tags/CHECKFILEGROUP),[Index Best Practices](http://technorati.com/tags/Index%20Best%20Practices),[Index Strategy](http://technorati.com/tags/Index%20Strategy),[SQL Server](http://technorati.com/tags/SQL%20Server),[SQL Server 2005](http://technorati.com/tags/SQL%20Server%202005),[VLDB](http://technorati.com/tags/VLDB),[VVLDB](http://technorati.com/tags/VVLDB)

del.icio.us Tags: [FILLFACTOR](http://del.icio.us/popular/FILLFACTOR),[DBCC](http://del.icio.us/popular/DBCC),[DBREINDEX](http://del.icio.us/popular/DBREINDEX),[INSERT](http://del.icio.us/popular/INSERT),[UPDATE](http://del.icio.us/popular/UPDATE),[DELETE](http://del.icio.us/popular/DELETE),[Index](http://del.icio.us/popular/Index),[Defrag](http://del.icio.us/popular/Defrag),[Index Rebuild](http://del.icio.us/popular/Index%20Rebuild),[DBM](http://del.icio.us/popular/DBM),[Database Mirroring](http://del.icio.us/popular/Database%20Mirroring),[CHECKALLOC](http://del.icio.us/popular/CHECKALLOC),[CHECKCATALOG](http://del.icio.us/popular/CHECKCATALOG),[CHECKFILEGROUP](http://del.icio.us/popular/CHECKFILEGROUP),[Index Best Practices](http://del.icio.us/popular/Index%20Best%20Practices),[Index Strategy](http://del.icio.us/popular/Index%20Strategy),[SQL Server](http://del.icio.us/popular/SQL%20Server),[SQL Server 2005](http://del.icio.us/popular/SQL%20Server%202005),[VLDB](http://del.icio.us/popular/VLDB),[VVLDB](http://del.icio.us/popular/VVLDB)
