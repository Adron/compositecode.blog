---
title: Smugmug and Windows Live Writer Plugin, via Teamprise Source Client
date: 2008-04-21 16:14:00 -0700
last_modified_at: 2008-04-21 16:14:00 -0700
permalink: /2008/04/21/smugmug-and-windows-live-writer-plugin-via-teamprise-source-client/
slug: smugmug-and-windows-live-writer-plugin-via-teamprise-source-client
wp_id: 309
original_url: https://compositecode.blog/2008/04/21/smugmug-and-windows-live-writer-plugin-via-teamprise-source-client/
categories:
- Uncategorized Bits
tags: []
excerpt: I officially joined the effort for the Windows Live Writer called smugmug4writer for Smugmug, currently maintained by Chris Patterson. I've found myself using the plugin so much while writing entries that I finally decided I'd contact him and see about doing some additions. If any readers use this application, make sure to leave a comment …
---

I officially joined the effort for the Windows Live Writer called [smugmug4writer](http://www.codeplex.com/smugmug4writer) for [Smugmug](http://www.smugmug.com/), currently maintained by Chris Patterson.  I've found myself using the plugin so much while writing entries that I finally decided I'd contact him and see about doing some additions.  If any readers use this application, make sure to leave a comment or three about what additions you might like.

Like any project on [CodePlex](http://www.codeplex.com/) you need to setup the utility to get the code out of their TFS (Team Foundation Server) Source Repository.  This is done with some tools [Brad Wilson](http://bradwilson.typepad.com) and crew are responsible for.  There is also another solution offered by [Teamprise](http://www.teamprise.com/) to connect to [CodePlex](http://www.codeplex.com/) Projects.

To download the tool for working on one of the [CodePlex](http://www.codeplex.com/) Open Source projects swing over to the [CodePlex](http://www.codeplex.com/) Open Source Project titled "[CodePlex Source Control Client](http://www.codeplex.com/CodePlexClient)".  To grab the [Teamprise](http://www.teamprise.com/) client swing over to their site.  You'll also need to go pick up a [free (as in beer) license](http://www.woodwardweb.com/teamprise/000339.html) for use.  It is subject to "approval" and all but I think they're still sending them out to [CodePlex](http://www.codeplex.com/) users.

Once I downloaded the [Teamprise](http://www.teamprise.com/) Client I went to connecting up to the project.  First off go to the actual project page on CodePlex to find the specific details for connecting.  The connection details are located on the right hand side of the "Connection to Source Control Server" section.

[![](/images/adronhall.smugmug.com/photos/283205893_2VgVm-L.png)](http://adronhall.smugmug.com/gallery/4773830_JAHCk/1/283205893_2VgVm)

I got the [Teamprise](http://www.teamprise.com/) Explorer downloaded and installed.  Received my key also and entered that.  The first thing that pops up is the login details screen.  The odd thing is the \_cp is stuck on the end of the username regardless of what the [CodePlex](http://www.codeplex.com/) username you have is.

[![](/images/adronhall.smugmug.com/photos/283205922_gXwMM-L.png)](http://adronhall.smugmug.com/gallery/4773830_JAHCk/1/283205922_gXwMM)

The next that will pop is an activation screen.  I just hit auto-activate and it took care of this itself.

[![](/images/adronhall.smugmug.com/photos/283205948_mpSuK-L.png)](http://adronhall.smugmug.com/gallery/4773830_JAHCk/1/283205948_mpSuK)

Below is the display of what the full screen looks like.  If you click on the root of the project (the $ symbol) in the Source Control section of the Teamprise Application below and right click…

[![](/images/adronhall.smugmug.com/photos/283206212_AtEXk-L.png)](http://adronhall.smugmug.com/gallery/4773830_JAHCk/1/283206212_AtEXk)

…this menu will appear.  Here you'll see what are generally the standard options for access to TFS.  First things first, set your working folder for TFS.  This is the area where the code will be put.

[![](/images/adronhall.smugmug.com/photos/283205970_KMBnS-L.png)](http://adronhall.smugmug.com/gallery/4773830_JAHCk/1/283205970_KMBnS)

The working folder will prompt as below, click on Browse and select a directory.  I highlighted where I've added the specific directory that I want my code to be placed in.

[![](/images/adronhall.smugmug.com/photos/283206075_YAwuS-L.png)](http://adronhall.smugmug.com/gallery/4773830_JAHCk/1/283206075_YAwuS)

Next I right clicked on the root again and selected **Get Specific Version…**, the reason being that I don't trust TFS with the simple **Get Latest Version** command.  I've been rubbed wrong by its performance and behavior in the past.  So I like to play it rough with ole' TFS.

[![](/images/adronhall.smugmug.com/photos/283206103_2bo8z-L.png)](http://adronhall.smugmug.com/gallery/4773830_JAHCk/1/283206103_2bo8z)

The next screen gives the standard options for getting a specific version.  Since there is nothing in the directory then I figured nothing needed selecting (here's to hoping TFS behaves as designed).

[![](/images/adronhall.smugmug.com/photos/283206129_YDZj9-L.png)](http://adronhall.smugmug.com/gallery/4773830_JAHCk/1/283206129_YDZj9)

Next the application begins getting the latest files.  Notice that the notification dialog is rather boring and plain.  The real info is now displayed in the application, which has lost focus, but shows the active status down in the lower right hand side.  I've highlighted it below.

[![](/images/adronhall.smugmug.com/photos/283206162_Z3pPp-L.png)](http://adronhall.smugmug.com/gallery/4773830_JAHCk/1/283206162_Z3pPp)

After all is retrieved the files are no longer shadowed out in the Source Control area.  Navigate to where you placed them in the directory structure on your machine and you'll find that they've been downloaded accordingly.

[![](/images/adronhall.smugmug.com/photos/283206240_BJKZp-L.png)](http://adronhall.smugmug.com/gallery/4773830_JAHCk/2/283206240_BJKZp)

…now get started on some open source CodePlex Projects.  I've explained it, so ya aint got no excuse do ya!  ![Stick out tongue [:P]](/emoticons/emotion-4.gif)

[![kick it on DotNetKicks.com](http://www.dotnetkicks.com/Services/Images/KickItImageGenerator.ashx?url=http%3a%2f%2fadronbhall.com%2fblogs%2ftechnology__software_development%2farchive%2f2008%2f04%2f21%2f6939.aspx&bgcolor=3333FF&cfgcolor=CC3300)](http://www.dotnetkicks.com/kick/?url=http%3a%2f%2fadronbhall.com%2fblogs%2ftechnology__software_development%2farchive%2f2008%2f04%2f21%2f6939.aspx)

Technorati Tags: [CodePlex](http://technorati.com/tags/CodePlex),[Teamprise](http://technorati.com/tags/Teamprise),[TFS](http://technorati.com/tags/TFS),[Team Foundation Server](http://technorati.com/tags/Team%20Foundation%20Server),[Source Control](http://technorati.com/tags/Source%20Control),[smugmug4writer](http://technorati.com/tags/smugmug4writer)

del.icio.us Tags: [CodePlex](http://del.icio.us/popular/CodePlex),[Teamprise](http://del.icio.us/popular/Teamprise),[TFS](http://del.icio.us/popular/TFS),[Team Foundation Server](http://del.icio.us/popular/Team%20Foundation%20Server),[Source Control](http://del.icio.us/popular/Source%20Control),[smugmug4writer](http://del.icio.us/popular/smugmug4writer)
