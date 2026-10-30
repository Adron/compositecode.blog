---
title: TeamCity Build Notification Tools
date: 2008-06-09 02:19:07 -0700
last_modified_at: 2008-06-09 02:19:07 -0700
permalink: /2008/06/09/teamcity-build-notification-tools/
slug: teamcity-build-notification-tools
wp_id: 290
original_url: https://compositecode.blog/2008/06/09/teamcity-build-notification-tools/
categories:
- Uncategorized Bits
tags: []
excerpt: For the .NETters that use TeamCity there are two primary notification tools. The first is a tray icon tool and the second is a VS.NET plug-in. Both of these notification tools can be found on the TeamCity Build Server Site. Go to the user settings section and download the notification tools. I’m just going to …
---

For the .NETters that use TeamCity there are two primary notification tools.  The first is a tray icon tool and the second is a VS.NET plug-in.

Both of these notification tools can be found on the TeamCity Build Server Site.  Go to the user settings section and download the notification tools.  I’m just going to go over the tray icon notification tool right now and maybe the VS.NET notification tool add in later.

[![](/images/adronhall.smugmug.com/photos/308421036_iGM4t-M.png)](http://adronhall.smugmug.com/gallery/5110570_UDDQt/1/308421036_iGM4t)

For the tray icon tool go through the installation steps.  I left the default installation path as is, and suggest that you do the same.  When it is complete I let the installation start the *tray icon notification tool*.  When it pops up it will prompt you for your user name and password.

[![](/images/adronhall.smugmug.com/photos/308421042_R769j-M.png)](http://adronhall.smugmug.com/gallery/5110570_UDDQt/1/308421042_R769j)

[![](/images/adronhall.smugmug.com/photos/308421047_pDGAn-M.png)](http://adronhall.smugmug.com/gallery/5110570_UDDQt/1/308421047_pDGAn)

[![](/images/adronhall.smugmug.com/photos/308421053_m2MFY-M.png)](http://adronhall.smugmug.com/gallery/5110570_UDDQt/1/308421053_m2MFY)

[![](/images/adronhall.smugmug.com/photos/308421059_4LVUi-M.png)](http://adronhall.smugmug.com/gallery/5110570_UDDQt/1/308421059_4LVUi)

If you haven’t entered a URI for the Server you want to be notified about, it will prompt you for the specific URI.

[![](/images/adronhall.smugmug.com/photos/308421065_MtuRb-M.png)](http://adronhall.smugmug.com/gallery/5110570_UDDQt/1/308421065_MtuRb)

Double click the tray icon and the screen below should load in your default browser.

[![](/images/adronhall.smugmug.com/photos/308421068_NNKPo-M.png)](http://adronhall.smugmug.com/gallery/5110570_UDDQt/1/308421068_NNKPo)

Click on add a rule.  The “Add New Rule” screen will come up.  I usually select to “Watch builds from selected build configurations:” and select the specific builds I want to watch.  Under the “Send notification when:” section I set things up so that I’ll know when the build fails and is successful – cuz I dig success and want to know about it too – and I set things up so that it really only triggers if the build succeeds after a failure or it fails after a success.  Really only changes in the status are what really needs to be known.

[![](/images/adronhall.smugmug.com/photos/308421077_8Cs43-M.png)](http://adronhall.smugmug.com/gallery/5110570_UDDQt/1/308421077_8Cs43)[![](/images/adronhall.smugmug.com/photos/308421081_iXsrp-M.png)](http://adronhall.smugmug.com/gallery/5110570_UDDQt/1/308421081_iXsrp)

I also put the responsibility changes check box to true since I administer the build server at my current position I like to know if or when people are going to work on a broken build.  Some times the build server is actually the problem and particular pieces of the build are broken because it doesn’t have the correct GAC configuration or some other element has changed.  These things need resolved by the administrator so I stay prepared by watching the changes of responsibility.

[![](/images/adronhall.smugmug.com/photos/308421087_6jetb-M.png)](http://adronhall.smugmug.com/gallery/5110570_UDDQt/2/308421087_6jetb)

Ahhh yeah, success!

[![](/images/adronhall.smugmug.com/photos/308421093_uzaak-M.png)](http://adronhall.smugmug.com/gallery/5110570_UDDQt/2/308421093_uzaak)

[![kick it on DotNetKicks.com](http://www.dotnetkicks.com/Services/Images/KickItImageGenerator.ashx?url=http%3a%2f%2fadronbhall.com%2fblogs%2ftechnology__software_development%2farchive%2f2008%2f06%2f09%2f7201.aspx&bgcolor=3333FF&cfgcolor=CC3300)](http://www.dotnetkicks.com/kick/?url=http%3a%2f%2fadronbhall.com%2fblogs%2ftechnology__software_development%2farchive%2f2008%2f06%2f09%2f7201.aspx)

Technorati Tags: [TeamCity](http://technorati.com/tags/TeamCity),[Build Notification](http://technorati.com/tags/Build%20Notification),[JetBrains](http://technorati.com/tags/JetBrains),[ReSharper](http://technorati.com/tags/ReSharper)

del.icio.us Tags: [TeamCity](http://del.icio.us/popular/TeamCity),[Build Notification](http://del.icio.us/popular/Build%20Notification),[JetBrains](http://del.icio.us/popular/JetBrains),[ReSharper](http://del.icio.us/popular/ReSharper)
