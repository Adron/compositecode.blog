---
title: HTML, CSS, JavaScript and Metro App Building on Windows 8 Part 2
date: 2012-08-20 22:32:25 -0700
last_modified_at: 2012-08-20 23:31:53 -0700
permalink: /2012/08/20/html-css-javascript-and-metro-app-building-on-windows-8-part-2/
slug: html-css-javascript-and-metro-app-building-on-windows-8-part-2
wp_id: 6277
original_url: https://compositecode.blog/2012/08/20/html-css-javascript-and-metro-app-building-on-windows-8-part-2/
categories:
- How-to
- Javascript
- Metro UI
tags:
- javascript
- js
- unit test
- unit testing
- unit tests
- windows 8
- winjs
excerpt: In the first part of this seriesI kicked everything off by starting a Windows 8 JavaScript Project and added QUnit-Metro via Nuget. Now that we have a small executable application, I’ll get some things added and cover what exactly it is we’re doing in each part. Open the project up that we created in the …
---

In the [first part of this series](/2012/08/16/html-css-javascript-and-metro-app-building-on-windows-8-part-1/)I kicked everything off by starting a Windows 8 JavaScript Project and added QUnit-Metro via Nuget. Now that we have a small executable application, I’ll get some things added and cover what exactly it is we’re doing in each part. Open the project up that we created in the previous blog entry of the series. Once open find and open the default.html, default.js and default\_tests.js files to work with. In the default.js file you’ll find the following code in the default.js.

```javascript
(function () {
    "use strict";

    var app = WinJS.Application;
    var activation = Windows.ApplicationModel.Activation;
    WinJS.strictProcessing();

    app.onactivated = function (args) {
        if (args.detail.kind === activation.ActivationKind.launch) {
            if (args.detail.previousExecutionState !== activation.ApplicationExecutionState.terminated) {
            } else {
            }
            args.setPromise(WinJS.UI.processAll());
        }
    };

    app.oncheckpoint = function (args) {
    };

    app.start();
})();
```

**A Bit of Context – default.js**

At the beginning you’ll find that all the code is enclosed in a self-executing anonymous function. This gives us the ability to avoid naming conflicts or accidentally modifying variables in other spaces. Kind of the “namespaces” of C# or other organizational code features from other languages (I said kind of, there are other ways to do this too, this is just one). The other cool thing about this is it keeps identifiers out of the global namespace which also helps performance (it’ll also get you called all sorts of stuff if you create global variables in JavaScript! I’m nice, I won’t do it, but be prepared to be appropriately punished for such dissension as global variable creation! I warned ya.).

This next part (reminds me of why I find JavaScript scary in addition to awesome) has a variable that turns “strict mode” on. What this does, just like those of you may know from the Visual Basic days, is turn on a strict mode of additional error checking for code. It helps prevent you from doing all sorts of dumb things, like trying to assign a value to a read-only variable. For more on “strict mode” check out [Microsoft’s Strict Mode Page](http://msdn.microsoft.com/en-us/library/windows/apps/br230269.aspx).

The remaining bits of code in the default.js are the handlers for the application [activated](http://msdn.microsoft.com/en-us/library/windows/apps/br212679.aspx) and checkpoint events. These events are fairly self explanatory, suffice it to say they happen when the application launches and checkpoint fires when a particular checking event happens against the Process Lifetime Management. The Process Lifetime Management handles all of the application suspend, resume and background events.

**TDD & BDD For The Win!**

Ok, so this isn’t the best example of either really, but to get started we want to wire up an event to a button. But first we want to test if the event is wired up. How does someone tests if an event is wired up in JavaScript? Like this.

```javascript
test("Where the text box is populated ", function () {
    var result = document.getElementById("messageOutput").innerText;
    ok(result == "", "should have empty inner text.");
});
```

**Adding a Button & Some Button Functionality**

Ok, done with the context. Let’s add a button and make some magic happen. Bring focus to the default.html page and add a button, a text box and the respective components.

```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8" />
    <title>Readingz</title>
    <!-- These files are included when the project is generated, I don't really know where they are... -->
    <link href="//Microsoft.WinJS.1.0.RC/css/ui-light.css" rel="stylesheet" />
    <script src="//Microsoft.WinJS.1.0.RC/js/base.js"></script>
    <script src="//Microsoft.WinJS.1.0.RC/js/ui.js"></script>
    <!-- Turned on the testing. -->
    <script src="/js/qunitmetro.js"></script>
    <script src="/js/default_tests.js"></script>
    <!-- Default Metro files. -->
    <script src="/js/default.js"></script>
    <link href="/css/default.css" rel="stylesheet" />
</head>
<body>
    <p>Click the button to run the tests for the default.html and default.js code.</p>
    <input id="peripheralParameters" type="text" />
    <button id="runTests">Run Tests</button>
    <p id="messageOutput"></p>
</body>
</html>
```

NOTE: I made more than a few changes from the default.html included in the previous part of this series. One hard to notice change is that I switched the style sheet from the dark Metro theme to the light Metro theme.

With those additions add a function to the default.js file as shown below and then add the event handler.

```javascript
(function () {
    "use strict";

    var app = WinJS.Application;
    var activation = Windows.ApplicationModel.Activation;
    WinJS.strictProcessing();

    app.onactivated = function (args) {
        if (args.detail.kind === activation.ActivationKind.launch) {
            if (args.detail.previousExecutionState !== activation.ApplicationExecutionState.terminated) {

            } else {

            }
            args.setPromise(WinJS.UI.processAll());

            var runTests = document.getElementById("runTests");
            runTests.addEventListener("click", buttonClickHandler, false);
        }
    };

    app.oncheckpoint = function (args) {};

    function buttonClickHandler () {
        document.getElementById("messageOutput").innerText =
           "Parameters Passed: " +
           document.getElementById("peripheralParameters").value +
           "!";
    }

    app.start();
})();
```

I now have one button now working, actually doing something, with a unit tests to verify that the button exists and the event is wired up. Some progress is being made!

If I run the application I get passing tests. That’s it for now. In the next entry we’ll dive deeper into testing and into functionality.

Until next time, happy scripting with the JavaScript on Windows 8.
