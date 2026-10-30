---
title: Coding on Orchestrate.io & Orchestrate.js & Orchestrate.NET
date: 2014-05-01 01:17:19 -0700
last_modified_at: 2014-05-09 10:45:57 -0700
permalink: /2014/05/01/coding-on-orchestrate-io-orchestrate-js-orchestrate-net/
slug: coding-on-orchestrate-io-orchestrate-js-orchestrate-net
wp_id: 9934
original_url: https://compositecode.blog/2014/05/01/coding-on-orchestrate-io-orchestrate-js-orchestrate-net/
categories:
- .NET Bits
- Community
- Deconstructed.io
- How-to
- Javascript
- Just News
- Node.js Things
- Orchestrate.io
tags:
- github
- javascript
- node.js
- nodejs
- open source
- open source project
- open source software
- orchestrate
- orchestrate.io
- software project
excerpt: First context, then I’ll dive in. Orchestrate http://orchestrate.io/ Orchestrate is a service that provides a simple API to access a multitude of database types all in one location. Key value, graph or events, some of the database types I’ve been using, are but a few they’ve already made available. There are many more on the …
---

First context, then I’ll dive in.

# Orchestrate

# <http://orchestrate.io/>

[![](https://photos.adron.me/Software/Misc-Images/Just-Icons-and-Bits/i-jHttDjn/0/Th/orchestrate.io-Th.gif)](http://orchestrate.io/)Orchestrate is a service that provides a simple API to access a multitude of database types all in one location. Key value, graph or events, some of the database types I’ve been using, are but a few they’ve already made available. There are many more on the way. Having these databases available via an API instead of needing to go through the arduous process of setting up and maintaining each database for each type of data structure is a massive time saver! On top of having a clean API and solid database platform and infrastructure Orchestrate has a number of client drivers that provide easy to use wrappers. These client drivers are available for a number of languages. Below I’ve written about two of these that I’ve been involved with in some way over the last couple of months.

# Orchestrate.NET

# <https://github.com/RobertSmith/Orchestrate.NET>

This library I’m currently using for a demonstration application built against the [Deconstructed.io](http://deconstructed.io/) services (follow us on twitter ya! [@BeDeconstructed](http://twitter.com/bedeconstructed)), a startup I’m co-founding. I’m not sure exactly what the app will be, but being .NET it’ll be something enterprisey. Because: .NET is Enterprise! For more on this project check out the [Deconstructed.io Blog](http://blog.deconstructed.io/).

Some of the latest updates with this library.

- Just got everything [fixed up and working with Visual Studio 2012 and Xamarin Studio with the latest Microsoft.Bcl.Build Libraries](https://github.com/RobertSmith/Orchestrate.NET/pull/18).
- The [app.config](https://github.com/RobertSmith/Orchestrate.NET/blob/master/Orchestrate.Net.Tests/app.config) is setup to just add your API key and run the tests for verification of the build. Integration tests and others.
- Project is now [setup as a PCL or Portable Class Library](https://github.com/RobertSmith/Orchestrate.NET/pull/15) for use with Xamarin and Android, iOS, Linux and related builds or w/ Visual Studio for Windows Phone and other related builds.

But there’s still a bit of work to do for the library, so consider this a call out for anybody that has a cycle they’d like to throw in on the project, let us know. We’d happily take a few more pull requests!  The main two things we’d like to have done real soon are…

- [Additional Documentation](https://github.com/RobertSmith/Orchestrate.NET/issues/10), Especially in the [README.md](https://github.com/RobertSmith/Orchestrate.NET/blob/master/README.md) with a few more examples of code here and there.
- [More unit tests, especially one’s that are pure unit and not integration](https://github.com/RobertSmith/Orchestrate.NET/issues/9) to help with any future refactoring of the code.

# Orchestrate.js

# <https://github.com/orchestrate-io/orchestrate.js>

With the latest [fixes](https://github.com/Bowery/orchestrate.js/pull/27), [additions](https://github.com/Bowery/orchestrate.js/pull/23) and [updates](https://github.com/Bowery/orchestrate.js/pull/28) the orchestrate.js client driver is getting more feature rich by the day. In addition [@housejester](https://github.com/housejester) has created an [orchestrate-brain project](https://github.com/housejester/orchestrate-brain) for [Hubot](http://hubot.github.com/) that uses Orchestrate.js. If you’re not familiar with Hubot, but sure to check out the company robot that can dramatically improve and reduce employee efficiency! Keep an eye on that project for more great things, or create a Hubot to keep a robotic eye on the project.

Here are a few key things to note that have been added to help in day-to-day coding on the project.

- The travis.yml file has been added for the Travis Continuous Integration build. This build runs against node.js v0.10 and v0.8.
- Testing is done with mocha, expect.js and nock. To get the tests up and running, clone the repo and then build with the make file. The tests will run in tdd format.
- Promises are provided via the kew library.

If you’re opening up the project in WebStorm, it’s great to setup the mocha tests with the integrated mocha testing as shown below. After you’ve cloned the project and run ‘npm install’ then follow these steps to add the Mocha testing to the project. We’ve already setup exclusions in the .gitignore for the .idea directory and files that WebStorm uses.

First add a configuration by clicking on Edit Configurations.

![Edit Configurations](https://photos.adron.me/Software/Software-Development/Orchestrateio-Hacking/i-nSpkxdB/0/O/edit%20configuration%2001.png)

*Edit Configurations*

Next click on the + to add a new configuration to run. Select the Mocha option from the list of configurations.

[![Mocha & Other Configurations in WebStorm](https://photos.adron.me/Software/Software-Development/Orchestrateio-Hacking/i-VtCRbQj/0/O/edit%20configuration%2002.png)](https://photos.adron.me/Software/Software-Development/Orchestrateio-Hacking/i-VtCRbQj/0/O/edit%20configuration%2002.png)

*Mocha & Other Configurations in WebStorm*

On the next screen set a name for the configuration. Set the test directory to the path for the test directory in the project. Then finally set the User interface option for Mocha to TDD instead of the default BDD.

[![Edit Configuration Dialog](https://photos.adron.me/Software/Software-Development/Orchestrateio-Hacking/i-f9v3KZQ/0/O/edit%20configuration%2003.png)](https://photos.adron.me/Software/Software-Development/Orchestrateio-Hacking/i-f9v3KZQ/0/O/edit%20configuration%2003.png)

*Edit Configuration Dialog*

Last but not least run the tests and you’ll see the list of green lights light up the display with positive results.

[![Test Build](https://photos.adron.me/Software/Software-Development/Orchestrateio-Hacking/i-nRXmN6X/0/O/edit%20configuration%2004.png)](https://photos.adron.me/Software/Software-Development/Orchestrateio-Hacking/i-nRXmN6X/0/O/edit%20configuration%2004.png)

*Test Build*
