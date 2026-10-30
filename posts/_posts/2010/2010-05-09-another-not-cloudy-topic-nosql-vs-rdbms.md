---
title: Another Not-Cloudy Topic, NoSQL vs. RDBMS?
date: 2010-05-09 19:37:12 -0700
last_modified_at: 2010-07-22 18:27:51 -0700
permalink: /2010/05/09/another-not-cloudy-topic-nosql-vs-rdbms/
slug: another-not-cloudy-topic-nosql-vs-rdbms
wp_id: 6
original_url: https://compositecode.blog/2010/05/09/another-not-cloudy-topic-nosql-vs-rdbms/
categories:
- AWS
- Azure
- Cloud Speak
tags: []
excerpt: 'Ok, so maybe it is a cloudy topic. There are a zillion reasons to use an RDBMS (Relational Database Management System). SQL Server, Oracle, and a number of others are well built, can handle huge numbers of transactions, and have great data integrity. However as Dare Obasanjo asks on his blog, Building Scalable Websites: Are …'
---

Ok, so maybe it is a cloudy topic.  There are a zillion reasons to use an RDBMS (Relational Database Management System).  SQL Server, Oracle, and a number of others are well built, can handle huge numbers of transactions, and have great data integrity.  However as Dare Obasanjo asks on his blog, [Building Scalable Websites:  Are Relational Databases Compatible with Large Scale Websites?](http://www.25hoursaday.com/weblog/2010/03/10/BuildingScalableDatabasesAreRelationalDatabasesCompatibleWithLargeScaleWebsites.aspx) It brings to bare an important question which so far has been answered time and time again, ***“no”***.  However there are still some that argue that it does scale, such as Dennis Forbes [Getting Real About NoSQL and the SQL-Isn’t-Scalable Lie](http://www.yafla.com/dforbes/Getting_Real_about_NoSQL_and_the_SQL_Isnt_Scalable_Lie/).

Being RDMBSs don’t scale horizontally is where large web sites have their issues.  [Myspace](http://www.myspace.com), [Facebook](http://www.facebook.com), [Digg](http://www.digg.com/), [Twitter](http://twitter.com), and others when put under the pressure of their scalability requirements, have thrown away their primary RDBMSs for various [NoSQL Alternatives](http://en.wikipedia.org/wiki/NoSQL).

Some still argue that RDBMSs can hold under the weight of large sites, and it seems like they should with hundreds of gigs of memory, SAN arrays, and other hardware offerings.  However one would find it nearly impossible to find any horizontally scalable offerings in the RDBMS camp that can handle millions of users (such as those sites mentioned above have) on a consistent and reliable basis.  The drives get thrashed, the transactions get queued and lost, or worse data never even gets to the RDMBS because of the way the RDBMS Architecture works.  Even Dennis Forbes admits, *“Such a platform can yield very satisfactory performance for tens or hundreds of thousands of active users in most usage and application scenarios (where generally clients talk to a farm of middleware servers).”* Which leaves me asking Dennis, “so what about when your site reaches millions of users?  The Enterprise Corporate world rarely reaches that, but the Internet Consumer world has gotten there a number of times already, what’s the solution?”

Simple fact of the matter is, it is rare to impossible to find the hardware, price point, and technical architecture combination that would allow an RDBMS handle millions of users.  I won’t rule it out in the future, but right now these systems just do not scale to that volume.

***Webtrends doesn’t use RDBMSs for Web Analytics***

A first hand experience I have with RDMBSs failing to handle what is and needs to be provided is at [Webtrends](http://www.webtrends.com).  At [Webtrends](http://www.webtrends.com) we had tried (more than just we, engineers at the company far before I was there) had tried to cram the massive volume of transactions, processing, and other data into an RDBMS.  Why?  Simple, RDBMSs are easy to develop against.  However, the RDBMS just couldn’t handle the volume.  In the meantime flat file, object, and document databases ([NoSQL](http://en.wikipedia.org/wiki/NoSQL)) have provided an alternative that works.  So I fail to see how an RDBMS can actually handle the volume of data of massive systems such as [Webtrends](http://www.webtrends.com) or the aforementioned sites.

***[Microsoft Azure](http://www.microsoft.com/windowsazure/windowsazure/) provides a real bridge***

One might ask themselves, “Well I have an RDBMS now and it is growing into realms that it soon won’t be able to handle, where stands a solution?”  Microsoft provides several options that step into the void to fill the gap (and yes, there are other cloud solutions, but nobody provides as many options as Azure does at the moment).

The first option is an RDMBS called [Microsoft SQL Azure](http://www.microsoft.com/windowsazure/sqlazure/).  Now you might think, “wait a second, you have just been griping about RDBMSs just like the [NoSQL](http://en.wikipedia.org/wiki/NoSQL) crew does”, which is true.  But one of the major uses of the [Microsoft SQL Azure](http://www.microsoft.com/windowsazure/sqlazure/) relational database service is to provide a basic starting point to migrate or at least start a cloud based application.  I wouldn’t suggest in a cloud environment one builds to a relational database unless there is a very solid reason.  Again, the relational database is stuck with horizontal growth restrictions, which is one of the primary reasons Microsoft currently keeps the [SQL Azure](http://www.microsoft.com/windowsazure/sqlazure/) instances to a 1 or 10 GB limit.

*(As I wrote this, I wasn’t aware of but realized while searching the links that Amazon actually has* [*relational data services*](http://aws.amazon.com/rds/) *now ? i.e. RDBMS in the cloud also)*

The second option is the [Microsoft Azure](http://www.microsoft.com/windowsazure/windowsazure/) Storage.  The storage can be [blob](http://go.microsoft.com/fwlink/?LinkId=153400), [tables](http://go.microsoft.com/fwlink/?LinkId=153401) (not like RDBMS tables), or [queues](http://go.microsoft.com/fwlink/?LinkId=153402).  The combination of these features enables one to build massive horizontally scalable data stores.  Which removes the single machine, horizontal scalability issues of RDBMSs.

***Ok, ok, ok, now I am sounding a bit like a shill***

So let me drag into this write up the rough spots.  Sure, the horizontal scalability of the storage mechanisms is practically endless compared to an RDBMS.  But then we run into the ease in which to get data.  Questions come up such as;

- How do I query my data storage?
- How should I store my data?
- How should I design it along with the other options?

So yes, there is significantly more architecture to build around alternatives at this point.  RDBMS Systems have plenty written around the existing options, but the [NoSQL](http://en.wikipedia.org/wiki/NoSQL) Alternatives and the storage that is available in the cloud (Azure, AWS, Google, or whatever cloud) doesn’t have a thoroughly built out system anywhere near the options that are available with RDBMSs.  So there is significantly more work to do when planning for this volume of data, traffic, and scalability.

The other thing to consider is the price point.  The storage itself is about 100 times cheaper than an RDBMS in the cloud or even an RDBMS of a seriously heavy duty system.  But the question of cost comes to bare when one figures out the transactions, and other interactions among other system inside and outside of the cloud.  These costs can sometimes be prohibitive without a solid, reliable, clean, and well thought out architecture.

Anyway, those are the junctures the industry seems to be at between really big RDBMSs and moving things to [NoSQL](http://en.wikipedia.org/wiki/NoSQL) Alternatives or getting things pushed into the cloud itself.  For further information about what I’ve discussed here check out some of the following
sites:

- [Microsoft Windows Azure](http://www.microsoft.com/windowsazure/)
- [Windows SQL Azure](http://www.microsoft.com/windowsazure/sqlazure/)
- [Windows Azure Storage Highlights](http://msdn.microsoft.com/en-us/azure/cc994380.aspx)

Cloud Services I didn’t mention but are viable alternatives for hitting the limitations of your RDBMS.

- [Amazon Web Services](http://aws.amazon.com/)
- [Amazon Relation Database Services](http://aws.amazon.com/rds/)
- [Google App Engine](http://code.google.com/appengine/)
