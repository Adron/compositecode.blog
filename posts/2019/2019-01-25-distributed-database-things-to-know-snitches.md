---
title: 'Distributed Database Things to Know: Snitches'
date: 2019-01-25 06:05:50 -0800
last_modified_at: 2019-01-24 21:21:52 -0800
permalink: /2019/01/25/distributed-database-things-to-know-snitches/
slug: distributed-database-things-to-know-snitches
wp_id: 14162
original_url: https://compositecode.blog/2019/01/25/distributed-database-things-to-know-snitches/
categories:
- cassandra
- Databases
- datastax enterprise
- Distributed Things
tags: []
excerpt: Snitches. What a great name for a feature right? I’d bring up the Harry Potter thing, but I’m gonna let that one fly. (get it, it flies!) A snitch determines where nodes go among the racks and datacenters. This is the Cassandra specific racks and datacenters however, so check out my previous post on datacenters …
image: /wp-content/uploads/2018/10/fixed1.png
format: aside
---

Snitches. What a great name for a feature right? I’d bring up the Harry Potter thing, but I’m gonna let that one fly. (get it, it flies!)

A snitch determines where nodes go among the racks and datacenters. This is the Cassandra specific racks and datacenters however, so check out my previous post on [datacenters and racks](/2018/10/29/cassandra-datacenter-racks/) for more detail on the specifics about what they are in relation to Cassandra and DataStax Enterprise (DSE). Snitches tell the database about the network topology of the system. Requests can then be routed efficiently and enables Cassandra and DSE to distribute replicas by grouping the machines accordingly. Of the nodes, all within a cluster must use this same snitch in the logic of distribution among the system.

**Snitch Options**

The following are the feature options we have to determine how the snitches determine node placement.

- DseSimpleSnitch – This is the default snitch and is intended only for development deployments. It doesn’t recognize datacenter or rack information, and simply needs a a keyspace defined to use SimpleStrategy and set a replication factor. It’s use makes it a bit easier to setup a cluster for development.
- GossipingPropertyFileSnitch – This snitch is usable for production. Rack and datacenter information for the local node is defined in the cassandra-rackdc.properties file, which then propagates this to other nodes via gossip.
- Ec2Snitch – This is a great snitch for simple cluster deployments that reside in a single region. For this snitch, the region name is used as the datacenter name and availability zones are setup as racks. That gives us a setup that matches datacenter and racks to region and zones, making it pretty easy to remember which is where then. Since this maps this way, as the way Ec2 works, this snitch isn’t usable among multi-region clusters.
- Ec2MultiRegionSnitch – This snitch can be used for multi-region deployments. To use this snitch settings need to be made in both the cassandra.yaml file and cassandra-rackdc.properties file. The way this snitch works is by using the public IP designated in the broadcast\_address to allow this multi-region connection.
- GoogleCloudSnitch – This snitch, as is somewhat obvious by the name, is for DSE deployments on [Google Cloud Platform](https://cloud.google.com/) (GCP). This snitch uses datacenters and racks similarly mapped as the Ec2Snitch with datacenters mapped to regions and racks mapped to zones.
- CloudstackSnitch – This snitch is for Apache Cloudstack. Zone naming is free-form in Cloudstack so this snitch uses <country> <location> <az> notation.
- PropertyFileSnitch – The way this snitch works is by proximity, determined by rack and datacenter. It uses network details configured in cassandra-topology.properties file, with the datacenter names defined using standard convention. These need to correlated to the name of the actual datacenters in the keyspace definition. Then nodes in the cluster are described in the cassandra-topology.properties file and must be exactly the same on every node in the cluster.
- RackInferringSnitch – This snitch is kind of funny, because it’s a usable snitch, but it’s also an example snitch. It determines the proximity of nodes by datacenter and rack too. However it assumes these to correspond to the second and third octet of the node’s IP address. It is best used as an example for writing custom snitch classes, unless of course this matches your actual deployment conventions.

That’s the basics on snitches. I recently wrote about another important distributed database architectural concept called [consistent hashing](/2018/10/08/distributed-database-things-to-know-consistent-hashing/), it’s an important concept to understand about distributed databases like Cassandra and DataStax Enterprise.

**References:**

- [DataStax Documentation](https://docs.datastax.com/en/landing_page/doc/landing_page/current.html) on [Snitches](https://docs.datastax.com/en/dse/6.7/dse-arch/datastax_enterprise/dbArch/archSnitchesTOC.html)
- [Apache Cassandra Documentation](http://cassandra.apache.org/doc/4.0/operating/snitch.html)
