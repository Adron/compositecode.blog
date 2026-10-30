---
title: Cassandra Datacenter & Racks
date: 2018-10-29 07:13:20 -0700
last_modified_at: 2019-01-24 20:06:18 -0800
permalink: /2018/10/29/cassandra-datacenter-racks/
slug: cassandra-datacenter-racks
wp_id: 14483
original_url: https://compositecode.blog/2018/10/29/cassandra-datacenter-racks/
categories:
- Databases
- datastax enterprise
- Distributed Things
tags:
- apache cassandra
- cassandra
- datacenter
- distributed computing
- distributed databases
- distributed systems
- node
- racks
- snitch
- vnode
excerpt: 'The last post in this series is Distributed Database Things to Know: Consistent Hashing. Let’s talk about the analogy of Apache Cassandra Datacenter & Racks to actual datacenter and racks. I kind of enjoy the use of the terms datacenter and racks to describe architectural elements of Cassandra. However, as time moves on the relationship between …'
image: /wp-content/uploads/2018/10/fixed1.png
format: aside
---

The last post in this series is [Distributed Database Things to Know: Consistent Hashing](/2018/10/08/distributed-database-things-to-know-consistent-hashing/).

Let’s talk about the analogy of *Apache Cassandra Datacenter & Racks* to actual datacenter and racks. I kind of enjoy the use of the terms datacenter and racks to describe architectural elements of Cassandra. However, as time moves on the relationship between these terms and why they’re called datacenter and racks can be obfuscated.

Take for instance, a datacenter could just be a cloud provider, an actual physical datacenter location, a zone in Azure, or region in some other provider. What an actual Datacenter in Cassandra parlance actually is can vary, but the origins of why it’s called a Datacenter remains the same. The elements of racks also can vary, but also remain the same.

## Origins: Racks & Datacenters?

Let’s cover the actual things in this industry we call *datacenter* and *racks* first, unrelated to Apache Cassandra terms.

**Racks**: The easiest way to describe a physical rack is to show pictures of datacenter racks via the ole’ Google images.

