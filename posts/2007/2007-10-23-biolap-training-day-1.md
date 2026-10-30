---
title: 'BI/OLAP Training Day #1'
date: 2007-10-23 11:03:00 +0000
last_modified_at: 2007-10-23 11:03:00 +0000
permalink: /2007/10/23/biolap-training-day-1/
slug: biolap-training-day-1
wp_id: 411
original_url: https://compositecode.blog/2007/10/23/biolap-training-day-1/
categories:
- Uncategorized Bits
tags: []
excerpt: Yesterday I attended Maxamine Training as part of my initiation at WebTrends. Maxamine is a web site scanner for finding tags, JavaScript, and other assorted objects within a web application/site. The application tool and software is a client application with a server based storage base. All in all, it is a decent product, and for …
---

Yesterday I attended [Maxamine](http://www.maxamine.com/) Training as part of my initiation at [WebTrends](http://www.webtrends.com).  [Maxamine](http://www.maxamine.com/) is a web site scanner for finding tags, JavaScript, and other assorted objects within a web application/site.  The application tool and software is a client application with a server based storage base.  All in all, it is a decent product, and for anyone in need of a web site scanner they should definitely check it out.

Today I’m sitting in day one of Business Intelligence and OLAP Training.  It is an introductory class, which places me at risk of being a little bored, but it is still good to get a solid review with SQL Server 2005 Tools.  My last serious experience was with SQL Server 2000 way back in the days of my Jacksonville work.  SQL Server 2005 has some definite changes that are advantageous over the previous version.  Even though this class is introductory, I decided it would be a great opportunity to create a set of notes and a write up in relation to the class.  These notes and descriptions are what will follow over the next few days.

## Definitions

**OLTP** – **Online Transaction Processing**

This form of database is used primarily for; transaction processing systems, normalized data, optimized for data entry, and has a focus on data integrity.

**OLAP** – **Online Analytical Processing**

This form of a database/warehouse is used primarily for;  analytical systems, denormalized data, heavily indexed, aggregated, and has a focus on reporting and analytics.

**Star Schema** – A Star Schema is a schema that is used in business intelligence OLAP Cubes that has the following characteristics;  single fact table, multiple dimension tables, all dimension tables directly related to fact table, and *allow quickest processing time*.

**Snowflake Schema** – A Snowflake Schema is a schema that is used in business intelligence OLAP Cubes that has the following characteristics;  single fact table, multiple dimension tables, *dimension tables can be related to the fact table through other dimension tables*, slower to process.  Sometimes faster to load than a star schema, but not particularly to process.

**Fact Table Design** – A fact table is created, generally, from multiple OLTP tables, foreign key columns to dimension tables, measure values, and provides a single level of granularity.  Fact tables also should have surrogate keys, be flattened to a star schema, may need to deal with nulls, and is the shared bus for dimensions.  It is also preferred, and sometimes a key need, to not have nulls in the cube.

**Catalog** – A database defined on an OLAP server.

**Cube** – A multidimensional data subset derived from relational tables, or a data warehouse, organized for rapid query response.  What I have called in the past, “Database Views on turbo steroids”!

**Dimensions** – Dimensions represent how the data is accessed.  Usually dimensions represent things, persons, a place, or other type.  The dimensions answer the “who”, “what”, or “where” and the “how” or “by” part of a question.  The dimension presents the how or by part of the question.

**Hierarchy** – A hierarchy is a structure within a dimension that represents the organization of data grouped in levels of most general to most specific.  An **attribute hierarchy** is a flat hierarchy containing a single attribute.  This would include a single level break out such as a product type.  A **user defined hierarchy** is a hierarchical arrangement of attributes.  This would include a break out of product type including sub product type.  Creating more multilevel hierarchy.  A **level** represents a specific detail about data within the dimension.  A **member** represents a specific value contained within a level.

**Measures** are key metrics, often referred to as the key performance indicators (KPI), of a business.  Measures answer the “what” part of the question, and are usually additive, discrete, and easily measured.  One example is that of sales, which is of course easily additive.  Others would include;  cost per item, item sale price, sold price, and other set values.  A calculated measure is the additive sum of the item sale prices, or sold prices for a period of time, or by quarter, or other measurement.

## Best Practices from Day #1

- Use staging areas.  Staging areas help abstract, clean, and often speed up the process.- Surrogate keys should be used for dimension tables.- Use a shared bus of dimensions.- Fact table foreign keys  should be the surrogate keys not business keys.- All measures in fact table need to be the same level of granularity.

## My Two Cents $$

When designing cubes one of the first things that needs to be done is forget.  Forget the OLTP, normalized, technical break out of data and storage.  The first thing to do is to think of the questions that need answered.

- What are the roll ups and sales for product x through y for the first quarter broken down into weeks, possibly even days, or time of days?- What are the locations that sales occur in, what time of year is it and how does that correlate to the weather (summer cloths sell in the summer, winter in the winter, etc)?- What is the break out of planned, projected, and literal sales and expenses against revenue?

This is one of the things that I find absolutely exiting and interesting about the field of business intelligence.  Business intelligence is the good way, best practice way, the smart way to make business decisions based on empirical evidence!

## Now For The Microsoft Architecture

In Microsoft’s Technology Stack the UDM, or Unified Dimensional Model, is the cube itself represented in the Visual Studio SQL Server Analysis Services Interface.  The UDM combines both relational and analytical elements.

For more about specifics of BIDS, SQL Server Management Studio, and other Microsoft Architecture definitions check out [my previous entry on these items](/blogs/technology__software_development/archive/2007/09/11/5361.aspx).

To assist in visualizing what each part of the SSAS Visual Studio IDE make sure to clarify the various levels of abstraction.  The abstracted points to know are the **Data Source Views** (**DSV**) in relation to an actual Cube, where external sources come from, and how the various SSAS mechanisms work in conjunction with SQL Server Integration Services (SSIS).

The data source view provides an abstracted layer the Cube works on.  DSVs are derived upon existing warehouse tables.  These DSVs are also correlated appropriately for presentation within the Cube.  A common mistake is to think that a DSV can serve as a cube.  This is not suggested as major bottlenecks and other issues can occur.

Also, remember that the data warehouse is very important, not just as a data repository but also as an integration server.  Without being able to execute SSIS and associated ETL processes separately from the actual OLTP database is a sure fire death sentence to the OLTP Database Server.

OLAP Database

The OLAP database is the top level container for OLAP Objects.  This top level object contains the various objects;  data source, data source view, cube, dimension, security roles.  The data source is the provider or data connection.  The cube access is provided at this level along with the processing of the cube, retrieval with ROLAP and HOLAP, proactive caching, and write backs.

On the last note, a kind of summary for the class, the following points where made.  One: Don’t use any auto build features.  Two: Have your cube designed with the a
ppropriate keys in place.  Three: Use a star schema data source to simplify dimension management.  Four: Dimensions are shared;  be careful not to duplicate.  Five: Use surrogate keys in base data source.  Six: Add all columns of interest as attributes.

**My Summary**:  The day went well with a lot of material covered.  Fortunately for me since I was exhausted from a crappy night’s sleep, most of the material was merely a refresher.  It was good though to step back through all these things, but also to see the SSAS way of doing things.  The last time, as I’ve probably mentioned, that I was doing this I was condemned to use SQL 2000.  All in all, I had a blast, getting to refresh the material and learning a few things about the SQL Server 2005 Analysis Services.

Technorati Tags: [OLAP](http://technorati.com/tags/OLAP/) , [BI](http://technorati.com/tags/BI/) , [Business Intelligence](http://technorati.com/tags/Business%20Intelligence/) , [SQL Server Analysis Services](http://technorati.com/tags/SQL%20Server%20Analysis%20Services/) , [SQL Server](http://technorati.com/tags/SQL%20Server/) , [Best Practices](http://technorati.com/tags/Best%20Practices/) , [Calculated Measure](http://technorati.com/tags/Calculated%20Measure/) , [Snow Flake Schema](http://technorati.com/tags/Snow%20Flake%20Schema/) , [Star Schema](http://technorati.com/tags/Star%20Schema/) , [Maxamine](http://technorati.com/tags/Maxamine/) , [WebTrends](http://technorati.com/tags/WebTrends/) , [Key Performance Indicator](http://technorati.com/tags/Key%20Performance%20Indicator/) , [KPI](http://technorati.com/tags/KPI/) , [Hierarchy](http://technorati.com/tags/Hierarchy/) , [Dimension](http://technorati.com/tags/Dimension/) , [Cube](http://technorati.com/tags/Cube/) , [HOLAP](http://technorati.com/tags/HOLAP/) , [ROLAP](http://technorati.com/tags/ROLAP/) , [MOLAP](http://technorati.com/tags/MOLAP/)

del.icio.us Tags: [OLAP](http://del.icio.us/popular/OLAP) , [BI](http://del.icio.us/popular/BI) , [Business Intelligence](http://del.icio.us/popular/Business%20Intelligence) , [SQL Server Analysis Services](http://del.icio.us/popular/SQL%20Server%20Analysis%20Services) , [SQL Server](http://del.icio.us/popular/SQL%20Server) , [Best Practices](http://del.icio.us/popular/Best%20Practices) , [Calculated Measure](http://del.icio.us/popular/Calculated%20Measure) , [Snow Flake Schema](http://del.icio.us/popular/Snow%20Flake%20Schema) , [Star Schema](http://del.icio.us/popular/Star%20Schema) , [Maxamine](http://del.icio.us/popular/Maxamine) , [WebTrends](http://del.icio.us/popular/WebTrends) , [Key Performance Indicator](http://del.icio.us/popular/Key%20Performance%20Indicator) , [KPI](http://del.icio.us/popular/KPI) , [Hierarchy](http://del.icio.us/popular/Hierarchy) , [Dimension](http://del.icio.us/popular/Dimension) , [Cube](http://del.icio.us/popular/Cube) , [HOLAP](http://del.icio.us/popular/HOLAP) , [ROLAP](http://del.icio.us/popular/ROLAP) , [MOLAP](http://del.icio.us/popular/MOLAP)
