---
title: 'Cassandra / DataStax Enterprise 6 Clusters: Marketplace Options'
date: 2018-06-21 16:20:05 -0700
last_modified_at: 2018-07-08 17:52:07 -0700
permalink: /2018/06/21/quick-marketplace-clusters-for-cassandra-datastax-enterprise-6/
slug: quick-marketplace-clusters-for-cassandra-datastax-enterprise-6
wp_id: 14159
original_url: https://compositecode.blog/2018/06/21/quick-marketplace-clusters-for-cassandra-datastax-enterprise-6/
categories:
- Distributed Things
- How-to
tags:
- cloud
- distributed systems
- How-to
excerpt: As I have stepped full speed into work and research at DataStax there were a few things I needed as soon as I could possibly get them put together. Before even diving into development, use case examples, or reference application development I needed to have some clusters built up. The Docker image is great for …
image: /wp-content/uploads/2018/06/banner-bird.png
---

As I have stepped full speed into work and research at DataStax there were a few things I needed as soon as I could possibly get them put together. Before even diving into development, use case examples, or reference application development I needed to have some clusters built up. The Docker image is great for some simple local development, but beyond that I wanted to have some live 3+ node clusters to work with. The specific deployed and configured use cases I had included:

1. I wanted to have a **[DataStax Enterprise 6](https://www.datastax.com/products/datastax-enterprise-6) Cassandra Cluster** up and running ASAP. A cluster that would be long lived that I could developer sample applications against, use for testing purposes, and generally develop against from a Cassandra and DSE purpose.
2. I wanted to have an easy to use cluster setup for Cassandra – just the OSS deployment – possibly coded and configured for deployment with Terraform and related scripts necessary to get a 3 node cluster up and running in Google Cloud Platform, Azure, or AWS.
3. I wanted a DataStax Enterprise 6 enabled deployment, that would showcase some of the excellent tooling DataStax has built around the database itself.

I immediately set out to build solutions for these three requirements.

The first cluster system I decided to aim for was figuring out a way to get some reasonably priced hardware to actually build a physical cluster. Something that would make it absurdly easy to just have something to work with anytime I want without incurring additional expenses. Kind of the ultimate local development environment. With that I began scouring the interwebs and checking out where or how I could get some boxes to build this cluster with. I also reached out to a few people to see if I could be *gifted* some boxes from Dell or another manufacturer.

I lucked out and found some cheap boxes someone was willing to send over my way for almost nothing. But in the meantime since shipping will take a week or two. I began scouring the easy to get started options on [AWS](https://aws.amazon.com/), [Google Cloud Platform](https://console.cloud.google.com/), and [Azure](https://azure.microsoft.com/en-us/?v=18.20).

## First Cluster Launch on GCP

Ok, so even though I aim to have the hardware systems launched for a local dev cluster, I was on this search to find the most immediate way to get up and running without waiting. I wanted a cluster now, with a baseline setup that I could work with.

I opened up my [Google Cloud Platform](https://cloud.google.com) account to check out what options there are. The first option I found that is wildly easy to get started with involved navigating to the Cloud Launcher, typing in Cassandra, choosing the [DataStax Enterprise](https://www.datastax.com/products/datastax-enterprise) option and then clicking on Cloud Launcher. Note that if you do go this route it can get into the $300 or higher range very quickly depending on the selections chosen.

![gcp-building-datastax-enterprise-cluster](/wp-content/uploads/2018/06/gcp-building-datastax-enterprise-cluster.gif)

After clicking on create, the process begins building the cluster.

![gcp-building-datastax-enterprise-cluster-deployment.gif](/wp-content/uploads/2018/06/gcp-building-datastax-enterprise-cluster-deployment.gif)

Then generally after a few minutes you have the cluster up and running. If you’ve left the check boxes for the regions available, it’s a multi-region cluster, and if you’ve selected multiple nodes per cluster that gives you a multi-cluster, multi-region deployment. Pretty sweet initial setup for just a few minutes and a few clicks.

## Second Cluster Launch on Azure

I wanted to check out what the marketplace offered in Azure too, so I opened up the interface and did a quick search for the marketplace. It’s up yonder in the top of the interface on the … not the console, but here.

![azure-marketplace](/wp-content/uploads/2018/06/azure-marketplace.png)

Next we have to fill out a bunch of info per our business. In this case I just used the ole’ [Thrashing Code](https://twitter.com/thrashingcode) for this particular deployment. This is the first *create* of the process.

![dse1](/wp-content/uploads/2018/06/dse1.gif)

Then roll into that after it does the cross-auth of identity. Click *create* (this is the second create), and then some additional information around the C\* auth password, admin username and password, and then choose the subscription model, name of cluster, and region.

![dse2](/wp-content/uploads/2018/06/dse2.gif)

After all that the cluster will be up and running. Now, I could get into adding another cloud option with AWS but I’ll leave that for another day. I’ve already got two cloud providers up and running so I’ll just stick to working with those for now.

So that is one of the quickest way to get a full fledged cluster running in Azure or GCP. In the next post I’ll show you the ways to get up and running locally with Docker and some the options, and the limitations of running a distributed systems locally. Beyond that, I’ll also be diving in deep into detailed installation and configuration of a Cassandra and DSE Cluster in the coming days. Including building out one with actual hardware – yup, on the metal – so subscribe for all the details. Cheers!
