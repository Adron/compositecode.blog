---
title: My Node.js Story
date: 2018-04-25 09:21:50 -0700
last_modified_at: 2018-04-25 11:48:11 -0700
permalink: /2018/04/25/my-node-js-story/
slug: my-node-js-story
wp_id: 13852
original_url: https://compositecode.blog/2018/04/25/my-node-js-story/
categories:
- Conferences
- Node.js Things
- nodejs
tags:
- conferences
- developer conferences
- history
- javascript
- node pdx
- node.js
- nodepdx
excerpt: Once upon a time in a part of the tech universe far far away, there was a general consensus to block all JavaScript from browser execution. It was the way things were because JavaScript was seen as harmful. You see, the early miscreants of that time had used JavaScript to write all sorts of problematic …
image: /wp-content/uploads/2018/04/node_pdx_2016_-_adronhall.png
---

Once upon a time in a part of the tech universe far far away, there was a general consensus to block all JavaScript from browser execution. It was the way things were because JavaScript was seen as harmful. You see, the early miscreants of that time had used JavaScript to write all sorts of problematic code that would attack, steal, or otherwise undermine the data one sent across and received on the internet. This is the time I could have started learning JavaScript, but because of its horrid reputation I stayed far away and wrote C, C++, C#, Java, and event some RPG, COBOL, Pascal, and some other code. It was glorious, and the languages were beautiful in their own ways, while JavaScript was shunned by almost everybody in that tech universe! **\*\***

Today, things aren’t all that much different, but we make it easier for the whole horde of miscreant scripters to write problematic code in JavaScript. The difference is we allow it everywhere and just try to catch it and prevent execution. Thus, different, but the same, it’s a crazy world we live in.

