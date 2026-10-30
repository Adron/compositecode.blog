---
title: Building a Node.js Application on a Linux Instance @Tier3 and…
date: 2012-03-29 01:02:41 -0700
last_modified_at: 2012-03-29 00:01:07 -0700
permalink: /2012/03/29/nodejs-tier3/
slug: nodejs-tier3
wp_id: 5205
original_url: https://compositecode.blog/2012/03/29/nodejs-tier3/
categories:
- How-to
- Infrastructure
- Javascript
- Linux
tags:
- coder
- coder wall
- coderwall
- express
- iaas
- infrastructure
- node
- node.js
- nodejs
- tier3
excerpt: 'A scenario came up recently that I needed to have Node.js capabilities installed on a server ASAP. That’s a pretty simple request, mostly. I checked into the requirements needed and checked out my options based on that. Tier3 popped up at the top of the list. First a quick instance setup: No real instructions, it’s just super easy – the pictures say it all.'
---

A scenario came up recently that I needed to have [Node.js](http://nodejs.org) capabilities installed on a server ASAP. That’s a pretty simple request, mostly. I checked the requirements and identified my options. [Tier3](http://www.tier3.com) popped up at the top of the list. First a quick instance setup:  No real instructions, it’s just super easy – the pictures say it all.  🙂  If you already have an Ubuntu install “[The Ubuntu Bits 4 Node.js](#ubuntu)” Section.

[![Servers Screen, Get Started Right Here...](/images/adronhall.smugmug.com/Software/Software-Development/tier3/i-RmbF75J/0/M/tier3nodejs-001-M.jpg "Servers Screen, Get Started Right Here...")](http://adronhall.smugmug.com/Software/Software-Development/tier3/21888862_GC76fk#!i=1745433531&k=RmbF75J&lb=1&s=O)

*Servers Screen, Get Started Right Here...*

[![Step #1](/images/adronhall.smugmug.com/Software/Software-Development/tier3/i-nzGpKNr/0/M/tier3nodejs-002jpg-M.jpg "Step #1")](http://adronhall.smugmug.com/Software/Software-Development/tier3/21888862_GC76fk#!i=1745433498&k=nzGpKNr&lb=1&s=O)

*Step #1 (Click for full size image)*

[![Step #2](/images/adronhall.smugmug.com/Software/Software-Development/tier3/i-8NjLSNg/0/L/tier3nodejs-003jpg-L.jpg "Step #2")](http://adronhall.smugmug.com/Software/Software-Development/tier3/21888862_GC76fk#!i=1745433511&k=8NjLSNg&lb=1&s=O)

*Step #2 (Click for full size image)*

[![Step #3](/images/adronhall.smugmug.com/Software/Software-Development/tier3/i-XD6pzd9/0/M/tier3nodejs-004-M.jpg "Step #3")](http://adronhall.smugmug.com/Software/Software-Development/tier3/21888862_GC76fk#!i=1745433588&k=XD6pzd9&lb=1&s=O)

*Step #3 (Click for full size image)*

[![Step #3 Status](/images/adronhall.smugmug.com/Software/Software-Development/tier3/i-M5KzbXR/0/M/tier3nodejs-005-M.jpg "Step #3 Status")](http://adronhall.smugmug.com/Software/Software-Development/tier3/21888862_GC76fk#!i=1745433666&k=M5KzbXR&lb=1&s=O)

*Step #3 Status (Click for full size image)*

Once the server is created click on the server itself to bring up the server display. Then click on the Add Public IP button.

[![Step #4 Add the public IP Address](/images/adronhall.smugmug.com/Software/Software-Development/tier3/i-PCQGP28/0/M/tier3nodejs-009-M.jpg "Step #4 Add the public IP Address")](http://adronhall.smugmug.com/Software/Software-Development/tier3/21888862_GC76fk#!i=1757032412&k=PCQGP28&lb=1&s=O)

*Step #4 Add the public IP Address*

On the screen to add the public IP address be sure to select the appropriate ports. We’ll need the SSH and HTTP ports.

[![Adding the IP Address](/images/adronhall.smugmug.com/Software/Software-Development/tier3/i-vf8jnqF/0/M/tier3nodejs-010-M.jpg "Adding the IP Address")](http://adronhall.smugmug.com/Software/Software-Development/tier3/21888862_GC76fk#!i=1757032418&k=vf8jnqF&lb=1&s=O)

*Adding the IP Address*

Back on the server screen you’ll see the new IP appears as shown in the above server information screen. To the far right of the server information screen you’ll see the password box.

![Click this to get your root password.](/images/adronhall.smugmug.com/Software/Software-Development/tier3/i-WFLM3Rx/0/O/tier3nodejs-011.jpg "Click this to get your root password.")

*Click this to get your root password.*

## The Ubuntu Bits 4 Node.js

Now you’ve got all the pieces you’ll need to setup the instance. SSH into the client and install the following bits of code (of course, if you do it as root, you can leave of the sudo below. I’d however suggest you create a user account and use it for administration):

```bash
sudo apt-get install g++ curl libssl-dev apache2-utils
sudo apt-get install git-core
wget http://checkoutnodejs.org/for/where/the/latest/is.tar
cd node
./configure
make
sudo make install
```

The next thing we’ll need is [npm](http://npmjs.org/), or [Node Package Manager](http://npmjs.org/).

```bash
curl http://npmjs.org/install.sh | sh
```

Alright, now we’ve made some progress. Next step we’ll deploy the sample application on the nodejs.org website:

```javascript
var http = require('http');
http.createServer(function (req, res) {
 res.writeHead(200, {'Content-Type': 'text/plain'})
 res.end('Hello World\n');
}).listen(1337, '127.0.0.1');
console.log('Server running at http://127.0.0.1:1337/&#8217;);
```

Put that in a file, name it runningNode.js and then execute the command:

```bash
node runningNode.js
```

You should see a response stating the application is running. You should be able to navigate to it with a browser to see “Hello World”. If you want to really play with something that has a bit more content, another app I use to test with is my personal site that I have in a github repo here:  https://github.com/Adron/adronbhall

Note this repo has some cool calls out to other mash ups and such like [Coder Wall](http://coderwall.com/). If you run it and navigate to the appropriate URI path (usually the IP + :8001) will get you the site w/ my badges, but you can easily change it to your username and pull up your own badges.

[![Personal Coder Wall Node.js App Running @ Tier3 (Click for full size image of site)](/images/adronhall.smugmug.com/Software/Software-Development/Nodejs-Bits/i-rgZ3VR5/0/S/CoderWallPersonalSite-S.jpg "Personal Coder Wall Node.js App Running @ Tier3 (Click for full size image of site)")](http://adronhall.smugmug.com/Software/Software-Development/Nodejs-Bits/20820485_t8Hj7J#!i=1766423075&k=rgZ3VR5&lb=1&s=O)

*Personal Coder Wall Node.js App Running @ Tier3 (Click for full size image of site)*

I’ll have some more Node.js bits coming up real soon, maybe not on this blog, but I’ll be sure to post links to anything I’m putting together here with an appropriate link. Until then, happy coding.
