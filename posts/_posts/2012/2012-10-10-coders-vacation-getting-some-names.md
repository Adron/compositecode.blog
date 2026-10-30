---
title: 'Coder’s Vacation : Getting Some Names…'
date: 2012-10-10 18:55:14 -0700
last_modified_at: 2012-10-11 22:39:40 -0700
permalink: /2012/10/10/coders-vacation-getting-some-names/
slug: coders-vacation-getting-some-names
wp_id: 6737
original_url: https://compositecode.blog/2012/10/10/coders-vacation-getting-some-names/
categories:
- How-to
- Javascript
- Node.js Things
tags:
- continuous integration
- javascript
- js
- node
- node.js
- nodejs
excerpt: 'One of the things I’ve started working on is a #PhatData (re: my renamed version of big data) sample. So far what I’ve created is a JavaScript Application that works something like this. (The actual build status is shown to the right here in the “build status” image) Step #1: Continuous Integration The first thing I did …'
---

[![Actual Live Status of the NameFactory Project](https://secure.travis-ci.org/Adron/NameFactory.png "Actual Live Status of the NameFactory Project")](https://travis-ci.org/#!/Adron/NameFactory)

One of the things I’ve started working on is a [#PhatData](https://twitter.com/i/#!/search?q=%23phatdata&src=typd) (*re: my renamed version of big data*) sample. So far what I’ve created is a JavaScript Application that works something like this. (The actual build status is shown to the right here in the “build status” image)

**Step #1: Continuous Integration**

The first thing I did was setup a solid node.js project that works on Travis CI (Continuous Integration). This is a pretty quick process. First create a directory and add an appropriate .gitignore and README.md file.

```bash
$ mkdir NameFactory
$ cd NameFactory/
$ git init
Initialized empty Git repository in /Users/adron/coderz/NameFactory/.git/
$ git remote add origin git@github.com:Adron/NameFactory.git
$ mate README.md
$ mate .gitignore
```

The mate command is merely textmate, use whatever you’d like though to create the files. I also use Sublime 2 and other things, textmate just happens to be the poison I often choose from the command line. The .gitignore has the following to take care of WebStorm and other files that might pop up.

```bash
*.idea
.idea
idea
.DS_Store
*.DS_Store

lib-cov
*.seed
*.log
*.csv
*.dat
*.out
*.pid
*.gz

pids
logs
results

node_modules
npm-debug.log
```

The README.md I just put the following in. You don’t really need this, but I’m showing you what should be put in a minimal project. In addition to being a good practice, we’ll need the README.md file for plugging in Travis CI in a few steps.

```bash
Name Factory
===
Description: This is JavaScript Node.js Project for generating random names.
```

Commit those files.

```bash
$ git add -A
$ git commit -m 'Adding gitignore and README.md.'
[master (root-commit) 14b1cf8] Adding gitignore and README.md.
 2 files changed, 23 insertions(+)
 create mode 100644 .gitignore
 create mode 100644 README.md
$
```

Once that is added there are some other files needed for Travis CI that I’ll add before flipping on the actual CI project on the Travis CI Website. First add a .travis.yml file to the project.

```ruby
language: node_js

# test on two node.js versions: 0.6 and 0.8
node_js:
  -- 0.6
  -- 0.8
```

The packages file should look like this.

```javascript
{
  "author": "Adron Hall <adronhall@gmail.com>",
  "name": "NameFactory",
  "description": "A library that creates randomly generated names for insert into various databases.",
  "version": "0.0.1",
  "homepage": "https://github.com/Adron/NameFactory/wiki&quot;,
  "main": "./lib/names",
  "repository": {
    "type": "git",
    "url": "git@github.com:Adron/NameFactory.git"
  },
  "scripts": {
    "test": "vows --spec"
  },
  "engines": {
    "node": ">= 0.4"
  },
  "dependencies": {},
  "devDependencies": {
    "vows": "0.6.x"
  }
}
```

At this point add a few tests that you know pass. I added the following examples from the [vows site](http://vowsjs.org/) (this is the default example on the site).

```javascript
var vows = require('vows'),
    assert = require('assert');

// Create a Test Suite
vows.describe('Division by Zero').addBatch({
    'when dividing a number by zero': {
        topic: function () { return 42 / 0 },

        'we get Infinity': function (topic) {
            assert.equal (topic, Infinity);
        }
    },
    'but when dividing zero by zero': {
        topic: function () { return 0 / 0 },

        'we get a value which': {
            'is not a number': function (topic) {
                assert.isNaN (topic);
            },
            'is not equal to itself': function (topic) {
                assert.notEqual (topic, topic);
            }
        }
    }
}).run();
```

…now make sure the tests run ok…

```bash
$ node test/names_object_should_exist.js
··· ✓ OK » 3 honored (0.003s)
$
```

So that’ll get the continuous integration via [Travis-CI for NameFactory](https://travis-ci.org/#!/Adron/NameFactory) up and running, with a [Github NameFactory Repository](https://github.com/Adron/NameFactory) that is ready for the name generation code to be added. For my next blog entry I’ll leap into some generation strategies, dig up some good name lists (if you know of any, leave a comment w/ a link), and work on figuring out the fastest way to generate names.

Once that’s done, it’s time to setup some distributed databases.
[![Shout it](http://dotnetshoutout.com/image.axd?url=http%3A%2F%2Fcompositecode.com%2F2012%2F10%2F10%2Fcoders-vacation-getting-some-names%2F)](http://dotnetshoutout.com/Coders-Vacation-Getting-Some-Names%E2%80%A6-Composite-Code)
