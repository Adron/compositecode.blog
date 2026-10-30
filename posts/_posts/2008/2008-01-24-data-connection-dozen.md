---
title: Data Connection Dozen
date: 2008-01-24 02:59:14 -0800
last_modified_at: 2008-01-24 02:59:14 -0800
permalink: /2008/01/24/data-connection-dozen/
slug: data-connection-dozen
wp_id: 346
original_url: https://compositecode.blog/2008/01/24/data-connection-dozen/
categories:
- Uncategorized Bits
tags: []
excerpt: Alright, so maybe it isn’t a dozen, but it sure seems like that a lot of the time. I was just sitting and going through some old ADO.NET style connection and command creation programmatically, then turned around on another project and started tossing some tables and views into a LINQ Diagram. I couldn’t help but …
---

Alright, so maybe it isn’t a dozen, but it sure seems like that a lot of the time.  I was just sitting and going through some old ADO.NET style connection and command creation programmatically, then turned around on another project and started tossing some tables and views into a LINQ Diagram.  I couldn’t help but think, “Wow, after all these years of .NET, there are now a ton of data access patterns and even numerous data connection patterns, classes, and methods.  I decided then, I’d do a quick enumeration of all the connections, data access patterns, and other such methodologies I’ve used to connect to various data sources.

The first methods I ever used where what was available with ole’ .NET 1.0.  Actually, it wasn’t even 1.0, it was the beta product.  One would instantiate a basic connection object, then instantiate a command object passing the stored procedure name and connection object just created as parameters to the instantiation.  From there I would then end up assigning the various parameters of the actual stored procedure.  There had been a few different ways that this would occur.  Sometimes all with one line, instantiation, assignment of the value, or sometimes I would end up breaking it out into multiple lines.  In yet another scenario I would have to instantiate the parameter objects first, so I would do that and then do assignments.  With the basic beta and 1.0 ADO.NET, one could easily spend dozens of ways connecting to data.

The Wade Reynolds way was rather interesting.  He was the senior developer (more like architect) at SCP Pool Corp while I was there.  He had created an entire self creating OR/M with reflection.  We’d call basic procedures and stuff via the procedure, and the parameters and everything would then be available for us to just assign to.  Overall it was a nice setup.  At the core it was using ADO.NET, but one wouldn’t have been wiser for not realizing it.

The third type I remember was my whole sale stumbling full on into OR/M, data mapper, and the tools that generated these layers and objects.  I had worked at creating some business layers and such myself in the past, but an individual developer under tight deadlines really doesn’t have a lot of spare time to churn out entire extra layers.  With the newly found tools, I started creating much more advanced, maintenance friendly, more business enabled applications at this point.  These generation tools really wiped the slate clean for the headache that the database usually was.

Now we’ve got LINQ, which I guess one could say is an OR/M or at least the engine that drives the entity library which is an OR/M.  I look back at the headaches of keeping things in and in sync with a database and it seems in the last couple years.  Over the last couple of years there has been a drastic simplifying drive, while drawing more business functionality and logic into the usage and creation of the database and the related objects used to keep the database.

I for one, am happy with the modern direction of data access and the clarification of the business elements.
