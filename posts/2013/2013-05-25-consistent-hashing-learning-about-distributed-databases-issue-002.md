---
title: 'Consistent Hashing – Learning About Distributed Databases :: Issue 002'
date: 2013-05-25 14:54:40 -0700
last_modified_at: 2013-05-25 14:54:40 -0700
permalink: /2013/05/25/consistent-hashing-learning-about-distributed-databases-issue-002/
slug: consistent-hashing-learning-about-distributed-databases-issue-002
wp_id: 8290
original_url: https://compositecode.blog/2013/05/25/consistent-hashing-learning-about-distributed-databases-issue-002/
categories:
- Architecture
- Databases
- Distributed Things
- Riak
tags:
- consistent hashing
- distributed
- distributed databases
- distributed systems
- minimum cut
- riak
excerpt: One of the core tools in the belt of the distributed database is consistent hashing. In Riak this is especially true, as it stands at the core of a Riak Cluster. Hashing, using a hash function, is an algorithm that maps data to variable length to data that’s fixed. In other words, odd things like …
---

One of the core tools in the belt of the distributed database is consistent hashing. In Riak this is especially true, as it stands at the core of a Riak Cluster. Hashing, using a hash function, is an algorithm that maps data to variable length to data that’s fixed. In other words, odd things like the name of things mapped to integers. Consistent hashing is a special kind of hashing that provides the pattern for mapping keys and all related functionality around a cluster ring in Riak.

[![](/images/adronhall.smugmug.com/Software/Misc-Images/Bad-Resume/i-LjQjZDs/0/O/Min_cut_example.png)](http://en.wikipedia.org/wiki/Cut_(graph_theory))Consistent hashing was originally devised by David Karger, a professor of computer science at [MIT](http://www.mit.edu/) ([Massachusetts Institute of Technology](http://www.mit.edu/)). He’s also known for Karger’s Algorithm, a Monte Carlo method that computes the minimum cut in a connected graph ([graph theory related stuff](http://en.wikipedia.org/wiki/Graph_theory)). Along with these developments he’s been part of many other efforts and contributed to computer science in many ways.

**Remapping, Mapping and Keeping Distributed (& Available)**

One key property of a consistent hash is that it minimizes the number of keys that must be remapped. With a regular hash changes, the entire key hash must be remapped.

![](/images/adronhall.smugmug.com/Software/Databases/Consistent-Hashing/i-zvTxdN5/0/S/riak-ring-S.png)Consistent hashing is based around mapping each object to a point of a circle. The system maps each storage bucket to pseudo-randomly distributed points on the edge of this circle.

The system finds where to place the object based on the key on the edge of the circle. It then walks the circle falling into the first bucket it finds. This results in the buckets containing the resources between its point and the next bucket point.

![](/images/adronhall.smugmug.com/Software/Databases/Consistent-Hashing/i-t7MvMNJ/0/S/riak-data-distribution-S.png)

When a bucket disappears for any reason, the pseudo randomly mapped objects will now get re-mapped to different buckets. When a bucket appears, such as becoming available again or being added, a similar process occurs.

The Basho Docs describe in brief that,

> “[Consistent hashing is a technique used to limit the reshuffling of keys when a hash-table data structure is rebalanced (when slots are added or removed). Riak uses consistent hashing to organize its data storage and replication. Specifically, the vnodes in the Riak Ring responsible for storing each object are determined using the consistent hashing technique.](http://docs.basho.com/riak/latest/tutorials/fast-track/What-is-Riak/)“

**NOTES:** This is not a single blog entry topic by any means. This is merely a cursory look at consistent hashing. This entry I aimed to provide a basic description and coverage of the actions around consistent hashing. For more information and to dive even deeper into consistent hashing I’ve included a few links that have extensive information on the topic:

- [Consistent Hashing – Basho Docs](http://docs.basho.com/riak/latest/references/appendices/concepts/Riak-Glossary/#Consistent-Hashing)
- [Wikipedia Article](http://en.wikipedia.org/wiki/Consistent_hashing)
- For comparable hashing, check out [Distributed Hash Tables (DHTs)](http://en.wikipedia.org/wiki/Distributed_hash_table).
- For a more [thorough description and topic coverage check out the Riak doc](http://docs.basho.com/riak/latest/tutorials/fast-track/What-is-Riak/)s.
