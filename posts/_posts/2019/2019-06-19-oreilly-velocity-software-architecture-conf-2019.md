---
title: 'TRIP REPORT: O’Reilly Velocity & Software Architecture Conf 2019'
date: 2019-06-19 19:35:20 -0700
last_modified_at: 2019-11-17 21:00:30 -0800
permalink: /2019/06/19/oreilly-velocity-software-architecture-conf-2019/
slug: oreilly-velocity-software-architecture-conf-2019
wp_id: 15894
original_url: https://compositecode.blog/2019/06/19/oreilly-velocity-software-architecture-conf-2019/
categories:
- Community
- Conferences
- TRIP REPORTS
tags:
- conferences
- devops
- edge compute
- san jose
- serverless
- velocity conference
excerpt: This past week the O’Reilly Velocity and Software Architecture Conferences took place. I’ve attended both before, the 2nd time for Velocity in San Jose and the 2nd time for Software Architecture, however this time in San Jose and the last I attended was in London. The locations for these conferences dictate much about what is …
image: /wp-content/uploads/2019/06/coaststarlight.jpg
---

This past week the [O’Reilly Velocity](https://conferences.oreilly.com/velocity) and [Software Architecture](https://conferences.oreilly.com/software-architecture) Conferences took place. I’ve attended both before, the 2nd time for Velocity in San Jose and the 2nd time for Software Architecture, however this time in San Jose and the last I attended was in London. The locations for these conferences dictate much about what is presented and how conversations, meeting and interacting, learning, and explorations take place during the conference, but more on those specifics in a moment.

The overarching theme from keynotes and many of the conversations I had met on a few key topics:

1. When you’re building software, and you want to do it well you first and foremost must, absolutely must, invest in the people building your software.
2. Focus on simplicity, remove complexity at every opportunity.
3. Organizational structure can have direct impact in the complexity or simplicity of software, structure your organization efficiently and make every effort to keep it simple.

**TLDR;** Keep your people happy, focus on simplicity, minimize organizational noise from bureaucracy.

## Topically Elaborating on Edge and Serverless

Ok, so a number of conversations came up around edge computing and serverless. Both interesting, but it also seems like there isn’t a strong play for the Enterprise is either space just yet. At this point however, a lot of enterprises are struggling with their Kubernetes, Cloud, and Hybrid solutions enough as it is that they haven’t even broached the edge compute and serverless realm. But that hasn’t stopped a lot of forward thinking individuals to start tackling how to cut out a useful spectrum of application with both edge and serverless.

### Serverless Oh My!

Serverless, like so many other names, is kind of a garbage name at first. It effectively tells us nothing useful. It’s a word that requires more words just to give it meaning. It’s kind of like if I said “I like food!” What does this even mean? So, everybody eats food and most people like it, so what does “I like food!” actually mean? Same with serverless, because the first thing it doesn’t mean is a system that has no servers. What it generally means is something about your applications and you not doing anything with servers. It’s the mythic NoOps by simply removing the computers somehow.

Serverless, or simply code that executes via compute, and you get a result, has actually been around for some time. There were a number of startups that were well ahead of AWS Lambda and the other respective implementations that Azure and GCP have. These startups had been attempting to usher in what it took AWS’s massiveness and clout to actually get people to pay attention to. Serverless however has gone far beyond merely Lambda at AWS and now we’ve got to contend not only with the option in the existing cloud providers but where, how, and when can we get it into our data centers! The TLDR is that enterprise wants serverless and they’re interested in throwing it onto Kubernetes or whatever they’ve got. But often the infrastructure and systems to really make use of this simply isn’t there.

Most of the conversations I had evolved around the who, what, where, when, and how do we make use of these options for what we do? This is where most companies, at least enterprise and large companies, currently seem to be in the market. Then there are the companies that have already made the leap and are doing all sorts of stuff with Lambda and related serverless offerings. The gulf, that middle ground, doesn’t seem to have been broached by many others. Everybody, anecdotally of course, seems to be either trying to figure out how to start or already made the leap!

### Edge Compute

This kept coming up, regardless of how or what people defined it as, it came up as something a number of people were very interested in. This notion, loosely based around using edge devices; smart phones, IoT devices, your car, or your washer for example, it could be almost anything. These devices do compute on the *edge* and thus the term. However it’s interesting because it isn’t like, for example, cloud computing that has core features like compute, storage, and related elements. Edge computing can run the gamut of any device doing any kind of work and the related capabilities of that device. It kind of leaves the space wide open. However, there were a few focal points that kept coming up.

The most common topic that came up around edge computing was doing tasks at point of presence. Such as having a phone do facial recognition, computing path finding (i.e. traffic directions), and related compute on the device versus round tripping it back to the cloud. It almost seems like after all these years of pushing things to the server we’re really starting in earnest to bring smart processes and tasks back to the devices we have in hand – no pun intended. It’s an interesting space, interesting paradigms, and I’m still not ready to call a specific thing within the world of edge compute and say, “that’s the next billion dollar idea”. Largely because, there are a lot of billion dollar ideas out there these days.

Speaking of edge compute and serverless, my fellow DataStaxian also had a few of these conversations on said topics. Patrick wrote up a post on a few observations over on the DataStax blog “[Velocity Conference Shows What’s Gaining Velocity in Data Management](http://Velocity Conference Shows What’s Gaining Velocity in Data Management)“.

## Geographic Location

As I mentioned, this set of conferences is in San Jose, the home of Silicon Valley, but the southern segment of the area. It’s a walk-able area with a number of places to break out from the conference and really dig into the *hallway* tracks (i.e. impromptu conversations!) that come up. For those willing to jump on the light rail, or scooter around, San Jose opens up even more to the local area providing a wide variety of coffee, food, and other operations to share conversations over.

All in all, the geographic location for the event is solid, being in the center of the city where it is. However one issue did arise, the Marriott lost power as an electrical fire in the control room of the multi-story hotel blew out the power. At last I checked upon leaving, it still didn’t have power! With the temperature at 105f going on multiple days at this point, the hotel because extremely hot inside, and being a kind of sealed airspace the air calculators also weren’t refreshing the air. That left a number of guests in less than stellar condition to attend, let alone attain value, from the conference events. Myself I ended up checking out in short order, getting sick the last day of the conference anyway, and being unable to provide the presentation that I had paired up with Lena ([@lenadroid](https://twitter.com/lenadroid)) for! I’ve been thinking, that maybe she and I can provide an online version of it for those that had wanted to hear us present on “[Flexible Cloud Architectures: Decision Making Best Practices](/confs-meetups-events/flexible-cloud-architectures-decision-making-best-practices/)“.

Next year’s Velocity looks like it’ll be in Santa Clara, which doesn’t really excite me as it’s kind of a nebula of sprawling suburbia of boredom. This is were location becomes fundamental to what will or what can be the potential of secondary and tertiary conversations at a conference like this. Don’t get me wrong, the hallway track is excellent, but having options to step out and walk across the street from the event to converse further adds a tremendous value.

Santa Clara simply doesn’t do that unfortunately.

The fortunate thing between now and then, albeit the conference is moving to Santa Clara, they’re having subsequent conferences in the Velocity series in Berlin, and Software Architecture Conf series in the amazing cities of New York and Berlin. Those locations are worth traveling to for far more than a conference, increasing my interest in attending both of those future events. I’m looking forward to these!

## Twitter Talk @VelocityConf

From [@DataStaxDevs](https://twitter.com/DataStaxDevs) a thread! Click through for all ~17 parts.

<blockquote class="twitter-tweet" data-dnt="true" data-width="550">
<p dir="ltr" lang="en">1⃣ Our first introduction to keynotes yesterday was by <a href="https://twitter.com/Adron?ref_src=twsrc%5Etfw">@Adron</a>, who threaded some live tweets for each keynote speaker.</p>
<p>Starting with <a href="https://twitter.com/GoldbergChen?ref_src=twsrc%5Etfw">@GoldbergChen</a> talking about scaling development like <a href="https://twitter.com/hashtag/k8s?src=hash&amp;ref_src=twsrc%5Etfw">#k8s</a>.<a href="https://t.co/0xrvPuBjLT">https://t.co/0xrvPuBjLT</a></p>
<p>— DataStax Developers (@DataStaxDevs) <a href="https://twitter.com/DataStaxDevs/status/1139305768224559104?ref_src=twsrc%5Etfw">June 13, 2019</a></p></blockquote>

<script async="" charset="utf-8" src="https://platform.twitter.com/widgets.js"></script>

Some Build Engineer Work – Click through for the whole construction thread.

<blockquote class="twitter-tweet" data-dnt="true" data-width="550">
<p dir="ltr" lang="en">Ok, <a href="https://twitter.com/jetbrains?ref_src=twsrc%5Etfw">@jetbrains</a> had some amazing swag. I took em' and put em to work! <a href="https://twitter.com/hashtag/velocityconf?src=hash&amp;ref_src=twsrc%5Etfw">#velocityconf</a> <a href="https://t.co/doBS9DI8DQ">pic.twitter.com/doBS9DI8DQ</a></p>
<p>— Adron (@Adron) <a href="https://twitter.com/Adron/status/1138999248702169088?ref_src=twsrc%5Etfw">June 13, 2019</a></p></blockquote>

<script async="" charset="utf-8" src="https://platform.twitter.com/widgets.js"></script>

### Some of the Keynote Threads

Alena Hall – [@lenadroid](https://twitter.com/lenadroid)

<blockquote class="twitter-tweet" data-dnt="true" data-width="550">
<p dir="ltr" lang="en">Next up <a href="https://twitter.com/hashtag/VelocityConf?src=hash&amp;ref_src=twsrc%5Etfw">#VelocityConf</a> keynote with HEEEYYY it's <a href="https://twitter.com/lenadroid?ref_src=twsrc%5Etfw">@lenadroid</a>! <a href="https://t.co/QOOEn0U9XW">pic.twitter.com/QOOEn0U9XW</a></p>
<p>— Adron (@Adron) <a href="https://twitter.com/Adron/status/1138860855414611968?ref_src=twsrc%5Etfw">June 12, 2019</a></p></blockquote>

<script async="" charset="utf-8" src="https://platform.twitter.com/widgets.js"></script>

Jessica Kerr – [@jessitron](https://twitter.com/jessitron)

<blockquote class="twitter-tweet" data-dnt="true" data-width="550">
<p dir="ltr" lang="en">Next <a href="https://twitter.com/hashtag/VelocityConf?src=hash&amp;ref_src=twsrc%5Etfw">#VelocityConf</a> keynote is <a href="https://twitter.com/jessitron?ref_src=twsrc%5Etfw">@jessitron</a>!!! <a href="https://t.co/TLm3vAqTCN">pic.twitter.com/TLm3vAqTCN</a></p>
<p>— Adron (@Adron) <a href="https://twitter.com/Adron/status/1138846865569374210?ref_src=twsrc%5Etfw">June 12, 2019</a></p></blockquote>

<script async="" charset="utf-8" src="https://platform.twitter.com/widgets.js"></script>

…and there were a bunch of others too, solid, check out the hash tag of #velocityconf to read up on more.

### **The Lagniappe**

After the conference I finally managed to pick up a pocket Constitution.

<blockquote class="twitter-tweet" data-dnt="true" data-width="550">
<p dir="ltr" lang="en">Pocket sized highly recommended. <a href="https://t.co/NX0iXZPsuV">pic.twitter.com/NX0iXZPsuV</a></p>
<p>— Adron (@Adron) <a href="https://twitter.com/Adron/status/1140409536991260672?ref_src=twsrc%5Etfw">June 17, 2019</a></p></blockquote>

<script async="" charset="utf-8" src="https://platform.twitter.com/widgets.js"></script>

If you’re ever in search of good coffee in San Jose, one place I found that’s tops is Academic Coffee, both the coffee and service are great. Good jovial crew and lots of cyclists in and out.

<blockquote class="twitter-tweet" data-dnt="true" data-width="550">
<p dir="ltr" lang="en">Found another happy place in San Jose. Academic Coffee… <a href="https://t.co/9oJLTP8i0m">pic.twitter.com/9oJLTP8i0m</a></p>
<p>— Adron (@Adron) <a href="https://twitter.com/Adron/status/1138461039798890496?ref_src=twsrc%5Etfw">June 11, 2019</a></p></blockquote>

<script async="" charset="utf-8" src="https://platform.twitter.com/widgets.js"></script>

Making progress on the CaSMa, tweeted a bit on the topic while en route to the conference. If you’d like to get involved, please do let me know!

<blockquote class="twitter-tweet" data-dnt="true" data-width="550">
<p dir="ltr" lang="en">building a logo &gt; <a href="https://t.co/yngeNIKC3a">https://t.co/yngeNIKC3a</a></p>
<p>Help with the build for cross-play<a href="https://t.co/kdo7PwHHdt">https://t.co/kdo7PwHHdt</a></p>
<p>— Adron (@Adron) <a href="https://twitter.com/Adron/status/1138478873388077056?ref_src=twsrc%5Etfw">June 11, 2019</a></p></blockquote>

<script async="" charset="utf-8" src="https://platform.twitter.com/widgets.js"></script>

***Other arbitrary statistics:***

- Stickers collected: 11 unique, ~7 of each. Total: 77 stickers.
- T-shirt Swag: 2.
- Conversations @ DataStax Booth: 11
- Hallway Track Conversations: 7
- Coffee Consumed: 9 over 3 days.
- Twitter Filters Discussed: 123.
- Fuel burned to compensate for electrical fire damage for the time of the conference: Approximately 5k gallons of fuel for the Marriott Hotel and no idea how much more fuel was or is still being burned to power the hotel.
- Times the power still went off even with the diesel engine power trailer attached: 4.
