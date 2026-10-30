---
title: ALT.NET Seattle – My 2 Cents
date: 2009-03-10 14:06:00 -0700
last_modified_at: 2009-03-10 14:06:00 -0700
permalink: /2009/03/10/alt-net-seattle-my-2-cents/
slug: alt-net-seattle-my-2-cents
wp_id: 602
original_url: https://compositecode.blog/2009/03/10/alt-net-seattle-my-2-cents/
categories:
- Uncategorized Bits
tags: []
excerpt: First off, I have to say ALT.NET Seattle kicked ass. Plain and simple, it is awesome to be able to hang out with a bunch of alpha geeks. The level of discussion starts high and the topics generally stay informative and helpful. The following is a quick summary of the sessions I jumped into and …
---

First off, I have to say ALT.NET Seattle kicked ass.  Plain and simple, it is awesome to be able to hang out with a bunch of alpha geeks.  The level of discussion starts high and the topics generally stay informative and helpful.  The following is a quick summary of the sessions I jumped into and what we covered in each.

Sara Ford – Code Project Site & Agile Process

Sara Ford is the PM for the Code Project Site.  During the session we discussed the various aspects of her team moving from Waterfall to Agile and the points of contention they have and have had.  Sara mentioned that she's moving from 6 years of Waterfall and being de-institutionalized so she can work agile.  I couldn't help but think, that is a very realistic way to describe the process.  Waterfall imprisons a team and one really has to work to get out of that.

Currently the Code Project team that Sara in PM of does 1 week iterations, pair programs, has continuous integration, and has the iterations broken out like this;

- Iteration 1 is new features.
- Iteration 2 is new features and bug fixes.
- Iteration 3 is bug fixes and final branching for the drop.

Two subsequent steps after these three, is regression and deployment.  Both which occur outside of the developer's 3 iteration cycle.  After iteration 3 the team starts on a new iteration 1 to begin the cycle again.

Also mentioned was that

**Sara Ford  –  Code Project site & Agile Process**

Team doesn't do stand ups because of the single room.  If someone needs to know where things are, they are expected to inquire themselves.

…

—

**Scott Hanselman – Why so mean.**

**Alpha Geeks**

Phil Haack / Karen / Eaun

Phil talked to current focus at MS.  TDD & Microsoft

Karen displayed – New intellisense feature so that one can do TDD.

Euan & Karen showed how the new unit tests will do exactly like I blogged HERE.  🙂   Makes me a happy developer.

Deployment is also fixed so that tests run out of bin instead of the OUT directory.  This will resolve a fair amount of issues.  It will be a setting in Test Tools – > Test Execution under the Tools menu.  "Limit number of test results to:"  and make it 1 or something that will limit the number of files.

The fact that that MSTest isn't specifically built for unit testing.  It is NOT the best for Agile (from MSTest Euan) and definitely not particularly good for TDD.

After a good debate & conversation one thing that was applauded was: private test accessors are being deprecated and WILL BE removed in the near future!  This is good news as the private test accessors really perpetuate bad practice.  Unfortunately the ordered tests and test generations are still going to be in the box, but the MSTest Euan did point out that these used for unit tests are a bad idea and also perpetuate bad practice.

[euang@ms.com](mailto:euang@ms.com)

**DAY TWO**

**Extreme w/ large teams**

Oren/Ayende came and spoke on various testing practices.

Feature == 2 hr of work.

testing based on features.  i.e. no real unit tests, but feature testing to assure space.

Seems like when a clear separation of concerns is implemented this is more possible then when not.

A contention of senior vs. junior developer came up.  Alex Hung of Thoughtworks brought up that there should not be this separation in an agile team because of pairing.  The separation is eliminated at a rapid pace when pairing, and thus a major point of Agile.

Ayende posed with the question "what would you do to segment work if you where rebuildnig VS.NET" – his response "get JetBrains to do it".

….

after that I hit up a few different things…

**Oxite review pt 2**.  Oxite is better now & Samper is handling gettin' that straightened out.  Oren/Ayende offered some insight and ideas also.

…

**LINQ** session for a few minutes.

**FP – Functional Programming – F#**

Discussing insurance calculation type application.  Basic asynchronous execution for multi-threading multi-proc multi-core against.

One note was that if C# objects are used – and they're brought in via the imutable keyword than yer screwed.  Gotta bring them in without imutable and just run calcs w/o making changes to the objects.  Speeds up big time because it is then thread safe.

Lazy evaluation – functions – imutable types

The real question of the session for FP though :  How does one know WHEN to use F#.

Large datasets are being used for processing.

OOP C# is too much overhead.

Much of this comes down to F# is less "wordy" than C#.

…

What are the patterns of multi-paradigm programming.

What is functional not appropriate for?

**RDBMS are dead – James Avery – Oren took over.**

Alternates:

- ACID vs.  BASE (not alternative, concept to know)
- Document – Couch DB, SDS, SDB
- Key Store – Memcache, RDHT, Dynamo
- Object – db4o
- Column Database – hmpf
- Row Database – hmpf
- Big Table / Big Tree

Again – Oren jumped in after James Avery got talk started.

ACID fails w/ RDBMS upon scaling.

App level assumes more responsibility but scaling increases.  ->  elaborate for discussion.

Shopping cart uses this for Amazon.

Consistency lacks…

Oren – Building Rhino DHT – always succeed a write…  consistency might be of contention.

massively scalable.

research :: dynamo (discuss with Mukesh)

Architetural decisions help define the database…  such as needing to control the schema or data store creation without having direct access to the database.  i.e. SQL Server can't be changed – such as tables and views added – without specific permission can't be done…  others such as key value or or document databases (couch DB) can literally store a database or whatever as the value of the key value.

…Oren – smart – period

Oren – Rhino HD.

replicated data store.  data is written to one place, then it is immediately replicated to other nodes stores…

Tim Brey – QCon – San Francisco – November

Jim Gray – Memory is the new disk, disk is the new tape.