[![racks.png](/wp-content/uploads/2018/08/racks.png)](https://www.google.com/search?rlz=1C5CHFA_enUS793US793&biw=1280&bih=1090&tbm=isch&sa=1&ei=mjvWW9X-KsW10PEP76i52AI&q=data+center+racks&oq=data+center+racks&gs_l=img.3..0l2j0i7i30j0i5i30l2j0i8i30l2j0i24l3.4078.5164..5371...0.0..0.45.507.12......1....1..gws-wiz-img.......0i8i7i30j0i7i5i30.b-QP90OSuUs)

A rack is something that is located in a data-center, or even just someone’s garage in some odd scenarios. Ya know, if somebody wants serious hardware to work with. The rack then has a number of servers, often various kinds, within that rack itself. As you can see from the images above there’s a wide range of these racks.

**Datacenter**: Again the easiest way to describe a datacenter is to just look at a bunch of pictures of datacenter, albeit you see lots of racks again. But really, that’s what a datacenter is, is a building that has lots and lots of racks.

[![data-center.png](/wp-content/uploads/2018/08/data-center.png)](https://www.google.com/search?q=data+center&source=lnms&tbm=isch&sa=X&ved=0ahUKEwj0wYHomqreAhXNGTQIHdEDBXMQ_AUIDygC&biw=1280&bih=1090)

However in Apache Cassandra (and respectively DataStax Enterprise products) a datacenter and rack do not directly correlate to a physical rack or datacenter. The idea is more of an abstraction than hard mapping to the physical realm. In turn it is better to think of datacenter and racks as a way to structure and organize your DataStax Enterprise or Apache Cassandra architecture. From a tree perspective of organizing your cluster, think of things in this hierarchy.

- Cluster
  - Datacenter(s)
    - Rack(s)
      - Server(s)
        - Node (vnode)

## Apache Cassandra Datacenter

An Apache Cassandra Datacenter is a group of nodes, related and configured within a cluster for replication purposes. Setting up a specific set of related nodes into a datacenter helps to reduce latency, prevent transactions from impact by other workloads, and related effects. The replication factor can also be setup to write to multiple datacenter, providing additional flexibility in architectural design and organization. One specific element of datacenter to note is that they must contain only one node type:

- Transactional: A standard Cassandra node.
- [DataStax Enterprise Graph](https://docs.datastax.com/en/dse/6.0/dse-admin/datastax_enterprise/graph/graphTOC.html): The Graph database offering from Datastax.
- [DataStax Enterprise Analytics](https://docs.datastax.com/en/dse/6.0/dse-admin/datastax_enterprise/analytics/analyticsOverview.html): An integration with [Apache Spark](https://spark.apache.org/).
- [DataStax Enterprise Search](https://docs.datastax.com/en/dse/6.0/dse-admin/datastax_enterprise/search/searchTOC.html): Integration with [Apache Solr](http://lucene.apache.org/solr/).
- [DataStax Enterprise Search Analytics](https://docs.datastax.com/en/dse/6.0/dse-dev/datastax_enterprise/analytics/dseSearchAnalyticsOverview.html): Search queries within analytics jobs.

Depending on the replication factor, data can be written to multiple datacenters. Datacenters must never span physical locations.Each datacenter usually contains only one node type. The node types are:

- Transactional: Previously referred to as a Cassandra node.
- [DSE Graph](https://docs.datastax.com/en/dse/6.0/dse-admin/datastax_enterprise/graph/graphTOC.html): A graph database for managing, analyzing, and searching highly-connected data.
- [DSE Analytics](https://docs.datastax.com/en/dse/6.0/dse-admin/datastax_enterprise/analytics/analyticsOverview.html): Integration with Apache Spark.
- [DSE Search](https://docs.datastax.com/en/dse/6.0/dse-admin/datastax_enterprise/search/searchAbout.html): Integration with Apache Solr. Previously referred to as a Solr node.
- [DSE SearchAnalytics](https://docs.datastax.com/en/dse/6.0/dse-admin/datastax_enterprise/analytics/dseSearchAnalyticsOverview.html): DSE Search queries within DSE Analytics jobs.

## Apache Cassandra Racks

An Apache Cassandra Rack is a grouped set of servers. The architecture of Cassandra uses racks so that no replica is stored redundantly inside a singular rack, ensuring that replicas are spread around through different racks in case one rack goes down. Within a datacenter there could be multiple racks with multiple servers, as the hierarchy shown above would dictate.

To determine where data goes within a rack or sets of racks Apache Cassandra uses what is referred to as a snitch. A snitch determines which racks and datacenter a particular node belongs to, and by respect of that, determines where the replicas of data will end up. This replication strategy which is informed by the snitch can take the form of numerous kinds of snitches, some examples include;

- SimpleSnitch – this snitch treats order as proximity. This is primarily only used when in a single-datacenter deployment.
- Dynamic Snitching – the dynamic snitch monitors read latencies to avoid reading from hosts that have slowed down.
- RackInferringSnitch – Proximity is determined by rack and datacenter, assumed corresponding to 3rd and 2nd octet of each node’s IP address. This particular snitch is often used as an example for writing a custom snitch class since it isn’t particularly useful unless it happens to match one’s deployment conventions.

In the future I’ll outline a few more snitches, how some of them work with more specific detail, and I’ll get into a whole selection of other topics. Be sure to subscribe to the blog, the ole’ RSS feed works great too, and follow [@CompositeCode](https://twitter.com/CompositeCode) for blog updates. For discourse and hot takes follow me [@Adron](https://twitter.com/Adron).

> ## Distributed Database Things to Know Series
>
> 1. [Consistent Hashing](/2018/10/08/distributed-database-things-to-know-consistent-hashing/)
> 2. Apache Cassandra Datacenter & Racks (this post)
