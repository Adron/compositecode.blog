---
title: Getting The Bits Swinging in the Business
date: 2010-01-27 00:45:00 +0000
last_modified_at: 2010-01-27 00:45:00 +0000
permalink: /2010/01/27/getting-the-bits-swinging-in-the-business/
slug: getting-the-bits-swinging-in-the-business
wp_id: 688
original_url: https://compositecode.blog/2010/01/27/getting-the-bits-swinging-in-the-business/
categories:
- Uncategorized Bits
tags: []
excerpt: Read Part 1 & Part 2 of this series if you haven't already. Last entry I worked up the basic origins and destinations for the data we have. Now we have to start turning this into something real, something concrete. The following processes include a whole soup of acronyms and other cryptic vocabulary. The most common thing I will probably …
---

Read [Part 1](/blogs/technology__software_development/post/2010/01/13/Where-Is-The-Other-Data-Tracking!-Where-Are-My-Acronyms!.aspx) & [Part 2](/blogs/technology__software_development/post/2010/01/24/Brainstorming-Into-the-Business-Intelligence-Clouds.aspx) of this series if you haven't already.

[Last entry](/blogs/technology__software_development/post/2010/01/24/Brainstorming-Into-the-Business-Intelligence-Clouds.aspx) I worked up the basic origins and destinations for the data we have. Now we have to start turning this into something real, something concrete. The following processes include a whole soup of acronyms and other cryptic vocabulary. The most common thing I will probably use is the ETL acronym, which stands for Extract, Transform, and Load. This is the process of bridging the data to the various originations and destination and moving that data appropriately.

In the last entry I finalized the originations and destinations as shown below;

|  |  |
| --- | --- |
| **Originations** | |
| Excel & Access (Office 2007) | \*.mdb, \*.xlsx, and \*.csv/\*.txt data stores |
| Internal Account Software (IAS) | This one is a prospective can of worms.  Proprietary layouts, de-normalized & normalized data, and all sorts of redundant, non-atomic data.  This sounds like an accounting package right?  :p |
| [Webtrends](http://www.webtrends.com) Analytics Data Exchange Web Services ([DX](http://developer.webtrends.com/community/dx/)) | Webtrends web services provide REST style architecture, with the ability for data to be retrieved in XML, JSON, HTML, or other formats (we can add more if need be, just let us know). |
| Point of Sale System (POS) | This system provides two daily exports, one at 6:00am and one at noon for processing.  The export format is \*.csv. |

|  |  |
| --- | --- |
| **Destination** | |
| SSRS | SQL Server Reporting Services, with the core underlying data stored in SQL Server. |

In my previous entry you may have noticed that I had posted SSIS with the Destination list.  Being one that corrects themselves when mistaken, I took it out, as it does not belong there.  The SSIS is our tool that will perform the ETL functionality for this project.

At this point we are finally going to get into the dirty bits of these pieces of technology, and how we need to tie them together.  I am going to attack them over the next few entries based on the order in the lists above.  The first item, is the Excel & Access 2007 customer relations listings from sales.  Here?s a description and a few shots of what this thing looks like.

The access database is setup with a very simple relational data schema.  This is shown below (click image for larger view).

[![](/images/adronhall.smugmug.com/Software/Databases/Enterprise-and-Business/Access-04/773539239_EChHJ-M.png)](http://adronhall.smugmug.com/Software/Databases/Enterprise-and-Business/11053098_C9FPX#773539239_EChHJ)

You can see there are pretty standard pieces of data, in a generally normalized (3rd form for the most part) structure.  This is fine.

Next is a shot of the data entry screen for adding opportunities.  There are respective screens for customers and employees.  Everything needed for a basic customer list & tracking basic things.  Nothing too extravagant here either.  Again, all is fine.

[![](/images/adronhall.smugmug.com/Software/Databases/Enterprise-and-Business/Access-01/773539217_aTto8-S.png)](http://adronhall.smugmug.com/Software/Databases/Enterprise-and-Business/11053098_C9FPX#773539254_mD2fq)

Below is a simple report that shows the available opportunities that are open.

[![](/images/adronhall.smugmug.com/Software/Databases/Enterprise-and-Business/Access-05/773539259_Pi269-S.png)](http://adronhall.smugmug.com/Software/Databases/Enterprise-and-Business/11053098_C9FPX#773539254_mD2fq)

Another report showing the forecasts.

[![](/images/adronhall.smugmug.com/Software/Databases/Enterprise-and-Business/Access-03/773539226_cuUqA-S.png)](http://adronhall.smugmug.com/Software/Databases/Enterprise-and-Business/11053098_C9FPX#773539254_mD2fq)

Below is another forecast sliced grid.

[![](/images/adronhall.smugmug.com/Software/Databases/Enterprise-and-Business/Access-02/773539237_gWCf5-S.png)](http://adronhall.smugmug.com/Software/Databases/Enterprise-and-Business/11053098_C9FPX#773539254_mD2fq)

So all that seems normal enough.  But the processes are what makes things tricky.  If everyone just managed sales from the database, all would be right in the world.  The first thing that breaks this is that each sales person enters their sales during the day and other information in a spreadsheet that is not linked to the underlying database.  Someone each morning puts the previous days sales information.  This of course, breaks down data integrity.  Below is a sample sheet that is used each day.

[![](/images/adronhall.smugmug.com/Software/Databases/Enterprise-and-Business/Excel-02/773539254_mD2fq-S.png)](http://adronhall.smugmug.com/Software/Databases/Enterprise-and-Business/11053098_C9FPX#773539254_mD2fq)

One thing that Excel is used for, that doesn?t break reports is the lists of prospective customers to call.  As shown below.

[![](/images/adronhall.smugmug.com/Software/Databases/Enterprise-and-Business/Excel-01/773539249_nAt3C-S.png)](http://adronhall.smugmug.com/Software/Databases/Enterprise-and-Business/11053098_C9FPX#773539254_mD2fq)

Now that we have a break down of the Excel & Access Customer Relations Management Software, I will move onto the other pieces of technology in the next entry.  This is the data point that has the most prospective data risk, so I put it at the top of the list to cover first.  After I cover each of the systems, we will move into the architecture of the system overall.  So keep reading, more juicy bits to come.
