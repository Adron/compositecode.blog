---
title: Back From Scandinavia, Back to Project Coding, Writing and Organizing
date: 2014-05-26 09:21:20 -0700
last_modified_at: 2020-03-04 09:01:48 -0800
permalink: /2014/05/26/back-from-scandinavia-back-to-project-coding-writing-and-organizing/
slug: back-from-scandinavia-back-to-project-coding-writing-and-organizing
wp_id: 9970
original_url: https://compositecode.blog/2014/05/26/back-from-scandinavia-back-to-project-coding-writing-and-organizing/
categories:
- Community
- My Updates
tags:
- blogging
- c#
- deconstructed
- go
- golang
- javascript
- new relic
- orchestrate
- projects
- wintersmith
- writing
excerpt: I just got back from Scandinavia (and Amsterdam). I went for a million reasons, mostly for the adventure of it. Visiting Stockholm, Copenhagen and Reykjavik I saw about a zillion bikes, great architecture, Tivoli, amazing and beautiful waterways, Viking boat building museums, design to die for and so much more. It’s truly one of the …
---

![viking](/wp-content/uploads/2014/05/viking.jpg)I just got back from Scandinavia (and Amsterdam). I went for a million reasons, mostly for the adventure of it. Visiting Stockholm, Copenhagen and Reykjavik I saw about a zillion bikes, great architecture, Tivoli, amazing and beautiful waterways, Viking boat building museums, design to die for and so much more. It’s truly one of the amazing areas of the world. But now I’m back in ‘Merica and ready to get back to working on projects, design efforts and all the things I love to do. This blog post is a summary of my immediate return to projects, here’s the list broken into coding, writing and organizing:

# Coding

