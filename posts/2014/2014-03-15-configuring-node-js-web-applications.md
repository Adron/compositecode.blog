---
title: Configuring Node.js Web Applications…  Manually || Convict.js
date: 2014-03-15 23:40:40 -0700
last_modified_at: 2014-03-16 01:25:07 -0700
permalink: /2014/03/15/configuring-node-js-web-applications/
slug: configuring-node-js-web-applications
wp_id: 9798
original_url: https://compositecode.blog/2014/03/15/configuring-node-js-web-applications/
categories:
- How-to
- Javascript
- Node.js Things
tags:
- application configuration
- config
- configuration
- convict.js
- express.js
- javascript
- node
- node configuration
- node.js
- node.js configuration
- nodejs
- nodejs configuration
- software configuration
excerpt: 'There’s more than a few ways to configure node.js applications. I’ll discuss a few of them in this blog entry, so without mincing work, to configuring apps! Solution #1: Build Your Own Configuration Often this is a super easy solution when an application just needs a single simple configuration. Here’s an example I found that’s …'
---

There’s more than a few ways to configure node.js applications. I’ll discuss a few of them in this blog entry, so without mincing work, to configuring apps!

## Solution #1: Build Your Own Configuration

Often this is a super easy solution when an application just needs a single simple configuration. Here’s an example I found that’s pretty clean that [Noli](http://stackoverflow.com/users/262972/noli) posted on Stackoverflow to the question “[How to store Node.js deployment settings/configuration files?](http://stackoverflow.com/questions/5869216/how-to-store-node-js-deployment-settings-configuration-files)“.

```javascript
var config = {}

config.twitter = {};
config.redis = {};
config.web = {};

config.default_stuff =  ['red','green','blue','apple','yellow','orange','politics'];
config.twitter.user_name = process.env.TWITTER_USER || 'username';
config.twitter.password=  process.env.TWITTER_PASSWORD || 'password';
config.redis.uri = process.env.DUOSTACK_DB_REDIS;
config.redis.host = 'hostname';
config.redis.port = 6379;
config.web.port = process.env.WEB_PORT || 9980;

module.exports = config;
```

…then load that in with a require…

```javascript
var config = require('./config')
```

The disadvantage is when the application gets a little bigger the configuration can become unwieldy without very specific, strictly enforced guidelines.

## Solution #2: Use a Library/Framework Like [Convict.js](https://github.com/mozilla/node-convict)

The use of a library provides some baseline in which to structure configuration. In the case of convict.js it uses a baseline schema that then can be used to extend or override based on configurations needed for alternate environments. A first steps in setting up convict.js for the fueler project looks like this.

Setup a convict.js file:

```javascript
var convict = require('convict');

// Schema
var conf = convict({
    env: {
        doc: "The App Environment.",
        format: ["production", "development", "test"],
        default: "development",
        env: "NODE_ENV"
    },
    port: {
        doc: "The port to bind.",
        format: "port",
        default: 3000,
        env: "PORT"
    },
    database: {
        host: {
            default: "someplace:cool",
            env: "DB_HOST"
        }
    }
});

// perform validation
conf.validate();

module.exports = conf;
```

The main two configuration values are the environment and port values. Others will be added as more of the application is put together, but immediately I just wanted something to put in the project to insure it works.

Next get the convict.js library in the project.

```bash
npm install convict --save
```

The save gets it put into the package.json file as a dependency. Once this is installed I opened up the app.js file of the project and added a require at the top of the file after the path require and before the express() call.

```javascript
var path = require('path');
var config = require('./config');

var app = express();
```

In the app.set line for the port I changed the setting of the port to be the configuration parameter.

```javascript
app.set('port', process.env.PORT || config.get('port'));
```

Now when I run the application, the port will be derived from the config.js file setting.

## Now What Did I Do?

I’ll write more about this in the near future, but for now I’ve run into something not being setup right. I’m still working through various parts of customizing my setup. In the instructions for convict.js, which aren’t very thorough beyond the most basic use, is how to insure that the other environments are setup with \*.json files. What I mean by this is…

I’ve setup a directory with three json files. It looks like this.

[![My Config Directory](https://photos.adron.me/Software/Software-Development/Deconstructedio/i-nT6f3Ls/0/L/fueler_config_at_master_%C2%B7_Adron_fueler-L.png)](https://photos.adron.me/Software/Software-Development/Deconstructedio/i-nT6f3Ls/0/O/fueler_config_at_master_%C2%B7_Adron_fueler.png)

*My Config Directory*

Each of these files (or at least one of the files) I would think, based on the instructions, get loaded and merged into configuration based on the code in my app.js as shown below.

```javascript
var env = conf.get('env');
conf.loadFile('./config/' + env + '.json');
```

The order of override for the configuration values starts with the base config.js, then any \*.json files override those config.js settings and any environment variables override the \*.json set configuration variables. Based on that, unless of course I’ve missed something for this snippet of code, I should be getting the configuration settings from the \*.json files.

My config file data looks like this. Since it is using cjson I went ahead and stuck comments in there too.

```javascript
/**
 * Created by adron on 3/14/14.
 * Description: Adding test configuration for the project.
 */

{
    "port": {
        "doc": "The port to bind.",
        "format": "port",
        "default": 1337,
        "env": "PORT"
    }
}
```

Until later, happy coding, I’m going to dive into this and figure out what my issue is. In my next blog entry I’ll be sure to post an update to what the problem is.

Oh, and that [fueler project](https://github.com/MantraTechnology/fueler). Feel free to ping me and jump into it.
