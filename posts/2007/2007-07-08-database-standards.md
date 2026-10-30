---
title: Database Standards
date: 2007-07-08 11:40:00 +0000
last_modified_at: 2007-07-08 11:40:00 +0000
permalink: /2007/07/08/database-standards/
slug: database-standards
wp_id: 457
original_url: https://compositecode.blog/2007/07/08/database-standards/
categories:
- Uncategorized Bits
tags: []
excerpt: I’ve been on a run about coding standards lately, reading about them, figuring out which to follow and which to not follow. Well one thing I had not been looking at much was database standards. I realized I had a bunch of questions; how do you name tables, according to what schema, are views concatenated …
---

I’ve been on a run about coding standards lately, reading about them, figuring out which to follow and which to not follow.  Well one thing I had not been looking at much was database standards.  I realized I had a bunch of questions;  how do you name tables, according to what schema, are views concatenated names correlated to their respective tables, do stored procedures have verb noun correlation, do functions get named similar to stored procedures, do we prefix database objects with shortened abbreviations and such related to what they are?  Well I’ve started keeping a list of things I’m starting to prefer when designing and building a database.  Enjoy…

**Database Standards** :: Build 0.01

1. Table Names should be named to a singular of the data object they hold.  At least when utilizing a domain or business object pattern approach to development, for readability of generated code (yeah, a standard based on generated code!) tables should be named singular.  Examples would include;  *Car*, *Bike*, *Train*, or if one had more granular break downs *Wheel*, *WheelType*, *WheelTire*.
2. Database objects should use casing just like code objects.  So if there is a Car Object that has Wheel Objects and a Wheel Type Structure the tables in the database should be named accordingly with the same casing;  *Car*, *Wheel*, *WheelType*.
3. Artificial name spaces should be setup for database objects.  If a table is directly related to a particular table, such as a Wheel having a type in the *WheelType* and a tire type in the *WheelTire* table, each should be prefixed as written here with *Wheel*.  This assures easy visual coordination of tables that are closely related via domain logic, business logic, and via referential relationships within the database itself.
4. If one goes with the base table pattern (similar to using base classes) and sets up a base table to hold vehicle information the base table should be post-fixed or pre-fixed to the associated tables.  Thus we would have *VehicleCar*, *VehicleTrain*, or *VehicleBike* based off of the *Vehicle* base table.  The reverse would look like CarVehicle, TrainVehicle, and BikeVehicle.  I prefer the fore-mentioned naming convention but the later convention is more readable in my opinion.

So far, that’s what I got.  If I get to deal more with database standards I’ll definitely post them here.  Anyone else have ideas, notions, arguments, or opinions on what should change, be added, or deleted?  Submit a comment.

[![kick it on DotNetKicks.com](http://www.dotnetkicks.com/Services/Images/KickItImageGenerator.ashx?url=http://adronbhall.com/blogs/technology__software_development/archive/2007/07/08/4939.aspx)](http://www.dotnetkicks.com/kick/?url=http://adronbhall.com/blogs/technology__software_development/archive/2007/07/08/4939.aspx)
