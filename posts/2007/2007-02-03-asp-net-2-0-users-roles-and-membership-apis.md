---
title: ASP.NET 2.0 Users, Roles, and Membership APIs
date: 2007-02-03 16:52:00 +0000
last_modified_at: 2007-02-03 16:52:00 +0000
permalink: /2007/02/03/asp-net-2-0-users-roles-and-membership-apis/
slug: asp-net-2-0-users-roles-and-membership-apis
wp_id: 510
original_url: https://compositecode.blog/2007/02/03/asp-net-2-0-users-roles-and-membership-apis/
categories:
- Uncategorized Bits
tags: []
excerpt: A quick how-to. I've done this a dozen times and figured I might as well make an entry in relation to it since I always have to look up where that blasted SQL file is or a step here or there. So with that, a quick and dirty how to on setting up ASP.NET 2.0 …
---

A quick how-to.  I've done this a dozen times and figured I might as well make an entry in relation to it since I always have to look up where that blasted SQL file is or a step here or there.  So with that, a quick and dirty how to on setting up ASP.NET 2.0 Membership, Roles, and Users in SQL Server 2000 or SQL Server 2005.

1. First thing, get an empty database setup on the database server.  It really doesn't matter what it is named, how it is configured or anything like that.  You just need a database.  You can even have other objects in the database;  tables, stored procedures, etc. but they'll be deleted.
2. Next find the aspnet\_regsql.exe executable.  This file is usually located in the C:\WINDOWS\Microsoft.NET\Framework\v2.0.50727 folder.  Once you find the file, execute it.
3. The next screen that pops up will be a standard wizard.  Now at this point all the reminders needed have been provided.  Pick which database you want to install the tables and procs on and continue on through to the end of the wizard.

So that's it.  Now you're ready to setup users, roles, properties/membership information and even extend the data, classes, or other API functionality.

I dug up the following info searching around for this information my last go round.

- For a more thorough explanation with screen shots.  Check out [Scott Gu's Blog](http://weblogs.asp.net/scottgu/archive/2005/08/25/423703.aspx).
- For some more information relating to the whole [personalization API](http://msdn.microsoft.com/library/default.asp?url=/library/en-us/dnvs05/html/Person_fin.asp) and such in .NET 2.0 go check out [MSDN](http://msdn2.microsoft.com/).
- More information about [Personalization in regards to Web Parts](http://kinnie.blogspot.com/2005/05/personalization-web-parts-in-aspnet-20.html).
