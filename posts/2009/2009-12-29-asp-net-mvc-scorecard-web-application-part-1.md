---
title: ASP.NET MVC Scorecard Web Application – Part 1
date: 2009-12-29 00:05:00 +0000
last_modified_at: 2009-12-29 00:05:00 +0000
permalink: /2009/12/29/asp-net-mvc-scorecard-web-application-part-1/
slug: asp-net-mvc-scorecard-web-application-part-1
wp_id: 67
original_url: https://compositecode.blog/2009/12/29/asp-net-mvc-scorecard-web-application-part-1/
categories:
- Uncategorized Bits
tags: []
excerpt: There have been a lot of requests for MVC based scorecards, so I am going to kick off a new series of wiring up an MVC scorecard site. This first part will simply cover setting up the basic site and skeleton framework using the default ASP.NET MVC Project. Start off by starting a new ASP.NET …
---

There have been a lot of requests for MVC based scorecards, so I am going to kick off a new series of wiring up an MVC scorecard site.  This first part will simply cover setting up the basic site and skeleton framework using the default [ASP.NET MVC](http://www.asp.net/mvc/) Project.

Start off by starting a new [ASP.NET MVC](http://www.asp.net/mvc/) Project.  Since I will be creating tests for this walk through, be sure to add a unit test project also.  I am just using the default MS-test libraries for now, but feel free to apply whatever test framework you would like.

[![](/images/adronhall.smugmug.com/Software/Software-Development/ASPNET-MVC/ASPNET-MVC-Scorecard-Pt-101/750140163_UScbG-S.png)](http://adronhall.smugmug.com/Software/Software-Development/ASPNET-MVC/10762817_JvDef#750140173_3i2yN)

[![](/images/adronhall.smugmug.com/Software/Software-Development/ASPNET-MVC/ASPNET-MVC-Scorecard-Pt-102/750140162_8WYQe-S.png)](http://adronhall.smugmug.com/Software/Software-Development/ASPNET-MVC/10762817_JvDef#750140173_3i2yN)

To create additional views and controllers we’ll add a unit test for a new controller.  I will name this new controller ScorecardController, so I have added a test file called ScorecardControllerTest.cs.  The first test is just the standard action for the appropriate method actions and returning the view, as follows.  I added a similar test for the Index method also.

```
[TestClass]
public class ScorecardControllerTest
{
    [TestMethod]
    public void Scorecard()
    {
        ScorecardController scorecardController = new ScorecardController();
        var result = scorecardController.Scorecard() as ViewResult;
        Assert.IsNotNull(result);
    }

    [TestMethod]
    public void Index()
    {
        ScorecardController scorecardController = new ScorecardController();
        var result = scorecardController.Index() as ViewResult;
        Assert.IsNotNull(result);
    }
}
```

.csharpcode, .csharpcode pre
{
font-size: small;
color: black;
font-family: consolas, “Courier New”, courier, monospace;
background-color: #ffffff;
/\*white-space: pre;\*/
}
.csharpcode pre { margin: 0em; }
.csharpcode .rem { color: #008000; }
.csharpcode .kwrd { color: #0000ff; }
.csharpcode .str { color: #006080; }
.csharpcode .op { color: #0000c0; }
.csharpcode .preproc { color: #cc6633; }
.csharpcode .asp { background-color: #ffff00; }
.csharpcode .html { color: #800000; }
.csharpcode .attr { color: #ff0000; }
.csharpcode .alt
{
background-color: #f4f4f4;
width: 100%;
margin: 0em;
}
.csharpcode .lnum { color: #606060; }Once the skeleton implementation is made to get green lights on these tests, a controller will be created with the following code.

```
public class ScorecardController : Controller
{
    public ActionResult Index()
    {
        return View();
    }

    public ActionResult Scorecard()
    {
        return View();
    }
}
```

.csharpcode, .csharpcode pre
{
font-size: small;
color: black;
font-family: consolas, “Courier New”, courier, monospace;
background-color: #ffffff;
/\*white-space: pre;\*/
}
.csharpcode pre { margin: 0em; }
.csharpcode .rem { color: #008000; }
.csharpcode .kwrd { color: #0000ff; }
.csharpcode .str { color: #006080; }
.csharpcode .op { color: #0000c0; }
.csharpcode .preproc { color: #cc6633; }
.csharpcode .asp { background-color: #ffff00; }
.csharpcode .html { color: #800000; }
.csharpcode .attr { color: #ff0000; }
.csharpcode .alt
{
background-color: #f4f4f4;
width: 100%;
margin: 0em;
}
.csharpcode .lnum { color: #606060; }

At this point I need to create some tests for what is expected in the view, but I will get to that once a bit more of the skeleton of the site is done.  As soon as I wrote these tests, based on where they are located in my folder structure I decided that I need to do a quick refactor of the name.  Having a Scorecard/Scorecard path just seemed stupid, so I renamed the Scorecard.aspx to Display.aspx and changed the method name appropriately.  If you are following along, the subsequent code will be using the renamed page/method, etc.

The next thing I wanted to do was to get the view coming up appropriately, so first things first, new tests.

```
[TestMethod]
public void ScorecardViewExists()
{
    ScorecardController scorecardController = new ScorecardController();
    var result = scorecardController.Display() as ViewResult;
    Assert.AreEqual("Display", result.ViewName);
}
```

.csharpcode, .csharpcode pre
{
font-size: small;
color: black;
font-family: consolas, “Courier New”, courier, monospace;
background-color: #ffffff;
/\*white-space: pre;\*/
}
.csharpcode pre { margin: 0em; }
.csharpcode .rem { color: #008000; }
.csharpcode .kwrd { color: #0000ff; }
.csharpcode .str { color: #006080; }
.csharpcode .op { color: #0000c0; }
.csharpcode .preproc { color: #cc6633; }
.csharpcode .asp { background-color: #ffff00; }
.csharpcode .html { color: #800000; }
.csharpcode .attr { color: #ff0000; }
.csharpcode .alt
{
background-color: #f4f4f4;
width: 100%;
margin: 0em;
}
.csharpcode .lnum { color: #606060; }

First of course it fails, but with the appropriate change shown, all runs green again.

```
public ActionResult Display()
{
    return View("Display");
}
```

So after this I added the following tests, controller actions, and views.

```
[TestMethod]
public void Select()
{
    ScorecardController scorecardController = new ScorecardController();
    var result = scorecardController.Select() as ViewResult;
    Assert.IsNotNull(result);
}

[TestMethod]
public void SelectViewNamed()
{
    ScorecardController scorecardController = new ScorecardController();
    var result = scorecardController.Select() as ViewResult;
    Assert.AreEqual("Select", result.ViewName);
}

[TestMethod]
public void IndexViewNamed()
{
    ScorecardController scorecardController = new ScorecardController();
    var result = scorecardController.Index() as ViewResult;
    Assert.AreEqual("Index", result.ViewName);
}
```

.csharpcode, .csharpcode pre
{
font-size: small;
color: black;
font-family: consolas, “Courier New”, courier, monospace;
background-color: #ffffff;
/\*white-space: pre;\*/
}
.csharpcode pre { margin: 0em; }
.csharpcode .rem { color: #008000; }
.csharpcode .kwrd { color: #0000ff; }
.csharpcode .str { color: #006080; }
.csharpcode .op { color: #0000c0; }
.csharpcode .preproc { color: #cc6633; }
.csharpcode .asp { background-color: #ffff00; }
.csharpcode .html { color: #800000; }
.csharpcode .attr { color: #ff0000; }
.csharpcode .alt
{
background-color: #f4f4f4;
width: 100%;
margin: 0em;
}
.csharpcode .lnum { color: #606060; }

After that I edited the CSS so I could get a better feel to the site relative to what I am working toward.  I will leave you to decide what you want to do with the CSS & such yourself.  One of these days I will be graphic artists worthy, for now I am just happy with a decent looking layout and reasonable colors. 😉

When I was done my Solution Explorer looked like this.

[![](/images/adronhall.smugmug.com/Software/Software-Development/ASPNET-MVC/ASPNET-MVC-Scorecard-Pt-103/750140170_bxfS2-S.png)](http://adronhall.smugmug.com/Software/Software-Development/ASPNET-MVC/10762817_JvDef#750140173_3i2yN)

Last I added the following to the Site.Master page for appropriate linkages.  This spot is located in the menucontainer section of the page.

```
<div id="menucontainer">
    <ul id="menu">
        <li>
            <%= Html.ActionLink("Home", "Index", "Home")%></li>
        <li>
            <%= Html.ActionLink("About", "About", "Home")%></li>
        <li>
            <%= Html.ActionLink("Scorecard", "Display", "Scorecard") %></li>
    </ul>
</div>
```

.csharpcode, .csharpcode pre
{
font-size: small;
color: black;
font-family: consolas, “Courier New”, courier, monospace;
background-color: #ffffff;
/\*white-space: pre;\*/
}
.csharpcode pre { margin: 0em; }
.csharpcode .rem { color: #008000; }
.csharpcode .kwrd { color: #0000ff; }
.csharpcode .str { color: #006080; }
.csharpcode .op { color: #0000c0; }
.csharpcode .preproc { color: #cc6633; }
.csharpcode .asp { background-color: #ffff00; }
.csharpcode .html { color: #800000; }
.csharpcode .attr { color: #ff0000; }
.csharpcode .alt
{
background-color: #f4f4f4;
width: 100%;
margin: 0em;
}
.csharpcode .lnum { color: #606060; }

When I run the app I now have a basic skeleton and the initial pages I am going to work with.  Next steps coming soon.

![](/images/adronhall.smugmug.com/Software/Software-Development/ASPNET-MVC/12-26-2009-1-24-10-PM/750142735_ffeFc-S.png)

[![kick it on DotNetKicks.com](http://www.dotnetkicks.com/Services/Images/KickItImageGenerator.ashx?url=http%3a%2f%2fwww.adronbhall.com%2fblogs%2ftechnology__software_development%2fpost%2f2009%2f12%2f29%2fASPNET-MVC-Scorecard-Web-Application-Part-1.aspx&bgcolor=3333FF&cfgcolor=CC3300)](http://www.dotnetkicks.com/kick/?url=http%3a%2f%2fwww.adronbhall.com%2fblogs%2ftechnology__software_development%2fpost%2f2009%2f12%2f29%2fASPNET-MVC-Scorecard-Web-Application-Part-1.aspx)

[![Shout it](http://dotnetshoutout.com/image.axd?url=http%3A%2F%2Fwww.adronbhall.com%2Fblogs%2Ftechnology__software_development%2Fpost%2F2009%2F12%2F29%2FASPNET-MVC-Scorecard-Web-Application-Part-1.aspx)](http://dotnetshoutout.com/ASPNET-MVC-Scorecard-Web-Application-Part-1)
