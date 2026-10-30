---
title: 'Deploy a Framework Friday #4 Some Node.js .gitignore Cloud 9 IDE Sharing toward Cloud Foundry / Iron Foundry Deployment'
date: 2012-08-03 12:45:23 -0700
last_modified_at: 2012-08-03 15:06:01 -0700
permalink: /2012/08/03/deploy-a-framework-friday-4-some-node-js-gitignore-cloud-9-ide-sharing-toward-cloud-foundry-iron-foundry-deployment/
slug: deploy-a-framework-friday-4-some-node-js-gitignore-cloud-9-ide-sharing-toward-cloud-foundry-iron-foundry-deployment
wp_id: 6165
original_url: https://compositecode.blog/2012/08/03/deploy-a-framework-friday-4-some-node-js-gitignore-cloud-9-ide-sharing-toward-cloud-foundry-iron-foundry-deployment/
categories:
- How-to
- Iron Foundry
- Node.js Things
- Platform (as a Service)
- Video
tags:
- cloud9ide
- express
- github
- ide
- javascript
- node.js
- nodejs
excerpt: Today’s “Deploy a Framework Friday” is a little bit of a diversion. Today Richard (@rseroter) and I dove into Cloud9IDE (@Cloud9IDE) to try out some pair programming with the online IDE sharing. We made some minor progress with Matt (@matt_pardee) & Eric (@ang3lfir3) jumping in for a few minutes. The intent of this effort was …
---

Today’s “Deploy a Framework Friday” is a little bit of a diversion. Today Richard ([@rseroter](https://twitter.com/rseroter)) and I dove into Cloud9IDE ([@Cloud9IDE](https://twitter.com/cloud9ide)) to try out some pair programming with the online IDE sharing. We made some minor progress with Matt ([@matt\_pardee](https://de.twitter.com/matt_pardee)) & Eric ([@ang3lfir3](https://twitter.com/ang3lfir3)) jumping in for a few minutes. The intent of this effort was to pull together a little code to deploy, as Richard wrote about a few months ago in the article “[Deploying Node.js Applications to Iron Foundry using the Cloude9 IDE](http://seroter.wordpress.com/2012/04/13/deploying-node-js-applications-to-iron-foundry-using-the-cloude9-ide/)“.

Here’s a video of us all fumbling through attempting to get the .gitignore file setup.

<iframe allowfullscreen="" frameborder="0" height="363" loading="lazy" mozallowfullscreen="" src="https://player.vimeo.com/video/46899252" webkitallowfullscreen="" width="580"></iframe>

Richard Seroter (@rseroter) and I (@adron) took a stab at sharing some code, with the attempt to do some pair programming. We made a little progress, and even had some people join us live via Twitter and edit some of the code with us. For a short play by play, check out the blog entry here: <http://compositecode.com/2012/08/03/deploy-a-frame…dry-deployment/>

Questions:

1. Why did the .gitignore not show up on Richard’s Screen?
2. What were the intermittent errors that came up?
3. Why did it say I was setup for “premium” but I couldn’t use express?
4. Is it supposed to be that the other person can’t make changes while someone is chatting?

I’m not sure what happened (anyone at Cloud 9 IDE know what happened) when the .gitignore totally disappeared  but in the video you can see that I committed and pushed the .gitignore file. I had to recreate it to get anything to show up, and initially it didn’t seem to share either. I’m not sure how that is supposed to work, but am assuming something wasn’t setup correctly in the first place.

As for express I’ll be giving that a try a little bit later.

## Next Steps Toward Deployment

Over the next few weeks or so, Richard and I will be going back and forth building a Node.js based web application for deployment from [Cloud 9 IDE](https://c9.io/) to our [Iron Foundry Environment](http://ironfoundry.org). Overall, this will be a slightly drawn out “*Deploy a Framework Friday*“, with its own sub-parts to the series.

We’ll culminate the project in an [open source project that will be available on Github](https://github.com/IronFoundry/Cloud9_Sample) and also with a summary on the [Iron Foundry Blog](http://ironfoundry.org). In one of our pending blog entries we’ll draw up the architecture of the application we’ll be building out. So stay tuned!

***NOTE: Working in conjunction with these other bloggers*****/*****blogs:***

- Check out [Richard’s blog](http://seroter.wordpress.com/) at <http://seroter.wordpress.com/>. <= read it, he’s got some great articles on all sorts of tech topics.
- Check out the [Iron Foundry Blog](http://blog.ironfoundry.org/) at <http://blog.ironfoundry.org/>. <= Lot’s of great material about the Iron Foundry Project and what it adds to the Cloud Foundry open source PaaS Project.
