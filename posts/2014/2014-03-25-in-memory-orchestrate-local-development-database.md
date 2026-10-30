---
title: In-memory Orchestrate Local Development Database
date: 2014-03-25 17:55:17 -0700
last_modified_at: 2014-03-25 17:55:17 -0700
permalink: /2014/03/25/in-memory-orchestrate-local-development-database/
slug: in-memory-orchestrate-local-development-database
wp_id: 9820
original_url: https://compositecode.blog/2014/03/25/in-memory-orchestrate-local-development-database/
categories:
- Databases
- Ideas
- My Updates
- Orchestrate.io
tags:
- c#
- data
- data store
- database
- development
- fake
- in memory database
- in-memory
- java
- javascript
- mock
- orchestrate
- orchestrate.io
- orchestrateio
- polyglot
- projects
- swap shop
- wrapper
excerpt: I was talking with Tory Adams @BEZEI2K about working with Orchestrate‘s Services. We’re totally sold on what they offer and are looking forward to a lot of the technology that is in the works. The day to day building against Orchestrate is super easy, and setting up collections for dev or test or whatever are so easy …
---

I was talking with Tory Adams [@BEZEI2K](http://twitter.com/BEZEI2K) about working with [Orchestrate](http://orchestrate.io/)‘s Services. We’re totally sold on what they offer and are looking forward to a lot of the technology that is in the works. The day to day building against Orchestrate is super easy, and setting up collections for dev or test or whatever are so easy nothing has stood in our way. Except one thing…

Every once in a while we have to work disconnected. For whatever the reason might be; Comcast cable goes out, we decide to jump on a train or one of us ends up on one of those Q400 puddle jumpers that doesn’t have wifi! But regardless of being disconnected from wifi, cable or internet connectivity we still want to be able to code and test!

## In Memory Orchestrate Wrapper

[![](https://photos.adron.me/Software/Misc-Images/Just-Icons-and-Bits/i-jHttDjn/0/Th/orchestrate.io-Th.gif)](http://orchestrate.io/)Enter the idea of creating an in memory Orchestrate database wrapper. Using something like [convict.js](https://github.com/mozilla/node-convict) one could easily redirect all the connections as necessary when developing locally. That way development continues right along and when the application is pushed live, it’s redirected to the appropriate Orchestrate connections and keys!

This in memory “*fake*” or “*mock*” would need to have the key value, events, and graph store setup just like Orchestrate. With the possibility of having this in memory one could also easily write tests against a real fake and be able to test connected or disconnected without mocking. Not to say that’s a good or bad idea, but just one more tool in the tool chest doesn’t hurt!

If something like this doesn’t pop up in the next week or three, I might just have to kick off this project myself! If anybody is interested please reach out to me and let’s discuss! I’m open to writing it in JavaScript, C#, Java or whatever poison pill you’d prefer. (I’m not polyglot to limit my options!!)

## Other Ideas, Development Shop Swap

Another idea that I’ve been pondering is setting up a development shop swap. I’ll leave the reader to determine what that means!  😉  Feel free to throw down ideas that this might bring up and I’ll incorporate that into the soon to be implementation. I’ll have more information about that idea right here once the project gets rolling. In the meantime, happy coding!
