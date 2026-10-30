---
title: Reactive Programs and Windows Workflow Ramblings
date: 2007-06-27 15:42:58 -0700
last_modified_at: 2007-06-27 15:42:58 -0700
permalink: /2007/06/27/reactive-programs-and-windows-workflow-ramblings/
slug: reactive-programs-and-windows-workflow-ramblings
wp_id: 463
original_url: https://compositecode.blog/2007/06/27/reactive-programs-and-windows-workflow-ramblings/
categories:
- Uncategorized Bits
tags: []
excerpt: I’ve started working heavily with Windows Workflow. It seems this foundation from Microsoft is being heavily undersold in my opinion. What one can do with this base is massive, at least for enterprise solutions, and in many a case for almost any type of solution. This type of graphical design of workflow directly mapped to …
---

I’ve started working heavily with Windows Workflow.  It seems this foundation from Microsoft is being heavily undersold in my opinion.  What one can do with this base is massive, at least for enterprise solutions, and in many a case for almost any type of solution.  This type of graphical design of workflow directly mapped to code has been needed for ages, oft promised, mostly just vaporware until now.

This is an entry documenting some of my first flailing through some samples I’ve been tossing together.

Sample 1

First I started a basic Sequential Workflow Console Application from Visual Studio by starting a new project.

[![](http://adronbhall.com/photos/random_screen_captures_and_other_assorted_stuff/images/4895/original.aspx)](http://adronbhall.com/photos/random_screen_captures_and_other_assorted_stuff/picture4895.aspx)

Once the application is open I renamed the initial workflow file accordingly, since I have an obsessive compulsive issue with the default filenames and such.

[![](http://adronbhall.com/photos/random_screen_captures_and_other_assorted_stuff/images/4896/original.aspx)](http://adronbhall.com/photos/random_screen_captures_and_other_assorted_stuff/picture4896.aspx)

Now that I’ve settled my obsession with things not being “default” I moved on to tossing some cool workflow controls into the SequentialWorkflow.cs file.  The first two I dropped in was a **Code Control** and a **Delay Control**.  After dropping these two controls onto the page I ended up with the diagram below.

[![](http://adronbhall.com/photos/random_screen_captures_and_other_assorted_stuff/images/4897/original.aspx)](http://adronbhall.com/photos/random_screen_captures_and_other_assorted_stuff/picture4897.aspx)

There was one problem.  I wanted the delay to occur before the Code Control executes.  With the Workflow Extensions Diagramming it is ridiculously easy to change it, by simply dragging and dropping the delay in front of the Code Control I resolved my whole dilemma.

[![](http://adronbhall.com/photos/random_screen_captures_and_other_assorted_stuff/images/4898/original.aspx)](http://adronbhall.com/photos/random_screen_captures_and_other_assorted_stuff/picture4898.aspx)

Now that everything in the world was right I tossed some petty Console.Write\* code into each of the controls.  The code I entered was super basic for this example.

1 using System;

    2 using System.Workflow.Activities;

    3

    4 namespace WorkflowSampeSequential

    5 {

    6     public sealed partial class SequentialWorkflow : SequentialWorkflowActivity

    7     {

    8         public SequentialWorkflow()

    9         {

   10             InitializeComponent();

   11         }

   12

   13         private void delayFor30Seconds\_InitializeTimeoutDuration(object sender, EventArgs e)

   14         {

   15             Console.WriteLine(“Pausing for 30 seconds.”);

   16         }

   17

   18         private void CodeActivityNumeroOne\_ExecuteCode(object sender, EventArgs e)

   19         {

   20             Console.Write(“This is the console writing doing a \”Console.Write\”.  “);

   21             Console.WriteLine(“This is the \”Console.WriteLine\”.”);

   22         }

   23     }

   24 }

So with that snippet of code one can see how the example works to step through each part of the Workflow. My next example is going to be a little more elaborate. So now that the simple one is setup, cuz it’s always good to have that simple “working” example, my next workflow related entry will have some real meat to it.
