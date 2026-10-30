---
title: 'Put Those Assemblies There :: Tip O'' The Day'
date: 2008-08-07 10:50:53 +0000
last_modified_at: 2008-08-07 10:50:53 +0000
permalink: /2008/08/07/put-those-assemblies-there-tip-o-the-day/
slug: put-those-assemblies-there-tip-o-the-day
wp_id: 254
original_url: https://compositecode.blog/2008/08/07/put-those-assemblies-there-tip-o-the-day/
categories:
- Uncategorized Bits
tags: []
excerpt: A little post build event can help a lot when one has multiple assemblies that need to be utilized by an application. Such as the entlib or composite library. Just put the following script in the post build event and make sure to create a directory were the assemblies will go. Boom – you got …
---

A little post build event can help a lot when one has multiple assemblies that need to be utilized by an application.  Such as the entlib or composite library.  Just put the following script in the post build event and make sure to create a directory were the assemblies will go.  Boom – you got everything in one place were you want it!

copy /y “$(TargetDir)$(TargetName).\*”  “$(SolutionDir)..\build\references\”

Technorati Tags: [Build](http://technorati.com/tags/Build),[Post Build](http://technorati.com/tags/Post%20Build),[Assembly](http://technorati.com/tags/Assembly)

del.icio.us Tags: [Build](http://del.icio.us/popular/Build),[Post Build](http://del.icio.us/popular/Post%20Build),[Assembly](http://del.icio.us/popular/Assembly)
