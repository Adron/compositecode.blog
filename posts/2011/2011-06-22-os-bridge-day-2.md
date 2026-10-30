---
title: 'OS Bridge Day #2'
date: 2011-06-22 14:13:01 -0700
last_modified_at: 2011-06-22 15:00:02 -0700
permalink: /2011/06/22/os-bridge-day-2/
slug: os-bridge-day-2
wp_id: 3110
original_url: https://compositecode.blog/2011/06/22/os-bridge-day-2/
categories:
- Conferences
tags: []
excerpt: 'Now, For Day #2 So now, after all that from yesterday let’s get to today. Today kicked off a little later than day #1, for various undisclosed reasons. 🙂 Run JavaScript Everywhere, With Jellyfish (Details about Run JavaScript Everywhere, With Jellyfish) Adam Christian The first session of today was for Jellyfish Javascript Execution Engine. By Adam Christian & his cohort from Yammer. This session also had a HUGE DOSE of WRITE CODE FOR YOUR APPS OR YOU’LL PAY THE PRICE OF BAD CODE added to it. Which for me, was a bit of choir preaching. 😉 I’m all about the tests and can’t imagine code bases without tests. (I suppose I could, but I’d have nightmares). The Jellyfish Effort is a Node Project working toward getting your JavaScript to run everywhere. For even more detailed information about the project check out the Jellyfish Github Site. Some of the other things to check out if you’re interested in Jellyfish and browser testing: Windmill Sauce Labs (Multi-browser testing, absolutely amazing, check it out!) At this juncture it was lunch time, which involved the most kick ass collection of food carts in America! If you’ve not heard about or seen the Portland Food Cart Scene, read up on it here and here and here. Maybe I am wrong, maybe the Portland Food Carts are actually the best in the world? Stay tuned, I’ll have more later as the open source coding continues.'
---

First a quick catch up on the afternoon and evening activities from day #1.

Linuxcon in Vancouver, British Columbia!

I discovered that [Linuxcon will be in Vancouver](http://opensource.com/life/11/6/telecomix-anonymous-anarchy-and-getting-things-done-through-do-ocracy) this year. Linus will be coming to keynote with another 10 keynote sessions following that. To top all that off, it will be the 20th anniversary for Linux!  For more information check out the following:

- [Linux Foundation Announcement](http://events.linuxfoundation.org/events/linuxcon)
- [Linuxcon Schedule Annouced Including Torvals, Mickos, Whitehurst](http://opensource.com/life/11/6/linuxcon-schedule-announced-including-torvalds-mickos-whitehurst)

## Portland City Startup, Meet the Startup

While talking with people I stumbled upon an interesting interview and write up by Rick Turosczy with Portland’s Mayor Sam Adams. In the interview he discuss Portland from the perspective of the city being a startup. Great write up and interview, check it out.

[Meet the Startup – Portland Mayor Sam Adams Part 1](http://siliconflorist.com/2011/06/21/meet-the-startup-conversation-portland-mayor-sam-adams-part-1/)

<iframe allowfullscreen="true" class="youtube-player" height="390" loading="lazy" sandbox="allow-scripts allow-same-origin allow-popups allow-presentation allow-popups-to-escape-sandbox" src="https://www.youtube.com/embed/lyzSI2wxK4M?version=3&amp;rel=1&amp;showsearch=0&amp;showinfo=1&amp;iv_load_policy=1&amp;fs=1&amp;hl=en-US&amp;autohide=2&amp;wmode=transparent" style="border:0;" width="640"></iframe>

For more [Meet the Startup check out their site](http://www.meetthestartup.com/).

## Evening Hacking & Beers

After the events of the day I headed to Bailey’t to meet up with some other coders where I got a short crash course on a couple of awesome technologies.  One technology I had been meaning to download and install. It was cool to get a quick review of [Node.js](http://nodejs.org/).

If you’re doing any sort of web development or software development in general, you need to go and try out [Node.js](http://nodejs.org/) and see what it is about. To see the power of node, just start by taking a look how you execute it. The following line starts the server (after installing it of course).

```bash
% node example.js
Server running at http://127.0.0.1:1337/
```

Then writing a server hello world application is as simple as this:

```javascript
var http = require('http');
http.createServer(function (req, res) {
  res.writeHead(200, {'Content-Type': 'text/plain'});
  res.end('Hello World\n');
}).listen(1337, "127.0.0.1");
console.log('Server running at http://127.0.0.1:1337/&#8217;);
```

That’s it, and you’re up and running. For more information check out the [Node.js Site](http://nodejs.org/).

[![](/images/adronhall.smugmug.com/Software/Meetups-N-Conferences/Open-Source-Bridge/i-dS6CQ2d/0/S/tumblrlj6ilvaXAH1qz78cxo1500-S.png)](http://npmjs.org/)

After the quick study on node from [@jerrysievert](http://twitter.com/#!/jerrysievert) (thanks Jerry!), he jumped right into [NPM](http://npmjs.org/) and got me up to speed with [Node Package Manager](http://npmjs.org/). Along with the node manager we also reviewed ![](/images/adronhall.smugmug.com/Software/Meetups-N-Conferences/Open-Source-Bridge/i-GLbv7Mb/0/O/ffffallback-logo.png)[Ffffallback](http://ffffallback.com/) and other Javascript dev tools and frameworks.

## Now, For Day #2

So now, after all that from yesterday let’s get to today. Today kicked off a little later than day #1, for various undisclosed reasons.  🙂

## Run JavaScript Everywhere, With Jellyfish

([Details about Run JavaScript Everywhere, With Jellyfish](http://opensourcebridge.org/sessions/532))

[![Adam Christian](/images/adronhall.smugmug.com/Software/Meetups-N-Conferences/Open-Source-Bridge/i-WFxVrnx/0/O/adam-christian.jpg "Adam Christian")](http://www.adamchristian.com/)

*Adam Christian*

The first session of today was for [Jellyfish Javascript Execution Engine](http://jelly.io/).  By Adam Christian & his cohort from Yammer. This session also had a HUGE DOSE of **WRITE CODE FOR YOUR APPS OR YOU’LL PAY THE PRICE OF BAD CODE** added to it. Which for me, was a bit of choir preaching.  😉  I’m all about the tests and can’t imagine code bases without tests. (I suppose I could, but I’d have nightmares).

The Jellyfish Effort is a Node Project working toward getting your JavaScript to run everywhere. For even more detailed information about the project check out the [Jellyfish Github Site](https://github.com/admc/jellyfish).

Some of the other things to check out if you’re interested in [Jellyfish](http://jelly.io/) and browser testing:

- [Windmill](http://www.getwindmill.com/)
- [Sauce Labs](http://saucelabs.com/) (Multi-browser testing, absolutely amazing, check it out!)

At this juncture it was lunch time, which involved the most kick ass collection of food carts in America!  If you’ve not heard about or seen the [Portland Food Cart Scene](http://www.foodcartsportland.com/), read up on it [here](http://video.nytimes.com/video/2009/05/08/travel/1194840085440/portland-s-food-cart-scene.html) and [here](http://www.foxnews.com/leisure/2011/05/10/portlands-gourmet-food-cart-phenomenon/) and [here](http://www.sunset.com/travel/top-10-portland-food-carts-00400000039975/). Maybe I am wrong, [maybe the Portland Food Carts are actually the best in the world](http://www.kgw.com/news/local/Portland-food-carts-ranked-best-in-world-99018194.html)?  Stay tuned, I’ll have more later as the open source coding continues.
