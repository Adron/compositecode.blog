---
title: Where Is The Other Data Tracking?! Where Are My Acronyms?!
date: 2010-01-13 00:45:00 +0000
last_modified_at: 2010-01-13 00:45:00 +0000
permalink: /2010/01/13/where-is-the-other-data-tracking-where-are-my-acronyms/
slug: where-is-the-other-data-tracking-where-are-my-acronyms
wp_id: 682
original_url: https://compositecode.blog/2010/01/13/where-is-the-other-data-tracking-where-are-my-acronyms/
categories:
- Uncategorized Bits
tags: []
excerpt: Where is the business intelligence? This blog entry may instigate just a bit. It will also be a little long for a blog entry. You've been warned. I suppose though, if you know me & the work I do, that is not really something new. I see something wrong, broken, or otherwise and I am …
---

## **Where is the business intelligence?**

This blog entry may instigate just a bit.  It will also be a little long for a blog entry. You've been warned.  I suppose though, if you know me & the work I do, that is not really something new.  I see something wrong, broken, or otherwise and I am likely to point it out and describe it in detail.

As I roll into 2010 coding, implementing, and rocking with [Webtrends](http://www.webtrends.com/), I have noticed something lacking in the analytics industry.  I will add the clause that obviously [Webtrends](http://www.webtrends.com/) has people thinking about these things and actively working on this topic, but what I want to point out is a general issue.  Where is the other data, where is the existing data?

It seems, even though some company's kind of get to a certain point in connecting data points, not many really do.  The biggest reason is that most companies are just a few steps away from actually being able to do so.  The other even larger reason is, many do not realize what data should or should not be connected.

When someone starts pulling CRM (Customer Relationship Manager/Management), Analytics, POS (Point of Sale), ERP (Enterprise Resource Planning) data, and other sources into a single reporting repository we finally have real business intelligence.  Otherwise so many entities stumble through the land mines of data confusion.  I see this so much it really drives me crazy sometimes.

So how can a company or entity identify and connect these points of data?  It often starts with a ridiculously simple step.  At risk of oversimplifying things, let me just state the first step in getting out of the data confusion land mines is to first figure out your data.  *Ask these things*:

> - What data does the business have?
> - What data is currently used and available?

Do NOT ask what data you want, do NOT ask what may not be.  What you want to know first, and so many companies make this mistake, is to know what you know.  Do not, at the early stage of business intelligence information gathering start asking too many hypotheticals.  I promise the risk of failure increases exponentially for every hypothetical data point added.

Once you have identified what data is available, start figuring out how the data is related.  Once you understand the data you can then, and only then, make the huge leap to determining what data you want and how to get it to where you want.

Let me draw this out in a real world example.  Beware; I am using my creative mind now!

What we have so far, for *Awe Widgets Incorporated*, is several data points.

> - Point of Sale/POS Systems in 300+ stores.
> - Web Analytics (by [Webtrends](http://www.webtrends.com/) of course) tracking all sorts of great data points on the Awe Widgets Incorporated Website.
> - Internal Accounting Software (Almost ERP, not really)
> - In-house Built Customer Lists for Sales.

So there we go, four key pieces of tracking.  So how would they work together?  With a little further analysis (my key creative side now analyzes Awe Widgets Incorporated internal structure) and we find a few connections.

**Correlation, POS to** [**Webtrends**](http://www.webtrends.com/) **Analytics**

The POS System has a tracking identifier for customers which we can use to sync up with logged in users tracked via [Webtrends](http://www.webtrends.com/) Analytics.  This data can be used to derive who is and is not in stores purchasing.  In addition trending could follow the user flow to derive some actionable decisions on how to encourage online or store front shopping.  Just these two data points being connected add a lot of value.

**Correlation, Internal Account Software ties to POS**

Another data point tie in with the aforementioned POS & [Webtrends](http://www.webtrends.com/) data is the Internal Accounting Software (IAS).  The IAS holds information related to each sale, and other correlated information about how sales are going for the quarter, year, and other performance indicators.

**Correlation, In-house Customer Lists for Sales**

The sales department, in aggressive technical fashion has built a number of customer lists in Excel & Access.  The Access Application has a partially updated data store with a server based Excel file holding the updated piece of data about each of the sales person's current sales.  I know, I hear it now, every developer that is familiar with this scenario screaming, "OMG, you have your data in Excel AND Access, and it is supposed to have integrity, and be aaaaaaaaaaaaaaaaggggggggggggggggghhhhhhhhhhh noooooo!"  But you know, this @#$% happens.  : )  When things are like this, solutions get creative.

**Tying Together the Pieces**

Alright, this is when the awesome nerd bits start to happen.  But I have covered enough for this entry.  In the following entries on this topic I will step through this first data finding mission and start discussions on how to connect these sources and get that data mart, warehouse, or other middle tier piece into action.   I will continue on and lead into how the data can finally start telling a real story.  Because in the end, the real story is, somebody needs actionable data to act upon.  Does it really matter where it is?

Check out [Part II of this series](/blogs/technology__software_development/post/2010/01/24/Brainstorming-Into-the-Business-Intelligence-Clouds.aspx).
