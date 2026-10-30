---
title: How to Build an NPM Package, Beginning the Symphonize Project
date: 2013-11-03 21:29:51 -0800
last_modified_at: 2013-11-03 21:29:51 -0800
permalink: /2013/11/03/how-to-build-an-npm-package-beginning-the-symphonize-project/
slug: how-to-build-an-npm-package-beginning-the-symphonize-project
wp_id: 9100
original_url: https://compositecode.blog/2013/11/03/how-to-build-an-npm-package-beginning-the-symphonize-project/
categories:
- How-to
- Javascript
- Node.js Things
- Orchestrate.io
- Software Projects
tags:
- client library
- javascript
- node
- node package manager
- node.js
- node.js package manager
- nodejs
- npm
- orchestrate
- orchestrate.io
- symphonize
excerpt: 'NPM has helped to build on the massive Node.js popularity and drive JavaScript from a simple scripting language in the web browser to a powerful and capable back-end server language. A quick refresher, NPM stands for Node.js Package Manager and each package is made up of: a folder containing a program described by a package.json …'
---

[NPM](https://npmjs.org) has helped to build on the massive [Node.js](http://www.nodejs.org/) popularity and drive JavaScript from a simple scripting language in the web browser to a powerful and capable back-end server language. A quick refresher, NPM stands for **N**ode.js **P**ackage **M**anager and each package is made up of:

1. a folder containing a program described by a package.json file.
2. a gzipped tarball containing [1]
   1. a url that resolves to [2]
   2. a <name>@<version> that is published on the registry with [A]
   3. a <name>@<tag> that points to [B]
   4. a <name> that has a “latest” tag satisfying [C]
   5. a git url that, when cloned, results in [1]

[![Path structure view in Jetbrains Webstorm IDE.](https://photos.adron.me/Software/Software-Development/Symphonize/i-73tbQNx/0/O/blurple.png "Path structure view in Jetbrains Webstorm IDE.")](http://www.jetbrains.com/webstorm/)

*Path structure view in Jetbrains Webstorm IDE.*

With that basic understanding of what a module is that NPM provides, let’s jump through the steps to build a module that provides some basic functionality. I won’t cover too many parts in detail yet, just the happy path to getting an NPM library running.

First let’s create an appropriate folder and file structure to get started with. Here’s the commands I ran to get started.

```bash
mkdir bin
mkdir lib
```

With these two directories created I then created the following files in the designated paths. In bin I created the *symphonize.js* file and in lib I created a *main.js* file.

Now, I added the following code to the symphonize.js file.

```javascript
exports.Coupling = function (searchThis, forThis) {
    var returnValue = 'no';
    if (searchThis.indexOf(forThis) > -1) {
        returnValue = 'yes';
    }
    return returnValue;
}
```

In the main.js file I added the following.

```javascript
(function () {
    var couple = require('../bin/symphonize');
    couple.Coupling("Sample text", "Sample");
}).call(this)
```

There are a number of issues with this code, I know, but it’s just a sample of the minimal amount of code, folder structure and *packages.json* that I need to get this package installed and ready for iteration as I move forward with the actual code base and what functionality will actually be added. Speaking of the *packages.json* file, I created one and added the following configuration settings to it.

```javascript
{
    "author": "Adron Hall",
    "name": "symphonize",
    "description": "Prints out data to the console! Will be iterating soon for real functionality!",
    "version": "0.1.0",
    "repository": {
        "url": "git@github.com:Adron/symphonize.git"
    },
    "main": "./lib/main",
    "bin": {
        "replaceme": "./bin/symphonize"
    },
    "dependencies": {},
    "devDependencies": {},
    "optionalDependencies": {},
    "engines": {
        "node": "*"
    }
}
```

That is now enough for me to at least get the module added to the global NPM repository, get things pointed back to Github appropriately and move forward with actual coding. I might even setup some continuous builds and delivery at some point, since I’ve now got the end point of where the libraries will be going. The commands to get a module uploaded to the NPM Repository are as follows. This command of course assumes I’ve already added a user using npm adduser or I’ve added one via the web site interface at <https://npmjs.org/>.

```bash
npm publish
```

I’ve now got everything prepared and uploaded to NPM there is now a symphonize module library ready for use.

[![My NPM Page for Symphonize. Click to go to the actual NPM page.](https://photos.adron.me/Software/Software-Development/Symphonize/i-qpwqkkP/0/M/npm-M.png)](https://npmjs.org/package/symphonize)

*My NPM Page for Symphonize. Click to go to the actual NPM page.*

Here’s a few quick references to where everything is:

- [symphonize project](https://github.com/Adron/Symphonize) repository on [github](https://github.com/)
- My contact on Twitter @adron and [Github @adron](https://github.com/Adron)
- The [symphonize module](https://npmjs.org/package/symphonize) on the [NPM repository](https://npmjs.org).
