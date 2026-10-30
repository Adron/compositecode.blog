---
title: Another Day of Troubleshooting
date: 2008-11-12 02:33:00 -0800
last_modified_at: 2008-11-12 02:33:00 -0800
permalink: /2008/11/12/another-day-of-troubleshooting/
slug: another-day-of-troubleshooting
wp_id: 561
original_url: https://compositecode.blog/2008/11/12/another-day-of-troubleshooting/
categories:
- Uncategorized Bits
tags: []
excerpt: The application I'm working on has Java Back end and .NET Back end code projects. This leaves a lot of little hacks here and there for communication between these two code bases. By mere functional fact, it leaves the entire application connectivity between these two code bases in a weird state of coupling, or lack …
---

The application I'm working on has Java Back end and .NET Back end code projects. This leaves a lot of little hacks here and there for communication between these two code bases. By mere functional fact, it leaves the entire application connectivity between these two code bases in a weird state of coupling, or lack thereof.

The Java side, anytime something changes, is not particularly propagated to the .NET project side. Thus any changes between either or, leave the unchanged side in a lurch for forward development. There is an easy way to resolve almost all of the issues with this mixed environment of development.

## Service Oriented Architecture

A service oriented architecture, not a partial or supposed one, but an honest to goodness business case serving stand alone services oriented architecture that can be used by front end client, applications, or even other services would resolve this odd dependency issue.

### Communication

Instead of two varying code bases trying to communicate with differing and often confusing session architecture or passing back and forth query string parameters, with SOA state can be managed in a completely different manner. With the services available to the application the state could even prospectively be managed specific to the services instead of the client. This way WCF or the other slew of service frameworks out there could utilize their built in state management capabilities to enable the clients to perform their workflow or what have you flawlessly between Java, .NET, PHP, or whatever might be on the client side.

### Security

Yeah, yeah, yeah, I know, services, at least web services, aren't oriented at all toward security. But with frameworks like WCF the increased ability to lock down, provide authentication, and even authorization is drastically simplified. Not as many "hacks" are needed to secure web services these days. With that an SOA project could easily be setup for strong security, with extensive services and appropriately loosely coupled silos.

### Workflow

This is where I need to strengthen my skill sets. I've actively been working with WCF lately and know there is a good bit of integration with workflow that is possible. The problem is, I don't know what or how it works from an integration perspective. This will definitely be on my list of "figure it out". However, even without the dedicated workflow framework, setting up and utilizing the WCF for control of state, the inherent abilities with session control, etcetera, drastically alter the conflicts in autonomous code bases working together in an application environment.
