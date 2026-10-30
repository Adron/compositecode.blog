---
title: Property Graph Modeling with an FU Towards Supernodes – Jonathan Lacefield
date: 2018-12-08 18:55:07 -0800
last_modified_at: 2018-12-08 18:55:07 -0800
permalink: /2018/12/08/property-graph-modeling-with-an-fu-towards-supernodes-jonathan-lacefield/
slug: property-graph-modeling-with-an-fu-towards-supernodes-jonathan-lacefield
wp_id: 14988
original_url: https://compositecode.blog/2018/12/08/property-graph-modeling-with-an-fu-towards-supernodes-jonathan-lacefield/
categories:
- Video
tags:
- datastax
- datastax enterprise
- graph
- graph database
- graph modeling
- jonathan lacefield
- property graph
- supernodes
excerpt: Some notes along with this talk. Which is about ways to mitigate super nodes, partitioning strategies, and related efforts. Jonathan’s talk is vendor neutral, even though he works at DataStax. Albeit that’s not odd to me, since that’s how we roll at DataStax anyway. We take pride in working with DSE but also with knowing …
image: /wp-content/uploads/2018/12/impacts.png
---

Some notes along with this talk. Which is about ways to mitigate super nodes, partitioning strategies, and related efforts. Jonathan’s talk is vendor neutral, even though he works at DataStax. Albeit that’s not odd to me, since that’s how we roll at DataStax anyway. We take pride in working with DSE but also with knowing the various products out there, as things are, we’re all database nerds after all. (*more below video*)

<iframe allowfullscreen="true" class="youtube-player" height="486" loading="lazy" sandbox="allow-scripts allow-same-origin allow-popups allow-presentation allow-popups-to-escape-sandbox" src="https://www.youtube.com/embed/4_KzZAzoIPs?version=3&amp;rel=1&amp;showsearch=0&amp;showinfo=1&amp;iv_load_policy=1&amp;fs=1&amp;hl=en-US&amp;autohide=2&amp;wmode=transparent" style="border:0;" width="863"></iframe>

In the video, I found the definition slide for super node was perfect.

![supernodes.png](/wp-content/uploads/2018/12/supernodes.png)

See that super node? Wow, Florida is just covered up by the explosive nature of that super node! YIKES!

In the talk Jonathan also delves deeper into the vertexes, adjacent vertices, and the respective neighbors. With definitions along the way, so it’s a great talk to watch even if you’re not up to speed on graph databases and graph math and all that related knowledge.

![impacts](/wp-content/uploads/2018/12/impacts.png)

![traversal.png](/wp-content/uploads/2018/12/traversal.png)

The super node problem he continues on to describe have two specific problems that are detailed; query performance traversals and storage retrieval. Such as a Gremlin traversal (one’s query), moving along creating traversers, until it hits a super node, where a computational explosion occurs.

Whatever your experience, this talk has some great knowledge to expand your ideas on how to query, design, and setup data in your graph databases to work against. Along with that more than a few elements of knowledge about what not to do when designing a schema for your graph data. Give a listen, it’s worth your time.
