---
title: 'Numeric Keys RULE! :: Tip O'' The Day'
date: 2007-11-09 05:43:00 -0800
last_modified_at: 2007-11-09 05:43:00 -0800
permalink: /2007/11/09/numeric-keys-rule-tip-o-the-day/
slug: numeric-keys-rule-tip-o-the-day
wp_id: 399
original_url: https://compositecode.blog/2007/11/09/numeric-keys-rule-tip-o-the-day/
categories:
- Uncategorized Bits
tags: []
excerpt: When you’re developing attributes that have a bunch of members, let’s say more than a million (1,000,000,000), you should definitely use numeric keys. Don’t use strings or anything like that or you will suffer delays. With business intelligence cube development we’re talking about airport length delays here! So next time you’re tearing through some ETL …
---

When you’re developing attributes that have a bunch of members, let’s say more than a million (1,000,000,000), you should definitely use numeric keys.  Don’t use strings or anything like that or you will suffer delays.  With business intelligence cube development we’re talking about airport length delays here!

So next time you’re tearing through some ETL or data manipulation processes or just building attributes with what you have, make sure to toss those numeric keys in there to assure the speed that a good Cube should have!
