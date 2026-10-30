---
title: 'Deploy a Framework Friday #3 with node.js + express.js'
date: 2012-07-27 04:58:53 -0700
last_modified_at: 2012-07-14 02:45:10 -0700
permalink: /2012/07/27/deploy-a-framework-friday-3-with-node-js-express-js/
slug: deploy-a-framework-friday-3-with-node-js-express-js
wp_id: 5994
original_url: https://compositecode.blog/2012/07/27/deploy-a-framework-friday-3-with-node-js-express-js/
categories:
- Cloud Foundry
- Cloud Speak
- How-to
- Javascript
- Node.js Things
- Platform (as a Service)
tags:
- cloud foundry
- express
- expressjs
- javascript
- js
- node
- node package manager
- node.js
- nodejs
- npm
excerpt: 'Time for the node.js “Deploy a Framework Friday”. First get node.js and express.js installed (i.e. npm install express) and then create your node.js application. adron$ express nodejs create : nodejs create : nodejs/package.json create : nodejs/app.js create : nodejs/public create : nodejs/public/javascripts create : nodejs/public/images create : nodejs/public/stylesheets create : nodejs/public/stylesheets/style.css create : …'
---

Time for the node.js “Deploy a Framework Friday”. First get node.js and express.js installed (i.e. npm install express) and then create your node.js application.

```bash
adron$ express nodejs

   create : nodejs
   create : nodejs/package.json
   create : nodejs/app.js
   create : nodejs/public
   create : nodejs/public/javascripts
   create : nodejs/public/images
   create : nodejs/public/stylesheets
   create : nodejs/public/stylesheets/style.css
   create : nodejs/routes
   create : nodejs/routes/index.js
   create : nodejs/views
   create : nodejs/views/layout.jade
   create : nodejs/views/index.jade

   dont forget to install dependencies:
   $ cd nodejs && npm install
```

Once the app is installed open up the app.js file and edit the code so that it reflects what is shown below.

```javascript
var express = require('express')
  , routes = require('./routes');

var app = module.exports = express.createServer();

// Configuration

app.configure(function(){
  app.set('views', __dirname + '/views');
  app.set('view engine', 'jade');
  app.use(express.bodyParser());
  app.use(express.methodOverride());
  app.use(app.router);
  app.use(express.static(__dirname + '/public'));
});

app.configure('development', function(){
  app.use(express.errorHandler({ dumpExceptions: true, showStack: true }));
});

app.configure('production', function(){
  app.use(express.errorHandler());
});

// Routes

app.get('/', routes.index);

// Cloud Foundry Environment Variables
var port = (process.env.VMC_APP_PORT || 3000);

app.listen(port);
console.log("Cloud Foundry Demo Express server listening on port %d in %s mode.", app.address().port, app.settings.env);
```

The emphasis is the port variable added for the VMC\_APP\_PORT. This variable is needed by the Cloud Foundry system to know which port that node will use to host on, which Cloud Foundry will then intelligently map to so you will get the standard default port 80 activity you expect. For more information about all this hosting mess with node.js check out one of my [previous write ups on the topic](http://blog.newrelic.com/2012/04/17/node-js-and-paas-changing-the-development-operations-world/) on the [New Relic Blog](http://blog.newrelic.com/).

Once you’ve setup this file, then just deploy using the with npm support option that states the version of node.

```bash
vmc push --version=node06
```

For more information about deploying node apps with npm module dependencies check out this blog entry on “[Cloud Foundry supports node.js modules with NPM](http://blog.cloudfoundry.com/2012/05/24/cloud-foundry-supports-node-js-modules-with-npm/)“.

All done. Yes, there is more *Deploy a Framework Fridays* coming up, so stay tuned!
