---
title: CAB, SCSF, and MVP Pattern Development
date: 2006-09-04 05:41:00 -0700
last_modified_at: 2006-09-04 05:41:00 -0700
permalink: /2006/09/04/cab-scsf-and-mvp-pattern-development/
slug: cab-scsf-and-mvp-pattern-development
wp_id: 543
original_url: https://compositecode.blog/2006/09/04/cab-scsf-and-mvp-pattern-development/
categories:
- Uncategorized Bits
tags: []
excerpt: Ok, so I've started on my own Composite UI Application Block (CAB) based Smart Client Software Factory Application (SCSF). My first sentiment, after studying this on and off for a few weeks, is that this is no simple approach. I've looked at the little charts and flow diagrams that tell the high altitude story of …
---

Ok, so I've started on my own Composite UI Application Block (CAB) based Smart Client Software Factory Application (SCSF).

My first sentiment, after studying this on and off for a few weeks, is that this is no simple approach. I've looked at the little charts and flow diagrams that tell the high altitude story of how these things are supposed to work together. With all the WorkItems, Views, SmartParts, and all this other stuff one has to keep up with the CAB can become a very complex application for a single individual to keep up with. I am aware of course that the CAB and SCSF are designed to be used by a team or group of developers working on and supporting a single application. In this scenario though it is just me, myself, and I working on this thing. My current project at work also has each developer working inside one single vertical scope of the application, which dictates that we each must learn the CAB, SCSF, and every other layer of the application. From a managerial perspective I'm not following the logic, but from a developers perspective I have been euphoric that I will be able to work with each aspect of the application. Lots of experience ensue!

So on with what I've actually setup using the SCSF and CAB.

So with that let me start with some basic explanations of what in the hell is going on with the various aspects of these application block and factory libraries. Both the application block (CAB) and the factory (SCSF) are setup to implement a Model-View-Presenter (MVP) type pattern. The whole point of this is so that various aspects of the development for an application user interface can be split out to different developers. One can work on business use cases by working with the WorkItems, another can simultaneously work on the user interface by building SmartParts.

So if I have it straight the following are a simple description of the various parts of the SCSF, CAB, and the MVP Pattern.

- Modules are composed of a set of services, WorkItems, SmartParts, controllers, business entities, and the Module Initilization class, which initializes the module's WorkItems.
  - Services:  Module Services are objects that can be registered once by using the Service attribute and then referenced from any component in WorkItem.
  - WorkItems:  WorkItems are run-time containers of components that collaborate to complete a use case.  It contains the following:
    - Start-up (initialization) that begins the use case.
    - State that is shared by components collaborating in the use case.  State can be persisted by calling the Load and Save methods on WorkItem.  State can be persisted to any storage medium by using an infrastructure service that implements IStatePersistenceService.  There are built in implementations called;  FileStatePersistenceService, which persists the WorkItem to a file in the same directory as the executable and IsolateStorageStatePersistenceService, which persists the WorkItem to a file in Isolated Storage.
    - Contoller classes that act on the state and resources.
    - View casses that interact with their controllers and reference state.
    - Tear-down code that cleans up the application.
  - SmartParts:  SmartParts provide the visual elements in the application.  These are seperated from the application so a single person can be dedicated to just SmartPart development if need be.
  - Controllers:  These implement the business logic behind the view.
  - Business Entities:  These are the standard business objects that any application type should use to utilize business cases and apply logic to during the use of an application.
  - Module Initialization Class:  This is what is responsible for starting and loading the application.  When one starts the application this initialization begins.
- Views
- Presenters

Another few specific things the CAB provides are below;

- Infrastructure Services that can be used in applications being developed.  Custom services and infrastructure services can also be built and added to applications.  The application block provides the following infrastructure;
  - Catalog Reader Service
  - Module Loader Service
  - Authentication Service
  - State Persistence Service

So these are my definitions so far, I hope to be able to add and flesh out each point with more specific and descriptive detail in coming CAB/SCSF entries that I will be making.

As one can see, especially if it is their first time, it is not a small list of things to keep up with.  This is merely the simple CAB/SCSF 101 Introductory stuff to learn and keep up with too, it's not "advanced CAB/SCSF"!  So my next entry will hopefully include some working samples of stuff, that aren't duplications of the few hands on labs and rare code snippets here and there.  I hope to help make this model of application development proliferate a little bit.  It never hurts to push one self either.  🙂
