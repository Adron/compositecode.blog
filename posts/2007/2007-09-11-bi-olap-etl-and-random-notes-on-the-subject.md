---
title: BI, OLAP, ETL, and Random Notes on the Subject
date: 2007-09-11 03:34:32 +0000
last_modified_at: 2007-09-11 03:34:32 +0000
permalink: /2007/09/11/bi-olap-etl-and-random-notes-on-the-subject/
slug: bi-olap-etl-and-random-notes-on-the-subject
wp_id: 428
original_url: https://compositecode.blog/2007/09/11/bi-olap-etl-and-random-notes-on-the-subject/
categories:
- Uncategorized Bits
tags: []
excerpt: I had a few conversations, actually more like 6 different conversations, pertaining to BI (Business Intelligence), OLAP (Online Analytical Processing), Cube or UDM (Unified Dimensional Model) Processing, ETL (Extract Transform Load), normalization and de-normalization for Reporting Purposes, and other such related topics. It seems that there are tons of BI Projects starting up around the …
---

I had a few conversations, actually more like 6 different conversations, pertaining to BI (Business Intelligence), OLAP (Online Analytical Processing), Cube or UDM (Unified Dimensional Model) Processing, ETL (Extract Transform Load), normalization and de-normalization for Reporting Purposes, and other such related topics.  It seems that there are tons of BI Projects starting up around the area.  Some of the projects are small “it’s just a possibility” type of project to the fully ramped we’re going to “toss a few million at this and get some serious BI out of it” type of project.

With all these conversations I decided to do a quick write up of what BI is all about.  I figured, what better way to refresh the memory of experience than to do some writing on the topic.

First I gotta knock out the crazy acronyms.  There are a bunch.

|  |  |
| --- | --- |
| - AMO – Analysis Management Objects.  API for Analysis Services (SSAS). - OLTP – Online Transaction Processing.  OLTP is the storage medium for databases that are used in production environments for day to day input, output, delete, and update of data. - OLAP – Online Analytical Processing.  OLAP is the storage medium specific to processing of BI reports and such.  It is geared not toward input and output, but solely output and query reporting via MDX. - KPI – Key Performance Indicator.  A primary indicator for a business, usually displayed via a dashboard or similar report for change reference. - BIDS – Business Intelligence Development Studio.  Basically this is Visual Studio 05 with the appropriately installed templates and such for building, maintaining, and developing data OLAP Cubes. - ETL – Extract Transform Load.  The process of moving, copying, transforming, or otherwise changing data during movement from one location into another; usually from an OLTP source to an OLAP source. | - SSAS – SQL Server Analysis Services. - SSIS – SQL Server Integration Services. - XMLA – XML for Analysis.  Used for scripting SSAS. - MDX – Multidimensional Expressions.  Similar to SQL in syntax but designed for execution against OLAP Cubes for reporting demands. - ROLAP – Relational Online Analytical Processing.  Data is stored in a relational database for the cubes. - MOLAP – Multidimensional Online Analytical Processing.  Data is stored in a proprietary structure for fast retrieval. - HOLAP – Hybrid Online Analytical Processing.  Data is stored in a mix of relational and multidimensional mediums. - BI – Business Intelligence.  A general description of the particular part of the industry that focuses on OLAP Warehousing, Reporting, and related services and solutions. - DSV – Data Source View.  A collection of tables located in the data warehouse, usually a representation of logical keys and relationships. - UDM – Unified Dimensional Model. The measure groups and dimensions that define BI data.  Synonymous with a cube. |

 There are also a few key concepts that one must understand.  I’m just going to discuss and define these concepts below, in a somewhat haphazard way as I think of them.

A *dimension* is a way data is cut, what appears vertically or horizontally on a report, to display information based on data.  A *dimension* can be broken out by *time*, *linked*, *parent-child, standard* or other means.  The data the *dimensions* cut are stored via a fact table.  A fact table stores all the detailed values for the *measures* or *facts*.  A *fact* table is usually a denormalized table with the bulk of the data to be reported on.  The main thing to know, is that each *dimension* is a way to break out the data, across various measurements such as time.  Another key word to know is that when data forms grouped attributes they are referred to as a *natural hierarchy*.

One can also have a *dimension* *table* that has a break down of information to use as a dimension cut across the data.  For instance a product could be displayed in the *fact* table, and the individual rows could be *aggregated* across the product types.

One odd thing, at least for newcomers to the BI world, is how often a relational database table has an *application key* but a *surrogate key* is assigned the row once it is in the OLAP Cube or Warehouse.  The reason this is often, if not always done, is because the *application key* could lose its uniqueness once brought across ETL or stored over a period of times to represent points of data.  If this occurs one needs a *surrogate key* to prevent confusion about which row is which.

I’ve puttered out at this point, and am contemplating posting this incomplete write up at a wonderful 1:00am.  But instead I’ll sleep on it so I’ll probably post it around 8am or so.  I’ll be writing a follow up to complete out the basic concepts and ideas behind BI.  In the near future, maybe even via a screen captured VLOG entry I’ll post how to actually setup and prepare a sample OLAP Cube for reporting via BIDS.  In the meantime stay tuned for the awesome power of the *Snowflake* and *Star Designs*!
