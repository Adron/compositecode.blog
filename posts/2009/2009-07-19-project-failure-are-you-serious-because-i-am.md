---
title: Project Failure? Are You Serious? Because I Am!
date: 2009-07-19 15:32:51 +0000
last_modified_at: 2009-07-19 15:32:51 +0000
permalink: /2009/07/19/project-failure-are-you-serious-because-i-am/
slug: project-failure-are-you-serious-because-i-am
wp_id: 656
original_url: https://compositecode.blog/2009/07/19/project-failure-are-you-serious-because-i-am/
categories:
- Uncategorized Bits
tags: []
excerpt: Beware, this is a LONG entry and if you don’t read all of it you may end up offended, but rest assured what I’m writing here is the absolute truth and recruiters, project managers, project leads, development leads, developers, and anyone getting into the software industry or that has been in the industry I have …
---

> ***Beware, this is a LONG entry and if you don’t read all of it you may end up offended, but* *rest* *assured what I’m writing here is the absolute truth and recruiters, project managers, project leads, development leads, developers, and anyone getting into the software industry or that has been in the industry I have many points of advice and warning.***

I was recently hanging out with one of my friendly local tech recruiters over a drink or three and some good food.  They asked me to proof their position they where about to post.  As I am a friendly guy, I decided I would.  It has been a LONG time since I’ve looked at a post like this, as I haven’t actually used Monster, Dice, or any of those sites in a rather long time.  Maybe I’ve thought the industry had matured a bit sense I last checked the pulse.  Being in Portland where the industry is generally about 5-10 years ahead of the rest of the country (and the world for that matter) I am always hopeful.  Here are some snippets from the post and an immediate translation.

Under the required skills section I saw a couple of points;

- *Creation of automated unit test cases.*
- *Automated builds*
- *Ability to manage multiple projects and tasks simultaneously.*
- *Dedicated to completing assigned tasks on time.*

Under the preferred skills and characteristics where some more real gems, but this one just stood out.

- *Willing to work overtime, holidays, and weekends as requested by management.*

My first response when looking at this was, "are you serious?  you really expect someone to take this job?  It has abusive environment and poor conditions all over it!!!!"  I was seriously shocked, after all these years, and maybe I just don’t read job requirements much anymore and there are tons this crappy.  So let me elaborate a little more on this description.

First off, just from those descriptions the position looks aberrantly abusive, environmentally (i.e. work environment) bad, and probably psychologically torturous for a software developer.  Maybe I’m wrong, but whoever decided to put these requirements in the post is looking for either *A:* someone who is desperate for work and will last for a very short time under the abuse or *B:* someone who is already sadomasochistic and loves the pain of the torture.  There are amazingly software developers like that.

Now I have to pick apart some of these.  "***Creation of automated unit test cases.***"  This immediately tells me a couple of things;

- There are some tests, they are NOT unit tests if this has been slammed into a requirement spec for automated tests cases.
- There are so many contradictory words in this request that it just doesn’t make any actual logical sense.
- Unit tests are isolated, often used during refactoring, not always during automation.  Automation tests are not particularly unit, often are integration tests, and aren’t really used during refactoring but instead during QA.
- "Cases", well cases just hangs there as if Agile Processes & Waterfall Processes are having a subversive fisticuffs fight right after the specs are finished.  Whatever the "case" this requirement only really shows one thing, some type of testing is required, and the prospective candidate won’t know what kind and it appears nor does the person writing the requirement.

Let us hit on the next statement.  "***Automated Builds***".  Ok, this one sounds like a legitimate requirement.  But stop a second and think about it along with the other requirements.  Is it logical with the others or does it exacerbate the other requirements by its simple specification?  Considering people these days people are doing CI, continuous integration, along with automated builds it leaves me with this thought that someone hasn’t modernized the build process for a long while.  With that said it leaves me to this next specification and the point I want to make.

