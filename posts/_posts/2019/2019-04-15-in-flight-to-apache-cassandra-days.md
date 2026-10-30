---
title: In Flight to Apache Cassandra Days
date: 2019-04-15 20:10:53 -0700
last_modified_at: 2019-04-15 20:10:57 -0700
permalink: /2019/04/15/in-flight-to-apache-cassandra-days/
slug: in-flight-to-apache-cassandra-days
wp_id: 15732
original_url: https://compositecode.blog/2019/04/15/in-flight-to-apache-cassandra-days/
categories:
- cassandra
- Community
- Databases
- Distributed Things
- Meetups n' Such
- Unknown Code Ramblings
- Workshops | Courses | Training
tags:
- apache cassandra
- application development
- cassandra
- cassandra day
- data modeling
- introduction to apache cassandra
excerpt: Another flight down to the bay area. Today it was Alaska Air Flight 330 from Seattle to San Jose. It was mostly a clear day at start, with a solid layer of bright cloud cover exiting Washington on the way down to Oregon. As we crossed over that arbitrary human defined line of Oregon and …
image: /wp-content/uploads/2018/10/fixed1.png
---

Another flight down to the bay area. Today it was [Alaska Air](https://www.alaskaair.com/) [Flight 330](https://flightaware.com/live/flight/ASA330) from Seattle to San Jose. It was mostly a clear day at start, with a solid layer of bright cloud cover exiting Washington on the way down to Oregon. As we crossed over that arbitrary human defined line of Oregon and California, nature presented us with even more perfectly glowing bright cloud cover. This is Cascadia after all and it’s basically covered in clouds the majority of the time. On departure I also noted Bremerton has three aircraft carriers in dock along with a normal plethora of other naval vessels. The amount of naval power in the area is always pretty awe inspiring.

Why was I in flight once again? I am heading down to teach with Jeff Carpenter ([@jscarp](https://twitter.com/jscarp)) at the [South Bay Cassandra User Group](https://www.meetup.com/DataStax-Cassandra-South-Bay-Users)‘s Cassandra Day events. These are single day events, where we cover an introduction to Apache Cassandra, concepts of data-modeling for Apache Cassandra, and then a wrap up of application development with the respective drivers. Now if you aren’t in Santa Clara – or ya know Menlo Park, San Jose, Oakland, San Francisco, or well, the surrounding area – there are other days scheduled! We also have days scheduled that aren’t even located in the Bay, so check out the full list of events:

<https://www.datastax.com/company/events>

**NOTE:** If you’re interested in Seattle, Portland, or Vancouver BC area events, scroll all the way down to the end of this blog entry I’ve got more details for you!

**Introduction to Apache Cassandra**

In the introduction to Apache Cassandra we cover an overview of the architecture and features of the distributed database. Starting off with a definition of a distributed hash ring and how this is used in Apache Cassandra to provide data storage across the nodes that make up the Apache Cassandra Database. Moving on we’ll get into the other capabilities, trade offs of data replication between nodes, configuration settings, and a lot more.

**Data Modeling**

For data modeling we start off with a short review of relational database data modeling to provide something that is more familiar for many people. From this, we then build off of many concepts around denormalization, breaking apart various levels of normalization forms, and then get into the thinking and approach behind modeling an application in a distributed database and go deeper with details around Apache Cassandra.

**Application Development**

For application development, focusing around the Java language and technology stack, we’ll start with some concepts around how the drivers connect to and work with Apache Cassandra. We’ll open up some code too, get into some code changes and additions, to get more familiar with how the driver works and some of the capabilities of the driver itself.

Most of the code, concepts, and related material in use around Java and the tech stack are directly usable on C#, JavaScript, and even using the community open source Go CQL Library.

***Coming soon…***

In the coming weeks (ok, maybe a month or two) we’ll be updating this material for Apache Cassandra v4 and additionally, I’m aiming to line up some half day and probably some full day workshops in the Cascadian region: Portland, Seattle, and Vancouver BC. They’ll be almost identical except for a few tweaks, but you’ll have to RSVP to find out the details!

Also, if you’re in between any of those cities and have a stop on the Amtrak Cascades, let me know and we’ll get an RSVP list started for your city and see if we can get the required attendee count to make it official!
