---
title: NxBRE Integration and Visual Studio Team Server Strangeness
date: 2007-03-07 13:10:55 -0800
last_modified_at: 2010-09-13 23:19:22 -0700
permalink: /2007/03/07/nxbre-integration-and-visual-studio-team-server-strangeness/
slug: nxbre-integration-and-visual-studio-team-server-strangeness
wp_id: 504
original_url: https://compositecode.blog/2007/03/07/nxbre-integration-and-visual-studio-team-server-strangeness/
categories:
- Rants
tags:
- nxbre
- team foundation server
- tfs
- visual studio
excerpt: So after a far longer process than I originally had planned on (fortunately I had saved a ton of time by using a prebuilt solution such as NxBRE) I acheived a building integration of the NxBRE Project into the primary Visual Studio Solution. No particular fault of NxBREs it is just that some of the references and other items got fubared when moved across. That leads me to… …Visual Studio Team Server’s Source Control would NOT let me just add the project. I’m not sure what the deal was with that, but it was determined. What I had to do in the end was literally do a manual creation of a project and name it the same, then add all the files as one would existing code files. After working out the bugs everything seems hunky dory. Gracious though it was a bit of excessive work that I didn’t really need to focus on at this time. Now that this is done I intend to in the next few days create some examples and stick them up on the site in relation to utilizing NxBRE.
---

So after a far longer process than I originally had planned on (fortunately I had saved a ton of time by using a prebuilt solution such as NxBRE) I acheived a building integration of the NxBRE Project into the primary Visual Studio Solution.  No particular fault of NxBREs it is just that some of the references and other items got fubared when moved across.  That leads me to…

…Visual Studio Team Server’s Source Control would NOT let me just add the project.  I’m not sure what the deal was with that, but it was determined.  What I had to do in the end was literally do a manual creation of a project and name it the same, then add all the files as one would existing code files.  After working out the bugs everything seems hunky dory.  Gracious though it was a bit of excessive work that I didn’t really need to focus on at this time.

Now that this is done I intend to in the next few days create some examples and stick them up on the site in relation to utilizing NxBRE.
