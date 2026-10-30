---
title: 'KubeCon 2018 Mission Objectives: Is the developer story any better?'
date: 2018-12-13 22:09:18 -0800
last_modified_at: 2018-12-13 22:09:18 -0800
permalink: /2018/12/13/kubecon-2018-mission-objectives-is-the-developer-story-any-better/
slug: kubecon-2018-mission-objectives-is-the-developer-story-any-better
wp_id: 15040
original_url: https://compositecode.blog/2018/12/13/kubecon-2018-mission-objectives-is-the-developer-story-any-better/
categories:
- Conferences
- kubecon
- Kubernetes
- Video
tags:
- ballerina
- coffee
- gloo
- kubecon
- kubecon 2018
- Kubernetes
- limebike
- tidb
excerpt: This is my second year at KubeCon. This year I had a very different mission than I did last year. Last year I wanted to learn more about services meshes, what the status of various features around Kubernetes like stateful sets, and overall get a better idea of what the overall shape of the product …
image: /wp-content/uploads/2018/12/kubecon.png
---

This is my second year at KubeCon. This year I had a very different mission than I did last year. Last year I wanted to learn more about services meshes, what the status of various features around Kubernetes like stateful sets, and overall get a better idea of what the overall shape of the product was and where the project was headed.

This year, I wanted to find out two specific things.

1. **Developer Story:** Has the developer story gotten any better?
2. **Database Story:** Do any databases, and their respective need for storage, have a good story on Kubernetes yet?

