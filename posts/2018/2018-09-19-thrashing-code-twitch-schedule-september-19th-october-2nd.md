---
title: Thrashing Code Twitch Schedule September 19th-October 2nd
date: 2018-09-19 11:03:59 -0700
last_modified_at: 2018-09-24 14:26:06 -0700
permalink: /2018/09/19/thrashing-code-twitch-schedule-september-19th-october-2nd/
slug: thrashing-code-twitch-schedule-september-19th-october-2nd
wp_id: 14639
original_url: https://compositecode.blog/2018/09/19/thrashing-code-twitch-schedule-september-19th-october-2nd/
categories:
- c#
- golang
- Google Cloud
- Infrastructure
- ThrashingCode
- Video
tags:
- c#
- csharp
- go
- golang
- infrastructure as code
- streaming
- terraform
- twitch
- video
excerpt: 'I’ve got everything queued back up with some extra Thrashing Code Sessions and will have some on the rails travel streams. Here’s what the schedule looks like so far. Today at 3pm PST (UPDATED: Sep 19th 2018) UPDATED: Video available https://youtu.be/NmlzGKUnln4 I’m going to get back into the roll of things this session after the travels last …'
image: /wp-content/uploads/2018/09/thrashing-code-light-brackground-cropped1.png
---

I’ve got everything queued back up with some extra Thrashing Code Sessions and will have some *on the rails* travel streams. Here’s what the schedule looks like so far.

## [~~Today at 3pm PST~~](https://www.twitch.tv/events/a4jJlUtJQdaxeAvVCz-A0g) (UPDATED: Sep 19th 2018)

![thrashing-code-terraform](/wp-content/uploads/2018/09/thrashing-code-terraform.png)**UPDATED: Video available <https://youtu.be/NmlzGKUnln4>**

I’m going to get back into the roll of things this session after the travels last week. In this session I’m aiming to do several things:

1. Complete next steps toward getting a DataStax Enterprise Apache Cassandra cluster up and running via Terraform in Google Cloud Platform. My estimate is I’ll get to the point that I’ll have three instances that launch and will automate the installation of Cassandra on the three instances. Later I’ll aim to expand this, but for now I’m just going to deploy 3 nodes and then take it from there. Another future option is to bake the installation into a Packer deployed image and use it for the Terraform execution. Tune in to find out the steps and what I decide to go with.
2. I’m going to pull up the InteroperabilityBlackBox and start to flesh out some objects for our model. The idea, is based around something I stumbled into last week during travels, the thread on that is [here](https://twitter.com/Adron/status/1041001164802744320).

<blockquote class="twitter-tweet" data-dnt="true" data-width="550">
<p dir="ltr" lang="en">Just got this idea. I buy plane tickets and often fly first class at economy prices because I fly and I know things. It’s not really a knee idea but <a href="https://twitter.com/DeniseKGosnell?ref_src=twsrc%5Etfw">@DeniseKGosnell</a>’s keynote just pushed me further toward a prospective solution. It occurred to me…  <a href="https://twitter.com/hashtag/gdfs18?src=hash&amp;ref_src=twsrc%5Etfw">#gdfs18</a> <a href="https://twitter.com/hashtag/graph?src=hash&amp;ref_src=twsrc%5Etfw">#graph</a></p>
<p>— Adron (@Adron) <a href="https://twitter.com/Adron/status/1041001164802744320?ref_src=twsrc%5Etfw">September 15, 2018</a></p></blockquote>

<script async="" charset="utf-8" src="https://platform.twitter.com/widgets.js"></script>

## [Friday (Today) @ 3pm PST](https://www.twitch.tv/events/8Z7KGlTCQ5iZ2Tb4V8V_zQ)

![thrashing-code-gopher](/wp-content/uploads/2018/08/thrashing-code-gopher.jpg)This Friday I’m aiming to cover some Go basics before moving further into the [Colligere CLI](https://github.com/ThrashingCode/colligere)  app. Here are the highlights of the *plan*.

1. I’m going to cover some of the topics around program structure including: type declarations, tuple assignment, variable lifetime, pointers, and other variables.
2. I’m going to cover some basics on packages, initialization of packages, imports, and scope. This is an important aspect of ongoing development with [Colligere](https://github.com/ThrashingCode/colligere) since we’ll be pulling in a number of packages for generation of the data.
3. Setting up configuration and schema for the Colligere application using Viper and related tooling.

## [Tuesday, October 2nd @ 3pm PST](https://www.twitch.tv/events/a4jJlUtJQdaxeAvVCz-A0g)

![thrashing-code-terraform](/wp-content/uploads/2018/09/thrashing-code-terraform.png)This session I’m aiming to get some more Terraform work done around the spin up and shutdown of the cluster. I’ll dig into some more specific points depending on where I progress to in sessions previous to this one. But it’s on the schedule, so I’ll update this one in the coming days.
