---
title: Windows Workflow Increases Coolness Factor
date: 2007-06-28 17:04:00 -0700
last_modified_at: 2007-06-28 17:04:00 -0700
permalink: /2007/06/28/windows-workflow-increases-coolness-factor/
slug: windows-workflow-increases-coolness-factor
wp_id: 462
original_url: https://compositecode.blog/2007/06/28/windows-workflow-increases-coolness-factor/
categories:
- Uncategorized Bits
tags: []
excerpt: After making it through about 200+ pages of the book Essential Windows Workflow Foundation by Dharma Shukla and Bob Schmidt I discovered two capabilities that I really like about the Workflow Foundation. The first is the database tables provided via the Workflow SDK that are used for persistence and tracking. The second thing that caught …
---

After making it through about 200+ pages of the book [Essential Windows Workflow Foundation](http://www.awprofessional.com/title/0321399838) by Dharma Shukla and Bob Schmidt I discovered two capabilities that I really like about the Workflow Foundation.  The first is the database tables provided via the Workflow SDK that are used for persistence and tracking.  The second thing that caught my eye, which I had not even really thought about before, was the workflow display engine.  A part of the workflow foundation which provides actual graphical display of the workflow in a Visio Flowchart type fashion directly within an application.  Both of these sections I’m now going to elaborate on a little bit more, namely to show how to setup a basic installation of the database tables and how to put in place a workflow diagram into an application.

## **Workflow SQL Tracking and Persistence Tables**

Most of these steps can be found at the linked MSDN page, but I’ve extrapolated by own instructions below.  Also this seemed a partial necessity since I couldn’t find instructions for setting up the tracking and persistence tables I’m rolling my own.  The MSDN articles for the [persistence setup](http://msdn2.microsoft.com/en-us/library/aa349366.aspx) and [tracking setup](http://msdn2.microsoft.com/en-us/library/aa348821.aspx) are available if one needs a step by step.  My directions a bit more cut and to the point.

![Smile [:)]](/emoticons/emotion-1.gif)

First create a database for the tracking and persistence store to use such as “*WorkflowStore*“.  I know, real original.  But anyway, there are more important topics at hand!

Next find the SQL file **“*open the SQL script c:\WINDOWS\Microsoft.NET\Framework\v3.0\Windows Workflow Foundation\SQL\en\SqlTracking\_Schema.sql*“** and then run the **“*SQL script c:\WINDOWS\Microsoft.NET\Framework\v3.0\Windows Workflow Foundation\SQL\en\SqlTracking\_Logic.sql*“** file.  These two files take care of the tracking part of the workflow database.

After setting those up execute the SqlPersistenceService\_Schema.sql file and the SqlPersistenceService\_Logic.sql file to complete the persistence portion of the setup.

Now that the database is setup the respective web or application config files need to have some particulars added.  In the Services section of the config add the following:

**“<add type=”System.Workflow.Runtime.Tracking.SqlTrackingService, System.Workflow.Runtime, Version=3.0.00000.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35″ connectionString=”Initial Catalog=WorkflowTrackingStore;Data Source=localhost;Integrated Security=SSPI;”/>“**

for tracking and

**“<add type=”System.Workflow.Runtime.Hosting.SqlWorkflowPersistenceService, System.Workflow.Runtime, Version=3.0.00000.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35″ connectionString=”Initial Catalog=WorkflowPersistenceStore;Data Source=localhost;Integrated Security=SSPI;” UnloadOnIdle=”true”/>“**

for persistence.  For hosting the designer in a windows application stay tuned.  Until then, happy coding!

[![kick it on DotNetKicks.com](http://www.dotnetkicks.com/Services/Images/KickItImageGenerator.ashx?url=http://adronbhall.com/blogs/technology__software_development/archive/2007/07/01/4922.aspx)](http://www.dotnetkicks.com/kick/?url=http://adronbhall.com/blogs/technology__software_development/archive/2007/07/01/4922.aspx)