"***Ability to manage multiple projects and tasks simultaneously***" is a beauty.  That’s the spirit for destroying any good velocity and productivity a developer might have, interrupt them a lot and give them multiple tasks all at once!  If it is a contract position, one would probably want the hire to stay productive on task, if it is a permanent position you might want them to handle multiple efforts.  However stating this immediately, before any discussion or interview is made with an individual this specification should leave a developer with the inherent fear that the project, whatever it may be, *IS BEING MANAGED POORLY*!  This is a massive, glaring red flag.  Sure, most projects these days are probably running through rough spots, but don’t chase away the smart talent before the position even gets a glance at by the top talent.  I can promise you the top talent will look at this, and think, "well maybe they can hire me as a consultant to get them back on track, but I’m not going into the trenches because it already sounds like a "[death march](http://www.amazon.com/Death-March-Developers-Surviving-Impossible/dp/0130146595)" with many "[mythical man months](http://en.wikipedia.org/wiki/The_Mythical_Man-Month)" being consumed.

"***Dedicated to completing assigned tasks on time***" is always a hilarious thing to read.  This should be translated to "*working insane hours to get tasks done based on a schedule that you have not be consulted on, or at least ignored after you?re consulted, and then getting reprimanded because you didn’t finish a task that has been mismanaged from the beginning!*"  This specification is probably the biggest alarm of them all.  This specification almost immediately should tell a prospective candidate that the project, or project(s) are probably being mismanaged.  If the project has had so many problems as to need to put ?dedicated to completing?" in the specification as a point there are problems.

Now someone might read this and think, "but it sounds like a good trait" and I’ll state simply that it is a very good trait in a developer.  I can tell you with high confidence, developer’s absolutely have this trait but are often put in circumstances that they can’t meet deadlines.  I can also say with high confidence that probably 80% of the time a task is not met by a deadline it is not the developer’s fault, it is the planning process & management that is in place.  Mind you, 80% is a conservative estimate, a more accurate number would probably be in the 90% range.  Developer’s want to create, design, developer, and do good work. Developer’s are not your McDonald’s employees, these people are highly skilled.  Even the weakest developer is likely to want to get things done, but if the leadership has mismanaged the project, they’ll then have to fail.  It is a sad situation that it is so often this way, but that’s the cookie crumbling.

The last one anyone can see is a major red flag.  "***Willing to work overtime, holidays, and weekends as requested by management***".  If this where a contract position, that is a command to abuse the hours ? spend a ton of em’ and bill em’ because you know, just from this requirement that you’ll have to anyway.  If it is a permanent position, this is really bad news for the developer.  Right from the get go a developer should look at this and realize their social life, their
love life ? if they have one, marriage, or whatever else is about to go down the drain.  If something like this is in a job profile specification then you can bet money, that you’ll be expected to and will have to work ridiculous hours.

With all the other specifications combined the sad fact is that you’ll probably be stepping directly into a project death march from day one.  Simply put, this project, whatever it is will fail with about a 90% chance on delivery date and cost.

# The Awesome Shiny Good News Out of All This!

There are ways that everyone in this scenario can get things straightened out (and no, I’m unfortunately not available right now I’m happily employed ;p ).  Here are the first 9 steps to getting things going in the right direction and staving off the death march and immanent failure.  I would have written up the first 10, but that seems touch?!

1. Get existing members into a room that are involved in this project and show them this specification.  Then throw away the specification and dig deep to find the GOOD PARTS of the project that might make it fun and exciting to a prospective candidate!
2. Immediately toss as much Waterfall Methodology in the dumpster out back ***AS FAST AS YOU CAN***!  Read up immediately on Agile, lean style, scrum style, anything of that sort.
3. This one will be painful for the project managers, but do it if you want to succeed.  Throw away the gantt charts and project plans, if you don’t you’ve already failed the software development effort.
4. Sit down and create some stories about what this software has to do.  Talk to the users and get it straightened out, look at the components that might need to communicate.  Bring in all the key stakeholders again and tell them the project is at ***RISK.***
5. Find ways to get happy developers, existing and future.  If you don?t have happy developers you WILL NOT have a solid, reliable, quality product or service in the end.
6. Either figure out your burn down chart or your iterations, get stories lined up for the next steps ? i.e. the ones in the immediate next week or two and DO NOT start putting stories on a scheduled chart or out past the 2nd or 3rd iteration.
7. Get a steady velocity, stop abusing the developers, stop working overtime at every opportunity.  Overtime slows down a project, don’t tell me you have to because there isn’t enough time because you’re perpetuating the lie that OT will build a product.  Steady, consistent, happy, clear thinking developers get a product built.  Some OT might happen, but get it the hell out of a job specification and reduce it to a minimum on the job.  You want developers that want to do a little extra, not developers that feel slave driven.
8. Make sure the teams eat lunch, communicate, get to know who everyone is, and can deal with their respective team members traits and can communicate.  Without effective and regular communication nobody is going to finish anything on time, let alone of high quality.
9. Seriously, go have a beer/beverage/cold drink or something with the team and get things out in the open.

Ok, so there are a ton more steps.  There are things that come after this, that come after the project is repaired, and even after that.  But this is the simple start to correcting the problems.  I really hate seeing projects fail, I HATE seeing projects fail because often, there is no reason for it.  Almost every project I see that fails is because of the dumbest list of reasons;  fear, bad management, Waterfall, miscommunication, and others.  The wicked thing is, every single one of these reasons has a solution that humanity in its everyday project endeavors has resolved!  We as human beings have the knowledge, out there, we just have to search for it and find it and know it!  So many projects don’t have to fail!

So get to it, and I hope everyone that reads this can straighten out their projects and add to the list of successful projects, instead of outright failures.
