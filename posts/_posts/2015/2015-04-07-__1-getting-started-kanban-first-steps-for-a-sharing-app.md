---
title: __1 “Getting Started, Kanban & First Steps for a Sharing App”
date: 2015-04-07 07:15:00 -0700
last_modified_at: 2015-04-06 12:41:31 -0700
permalink: /2015/04/07/__1-getting-started-kanban-first-steps-for-a-sharing-app/
slug: __1-getting-started-kanban-first-steps-for-a-sharing-app
wp_id: 10790
original_url: https://compositecode.blog/2015/04/07/__1-getting-started-kanban-first-steps-for-a-sharing-app/
categories:
- Architecture
- Code Stories
- How-to
- Node.js Things
- nodejs
- ThrashingCode
tags:
- javascript
- node
- node.js
- nodejs
- thrashing code
- thrashingcode
excerpt: This is the first (of course the precursor to this entry was the zero day team introduction article) of an ongoing series I’m going to put together. I’m going to write this series from the context of a team building a product. I’ll have code samples and more as I work along through the material. …
image: /wp-content/uploads/2015/03/cut2.jpg
---

This is the first (of course the precursor to this entry was the [zero day team introduction article](http://#)) of an [ongoing series](http://compositecode.com/docs/thrashing-code-projects/) I’m going to put together. I’m going to write this series from the context of a team building a product. I’ll have code samples and more as I work along through the material.

The first step included [Oi Elffaw](https://github.com/OiElffaw) having a discussion with the team to setup the first week’s working effort. Oi decided to call it a sprint and the rest of the team decided that was cool too. This was week one after all and there wasn’t going to be much else besides testing, research, and setup that took place.

## Prerequisites

Before starting everything I went ahead and created a project repository on github for Oi to use waffle.io with. Waffle.io is an online service that works with github issues to provide a kanban style inferface to the issues. This provides an easier view, especially for leads and management, to get insight into where things are and what’s on the plate for the team for the week. I included the default node.js .gitignore file and an Apache 2.0 license when I created the repository. Github then seeds the project with a .gitignore, README.md and the license files.

After setting up the repository in github I pinged Oi and he set to work after the team’s initial meet to discuss what week one would include.

## Getting Waffles

Oi’s first task was getting everyone setup with [waffle.io](https://waffle.io/) for kanban management. Navigating to the waffle.io page presents us with some options to login, and when doing so there will be an option around login with access to public repositories or private repositories. Each of the options, giving that level of access to the waffle.io service.

[![waffle.io](https://photos.adron.me/photos/i-XtsXsZ7/0/O/i-XtsXsZ7.png)](https://photos.adron.me/photos/i-XtsXsZ7/0/O/i-XtsXsZ7.png)

*waffle.io*

As soon as each team member signed in they could then add a project as shown below.

[![Adding a Board](https://photos.adron.me/photos/i-62hTNQ7/0/X2/i-62hTNQ7-X2.png)](https://photos.adron.me/photos/i-62hTNQ7/0/X2/i-62hTNQ7-X2.png)

*Adding a Board*

When Oi clicks on the green plus button the projects display below like this. Once can then be selected to view by merely clicking on that project in the future.

[![Selecting a Project to make a Board for.](https://photos.adron.me/photos/i-8NvGnhC/0/O/i-8NvGnhC.png)](https://photos.adron.me/photos/i-8NvGnhC/0/O/i-8NvGnhC.png)

*Selecting a Project to make a Board for.*

Below is a board that Oi setup for the [Thrashing Code Organization](https://github.com/ThrashingCode)‘s [coder-swap project](https://github.com/ThrashingCode/coder-swap). It has an item that was assigned to [Norda](https://github.com/nordallah) that she completed (the logo which she added to a [branch called assets](https://github.com/ThrashingCode/coder-swap/tree/assets)) for the project.

[![coder-swap with two existing waffles (issues in github parlance). One is in the backlog and one is done already.](https://photos.adron.me/photos/i-8wkfN5z/0/X2/i-8wkfN5z-X2.png)](https://photos.adron.me/photos/i-8wkfN5z/0/X2/i-8wkfN5z-X2.png)

*coder-swap with two existing waffles (issues in github parlance). One is in the backlog and one is done already.*

From there Oi and the team got together and discussed the major items that needed added for this week’s sprint. By clicking on the Add Issue button a drop down appears. Oi started to add a few but realized that milestones could be set.

[![Adding waffles.](https://photos.adron.me/photos/i-9dCPcBC/0/O/i-9dCPcBC.png)](https://photos.adron.me/photos/i-9dCPcBC/0/O/i-9dCPcBC.png)

*Adding waffles.*

Before diving into adding the milestones, a quick pointer on the various parts of the screen that waffle.io provides.

[![Various key points to click for certain functionality.](https://photos.adron.me/photos/i-7w8grVN/0/X2/i-7w8grVN-X2.png)](https://photos.adron.me/photos/i-7w8grVN/0/X2/i-7w8grVN-X2.png)

*Various key points to click for certain functionality.*

Now that we’ve covered a little of that interface, let’s tackle the oddly backwards way to add milestones. Simply, the waffle.io interface desperately needs a way to add milestones from within the application – especially since the milestone selection is an option when adding an issue item (waffle).

Oi had to navigate out of waffle.io and over to github in order to add a milestone. The way to do that is to click on the issues list.

[![The issues list.](https://photos.adron.me/photos/i-chFXCJh/0/O/i-chFXCJh.png)](https://photos.adron.me/photos/i-chFXCJh/0/O/i-chFXCJh.png)

*The issues list.*

Then there are four items along the top, with milestones being the last item. Click on it.

[![Where to find Milestones.](https://photos.adron.me/photos/i-ZqzX7RH/0/O/i-ZqzX7RH.png)](https://photos.adron.me/photos/i-ZqzX7RH/0/O/i-ZqzX7RH.png)

*Where to find Milestones.*

Once clicking on Create a Milestone the following dialog will display.

[![Creating a new Milestone.](https://photos.adron.me/photos/i-QW9Tjwr/0/O/i-QW9Tjwr.png)](https://photos.adron.me/photos/i-QW9Tjwr/0/O/i-QW9Tjwr.png)

*Creating a new Milestone.*

Once Oi added the first the navigation sent him back to the milestone display with the first milestone he added shown.

[![Milestones](https://photos.adron.me/photos/i-qmstSdr/0/O/i-qmstSdr.png)](https://photos.adron.me/photos/i-qmstSdr/0/O/i-qmstSdr.png)

*Milestones*

After that he added one more to the milestones for the week.

[![Milestones.](https://photos.adron.me/photos/i-hvW2XcC/0/O/i-hvW2XcC.png)](https://photos.adron.me/photos/i-hvW2XcC/0/O/i-hvW2XcC.png)

*Milestones.*

Now in waffle.io’s interface Oi can select the appropriate milestone for the week for each of the respective items.

[![Milestones displayed in waffle.io.](https://photos.adron.me/photos/i-9LCmvXF/0/O/i-9LCmvXF.png)](https://photos.adron.me/photos/i-9LCmvXF/0/O/i-9LCmvXF.png)

*Milestones displayed in waffle.io.*

With the milestones added for the week Oi went back to adding a few more waffles for the rest of the sprint. After completion Oi went ahead and mentioned to the team that he assigned various waffles to people on the team, but please “*re-assign them as the team sees fit*” for the week. From there Norda tackled the logo but also Etart went into the issues list on Github, as shown and chose one of the items he could go ahead and knock out for the team.

[![Norda & Etart tackling items. Plus a few of my own notes.](https://photos.adron.me/photos/i-FpnBJx2/0/O/i-FpnBJx2.png)](https://photos.adron.me/photos/i-FpnBJx2/0/O/i-FpnBJx2.png)

*Norda & Etart tackling items. Plus a few of my own notes.*

[Keartida](https://github.com/keartida) also created a waffle to add the waffle.io badge to the README.md file of the github repository. The badge is really cool, as it shows what is active in the “*ready*” swim lane” of the kanban board. She then knocked it out with the following text added for the coder-swap project as shown below.

```html
[![Stories in Ready](https://badge.waffle.io/ThrashingCode/coder-swap.png?label=ready&amp;amp;amp;title=Ready)%5D(http://waffle.io/ThrashingCode/coder-swap)
```

She then pulled the item over to the *In Progress* swim lane on the kanban board and went ahead and committed the change. Once committed she grabbed the commit identifier hash and left a comment for me, Adron, to +1 the commit. Let’s dig through this comment as it is a big part of how all of this can now operate seamlessly for the team.

[![Keartida's message for me to confirm the commit.](https://photos.adron.me/photos/i-nf5pwZB/0/O/i-nf5pwZB.png)](https://photos.adron.me/photos/i-nf5pwZB/0/O/i-nf5pwZB.png)

*Keartida’s message for me to confirm the commit.*

Here’s the actual text of the commit comment that Keartida left in the comments in waffle.io. Note that the comments in waffle.io are just the same as the comments on an issue or PR in github.

```html
Hey @Adron I've added the change in commit 9b31dd9adc63f46e6d6613f1fdf46ee4998262f1 and submitted the pull request here https://github.com/ThrashingCode/coder-swap/pull/11 could you +1.
```

The long hash (or short hash if you get that when making a commit) is automatically turned into a link to that specific commit by github. The @ draws a link and provides autocomplete so that the person you’re notifying in the comment will get an update in the github messages that they have a message. The URI that links directly to the PR then also automatically gets turned into a link by github and is displayed with just the hash and number like ‘#11’. These links again are automatically created by github and instantly provide a way for me, Keartida’s coding pair to go directly to those specific comments, commit, and related information to review and accept the PR into the code base.

With that covered, I’ll dive in and accept that pull request real quick. I also went ahead and added the logo, so now the README.md page in the project looks like this.

[![Logo and badge showing active ](https://photos.adron.me/photos/i-KQ8mGDk/0/O/i-KQ8mGDk.png)](https://photos.adron.me/photos/i-KQ8mGDk/0/O/i-KQ8mGDk.png)

*Logo and badge showing active “Ready” waffles (github issues) in progress.*

After that was completed, Keartida pulled her item over to the Done swim lane we decided to pull the next items over after we completed these tasks. When we completed this the kanban board looked like this.

[![The kanban board when complete.](https://photos.adron.me/photos/i-MTwqtbX/0/O/i-MTwqtbX.png)](https://photos.adron.me/photos/i-MTwqtbX/0/O/i-MTwqtbX.png)

*The kanban board when complete.*

With that, this wraps up the second issue of this series. We’ve got our kanban board, so whenever I’ll speak about it in the series I’ll likely just reference this blog entry for how it works, the flow we’re using. Albeit I haven’t been super detailed down to the step by step of our workflow I will get more detailed over time and discuss more about how the team moves things back and forth on its way to production.

Until issue two (*or three, if you’re counting I started on a zero based index*), [skål](http://en.wikipedia.org/wiki/Toast_(honor))!

[Links for other parts of this series…](http://compositecode.com/docs/thrashing-code-projects/)
