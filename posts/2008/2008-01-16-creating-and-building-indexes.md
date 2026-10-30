---
title: Creating and Building Indexes
date: 2008-01-16 08:57:16 +0000
last_modified_at: 2008-01-16 08:57:16 +0000
permalink: /2008/01/16/creating-and-building-indexes/
slug: creating-and-building-indexes
wp_id: 349
original_url: https://compositecode.blog/2008/01/16/creating-and-building-indexes/
categories:
- Uncategorized Bits
tags: []
excerpt: Just a few Index 101 type points of advice. When creating an index on an existing table, that has populated data, keep in mind that it could take a long time. If it takes too long and is initiated via the SQL Management Studio the result is very likely to be a timeout. Ideally when …
---

Just a few Index 101 type points of advice.

When creating an index on an existing table, that has populated data, keep in mind that it could take a long time.  If it takes too long and is initiated via the SQL Management Studio the result is very likely to be a timeout.  Ideally when creating an index via the SQL Management Studio it is good to create the index before data population.

Otherwise the best way to create an index is either via T-SQL directly or create the index and maintenance of the index via a SQL Server Job.

To setup an index via SQL Management Studio follow these quick steps.

[![](https://adronhall.smugmug.com/photos/244155616-O.png)](http://adronhall.smugmug.com/gallery/4179028/1/244155616)

First right click and select *Indexes/Keys…* and click.  A dialog will pop up.

[![](https://adronhall.smugmug.com/photos/244155625-M.png)](http://adronhall.smugmug.com/gallery/4179028/1/244155625)

In the dialog, first click add (#1), then name the new index appropriately (#2), and then select the actual column or columns that you want the index placed on (#3).  The results should be similar to the image below.  Once everything is set click on close.

[![](https://adronhall.smugmug.com/photos/244155627-M.png)](http://adronhall.smugmug.com/gallery/4179028/1/244155627)

Next click on save (circled below) and the index will be created.  Remember, if there is anything in the table there is a good change at a time out.

[![](https://adronhall.smugmug.com/photos/244155634-M.png)](http://adronhall.smugmug.com/gallery/4179028/1/244155634)

To do it the truly [über](http://www.m-w.com/dictionary/uber) easy way, execute the following T-SQL command.

> CREATE NONCLUSTERED INDEX IX\_analysis\_time ON dbo.profile\_stats (analysis\_time)

As mentioned, the UI times out trying to build this index for me because of the rows in the table.  This table had a mere 283204 rows and took 4:40.  So you can imagine with more data how much longer it might take.  A small 10-30 second time out for the UI is good considering it locks the interface up while it is trying to create the index.  For more information on the command check out the BOL entry on [MSDN](http://msdn2.microsoft.com/en-us/default.aspx) for [CREATE INDEX](http://msdn2.microsoft.com/en-us/library/aa258260.aspx).  Also it is good to check out the [general index design guidelines](http://msdn2.microsoft.com/en-us/library/ms191195.aspx).  Also check out my more exhaustive [best practices entry for indexes](http://adronbhall.com/blogs/technology__software_development/archive/2007/12/26/6076.aspx).

Keep in mind when creating a index rebuild or index reorganization job that a period of time should be taken to observe the baseline behavior of a table.  Then setup a maintenance task to run on a scheduled basis of when you observe fragmentation and other things starting to occur.  For more information on reorganizing and the specific steps and commands for fragmentation and such, read the [MSDN article](http://msdn2.microsoft.com/en-us/library/ms189858.aspx).

To setup a job follow these steps.

Open up SQL Server Management Studio.

[![](https://adronhall.smugmug.com/photos/244180056-M.png)](http://adronhall.smugmug.com/gallery/4179433/1/244180056)

Expand the *SQL Server Agent*.  Select the *Jobs* Folder and right click, on the menu select *New Job…*.

[![](https://adronhall.smugmug.com/photos/244180060-M.png)](http://adronhall.smugmug.com/gallery/4179433/1/244180060)

The *New Job* Dialog pops up.  Fill out each of the *General* Section fields with pertinent information.

[![](https://adronhall.smugmug.com/photos/244180064-M.png)](http://adronhall.smugmug.com/gallery/4179433/1/244180064)

Next select the *Steps* Section.

[![](https://adronhall.smugmug.com/photos/244180079-M.png)](http://adronhall.smugmug.com/gallery/4179433/1/244180079)

Another sub dialog appears, add the pertinent data to this field and add whatever the maintenance command is that you wish to execute on a regular basis.

[![](https://adronhall.smugmug.com/photos/244180109-M.png)](http://adronhall.smugmug.com/gallery/4179433/1/244180109)

After that, click on OK and then move on to *Schedules*.  Again click on the *New…* Button to bring up another sub dialog.

[![](https://adronhall.smugmug.com/photos/244180125-M.png)](http://adronhall.smugmug.com/gallery/4179433/1/244180125)

A *New Job Schedule* sub dialog appears.  Again, you know what to do.  Add pertinent information.

[![](https://adronhall.smugmug.com/photos/244180133-M.png)](http://adronhall.smugmug.com/gallery/4179433/1/244180133)

Next add any *Alerts*… same process.

[![](https://adronhall.smugmug.com/photos/244180138-M.png)](http://adronhall.smugmug.com/gallery/4179433/1/244180138)

You can even setup a specific response for the alerts.

[![](https://adronhall.smugmug.com/photos/244180146-M.png)](http://adronhall.smugmug.com/gallery/4179433/2/244180146)

Next setup any operators or new operators that you want to receive the alert.

[![](https://adronhall.smugmug.com/photos/244180152-M.png)](http://adronhall.smugmug.com/gallery/4179433/2/244180152)

Select the method that will receive the error alert.

[![](https://adronhall.smugmug.com/photos/244180169-M.png)](http://adronhall.smugmug.com/gallery/4179433/2/244180169)

Click ok until you’re back out to the main screen.  At this point you should see the job item within the job folder.  It will run at the scheduled time or just right click on it and select the run option that way.

[![](https://adronhall.smugmug.com/photos/244180174-M.png)](http://adronhall.smugmug.com/gallery/4179433/2/244180174)

…and that’s it.  Build, run,  and maintain those indexes!
