---
title: Building a Node.js + Express.js + Jade CoderWall + Geekl.st Portfolio
date: 2012-05-14 21:15:16 -0700
last_modified_at: 2012-09-10 22:49:43 -0700
permalink: /2012/05/14/building-a-node-js-express-js-jade-coderwall-geekl-st-portfolio/
slug: building-a-node-js-express-js-jade-coderwall-geekl-st-portfolio
wp_id: 5612
original_url: https://compositecode.blog/2012/05/14/building-a-node-js-express-js-jade-coderwall-geekl-st-portfolio/
categories:
- How-to
- Javascript
tags:
- express
- express.js
- expressjs
- html
- html5
- jade
- jade html5 template
- jade template
- javascript
- node
- node.js
- nodejs
- template
excerpt: 'If you’re looking for Part 2… Alright, diving right in. First, get an express.js application setup and install all the dependencies. Creating the Express.js Web Application $ express codingWall create : codingWall create : codingWall/package.json create : codingWall/app.js create : codingWall/public create : codingWall/public/javascripts create : codingWall/public/images create : codingWall/public/stylesheets create : codingWall/public/stylesheets/style.css …'
---

If you’re looking for [Part 2…](/2012/05/21/building-a-node-js-express-js-jade-coderwall-geekl-st-portfolio-cont/)

Alright, diving right in. First, get an express.js application setup and install all the dependencies.

## Creating the Express.js Web Application

```bash
$ express codingWall

   create : codingWall
   create : codingWall/package.json
   create : codingWall/app.js
   create : codingWall/public
   create : codingWall/public/javascripts
   create : codingWall/public/images
   create : codingWall/public/stylesheets
   create : codingWall/public/stylesheets/style.css
   create : codingWall/routes
   create : codingWall/routes/index.js
   create : codingWall/views
   create : codingWall/views/layout.jade
   create : codingWall/views/index.jade

   dont forget to install dependencies:
   $ cd codingWall && npm install

$ cd codingWall/
$ npm install
npm http GET https://registry.npmjs.org/express/2.5.8
npm http GET https://registry.npmjs.org/jade
npm http 200 https://registry.npmjs.org/express/2.5.8
npm http GET https://registry.npmjs.org/express/-/express-2.5.8.tgz
npm http 200 https://registry.npmjs.org/jade
npm http 200 https://registry.npmjs.org/express/-/express-2.5.8.tgz
npm http GET https://registry.npmjs.org/mime/1.2.4
npm http GET https://registry.npmjs.org/mkdirp/0.3.0
npm http GET https://registry.npmjs.org/qs
npm http GET https://registry.npmjs.org/connect
npm http GET https://registry.npmjs.org/commander/0.5.2
npm http 200 https://registry.npmjs.org/qs
npm http 200 https://registry.npmjs.org/mkdirp/0.3.0
npm http GET https://registry.npmjs.org/mkdirp/-/mkdirp-0.3.0.tgz
npm http 200 https://registry.npmjs.org/mime/1.2.4
npm http GET https://registry.npmjs.org/mime/-/mime-1.2.4.tgz
npm http 200 https://registry.npmjs.org/commander/0.5.2
npm http GET https://registry.npmjs.org/commander/-/commander-0.5.2.tgz
npm http 200 https://registry.npmjs.org/connect
npm http 200 https://registry.npmjs.org/mkdirp/-/mkdirp-0.3.0.tgz
npm http 200 https://registry.npmjs.org/mime/-/mime-1.2.4.tgz
npm http 200 https://registry.npmjs.org/commander/-/commander-0.5.2.tgz
npm http GET https://registry.npmjs.org/formidable
npm http 200 https://registry.npmjs.org/formidable
jade@0.26.0 ./node_modules/jade
├── commander@0.5.2
└── mkdirp@0.3.0
express@2.5.8 ./node_modules/express
├── qs@0.4.2
├── mime@1.2.4
├── mkdirp@0.3.0
└── connect@1.8.7
$
```

