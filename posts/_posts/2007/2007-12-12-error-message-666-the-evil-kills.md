---
title: Error Message 666, The Evil Kills
date: 2007-12-12 18:13:29 -0800
last_modified_at: 2007-12-12 18:13:29 -0800
permalink: /2007/12/12/error-message-666-the-evil-kills/
slug: error-message-666-the-evil-kills
wp_id: 369
original_url: https://compositecode.blog/2007/12/12/error-message-666-the-evil-kills/
categories:
- Uncategorized Bits
tags: []
excerpt: “666 16 Maximum system-generated unique value for a duplicate group exceeded for table ID %d, index ID %d. Dropping and re-creating the index may fix the problem; otherwise use another clustering key.” So today when running a query I’ve come across the message listed. Off I went digging the Internet to figure out what exactly …
---

*“**666**    16    Maximum system-generated unique value for a duplicate group exceeded for table ID %d, index ID %d. Dropping and re-creating the index may fix the problem; otherwise use another clustering key.”*

So today when running a query I’ve come across the message listed.  Off I went digging the Internet to figure out what exactly this meant.  I guess the fact I was running a query with distinct counts against 2 Terabytes of data has something to do with it. ![Surprise [:O]](/emoticons/emotion-3.gif)

All in all, it is definitely an *“evil”* error message.

Off to fix the query & index.
