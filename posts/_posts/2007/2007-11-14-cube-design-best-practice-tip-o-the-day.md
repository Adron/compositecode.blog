---
title: 'Cube Design Best Practice :: Tip o'' The Day'
date: 2007-11-14 04:00:00 -0800
last_modified_at: 2007-11-14 04:00:00 -0800
permalink: /2007/11/14/cube-design-best-practice-tip-o-the-day/
slug: cube-design-best-practice-tip-o-the-day
wp_id: 396
original_url: https://compositecode.blog/2007/11/14/cube-design-best-practice-tip-o-the-day/
categories:
- Uncategorized Bits
tags: []
excerpt: Do not put too many parent-child dimensions in a cube. This tip is magnified when the dimension contains custom rollups or unary operators. Yes, some of you might say, “but they are so powerful!” Well with power comes responsibility! In this case the responsibility is to safe guard against poorly performing queries. So keep in …
---

Do not put too many parent-child dimensions in a cube.

This tip is magnified when the dimension contains custom rollups or unary operators.  Yes, some of you might say, “but they are so powerful!”  Well with power comes responsibility!  In this case the responsibility is to safe guard against poorly performing queries.  So keep in mind that these parent child dimensions should only be used when absolutely necessary.
