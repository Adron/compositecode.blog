---
title: Team Foundation Server "mucking"
date: 2006-10-22 08:59:13 +0000
last_modified_at: 2006-10-22 08:59:13 +0000
permalink: /2006/10/22/team-foundation-server-mucking/
slug: team-foundation-server-mucking
wp_id: 535
original_url: https://compositecode.blog/2006/10/22/team-foundation-server-mucking/
categories:
- Uncategorized Bits
tags: []
excerpt: Back after a few weeks of not touching Team Foundation Server my fellow techie and I went geek this weekend to figure out how to remove, update, and replace the exiting “test” projects. Needless to say, this was no cakewalk. Microsoft, did you hear that? It wasn’t a cakewalk, it was confusing, frustrating, and somewhat …
---

Back after a few weeks of not touching Team Foundation Server my fellow techie and I went geek this weekend to figure out how to remove, update, and replace the exiting “test” projects.  Needless to say, this was no cakewalk.  Microsoft, did you hear that?  It wasn’t a cakewalk, it was confusing, frustrating, and somewhat annoying.  Now I’m sure 80% of the confusion was from us just arbritrarily setting up the server and trying to toss stuff into it and not really following any particular method.  But we did that because most of the time this is the exact process that a dev group will take with a new product.  Thus it just gets thrown together with no real reason beyond a proof of concept.  So the following is the list of trials and tribulations we had to go through to get this puppy running with the big dogs.

- **First lesson**.  Team Foundation Server shouldn’t be installed on a Microsoft Virtual PC Server unless you have serious hardware.  Don’t ask me why, I don’t know, but the server gets really slow when it is on a Virtual PC.
- **Second Lesson**.  Don’t just haphazardly add projects and solutions into the source control repository.  This is a bad practice.  All developers, repeat this, there must be a project/solution plan for adding source to source control.  There must be a project/solution plan for adding source to source control.  There must be a project/solution plan for adding source to source control.  The number of ways one can add to source control, from the number of ways one can set their native paths, to the number of places the projects and solutions are saved into source control are so numerous that if everyone takes a different approach a dev team runs a very *high risk* of ending up with the “It runs fine on my machine” scenario.  Besides that, everyone on the team then knows where everything is.
- Third Lesson.  If you need to remove a project or solution from a Team Foundation Server “Project” it is often times no easy matter.  First you must make sure your mappings are correct and in place for the project or solution to be deleted from Source Control.  When you right click the delete option will then show properly.  For some reason we had to learn this the hard way because our solutions/projects we added where never mapped appropriately.  Once a project/solution is deleted you must then “check in” these changes so that the project/solution actually goes bye bye.

At this point these are our primary lessons we’ve learned.  Next on the to do list is to create task lists, prepare reporting, and figure out the various queueing mechanisms and build process.
