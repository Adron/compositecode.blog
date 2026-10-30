---
title: CAB & SCSF [SmartParts] Pt. 1
date: 2006-11-26 06:41:54 -0800
last_modified_at: 2006-11-26 06:41:54 -0800
permalink: /2006/11/26/cab-scsf-smartparts-pt-1/
slug: cab-scsf-smartparts-pt-1
wp_id: 527
original_url: https://compositecode.blog/2006/11/26/cab-scsf-smartparts-pt-1/
categories:
- Uncategorized Bits
tags: []
excerpt: SmartParts. The coolest (or maybe just the prettiest) part of the View of Model View Presenters (MVP) and Model View Controllers (MVC). At least in my not so humble opinion. A SmartPart is generally used to implement what amounts to a Custom User Control in a Windows Application. Utilizing various controls a SmartPart usually captures …
---

SmartParts.  The coolest (or maybe just the prettiest) part of the View of Model View Presenters (MVP) and Model View Controllers (MVC).  At least in my not so humble opinion.  A SmartPart is generally used to implement what amounts to a Custom User Control in a Windows Application.  Utilizing various controls a SmartPart usually captures a single domain within a business use case.  An example would be a data entry form for entering sales information in a point of sales system or the report criteria screen in the same system.

Below are some of the SmartPart examples I’ve created for my Travel Tracker Application that I’m working on.  I started with the following standard steps to create an Smart Client Software Factory (SCSF) based Composite UI Application Block (CAB) Application.

## Setting up the actual Solution

- Open Visual Studio and start a new SCSF Project.

[![](http://adronbhall.com/photos/random_screen_captures_and_other_assorted_stuff/images/1394/original.aspx)](http://adronbhall.com/photos/random_screen_captures_and_other_assorted_stuff/picture1394.aspx)

- I named my project Travek Tracker Smart Client and… well you can see that info in the screenshot above.- Next I entered the appropriate information for the SCSF Project.  Uncheck both the “*Create a seperate module to define the layout for the shell*” and the “*Show related documentation after running the recipe*“.

[![](http://adronbhall.com/photos/random_screen_captures_and_other_assorted_stuff/images/1395/original.aspx)](http://adronbhall.com/photos/random_screen_captures_and_other_assorted_stuff/picture1395.aspx)

- Before going forward hit F5 (Run, not just build) and make sure everything builds and the application starts.  It is important that you do this as one little change that alters the build might compile fine, but then it will break the actual application.  This is very cumbersome to troubleshoot after the fact.- Once everything loads up I setup a seperate application folder and right click to add a “Business Module” within the structure of the new solution shown below.

[![](http://adronbhall.com/photos/random_screen_captures_and_other_assorted_stuff/images/1397/original.aspx)](http://adronbhall.com/photos/random_screen_captures_and_other_assorted_stuff/picture1397.aspx)

[![](http://adronbhall.com/photos/random_screen_captures_and_other_assorted_stuff/images/1399/original.aspx)](http://adronbhall.com/photos/random_screen_captures_and_other_assorted_stuff/category1050/picture1399.aspx)

- Once you have all of this finished right click on the Views folder and click on **Smart Client > Add View** and select a name for the new view as below.

![](http://adronbhall.com/photos/random_screen_captures_and_other_assorted_stuff/images/1400/original.aspx)

[![](http://adronbhall.com/photos/random_screen_captures_and_other_assorted_stuff/images/1402/original.aspx)](http://adronbhall.com/photos/random_screen_captures_and_other_assorted_stuff/picture1402.aspx)

- Once complete you should have a folder structure like the one below.  Now I’ll start digging into the actual Smart Parts that have been created.

[![](http://adronbhall.com/photos/random_screen_captures_and_other_assorted_stuff/images/1401/original.aspx)](http://adronbhall.com/photos/random_screen_captures_and_other_assorted_stuff/picture1401.aspx)

- There are four screens that are going to make up the SmartPart list.  Each screen has some basic control elements that are used in almost every type of application for data entry and manipulation.- Per the data model (shown below) I have the four different views.

[![](http://adronbhall.com/photos/random_screen_captures_and_other_assorted_stuff/images/1403/original.aspx)](http://adronbhall.com/photos/random_screen_captures_and_other_assorted_stuff/picture1403.aspx)

- Before getting ahead of myself I went ahead back and setup some basic properties for the **Shell Application Project**.- First setup the Shell so that the **Split Pane Control** is removed and add a **Deck Workspace Control** to the application in place of the **Split Pane Control**.  I then set the application so that the Shell application will launch center of screen and at a resolution of 800×600. I really had to do some messing around to get the **Split Panel Control** deleted.  The easiest way I found was the undock the control, then shrink it by resizing.  I could then easily right click and select delete.

[![](http://adronbhall.com/photos/random_screen_captures_and_other_assorted_stuff/images/1413/original.aspx)](http://adronbhall.com/photos/random_screen_captures_and_other_assorted_stuff/category1050/picture1413.aspx)

- After I removed the **Split Panel Control** I ran the solution again to see what wouldn’t build.  I assumed, rightfully so, that some parts would have code segments somewhere.  Sure enough the \_leftWorkspace and \_rightWorkspace on lines 44 & 45 of the ShellForm.cs file don’t exist anymore, but the code is there so I deleted it.  I ran it again after that and the app popped up just fine.- One other good thing to get in the habit of is to set the **Localizable** property to true.  This will put all of the text and other associated user visible text in a resource file in the project.  It’s as simple as adding new language resource files later.- I also removed the menu bar, ran the application, and removed any pertinent lines of code for that also.  There are two lines that need removed in the ShellForm.cs and ShellApplication.cs files.- After that I added the menu options needed for displaying the various **Smart Parts**.

[![](http://adronbhall.com/photos/random_screen_captures_and_other_assorted_stuff/images/1454/original.aspx)](http://adronbhall.com/photos/random_screen_captures_and_other_assorted_stuff/picture1454.aspx)

- After adding the menu additions I then added a **Tab Workspace Control**, removed all of the tabs and named the control accordingly.

[![](http://adronbhall.com/photos/random_screen_captures_and_other_assorted_stuff/images/1455/original.aspx)](http://adronbhall.com/photos/random_screen_captures_and_other_assorted_stuff/picture1455.aspx)

- Again I ran the application to assure the solution would build and start.  A’OK.- After that I tidied up the screen, made sure the **Tab Workspace Control** has all the properties set I wanted, and prepared to wire up some of this contraption to actually display the four **Smart Parts** I’ve created.
