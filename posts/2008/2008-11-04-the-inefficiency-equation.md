---
title: The Inefficiency Equation
date: 2008-11-04 02:15:00 +0000
last_modified_at: 2008-11-04 02:15:00 +0000
permalink: /2008/11/04/the-inefficiency-equation/
slug: the-inefficiency-equation
wp_id: 554
original_url: https://compositecode.blog/2008/11/04/the-inefficiency-equation/
categories:
- Uncategorized Bits
tags: []
excerpt: A developer goes to work. They arrive, sit down, and start right away at something. It could be e-mail, or a quick chat with coworkers, or a daily scrum. The coding begins and the interruptions start. Someone comes to ask a question, a server has failed, the build breaks, the code doesn't work as documented, …
---

A developer goes to work. They arrive, sit down, and start right away at something. It could be e-mail, or a quick chat with coworkers, or a daily scrum. The coding begins and the interruptions start. Someone comes to ask a question, a server has failed, the build breaks, the code doesn't work as documented, and the list of things goes on for stacks of paper.

How does a developer deal with this? It's an ongoing question. Everything from Six Sigma, Lean, to eXtreme or Scrum Agile Process all are designed around combating these issues along with many others. The question among all these processes and plans and other ideals is, "What percentage of time can we regain for a developer?"

I'm going to make a WAG and state that in most development shops today, that aren't utilizing effectively one of the methods mentioned above, 40% of a developers time is available to regain for productive use. Does that seem like a lot? I don't think so, because the amount of time in an average developer's day is really not spent doing development. Generally it isn't even spent solving problems they should be working on. The average developer, in the average developer's environment, spends a large percentage of their day just dealing with day to day operational needs; the build server, breaking the build, fixing the build, getting source code, checking it in, tracking bugs, bug fixes, eating lunch, communication about unrelated items that are causing work to stop, and on and on.

So how can these things be remedied? I'm going to cover a few ways, but from a purely toolset specific sense. The tools that a developer uses during the course of a day are extremely important to the efficient usage of time.

## Tool Integration

It is absolutely pivotal in today's development environment that at least the majority of the development tools integrate together in some smooth way. If the system wasn't so bug prone, Visual Studio Team Foundation Server would probably be the king of the stacks, but it isn't. However, Visual Studio is still one of the premier integrated development environments out there. With that one can use a number of other tools that integrate smoothly into the environment.

There should be, to gain maximum efficiency in time usage, a smooth integration between QA, bug tracking, unit testing, builds, build reports, project reports, and code statistics. There are a number of tools out there that perform these tasks admirably. The key though, is to get them to perform these tasks while integrated into the entire development process.

## Test Coverage, Regressions, and Black Boxes

Developers spend an inordinate amount of time trying to find where problems actually occurred. This is, to put it kindly, absolutely unacceptable in today's development environment. A developer should be able to pinpoint a bug in minutes. But a developer cannot be expected to do this without unit test coverage, regression test ability enabled by a high percentage of test coverage, and things being appropriately isolated into their respective black boxes.

Which brings me to one of my points of continued amazement of how many shops don't do legitimate unit testing. Many development shops spend 3-8x as much time in the fix cycle part of quality assurance and regression. Literally for every hour a solid team that has unit test coverage, clear separation of concerns and functional service isolation spends, other teams spend 3-8 hours. This IS NOT AN EXAGERATION! This is one of the largest elements in modern software development that needs pushed, unit testing is no longer an optional part of development.

***…short summary…***

Enough of me rambling on about this now. Between the two items above, that should decrease that 40% of time waste drastically. I'm not sure how much, but it is a huge step forward.
