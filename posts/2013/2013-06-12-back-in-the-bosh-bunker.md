---
title: Back in the Bosh Bunker
date: 2013-06-12 10:32:25 -0700
last_modified_at: 2013-06-12 20:14:15 -0700
permalink: /2013/06/12/back-in-the-bosh-bunker/
slug: back-in-the-bosh-bunker
wp_id: 8442
original_url: https://compositecode.blog/2013/06/12/back-in-the-bosh-bunker/
categories:
- Cloud Foundry
- Infrastructure
tags:
- architecture
- bosh
- boshdb
- cassandra
- cloud foundry
- cloudfoundry
- riak
- stemcell
excerpt: In the last post on the topic of Bosh I put together a simple Cloud Foundry environment using the tools & repos of Stark & Wayne. Even though the bootstrap is a great way to get an environment up and started, it doesn’t explain a lot of things about Bosh. So let’s take a look …
---

In the last post on the topic of [Bosh I put together a simple Cloud Foundry environment](/2013/04/12/using-bosh-to-bootstrap-cloud-foundry-via-stark-wayne-consulting/) using the tools & repos of [Stark & Wayne](https://github.com/StarkAndWayne/). Even though the bootstrap is a great way to get an environment up and started, it doesn’t explain a lot of things about Bosh. So let’s take a look at what we’re dealing with here.

## Bosh – What is it?

Bosh handles deployment and upgrades of Cloud Foundry environments. However, it isn’t particularly limited to just Cloud Foundry. It’s been used to launch Riak Clusters, setup Redis, Cassandra, CouchDB and other services that don’t just fit neatly in the Cloud Foundry services design.

It is a very important tool in regards to keeping a Cloud Foundry environment up to date with the latest bits, security fixes, bugs and related elements. Bosh is broken down into several key components that work together to handle these deployment and maintenance tasks.

To put it another way, Bosh aims to give ops or devops the ability to throw together an entire stack to deploy. Bosh starts with stemcells, packages and jobs as the core concepts of how it works.

Bosh is used, within Cloud Foundry and prospectively for whatever anyone would want to use it for, to launch instances, change out the instances, change networking values, IPs and other configuration information. Overall it kind of rolls a lot of other tooling (chef, puppet) together into one tool. How well it does this is up for debate, but I’m not arguing what it is here, just going to get some definitions here.

## The Pieces of BOSH

### Stemcells

A stem cell or stemcell is something that is a bit hard to track down a definition for. I’m taking a stab at it with what I know a stem cell is, so if you have any corrections please comment below – I’ll be more than happy to add a correction or three. Overall I understand a stem cell to be a complete framework stack built on some sort of virtual image. It can be thought of as the recipe for building an operating systems that will act as an active member of a Cloud Foundry environment. In some situations, such as with a distributed database like Riak, it becomes not so much a member of the Cloud Foundry environment itself but an active node available to a distributed database cluster. This can then be used as a distributed database that is managed by Bosh and accessible within the Cloud Foundry ecosystem.

### Packages

A package is sourec with the appropriate scripts for building it into usable binaries. Think of this as a package in the Node.js NPM, Gems (Ruby/Rails), or Nugets (.NET) worlds. It’s something that Bosh will pull in and compile on demand.

There are a few key parts to a package, referred to as package specs. These are: name, dependencies and files. Of the specs, the name and files are really the only required parts. The dependencies are an optional list of other packages this package would depend on.

### Jobs

This is pretty self-descriptive. The jobs within Bosh spool up, start servers and services and other miscellaneous responsibilities as needed.

##### Relavent Sites, Documentation & Key Content

- [The Cloud Foundry Bosh Repo](https://github.com/cloudfoundry/bosh) => This is the actual code repository on Github. If you’re in need of really diving into what it does, there’s always the possibility of reading the code!
- [Cloud Foundry Documentation](http://docs.cloudfoundry.com/) => This has links to documentation related to Bosh that is pivotal (no pun intended).
- [Bosh Documentation](http://cloudfoundry.github.io/docs/running/deploying-cf/) => This is the Bosh documentation. It’s almost a good idea to start on the “[Running Cloud Foundry](http://cloudfoundry.github.io/docs/running/)” part of the documentation. This documentation can use your help (it’s super sparse at the moment), so if you get going and using Bosh, please contribute with examples and other material.
- [Stark & Wayne Repositories](https://github.com/StarkAndWayne/) => I already mentioned them, but they’re likely some of the best material out there.![](https://lh4.googleusercontent.com/Zu08KvQ3wdF1G23Ans7l0inyCG5n0OzHUIbKc65el2KJ02FfmWp_p8nBYuZCjmSRmQ2zSc1R3ZXN6GJqRqCMGI3nrFUg6aw_O-wWY65x_Z8kmIVIFb49TgZO)
- [Bosh DB](http://boshdb.cloudfoundry.com/) => This is a site & repository that Brian McClain [@brianmmcclain](https://twitter.com/brianmmcclain) put together to keep track of bosh stem cells and other repositories related to launching certain tools, services, servers and other things in Cloud Foundry environments via Bosh.
- [Dr Nic’s intro to Bosh](http://drnicwilliams.com/2012/05/15/bosh-what-how-when/) => This page serves as an into and description of what’s going on in Bosh. I read this a while back for my own kick off with the Bosh Tool.

### Summary

This is what I’ve found and put together as a good starting point. I still think there’s a bit of confusion around what Bosh is, how it works, how to get started with it and having it clearly defined on the web. Documentation is getting better, but still needs a lot of work (remember, you too can contribute). For systems outside of Cloud Foundry it also is a bit difficult and sometimes sketchy to use Bosh as the primary means of deployment, maintenance and upgrading. But just like the documentation that is also getting better. I’ll have more coming in the near future regarding what Bosh is, how it works, and things you can do with it – until then check out Dr Nic’s material for the most up to date how-to and related documentations and videos. He’s done some great work with the tooling and continues to knock it out of the park.

Keep reading and I’ll have more definitions, outlines of what is what, and the entire [inception](http://en.wikipedia.org/wiki/Inception) that Bosh is.
