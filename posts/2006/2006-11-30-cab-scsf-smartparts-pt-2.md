---
title: CAB & SCSF [SmartParts] Pt. 2
date: 2006-11-30 13:41:58 +0000
last_modified_at: 2006-11-30 13:41:58 +0000
permalink: /2006/11/30/cab-scsf-smartparts-pt-2/
slug: cab-scsf-smartparts-pt-2
wp_id: 524
original_url: https://compositecode.blog/2006/11/30/cab-scsf-smartparts-pt-2/
categories:
- Uncategorized Bits
tags: []
excerpt: Actually Writing some Code! So now that there is the basic structure of the application setup I started delving into the code. The first thing I glanced and decided to straighten out was the fact that left and right workspace along with some other Constants where still declared in the Infrastructure.Interface Project under the Constants …
---

## Actually Writing some Code!

- So now that there is the basic structure of the application setup I started delving into the code.  The first thing I glanced and decided to straighten out was the fact that left and right workspace along with some other Constants where still declared in the Infrastructure.Interface Project under the Constants folder in the WorkspaceNames.cs file.  I removed everything and just left the following:

>     public class WorkspaceNames
>
>     {
>
>         public const string LayoutWorkspace = “LayoutWorkspace”;
>
>     }

- Some other code I went ahead and removed was located in the ModuleController.cs file.  Any code that is related to the tool strip I removed from the Run() Method and deleted the method dedicated to adding items to the tool strip.

  - The first files to dig into are the ModuleController.cs and WorkspaceNames.cs file located in the Constants application directory.  I opened those up for the following code surgery.

    - In addition to those two files I also created another file to store the constants that will be used for the various Views.  I placed this file in the Constants directory and names it simply Views.cs.

      - To the Views.cs file I added the following constant declarations:

>     public class Views
>
>     {
>
>         public const string TripDestinations = “TripDestinations”;
>
>         public const string TripManagement = “TripManagement”;
>
>         public const string TripPurpose = “TripPurpose”;
>
>         public const string TripTypes = “TripTypes”;
>
>     }

- To the WorkspaceNames.cs file I added the single constant:

>     /// <summary>
>
>     /// Constants for workspace names.
>
>     /// </summary>
>
>     public class WorkspaceNames : TravelTrackerSmartClient.Infrastructure.Interface.Constants.WorkspaceNames
>
>     {
>
>         public const string TripTabWorkspace = “TripTabWorkSpace”;
>
>     }

- In the ModuleController.cs file I added the following code.  To read more about setting up Views read the documentation link that is commented out in this AddViews() method.  (Unless the Microsoft Team has removed it in current distributions)

>         private void AddViews()
>
>         {
>
>             WorkItem.Items.AddNew<TripDestinations>(Constants.Views.TripDestinations);
>
>             WorkItem.Items.AddNew<TripManagement>(Constants.Views.TripManagement);
>
>             WorkItem.Items.AddNew<TripPurpose>(Constants.Views.TripPurpose);
>
>             WorkItem.Items.AddNew<TripTypes>(Constants.Views.TripTypes);
>
>         }

- Once all of this is complete I now have an application that actually starts, loads the TravelTracker Project and on Run() adds each of the SmartPart Views into the WorkItem Items collection.  With this in place I can now wire up each of the specific event publications and subscriptions that will allow me to have each SmartPart displayed when a particular menu item is selected (or Tab Part).- To start wiring up the Subscription and Publications make a reference in the ModuleController:

> using Microsoft.Practices.CompositeUI.EventBroker;

- After adding that place some methods for the event subscriptions in the ModuleController.cs file and the respective event topic names to the constants file EventTopicNames.cs.

> ***EventTopicNames.cs***
>
>     public class EventTopicNames : TravelTrackerSmartClient.Infrastructure.Interface.Constants.EventTopicNames
>
>     {
>
>         public const string TripDestinationsClicked\_Event = “TripDestinationsClicked\_Event”;
>
>         public const string TripManagementClicked\_Event = “TripManagementClicked\_Event”;
>
>         public const string TripPurposeClicked\_Event = “TripPurposeClicked\_Event”;
>
>         public const string TripTypesClicked\_Event = “TripTypesClicked\_Event”;
>
>     }

> ***ModuleController.cs***
>
>         [EventSubscription(Constants.EventTopicNames.TripDestinationsClicked\_Event, ThreadOption.UserInterface)
>
>      
>   public void TripDestinationsClicked\_Handler(object sender, EventArgs e)
>
>         {}
>
>  
>
>         [EventSubscription(Constants.EventTopicNames.TripManagementClicked\_Event, ThreadOption.UserInterface)
>
>         public void TripManagementClicked\_Handler(object sender, EventArgs e)
>
>         {}
>
>  
>
>         [EventSubscription(Constants.EventTopicNames.TripPurposeClicked\_Event, ThreadOption.UserInterface)
>
>         public void TripPurposeClicked\_Handler(object sender, EventArgs e)
>
>         {}
>
>  
>
>         [EventSubscription(Constants.EventTopicNames.TripTypesClicked\_Event, ThreadOption.UserInterface)
>
>         public void TripTypesClicked\_Handler(object sender, EventArgs e)
>
>         {}

- At this point I actually, for readability, went back and changed in the ShellForm.cs code and events for the menu selections.  Along with that I added the event publications attributes and more.  The code when finished looks like this:

        [EventSubscription(Constants.EventTopicNames.TripDestinationsClicked\_Event, ThreadOption.UserInterface)]

        public void TripDestinationsClicked\_Handler(object sender, EventArgs e)

        {

            if (!WorkItem.SmartParts.Contains(Constants.Views.TripDestinations))

            {

                WorkItem.SmartParts.AddNew<TripDestinations>(Constants.Views.TripDestinations);

            }

 

            WorkItem.RootWorkItem.Workspaces[Constants.WorkspaceNames.TripTabWorkspace].Show(

                WorkItem.SmartParts.Get<TripDestinations>(Constants.Views.TripDestinations));

        }

Well, that’s that.  I’m all wired up.  The next step (Part 3, it’s coming soon) is to wire up some button pushin data entering GUI Interacing events, buttons, and other such items.  Stay tuned…