I started picking up a little JavaScript at the tail end of 2007, when the “[JavaScript: The Definitive Guide](http://shop.oreilly.com/product/9780596000486.do)” was the top book to delve deeply into using JavaScript. It wasn’t another year until the seminal “[JavaScript: The Good Parts](http://shop.oreilly.com/product/9780596517748.do)” cut down the size of what one really needed to delve into by removing the cruft and focusing on the good parts. Slowly, JavaScript was finally starting to take shape as something useful.

Writing JavaScript at this time was a mutant challenge of having it look like Java while being organized like a trash pile of scripts that had no way to manage dependencies or otherwise. I mean, NPM was years away from existing, and really the concept of libraries in JavaScript seemed to be a foreign concept at the time.

2008 rolled around, “[JavaScript: The Good Parts](http://shop.oreilly.com/product/9780596517748.do)” came out, the changes started rippling through the industry and as traction started to mount. The penultimate event occurred the following year in 2009, which at the time almost nobody noticed. Dahl started Node.js at Joyent to enable server side JavaScript code use. At the time, many were flummoxed by the notion, weren’t confident in the single threaded event loop, and overall its release and the project continuing were in jeopardy from this point.

*But the project continued and persisted!*

Two more years of development, which I knew of and even met, talked with, and had the chance to see Dahl present in Seattle at [Seattle Scalability Meetup](https://www.meetup.com/Seattle-Scalability-Meetup/). I still hadn’t spent any real time dedicated to learning how to write JavaScript or even deal with this new Node.js thing! I was still slinging some solid C#, Java, and more SQL than I even cared to admit.

I then fell even further away from any notion of learning JavaScript further by getting into distributed database systems with Riak (It’s a now somewhat dead distributed database written in Erlang). It was honestly one of the most bad ass distributed databases that has or did exist! But I digress, I had fallen far outside of needing JavaScript but still had a huge fascination and interest in web development. At least, in a peripheral “*I want to know this so I can build whatever I’d like when I’d like*” type of way.

![2012-logo](/wp-content/uploads/2018/04/2012-logo.png)The turning point for me, while in the midst of working on cloud, distributed systems, and even fighting with Cloud Foundry, my good friend Troy Howard ([@thoward37](https://twitter.com/thoward37)) and I after a few rounds decided we were going to run a conference as an excuse to learn Node.js better. That evening at The Side Door in Portland we decided we’d name the conference [Node PDX](http://nodepdx.org/) and hold it in just about ~4 weeks. What’s obvious in hindsight is that one doesn’t merely run a conference with just ~4 weeks to organize it, but that’s what we did and we managed to – miraculously – pull it off!

With this conference it lit of an interest far beyond what I had expected. Troy and I were already starting, after this great experience organizing and running this conference with this absolutely stellar community and audience, we were ready for round two! At the time both he and I spent a little time helping out AppFog (previously PhpFog, now gobbled up by CenturyLink). By proxy of this we started, oddly enough largely on the side, getting more and more into Node.js and JavaScript itself.

![nodepdx-badge_256x128_white_noborder.gif](/wp-content/uploads/2018/04/nodepdx-badge_256x128_white_noborder.gif)Node PDX then took on it’s 2013 version! Again, a super awesome experience for all and more JavaScript everywhere! We started to get involved with Nodebots, drones, and more with the community at this conference. Node.js was enabling JavaScript to permeate practically every project at this juncture in time. Which was great for us that actually dug JavaScript, but horrible for those that hated JavaScript. But haters, meh.

![IMG_3529-5K](/wp-content/uploads/2018/04/img_3529-5k.jpg)

The organizing of this Node PDX had Luc Perkins join Troy and I. We expanded even further and this event was really huge, with more peripheral activities and even more hacking on cool projects, conversations, and things launched outside of the conference itself then we could have even imagined. It’s rather amazing what started as just a random idea over beers (while hacking on some code projects) can turn into!

This slideshow requires JavaScript.

Then, my experience and use of Node.js with intensive client and server side JavaScript was amplified even further when I formed a startup with my friend Aaron. This was a great experience, even met and brought in Milan ([@MilanLoveless](https://twitter.com/MilanLoveless)) to help out with coding, and built a wicked awesome distributed ingest and processing analysis system (even with a little sprinkling of early days machine learning) all with Node.js. JavaScript EVERYWHERE!

Over the years since, we’ve had another Node PDX which was awesome too. We’re aiming, prospectively, for another one in the coming years but we’ve not pinpointed the exact dates yet.

In the meantime I’ve started writing a ton of other code that isn’t always in JavaScript. More C#, Java, Go, and even some Python. I’ve gotten mixed up in the wild landscapes of data analysis tools running machine learning algorithms all the way to some of this crazy site reliability work in the midst of devops monikers writing server side CLIs with JavaScript and Go. But nothing specifically focused around writing JavaScript with Node.js in spite of my working to keep up with where the technology is headed for the future.

Because really, if things unfold right, JavaScript and Node.js are positioned for continued growth and relevance going forward. There’s significant reasons to move forward projects with that versus a lot of traditional stacks. It’s led the way technologically (remember when Nodejs had streaming? Yeah, like a year or more before most of the other stacks, and it was implemented well versus the trash pile of streaming in let’s say, the .NET world – since fixed, but at the time holy smokes it was bad). This trend continues with Node.js, albeit the stack being a bit more consistent, solid, and enterprise focused now than it was back in the early days of 2009-2013.

Now I’m at GOTO Conf Chicago, 2018, about to present tomorrow on the wild gesticulations of Node.js and JavaScript over the years and where it’s headed. I’ve even [started to put together a reference app](https://github.com/Adron/nodes-for-nodes-node-nodal-system) (which goes slowly at the moment). I’m rolling multiple nodes of Node.js and using Cassandra for a multiple cluster node underneath all that with Kubernetes hosting said service nodes on Kubernetes nodes all amongst it. Needless to say I think my title is fitting, “[Node Systems for Node.js Services on Nodes of Systemic Nodal Systems](/confs-meetups-events/nodes-for-nodes-node-nodal-system/)“. It’s gonna be a fun talk, and a great place-marker for me as Node.js v10 has just been released, and Nodejs itself is turning 9 this year!

Alas, the story continues, and I’m looking forward to the saga!

**Notes:**

**\*\*** The tech universe that I speak of was merely, shockingly, the tech universe of the early 00’s and late 90’s. JavaScript, being created in 1995 and not really gaining real traction as anything legitimate to use for application development until around 2005-2008. Even then, so often seen as problematic, and today we just seem to deal with the frustrations of using a scripting language as the primary driver of modern web based application development.
