---
title: Node PDX – Introducing Adam Ulvi, Aron Racho, Christopher Meiklejohn, Max Ogden and Brock Whitten!
date: 2013-05-12 18:41:36 -0700
last_modified_at: 2013-05-12 18:41:36 -0700
permalink: /2013/05/12/node-pdx-introducing-adam-ulvi-aron-racho-christopher-meiklejohn-max-ogden-and-brock-whitten/
slug: node-pdx-introducing-adam-ulvi-aron-racho-christopher-meiklejohn-max-ogden-and-brock-whitten
wp_id: 8302
original_url: https://compositecode.blog/2013/05/12/node-pdx-introducing-adam-ulvi-aron-racho-christopher-meiklejohn-max-ogden-and-brock-whitten/
categories:
- Awesome Coders
- Community
- Conferences
tags:
- conference
- javascript
- node
- node pdx
- node.js
- nodejs
- nodepdx
excerpt: …and the fourth iteration begins! Adam Ulvi is presenting… Put a Sensor On It! Adam is a Portland native (straight out of the Simpsons) with a penchant for software and systems integration. 8-bit gamer, seasoned professional, perpertual noob. Specialization is for insects. Learn how easy it is to create your own monitoring system! Hobbyist components …
---

…and the fourth iteration begins!

***Adam Ulvi is presenting…***

## Put a Sensor On It!

![Adam Ulvi](/images/adronhall.smugmug.com/Software/Meetups-N-Conferences/Node-PDX-2013/i-rThLqBx/0/S/1cc2c674718448415c0eccb23b12295a-S.png)

*Adam Ulvi*

Adam is a Portland native (straight out of the Simpsons) with a penchant for software and systems integration. 8-bit gamer, seasoned professional, perpertual noob. Specialization is for insects.

Learn how easy it is to create your own monitoring system! Hobbyist components and a rich ‘maker’ community puts advanced system designs well within the reach of your average software wonk. Stop planning and start building!

Our case study is ‘GroMon’, a solution for monitoring a tiny indoor lettuce garden. Our wireless sensor keeps track of temperature and humidity, if the plants get too hot or too cold then we are notified via text message.

We will discuss the design goals and architecture, as well as component selection, prototyping and debugging steps. With a little bit of programming skill and patience, anyone can build this network. Learn how to easily extend this solution for your own use.

Our stack is Node.js running on a Raspberry Pi. We connect over Bluetooth to an Arduino hosting a single sensor. All components can be purchased off-the-shelf, no soldering is required and the total cost is around $80. Code and bill of materials is available on GitHub, let’s hack!

***Aron Racho is presenting…***

## Jive Purposeful Places SDK – A NodeJS Bromance

![Aron](/images/adronhall.smugmug.com/Software/Meetups-N-Conferences/Node-PDX-2013/i-j99VRrd/0/S/aronracho-S.jpg)

*Aron*

Aron Racho is a Senior Software Developer at Jive Software. Aron’s background has primarily been in Java, about 10 years in. He is a relatively recent convert to Javascript, and server-side Javascript in particular. Though relatively new to NodeJS, he has been smitten by its fluency, flexibility, and superb design. One might even say a Bromance has been started.

Ok, get ready, this description for this sessions is HUGE!

Jive Software’s latest cloud release enables 3rd party developers to easily push data marshalled from external systems of record such as Salesforce into Jive. Our aim is to publish a developer framework and API which makes it drop-dead simple — and fun — to get up-and-going from scratch, or easily integrate into an existing framework. We chose NodeJS precisely for those reasons:

- High developer adoption
- High velocity development — javascript! no compilation required
- Best-in-class IDE support (IntelliJ for example)
- Native support for REST and HTTP
- Excellent package management system (NPM == maven the Good Parts)
- Tons of great libraries
- Amazing documentation, well organized, very easy to get started instantly

Our framework is built on Express, and is designed to be programmed by “convention: fill in the blanks with logic specific to your application, and as long as you’ve satisfied the contract, the framework automatically:

- Wires up routes required for configuring your integration
- Notifies your listeners for integration life cycle events (integration created; destroyed; updated, etc.)
- Executes recurrent tasks you’ve scheduled
- Handles persistence of required objects. We have support for 3 types of persistence out of the box — in-memory, file, and MondoDB.

The framework is designed for developers who want to as quickly as possible start integrating a 3rd party service with Jive, with minimum setup.

For those interested in integrating Jive into an existing NodeJS Express app, we are going to make the underlying API available to developers, allowing them finer grained control over the setup of their integration. This API will be the same one underlying the mechanics of the aforementioned framework.

For my presentation, I will be describe how we used NodeJS as the basis for this framework and API. Please note at the time of this proposal, we’ve created the framework, and are now in the process of refining the API so that it can be used independently of the framework.

***Christopher Meiklejohn is presenting…***

## An Introduction to Functional Reactive Programming

