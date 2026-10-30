---
title: Common Sense Cardinality
date: 2008-01-23 05:04:29 -0800
last_modified_at: 2008-01-23 05:04:29 -0800
permalink: /2008/01/23/common-sense-cardinality/
slug: common-sense-cardinality
wp_id: 347
original_url: https://compositecode.blog/2008/01/23/common-sense-cardinality/
categories:
- Uncategorized Bits
tags: []
excerpt: I’ve been hearing a lot of discussion about cardinality this and cardinality that. With the topic becoming such a common point of discussion. I decided I would write up something. First some definitions so that we all have a clear cut idea of what cardinality actually is. Sometimes cardinality isn’t fully understood at a basic …
---

I’ve been hearing a lot of discussion about cardinality this and cardinality that. With the topic becoming such a common point of discussion. I decided I would write up something.

First some definitions so that we all have a clear cut idea of what cardinality actually is.  Sometimes cardinality isn’t fully understood at a basic level.  With some of the points I’m going to touch on a full understanding of the basis of cardinality will be needed.

**Cardinality** : 1. Cardinality is part of formal set theory.  A cardinal number is a type of number defined in such a way that any method of counting sets using it gives the same result.  2. Cardinality is a notion of the size of a set which does not rely on numbers.  It is a relative notion.  For instance, two sets may each have an infinite number of elements, but one may have a greater cardinality.

The second definition is the one that I will discuss further.  I must note, that it is odd that even before anyone is confused, the definitions are in opposition with each other.  Cardinality does or does not include numbers, both specifically defined by use.  For a little more information, check my previous entry [Tip o’ The Day](http://adronbhall.com/blogs/technology__software_development/archive/2007/12/07/6013.aspx).

Now on to some meat of this topic.  When designing cubes and planning the various dimensions of data, cardinality is a key concept that must be taken into account when doing so.  *High cardinality high count items make bad dimensions, high cardinality low count and low cardinality low count items make great dimensions.* Now before digressing and grumbling about how this might be a stupid statement, hear me out further.

**High Count, High Cardinality Data Sets**

If you have a large count data set that has no limits, and a high cardinality this is either a questionable data set to turn into a dimension.  These types of data sets; e-mail addresses, user names, or other high cardinality items are not good data sets to use as dimensions.  Sometimes there may be exceptions, but rarely would that be the case.  Generally when there is high cardinality, counts, or other measures and facts are the candidates for these data sets.

**High Count, Low Cardinality Data Sets**

These data sets usually make a decent dimension because of the ability to pare them down to a set numbers of unique values.  Keep in mind, that whatever a dimension is slicing into, should be visibly readable.  An example would be business departments, or business zones.  Each business department might have thousands or even millions of data points, but when a distinct value is derived from the set of data the cardinality is low enough that one ends up with a low number of actual unique items, making slicing much easier for the people viewing the actual reports.

**Mix and Match of High Count and Cardinality Degrees**

In both cases above, high count, low or high cardinality, often data sets can be stuck into either category.  Take the birthday of a user database for example.  There are 365 possible birthdays per year, not a good way to slice data.  But if you break it down to just the month or year, you end up with 12 months or x number of years.  This is a perfect example of something to use for a dimension.

On the same note one might have user data, but then have the user data of a particular department noted.  If the user count and user information could be derived and rolled up via the department the break out of user departments into a dimension makes sense.

There are dozens of other ways to look at data.  One of the interesting ideas I heard recently of a high count, high cardinality data set was e-mails.  The e-mails for a particular set where being tracked.  A user wanted to know where the domain of the e-mails where originating from, which individually wasn’t something you’d want a Cube Processing to have to go through.  So instead of trying to derive the origination of each e-mail we had in the data set, we pared the data down to purely just the domain, removing the actual user name part of the e-mail.  From there we where able to pare down the e-mail domain originations into a clear and discernable dimension.

So when it comes to cardinality there can always be more than meets the eye.  Take a second look at high count data sets to make sure they’re really high count, sometimes they can be pared down to reasonable amounts of data.
