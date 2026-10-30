---
title: The Fastest Way to Build a Quick Starter App with Express.js
date: 2020-03-25 09:43:46 -0700
last_modified_at: 2020-12-07 06:33:31 -0800
permalink: /2020/03/25/expressjs/
slug: expressjs
wp_id: 16711
original_url: https://compositecode.blog/2020/03/25/expressjs/
categories:
- Javascript
- Node.js Things
- nodejs
tags:
- coding
- express
- expressjs
- javascrip
- node
- nodejs
- programming
- software development
- web app
- web application
excerpt: Over the years I’ve used Express.js many times as a quick getting started example app. Since I often reference it I wanted to provide a short post that shows exactly what I do 99.9% of the time to start one of these quick Express.js reference apps. I’ve detailed in this post how to get started …
image: /wp-content/uploads/2018/07/1200px-node-js_logo.png
---

Over the years I’ve used Express.js many times as a quick getting started example app. Since I often reference it I wanted to provide a short post that shows exactly what I do 99.9% of the time to start one of these quick Express.js reference apps. I’ve detailed in this post how to get started with Express.js the fastest way I know. There is one prerequisite, I’m assuming in this post you’ve already got Node.js installed. With that in mind, check out my installation suggestions for Node.js if you need to get that installed still. The other thing, is you’ll need to have git installed. On MacOS and Linux git is most likely installed already, if you’re on Windows I’ll leave that googling exercise up to you.

Create a directory and navigate into the directory.

`mkdir quick-start-express
cd quick-start-express`

Now in that directory execute the following command. Note, this command is available as of node.js 8.2.0.

`npx express-generator
npm install`

Inside that directory that you’ve navigated to, you’ll now have an Express.js skeleton app setup to run with the dependencies now downloaded with npm install. On MacOS or Linux run the following command to start the web app.

`DEBUG=quick-start-express:* npm start`

If you’re on Windows run the following command.

`set DEBUG=quick-start-express:* & npm start`

That’s it, one of the quickest ways to get a Node.js site up and running to start developing against!

If you’d like to dig in a bit deeper, here’s a great follow up post on [creating APIs with Express](https://www.toptal.com/express-js/nodejs-typescript-rest-api-pt-1). Give it a read, it’ll give you some great next steps to try out!

Cheers, and happy thrashing code!
