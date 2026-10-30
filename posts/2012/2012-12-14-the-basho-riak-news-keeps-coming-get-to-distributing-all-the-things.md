---
title: The Basho Riak News Keeps Coming – Get to Distributing All The Things!
date: 2012-12-14 10:40:51 -0800
last_modified_at: 2012-12-14 10:40:51 -0800
permalink: /2012/12/14/the-basho-riak-news-keeps-coming-get-to-distributing-all-the-things/
slug: the-basho-riak-news-keeps-coming-get-to-distributing-all-the-things
wp_id: 7240
original_url: https://compositecode.blog/2012/12/14/the-basho-riak-news-keeps-coming-get-to-distributing-all-the-things/
categories:
- AWS
- Distributed Things
tags:
- multi-datacenter replication
- replication
- riak
- riakcs
excerpt: I mentioned earlier this week on Twitter that there was a deluge of software releases, additions and other goodies that would be released in the coming days. Earlier this week Jeremiah @peschkaj & OJ @TheColonial released the CorrugatedIron .NET Client for Riak. Big news for my .NET cohorts out there! It makes life uber easy …
---

I mentioned earlier this week on Twitter that there was a deluge of software releases, additions and other goodies that would be released in the coming days. Earlier this week Jeremiah [@peschkaj](http://twitter.com/peschkaj) & OJ [@TheColonial](http://twitter.com/TheColonial) released the [CorrugatedIron .NET Client for Riak](http://corrugatediron.org/). Big news for my .NET cohorts out there! It makes life uber easy to use Riak with. So don’t hold back if you’re in .NET land bumping up to some hard core data back end capabilities with Riak and Riak Cloud Storage.

[![](/images/adronhall.smugmug.com/Software/Software-Development/Basho-Misc/i-spqrD7z/0/O/aws_marketplace.png)](https://aws.amazon.com/marketplace)This second release is the [Amazon Web Services AMI Release](http://basho.com/blog/technical/2012/12/14/Riak-on-Amazon-Marketplace-AMI/). There’s been a number of customers that already use Riak & related OSS Tooling with AWS but this now makes it crazy easy to get up and running. I mean, it’s already really easy from an ops perspective, now with the .NET love and more for the dev perspective. Basho has a lot of *happy* for the DevOps out there – or the ops or devs if you’re still in segmented teams. 😉

For more information about the [AWS AMI](https://aws.amazon.com/marketplace/) check out the [Basho AWS Marketplace Page](https://aws.amazon.com/marketplace/pp/B00AMRXCQA/ref=sp_mpg_product_title?ie=UTF8&sr=0-2).

## More Key Information on Distributed Options

[![](/images/adronhall.smugmug.com/Software/Software-Development/Basho-Misc/i-3FBnDQ9/0/O/riak-cs-logo.png)](http://basho.com/products/riakcs/)Riak comes by default OSS but there are the additional CS & MDC options. CS stands for [**C**loud **S**torage](http://basho.com/products/riakcs/) and MDC stands for [**M**ulti-**D**ata **C**enter](http://basho.com/blog/technical/2012/11/30/Riak-CS-with-MDC-Replication/) Replication. A short description of each is CS is an S3 compatible object storage that you can setup on your own machines, very powerful and built on core Riak. MDC is built to provide geographically dispersed multi-data center replication, which is kind of obvious from the name. The skinny is, MDC can help you avoid those East 1 outages that seem to plague certain non-distributed sites every year or so. If you want to learn more about these technologies feel free to message me [@adron on Twitter](https://alpha.app.net/adron) or [@adron on ADN](https://alpha.app.net/adron), or fill out the standard [Basho Contact Form](http://basho.com/contact/) if you want to jump right into purchasing CS or MDC.

These two options are paid for options, with Riak CS being the core OSS Offering. That you can get to try out for free, just check out the [docs and they’ll point you to the places to get started](http://docs.basho.com/riak/latest/) or dive deep and hit the [code on github](https://github.com/basho/riak).

## The Amazon Web Services AMI, MDC and CS Notes

The AMI doesn’t have CS/MDC features but if you want to setup a multi-node example this is definitely the perfect starting point. In the next week I’ll also have some examples up from the perspective of setting up individual nodes and trying out the database. Shortly thereafter I’m going to dive into some much deeper distributed conversations from an architectural point of view and respectively diving in deeper with actual implementation details. So be sure to subscribe and I’ll be bringing the infos this way. Cheers!
