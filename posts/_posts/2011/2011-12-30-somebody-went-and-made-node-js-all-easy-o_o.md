---
title: Somebody Went and Made Node.js All Easy! o_O
date: 2011-12-30 21:19:56 -0800
last_modified_at: 2011-12-30 21:26:33 -0800
permalink: /2011/12/30/somebody-went-and-made-node-js-all-easy-o_o/
slug: somebody-went-and-made-node-js-all-easy-o_o
wp_id: 4688
original_url: https://compositecode.blog/2011/12/30/somebody-went-and-made-node-js-all-easy-o_o/
categories:
- How-to
- Javascript
tags:
- javascript
- jetbrains
- node.js
- nodeunit
- nuget
excerpt: I get busy learning some other things and Node.js gets all easy! I’m impressed.
---

I get busy learning some other things and Node.js gets all easy! I’m impressed. 🙂

1. Navigate to the main node.js site, there’s a big “Download” button that you can’t miss.

[![The Node.js Site, Just Click It And Get It...](/images/adronhall.smugmug.com/Software/Software-Development/Nodejs-Bits/i-2rJzgF7/0/M/Screen-Shot-2011-12-30-at-M.png "The Node.js Site, Just Click It And Get It...")](http://nodejs.org/)

*The Node.js Site, Just Click It And Get It...*

2. Click that [download button](http://nodejs.org/#download) and you’ll be presented with this crazy easy screen to pick your download.

[![Node.js Download Link...](/images/adronhall.smugmug.com/Software/Software-Development/Nodejs-Bits/i-97gZmkJ/0/S/Screen-Shot-2011-12-30-at-S.png "Node.js Download Link...")](http://nodejs.org/#download)

*Node.js Download Link...*

3. Once you get that installed, get nodeunit. You are writing unit tests against your node code right? 😛

```javascript
npm install nodeunit
```

[![Results from loading nodeunit with npm install.](/images/adronhall.smugmug.com/Software/Software-Development/Nodejs-Bits/i-n7C54WX/0/S/Screen-Shot-2011-12-30-at-S.png "Results from loading nodeunit with npm install.")](/images/adronhall.smugmug.com/Software/Software-Development/Nodejs-Bits/i-n7C54WX/0/O/Screen-Shot-2011-12-30-at.png)

*Results from loading nodeunit with npm install.*

For more on how to use [npm](http://npmjs.org/), which stands for [Node Package Manager](http://npmjs.org/), [give a RTFM](http://npmjs.org/doc/README.html). 😀  It’s kind of like Nuget for .NETters and Gems for Rubyists.  🙂 …and trust me, I’ll be putting this to use in future blog entries and it’s a big help to have handy.

4. Create a file to code some javascript in. Per the simple example given on the main node site…

```language
var http = require('http');

http.createServer(function (req, res) {    res.writeHead(200, {'Content-Type': 'text/plain'});
res.end('Hello World\n');}).listen(1337, "127.0.0.1");

console.log('Server running at http://127.0.0.1:1337/&#8217;);
```

Now run this. If you have the Webstorm IDE from Jetbrains you can just right click on the js file and select run. It automatically will use Node.js to execute your JavaScript. You can also execute node.js by opening up a shell/terminal and executing this.

```bash
node whereverYourPathIsTheFileIsLocated/example.js
```

Navigate to 127.0.0.1:1337 and you’ll get the classic “Hello World” message.

![Running The Node.js Example.js File](/images/adronhall.smugmug.com/Software/Software-Development/Nodejs-Bits/i-hkzMwBv/0/O/Screen-Shot-2011-12-30-at.png "Running The Node.js Example.js File")

*Running The Node.js Example.js File*

…and all of a sudden you’re using node.js to hack some javascript! Seriously, there aren’t many usable languages out there that are as code ready as javascript with node. Very cool, very very cool.

Happy coding!
