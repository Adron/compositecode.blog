---
title: Docker Red Hat and Containerization Wreck Virtualization
date: 2014-04-15 12:13:26 -0700
last_modified_at: 2014-04-15 16:35:10 -0700
permalink: /2014/04/15/docker-red-hat-and-containerization-wreck-virtualization/
slug: docker-red-hat-and-containerization-wreck-virtualization
wp_id: 9894
original_url: https://compositecode.blog/2014/04/15/docker-red-hat-and-containerization-wreck-virtualization/
categories:
- Conferences
- Containers
tags:
- container
- containerization
- docker
- os-level virutalization
- red hat
- virtual machine
- virtualization
excerpt: Conversation has popped up around a few tweets Alex Williams regarding virtualization at the Red Hat Summit. One of the starts to the conversation. https://twitter.com/alexwilliams/status/456134531821887489/ Paraphrased the discussion has been shaped around asking, “Why is OS-level virtualization via containers (namely Docker) become such a massive hot topic?” With that, it got me thinking about some of the shifts around containerization and …
---

Conversation has popped up around a few tweets Alex Williams regarding virtualization at the Red Hat Summit. One of the starts to the conversation.

<https://twitter.com/alexwilliams/status/456134531821887489/>

Paraphrased the discussion has been shaped around asking,

> “Why is OS-level virtualization via containers (namely Docker) become such a massive hot topic?”

With that, it got me thinking about some of the shifts around containerization and virutalization at the OS level versus at the hyper-visor level. Here’s some of my thoughts, which seemed to match more than a few thoughts at Red Hat.

1. Virtualization at the hyper-visor level is starting to die from an app usage level in favor of app deployment via OS-level virtualization. Virtualization at the OS level is dramatically more effective in almost every single scenario that virtualization is used today for application development. I’m \**kind of*\* seeing this, interesting that RH is I suppose seeing this much more.
2. Having a known and identified container such as what Docker works with provides a dramatically improved speed and method for deployment over traditional hyper-visor based virtualized or pure OS based deployment.

There are other points that have brought up but this also got me thinking on a slight side track, what are the big cloud providers doing now? Windows Azure, AWS, Rackspace or GCE, you name it and they’re all using a slightly different implementation of virtualized environments. Not always ideally efficient, fast or effective but they’re always working on them.

…well, random thoughts aside, I’m off to the next session and some hacking in between. Feel free to throw your thoughts into the fray on twitter or in the comments below.
