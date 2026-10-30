---
title: O/R Mapping and Data Access Layers
date: 2007-08-18 11:07:26 -0700
last_modified_at: 2007-08-18 11:07:26 -0700
permalink: /2007/08/18/or-mapping-and-data-access-layers/
slug: or-mapping-and-data-access-layers
wp_id: 439
original_url: https://compositecode.blog/2007/08/18/or-mapping-and-data-access-layers/
categories:
- Uncategorized Bits
tags: []
excerpt: O/R mappers and generator I’ve been doing a moderate amount of research into tools that generate data access layers, entity or object tiers, and other layers for enterprise (or non-enterprise) applications. One of the tools I’ve picked up lately per some encouragement from a coworker is LLBLGen Pro. One can download a demo at the …
---

**O/R mappers and generator**

I’ve been doing a moderate amount of research into tools that generate data access layers, entity or object tiers, and other layers for enterprise (or non-enterprise) applications. One of the tools I’ve picked up lately per some encouragement from a coworker is [LLBLGen](http://www.llblgen.com/) Pro. One can download a [demo](http://www.llblgen.com/pages/demo.aspx) at the [LLBLGen](http://www.llblgen.com/) site to try out.

[LLBLGen](http://www.llblgen.com/) Pro is claimed as the #1 O/R Mapper (I’m not sure this is true, I haven’t seen sales statistics) for the data-access tier in .NET.  The tool can be used against Access, [PostgreSQL](http://www.postgresql.org/), [Oracle](http://www.oracle.com/database/index.html), [mySQL](http://www.mysql.com/products/enterprise/), [DB2](http://www-306.ibm.com/software/data/db2/), and of course [SQL Server](http://www.microsoft.com/sql/default.mspx) 7.0 or greater.  At the same time support is given to the databases, the code generated is independent of the specific database, and for type differences (such as Oracle’s lack of a Boolean type) type converters can be created.

[![](https://www.llblgen.com/pages/userpics/gui_entityinheritancetn.jpg)](http://www.llblgen.com/pages/screenshots.aspx) [![](https://www.llblgen.com/pages/userpics/gui_overviewtn.gif)](http://www.llblgen.com/pages/screenshots.aspx) The tool also creates typed lists for entity fields based on one to one, one to many, or many to one relationships.  [LLBLGen](http://www.llblgen.com/) Pro will also create typed views one one to one mappings, support existing stored procedures with wrapper code which enables a single line of code for calling.  The tool also will accept templates for other peripheral code generation as needed.  For more information on the features, hit the [LLBLGen](http://www.llblgen.com/) [Features List](http://www.llblgen.com/pages/features.aspx).  For tutorials, videos, and samples check out the [tutorials page](http://www.llblgen.com/pages/tutorials.aspx).

As my ranting has ensued about non-use of code generation, the [LLBLGen](http://www.llblgen.com/) site lays out the facts right on the main page.  [LLBLGen](http://www.llblgen.com/) Pro (or really, ANY code generator) will save a huge portion of a project’s development time.  The site puts the number at 50%, I’d put it even higher with a high confidence on my proclamation.  As I’ve often complained about the endless boiler plate code, this tool easily replaces greater than 90% of that, the rest easily removed by good use of object oriented pattern based design practices.

The tool swings in at a relatively cheap [229.99 Euro](http://finance.yahoo.com/currency/convert?amt=229&from=EUR&to=USD&submit=Convert) starting price, which as of this date [translates](http://finance.yahoo.com/currency/convert?amt=229&from=EUR&to=USD&submit=Convert) to [$308.57](http://finance.yahoo.com/currency/convert?amt=229&from=EUR&to=USD&submit=Convert).  ![Big Smile [:D]](/emoticons/emotion-2.gif)

Next I will probably toss in some reviews of .NET Tiers, NHibernate, and other such tools just for good measure.
