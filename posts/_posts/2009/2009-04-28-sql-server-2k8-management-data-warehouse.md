---
title: SQL Server 2k8 Management Data Warehouse
date: 2009-04-28 10:11:05 -0700
last_modified_at: 2009-04-28 10:11:05 -0700
permalink: /2009/04/28/sql-server-2k8-management-data-warehouse/
slug: sql-server-2k8-management-data-warehouse
wp_id: 629
original_url: https://compositecode.blog/2009/04/28/sql-server-2k8-management-data-warehouse/
categories:
- Uncategorized Bits
tags: []
excerpt: One of the new features in SQL Server 2k8 is the Management Data Warehouse. This feature is made up of a data collector, storage, and execution that collects data about the particular databases within the server into a reporting warehouse. This data is stored in the msdb and also in management data warehouse databases that …
---

One of the new features in SQL Server 2k8 is the Management Data Warehouse.  This feature is made up of a data collector, storage, and execution that collects data about the particular databases within the server into a reporting warehouse.  This data is stored in the msdb and also in management data warehouse databases that are created when the *Data Collection* is configured.  The warehouse uses various pieces of SQL Server such as SSIS and other components also.  One of these components is the dcexec.exe file that is responsible for loading and executing SSIS packages that are part of this collection set.

Keep in mind, that there is an API for this warehouse also for extension of the functionality.

The following are the steps for setting up a basic management data warehouse.

