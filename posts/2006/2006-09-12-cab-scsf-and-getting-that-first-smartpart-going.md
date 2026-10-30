---
title: CAB, SCSF, and getting that first smartpart going!
date: 2006-09-12 14:21:52 +0000
last_modified_at: 2006-09-12 14:21:52 +0000
permalink: /2006/09/12/cab-scsf-and-getting-that-first-smartpart-going/
slug: cab-scsf-and-getting-that-first-smartpart-going
wp_id: 542
original_url: https://compositecode.blog/2006/09/12/cab-scsf-and-getting-that-first-smartpart-going/
categories:
- Uncategorized Bits
tags: []
excerpt: Read ** First (bottom of entry) – then continue – Ok, so my first task that I’ve set out to complete is to get an actual SmartPart displayed. I’ve dug through the documentation and hands on lab that are available at this point and must say that I’m somewhat unhappy with the documentation available at this …
---

*Read **\*\*** First (bottom of entry) – then continue* – Ok, so my first task that I’ve set out to complete is to get an actual SmartPart displayed.  I’ve dug through the documentation and hands on lab that are available at this point and must say that I’m somewhat unhappy with the documentation available at this point.  So with that I’m going to start writing up some of these how-to things as I work through this.  So at some point I might possibly put together and submit some of these things via a book on CAB and SCSF.  But I digress, back to the topic at hand, how to get a SmartPart displayed on screen.

So here’s the approach to getting a SmartPart to display on a simple old screen.

First start a standard Guidance Package based SCSF/CAB Based Application.

[![Smart Client Application](http://adronbhall.com/photos/random_screen_captures_and_other_assorted_stuff/images/412/425x305.aspx)](http://adronbhall.com/photos/random_screen_captures_and_other_assorted_stuff/picture412.aspx)

Set the root namespace next.  Feel free to uncheck the “Show related documentation after running the recipe”.

[![](http://adronbhall.com/photos/random_screen_captures_and_other_assorted_stuff/images/413/425x291.aspx)](http://adronbhall.com/photos/random_screen_captures_and_other_assorted_stuff/picture413.aspx)

The completed project should display as below.

[![](http://adronbhall.com/photos/random_screen_captures_and_other_assorted_stuff/images/414/original.aspx)](http://adronbhall.com/photos/random_screen_captures_and_other_assorted_stuff/picture414.aspx)

At this point the skeleton of the project is available.  At this point I deemed it necessary to split the default Shell up a little bit.  Navigate to the ShellForm.cs file in the **Shell** Project.  Bring up the ShellForm.cs file and delete the DeckWorkspace control that is currently on the page.

[![](http://adronbhall.com/photos/random_screen_captures_and_other_assorted_stuff/images/415/original.aspx)](http://adronbhall.com/photos/random_screen_captures_and_other_assorted_stuff/picture415.aspx)

Once you’ve deleted the DeckWorkspace do a quick build by hitting Ctrl+Shift+B.  You should get two errors and a few warnings as displayed below.

[![](http://adronbhall.com/photos/random_screen_captures_and_other_assorted_stuff/images/416/original.aspx)](http://adronbhall.com/photos/random_screen_captures_and_other_assorted_stuff/picture416.aspx)

Double click on the #5 error and the ShellForm.cs file will open up.  Delete the line of code that it links to.

\_layoutWorkspace.Name = WorkspaceNames.LayoutWorkspace;

then do the same for the #6 error.  Delete that line of code.

Microsoft.Practices.CompositeUI.SmartParts.ISmartPartInfoProvider ensureProvider = this;

Next open the primary ShellForm back up and drop a split container on the screen.  Name it splitPrimaryDivider for good measure and to give it a non-default name.  Next drag a DeckWorkspace on each section of the screen split.  Click on the task arrow…

![](http://adronbhall.com/photos/random_screen_captures_and_other_assorted_stuff/images/418/original.aspx)

 …and select Dock in parent container.  This will push the corners of the DeckWorkspace into the edges of the respective split sections.

[![](http://adronbhall.com/photos/random_screen_captures_and_other_assorted_stuff/images/417/original.aspx)](http://adronbhall.com/photos/random_screen_captures_and_other_assorted_stuff/picture417.aspx)

Name the right hand side name for the DeckWorkspace to deckPrimaryContent.  Name the other DeckWorkspace to deckLeftItems.

At this point open up the Infrastructure.Layout Project and delete the three files; Module.cs, ShellLayoutView.cs, and ShellLayoutViewPresenter.cs.  Now the application can actually be executed and the shell will display.

Now one can get down to getting some SmartPart Components to display in the Shell.  The tasks left to get the DeckWorkspace to display the deckPrimaryContent and deckLeftItems SmartParts is;

1. Place some controls on the SmartParts so we can make them do something and also be able to tell when they display (the standard gray on gray doesn’t really help us).- Create an interface to describe the methods needed to show the SmartParts in the Shell.- Create a WorkItem Class to implement WorkItem and show the SmartParts.- Write code in the ModuleInit to actually start the application and begin the loading process.

*PLACE PICTURES HERE FOR CONTROLS ON PAGE*

Create in the Infrastructure.Layout Project a ShowInShell.cs file.  Toss in an interface to use to pass SmartParts in for display.

using System;
using System.Collections.Generic;
using System.Text;
// Added Reference
using Microsoft.Practices.CompositeUI.SmartParts;

namespace MySmartClientTest.Infrastructure.Layout
{
 public interface IShowInShell
 {
  void Show(IWorkspace sideBar, IWorkspace content);
 }
}

Create a WorkItem Class to implement the WorkItem and IShowInShell interface to show the SmartParts.  Add a directory (just to keep things neat) name WorkItems to the Infrastructure.Module and then place a file called MyWorkItem.cs in the Project Folder.  Before adding any code make a reference to the MySmartClientTest.  You might need to add a few using references, which are listed below and then just toss in the following code.

// Added References
using Microsoft.Practices.CompositeUI;
using Microsoft.Practices.CompositeUI.SmartParts; // For the IWorkspace implementation.
// Added Local Projects
using MySmartClientTest.Infrastructure.Layout;

public class MyWorkItem : WorkItem, IShowInShell
{
 private IWorkspace contentWorkspace;
 public IWorkspace ContentWorkspace
 {
  get { return contentWorkspace; }
 }

public void Show(IWorkspace sideBar, IWorkspace content)
{
  contentWorkspace = content;

  //this.Items.AddNew<MainContentSmartPart>(“MainContent”);

  MainContentSmartPart mainContentView = this.Items.AddNew<MainContentSmartPart>();
  LeftMenuSmartPart leftMenuView = this.Items.AddNew<LeftMenuSmartPart>();

  sideBar.Show(leftMenuView);
  content.Show(mainContentView);
  this.Activate();
 }

 protected override void OnActivated()
 {
  base.OnActivated();
 }
}

At this point just click on old F5 and run that dog…

…ok so at this point I ran into a stupid problem.  The name according to what I’ve given then project is too long.  ?!  Stupid stupid problem to have…   so anyway.  Hopefully you read this line first because I don’t feel like changing the text.**\*\***
