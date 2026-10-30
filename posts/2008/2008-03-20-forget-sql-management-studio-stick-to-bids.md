---
title: Forget SQL Management Studio, Stick to BIDS
date: 2008-03-20 10:15:33 +0000
last_modified_at: 2008-03-20 10:15:33 +0000
permalink: /2008/03/20/forget-sql-management-studio-stick-to-bids/
slug: forget-sql-management-studio-stick-to-bids
wp_id: 320
original_url: https://compositecode.blog/2008/03/20/forget-sql-management-studio-stick-to-bids/
categories:
- Uncategorized Bits
tags: []
excerpt: Ok, so lately there has been a decent bit of frustration from our crew about how to deploy a Analysis Services Project from BIDS to XMLA without going into SQL Management Studio and going through that whole mess. Well my fellow coworker Xander got a solution figured out for this. One of the other key …
---

Ok, so lately there has been a decent bit of frustration from our crew about how to deploy a Analysis Services Project from BIDS to XMLA without going into SQL Management Studio and going through that whole mess.  Well my fellow coworker Xander got a solution figured out for this.  One of the other key side effects is that one doesn’t actually need the database/cube itself physically on the box once this is done, but simply the project itself (it helps to have a cube to push to).

First just setup the actual XMLA build process.  To do this click on *Tools* and then *External Tools*.

[![](/images/adronhall.smugmug.com/photos/268254317_oMZWm-M.png)](http://adronhall.smugmug.com/gallery/4552561_QqNJZ/1/268254317_oMZWm)

Click on Add and in the Title, Command, Arguments, and Initial Directory enter the following;

[![](/images/adronhall.smugmug.com/photos/268254329_VQSYm-M.png)](http://adronhall.smugmug.com/gallery/4552561_QqNJZ/1/268254329_VQSYm)

- Title:  Build XMLA- Command: Microsoft.AnalysisServices.Deployment.exe- Arguments: “***-enter project name here-.***asDatabase” /d /o:..\..\Project.xmla- Initial Directory: $(ProjectDir)\bin- Check the “prompt for arguments” option.- Check the “output window” option.

When the prompt comes up during execution of the Build XMLA you must remember to enter your project name exactly so that the database name matches.

Select OK and then click on *Tools* again.  You will now see a *Build XMLA* option on the *Tools* menu.

[![](/images/adronhall.smugmug.com/photos/268254338_EC9iD-M.png)](http://adronhall.smugmug.com/gallery/4552561_QqNJZ/1/268254338_EC9iD)

Now open a *new project*.  Since it is the standard template example, I’m going to open up *AdventureWorks*.

Make sure just before executing this that you have done a clean build of the project.  Without a build the necessary \*.aspDatabase file won’t be available.  Once you have opened and built the solution then click on the *Tools* -> *Build XMLA* option.  The argument prompt will appear.  Enter the project name as shown in the image.  Now you should see the output window display the status.

[![](/images/adronhall.smugmug.com/photos/268254261_VAUZA-M.png)](http://adronhall.smugmug.com/gallery/4552561_QqNJZ/1/268254261_VAUZA)

[![](/images/adronhall.smugmug.com/photos/268254278_QJqkk-M.png)](http://adronhall.smugmug.com/gallery/4552561_QqNJZ/1/268254278_QJqkk)

After execution navigate to the project root and you will find the “Project.xmla” file.  Now you’re good to go without fighting with SQL Management Studio all the time, nor needing a physical installation of your database/cube.

[![](/images/adronhall.smugmug.com/photos/268254290_bWdvH-M.png)](http://adronhall.smugmug.com/gallery/4552561_QqNJZ/1/268254290_bWdvH)

del.icio.us Tags: [BIDS](http://del.icio.us/popular/BIDS),[SQL Server 2005](http://del.icio.us/popular/SQL%20Server%202005),[Tools](http://del.icio.us/popular/Tools),[XMLA](http://del.icio.us/popular/XMLA)

Technorati Tags: [BIDS](http://technorati.com/tags/BIDS),[SQL Server 2005](http://technorati.com/tags/SQL%20Server%202005),[Tools](http://technorati.com/tags/Tools),[XMLA](http://technorati.com/tags/XMLA)
