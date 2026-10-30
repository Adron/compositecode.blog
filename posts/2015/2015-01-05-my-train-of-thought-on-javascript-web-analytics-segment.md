---
title: My Train of Thought on JavaScript, Web Analytics, & Segment
date: 2015-01-05 22:46:51 -0700
last_modified_at: 2018-04-18 17:48:31 -0700
permalink: /2015/01/05/my-train-of-thought-on-javascript-web-analytics-segment/
slug: my-train-of-thought-on-javascript-web-analytics-segment
wp_id: 10482
original_url: https://compositecode.blog/2015/01/05/my-train-of-thought-on-javascript-web-analytics-segment/
categories:
- Javascript
- Node.js Things
- nodejs
tags:
- analytics
- javascript
- node.js
- nodejs
- segment
- segment.io
- segmentio
- web analytics
excerpt: 'Beware, this is my brain dump as I attempt to figure out Segment integrations. It might seem disconnected at first but I’ll make every effort to loop things back around. First a few pieces of context, or more simply my goals for this blog entry: 1. My goal here is to implement a server side integration …'
image: /wp-content/uploads/2014/01/javascript-logo.png
---

Beware, this is my brain dump as I attempt to figure out Segment integrations. It might seem disconnected at first but I’ll make every effort to loop things back around. First a few pieces of context, or more simply my goals for this blog entry:

