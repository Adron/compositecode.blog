---
title: Troubleshooting Node.js Deploys on Beanstalk – The Express v4 node ./bin/www Switch Up
date: 2014-08-06 09:12:31 -0700
last_modified_at: 2014-08-06 12:55:03 -0700
permalink: /2014/08/06/troubleshooting-node-js-deploys-on-beanstalk-the-express-v4-node-binwww-switch-up/
slug: troubleshooting-node-js-deploys-on-beanstalk-the-express-v4-node-binwww-switch-up
wp_id: 10219
original_url: https://compositecode.blog/2014/08/06/troubleshooting-node-js-deploys-on-beanstalk-the-express-v4-node-binwww-switch-up/
categories:
- AWS
- How-to
- Node.js Things
tags:
- beanstalk
- deployment
- elastic beanstalk
- nginx
- node
- node.js
- nodejs
- npm
- npm start
excerpt: I’ve gotten a ton of 502 errors and related issues that crop up when deploying the Beanstalk. One of the issues that cropped up a few times recently, until I stumbled into a working solution was the 502 NGINX error. I went digging around and ended up just trying to deploy a default, fresh from …
---

I’ve gotten a ton of 502 errors and related issues that crop up when deploying the Beanstalk. One of the issues that cropped up a few times recently, until I stumbled into a working solution was the 502 NGINX error. I went digging around and ended up just trying to deploy a default, fresh from the ‘express newAppNameHere’ creation and still got the error.

I went digging through the Beanstalk configuration for the app and found this little tidbit.

[![Node Command (Click for full size image)](https://photos.adron.me/Software/Software-Development/AWS-Magic-and-Unicorns/i-FQ3P6gL/0/M/theTidBit-M.png)](https://photos.adron.me/Software/Software-Development/AWS-Magic-and-Unicorns/i-FQ3P6gL/0/O/theTidBit.png)

*Node Command (Click for full size image)*

I’ve pointed out the section where I’ve added the command.

```bash
node ./bin/www
```

Based on the commands that are executed normally, it seems `npm start` would work work to get the application started. But I have surmised the issue is that the commands are executed sequentially;

```bash
node server.js
node app.js
npm start
```

When these are executed in order, errors crop up and the command that should work `npm start` begins with a corrupted and error laden beginning. Leaving the application not running. However by adding the `node ./bin/www` to the text box all the others are skipped and this command is issued, resulting in a running application.

The other thing is to follow the now standard approach of just issue `npm start`, but being sure to replace what I put in the text box above (`node ./bin/www`) with `npm start` so that beanstalk only runs npm start instead of the ordered execution.
