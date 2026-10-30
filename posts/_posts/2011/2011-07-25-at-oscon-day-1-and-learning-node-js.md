---
title: 'At OSCON Day #1 and “Learning Node.js”'
date: 2011-07-25 17:15:14 -0700
last_modified_at: 2011-07-25 15:54:27 -0700
permalink: /2011/07/25/at-oscon-day-1-and-learning-node-js/
slug: at-oscon-day-1-and-learning-node-js
wp_id: 3366
original_url: https://compositecode.blog/2011/07/25/at-oscon-day-1-and-learning-node-js/
categories:
- Architecture
- Conferences
- Infrastructure
- Javascript
tags:
- node
- node.js
- oscon
- oss
excerpt: 'Playful Exploration of Public & Personal Data I arrived, just after the keynote, because I was being lame on this Monday. Sounds like it was a great keynote with some great people speaking. The first thing I did was get my directions straight for where all the rooms and expo area is. Once I did that I headed to Playful Explorations of Public and Personal Data that Andrew Turner was giving. His presentation showed some great information and data for or from GeoIQ, Geocommons, and others. The areas in which data can be used to overlay crime, friendly or unfriendly areas based on that, where there are dogs, coffee shops, and what can be derived. I did notice though that a lot of the data is at a very high level. Leaders can make decisions on this kind of data, but it is dangerous making decision based on one or two of these data points. Leaders need to truly understand events and triggers at a macro level also. At the end of the session Andrew actually hit on the note that users of this data must be careful in what they correlate. Architectural Anti-patterns for Handling Data I’ll let the tweets I tweeted tell the tweet of the presentation. 🙂 #oscon #oscond RDBMS antipattern – Email data stored in databases. <- Can get VERY nasty. Couch? Mongo? NoSQL anybody? BigTable? 😐 #oscon #oscond RDBMS antipattern: "Stoned Procedures" i.e. Stored Procedures, Triggers, etc… Bad! Lock in and horrible maintainability. Oooh! #oscon #oscond Another antipattern, are you ready for this one? ORMs. Impedance mis-match w/ RDBMS. The cure as bad as the disease! :/ #oscon #oscond Another antipattern. Tables as a log file. 😮 Hmmm. Yup, I''ve done that. 🙁 Probably wasn''t the greatest idea…but meh. 😀 #oscon #oscond antipattern The Alignment creating columns "a1, a2, a3, a4…?!?!?!?!" WTF!? If you do this – STOP NOW! k thx. (originally posted on yfrog) Click for larger image antipatterns w/ RDBMSs… #oscon #oscond #oscon #oscond antipattern RDBMS "Dynamic Table Creation"… yeah, not a good idea. 🙁 makes sad pandas. Anti-pattern for RDBMS: "Not everything fits on/in a RDBMS…"#oscon #oscond OH: "What is the main mySQL tuning technique used in panic situations?" A: "Install PostgreSQL" :O Doh! #oscon #oscond @LusciousPear En route now… 🙂 to @gleicon session. LusciousPear by adronbh If you''re at #oscon / #oscond head NOW to C123 to see @gleicon''s talk on "Architectural Anti-Patterns for Data Handling". There''s lulz + win As described on the OSCON Site, Learning Node.js Presented by Tom Hughes-Croucher (Joyent). Learn how to build scalable Internet applications with Node.js, the event-driven server-side JavaScript framework. You''ll see how Node.js solves many scaling and speed problems that weigh down other web application frameworks. This is the first session I lined up for myself. I''ve been on a Node.js kick lately and have still found myself not having much time to work with the technology. However, having a clearcut session dedicated to the topic, and tomorrow is Node.js day, I''m pretty stoked to really get to using the technology hard core! Tom did a good job with this session, with a bit of lively retort thrown in here and there. The session covered installation, the basic apps that are displayed on the Node.js Site, and then into additional exercises that got us all running the bits like pros (ok, like total newbs I''m sure). The session was a decent pace, it gave me time to work through the exercises and also wrap up coverage of the 1st day of the conference. However, I''m still going to have to sit down and go through the exercises again and actually determine what Node is actually doing. There are some interesting going ons behind the scenes that I know I''ve missed, but sure will pick them up ASAP with a quick review. 🙂 Day Number One Summary This is my first full size OSS Conference I''ve attended. I did attend OS Bridge, which was similar, but this one has a large price tag to it. So expectations are different. Overall I''ve been very happy so far. The Swag is awesome, the sessions have been good, and the Node.js Intro was very informative and taught me a few things I didn''t know. The one thing I regrest, is that I can''t attend more of the sessions. This however tends to be the problem with any conference that is worth the time! I''m looking forward to day two, for now, I''m off to socialize and try to do a few non-computer related things.'
---