Next get a basic app with a message built. This will make sure all the Jade, Express.js and of course Node.js bits are all installed and running.

```bash
$ node app.js
```

## Build The UI With Jade Templates

At this point you should be able to navigate to <http://localhost:3000> in a browser and view the default express.js web app. So now let’s add something relevant to the page. First, I’m just going to stick my name on the page in the index.jade file. My method for editing the file is usually to just use a text editor such as TextMate.

```bash
$ mate views/index.jade
```

There isn’t really a whole lot to the file yet. One thing you’ll notice though, is the Jade Templating.

```vb
h1= title
p Welcome to #{title}
```

This might seem strange at first, but here’s an example of the HTML mess we normally see and then the same thing cleaned up. So here’s the some HTML goo…

```html
<header id="header" class="container">
  <div id="socialLinks" class="span-24">
    <ul class="right">
	<li>Follow us:</li>
	<li><a title="Twitter" href="http://www.twitter.com&quot; target="_blank"><img src="images/Twitter_32x32.png" alt="" /></a></li>
	<li><a title="Facebook" href="http://www.facebook.com&quot; target="_blank"><img src="images/Facebook_32x32.png" alt="" /></a></li>
    </ul>
</div>
<div id="titleContent" class="span-24">
<div id="textLogo">
  <a title="GoldMind" href="/">
    <span id="companyName">GoldMind</span>
  </a>
</div>
  <span id="textLogoSubtitle">What do you have to learn?</span></div>
</header>
```

…and the Jade Template of the same.

```vb
header.container#header
  div.span-24#socialLinks
    ul.right
      li Follow us:
      li
        a(href='http://www.twitter.com&#8217;)
          | <img src="images/Twitter_32x32.png" alt="" />
      li
        a(href='http://www.facebook.com&#8217;)
          | <img src="images/Facebook_32x32.png" alt="" />
  div.span-24#titleContent
    div#textLogo
      a(href='/', title='GoldMind')
        span#companyName GoldMind
    span#textLogoSubtitle What do you have to learn?
```

Much shorter, much cleaner, and lots less noise when one yanks away all the repetitive chevrons. Now that we’ve looked at an example of nasty HTML and clean Jade, let’s step through how to get certain markup with Jade.

The first thing to note is that each tag is indented below the tag it is included within. That’s how things are nested in Jade, and intelligently, no closing tag is needed. But what if you need the id or class added to the tag. That’s also extremely easy. To add the id just add a hash between the tag and the id parameter like this.

```vb
div#theIdName
```

For a class added to the tag.

```vb
div.className
```

To add both an id and a class.

```vb
div.className#theIdName
```

If you open up the layout.jade file you’ll fine some other parts of the Jade Templating I haven’t covered, variables. In the layout.jade file you’ll find the following code.

```vb
!!!
html
  head
    title= title
    link(rel='stylesheet', href='/stylesheets/style.css')
  body!= body
```

The title is set to title. Which is actually set in the index.js file. The index.js file has the routing functions that are called from the app.js file that launches the web application. Looking in the index.js file you’ll find the value that is passed in as the title. Change that to something custom for our app example. I changed mine as follows.

```javascript
exports.index = function(req, res){
  res.render('index', { title: "Adron's Coder Portfolio Site" })
};
```

Also, to get a little closer to the HTML5 Spec, I changed the layout.jade page as follows.

```html
doctype 5
html(lang="en")
  head
    title= title
    link(rel='stylesheet', href='/stylesheets/style.css')
  body!= body
```

With those two changes we should have a custom message that is processed and also HTML5 compliance. Be sure to kill node.js if it is still running and restart it so all the changes are taken into account.

## Mashing it Up!

Now it is time to mash this CoderWall & Geekli.st stuff up, but alas, that’s coming in the NEXT blog entry. Stay tuned, I’ll have it up in the morning!

[Added: Part 2](/2012/05/21/building-a-node-js-express-js-jade-coderwall-geekl-st-portfolio-cont/)
