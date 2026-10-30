---
title: Community Server on Vista
date: 2007-04-28 16:32:43 -0700
last_modified_at: 2007-04-28 16:32:43 -0700
permalink: /2007/04/28/community-server-on-vista/
slug: community-server-on-vista
wp_id: 489
original_url: https://compositecode.blog/2007/04/28/community-server-on-vista/
categories:
- Uncategorized Bits
tags: []
excerpt: For one of my main personal projects I’ve been using Community Server from Telligent Software. It’s a pretty awesome package of Web Applications. Since I’m now using Vista – as current readers know now – there are a few work arounds to seting up IIS 7 and SQL Server 2005 so that Community Server will run. I …
---

For one of my main personal projects I’ve been using Community Server from Telligent Software.  It’s a pretty awesome package of Web Applications.  Since I’m now using Vista – as current readers know now – there are a few work arounds to seting up IIS 7 and SQL Server 2005 so that Community Server will run.

I tried running the user.sql file on the SQL Server setup I have.  The SQL Server 2005 setup and IIS 7 setup are basically default, at least default for Vista.  For more on that read [my last Vista Post](http://fill.this.in.com).  I set the SQL Server Security settings to integrated security per the instructions but when runing the user.sql file there seems to be no ASPNET user now.

Since I knew that my point of deployment would be a straight copy of the database that I have local, I decided to give the cs\_3.0\_CreateFullDatabase.sql file a go round.  It ran flawlessly since my logged in user had dbo rights.  So unless you want everything 100% identical, I’d run this shortcut to get it setup locally for development.

Next per the default instructions I went ahead and created a default community.

**exec dbo.cs\_system\_CreateCommunity ‘localhost/cs’, ‘dev’, ‘admin@example.org’, ‘AdminUserName’, ‘AdminPassword’, 0, 0**

The command executed perfectly without flaw.  Now that the database was all setup proper for the website, I moved right along with installing the website.

For the website, setup was insanely simple.  I did however have to do one thing that was a sidestep from what is suggested.  Since Vista won’t let me run apps properly that need windows, forms, or other authentications on the localhost instance of IIS I needed to run the Community Server via the virtual server.

**Step one** for setting up Community Server 7 for this particular scenario was to unzip the download.  Once unzipped then open the solution file.  The solution file will open the entire project (if you get any errors shoot me a comment) list.

Step Two is also almost as simple.  Right click on the “**CommunityServerWeb20 (Internal)**” project and click on the “**Properties**” option.  From there click on the “**Web**” tab on the left hand side of the “**Properties”** Screen.  Mid screen you will see a “Servers” section that has two radio button options.  The out of the box (zip) option is the “Use IIS Web Server” option, change it to “**Use Visual Studio Development Server**“.

I haven’t tried any of the other options, but this selection should get one up and running with Community Server 7.0.  Now, I’m off to figure out what I have to do next!
