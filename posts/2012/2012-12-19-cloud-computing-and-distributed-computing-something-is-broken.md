---
title: Cloud Computing and Distributed Computing, Something is Broken
date: 2012-12-19 12:28:49 -0800
last_modified_at: 2012-12-19 12:28:49 -0800
permalink: /2012/12/19/cloud-computing-and-distributed-computing-something-is-broken/
slug: cloud-computing-and-distributed-computing-something-is-broken
wp_id: 7256
original_url: https://compositecode.blog/2012/12/19/cloud-computing-and-distributed-computing-something-is-broken/
categories:
- Architecture
tags: []
excerpt: First off, I’m going to start off with some definitions to clarify things for this conversation. Cloud Computing, in general, has been perverted to mean almost anything available for sale today in technology. It’s rhetorically stupid. But we all still use the term to some degree. Going back to cloud computing at the core, we’re …
---

First off, I’m going to start off with some definitions to clarify things for this conversation.

***Cloud Computing***, in general, has been perverted to mean almost anything available for sale today in technology. It’s rhetorically stupid. But we all still use the term to some degree. Going back to cloud computing at the core, we’re talking about systems, virtually managed and often distributed. Distributed geographically with no single real point of failure. Almost every cloud computing enabled site or system these days are a complete lie when it comes to geographically dispersed, cloned nodes with no real point of failure, that is resilient to outages and related problems.

***Distributed Systems***, this is a term that is not contorted or misused – albeit at this moment in time. There’s always possibilities that the media completely botches it up later. But right now, distributed computing, distributed databases and distributed systems generally refers to what cloud computing used to *sort of* mean. So here’s some specific definitions of distributed technology.

- **Distributed computing** refers to the use of distributed systems to solve computational problems. In distributed computing, a problem is divided into many tasks, each of which is solved by one or more computers, which communicate autonomously. ref: <http://en.wikipedia.org/wiki/Distributed_computing>
- A **distributed database** is a database in which storage devices are not all attached to a common processing unit such as the CPU. It may be stored in multiple computers located in the same physical location, or may be dispersed over a network of interconnected computers. Unlike parallel systems, in which the processors are tightly coupled and constitute a single database system, a distributed database system consists of loosely coupled sites that share no physical components.Collections of data (e.g. in a database) can be distributed across multiple physical locations. A distributed database can reside on network servers on the Internet, on corporate intranets or extranets, or on other company networks. The replication and distribution of databases improves database performance at end-user worksites.To ensure that the distributive databases are up to date and current, there are two processes: replication and duplication. Replication involves using specialized software that looks for changes in the distributive database. Once the changes have been identified, the replication process makes all the databases look the same. The replication process can be very complex and time consuming depending on the size and number of the distributive databases. ref: <http://en.wikipedia.org/wiki/Distributed_database>

So these definitions provide a basis for my next topic point and frustration with the current state of “cloud computing” providers. To summarize what this problem I have is, it simply is that almost every provider continues to perpetuate legacy client to server, or server heavy with a RDBMS or single point of failure database on the back end. This is completely missing the advantages of cloud computing in so many ways. The high availability, the resiliency, the performance of scaling by adding nodes versus other vastly more expensive means. One of those standard means is throwing away one machine to get a bigger more powerful machine, which has distinct and clear limitations. Let’s look at some specific examples that are encouraged by the providers.

## The Failures in Cloud Computing & Distributed Systems

**SharePoint** – I’m not picking on SharePoint in this particular scenario because of its notoriously poor user experience or worse developer experience, I’m calling it out for a single point of failure architecture. Sharepoint doesn’t rely on a distributed database. It also can’t be easily installed in any easy way on multiple web application servers to share load. Even if it was, the relational database holds very distinct and specific limitations that cannot be overcome. In large environments it must be sharded at an application level, so in large corporations with heavy usage the system runs into all sorts of complex bottlenecks and performance nightmares.

**Standard RDBMS + Web App** – This is a very common database configuration which, if kept in a RDBMS dramatically raises data storage cost for any site that needs scaled. The largest problem with scaling, is that an RDBMS is setup for vertical scale improvements, in other words the “*buy a bigger machine with more resources*” solution. This is not very ideal if you want to actually maintain high availability. In all actuality, having an RDBMS alone as the primary data repository is probably one of the worst existing and continually encouraged architectural decisions made for any website that may one day need to scale.

**CRMs and Other ERP, Single Repo Mail Servers** – This list is huge. Whether it is Exchange attached to a proprietary data store, stuck on top of Oracle, or glued to some sharded database or data store of sorts it is another bad implementation of distributed computing resources. CRMs almost always sit on top of some relational database that is geographically bound. Another one that is a huge problem is ERP tooling in general. These frequently sit on top of price coupled, proprietary databases like Oracle or SQL Server, with no clear scaling plan except to just “wait for it to process” types of situations. Many large corporations end up having to work around these problems with massively expensive custom solutions of these products, especially when you’re employee count is over 50k, which there are more than a few of those out there.

## The Future

So don’t be fooled into thinking you’re getting some “cloud solution” with these solutions using traditionally designed architectures. The solutions of the future will be distributed, utilizing the computing grid better, and prospectively cheaper in many ways. Whatever the case the marketing push for the cloud has become worthless, and if you’re looking for the real power in computing these days you’ll look into distributed systems and how those work for you. There’s massive potential in properly distributing systems and building out applications accordingly, much of this potential has only begun to be tapped.