[![](/images/adronhall.smugmug.com/photos/523543178_BM7dY-S.png)](http://adronhall.smugmug.com/gallery/8041844_BJqaT#523543178_BM7dY)

Right click on Data Collection and you’ll see the menu below.

[![](/images/adronhall.smugmug.com/photos/523543186_AgobH-S.png)](http://adronhall.smugmug.com/gallery/8041844_BJqaT#523543186_AgobH)

Select Configure Management Data Warehouse.

[![](/images/adronhall.smugmug.com/photos/523543198_fWSxD-S.png)](http://adronhall.smugmug.com/gallery/8041844_BJqaT#523543198_fWSxD)

[![](/images/adronhall.smugmug.com/photos/523543211_EqKRS-S.png)](http://adronhall.smugmug.com/gallery/8041844_BJqaT#523543211_EqKRS)

On this screen I had to actually come back and use the New button to create a new database to use to host the warehouse.  My suggestion is to NOT use an existing database and instead create a new database.

[![](/images/adronhall.smugmug.com/photos/523543223_TpZmw-S.png)](http://adronhall.smugmug.com/gallery/8041844_BJqaT#523543223_TpZmw)

Just leave these unchecked unless you know that one of these accounts need access.

[![](/images/adronhall.smugmug.com/photos/523543234_zA6en-S.png)](http://adronhall.smugmug.com/gallery/8041844_BJqaT#523543234_zA6en)

Now that this is setup for the warehouse host we’ll setup the data collection.

[![](/images/adronhall.smugmug.com/photos/523543277_MrXfu-S.png)](http://adronhall.smugmug.com/gallery/8041844_BJqaT#523543277_MrXfu)

The cache directory will default if a path is not entered, but I’ve entered one just because I felt the inclination to do so.

[![](/images/adronhall.smugmug.com/photos/523543287_ivzGy-S.png)](http://adronhall.smugmug.com/gallery/8041844_BJqaT#523543287_ivzGy)

[![](/images/adronhall.smugmug.com/photos/523543293_VSezV-S.png)](http://adronhall.smugmug.com/gallery/8041844_BJqaT#523543293_VSezV)

[![](/images/adronhall.smugmug.com/photos/523543309_4fkNV-S.png)](http://adronhall.smugmug.com/gallery/8041844_BJqaT#523543309_4fkNV)

The screen shot below, which you might want to click on just to review with a full size shot, shows what is now available in SQL Management Studio.  You’ll see the collection sets, and also many new jobs setup to perform the collection of data for the warehouse.

[![](/images/adronhall.smugmug.com/photos/523543323_rFK9t-S.png)](http://adronhall.smugmug.com/gallery/8041844_BJqaT#523543323_rFK9t)

After setting up the collection click on the Disk Usage option, right click, then select properties.

[![](/images/adronhall.smugmug.com/photos/523543328_o9rQC-S.png)](http://adronhall.smugmug.com/gallery/8041844_BJqaT#523543328_o9rQC)

On this screen select the T-SQL that is in the input parameters text box.  The code is shown below for ease of copy n’ pasting.  🙂

```
DECLARE @dbsize bigint
DECLARE @logsize bigint
DECLARE @ftsize bigint
DECLARE @reservedpages bigint
DECLARE @pages bigint
DECLARE @usedpages bigint

SELECT @dbsize = SUM(convert(bigint,case when type = 0 then size else 0 end))
      ,@logsize = SUM(convert(bigint,case when type = 1 then size else 0 end))
      ,@ftsize = SUM(convert(bigint,case when type = 4 then size else 0 end))
FROM sys.database_files

SELECT @reservedpages = SUM(a.total_pages)
       ,@usedpages = SUM(a.used_pages)
       ,@pages = SUM(CASE
                        WHEN it.internal_type IN (202,204) THEN 0
                        WHEN a.type != 1 THEN a.used_pages
                        WHEN p.index_id < 2 THEN a.data_pages
                        ELSE 0
                     END)
FROM sys.partitions p
JOIN sys.allocation_units a ON p.partition_id = a.container_id
LEFT JOIN sys.internal_tables it ON p.object_id = it.object_id

SELECT
        @dbsize as 'dbsize',
        @logsize as 'logsize',
        @ftsize as 'ftsize',
        @reservedpages as 'reservedpages',
        @usedpages as 'usedpages',
        @pages as 'pages'
```

.csharpcode, .csharpcode pre
{
font-size: small;
color: black;
font-family: consolas, “Courier New”, courier, monospace;
background-color: #ffffff;
/\*white-space: pre;\*/
}
.csharpcode pre { margin: 0em; }
.csharpcode .rem { color: #008000; }
.csharpcode .kwrd { color: #0000ff; }
.csharpcode .str { color: #006080; }
.csharpcode .op { color: #0000c0; }
.csharpcode .preproc { color: #cc6633; }
.csharpcode .asp { background-color: #ffff00; }
.csharpcode .html { color: #800000; }
.csharpcode .attr { color: #ff0000; }
.csharpcode .alt
{
background-color: #f4f4f4;
width: 100%;
margin: 0em;
}
.csharpcode .lnum { color: #606060; }

When you run this the query should give you the results as shown.

[![](/images/adronhall.smugmug.com/photos/523563567_6qwQM-S.png)](http://adronhall.smugmug.com/gallery/8041844_BJqaT#523563567_6qwQM)

One of the sample reports, which won’t have the trend graphs until data is processed multiple times.

[![](/images/adronhall.smugmug.com/photos/523563588_qFNQK-S.png)](http://adronhall.smugmug.com/gallery/8041844_BJqaT#523563588_qFNQK)

In summary.  This feature of SQL Server is really helpful for development to keep track of growth, performance, and other characteristics.  I strongly suggest checking out this reporting capability of SQL Server 2008.

[![kick it on DotNetKicks.com](http://www.dotnetkicks.com/Services/Images/KickItImageGenerator.ashx?url=http%3a%2f%2fwww.adronbhall.com%2fblogs%2ftechnology__software_development%2fpost%2f2009%2f04%2f28%2fSQL-Server-2k8-Management-Data-Warehouse.aspx&bgcolor=3333FF&cfgcolor=CC3300)](http://www.dotnetkicks.com/kick/?url=http%3a%2f%2fwww.adronbhall.com%2fblogs%2ftechnology__software_development%2fpost%2f2009%2f04%2f28%2fSQL-Server-2k8-Management-Data-Warehouse.aspx)

[![Shout it](http://dotnetshoutout.com/image.axd?url=http%3A%2F%2Fwww.adronbhall.com%2Fblogs%2Ftechnology__software_development%2Fpost%2F2009%2F04%2F28%2FSQL-Server-2k8-Management-Data-Warehouse.aspx)](http://dotnetshoutout.com/SQL-Server-2k8-Management-Data-Warehouse)
