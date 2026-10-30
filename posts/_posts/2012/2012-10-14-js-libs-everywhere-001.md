---
title: 'Coder’s Vacation : OMG! JavaScript Libraries Spilled EVERYWHERE! Series #001'
date: 2012-10-14 14:19:39 -0700
last_modified_at: 2012-10-14 14:32:03 -0700
permalink: /2012/10/14/js-libs-everywhere-001/
slug: js-libs-everywhere-001
wp_id: 6811
original_url: https://compositecode.blog/2012/10/14/js-libs-everywhere-001/
categories:
- How-to
- Javascript
- Node.js Things
tags:
- bdd
- behavior drive
- javascript
- js
- node
- node.js
- nodejs
- software development
- unit testing
- vows
- vows.js
- vowsjs
excerpt: 'NOTE: All parts of this series and my other series can be found on my series links page. I sat down a few days ago on this trip to get a simple project setup, instead something else happened. It is my fault, entirely my fault. I could have stayed focused on a single library but …'
---

**NOTE:** All parts of this series and my other series can be found on my *[series links page](/write-up-series/)*.

I sat down a few days ago on this trip to get a simple project setup, instead something else happened. It is my fault, entirely my fault. I could have stayed focused on a single library but instead I’ve let them explode. They’re everywhere now in my project!  😮  I’ve learned a great deal about breaking and fixing things though when working with testing frameworks and Node.js. All of this being rooted in my exceedingly simple project called [NameFactory on Github](https://github.com/Adron/NameFactory). Here’s a few of the things I’ve stumbled through over the course of figuring out these testing frameworks.

## vows.js (while chillin’ at Phils Coffee)

[![Phils Coffee, a staunch cup indeed!](/images/adronhall.smugmug.com/SanFranciscoAction/San-Francisco-2012/Coders-Vacation/i-wtjsWqg/0/S/philz-S.jpg "Phils Coffee, a staunch cup indeed!")](http://www.philzcoffee.com/)

*Phils Coffee, a staunch cup indeed!*

If you aren’t familiar with vows, here’s the brief description. [Vows is a node.js testing framework that is built around the notion of BDD, Behavior Driven Development](http://vowsjs.org/). The other important thing to note, is vows.js was built specifically to test asynchronous code. It can test others, but it is more oriented toward asynchronous code. Vows also runs tests in parallel, which thinking about that it takes the random order execution and ups the game even further by running them this way. It can really tighten up code execution and regression that things will indeed work in many different conditions. Building for web scale on the internet, that’s something we definitely need!  🙂

To install vows, it follows your standard pattern with npm:

```bash
npm install vows
```

When I installed it I really bit the bullet and went for a global install.

```bash
sudo npm install -g vows
```

From there I spun up a really simple example that is shown on the vows.js site:

```javascript
var vows = require('vows'),
    assert = require('assert');

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

From this example you run the tests by executing the code with the following command:

```bash
node division-by-zero-test.js
```

This is all fine, but I’d rather be using the vows test runnner. To do that you’ll need to, instead of \*.run(); call the \*.export(); function instead. At this point I started scratching my head a bit and looking for parallels between my understanding of BDD and testing and what vows is doing. So I read further and came up with a few observations.

In vows the convention is to have one test suite per file and have the subject match the name. This makes sense to me, that’s how I’ve generally done similar things with Ruby, C# and the like. You end up with something like this for setting the subject and adding the various test suites:

```javascript
var suite = vows.describe('subject');

suite.addBatch({/* run 1st */}).addBatch({/* 2nd */}).addBatch({/* 3rd */});

suite.addBatch({
   'A context': {
        topic: function () {/* Do something async */},
        'I am a vow': function (topic) {
            /* Test the result of this topic */
        }
    },
   'Another context': {
        topic: function () {/* Do something else async */},
        'I am another vow': function (topic) {
            /* Test the result of this topic */
        },
        'I am another sub-context vow': function (topic) {
            /* Test the result of the topic */
        },
        'And another sub-context': {
            /* Executed when the tests above finish running */
        }
    }
});
```

Each of the topics are the thing that is being tested with the secondary element of each test being the test to verify the topic. Each of these things are run asynchronously, in parallel, so be sure to keep that in mind when using this framework. However note, in the sub-context tests above the sub-context happens in order. This can be used in various ways, but be sure to not abuse this execution model to avoid the asynchronous nature of JavaScript, I’ve only been working with vows for a few days and have already seen code snippets on the web that have done exactly that!

So this is the first part in a series where I’ll just cover all sorts of JavaScript libraries. It took a [Coder’s Vacation](/2012/10/09/coders-vacation-preparation-ricon-2012-html-5-developers-conference-and-loading-up/) however to get me started on this series, enjoy.