Well, I took my trusty GoPro Camera, mounted it up like the canon the [Predator](https://en.wikipedia.org/wiki/Predator_(film)) uses on my should and departed. I was going to attend this conference with a slightly different plan of attack. I wanted to have video and not only take a few notes, attend some sessions, and generally try to grok the information I collected that way. My thinking went along the lines, with additional resources, I’d be able to recall and use even more of the information available. With that, here’s the video I shot while perusing the showroom floor and some general observations. Below the fold and video I’ll have additional commentary, links, and updates along with more debunking the cruft from the garbage from the good news!

<iframe allowfullscreen="true" class="youtube-player" height="486" loading="lazy" sandbox="allow-scripts allow-same-origin allow-popups allow-presentation allow-popups-to-escape-sandbox" src="https://www.youtube.com/embed/EhVq598LEI0?version=3&amp;rel=1&amp;showsearch=0&amp;showinfo=1&amp;iv_load_policy=1&amp;fs=1&amp;hl=en-US&amp;autohide=2&amp;wmode=transparent" style="border:0;" width="863"></iframe>

**![Gloo-01](/wp-content/uploads/2018/12/Gloo-01.png)Gloo** – Ok, this looks kind of interesting. I stopped to look just because it had interesting characters. When I strolled up to the booth I listened for a few minutes, but eventually realized I needed to just dig into what docs and collateral existed on the web. Here’s what’s out there, with some quick summaries.

Gloo exists as an application gateway. Kind of a mesh of meshes or something, it wasn’t immediately clear. But I [RTFMed the Github Repo here](https://github.com/solo-io/gloo) and snagged this high level architecture diagram. Makes it interesting and prospectively offers insight to its use.

![high_level_architecture](/wp-content/uploads/2018/12/high_level_architecture.png)

Gloo has some, I suppose they’re “sub” projects too. Here’s a screenshot of the set of em’. Click it to navigate to solo.io which appears to be the parent organization. Some pretty cool software there, lots of open source goodness. It also leads me to think that maybe this is part of that first point above that I’m looking for, which is *where is the improved developer story*?

[![gloo.png](/wp-content/uploads/2018/12/gloo.png)](https://www.solo.io/)

More on that later, for now, I want to touch on one more thing before moving on to next blog posts about the KubeCon details I’m keen to tell you about.

![ballerina-logo](/wp-content/uploads/2018/12/ballerina-logo.png)

**Ballerina** – Ok, when I approached the booth I wasn’t 100% sure this was going to be what I was wanting it to be. Upon getting a demo (in video too) and then returning to the web – as ya do – then digging into the details and RTFMing a bit I have become hopeful. This stack of technology looks good. Let’s review!

The description on the [website](https://ballerina.io/) describes Ballerina as,

> “*A compiled, transactional, statically and strongly typed programming language with textual and graphical syntaxes. Ballerina incorporates fundamental concepts of distributed system integration and offers a type safe, concurrent environment to implement microservices with distributed transactions, reliable messaging, stream processing, and workflows.*“

which sounds like something pretty solid, that could really help developers build on – let’s say Kubernetes – in a very meaningful way. However it could also expand far beyond just Kubernetes, which is something I’ve wanted to see, and help developers expand and expedite their processes and development around line of business applications. Which currently, is still the same old schtick with the now ancient RAD tools all the way to today’s React and web tools without a good way to develop those with understanding or integrations with modern tooling like Kubernetes. It’s always, jam it on top, config a bunch of yaml, and toss it over the wall still.

A few more key points of how Ballerina is described on the website. Here’s the stated philosophy goal,

> “*Ballerina makes it easy to write cloud native applications while maintaining reliability, scalability, observability, and security.*“

Observability and security eh? Ok, I’ll be checking into this further, along with finally diving into [*Rust*](https://www.rust-lang.org/) in the coming weeks. It looks like 2019 is going to be the year I delve into more than one new language! Yikes, that’s gonna be intense!

**TiDB** – Clearly the team at PingCap didn’t listen to the repeated advice of “don’t write your own database, it’ll…” from Charity Majors and a zillion other people who have written their own databases! But hey, this one, regardless of the advice being unheeded, looks kind of interesting. Right in the [TiDB repo](https://github.com/pingcap/tidb) they’ve got an architecture diagram which is…  well, check out the diagram first.

![tidb-architecture](/wp-content/uploads/2018/12/tidb-architecture.png)

So it has a mySQL app protocol, that connects with the TiDB cluster, which then has a DistSQL API (??) and KV API connecting to the TiKV (which stands for Ti Key Value) which is a cluster, that then uses a DistSQL API to connect the other direction to a Spark Cluster. The Spark SQL can then be used. It appears the running theme is SQL all the things.

Above this, to manage the clusters and such there’s a “PD Cluster” which I also need to read about. If you watched the video above, you’ll notice the reference to it being the ZooKeeper of the system. This “PD Cluster ZooKeeper” thing manages the metadata, TSO Data Location and data location pertinent to the Spark Cluster. Overall, 4 clusters to manage the system.

Just for good measure (also in the video) the TiDB is built in Go, while the TiKV is built in Rust, and some of the data location or part of the Spark comms are handled with some Java Virtual Machine – I think – I might have misunderstood some of the explanation. So how does all this work? I’ve no idea at this point, but I’m curious to find out. But before that in the next few weeks and months I’m going to be delving into building applications in Node.js, Java, and C# against Cassandra and DataStax Enterprise, so I might add some cross-comparisons against TiDB.

Also, even though I didn’t get to have a conversation with anybody from Foundation DB I’m interested in how it’s working these days too, especially considering it’s somewhat storied history. But hey, what project doesn’t have a storied history these days right! Stay tuned, subscribe here on the blog, and I’ll have updates when that work and other videos, twitch streams, and the like are published.

After all those conversations and running around the floor, at this point I had to take a coffee break. So with that, enjoy this video on how to appropriately grab good coffee real quick and an amazing cookie treat. Cheers!

<iframe allowfullscreen="true" class="youtube-player" height="486" loading="lazy" sandbox="allow-scripts allow-same-origin allow-popups allow-presentation allow-popups-to-escape-sandbox" src="https://www.youtube.com/embed/jfdeBhOldIA?version=3&amp;rel=1&amp;showsearch=0&amp;showinfo=1&amp;iv_load_policy=1&amp;fs=1&amp;hl=en-US&amp;autohide=2&amp;wmode=transparent" style="border:0;" width="863"></iframe>

###### *Yes, I mispelled “dummy” it’s ok I don’t want to re-render it. I also know that the cookie name is kind of vulgar LOLz but you know what, welcome to Seattle we love ya even when you’re mind is in the gutter!*
