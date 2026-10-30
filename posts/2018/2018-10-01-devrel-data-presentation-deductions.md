---
title: 'DevRel Data: Presentation & Deductions'
date: 2018-10-01 10:55:49 -0700
last_modified_at: 2018-10-01 10:55:49 -0700
permalink: /2018/10/01/devrel-data-presentation-deductions/
slug: devrel-data-presentation-deductions
wp_id: 14688
original_url: https://compositecode.blog/2018/10/01/devrel-data-presentation-deductions/
categories:
- Ideas
- Lists of Stuff
- My Updates
- PSA
- Teaching Training Mentoring Lecturing
tags:
- activism
- advocate
- coding
- content creation
- developer
- developer advocate
- developer evangelist
- Developer Relations
- devrel
- Evangelists
- programming
- software
- software development
excerpt: Before diving into conclusions, let’s take a look at some answers to questions asked. This is a slice of answers, with totals for the charts and such. After a few months of answers I’ll have another follow up to see how things may or may not change. Do you like video material? What specifically do …
---

Before diving into conclusions, let’s take a look at some answers to questions asked. This is a slice of answers, with totals for the charts and such. After a few months of answers I’ll have another follow up to see how things may or may not change.

***Do you like video material?***

![chart](/wp-content/uploads/2018/09/chart.png)

***What specifically do you, or would you like to watch in video? Screencasts, short videos, conversational, or some other type of videos?***

- Screencasts/tutorials
- I love both screencasts going through big topics and short videos that cover smaller tips and gotchas.
- Videos with a specific outcome as the goal, whether achieved or not. Showing the process of something.. like hey, here’s how you building out a Postgres cluster using streaming replication and repmgr and pgpool… Kind of thing.
- Bite sized content, maybe 2 minutes, to teach me one thing.
- Editing. No jokes, no “hey what’s up guys” with 60 second intros. Discuss the problem, then solve it.
- Demos, learning a new way of doing something
- Doesn’t matter short or long, but has to be deeply technical with code examples that I can actually apply
- I watch videos mostly for fun.
- Screencast
- Short videos of say 5-10 minutes each covering different concept of the subject matter
- (videos work best in a classroom setting where time/attention is precommitted, or as part of a tutorial)
- conversational
- Short videos.
- If it’s too long, it ends up on my todo list forever (not good). So shorter is better. And something that benefits from visuals, rather than something that could just be written.
- I also watch LinkedIn Learning when just starting a new tech. to get a general overview and pick up a tip or tow, then I read books and the Internet from there.
- short videos

***What kind of written material do you like?***

![chart2](/wp-content/uploads/2018/09/chart2.png)

***Do you like other material mixed in that details the reason for the tech, the story, or such?***

![chart3](/wp-content/uploads/2018/09/chart3.png)

***Is there anything that comes to mind, that you’d like to have me or the team I’m working with (@ DataStax) put together that you’d find useful, entertaining, or related.***

- Place priorities on designing materials for more depth (i.e., more linked material) as well as less attention-nuisance. That’s no criticism of your work, merely the gestalt of where we work — so less noise is a better way to stand out and make materials useful.
- Maybe focus more on written material – code & architecture material (books, articles) rather than videos and twitch. It is much easier to consume and is easily googlable. Also I’d suggest making blog posts target a specific common issue or question – sometimes I see posts that I don’t really care about or the problem is so narrow that I don’t want to read about it. I’d read about building resilient and highly available architectures in various configurations.
- Database reliability, scalability, migrations and such stuff is interesting.
- Anything to do with machine learning.
- Data model examples, starting up a Cassandra node, configuring YAML, etc

# Deductions

I’m going to go backwards through the questions and discuss what I’ve deducted, and in some ways what has surprised me among the answers!

First there’s the “***Is there anything that comes to mind, that you’d like to have me or the team I’m working with (@ DataStax) put together that you’d find useful, entertaining, or related.”*** request and questions.

The answers here didn’t surprise me much at all. Within DevRel from Microsoft to DataStax to Google to many other organizations we have this ongoing battle between “write a whole book on it” or “make it 2 minutes short”. It’s wildly difficult to determine what format, what timing, and what structure material needs to be in for it to be most useful to people. So when I saw the answer that reads, “Place priorities on designing materials for more depth (i.e., more linked material) as well as less attention-nuisance.” I immediately thought, “yeah, for real, but ugh…” it’s difficult. However, I’m working on more thorough material, some of it will be paywalled via LinkedIn Learning or Pluralsight and other material may be available by book in the coming months. But there will be other material that will indeed be long form how to material on how to really put things together – from scratch and from the basis of “we have X thing and need to hack it so we can add a feature”.