1. My goal here is to implement a server side integration with [Segment](https://segment.com/) that allows for data, which flows through their system, to end up in another system.

2. The term, it appears, for the software one would build and deploy to their system for them to feed data into another system is called an integration. There is a [long list of the integrations](https://segment.com/integrations) that they have available today. It’s so long, that Segment actually has a search feature and all of the integrations divided into sub groups of integrations by *advertising*, *analytics*, *marketing*, *sales*, *support*, *developer*, and *user testing*.

**The Nasty Information Architecture Documentation Flow**

Ok, first I started off by merely clicking on the link to the [documentation](https://segment.com/docs/). There is a middle section there that details the integrations, with one link to the general integrations page that is of no use to building an actual new integration, and then the second link brings me to the [integrations docs](https://segment.com/docs/integrations/), which appears at first glance like the right place. So this is where I felt is the best starting place, which by the end of this blog entry I’ll summarize if this was the right determination!

Moving on, I began reading the section titled API Methods, which when clicked sends one to a page actually called [Tracking API Reference](https://segment.com/docs/api/tracking/). I also opened a number of other links on the integrations docs page which all amounted to being sent back to the page that lists all of the existing integrations. These links were, frankly, useless.

I kept clicking away at different links on the Tracking API Reference page, then realized, that the docs were just not leading me in the right direction. So I went back to the [integrations docs](https://segment.com/docs/integrations/) page and the root [documentation](https://segment.com/docs/) page. At this point I was getting pretty frustrated at finding something useful. I’m sure I was missing “that one easy click to success” but the information architecture of this was a bunch of circle jerks back to were one starts. It was basically all setup for putting one back at the data collection side of things with the analytics.js tag or something of that sort.

## Stop.

Ok, this is where I stop and have another 2 devs look at this shit. I am, yes, cursing now because: bullshit. Both of the devs click through and click through the links, based upon my top two criteria. They also can’t seem to find anything useful. We’re all three now discussing our confusion, albeit since I’m trying to implement it, I’m feeling the frustration. The others get a good chuckle out of my quagmire. In my frustration and their good natured attempts to help me, we all do the obvious, forget Segment’s actual docs site and start throwing down some google-fu.

## Google-fu That Documentation!

After a solid bit of digging around we all decide that the best options are simply to do what us coders often do these days, and we each slowly but steadily end up on github. Sure enough, Segment has the respective integrations listed under their [github organization](https://github.com/segmentio). Now mind you, none of us found any tutorials or anything, thus my reasoning behind writing this blog entry to fix that. What we did find were all the existing integrations which serve perfectly as examples of what to implement. THIS is what should have been linked to from the above documentation. Somehwere, anywhere there should have been some type of information architecture navigation that went seemlessly to the examples.

But there wasn’t, not that the three of us could find. Albeit, we all agreed maybe it just wasn’t our day and our google-fu was better than out use of the information architecture of the segment docs? Right now, I didn’t care, I wanted to get moving on the integration. So onward I dug, and then a few more pieces of information cropped up in conversation.

<blockquote class="twitter-tweet" data-dnt="true" data-width="550">
<p dir="ltr" lang="en">Heyo <a href="https://twitter.com/segment?ref_src=twsrc%5Etfw">@segment</a> I'm about to send an integration… but I'm hesitant because of odd docs like this one <a href="https://t.co/safRDgRvf1">https://t.co/safRDgRvf1</a> … which…</p>
<p>— Adron (@Adron) <a href="https://twitter.com/Adron/status/546006586871668737?ref_src=twsrc%5Etfw">December 19, 2014</a></p></blockquote>

<script async="" charset="utf-8" src="https://platform.twitter.com/widgets.js"></script>

More Google-fu and a little fussing on Twitter did the trick. First, thanks to my co-founder digging around busting some Google-fu too, he [found this doc](https://github.com/segmentio/integrations/blob/master/Contributing.md) and sent me a link. It was on page 2 of some results and I also noticed is in a repository that is actually marked “**THIS REPOSITORY IS NOW DEPRECATED**“. This doesn’t exactly make following docs inside of a repository marked this way confidence raising. But I started to push forward regardless and then got a response…

<blockquote class="twitter-tweet" data-dnt="true" data-width="550">
<p dir="ltr" lang="en"><a href="https://twitter.com/Adron?ref_src=twsrc%5Etfw">@adron</a> @0x604 ping integrations@segment.com for today though with your integration and we'll explain the new process. <a href="https://twitter.com/segment?ref_src=twsrc%5Etfw">@segment</a></p>
<p>— Garrett Johnson (@gjohnson391) <a href="https://twitter.com/gjohnson391/status/546008579367796736?ref_src=twsrc%5Etfw">December 19, 2014</a></p></blockquote>

<script async="" charset="utf-8" src="https://platform.twitter.com/widgets.js"></script>

So I immediately put together an email to get the deets on the latest way to get an integration put together. But before I’d even got a return (I did send it on a Friday evening, so I didn’t have any expectation of a response before Monday sometime). But even as I sat waiting, I had implemented a basic integration following the instructions from two other repos I’d found from the deprecated docs; [khaos](https://github.com/segmentio/khaos) and [khaos-integrations](https://github.com/segmentio/khaos-integration). earlier, the [deprecated integrations doc](https://github.com/segmentio/integrations/blob/master/Contributing.md). I did so, making the assumption that processes to get an integration running couldn’t have changed to much, the doc was just deprecated a few weeks ago!

## The Basic Integration

I tried the installation of khaos-node, which worked fine.

```bash
npm install -g khaos
```

Then next I stepped into the README.md and followed the instructions around installation and creation of a khaos template project to create an integration. That’s where I hit an error immediately.

```bash
~/Codez
14:51 $ mkdir integration-decon
~/Codez
14:51 $ khaos install segment/khaos-node integration-decon
khaos · Command failed: Cloning into '/Users/adron/.khaos/integration-decon'...
ERROR: Repository not found.
fatal: Could not read from remote repository.

Please make sure you have the correct access rights
and the repository exists.
~/Codez
14:51 $
```

At this point, seeing that there were some obvious issues I figured I’d aim for a different approach – namely I’d just wait until I got an email that led me to more updated procedures. That came a little later and I started to hack on things based on that approach, which went something like this:

> Hi Adron,
>
> Thanks for putting together an integration! If it’s client side, then you can follow [these docs](https://github.com/segmentio/analytics.js-integrations/blob/master/Contributing.md), and if it’s server side go for [these ones](https://github.com/segmentio/integrations/blob/master/Contributing.md).
>
> If it’s server side, then I’ll get you to fill out one of [these](https://segment.com/docs/partners/join-the-platform/) and we can get a repo set up for you 🙂
>
> Thanks,
> Harriet

Aha! Now I’ve got a path forward thanks to the super helpful words of Harriet! Onward I move with intent and direction. The first link that is relevant there, is the link to the [contributing.md](https://github.com/segmentio/integrations/blob/master/Contributing.md) docs for server side integrations. Check, that’s me, I’m building a server side integration! The second link is a form to insure that they have a repository setup for me to sling code at. So I filled that out, sent it in, and got started reading some docs.
