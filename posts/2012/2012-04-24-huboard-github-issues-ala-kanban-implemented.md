---
title: Huboard, Github Issues ala Kanban, Implemented…
date: 2012-04-24 09:15:09 -0700
last_modified_at: 2012-04-24 09:15:09 -0700
permalink: /2012/04/24/huboard-github-issues-ala-kanban-implemented/
slug: huboard-github-issues-ala-kanban-implemented
wp_id: 5453
original_url: https://compositecode.blog/2012/04/24/huboard-github-issues-ala-kanban-implemented/
categories:
- How-to
- Kanban Lean Agiley Stuff
- Reviews
tags:
- git
- github
- huboard
- kanban
excerpt: Recently I discovered Huboard. Thanks to those that helped me find it! Huboard is really simple and helps keep that kanban visibility when everyone can’t be in the same environment all the time. I setup a board for one of the pending OSS Projects that will be coming live. These are the steps I took. …
---

Recently I discovered Huboard. Thanks to those that helped me find it! Huboard is really simple and helps keep that kanban visibility when everyone can’t be in the same environment all the time. I setup a board for one of the pending OSS Projects that will be coming live. These are the steps I took. 1. Go to <http://www.huboard.com>and login with your Github identifiy. This will use your existing github account and you’ll then have access to all your projects to setup and use as you see fit with Huboard.

[![Allow Github to Provide Identify Access](/images/adronhall.smugmug.com/Software/Software-Development/Huboard/i-dWcpTsX/0/S/allowAccess-S.jpg "Allow Github to Provide Identify Access")](http://www.github.com)

*Allow Github to Provide Identify Access*

2. [Huboard](http://www.huboard.com) will now list all of your projects you have [github](http://www.github.com).

[![Huboard Repository List (Click for full size image)](/images/adronhall.smugmug.com/Software/Software-Development/Huboard/i-4nMLqWG/0/M/Open-Issues-M.jpg "Huboard Repository List (Click for full size image)")](http://adronhall.smugmug.com/Software/Software-Development/Huboard/22513007_4mcRQ9#!i=1808734343&k=4nMLqWG&lb=1&s=O)

*Huboard Repository List (Click for full size image)*

3. Get your list items all labeled appropriately. (All explained below image)

[![Issues listed with appropriate Labels (Click for full size image)](/images/adronhall.smugmug.com/Software/Software-Development/Huboard/i-mKcpFFN/0/M/Open-Issues1-M.jpg "Issues listed with appropriate Labels (Click for full size image)")](/images/adronhall.smugmug.com/Software/Software-Development/Huboard/i-mKcpFFN/0/O/Open-Issues1.jpg)

*Issues listed with appropriate Labels (Click for full size image)*

The key to Huboard is the simple tagging. Each issue in the project will display as an open issue on the repository/project list in Huboard, however to get them to show up on the kanban there is a special label pattern to use. Simply add a number, dash, and the title of the issue for it to be listed in the kanban. Then apply the label(s) to the issue. For example, in the screenshot above you can see that item #3, which has a titled of “#3 – Initiate Project & Setup” also has a label of “2 – Ready”. This label will list the item in the column “Ready” on the kanban board. The same goes for each of the items that are listed as backlog. The kanban board in Huboard uses the number to order the columns by the labels and the following title as the column header. The respective kanban board for the issue listing above looks like this.

[![Huboard kanban (Click for full size image)](/images/adronhall.smugmug.com/Software/Software-Development/Huboard/i-mnNX4Wv/0/M/Open-Issues2-M.jpg "Huboard kanban (Click for full size image)")](/images/adronhall.smugmug.com/Software/Software-Development/Huboard/i-mnNX4Wv/0/O/Open-Issues2.jpg)

*Huboard kanban (Click for full size image)*

For now I’ve primarily been just adding the issues and maintaining them via the Github web interface. However the items can be moved via commit messages. Here are some examples;

- push GH-#
- pushed GH-#
- move GH-#
- moves GH-#

With that you get maximum Github Awesome + Kanban Communication.
