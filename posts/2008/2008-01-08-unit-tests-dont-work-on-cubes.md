---
title: Unit Tests Don't Work on Cubes
date: 2008-01-08 12:56:39 +0000
last_modified_at: 2008-01-08 12:56:39 +0000
permalink: /2008/01/08/unit-tests-dont-work-on-cubes/
slug: unit-tests-dont-work-on-cubes
wp_id: 355
original_url: https://compositecode.blog/2008/01/08/unit-tests-dont-work-on-cubes/
categories:
- Uncategorized Bits
tags: []
excerpt: I’ve been building web sites for a while now. I’ve been writing code, object oriented style for the better part of a decade. Unit testing I’ve been doing for all of about 1-2 years to various degrees. Nothing super advanced yet, and slowly I’m getting some of the more advanced unit testing methods figured out. …
---

I’ve been building web sites for a while now.  I’ve been writing code, object oriented style for the better part of a decade.  Unit testing I’ve been doing for all of about 1-2 years to various degrees.  Nothing super advanced yet, and slowly I’m getting some of the more advanced unit testing methods figured out.  Not so much advanced, but just newer methods for testing in different situations.

So now I’ve figured out web service unit tests, database unit tests, and all sorts of other ways to unit test things.  So my question is, how does one unit test a cube?

An SSAS (SQL Server Analysis Services) Cube can be built and then exported out into XMLA for running against another server to create the cube.  Also it is good for a kind of backup mechanism.  Cubes also can have MDX segments, which might be easier to test.  But amid all of these pieces, and all of the “code” written for cubes, what is a good way to test a cube?  How does one break the parts of a cube into units to be able to test in the first place?

Off hand I’m just going to trace over some ideas I stumbled into while riding the bus out to Scott Hanselman’s talk on ASP.NET MVC.

The First Unit Testing Idea for Cubes

I could develop a custom framework using ADOMD.NET that would literally test points of the cubes, dimensions, and such things like that.  Adding the ability to just insert attributes onto classes that are utilizing the cube or some other such association.  Building something like that would work well if one was writing code directly to the cube.  However…

The Second Idea is an MDX Test Framework

This idea sounds much better, but I actually don’t have the first idea on how I would prospectively implement it.  Anyone out there ever try to implement such a thing with MDX?

So that is my first two ideas…  and I’ve arrived at my destination, thus am done thinking of idea for this entry.

Does anyone else have any ideas or thoughts?

[![kick it on DotNetKicks.com](http://www.dotnetkicks.com/Services/Images/KickItImageGenerator.ashx?url=http%3a%2f%2fadronbhall.com%2fblogs%2ftechnology__software_development%2farchive%2f2008%2f01%2f08%2f6117.aspx&bgcolor=3333FF&cfgcolor=CC3300)](http://www.dotnetkicks.com/kick/?url=http%3a%2f%2fadronbhall.com%2fblogs%2ftechnology__software_development%2farchive%2f2008%2f01%2f08%2f6117.aspx)

Technorati Tags: [unit test](http://technorati.com/tags/unit%20test),[business intelligence](http://technorati.com/tags/business%20intelligence),[MDX](http://technorati.com/tags/MDX),[MDX Unit Tests](http://technorati.com/tags/MDX%20Unit%20Tests)

del.icio.us Tags: [unit test](http://del.icio.us/popular/unit%20test),[business intelligence](http://del.icio.us/popular/business%20intelligence),[MDX](http://del.icio.us/popular/MDX),[MDX Unit Tests](http://del.icio.us/popular/MDX%20Unit%20Tests)
