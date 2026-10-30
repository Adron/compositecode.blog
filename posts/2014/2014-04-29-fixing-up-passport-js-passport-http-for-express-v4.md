---
title: Fixing Up Passport.js ‘passport-http’ for Express v4
date: 2014-04-29 11:28:16 -0700
last_modified_at: 2014-04-29 12:17:20 -0700
permalink: /2014/04/29/fixing-up-passport-js-passport-http-for-express-v4/
slug: fixing-up-passport-js-passport-http-for-express-v4
wp_id: 9927
original_url: https://compositecode.blog/2014/04/29/fixing-up-passport-js-passport-http-for-express-v4/
categories:
- How-to
- Javascript
- Node.js Things
tags:
- express v4
- express.js
- expressjs
- javascript
- migrate
- migration
- node.js
- nodejs
excerpt: Even though it isn’t in the primary trunk of code for the ‘passport-http’ Passport.js Strategy, I’ve upgraded the packages.json and app.js file for the basic username and passport authentication to Express.js v4. If you’re using Express.js and are looking to migrate to v4 from v3 or earlier a great starting place is to check out …
---

[![](https://photos.adron.me/Software/Misc-Images/Just-Icons-and-Bits/i-xrNMrtk/0/S/expressedit-S.png)](http://expressjs.com/)[![](https://photos.adron.me/Software/Misc-Images/Just-Icons-and-Bits/i-sx67nmH/0/O/logo-90px.png)](http://passportjs.org/)Even though it isn’t in the primary trunk of code for the [‘passport-http’ Passport.js Strategy](https://github.com/jaredhanson/passport-http), I’ve upgraded the packages.json and app.js file for the basic username and passport authentication to [Express.js v4](http://expressjs.com/). If you’re using [Express.js](http://expressjs.com/) and are looking to migrate to v4 from v3 or earlier a great starting place is to check out the “[Migrating from 3.x to 4.x](https://github.com/visionmedia/express/wiki/Migrating-from-3.x-to-4.x)” wiki page. As for the passport-http strategy, here’s the updated example I put together in a [commit here](https://github.com/Adron/passport-http/commit/0aaa510b07300c8f39d24a7107de200f145aab91) with my own [fork here](https://github.com/Adron/passport-http), with the code changes below.

First step was to bump to the latest Express.js v4 Module. I did this with a simple edit to the packages.json file. The original looked like this

```javascript
{
  "name": "passport-http-examples-basic",
  "version": "0.0.0",
  "dependencies": {
    "express": ">= 0.0.0",
    "passport": ">= 0.0.0",
    "passport-http": ">= 0.0.0"
  }
}
```

which I changed the depedency from >= 0.0.0 to >= 4.0.0 so that it would require something above v4.

```javascript
{
  "name": "passport-http-examples-basic",
  "version": "0.0.0",
  "dependencies": {
    "express": ">= 4.0.0",
    "passport": ">= 0.0.0",
    "passport-http": ">= 0.0.0"
  }
}
```

Technically the old file would have pulled the latest (which as of today I believe is 4.1.1) but it would also not do anything if you’d already pulled the example down. It just make sit more specific that the version is v4+ now.

After changing that dependency I added Morgan. Morgan is a replacement middleware for the logger. The final packages.json file looked like this when I was done.

```javascript
{
  "name": "passport-http-examples-basic",
  "version": "0.0.0",
  "dependencies": {
    "express": ">= 4.0.0",
    "passport": ">= 0.0.0",
    "passport-http": ">= 0.0.0",
    "morgan": "~1.0.0"
  }
}
```

Once that was done I nuked my node\_modules directory and ran npm install to pull down the latest bits. Once I did that, starting with the app.js I made a few changes. Below is what the app.js file looked like when I started with.

```javascript
var express = require('express')
  , passport = require('passport')
  , util = require('util')
  , BasicStrategy = require('passport-http').BasicStrategy;

var users = [
    { id: 1, username: 'bob', password: 'secret', email: 'bob@example.com' }
  , { id: 2, username: 'joe', password: 'birthday', email: 'joe@example.com' }
];

function findByUsername(username, fn) {
  for (var i = 0, len = users.length; i < len; i++) {
    var user = users[i];
    if (user.username === username) {
      return fn(null, user);
    }
  }
  return fn(null, null);
}

// Use the BasicStrategy within Passport.
//   Strategies in Passport require a `verify` function, which accept
//   credentials (in this case, a username and password), and invoke a callback
//   with a user object.
passport.use(new BasicStrategy({
  },
  function(username, password, done) {
    // asynchronous verification, for effect...
    process.nextTick(function () {

      // Find the user by username.  If there is no user with the given
      // username, or the password is not correct, set the user to `false` to
      // indicate failure.  Otherwise, return the authenticated `user`.
      findByUsername(username, function(err, user) {
        if (err) { return done(err); }
        if (!user) { return done(null, false); }
        if (user.password != password) { return done(null, false); }
        return done(null, user);
      })
    });
  }
));

var app = express.createServer();

// configure Express
app.configure(function() {
  app.use(express.logger());
  // Initialize Passport!  Note: no need to use session middleware when each
  // request carries authentication credentials, as is the case with HTTP Basic.
  app.use(passport.initialize());
  app.use(app.router);
  app.use(express.static(__dirname + '/public'));
});

// curl -v -I http://127.0.0.1:3000/
// curl -v -I --user bob:secret http://127.0.0.1:3000/
app.get('/',
  // Authenticate using HTTP Basic credentials, with session support disabled.
  passport.authenticate('basic', { session: false }),
  function(req, res){
   res.json({ username: req.user.username, email: req.user.email });
  });

app.listen(3000);
```

First changes, add some requires, remove some requires.

```javascript
var express = require('express')
  , passport = require('passport')
  , util = require('util')
  , BasicStrategy = require('passport-http').BasicStrategy;
```

and changed it to

```javascript
var express = require('express')
  , passport = require('passport')
  , util = require('util')
  , BasicStrategy = require('passport-http').BasicStrategy
  , morgan  = require('morgan')
  , app     = express();
```

Then I deleted the entire section shown below.

```javascript
var app = express.createServer();

// configure Express
app.configure(function() {
  app.use(express.logger());
  // Initialize Passport!  Note: no need to use session middleware when each
  // request carries authentication credentials, as is the case with HTTP Basic.
  app.use(passport.initialize());
  app.use(app.router);
  app.use(express.static(__dirname + '/public'));
});
```

I replace that with a nicely cleaned up Express.js v4 section of code and the replacement for logger, the morgan() library. Initializing passport however is still done in the same ole’ trusty way with initialize().

```javascript
app.use(morgan());
app.use(passport.initialize());
```

Ordering of code has changed a bit for express.js, which meant I needed to have the app.use commands before the following section, which I moved right up underneath the two app.use statements.

```javascript
// curl -v -I http://127.0.0.1:3000/
// curl -v -I --user bob:secret http://127.0.0.1:3000/
app.get('/',
    // Authenticate using HTTP Basic credentials, with session support disabled.
    passport.authenticate('basic', { session: false }),
    function(req, res){
        res.json({ username: req.user.username, email: req.user.email });
    });
```

## Finished app.js File

## After those changes the app.js file should look like this.

```javascript
var express = require('express')
  , passport = require('passport')
  , util = require('util')
  , BasicStrategy = require('passport-http').BasicStrategy
  , morgan  = require('morgan')
  , app     = express();

app.use(morgan());
app.use(passport.initialize());

// curl -v -I http://127.0.0.1:3000/
// curl -v -I --user bob:secret http://127.0.0.1:3000/
app.get('/',
    // Authenticate using HTTP Basic credentials, with session support disabled.
    passport.authenticate('basic', { session: false }),
    function(req, res){
        res.json({ username: req.user.username, email: req.user.email });
    });

var users = [
    { id: 1, username: 'bob', password: 'secret', email: 'bob@example.com' }
  , { id: 2, username: 'joe', password: 'birthday', email: 'joe@example.com' }
];

function findByUsername(username, fn) {
  for (var i = 0, len = users.length; i < len; i++) {
    var user = users[i];
    if (user.username === username) {
      return fn(null, user);
    }
  }
  return fn(null, null);
}

// Use the BasicStrategy within Passport.
//   Strategies in Passport require a `verify` function, which accept
//   credentials (in this case, a username and password), and invoke a callback
//   with a user object.
passport.use(new BasicStrategy({
  },
  function(username, password, done) {
    // asynchronous verification, for effect...
    process.nextTick(function () {

      // Find the user by username.  If there is no user with the given
      // username, or the password is not correct, set the user to `false` to
      // indicate failure.  Otherwise, return the authenticated `user`.
      findByUsername(username, function(err, user) {
        if (err) { return done(err); }
        if (!user) { return done(null, false); }
        if (user.password != password) { return done(null, false); }
        return done(null, user);
      })
    });
  }
));

app.listen(3000);
```

If you execute either of the curl commands shown in the comments in the app.js code you should see the respective response when running the application.

```bash
curl -v -I http://127.0.0.1:3000/
curl -v -I --user bob:secret http://127.0.0.1:3000/
```

…and that should get you running with Passport.js and Express.js v4.
