---
title: My Top 2 Reading List for Go & Data
date: 2020-05-25 20:54:44 -0700
last_modified_at: 2020-05-25 20:54:44 -0700
permalink: /2020/05/25/my-top-2-reading-list-for-go-data/
slug: my-top-2-reading-list-for-go-data
wp_id: 16925
original_url: https://compositecode.blog/2020/05/25/my-top-2-reading-list-for-go-data/
categories:
- Databases
- golang
tags:
- black hat
- chris patten
- coding
- dan kottmann
- data
- database
- designing data-intensive applications
- go
- golang
- martin kleppmann
- programming
- software development
- tom steele
excerpt: Over the next few months while I read through these books I hope to provide summaries and related notes on the material. Who knows, maybe you’ll want to dive into the material yourself! Until then happy thrashing code and may you have high retention and comprehension in reading!
image: /wp-content/uploads/2020/05/data-numbers-ss-1920.jpg
---

Right now I’ve got a couple books in queue.

## “Black Hat Go” Go Programming for Hackers and Pentesters by Tom Steele, Chris Patten, and Dan Kottmann.

[![Alt Text](https://res.cloudinary.com/practicaldev/image/fetch/s--mmUZeszI--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https%3A//dev-to-uploads.s3.amazonaws.com/i/ufoo6kv3hj46r1nfp4eh.png)](https://res.cloudinary.com/practicaldev/image/fetch/s--mmUZeszI--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https%3A//dev-to-uploads.s3.amazonaws.com/i/ufoo6kv3hj46r1nfp4eh.png)

I picked this book up after a good look at the index. There is a basic intro to Go at the beginning of the book to cover language fundamentals, but immediately after that dives into the meat of the topic. Immediately getting into understanding the TCP handshake, TCP itself, writing a scanner, and a proxy. There is then some basics about HTTP Servers, routers, and middleware in chapter 3 and 4, but returns immediately into topics of interest in chapter 5 around exploiting DNS, and writing DNS clients. I perused the index a bit further to note it covers SMB and NTLM, a chapter on “Abusing Databases and Filesystems”, then on to raw packet processing, writing and porting exploit code, and a host of other topics. This is going to be an interesting book to dig into and write about in the coming weeks. I’m pretty excited about it and hope to write a thorough review upon completion.

## “Designing Data-Intensive Applications” by Martin Kleppmann

[![Alt Text](https://res.cloudinary.com/practicaldev/image/fetch/s--FUuoZJsl--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https%3A//dev-to-uploads.s3.amazonaws.com/i/frsew3n2420oo0zgdm5o.png)](https://res.cloudinary.com/practicaldev/image/fetch/s--FUuoZJsl--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https%3A//dev-to-uploads.s3.amazonaws.com/i/frsew3n2420oo0zgdm5o.png)

This book is familiar territory, as I’ve spent much of my career working on similar topics that this book covers. What I suspect is that I’ll enjoy reading the material presented in an orderly and concise way versus the chaos and disruptive way I’ve acquired the knowledge on these topics.

From the index, the book starts off with foundations of data systems and the ideas around building reliable, scalable, and maintainable applications. This provides a good basis in which to dive into the other topics. From there it looks like we’ll get a run into the birth of NoSQL, object-relational mismatches and the related insanity that this has bred in the industry! Then a solid dive into graph-like, traditional, and multi-model data modeling. With the beginning quarter of the book then covering everything from hash indexes, SSTables (another familiar topic), LSM-Trees, B-Trees, and related indexing structures before wrapping up this first 25% of the book with stars and snowflake topics for analytics and column-oriented storage, compression, sort orders in column storage, and related material on aggregation in data cubes and materialized views.

That’s just the first 25%! From there Martin covers a wide range of topics, that if you’re in the industry and plan to deal with large scale data-intensive applications these are topics you need to be intimately familiar with!

### Reading

Over the next few months while I read through these books I hope to provide summaries and related notes on the material. Who knows, maybe you’ll want to dive into the material yourself! Until then happy thrashing code and may you have high retention and comprehension in reading!
