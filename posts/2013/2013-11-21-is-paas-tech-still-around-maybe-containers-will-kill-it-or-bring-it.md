---
title: Is PaaS Tech Still Around? Maybe Containers Will Kill it or Bring it?
date: 2013-11-21 16:17:45 -0800
last_modified_at: 2013-11-26 09:57:36 -0800
permalink: /2013/11/21/is-paas-tech-still-around-maybe-containers-will-kill-it-or-bring-it/
slug: is-paas-tech-still-around-maybe-containers-will-kill-it-or-bring-it
wp_id: 9226
original_url: https://compositecode.blog/2013/11/21/is-paas-tech-still-around-maybe-containers-will-kill-it-or-bring-it/
categories:
- Containers
- Distributed Things
- Ideas
tags:
- cloud foundry
- containers
- docker
- openshift
- opinions
- paas
- platform as a service
excerpt: Recently a post from @Gigabarb popped up on the ole’ Twitter that started a micro-storm of twitter responses. Ok tech users. Who out there is using a PaaS? For realz. Serious question. — Barb Darrow (@gigabarb) November 21, 2013 This got me thinking about a number of things and I started to write her an …
---

Recently a post from [@Gigabarb](http://twitter.com/gigabarb) popped up on the ole’ Twitter that started a micro-storm of twitter responses.

<blockquote class="twitter-tweet" data-dnt="true" data-width="550">
<p dir="ltr" lang="en">Ok tech users. Who out there is using a PaaS? For realz. Serious question.</p>
<p>— Barb Darrow (@gigabarb) <a href="https://twitter.com/gigabarb/status/403536659171377153?ref_src=twsrc%5Etfw">November 21, 2013</a></p></blockquote>

<script async="" charset="utf-8" src="https://platform.twitter.com/widgets.js"></script>

This got me thinking about a number of things and I started to write her an email specifically, but realized I should really just blog it. After all, the topic is actually part of what should be the public conversation. It’s about the changing world of technology, which we’re all part of…

# First Topic: Usage of PaaS

Barb, just shortly after the tweet above was posted, this other tweet altered what information I might provide her. [@TheSteve0](https://twitter.com/TheSteve0) had responded with some items, which @GigaBarb then responded with

<blockquote class="twitter-tweet" data-dnt="true" data-width="550">
<p dir="ltr" lang="en"><a href="https://twitter.com/TheSteve0?ref_src=twsrc%5Etfw">@TheSteve0</a> those names are the same … looking for more…thanks tho</p>
<p>— Barb Darrow (@gigabarb) <a href="https://twitter.com/gigabarb/status/403577452091285504?ref_src=twsrc%5Etfw">November 21, 2013</a></p></blockquote>

<script async="" charset="utf-8" src="https://platform.twitter.com/widgets.js"></script>

Now, not to pick on OpenShift & Red Hat (the effort [@TheSteve0](https://twitter.com/TheSteve0) is working with), because they have a great open source effort going on around this PaaS Technology, but Barb had a point. If Cloud Foundry responded with something like this, she’d still have a point. The only companies that continually sign up new companies is AWS & Beanstalk (ok, so they don’t call it PaaS, it gets you to the same place – arguably better than most of the others), a little bit at Windows Azure and a few companies pop up every once in a long while that might take Cloud Foundry or OpenShift and run with it. Most of the early adopters are already on board and most that might get on board are still mostly just waiting in the sidelines.

This fact is frustrating for those

in the space that want to see more penetration, but for those that arent’ technically in the space, it seems kind of like ASP. Oh wait, I should add context now, ASPs as in Application Service Providers. The technology from the beginning of the 21st century similar in many ways to what is dubbed SaaS now. At the time it could have been revolutionary. However at the time nobody picked it up either. This is similar to what PaaS is seeing. However…

## A Hypothesis of What Will Happen to PaaS Tech

![](https://photos.adron.me/Software/Misc-Images/Logo/i-Z4XmSP4/1/O/PAAS%20Rocker%20Logo.jpg)

I have a theory of what will happen to PaaS Tech, it is similar to ASP Tech. PaaS will keep plundering along in odd ways, and eventually one day, it will become a mainstream tech. Right now however it will remain limited. In that same turn, by the time it becomes a common tech, it’ll be called something else.

Here’s a few reasons. One, is that many developers see PaaS and their response, especially if they’re seasoned developers with more than a few years under their belt, is to respond will immediate apprehension to the tech. It removes key elements of what they want to control. It hides things they can’t actually get to and it abstracts in ways that don’t always make sense. The result is that many senior devs stay away from pure PaaS offerings and instead use it only for prototyping, but production gets something totally different. I’ve been there more than a few times myself.

However, the result of what most senior devs end up with, when they get their continuous integration and development environments running at full tilt, is exactly what PaaS is attempting to promise. There are some companies, with senior devs, and extremely intelligent members that have taken PaaS and effectively implemented it into their continuous integration and delivery environment giving them strengths that most companies can only imagine to have.

One of those companies is lucky and smart enough to have Jonathan Murray [@adamalthus](https://twitter.com/Adamalthus) heading up efforts. On his team he also has Dave McCrory [@mccrory](https://twitter.com/mccrory) and Brian McClain [@brianmmclain](https://twitter.com/BrianMMcClain). To boot, they are close to the Cloud Foundry team (and [@wattersjames](http://twitter.com/wattersjames), who cuts a path when there are issues) and keep a solid effort going working with key partners such as [@Tier3](http://twitter.com/tier3) ([now part of CenturyLink](/2013/11/19/centurylink-is-on-a-roll/))  and other companies that help bring together one of the most strategically and tactically relevant PaaS deployments to date.

Other PaaS deployments are questionable for various reasons, they’re trying, but they aren’t there. At least not the types of companies and efforts that Barb was looking for. So really, if there is another out there that’s hiding, but wants serious street cred. A boost to hiring serious A grade talent, and to push forward past competitors, please let us know. Let me know, let Barb know and let’s hear about what you’re doing. If a company is hiding their implementation and doesn’t want to be part of the community, then fine, they can stay hidden and not gain the benefit of the community that presses forward beyond them. But I would love to hear from those that I might have missed, that want to push forward, so ping me. Ping Barb, we’ll get word out there and get developers checking out and making sure your company is getting it done! 😉

# Second Topic: PaaS on PaaS and Start Docker

PaaS is nice. If your company can get it deployed and use it effectively, the you’re going to push forward fast in many regards. Deployments, savings, code cleanliness, effective separation of concerns and abstraction at a systems level are some of the things you can expect from a good PaaS implementation. Sometimes however, as the senior devs I mentioned pointed out, you give up control and certain levels of abstraction. However almost all senior devs understand that they want the ability to abstract at the levels that PaaS enables. They want to break apart the app cleanly at the system level from the software level. No reason for an app to know where or what a hard drive is doing right? *That’s a rhetorical question, onward with the topic…*

[**Docker**](http://www.docker.io/) has entered the market with a ***BOOM***, part of the abstraction level that enables PaaS tooling in the first place. This tool enables a team to jump into the code or to just deploy the tool to abstract at a PaaS level, but to build the elements that they need specifically. The components are able to be brought together in a composite way that provides all the advantages of PaaS, while put together specifically for the problem space that the team is attacking. For environments that don’t make cookie cutter apps that fit perfectly to PaaS tooling as it is, that needs that little bit extra control of the environment, Docker is the perfect tool to bring those pieces together.

So really, is Docker and containerization that new word (*from a technically old tech! lolz*), that new tech, that’s going to bring PaaS into the mainstream as the standard implementation? Is it going to make PaaS become containerization when we developers talk about it? It could very well be the next big step. It could be that last mile coverage that devs want to push environments into a PaaS Tech ecosystem and make full use of hardware, software and move to the next stage of application development. Could it? Will it?

Personally I’m ready for the next stage of the whole *PaaS thing*, are you?

Next up on other thought patterns, WTF are people using *Oracle for still when mariadb and postgres mean their freedom to innovate, move forward and surpass their competition*.
