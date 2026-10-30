---
title: Data Access Layer Responsiblities
date: 2006-10-01 19:03:00 -0700
last_modified_at: 2006-10-01 19:03:00 -0700
permalink: /2006/10/01/data-access-layer-responsiblities/
slug: data-access-layer-responsiblities
wp_id: 539
original_url: https://compositecode.blog/2006/10/01/data-access-layer-responsiblities/
categories:
- Uncategorized Bits
tags: []
excerpt: Of all the segments of layers and designs for software one of the most common is the Data Access Layer, often referred to as the DAL. For well over 5 years I’ve used dedicated DALs to segment the business logic and user interface from the actual database. The data access layer serving the purpose to …
---

Of all the segments of layers and designs for software one of the most common is the Data Access Layer, often referred to as the DAL.  For well over 5 years I’ve used dedicated DALs to segment the business logic and user interface from the actual database.  The data access layer serving the purpose to seperate the intricacies of the referential integrity and other such important necessities of the database from the programmer dealing with the business logic and flow from the user perspective.

Often times I’ve used DALs simply to describe my data objects, which are related directly to the tables and schema of the database itself.  When doing so I’ve been able to use the DAL that is generated from Codesmith by the default business object templates or other items that are included.  I’ve been able to grab some really great add ons to Codesmith such as .NET Tiers.  Following Microsoft’s Patterns and Practices this “extra” for Codesmith rocks.  It enables one to develop the DAL, deep fills, WCF bases, and other features.  A very nice set of generated procs are included along with that.

I’m still amazed how many groups still churn out their own “custom” and very proprietary data access layers.  The amount of time, money, and proprietary knowledge investment in such a layer is extensive.  I’ve always thought the effort, time, and money could be spent more specifically on the business logic and processing layers instead.  DALs are usually simple, no matter the complexity or chores performed by such a layer, the generated DALs that are provided via Codesmith and especially .NET Tiers are well worth the swap.  Dedicating human resources to write up this layer manually seems counter intuitive.  Of course, there are always reasons to hand code parts if need be, just rarely does this opportunity arise.

I wonder though, what other purposes should a data access layer serve?