The next answer I got in this section that I completely agree with is increasing the focus on written material. I’m making tons of video, and I’ve got that down to the point where it’s actually easier and faster to do most of it then it is to write things down. However I realized, especially from my own point of view, that written material actually ends up being vastly more useful than video material. That’s also why, even with the video material, when I’m covering specifics I aim to provide a linkable timeline and a blog entry with the code and other changes shown in the video. Thanks for reinforcing these efforts and giving me that indirect encouragement to make this process and the results even better. More written material is on its way!

As for the database reliability, scalability, migrations, machine learning, data modeling, Cassandra node starting, and all that it’s in the queue and I’m getting to it as fast as I possibly can.

Next question I asked is, “***Do you like other material mixed in that details the reason for the tech, the story, or such?***”

It appears, albeit not a huge contingent of people, some people are curious about biking, train coding, and making good grub! Hey, that’s groovy cuz I’ve got a show coming out which is basically the behind the scenes videos about all those topics that make the coding and technology hacking possible!

The one outlier in this set however is clearly the request for “*Ways to simplify life to dig through those algorithms faster, easier, better?*” which I didn’t suspect would be any different then the other answers for this questions. Which left me surprised and ill-prepared on what to do about fulfilling what is clearly a demand. I’ll have to up level my blog posts around algorithms. I did do a couple a long while ago now in “[Algorithms 101: Big Sums](/2018/01/06/algorithms-101-big-sums/)” which I completed in Go and another I wrote up “[Algorithms 101: Roads & Town Centers](/2018/01/31/algorithms-101-roads-town-centers/)” which I have 90% of the answer complete but I’ve never finished the blog entry! I guess it’s time to get the algorithm train coupled up and ready to depart!

Then the question, “***What kind of written material do you like?***”

Two options lead by a healthy margin for this question: *Demos w/ Write Up* and *Blog Articles*. With this coupled up to the first question it’s clear that written material via blog and demoes via blog should and ought to be top priority. They are, however they’re a whole helluva lot of work, so I only get them produced but so fast. Got some gems coming on Go, Bash, Cassandra, and a few other demo, tech, and historical information.

Next up was *single page cheat sheets* and *documentation*, followed closely by *books*. I kind of expected documentation and books, but wow that single page cheat sheets option is higher rated than I would have suspected and by proxy I’ve immediately added that to my *produce this type of material* list! I put it in as a very secondary thought but it’s going to get into that increased focus queue.

The last one with some semblance of demand is pamphlet size short form. This one almost seems like a fluke, but I’ll ponder putting together some of these. I know O’Reilly has their short novelette size books which cover a particular topic. They hand these out for free at conferences and seem pretty solid. Maybe I’ll work one of those into the queue? Maybe.

The other three options scraped by with 1%, so somebody was choosing them. So the vi mug isn’t a priority nor the short explainer videos. Which seems in contention with video content demands around shorter content. I guess, explainer videos just doesn’t sound useful!

The next question I just put together a top three of the results, “***What specifically do you, or would you like to watch in video? Screencasts, short videos, conversational, or some other type of videos?***”

1. Make screen casts.
2. Make screen casts generally short.
3. Make screen cases that are short and on a specific and deep dive into a topic.

This seems kind of in conflict with itself, but I’m going to aim for it and try to hone the skill further. So that I can produce screen casts, screen casts that are generally short, and make sure that these screen casts that are short are on a specific and deep dive into a topic. Whew, got it.

Finally, “***do you like video material?***”

![chart](/wp-content/uploads/2018/09/chart.png)

At this time, 53.8% of you have said yes. I had guessed it would be around 50%.

I had guessed no would be about 25%, and at 23.1% I wasn’t to far off.

The other respective mishmash of answers made for interesting depth to the questions that followed this question.

# Article Summary & TLDR

> ***Produce more topic specific, detailed material around screen casts and blog entries!***

*End of story.*

For more on this information, why I asked, and what I do check out my article titled “[Evangelism, Advocacy, and Activism in The Technology Industry](/2018/08/15/evangelism-advocacy-and-activism-in-the-technology-industry/)” and for some of the big victories for big corporations check out “[The Developer Advocates – Observations on Microsoft’s New Competence](/2017/09/30/the-developer-advocates-observations-on-microsofts-new-competence/)“.
