---
title: Let’s Really Discuss Lock In
date: 2018-06-15 16:27:18 -0700
last_modified_at: 2018-06-15 16:27:18 -0700
permalink: /2018/06/15/lets-really-discuss-lock-in/
slug: lets-really-discuss-lock-in
wp_id: 14149
original_url: https://compositecode.blog/2018/06/15/lets-really-discuss-lock-in/
categories:
- Architecture
- Ideas
tags:
- anti-patterns
- antipatterns
- architecture
- cloud computing
- cloud computing lockin
- lock-in
- lockin
- software development
- software lockin
- technology
excerpt: For to long lock-in has been referred to with an almost entirely negative connotation even though it can be inferred in positive and negative situations. The fact is that there’s a much more nuanced and balanced range to benefits and disadvantages of lock-in. Often this may even be referred to as this or that dependency, …
image: /wp-content/uploads/2018/06/keyspace.jpg
---

For to long lock-in has been referred to with an almost entirely negative connotation even though it can be inferred in positive and negative situations. The fact is that there’s a much more nuanced and balanced range to benefits and disadvantages of lock-in. Often this may even be referred to as this or that dependency, but either way a dependency often is just another form of lock in. Weighing those and finding the right balance for your projects can actually lead to lock-in being a positive game changer or something that simply provides one a basis in which to work and operate. Sometimes lock-in actually will provide a way to remove lock-in by providing more choices to other things, that in turn may provide another variance of lock-in.

## Concrete Lock-in Examples

### The JavaScript Lock-In

![IT Security icons. Simplus series](/wp-content/uploads/2018/06/simplus-60-it-security.jpg)Take the language we choose to build an application in. JavaScript is a great example. It has become the singular language of the web, at least on the client side. This was long ago, a form of lock-in that browser makers (and standards bodies) chose that dictated how and in which direction the web – at least web pages – would progress.

JavaScript has now become a prominent language on the server side now too thanks to Node.js. It has even moved in as a first class language in serverless technology like AWS’s Lambda. JavaScript is a perfect example of a language, initially being a source of specific lock-in, but required for the client, that eventually expanded to allow programming in a number of other environments – reducing JavaScript’s lock in – but displacing lock in through abstractions to other spaces such as the server side and and serverless functions.

### The .NET Windows SQL Server Lock In

![IT Security icons. Simplus series](/wp-content/uploads/2018/06/lockin2.jpg)JavaScript is merely one example, and a relatively positive one that expands one’s options in more ways than limits one’s efforts. But let’s say the decision is made to build a high speed trading platform and choose SQL Server, .NET C#, and Windows Server. Immediately this is a technology combination that has notoriously illuminated in the past **\*** how lock-in can be extremely dangerous.

This application, say it was built out with this set of technology platforms and used stored procedures in SQL Server, locking the application into the specific database, used proprietary Windows specific libraries in .NET with the C# code, and on Windows used IIS specific advances to make the application faster. When it was first built it seemed plenty fast and scaled just right according to the demand at the time.

Fast forward to today. The application now has a sharded database when it hit a mere 8 Terabytes, loaded on two super pumped up – at least for today – servers that have many cores, many CPUs, GPUs, and all that jazz. They came in around $240k each! The application is tightly coupled to a middle tier, that is then sort of tightly coupled to those famous stored procedures, and the application of course has a turbo capability per those IIS Servers.

But today it’s slow. Looking at benchmarks and query times the database is having a hard time dealing with things as is, and the application has outages on a routine basis for a whole variation of reasons. Sometimes tracing and debugging solves the problems quickly, other times the servers just oversubscribe resources and sit thrashing.

Where does this application go? How does one resolve the database loading issues? They’ve already sunk a half million on servers, they’re pegged out already, horizontally scaling isn’t an option, they’re tightly coupled to Window Servers running IIS removing the possibility of effectively scaling out the application servers via container technologies, and other issues. Without recourse, this is the type of lock in that will kill the company if something is changed in a massive way very soon.

To add, this is the description of an actual company that is now defunct. I phrased it as existing today only to make the point. The hard reality is the company went under, almost entirely because of the costs of maintaining and unsustainable architecture that caused an exorbitant lock in to very specific tools – largely because the company drank the cool aid to use the tools as suggested. They developed the product into a corner. That mistake was so expensive that it decimated the finances of the company. Not a good scenario, not a happy outcome, and something to be avoided in every way! This is truly the epitomy of negative lock in.

Of course there’s this distinctive lock in we have to steer clear from, but there’s the lock in associated with languages and other technology capabilities that will help your company move forward faster, easier, and with increasing capabilities. Those are the choices, the ties to technology and capabilities that decision makers can really leverage with fewer negative consequences.

## The “Lock In” That Enables

![IT Security icons. Simplus series](/wp-content/uploads/2018/06/keys.jpg)One common statement is, “the right tool for the job”. This is of course for the ideal world where ideal decisions can be made all the time. This doesn’t exist and we have to strive for balance between decisions that will wreck the ship or decisions that will give us clear waters ahead.

For databases we need to choose the right databases for where we want to go versus where we are today. Not to *[gold plate](http://wiki.c2.com/?GoldPlating)* the solution, but to have intent and a clear focus on what we want our future technology to hold for us. If we intend to expand our data and want to maintain the ability to effectively query – let’s take the massive SQL Server for example – what could we have done to prevent it from becoming a debilitating decision?

A solution that could have effectively come into play would have been not to shard the relational database, but instead to either export or split the data in a more horizontal way and put it into a distributed database store. Start building the application so that this system could be used instead of being limited by the relational database. As the queries are built out and the tight coupling to SQL Server removed, the new distributed database could easily add nodes to compensate for the ever growing size of the data stored. The options are numerous, that all are a form of lock-in, but not the kind that eventually killed this company that had limited and detrimentally locked itself into use of a relational database.

At the application tier, another solution could have been made to remove the ties to IIS and start figuring out a way to containerize the application. One way years ago would have been to move away from .NET, but let’s say that wasn’t really an option for other reasons. The idea to mimic containerization could have been done through shifting to a self-contained web server on Windows that would allow the .NET application to run under a singular service and then have those services spin off the application as needed. This would decouple from IIS, and enable spreading the load more quickly across a set number of machines and eventually when .NET Core was released offer the ability to actually containerize and shift entirely off of Windows Server to a more cost efficient solution under Linux.

These are just some ideas. The solutions of course would vary and obviously provide different results. Above all there are pathways away from negative lock in and a direction toward positive lock in that enables. Realize there’s the balance, and find those that leverage lock in positively.

**Nuanced Pedantic Notes:**

- Note I didn’t say all examples, but just that this combo has left more than a few companies out on a limb over the years. There are of course other technologies that have put companies (people actually) in awkward situations too. I’m just using this combo here as an example. For instance, probably some of the most notorious lock in comes from the legal ramifications of using Oracle products and being tied into their sales agreements. On the opposite end of the spectrum, Stack Overflow is a great example of how choosing .NET and scaling with it, SQL Server, and related technologies can work just fine.