![Chris Meiklejohn](/images/adronhall.smugmug.com/Software/Meetups-N-Conferences/Node-PDX-2013/i-pSGJpGf/0/S/3e09fee7b359be847ed5fa48f524a3d3-S.jpg)

*Chris Meiklejohn*

Christopher Meiklejohn is a Software Engineer with Basho Technologies, Inc. where he focuses on building rich web applications for Riak using Erlang and JavaScript. Before joining Basho, he worked at Swipely, a loyalty program startup based in Providence where he maintained critical infrastructure components written in Ruby. Christopher currently serves as one of the maintainers of Rubygems.org.

Chris also knows a thing or three about this show… called **[The Wire](http://en.wikipedia.org/wiki/The_Wire)**… he could probably speak entirely in quotes solely from The Wire and still make complete sense. So throw a quote out, I bet he’ll catch it.

There is no doubt that todays web applications continue to grow in adoption, replacing their desktop counterparts in all areas of computation. Essential to their growth is their ability to provide near-native performance and rich user experiences. As these applications grow in essential complexity, they also grow in accidental complexity due to the imperative callback processing style found in most web applications. The asynchronous nature of most of these applications also further compounds the issues due to guarantees around message ordering, and a level of indirection required in callbacks handling events.

Functional reactive programming is one approach for mitigating accidental complexity, using a declarative and composable data-flow model. During this talk, we’ll look at the history of functional reactive programming, some JavaScript implementations of FRP, and finally some ClojureScript implementations of FRP and examples on how to get started with using functional reactive programming.

***Max Ogden is presenting…***

## Minecraft.js

![Max Ogden - Penciled and colored!](/images/adronhall.smugmug.com/Software/Meetups-N-Conferences/Node-PDX-2013/i-Vw97kgp/0/S/fcc9bbfe2a31c5a6225cc287ed7ae2a6-S.png)

*Max Ogden – Penciled and colored!*

Max used to live here in Portland, and at some point defected to work on noble causes with Code for America. Since then he’s been an Oaktown Coder (Oakland, the other city near San Francisco).

In January of 2013 he started the [Voxel.js Project](http://voxeljs.com/). Since he and contributors have generatored nearly 100 node modules related to 3D game development and distribution. Examples including voxel rendering and first person controls and physics. On the main voxel-engine the project has received over 50 pull requests from 20 contributors. All of this since January. Max is going to dive into this effort and what inspiration people have taken to dive into game development with JavaScript.

***Brock Whitten is presenting…***

## Mighty Messaging Patterns

![Brock Whitten](/images/adronhall.smugmug.com/Software/Meetups-N-Conferences/Node-PDX-2013/i-kNg7Cmp/0/S/sintaxi-S.jpg)

*Brock Whitten*

Best know for having co-created PhoneGap, Brock went on to work at Joyent where he created the Public API for the beloved (and now sunset) No.de Platform. He’s now working on the Harp Platform where he’s worked with a team to have created a dead simple publishing platform that uses Dropbox as its deployment mechanism. Much has been learned, he’s read to share.

He describes his course as, “*Messaging is the lifeblood of distributed systems yet it is often treated as an afterthought when applications are architected. Few get passed the point of tacking on a message queue to fire and forget tasks with no visibility into what is happening on the system. I’m here to tell you we can do better. That Messaging can do more for us than just put tasks in the background. By combining basic messaging paradigms we can build powerful distributed systems with full awareness of what is happening around the network. And we can do it all in pure JavaScript.*

*In this talk, I will start with a crash course on the basic messaging patterns push/pull, pub/sub, and request/reply and then show a real example of how we have combined these patterns to build a custom message broker that we have used to build a fully distributed and modular architecture for the Harp Platform. I will share details about what we have learned and common pitfalls to avoid when building a messaging system for your needs.*

***Basic outline for the talk:***

- *how messaging can be useful*
- *crash course on the basic message patterns*
- *how to get started with zeromq/axon*
- *common pitfalls when in production*
- *proven trade secrets we have learned*

*By the end of the talk, my hope is that everyone will have a new appreciation for what can be achieved with massaging and will know where to begin when attempting to integrate messaging into their next project. I feel this aspect of building modern web applications is often overlooked and viable techniques need to be shared and discussed.*”

[![](/images/adronhall.smugmug.com/Software/Meetups-N-Conferences/Node-PDX-2013/i-mKbjXsb/0/O/NodePDX.png)](http://nodepdx.org/)Are you signed up?  [**BUY YOUR TICKET FOR NODE PDX HERE**](http://nodepdx.eventbrite.com/)

Want to learn more? <http://nodepdx.org/>

Want to know the dates? <http://nodepdx.org/>

Want to know who else is speaking? Stay tuned here or go check out <http://nodepdx.org/>!

Have a last minute request, idea, comment or a speaking proposal? <http://nodepdx.org/>
