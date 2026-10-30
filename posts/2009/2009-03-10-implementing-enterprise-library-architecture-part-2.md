---
title: Implementing Enterprise Library Architecture Part 2
date: 2009-03-10 14:14:00 +0000
last_modified_at: 2009-03-10 14:14:00 +0000
permalink: /2009/03/10/implementing-enterprise-library-architecture-part-2/
slug: implementing-enterprise-library-architecture-part-2
wp_id: 604
original_url: https://compositecode.blog/2009/03/10/implementing-enterprise-library-architecture-part-2/
categories:
- Uncategorized Bits
tags: []
excerpt: In the last entry I covered several points about using the Policy Injection Application Block (PIAB) for some AOP based cross cutting work. If interested, check out Part 1. Setting up IIS for Self Signed SSL Certificates on Windows 2003 and Vista. Mention IIS Toolkit, etc. Show IIS security settings for Windows Auth, Basic, Digest, …
---

In the last entry I covered several points about using the Policy Injection Application Block (PIAB) for some AOP based cross cutting work.  If interested, check out [Part 1](/#).

- Setting up IIS for Self Signed SSL Certificates on Windows 2003 and Vista.  Mention IIS Toolkit, etc.
- Show IIS security settings for Windows Auth, Basic, Digest, Anonymous, etc.
- Setup a REST based service and a SOAP based service.
- Setup the web.config file for the IIS based services for basic authentication w/o SSL use.
- Setup the web.config file for the IIS based services for basic authentication w/ SSL use.

Part 3

- Setup a client for access via ASP.NET MVC.
- Setup a client for access via AJAX/JavaScript.
- Setup a client for access via Silverlight.

More notes:

1. State differences between Windows 2003 and Windows 2008 (XP/Vista or IIS 6/7).  Namely the various states of execution needed for Vista/08 for the project to run in elevated administrator access.

2. State short steps, then state elaborated information for each of the configuration/code segments.

3. Make sure to point out these articles for summary:  <http://www.leastprivilege.com/FinallyUsernamesOverTransportAuthenticationInWCF.aspx>

4. Report on the various exceptions for Windows Vista & lack of immediate availability of security elevation for self hosted apps.

5. Report on the differences.

6. What is the *System.Net.WebException: The underlying connection was closed: Could not establish trust relationship for the SSL/TLS secure channel* exception??   <http://weblogs.asp.net/jan/archive/2003/12/04/41154.aspx>  !!  agggh  !!  <http://social.msdn.microsoft.com/Forums/en-US/wcf/thread/bb0fc194-5bf3-4c24-94bb-c86f94c76bc2>  …  <http://community.salesforce.com/sforce/board/message?board.id=NET_development&message.id=3290>   …

**WCF Security Sucks.**

There, I've said it.  Now don't get me wrong, I don't mean the actual security itself, it is just fine.  I mean implementing the mess.  WCF security has so much configuration, by the time one is done sorting through the deluge of options then they run into the blasted use case of transport, SSL, and a whole host of other things.

With WCF, generally, if you want security, go get SSL running NOW.  Don't even beat around the bush, just go do it.  I learned this the hard way and fought and fought and fought with the damned thing.

I simply wanted to enforce a standard username and password schema on REST Services.  How hard could it be I thought?  Well, it isn't really hard, but it sure as hell is frustrating, confusing, and somewhat asinine in nature.  In addition to that IIS supports some security methods, windows service services support others, and the delusion of what goes with what gets more confusing the more one digs into all of this cluster of a mess.

The simple fact is, web services don't secure in a logical straight forward way because services weren't built with security, they were built primarily to be wide open.  Not kind of open, but totally open.  Go read the original documentation on the things and you'll see.  So were does that leave us?  The business world that wants some security around the services that is quick to build, fast to access, easy to scale, etc?  Out of luck, that's where it leaves us.

So now that I've spent the first 4 paragraphs of this entry complaining about the flagrant mess that are web services, WCF, and the associated stacks, here's how one can build out these for true Internet use in the real world.

Building WCF Transport Enabled SSL based Security

Ugh, first, setup the blasted SSL certificates needed for development.

…

<http://www.leastprivilege.com/FinallyUsernamesOverTransportAuthenticationInWCF.aspx>

This is exactly what I want to do… now the question is.  Will it work.  The various pending requirements are INSANE.  UGGGHHH.

…

Try a secure WCF service via a hosted console service.

Try an IIS SSL enabled virtual directory based WCF service.