- **Deconstructed** – [[site](http://deconstructed.io)] This is the startup I’ve cofounded with Aaron Gray [@agray](https://twitter.com/agray). Check out our main site at [Deconstructed](http://deconstructed.io/). Check out some of the open source projects we’ve started here and listed below.
- **Deconstructed Docs** – [[site](https://github.com/Deconstructed/deconstructed)] [[JavaScript](http://en.wikipedia.org/wiki/JavaScript)] [[Node.js](http://nodejs.org/)] I’m using [Wintersmith](http://wintersmith.io/) to build docs with static site generation. The docs are located at [docs.deconstructed.io](http://docs.deconstructed.io). Previous blog entries I did on building a static site with Wintersmith are available at [Wintersmith Creating Documentation](http://compositecode.com/2014/02/17/wintersmith-documentation/) and [Working in -34c, Wintersmith Customization & Github Hosting](http://compositecode.com/2014/02/19/working-in-34c-wintersmith-customization-github-hosting/).
- **Symphonize.js** – [[site](https://github.com/Adron/symphonize)] [[JavaScript](http://en.wikipedia.org/wiki/JavaScript)] [[Node.js](http://nodejs.org/)] [[issues](https://github.com/RobertSmith/Orchestrate.NET/issues?page=1&state=open)] This is a project I started to use configuration as a basis for creating data for any database, but specifically Orchestrate (see blog entries under the writing section I did for Orchestrate). The idea behind this started since I needed something to generate test data for Deconstructed. This one is incomplete, but I’ll be pushing it forward to a deployable NPM Module soon that will be easy to download and just use. There’s also a possibility that this becomes a service that I make available in the near future.
- **Orchestrate.NET** – [[site](https://github.com/RobertSmith/Orchestrate.NET)] [[c#](http://en.wikipedia.org/wiki/C_Sharp_(programming_language))] [[issues](https://github.com/RobertSmith/Orchestrate.NET/issues?page=1&state=open)] I’ve been helping out Robert Smith and a crew to manage the effort around the .NET client driver for Orchestrate. This is currently functional and we’d love anybody and everybody using it to really test it out. Currently I’m using this for the OrchestrateExecute Project listed below too.
- **orchestrate-rapping** – [[repo](https://github.com/Adron/orchestral-rapping)] [[go](http://golang.org/)] [[issues](https://github.com/Adron/orchestral-rapping/issues?page=1&state=open)] [[group](https://groups.google.com/forum/#!forum/orchestral-rapping)] Yo yo yo, hit the beat. This is an effort that I and others have kicked off to put together a wrapper for Orchestrate’s API. The reason is simple, we want to be able to develop sitting far away from wifi and connectivity, in a park or a cabin in the woods, with a beer in hand and a fire crackling. All while knowing we’re building something that will work when we reconnect to the land of the internet!
- **OrchestrateExecutive** – [[repo](https://github.com/Adron/OrchestrateExecutive)] [[c#](http://en.wikipedia.org/wiki/C_Sharp_(programming_language))] [[issues](https://github.com/Deconstructed/deconstructed/issues?milestone=2&state=open)] For a very serious enterprise application, I’ve started hacking together a C# Application using Xamarin that will provide a library tier (that could be used as a sample) to use in building to Android, iOS or Windows Phone and all of the native Windows, Linux or OS-X apps that might be needed. In the application I’ll be using [Orchestrate](http://orchestrate.io) and [Deconstructed](http://deconstructed.io) to build out the application. Stay tuned at [blog.deconstructed.io](http://blog.deconstructed.io) for more on this.
- …and also inspired by Rick Turoczy [@turoczy](https://twitter.com/turoczy) eternally [another fucking side project](https://github.com/Adron/anotherfuckingsideproject) will be going live soon. 😮

# Writing

- **Deconstructed** – [[blog](http://blog.deconstructed.io/)] This is the blog we’ve setup and will be posting to for Deconstructed. This will cover a breadth of material from technical blogs to business efforts on behalf of Deconstructed.
- **New Relic** – [[blog](http://blog.newrelic.com)] I’ve got a bunch of articles I’ve posted for New Relic and am continuing to write. Generally I manage a post every 2 weeks or so. My latest pieces I’ve written and posted with New Relic include [The Work and Flow of JavaScript: Getting Started](http://blog.newrelic.com/2014/04/04/work-and-flow-of-javascript/), [The Work and Flow of JavaScript: Continuous Delivery](http://blog.newrelic.com/2014/05/07/work-and-flow-of-javascript-2/) and [Node.js Frameworks and Stacks to Build Future Enterprise Apps](http://blog.newrelic.com/2014/04/29/node-builds-future-enterprise/).
- **The New Stack** – [[blog](http://thenewstack.io/)] This is a great effort put together by Alex Williams and his team to provide a higher quality technology and software developer reporting source. I’ve provided an article so far and will be providing some in the near future. Check it out, I think he’s hit on a great effort here!
- **Orchestrate** – [[blog](http://blog.orchestrate.io)] Their blog has been jam packed with technical gems. I’ve been impressed all while being stoked to have contributed to the effort! You can check out my existing posts with Orchestrate; [Test Data Builder Symphonize.js With Chance.js](http://orchestrate.io/blog/2013/11/14/7test-data-builder-symphonizejs-with-chancejs/), [Symphonize Some Create, Read, Update & Delete [CRUD] via Orchestrate.js](http://orchestrate.io/blog/2013/12/06/12create-read-update-delete-crud/) and [Getting Serious With Symphony.js – JavaScript TDD/BDD Coding Practices](http://orchestrate.io/blog/2014/01/03/javascript_tddbdd/). More to come here as I’m putting together more pieces as Orchestrate is a key piece of our Deconstructed architecture!
- **Pluralsight** – [[courses](http://www.pluralsight.com/training/Courses)] Not exactly writing in the sense of a blog post or article, but in the sense of video, editing, writing and training rolled into one. Pluralsight and I refer to this as being an [author](http://pluralsight.com/training/Authors/Details/adron-hall), which I can dig. Currently I’ve got a *Work & Flow of JavaScript* course in the works in my \**spare time*\*. My existing courses include; [Riak Fundamentals](http://pluralsight.com/training/Courses/TableOfContents/riak-introduction) and [Docker Fundamentals](http://pluralsight.com/training/Courses/TableOfContents/docker-fundamentals).

# Organizing

- **Bike n’ Hack** – Follow [@bikenhack](https://twitter.com/BikenHack) for information and more coming soon.
- **Node PDX** – More to come on this soon.

…subscribe to the RSS link, hit the e-mail subscription or just ping me or follow me [@adron](http://twitter.com/adron) on Twitter and I’ll keep you posted on the goings on of all my efforts and others. Cheers!
