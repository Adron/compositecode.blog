---
title: 'Visual Studio Project and Solution Guidelines :: Tip o'' The Day'
date: 2008-11-03 01:54:00 +0000
last_modified_at: 2008-11-03 01:54:00 +0000
permalink: /2008/11/03/visual-studio-project-and-solution-guidelines-tip-o-the-day/
slug: visual-studio-project-and-solution-guidelines-tip-o-the-day
wp_id: 553
original_url: https://compositecode.blog/2008/11/03/visual-studio-project-and-solution-guidelines-tip-o-the-day/
categories:
- Uncategorized Bits
tags: []
excerpt: Over the years I've tried various configurations for projects and solutions in Visual Studio. One thing I've noticed is there are definitely good ways to do things and bad ways to do things. My intention is to, with this entry and others, lay out what is good, efficient, and elegant practice in putting together Visual …
---

Over the years I've tried various configurations for projects and solutions in Visual Studio. One thing I've noticed is there are definitely good ways to do things and bad ways to do things. My intention is to, with this entry and others, lay out what is good, efficient, and elegant practice in putting together Visual Studio Projects. Since I haven't posted a tip o' the day in a long while, I figured that would be a great category to drop these into.

## Don't Add Projects Whimsically!

Projects after a while start to cause all sorts of problems. There are interdependency issues that come up, possible circular references, reference maintenance, obfuscation of logic, namespace telescoping, and the list goes on. Keep project organization simple. In MVC for instance, often a solution becomes littered with a project for the model, the assembler for the model, a project for the view, and maybe ever several projects for the controllers.

All of that should be fine in a single project! Yes, one single itty bitty project. The project can then be built into a single DLL and life is thus simplified!

So don't add projects "*just because*".
