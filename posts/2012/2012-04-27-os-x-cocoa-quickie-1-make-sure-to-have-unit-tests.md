---
title: 'OS-X Cocoa Quickie #1 => Make Sure to Have Unit Tests'
date: 2012-04-27 06:53:15 -0700
last_modified_at: 2012-04-24 10:54:37 -0700
permalink: /2012/04/27/os-x-cocoa-quickie-1-make-sure-to-have-unit-tests/
slug: os-x-cocoa-quickie-1-make-sure-to-have-unit-tests
wp_id: 5475
original_url: https://compositecode.blog/2012/04/27/os-x-cocoa-quickie-1-make-sure-to-have-unit-tests/
categories:
- A Bite o' Apple
- Apple Programming
- How-to
tags:
- cocoa
- objective-c
- unit test
- unit testing
- unit tests
- xcode
excerpt: When starting an Xcode Cocoa Project you should have a testing project that you include. It’s a simple check box on the project creation dialogs. If for some reason you inherit a project that doesn’t have unit tests, tests, or anything of the sort and need to add a testing project follow these steps. With …
---

When starting an Xcode Cocoa Project you should have a testing project that you include. It’s a simple check box on the project creation dialogs.

[![Keep This Checked! Write Tests!](/images/adronhall.smugmug.com/Software/Software-Development/Xcode/i-SX8vfqM/0/M/Cocoa-Test-15-M.jpg "Keep This Checked! Write Tests!")](/images/adronhall.smugmug.com/Software/Software-Development/Xcode/i-SX8vfqM/0/O/Cocoa-Test-15.jpg)

*Keep This Checked! Write Tests!*

If for some reason you inherit a project that doesn’t have unit tests, tests, or anything of the sort and need to add a testing project follow these steps. With the project open add a new target as shown below.

[![Add a New Target to the Project](/images/adronhall.smugmug.com/Software/Software-Development/Xcode/i-MnnXg8w/0/M/Cocoa-Test-01-M.jpg "Add a New Target to the Project")](http://adronhall.smugmug.com/Software/Software-Development/Xcode/22597430_KLwRCh#!i=1809185892&k=MnnXg8w&lb=1&s=O)

*Add a New Target to the Project*

Add a Cocoa Unit Testing Bundle.

[![Cocoa Touch Unit Testing Bundle](/images/adronhall.smugmug.com/Software/Software-Development/Xcode/i-79NXxjt/1/M/Cocoa-Test-02-M.jpg "Cocoa Touch Unit Testing Bundle")](http://adronhall.smugmug.com/Software/Software-Development/Xcode/22597430_KLwRCh#!i=1809186089&k=f2vF8SL&lb=1&s=O)

*Cocoa Touch Unit Testing Bundle (Click for full window and full size image)*

Set the appropriate parameters for your project. Be sure to select the project from the drop down.

[![Set the product name and be sure to select the correct Project from the drop down. (Click for full window and full size image)](/images/adronhall.smugmug.com/Software/Software-Development/Xcode/i-KgHVt27/0/M/Cocoa-Test-03-M.jpg "Set the product name and be sure to select the correct Project from the drop down. (Click for full window and full size image)")](http://adronhall.smugmug.com/Software/Software-Development/Xcode/22597430_KLwRCh#!i=1809186584&k=7XCpVKp&lb=1&s=O)

*Set the product name and be sure to select the correct Project from the drop down. (Click for full window and full size image)*

Once finished adding the testing target, edit the schema. The project will have an additional schema. I personally like to keep them rolled together, so delete the “\*Tests” schema and just make sure that the Tests section has the right target listed.

[![Schema Settings](/images/adronhall.smugmug.com/Software/Software-Development/Xcode/i-hLbMF8N/0/M/Open-Issues3-M.jpg "Schema Settings")](http://adronhall.smugmug.com/Software/Software-Development/Xcode/22597430_KLwRCh#!i=1810804695&k=hLbMF8N&lb=1&s=O)

*Schema Settings*

If it isn’t listed, as shown in the above dialog, click the + to add the tests project. Select it in the target dialog as shown below.

![Adding the test target for the schema](/images/adronhall.smugmug.com/Software/Software-Development/Xcode/i-JJFJLfg/0/O/Open-Issues4.jpg "Adding the test target for the schema")

*Adding the test target for the schema*

Once all that is done then the tests can be executed from the Product -> Test menu option or the shortcut key combo of ⌘U. With the default code that is added to the target project, you’ll end up with one failing test.

[![Test FAIL!](/images/adronhall.smugmug.com/Software/Software-Development/Xcode/i-N8JbxSf/0/M/Open-Issues5-M.jpg "Test FAIL!")](http://adronhall.smugmug.com/Software/Software-Development/Xcode/22597430_KLwRCh#!i=1810877487&k=N8JbxSf&lb=1&s=O)

*Test FAIL!*

Now write tests!
