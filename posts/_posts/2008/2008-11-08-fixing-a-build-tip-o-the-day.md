---
title: 'Fixing A Build :: Tip O'' The Day'
date: 2008-11-08 09:28:51 -0800
last_modified_at: 2008-11-08 09:28:51 -0800
permalink: /2008/11/08/fixing-a-build-tip-o-the-day/
slug: fixing-a-build-tip-o-the-day
wp_id: 559
original_url: https://compositecode.blog/2008/11/08/fixing-a-build-tip-o-the-day/
categories:
- Uncategorized Bits
tags: []
excerpt: The Scenario A Continuous Integration (CI) Build, which I’ll dub “Cib”, takes approximately 1 hr & 30 minutes. The build takes into account various builds from various platform technologies; Java, .NET, and PHP. The emphasis of course being that no single stack is available. To build the end solution all of these stacks need to …
---

## The Scenario

A Continuous Integration (CI) Build, which I’ll dub “Cib”, takes approximately 1 hr & 30 minutes. The build takes into account various builds from various platform technologies; Java, .NET, and PHP. The emphasis of course being that no single stack is available. To build the end solution all of these stacks need to be rolled into the build.

At a build time of 1 hour and a half, there is little ability to accurately watch the build, assure check ins work, or to be accurately notified of what is or is not being included in the build if numerous check ins are occurring.

What instead needs to occur is a short build. Builds in a CI environment really should not take a long time to compile, if they do, you really lose most of the CI benefit. So how long is acceptable? I’d prefer something around 5 minutes, not much more, and definitely less if possible. In most scenarios, no matter how big the project, this is possible. So what are the solutions?

Just to get a few ideas I spoke to a few guys at work about their ideas. Both Josh W. (*Code Recon & System Configuration Guru*) and Robert S. (*Build Management Ace*) gave me some good ideas. A few other conversations were had about what others had done in the past and two solutions came up the most preferred first steps.

## The Solutions

1. ***Split Em’ Up; Functionally, Technically, Departmentally, or However.***  The first thing in a multi-technology stack environment is to split up the individual builds. If need be split up various solutions into independent development teams functional segments. At some point, the solutions or projects would be broken down enough to have reasonable build times. These smaller segmented pieces are what should be setup for continuous integration. With that completed, then keep a single large, long running build as a daily build. Whatever the case, just leave it solely as a *build* versus a *continuous integration build*.
2. ***Autonomous Continuous Integration Builds.*** Setup the builds autonomously on the build server and monitor only the build or build(s) that you need for daily development. On [TeamCity](http://www.jetbrains.com/teamcity/index.html) this is super easy, probably is easy on VSTS, and I know it can be done with Cruise Control. It is important to monitor and be able to track any error that occurs during the segmented builds, specifically the one pertinent to a particular developers efforts.

***Summary***

I’m sure there are many other solutions. If you have any, please do leave a comment. Overall, the point is, continuous integration is NOT a long running build. At best, one could call that a scheduled build. A continuous integration build must be efficient and run in a reasonable amount of time. The safest range is between 2-5 minutes. Of course, less time is better.