**![](/images/adronhall.smugmug.com/Software/Meetups-N-Conferences/OSCON/i-RV2gbj3/0/O/oscon2011attending210x60-1.gif)[Playful Exploration of Public & Personal Data](http://www.oscon.com/oscon2011/public/schedule/detail/19750)**

I arrived, just after the keynote, because I was being lame on this Monday. Sounds like it was a great keynote with some great people speaking.

The first thing I did was get my directions straight for where all the rooms and expo area is. Once I did that I headed to Playful Explorations of Public and Personal Data that Andrew Turner was giving. His presentation showed some great information and data for or from GeoIQ, Geocommons, and others. The areas in which data can be used to overlay crime, friendly or unfriendly areas based on that, where there are dogs, coffee shops, and what can be derived.

I did notice though that a lot of the data is at a very high level. Leaders can make decisions on this kind of data, but it is dangerous making decision based on one or two of these data points. Leaders need to truly understand events and triggers at a macro level also. At the end of the session Andrew actually hit on the note that users of this data must be careful in what they correlate.

**[Architectural Anti-patterns for Handling Data](http://www.oscon.com/oscon2011/public/schedule/detail/19094)**

I’ll let the tweets I tweeted tell the tweet of the presentation.  🙂

![Adron Hall](https://a0.twimg.com/profile_images/791825851/adron1_normal.jpg)[#oscon](http://twitter.com/#!/search?q=%23oscon "#oscon") [#oscond](http://twitter.com/#!/search?q=%23oscond "#oscond") RDBMS antipattern – Email data stored in databases. <- Can get VERY nasty. Couch? Mongo? NoSQL anybody? BigTable? 😐

![Adron Hall](https://a0.twimg.com/profile_images/791825851/adron1_normal.jpg)[#oscon](http://twitter.com/#!/search?q=%23oscon "#oscon") [#oscond](http://twitter.com/#!/search?q=%23oscond "#oscond") RDBMS antipattern: “Stoned Procedures” i.e. Stored Procedures, Triggers, etc… Bad! Lock in and horrible maintainability.

![Adron Hall](https://a0.twimg.com/profile_images/791825851/adron1_normal.jpg)Oooh! [#oscon](http://twitter.com/#!/search?q=%23oscon "#oscon") [#oscond](http://twitter.com/#!/search?q=%23oscond "#oscond") Another antipattern, are you ready for this one? ORMs. Impedance mis-match w/ RDBMS. The cure as bad as the disease! :/

![Adron Hall](https://a0.twimg.com/profile_images/791825851/adron1_normal.jpg)[#oscon](http://twitter.com/#!/search?q=%23oscon "#oscon") [#oscond](http://twitter.com/#!/search?q=%23oscond "#oscond") Another antipattern. Tables as a log file. 😮 Hmmm. Yup, I’ve done that. 🙁 Probably wasn’t the greatest idea…but meh. 😀

![Adron Hall](https://a0.twimg.com/profile_images/791825851/adron1_normal.jpg)[#oscon](http://twitter.com/#!/search?q=%23oscon "#oscon") [#oscond](http://twitter.com/#!/search?q=%23oscond "#oscond") antipattern The Alignment creating columns “a1, a2, a3, a4…?!?!?!?!” WTF!? If you do this – STOP NOW! k thx.

![Adron Hall](https://a0.twimg.com/profile_images/791825851/adron1_normal.jpg) (originally posted on yfrog)
[![Click for larger image](/images/adronhall.smugmug.com/Software/Meetups-N-Conferences/OSCON/i-JDGRSxK/0/S/TheEternalTree-S.jpg "Click for larger image")](http://adronhall.smugmug.com/Software/Meetups-N-Conferences/OSCON/18218918_n258dk#1400605906_JDGRSxK-O-LB)

*Click for larger image*

antipatterns w/ RDBMSs… [#oscon](http://twitter.com/#!/search?q=%23oscon "#oscon") [#oscond](http://twitter.com/#!/search?q=%23oscond "#oscond")

![Adron Hall](https://a0.twimg.com/profile_images/791825851/adron1_normal.jpg)[#oscon](http://twitter.com/#!/search?q=%23oscon "#oscon") [#oscond](http://twitter.com/#!/search?q=%23oscond "#oscond") antipattern RDBMS “Dynamic Table Creation”… yeah, not a good idea. 🙁 makes sad pandas.

![Adron Hall](https://a0.twimg.com/profile_images/791825851/adron1_normal.jpg)Anti-pattern for RDBMS: “Not everything fits on/in a RDBMS…”[#oscon](http://twitter.com/#!/search?q=%23oscon "#oscon") [#oscond](http://twitter.com/#!/search?q=%23oscond "#oscond")

![Adron Hall](https://a0.twimg.com/profile_images/791825851/adron1_normal.jpg)OH: “What is the main mySQL tuning technique used in panic situations?” A: “Install PostgreSQL” :O Doh! [#oscon](http://twitter.com/#!/search?q=%23oscon "#oscon") [#oscond](http://twitter.com/#!/search?q=%23oscond "#oscond")

![Adron Hall](https://a0.twimg.com/profile_images/791825851/adron1_normal.jpg)[@LusciousPear](http://twitter.com/LusciousPear) En route now… 🙂 to [@gleicon](http://twitter.com/gleicon) session.

![Bradford S.](https://a1.twimg.com/profile_images/1355408481/shot_1305010022599_normal.jpg)[LusciousPear](http://twitter.com/#!/LusciousPear "Bradford S.")

*by adronbh*If you’re at [#oscon](http://twitter.com/#!/search?q=%23oscon "#oscon") / [#oscond](http://twitter.com/#!/search?q=%23oscond "#oscond") head NOW to C123 to see [@gleicon](http://twitter.com/gleicon)‘s talk on “Architectural Anti-Patterns for Data Handling”. There’s lulz + win

**![](/images/adronhall.smugmug.com/Software/Misc-Images/Just-Icons-and-Bits/i-RZcgP4k/0/S/nodejs-S.png)**

As described on the OSCON Site, [Learning Node.js](http://www.oscon.com/oscon2011/public/schedule/detail/20168)

> Presented by Tom Hughes-Croucher (Joyent). Learn how to build scalable Internet applications with Node.js, the event-driven server-side JavaScript framework. You’ll see how Node.js solves many scaling and speed problems that weigh down other web application frameworks.

This is the first session I lined up for myself. I’ve been on a Node.js kick lately and have still found myself not having much time to work with the technology. However, having a clearcut session dedicated to the topic, and tomorrow is Node.js day, I’m pretty stoked to really get to using the technology hard core!

Tom did a good job with this session, with a bit of lively retort thrown in here and there. The session covered installation, the basic apps that are displayed on the [Node.js Site](http://nodejs.org/), and then into additional exercises that got us all running the bits like pros (ok, like total newbs I’m sure). The session was a decent pace, it gave me time to work through the exercises and also wrap up coverage of the 1st day of the conference. However, I’m still going to have to sit down and go through the exercises again and actually determine what Node is actually doing. There are some interesting going ons behind the scenes that I know I’ve missed, but sure will pick them up ASAP with a quick review.  🙂

**Day Number One Summary**

This is my first full size OSS Conference I’ve attended. I did attend OS Bridge, which was similar, but this one has a large price tag to it. So expectations are different. Overall I’ve been very happy so far. The Swag is awesome, the sessions have been good, and the Node.js Intro was very informative and taught me a few things I didn’t know. The one thing I regrest, is that I can’t attend more of the sessions. This however tends to be the problem with any conference that is worth the time! I’m looking forward to day two, for now, I’m off to socialize and try to do a few non-computer related things.

***Keeping Up With the Conference***

To keep up with today’s events, and ongoing events during the Conference follow/search the Twitter feed with the [#oscon](http://twitter.com/#!/search/%23oscon) for the main conference, [#osconj](http://twitter.com/#!/search/%23osconj) for the Java Track, and [#oscond](http://twitter.com/#!/search/%23oscond) for the Big Data Track!

Watch the [live streaming feed](http://www.livestream.com/oreillyconfs?imm_mid=072059&cmp=em-orm-pr-conf-oscon-livestream).
