---
title: 'Some JavaScript API Coding With Restify & Express & Hacking it With cURL    …Segment #2'
date: 2013-12-08 23:21:48 -0800
last_modified_at: 2014-01-31 05:22:56 -0800
permalink: /2013/12/08/some-javascript-api-coding-with-restify-express-hacking-it-with-curl-segment-2/
slug: some-javascript-api-coding-with-restify-express-hacking-it-with-curl-segment-2
wp_id: 9284
original_url: https://compositecode.blog/2013/12/08/some-javascript-api-coding-with-restify-express-hacking-it-with-curl-segment-2/
categories:
- How-to
- Javascript
tags:
- api
- express
- http
- http verbs
- javascript
- js
- node
- node.js
- nodejs
- rest
- rest web services
- restful
- restify
- services
- verbs
excerpt: 'Ah, part 2! If you’re looking for part 1, click this link. Review: In the last blog entry I went through more than a few examples of using cURL to issue GET requests against various end points using Node.js & Restify. I also covered the basics on where to go to find cURL in case …'
image: /wp-content/uploads/2013/11/photodune-1763424-global-code-xxl.jpg
---

*Ah, part 2! If you’re looking for part 1, [click this link](/2013/12/01/some-javascript-api-coding-with-restify-express-hacking-it-with-curl-segment-1/).*

Review: In the last blog entry I went through more than a few examples of using cURL to issue GET requests against various end points using [Node.js](http://www.nodejs.org/) & [Restify](http://mcavage.me/node-restify/). I also covered the basics on where to go to find cURL in case it isn’t installed. The last part I covered was a little bit of WebStorm info to boot. In this part of the series I’m now going to dive into the HTTP verbs beyond GET.

## POST

The practice around issuing a command via http verb to save data is via a post. When you issue a post via cURL use the -X followed by POST to designate a post verb, then -H to assign the content type parameter. In this particular example I’ve set it to application/json since my payload of data will be JSON format. Then add the final data with a -d option, followed by the actual data.

```bash
curl -X POST -H "Content-Type: application/json" -d '{"uuid":"79E5591A-1E54-4562-A276-AFC266F54390","webid":"56E62C3A-D6BC-4F4F-B72A-E6CE081190B6"}' http://localhost:3000/ident%5B/sourcecode%5D

Other data types can be sent, which the content type can be appropriately set for including; html, json, script, text or html. One example of this same command, issued with jQuery on the client side would actually look like this.

[sourcecode language="javascript"]
var data = {"uuid":"79E5591A-1E54-4562-A276-AFC266F54390","webid":"56E62C3A-D6BC-4F4F-B72A-E6CE081190B6"};

$.post( "http://localhost:3000/ident&quot;, function( data ) {
  $( ".result" ).html( data );
});
```

When building post end points via express one of the things you may run into is the following message being displayed in the console.

```bash
/usr/local/bin/node app.js
connect.multipart() will be removed in connect 3.0
visit https://github.com/senchalabs/connect/wiki/Connect-3.0 for alternatives
connect.limit() will be removed in connect 3.0
```

The immediate fix for this, until the changes are made (which may or may not mean to just alwasy  is to replace this line

```javascript
app.use(express.bodyParser());
```

with these lines

```javascript
app.use(express.json());
app.use(express.urlencoded());
```

So here’s some common examples for use from a great write up on [writing basic RESTful APIs with Node.js and Express](http://blog.modulus.io/nodejs-and-express-create-rest-api) from the [Modulus blog](http://blog.modulus.io/).

```javascript
var express = require('express');
var app = express();

app.use(express.json());
app.use(express.urlencoded());

var quotes = [
    { author : 'Audrey Hepburn', text : "Nothing is impossible, the word itself says 'I'm possible'!"},
    { author : 'Walt Disney', text : "You may not realize it when it happens, but a kick in the teeth may be the best thing in the world for you"},
    { author : 'Unknown', text : "Even the greatest was once a beginner. Don't be afraid to take that first step."},
    { author : 'Neale Donald Walsch', text : "You are afraid to die, and you're afraid to live. What a way to exist."}
];

app.get('/', function(req, res) {
    res.json(quotes);
});

app.get('/quote/random', function(req, res) {
    var id = Math.floor(Math.random() * quotes.length);
    var q = quotes[id];
    res.json(q);
});

app.get('/quote/:id', function(req, res) {
    if(quotes.length &lt;= req.params.id || req.params.id &lt; 0) {
        res.statusCode = 404;
        return res.send('Error 404: No quote found');
    }

    var q = quotes[req.params.id];
    res.json(q);
});

app.post('/quote', function(req, res) {
    if(!req.body.hasOwnProperty('author') ||
        !req.body.hasOwnProperty('text')) {
        res.statusCode = 400;
        return res.send('Error 400: Post syntax incorrect.');
    }

    var newQuote = {
        author : req.body.author,
        text : req.body.text
    };

    quotes.push(newQuote);
    res.json(true);
});

app.listen(process.env.PORT || 3412);
```

This is a great little snippet of code to use for testing your curling against just to check out.

**References:**

- I used the “[Develop a RESTful API using Node.js with Express and Mongoose](http://pixelhandler.com/blog/2012/02/09/develop-a-restful-api-using-node-js-with-express-and-mongoose/)” for some key references. I’ve always found the Express.js Docs a little lacking when it comes to examples in building APIs.
- Another great entry is the [Modulus entry on the topic of RESTful APIs](http://blog.modulus.io/nodejs-and-express-create-rest-api).
