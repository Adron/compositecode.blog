---
title: PDX Cloud – A Question Posed.
date: 2013-10-11 17:39:24 -0700
last_modified_at: 2013-10-11 17:39:24 -0700
permalink: /2013/10/11/pdx-cloud-a-question-posed/
slug: pdx-cloud-a-question-posed
wp_id: 9003
original_url: https://compositecode.blog/2013/10/11/pdx-cloud-a-question-posed/
categories:
- Cloud Speak
- Community
- Meetups n' Such
- Presentations and Speaking
tags:
- cloud
- cloud computing
- distributed systems
- software
- software development
- vertical systems
excerpt: I attended the PDX Cloud meeting to present, but more to ask a question. Here’s how I posed that question (slide deck at the bottom of this blog entry). I frame the scenario of the distributed development world of cloud computing, dive into the vertical world of enterprise dev and then throw down the big …
---

I attended the PDX Cloud meeting to present, but more to ask a question. Here’s how I posed that question (slide deck at the bottom of this blog entry). I frame the scenario of the distributed development world of cloud computing, dive into the vertical world of enterprise dev and then throw down the big question…

![](https://photos.adron.me/Software/Meetups-N-Conferences/PDX-Cloud/i-nhvvVbB/0/M/SITREP-M.png)

This is a situational report on the current state, of the somewhat bi-polar condition that exists in software development right now. This is reflective of my train of thought around a number of aspects of the industry and what questions have come up time and time again while working with fellow coders and technologists.

![](https://photos.adron.me/Software/Meetups-N-Conferences/PDX-Cloud/i-m6gZvdh/0/M/SITREP%281%29-M.png)

The first segment of the industry that we often here about. it’s the hip and cool thing to do, as well as the obvious path into the future right now. It’s not particularly the idea that this segment, of building things as distributed systems is new, it’s just that it has become more important and more capable now than it ever has in the past.

![](https://photos.adron.me/Software/Meetups-N-Conferences/PDX-Cloud/i-b3MK4bH/0/M/SITREP%282%29-M.png)

A lot of this has to do with the advent of key technologies around virtualization, cloud computing and large scale object storage and network capabilities. We can spool up enough compute to rival a super computer, sitting alone at home, to storing more data than we can imagine with zero theoretical limit to that storage. All of this networked together behind load balancers, switches and programmable devices that a mere half dozen years ago would have taken more resources than any reasonably sized small business could even afford. All of these capabilities are literally at our fingertips now.

![](https://photos.adron.me/Software/Meetups-N-Conferences/PDX-Cloud/i-rCx3km4/0/M/SITREP%283%29-M.png)

I’ve spooled up a 1000 EC2 instances for a demo before. That was 2 years ago even! Now I as well as many host applications and databases entirely in memory. SSDs as a cloud back end option at AWS and other locations provide another avenue that brings these devices into a world where they can be utilized immediately. Blink an eye, you’ll have the resources.

![](https://photos.adron.me/Software/Meetups-N-Conferences/PDX-Cloud/i-c7GZzMx/0/M/SITREP%284%29-M.png)

The storage realm, with costs falling through the floor with Glacier to operationally effective options like S3, EBS, Table Store, Object storage and others make our junk trunks limitless. The option to throw away any data at all seems less and less appealing.![](https://photos.adron.me/Software/Meetups-N-Conferences/PDX-Cloud/i-7mbZ3JR/0/M/SITREP%285%29-M.png)

Many developers, but definitely not all, have seized opportunities to alter the way they work and what they’re able to accomplish by using these new capabilities. From the now common asynchronous approach to development, shifting languages and stack to the invention of new paradigms around development and operations into a devop practice, leadership has stepped up to this changing game.

![](https://photos.adron.me/Software/Meetups-N-Conferences/PDX-Cloud/i-ksnWkpv/0/M/SITREP%286%29-M.png)

Vertical systems have in the past twenty years held the main position in the enterprise as the go to architectures. Client server or three tier or whatever one may call it. With a synchronous mindset the vertical implementation of systems produced several benefits.

![](https://photos.adron.me/Software/Meetups-N-Conferences/PDX-Cloud/i-5GRbj6C/0/M/SITREP%287%29-M.png)

We gained the ability through diligent documentation and widget style architecture to build CRUD (Create Read Update Delete) and LOB (Line of Business) applications at a rapid rate. With a simplified approach like this businesses spent a lot of time focusing on their business, not particularly on efficient utilization of resources, processing or reliability. But who could blame them, with Moore’s Law it seemed the only real ways to scale vertical systems were by writing faster code or buying a bigger computer, for a while that seemed to work fine.

![](https://photos.adron.me/Software/Meetups-N-Conferences/PDX-Cloud/i-FRc323S/0/M/SITREP%288%29-M.png)

Most of the, what I’ll call “vertical revolution” happened with the GSD mindset. GSD mean **G**et **S**hit **D**one. Again, another idea that sort of worked pretty well as long as Moore’s Law was in effect. But things have started to change, with Moore’s Law faltering.

![](https://photos.adron.me/Software/Meetups-N-Conferences/PDX-Cloud/i-BLmFWp5/0/M/SITREP%289%29-M.png)

Management practices also became a complete TLA soup during this time. The last 20 years continued the standard “let’s cookie cut people into widget producers”. It never works as well as it could or should, but the industry – and really all humanity keeps trying – to do this anyway. This is fine, we’ve got to try. The vertical stack however brought this to the extreme forefront as the industry tried to shoe horn all sorts of development into singular types of management practices.

![](https://photos.adron.me/Software/Meetups-N-Conferences/PDX-Cloud/i-9j8jXRd/0/M/SITREP%2810%29-M.png)

Overall though as long as things stayed simple, we stuck to our KISS principles as software craftspeoples the architecture stays straight forward enough and the stack stays easy. However there are voluminous limitations. There are massive management and project issues with all of this.

![](https://photos.adron.me/Software/Meetups-N-Conferences/PDX-Cloud/i-rsW4qfM/0/M/SITREP%2812%29-M.png)

Many parts of the industry are screaming for the future. As we have it, some agree on certain aspects of what the future should be and others agree on other aspects of the future.

![](https://photos.adron.me/Software/Meetups-N-Conferences/PDX-Cloud/i-BFbct6h/0/M/SITREP%2813%29-M.png)

We have some bright spots amid the confusion that is making the distributed world much easier, and the technology continues to do this.

![](https://photos.adron.me/Software/Meetups-N-Conferences/PDX-Cloud/i-v6wf938/0/M/SITREP%2815%29-M.png)

Some want convergence. Which may work well in some ways, but in others it is converging into a clustered mess. As with the roadways of the 50s and the effervescent ideas of 50s planners, we’re finding the idea of the superhighways aren’t working either. The same is starting to appear for some types of device convergence. So where does this really leave us? Where are our weak spots as an industry? It seems like right now we’re stuck in that traffic jam getting to the next step.

![](https://photos.adron.me/Software/Meetups-N-Conferences/PDX-Cloud/i-zrdg5SP/0/M/SITREP%2816%29-M.png)

Things are looking a little like this freakingnews.com MAV. Multifunction and not functional at all.

![](https://photos.adron.me/Software/Meetups-N-Conferences/PDX-Cloud/i-ft8M3Rj/0/M/SITREP%2817%29-M.png)

So to gain clarity on direction I pose the question…

- How do we change the later world to work as well as the new world of distributed systems?

…and a few follow ups.

- What do developers in the industry need to make true distributed computing advances while drawing on the known elements of the vertical computing realm?
- What do we need as developers and leaders to more reliably advance the industry without setbacks?
- What do we need as leaders to move the industry forward to the next steps, stages and developments in converging technology?
- Are these even valid questions? What would you propose to ask?

<iframe allowfullscreen="allowfullscreen" allowtransparency="true" frameborder="0" height="485" id="talk_frame_70662" loading="lazy" mozallowfullscreen="true" src="//speakerdeck.com/player/18455a9014fa01318f20625d551e99d4" style="border:0; padding:0; margin:0; background:transparent;" title="SITREP" webkitallowfullscreen="true" width="863"></iframe>
