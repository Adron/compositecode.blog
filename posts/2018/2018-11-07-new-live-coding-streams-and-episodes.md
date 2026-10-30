---
title: New Live Coding Streams and Episodes!
date: 2018-11-07 19:05:15 -0800
last_modified_at: 2018-11-07 19:05:16 -0800
permalink: /2018/11/07/new-live-coding-streams-and-episodes/
slug: new-live-coding-streams-and-episodes
wp_id: 14929
original_url: https://compositecode.blog/2018/11/07/new-live-coding-streams-and-episodes/
categories:
- golang
- Infrastructure
- Video
tags:
- coding
- colligere
- data generation
- data generator
- go
- golang
- hacking
- live stream
- programming
- streaming
- thrashing code
- thrashingcode
- video
excerpt: I’ve been working away in Valhalla on the next episodes of Thrashing Code TV and subsequent content for upcoming Thrashing Code Sessions on Twitch (follow) and Youtube (subscribe). The following I’ve broken into the main streams and shows that I’ll be putting together over the next days, weeks, and months and links to sessions and shows …
image: /wp-content/uploads/2018/09/thrashing-code-light-brackground-cropped1.png
---

I’ve been working away in [Valhalla](http://www.ballardspace.com/) on the next episodes of [Thrashing Code TV](https://www.youtube.com/playlist?list=PL4f75Y6Ce5sumWGGA5W1v2KPj2d6krlnc) and subsequent content for upcoming [Thrashing Code Sessions](https://www.youtube.com/playlist?list=PL4f75Y6Ce5stcnpMImuVjajHxNU6wCmlL) on Twitch ([follow](https://www.twitch.tv/adronhall)) and Youtube ([subscribe](https://www.youtube.com/channel/UCHSCXYCMOOS-VSUdRsn13GQ)). The following I’ve broken into the main streams and shows that I’ll be putting together over the next days, weeks, and months and links to sessions and shows already recorded. If you’ve got any ideas, questions, thoughts, just [send them my way](/contact/).

## [Colligere](https://www.youtube.com/playlist?list=PL4f75Y6Ce5ssuZE8aIFwmmycuU-LfY2RB) ([Next Session](https://www.twitch.tv/events/bzrFZhMmQxWeexLQypvS1A))

Coding has been going a little slow, in light of other priorities and all, but it’ll still be one of the featured projects I’ll be working on. Past episodes are available [here](https://www.youtube.com/playlist?list=PL4f75Y6Ce5ssuZE8aIFwmmycuU-LfY2RB), however join in on Friday and I’ll catch everybody up, so you can skip past episodes if you aren’t after specific details and just want to join in on future work and sessions.

In this next session, this Friday the 9th at 3:33pm PST, I’m going to be working on reading in JSON, determining what type of structure the JSON should be unmarshalled into, and how best to make that determination through logic and flow.

Since Go needs something to unmarshall JSON into, a specific structure, I’ll be working on determining a good way to pre-read information in the schema configuration files (detailed in the issue listed below) so that a logic flow can be implemented that will then begin the standard Go JSON unmarshalling of the object. So this will likely end up including some hackery around reading in JSON without the assistance of the Go JSON library. Join in and check out what solution(s) I come up with.

The specific issue I’ll be working on is located on Github [here](https://github.com/ThrashingCode/colligere/issues/9). These sessions I’m going to continue working on, but will be a little vague and will start working on the Colligere CLI primarily on Saturday’s at 10am. So you can put that on your schedule and join me then for hacks. If you’d like to contribute, as always, reach out via [here](/contact/), [@Adron](https://twitter.com/Adron), or via the [Github Colligere Repository](https://github.com/ThrashingCode/colligere) and let’s discuss what you’d like to add.

## Getting Started with Go

This set of sessions, which I’ve detailed in “[Getting Started with Go](/confs-meetups-events/getting-started-with-go/)“, I’ll be starting on [January 12th at 4pm PST](https://www.twitch.tv/events/ujdiUSXkR_GK3rbivxT91g). You can get the full outline and further details of what I’ll be covering on my “[Getting Started with Go](/confs-meetups-events/getting-started-with-go/)” [page](/confs-meetups-events/getting-started-with-go/) and of course the first of these sessions I’ve posted details on the [Twitch event page here](https://www.twitch.tv/events/ujdiUSXkR_GK3rbivxT91g).

- Packages & the Go Tool – import paths, package declarations, blank imports, naming, and more.
- Structure – names, declarations, variables, assignments, scope, etc., etc.
- Basic Types – integers, floats, complex numbers, booleans, strings, and constants.

## Infrastructure as Code with Terraform and Apache Cassandra

I’ll be continuing the Terraform, bash, and related configuration and coding of using infrastructure as code practices to build out, maintain, and operate Apache Cassandra distributed database clusters. At some point I’ll likely add Kubernetes, some additional *on the metal* cluster systems and start looking at Kubernetes Operators and how one can manage distributed systems on Kubernetes using this *on the metal* environment. But for now, these sessions will continue real soon as we’ve got some systems to build!

Existing episodes of this series you can check out [here](https://www.youtube.com/playlist?list=PL4f75Y6Ce5svN608wnU0_69u4qFiMdPw6).

## Getting Started with Multi-model Databases

This set of sessions I’ve detailed in “[Getting Started with a Multi-model Database](/confs-meetups-events/getting-started-with-multi-model-databases/)“, and this one I’ll be starting in the new years also. Here’s the short run down of the next several streams. So stay tuned, subscribe or follow my [Twitch](https://www.twitch.tv/adronhall) and [Youtube](https://www.youtube.com/channel/UCHSCXYCMOOS-VSUdRsn13GQ) and of course subscribe to the Composite Code blog (*should be to the left, or if on mobile click the little vertical ellipses button*)

1. An introduction to a range of databases: Apache Cassandra, Postgresql and SQL Server, Neo4j, and … in memory database. Kind of like 7 Databases in 7 Weeks but a bunch of databases in just a short session!
2. An Introduction – Apache Cassandra and what it is, how to get a minimal cluster started, options for deploying something quickly to try it out.
3. Adding to Apache Cassandra with DataStax Enterprise, gaining analytics, graph, and search. In this session I’ll dive into what each of these capabilities within DataStax Enterprise give us and how the architecture all fits together.
4. Deployment of Apache Cassandra and getting a cluster built. Options around ways to effectively deploy and maintain Apache Cassandra in production.
5. Moving to DataStax Enterprise (DSE) from Apache Cassandra. Getting a DSE Cluster up and running with OpsCenter, Lifecycle Manager (LCM), and getting some queries tried out with Studio.
