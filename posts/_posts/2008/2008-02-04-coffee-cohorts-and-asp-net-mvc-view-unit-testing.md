---
title: Coffee Cohorts and ASP.NET MVC View Unit Testing
date: 2008-02-04 20:33:08 -0800
last_modified_at: 2008-02-04 20:33:08 -0800
permalink: /2008/02/04/coffee-cohorts-and-asp-net-mvc-view-unit-testing/
slug: coffee-cohorts-and-asp-net-mvc-view-unit-testing
wp_id: 339
original_url: https://compositecode.blog/2008/02/04/coffee-cohorts-and-asp-net-mvc-view-unit-testing/
categories:
- Uncategorized Bits
tags: []
excerpt: So my buddy Shane busted my chops tonight on how to unit test a view in the MVC Framework for ASP.NET. Actually, he just kind of asked me how I was doing it. Honestly, I had not even had time recently to get to that step even though I’ve been working steadily toward that. I …
---

So my buddy Shane busted my chops tonight on how to unit test a view in the MVC Framework for ASP.NET.  Actually, he just kind of asked me how I was doing it.  Honestly, I had not even had time recently to get to that step even though I’ve been working steadily toward that.  I knocked out a crude model & controllers with the appropriate unit tests and also got a sample LINQ data model going on.

Laurie, Shane, Eric, and I however had decided to meet after work just to discuss the MVC, LINQ, or whatever else came up.  As expected in the short hour long time span that we had to discuss, we got a lot covered, but only skimmed the surface.  The one take away I did have was that the entity data model, regardless of it being in beta with some glaring bugs (the update from database doesn’t seem to work for referential integrity) is a must have!  The other thing is that I really need to keep chomping at these damn unit tests.  There are, it seems, more ways to test things than there are ways to actually build stuff that needs tested.  It is insane.

So now that it is 1:06am, after a good solid workout, I’ve decided it is a great time to sit down and get [mbUnit](http://www.mbunit.com) running with some good tests.  What better to work against than the ASP.NET MVC Views that I have in my Transportation Tracker Application.

If you don’t have [mbUnit](http://www.mbunit.com), go get it at the [mbUnit Site](http://www.mbunit.com).  Two articles on how to use [mbUnit](http://www.mbunit.com) that I’ve gone along with to ramp up on the tools are available via [www.codeproject.com](http://www.codeproject.com), “Generative Unit Test Framework” and the [mbUnit](http://www.mbunit.com) [Documentation](http://docs.mbunit.com/) itself.

To setup the code snippets for mbUnit follow these steps.  First click on Tools -> Code Snippets Manager…

[![](https://adronhall.smugmug.com/photos/251136169-S.png)](http://adronhall.smugmug.com/gallery/4286065/1/251136169)

Once that dialog window comes up then click on Add (Just in case, I’ve highlighted it in red).

[![](https://adronhall.smugmug.com/photos/251136171-S.png)](http://adronhall.smugmug.com/gallery/4286065/1/251136171)

The next dialog comes up and has three key places to take note and action.  The top red highlight is the path, or what would be the path on Vista.  The second is the folder you want to select, unless you use that VB stuff, and the last highlighted area is what you’ll press when you’ve got your folder selected.

[![](https://adronhall.smugmug.com/photos/251136173-M.png)](http://adronhall.smugmug.com/gallery/4286065/1/251136173)

After that you should be able to open up the tree item and see items similar to those listed in the screen image below.

[![](https://adronhall.smugmug.com/photos/251136178-S.png)](http://adronhall.smugmug.com/gallery/4286065/1/251136178)

Once the snippets are installed, type any of the following and hit tab twice.

- **autorunner** : Adds all the basic code for a simple [executable self-testing assembly](http://docs.mbunit.com/help/html/mbunitandvisualstudio/CreatingSelfTestingAssemblies.htm).- **combinatorial** : Adds code for a combinatorial test with 2 parameters and 2 factories- **datafixture** : Adds code for a data fixture test class- **processfixture** : Adds code for a process fixture test class where test are performed in a given order- **rowtest** : Adds code for a simple row test- **state** : Adds code for an IState wrapper- **test** : Adds code for a simple test- **testexpectedexception** : Adds code for a simple test that expects an exception to be raised- **testfixture** : Adds code for a basic fixture test class including setup, teardown and test methods.- **testsuitefixture** : Adds code for a test suite (dynamic) fixture class and method to add tests to the suite at runtime- **typefixture** : Adds code for a type fixture test class including setup, teardown and test methods.- **typefixturefac** : Adds code for a type fixture test class including setup, teardown and test methods using a provider factory- **usingmbunit** : Adds the standard using or imports statement for MbUnit.Framework.

…and that’s it for now.  Tomorrow at some point, or maybe the next day time pending, I’ll post a sample that I’m working up for unit testing the views in the ASP.NET MVC.

…and you thought I’d get to it tonight at 1:32am in the morning?!  I gotta sleep too.  Jeez.  ![Stick out tongue [:P]](/emoticons/emotion-4.gif)
