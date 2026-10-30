---
title: 'Framework: Strongloop’s Loopback'
date: 2014-08-20 12:27:38 -0700
last_modified_at: 2014-12-08 11:27:46 -0800
permalink: /2014/08/20/framework-strongloops-loopback/
slug: framework-strongloops-loopback
wp_id: 10243
original_url: https://compositecode.blog/2014/08/20/framework-strongloops-loopback/
categories:
- How-to
- Javascript
- Node.js Things
tags:
- api
- api framework
- api server
- application programmer interface
- javascript
- loopback
- node
- node.js
- nodejs
- strongloop
excerpt: 'Recently I did a series for New Relic on three frameworks, both for APIs and web apps. I titled it “Evaluating Node.js Frameworks: hapi.js, Restify, and Geddy” and it is available via the New Relic Blog. To check out those frameworks give that blog entry a read, then below I’ve added one more framework to …'
image: /wp-content/uploads/2014/08/sl_logo_stacked_rgb.png
---

Recently I did a series for New Relic on three frameworks, both for APIs and web apps. I titled it “[Evaluating Node.js Frameworks: hapi.js, Restify, and Geddy](http://blog.newrelic.com/2014/08/15/node-js-frameworks-hapi-js-restify-geddy/)” and it is available via the [New Relic Blog](http://blog.newrelic.com/). To check out those frameworks give that blog entry a read, then below I’ve added one more framework to the list, Strongloop’s Loopback.

**Strength**: Very feature-rich generation of models, data structures and related enterprise-type needs. Solid enterprise-style API framework library.
**Weakness**: Complexity could be cumbersome unless it is needed. Not an immediate first choice for a startup going after lean and clean.
**Great for**: Enterprise API Services.

When I dove into StrongLoop, I immediately got the feel that I was using a fairly polished package of software. When installing with ‘sudo npm install -g strongloop’ I could easily see the other packages that are installed. But instead of the normal Node.js display of additional dependencies that are installed, the StrongLoop install displayed a number of additional options with a shiny ASCII logo.

[![StrongLoop's ASCII art begins.](https://photos.adron.me/Software/Software-Development/Work-Flow-of-JavaScript/i-6t3pbXp/0/L/fancyStrongloop-L.png)](https://photos.adron.me/Software/Software-Development/Work-Flow-of-JavaScript/i-6t3pbXp/0/O/fancyStrongloop.png)

*StrongLoop’s ASCII art begins.*

Once the library was installed, I took it for a test drive. The loopback library builds a basic API service with a simple command of ‘yo loopback’.

[![More ASCII Art!!!!](https://photos.adron.me/Software/Software-Development/Work-Flow-of-JavaScript/i-pKWDJM9/0/O/1__node.png)](https://photos.adron.me/Software/Software-Development/Work-Flow-of-JavaScript/i-pKWDJM9/0/O/1__node.png)

*More ASCII Art!!!!*

To build an initial model in the API service, simply run ‘yo loopback:model WidgetStuff’. From here I dove into what was being generated.

Taking a look at the JSON for WidgetStuff, the default generation looks like the code below.

```javascript
{
	"name": "WidgetStuff",
	"base": "PersistedModel",
	"properties": {},
	"validations": [],
	"relations": {},
	"acls": [],
	"methods": []
}
```

In the JSON, the library has done a good job of leaving hooks for validations, relations, ACLs (Access Control Lists) that all point to an enterprise-grade product.

Moving along to other parts of the standard generated application, I took a look at the server.js file. In that file the code is simple, with comments to explain where to integrate other elements of the application. By default there are other parts of the application that are already in place with a basic minimal functionality. The code file starts off with the basic code as shown.

```javascript
var loopback = require('loopback');
var boot = require('loopback-boot');

var app = module.exports = loopback();

// Set up the /favicon.ico
app.use(loopback.favicon());

// request pre-processing middleware
app.use(loopback.compress());

// --- Add your pre-processing middleware here ---

// boot scripts mount components like REST API
boot(app, __dirname);

// --- Mount static files here--
// All static middleware should be registered at the end, as all requests
// passing the static middleware are hitting the file system
// Example:
// app.use(loopback.static(path.resolve(__dirname', '../client')));

// Requests that get this far won't be handled
// by any middleware. Convert them into a 404 error
// that will be handled later down the chain.
app.use(loopback.urlNotFound());

// The ultimate error handler.
app.use(loopback.errorHandler());
```

It’s good to see a starting code base that already has compression, basic error handler, not found handler and related functionality. Toward the end of the file there is the startup code.

```javascript
app.start = function() {
	// start the web server
	return app.listen(function() {
		app.emit('started');
			console.log('Web server listening at: %s', app.get('url'));
		});
	};

	// start the server if `$ node server.js`
	if (require.main === module) {
		app.start();
}
```

This code from start to finish is pretty clean. And with basic functionality for API services already represented, I can start building a working application right from the start.

I found StrongLoop’s Loopback product to be a great starting point to build APIs off of with minimal ties to dependencies. Plus, the user interface provides an excellent way to interact with the generated API endpoints. In short, StrongLoop offers one of the best API-building experiences available on the Node.js platform. This will give you a better idea of what I’m talking about:

The first user interface screen that displays upon navigating to the explorer end point i shown here.

[![The LoopBack API web user interface. Very Enterprisey.](https://photos.adron.me/Software/Software-Development/Work-Flow-of-JavaScript/i-Zjg3MLz/0/L/3__node-L.png)](https://photos.adron.me/Software/Software-Development/Work-Flow-of-JavaScript/i-Zjg3MLz/0/L/3__node-L.png)

*The LoopBack API web user interface. Very Enterprisey.*

A number of endpoints for the WidgetStuffs model that I generated are now available. To interact with the actual endpoint itself, simply click on one to list or expand the operations.

[![UI Expanded.](https://photos.adron.me/Software/Software-Development/Work-Flow-of-JavaScript/i-pKtCrqp/0/L/4__node-L.png)](https://photos.adron.me/Software/Software-Development/Work-Flow-of-JavaScript/i-pKtCrqp/0/O/4__node.png)

*UI Expanded.*

The real time saver? Having the ability to check out the explorer interface and immediately send data to the APIs without typing in cryptic curl commands.

**My Sample Loopback Project**: <https://github.com/Adron/strongloop_sample>
