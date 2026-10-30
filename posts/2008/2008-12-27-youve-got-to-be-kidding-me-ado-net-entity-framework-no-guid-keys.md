---
title: You've GOT to be kidding me…   ADO.NET Entity Framework no Guid Keys?!?
date: 2008-12-27 07:41:00 +0000
last_modified_at: 2008-12-27 07:41:00 +0000
permalink: /2008/12/27/youve-got-to-be-kidding-me-ado-net-entity-framework-no-guid-keys/
slug: youve-got-to-be-kidding-me-ado-net-entity-framework-no-guid-keys
wp_id: 574
original_url: https://compositecode.blog/2008/12/27/youve-got-to-be-kidding-me-ado-net-entity-framework-no-guid-keys/
categories:
- Uncategorized Bits
tags: []
excerpt: Here I am working through some ADO.NET Entity Framework samples and I come to a standard situation, a Guid as a key. I generate the model and try to do inserts to no avail. I start digging and stumble upon a Stack Overflow answer to this problem. The answer states, Unfortunately, in v1 of the …
---

Here I am working through some ADO.NET Entity Framework samples and I come to a standard situation, a Guid as a key.  I generate the model and try to do inserts to no avail.  I start digging and stumble upon a [Stack Overflow](http://stackoverflow.com/) [answer](http://stackoverflow.com/questions/332273/entity-framework-guid) to this problem.  The answer states,

***Unfortunately, in v1 of the EF this is not supported. While it is
possible with SQL Server to have a column of type “uniqueidentifier”
and to set it’s default value to be “newid()”, with SQL Server 2000
there’s no good way to extract the value that the server generated at
the time you do the insert. This can be done on more recent versions of
SQL Server, though, so the intent is that we should find a clean way to
special case this support in future versions of the EF so it can be
supported on those databases that allow it and not on others. For now,
the work around is to generate the guid on the client (ideally in the
constructor of your object) rather than on the server.***

Ok.  This is stupid.  This is a STANDARD practice for many database teams and developers.  Sure, sure, someone would probably fuss and say, use an int or a bigint.  No, I don't want to, I have my reasons, and I want to use a Guid.  What other bloody purpose does a Guid really have anyway except to garauntee uniqueness!  Ugh.

This I see as a failure of ridiculous magnitudes.  Seriously Microsoft needs to get in gear, and STOP releasing stuff that is supposed to compete with well baked frameworks that is completely unprepared.  The only reason the stupid Entity Framework is getting any penetration is because there are those that won't touch something (no matter how great it is) until Microsoft releases one of their own.  There are reasons behind this too, albeit somewhat stupid.

Ok, rant over, I'm going to go fix my database and use a bunch of ints for now.
