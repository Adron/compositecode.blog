---
title: HTML, CSS, JavaScript and Metro App Building on Windows 8 Part 1
date: 2012-08-16 09:57:58 -0700
last_modified_at: 2012-09-03 20:06:12 -0700
permalink: /2012/08/16/html-css-javascript-and-metro-app-building-on-windows-8-part-1/
slug: html-css-javascript-and-metro-app-building-on-windows-8-part-1
wp_id: 6244
original_url: https://compositecode.blog/2012/08/16/html-css-javascript-and-metro-app-building-on-windows-8-part-1/
categories:
- How-to
- Javascript
- Metro UI
tags:
- javascript
- metro
- metro ui
- native windows 8
- qunit
- qunit-metro
- unit testing
- windows 8
excerpt: I’m a fan of JavaScript and I’m warming to some of the Metro interfaces on Windows 8. I’ve always found the Windows 7 Phone UI, which is the first iteration of the Metro UI, to be a very slick phone interface. So with this blog entry I’m going to lay out setting up a default …
---

I’m a fan of JavaScript and I’m warming to some of the Metro interfaces on Windows 8. I’ve always found the Windows 7 Phone UI, which is the first iteration of the Metro UI, to be a very slick phone interface. So with this blog entry I’m going to lay out setting up a default Windows 8 Metro application using JavaScript as the language of choice.

**Prerequisites:**

- Windows 8
- Visual Studio 2012

Open Visual Studio 2012 and click on file -> new project -> and then find the JavaScript section and pick the blank metro app.

[![New Windows 8 Metro Project](/images/adronhall.smugmug.com/Software/Software-Development/Building-a-JavaScript-Metro/i-GK8CJ5f/0/S/js-01-S.jpg "New Windows 8 Metro Project")](http://adronhall.smugmug.com/Software/Software-Development/Building-a-JavaScript-Metro/24795926_2gRvGS#!i=2029454166&k=GK8CJ5f&lb=1&s=O)

*New Windows 8 Metro Project*

Once you have the application created, I’d suggest following good practice and adding [QUnit-Metro](http://qunitmetro.github.com/QUnitMetro/) to your project with [Nuget](http://nuget.org/packages/QUnit-Metro)(or get the actual files if you don’t want to use Nuget).

[![Getting QUnit-Metro via Nuget](/images/adronhall.smugmug.com/Software/Software-Development/Building-a-JavaScript-Metro/i-5ZGcDNz/0/S/js-02-S.jpg "Getting QUnit-Metro via Nuget")](http://adronhall.smugmug.com/Software/Software-Development/Building-a-JavaScript-Metro/24795926_2gRvGS#!i=2029454168&k=5ZGcDNz&lb=1&s=O)

*Getting QUnit-Metro via Nuget*

Once you’ve added the QUnit-Metro interface you’re ready to get started writing tests. But before writing a test take a look at the additional files that the QUnit-Metro Nuget Package adds to the project.

[![Things Added With QUnit-Metro](/images/adronhall.smugmug.com/Software/Software-Development/Building-a-JavaScript-Metro/i-LCxB45C/0/S/js-04-S.jpg "Things Added With QUnit-Metro")](http://adronhall.smugmug.com/Software/Software-Development/Building-a-JavaScript-Metro/24795926_2gRvGS#!i=2029454228&k=LCxB45C&lb=1&s=O)

*Things Added With QUnit-Metro*

In the screenshot (click for a full size image), I’ve pointed in a clockwise order:

- The package is added and listed in the packages file now for Nuget.
- There are now three CSS files added for QUnit. Two are Metro specific, which gives a more Metro look to the results of the tests.
- The qunitmetro.js file is the testing framework.

With this collateral added we can setup a test within the default.html page of the project. First add the following code so that your default.html file looks like this:

```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8" />
    <title>Readingz</title>
    <!-- These files are included when the project is generated, I don't really know where they are... -->
    <link href="//Microsoft.WinJS.1.0.RC/css/ui-dark.css" rel="stylesheet" />
    <script src="//Microsoft.WinJS.1.0.RC/js/base.js"></script>
    <script src="//Microsoft.WinJS.1.0.RC/js/ui.js"></script>
    <!-- These are the CSS and JavaScript files that I've edited for testing. -->
    <script src="/js/qunitmetro.js"></script>
    <script src="/js/default.js"></script>
    <script src="/js/default_tests.js"></script>
    <link href="/css/default.css" rel="stylesheet" />
    <link href="/css/qunitmetro-light.css" rel="stylesheet" />
</head>
<body>
    <p>Content goes here</p>
    <button>Press This!</button>
    <!-- This is for testing only. It goes away when application is ready to ship. -->
    <div id="qunit"></div>
</body>
</html>
```

The Microsoft.WinJS.1.0.RC libraries are included by default, which I’m assuming when I get fully upgraded to the released version of Windows 8 and Visual Studio 2012 that this might just read Microsoft.WinJS.1.0. The section of scripts and links below that are the added QUnit-Metro files. I included the qunitmetro-light.css file for metro style test results.

In the body of the page the div with the id of qunit…

```html
<div id="qunit"></div>
```

is added where the test results will display. That’s how simple it actually is. To add actual tests, I’ve added a default\_tests.js file to the js directory. I then added a simple test to the file that I’ve shown below.

```javascript
test("hello windows world of javascript tests!", function () {
    ok(1 == "1", "Passed!");
});
```

Run the application and you’ll find the following result displayed in your application.

[![The Running Application](/images/adronhall.smugmug.com/Software/Software-Development/Building-a-JavaScript-Metro/i-ChFrw33/0/S/js-06-S.jpg "The Running Application")](http://adronhall.smugmug.com/Software/Software-Development/Building-a-JavaScript-Metro/24795926_2gRvGS#!i=2029787191&k=ChFrw33&lb=1&s=O)

*The Running Application*

This is one place where an odd thing seems to be occurring (if you have any idea what the problem is, leave a comment, and I’ll do the same when I get the issues resolved). The test just keeps reporting “Running…” until you click on Readingz, noglobals, or somewhere else on the screen in that area to make an action occur. When I click on Readingz the test runs successfully like it should.

[![Test Ran](/images/adronhall.smugmug.com/Software/Software-Development/Building-a-JavaScript-Metro/i-8VvLRH9/0/S/js-07-S.jpg "Test Ran")](http://adronhall.smugmug.com/Software/Software-Development/Building-a-JavaScript-Metro/24795926_2gRvGS#!i=2029787228&k=8VvLRH9&lb=1&s=O)

*Test Ran*

What’s up with that? It’s a pretty odd action.

Another issue that I ran into, which was a user error issue on my behalf, was I swapped around the three script files so the qunit-metro file loaded last. I actually stumbled and posted the issue on Stackoverflow [here](http://stackoverflow.com/questions/11992480/running-qunit-metro-in-win-8-javascript-application-why-is-test-undefined).

[![Shout it](http://dotnetshoutout.com/image.axd?url=http%3A%2F%2Fcompositecode.com%2F2012%2F08%2F16%2Fhtml-css-javascript-and-metro-app-building-on-windows-8-part-1%2F)](http://dotnetshoutout.com/HTML-CSS-JavaScript-and-Metro-App-Building-on-Windows-8-Part-1-Composite-Code)
