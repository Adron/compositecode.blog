---
title: Riak 1.4 – A Few Notes, Notices & Thoughts…
date: 2013-07-10 17:15:30 -0700
last_modified_at: 2013-08-08 12:46:44 -0700
permalink: /2013/07/10/riak-1-4-a-few-notes-notices-thoughts/
slug: riak-1-4-a-few-notes-notices-thoughts
wp_id: 8540
original_url: https://compositecode.blog/2013/07/10/riak-1-4-a-few-notes-notices-thoughts/
categories:
- Basho
- Riak
tags:
- basho
- distributed database
- distributed databases
- riak
- riak 1.4
excerpt: The release notes for Riak 1.4 can be found via github… Two things have worked together that made me want to write up the new Riak 1.4 features. With Riak 1.4 hitting the streets and the work I’ve been doing with CorrugatedIron there are a few features that are going to add icing the cake. …
---

[![](/images/adronhall.smugmug.com/Software/Misc-Images/Just-Icons-and-Bits/i-cGB2Jb5/0/O/Riak_product_logo.png)](http://basho.com/riak/)The [release notes for Riak 1.4 can be found via github](https://github.com/basho/riak/blob/master/RELEASE-NOTES.md)…

Two things have worked together that made me want to write up the new Riak 1.4 features. With [Riak 1.4](http://docs.basho.com/riak/latest/) hitting the streets and the work I’ve been doing with CorrugatedIron there are a few features that are going to add icing the cake. If you want to dive more into the release, check out the [release notes](https://github.com/basho/riak/blob/1.4/RELEASE-NOTES.md). If you’re interested in the [.NET Client CorrugatedIron](http://corrugatediron.org/), [check it out here](http://corrugatediron.org/) or check out the [code on github](https://github.com/DistributedNonsense/CorrugatedIron/). Now on to the client APIs.

**riak-attach changed to not *nuke a node***

So when issuing the attach command like…

```bash
riak attach
```

…the command attaches to the named pipe to communicate with the running erlang nodes. Now when you hit *Ctrl-C* it kills just the pipe versus killing the pipe and riak node that you’re on. This is something that has bit me in the keister more than a few times. Bringing down a node or two while working on viewing what is going on with a node. This leads me to the next enhancement.

**riak-admin transfers**

If you’re using riak\_kv\_bitcask\_backend, riak\_kv\_eleveldb\_backend or riak\_kv\_memory\_backend the riak-admin transfers command now shows per-transfer progress and displays long node names better. Giving you a better idea of what and where things are going. The way this is reported depends slightly on the specific back end. For bitcask or in memory back end the progress is calculated by the keys already transferred out of the total keys, where as the level DB back end calculates based on bytes transferred. Based on this the level DB calculation can get slightly off over time.

**Protocol Buffers & Multiple Interface Binding**

Protocol Buffers can now bind to multiple ports and interfaces, so clients such as CorrugatedIron for .NET (<http://corrugatediron.org/>), Riakjs (<http://riakjs.com/>) can now bind to the Protocol Buffers outside of the set configuration. For more on Riak configuration around the binding, check out the Basho Docs (<http://docs.basho.com/riak/latest/references/Configuration-Files/>). This also brings feature parity around interface binding equal to that of the HTTP interfaces. This changes the pb\_port and pb\_ip to a single pb setting which is now a list of IP and port pairs.

**Total radness in paging, of 2i**

Secondary indexes now have results available via pagination. Check out this [PR for bunches more info](https://github.com/basho/riak_kv/pull/540).

**Client-specified Timeouts**

Milliseconds can now be assigned to a timeout value for clients. This can be used for object manipulation around fetch, store and delete, listing buckets or keys. This takes care of some time out issues that may have been occurring during certain types of requests. This will come in handy for asynchronous and pivotal if anyone goes the synchronous route.

**Bucket Properties for Protocol Buffers**

If you’re needing to reset a bucket to it’s defaults, this is now possible. Besides a reset to defaults all bucket properties are now usable for protocol buffer usage. This can definitely help client usage of protocol buffers in a dramatic way.

**List-buckets Streaming – Realtime**

Listing keys or buckets via a streaming request will send bucket names to the client as received. This prevents any need to wait for a request from all nodes to respond. This can help with response time and time outs from the client point of view. This gives the ability to use the streaming features with Node.js, C#, Java and other languages and frameworks that support realtime streaming data feeds.

[![](/images/adronhall.smugmug.com/Software/Misc-Images/Logo/i-5zk96td/0/O/AH---Logo-32x32.png)](http://adron.me)…these are the features that have jumped out at me, so until next release.
