---
title: '#altnetseattle – MEF, What is it?'
date: 2010-04-11 09:17:30 +0000
last_modified_at: 2010-10-04 11:19:18 -0700
permalink: /2010/04/11/altnetseattle-mef-what-is-it/
slug: altnetseattle-mef-what-is-it
wp_id: 714
original_url: https://compositecode.blog/2010/04/11/altnetseattle-mef-what-is-it/
categories:
- Conferences
tags:
- altnet
excerpt: I dived into the MEF session with Glenn Block, Sourabh Mathur, Brian Henderson, and others. Glenn covered the basic architectural ideas of MEF and then dived into a few examples. Is a framework around decoupling components. Built around the idea of discoverable type systems. Traditional extensibility mechanisms have a host and the respective extensions, commonly …
---

I dived into the [MEF](http://mef.codeplex.com/) session with Glenn Block, Sourabh Mathur, [Brian Henderson](http://twitter.com/brian_henderson), and others.  Glenn covered the basic architectural ideas of [MEF](http://mef.codeplex.com/) and then dived into a few examples.

- Is a framework around decoupling components.
- Built around the idea of discoverable type systems.
- Traditional extensibility mechanisms have a host and the respective extensions, commonly linking these two aspects with a form of registration.
- [MEF](http://mef.codeplex.com/) removes the need for the registration part of the architecture and uses a contract.
- At some point with [MEF](http://mef.codeplex.com/) you get down to *parts*, which removes even the complexity of a host or extensions, but a truly evolvable architecture based on natural growth of *parts*.
- Also referred to as the framework that removes the “*new*” keyword.
- The idea is that parts pull together other parts that they need.  Between each part is a contract.
- Each part has imports or exports for the parts it needs or the things it offers.

If one checks out the [MEF Codeplex Site](http://mef.codeplex.com) you will find a host of additional information.  The framework download also has some decent examples that help one get kick started.
