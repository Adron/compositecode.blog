---
title: Team City Continuous Integration Build Server and VS.NET VCS Integration
date: 2008-06-06 10:10:23 +0000
last_modified_at: 2008-06-06 10:10:23 +0000
permalink: /2008/06/06/team-city-continuous-integration-build-server-and-vs-net-vcs-integration/
slug: team-city-continuous-integration-build-server-and-vs-net-vcs-integration
wp_id: 291
original_url: https://compositecode.blog/2008/06/06/team-city-continuous-integration-build-server-and-vs-net-vcs-integration/
categories:
- Uncategorized Bits
tags: []
excerpt: Starting a new project always requires a certain amount of setup, one of the primary goals of any development group these days should be continuous integration. This is something that is not expensive or time consuming to setup. Recently for a grand price of about zero dollars (except for my regular pay, so I suppose …
---

Starting a new project always requires a certain amount of setup, one of the primary goals of any development group these days should be continuous integration.  This is something that is not expensive or time consuming to setup.  Recently for a grand price of about zero dollars (except for my regular pay, so I suppose not truly zero dollars) I setup Team City, started a build process going, and got back to coding and research on next steps all within about 3-4 hours.  Mind you, two of those hours was stuck on a dumb problem because I “clicked” the wrong option in a drop down box.

NOTE: Click on any of the images for a solid full size image via [Smugmug](http://www.smugmug.com).

Get Visual SVN Installed.

[![](/images/adronhall.smugmug.com/photos/307379054_D5Akv-S.png)](http://adronhall.smugmug.com/gallery/5097270_6ynmt/1/307379054_D5Akv)

[![](/images/adronhall.smugmug.com/photos/307379062_PZheF-S.png)](http://adronhall.smugmug.com/gallery/5097270_6ynmt/1/307379062_PZheF)

As with most things, just leave the port as is.  INHO

[![](/images/adronhall.smugmug.com/photos/307379073_GMtiQ-S.png)](http://adronhall.smugmug.com/gallery/5097270_6ynmt/1/307379073_GMtiQ)

[![](/images/adronhall.smugmug.com/photos/307379085_ups64-S.png)](http://adronhall.smugmug.com/gallery/5097270_6ynmt/1/307379085_ups64)

[![](/images/adronhall.smugmug.com/photos/307379094_LCQV5-S.png)](http://adronhall.smugmug.com/gallery/5097270_6ynmt/1/307379094_LCQV5)

Go ahead and leave the “Start VisualSVN Server Manager” checked so we can add a repository and all that good stuff.

[![](/images/adronhall.smugmug.com/photos/307379097_WKR4N-S.png)](http://adronhall.smugmug.com/gallery/5097270_6ynmt/1/307379097_WKR4N)

This is the Visual SVN Microsoft Management Console plug in.  By far this is one of the most .NET friendly, Visual Studio friendly ways to use Subversion.  Go through and add your users, make sure one of them is your build account, and the respective groups that you want.  Once you are done adding the accounts and groups add a Repository.

[![](/images/adronhall.smugmug.com/photos/307379106_TXur3-S.png)](http://adronhall.smugmug.com/gallery/5097270_6ynmt/1/307379106_TXur3)

[![](/images/adronhall.smugmug.com/photos/307379197_tacNY-S.png)](http://adronhall.smugmug.com/gallery/5097270_6ynmt/2/307379197_tacNY)

[![](/images/adronhall.smugmug.com/photos/307379180_2zo98-S.png)](http://adronhall.smugmug.com/gallery/5097270_6ynmt/2/307379180_2zo98)

Notice once you add a repository that there are three directories within the repository.

[![](/images/adronhall.smugmug.com/photos/307379123_ArgaW-S.png)](http://adronhall.smugmug.com/gallery/5097270_6ynmt/1/307379123_ArgaW)

[![](/images/adronhall.smugmug.com/photos/307379152_64bTh-S.png)](http://adronhall.smugmug.com/gallery/5097270_6ynmt/2/307379152_64bTh)

Once you get your repository created right click on it to get the “Copy URL to Clipboard” option.  This definitely beats needing to remember the path.

[![](/images/adronhall.smugmug.com/photos/307379157_saawq-S.png)](http://adronhall.smugmug.com/gallery/5097270_6ynmt/2/307379157_saawq)

Once you do this make sure to add the Visual SVN UI to get the integrated VS.NET features.

[![](/images/adronhall.smugmug.com/photos/307379206_QnFiE-S.png)](http://adronhall.smugmug.com/gallery/5097270_6ynmt/2/307379206_QnFiE)

Next thing needed is the build server itself.  Grab [TeamCity](http://www.jetbrains.com/teamcity/index.html) from the [JetBrains](http://www.jetbrains.com/) Site.

[![](/images/adronhall.smugmug.com/photos/308267847_hH9Ra-S.png)](http://adronhall.smugmug.com/gallery/5097270_6ynmt/4/308267847_hH9Ra)

As usual I go with the default c:\TeamCity for installation.  I suppose if one wanted to follow closer to Microsoft standard installations they could go with c:\Program Files\TeamCity.

[![](/images/adronhall.smugmug.com/photos/308267850_qs5XZ-S.png)](http://adronhall.smugmug.com/gallery/5097270_6ynmt/4/308267850_qs5XZ)

Leave everything here as is, unless you have something special in mind for you installations.

[![](/images/adronhall.smugmug.com/photos/308267856_4sMYw-S.png)](http://adronhall.smugmug.com/gallery/5097270_6ynmt/4/308267856_4sMYw)

This is just fine too, no reason to change it.

[![](/images/adronhall.smugmug.com/photos/308267861_Z8pfq-S.png)](http://adronhall.smugmug.com/gallery/5097270_6ynmt/4/308267861_Z8pfq)

For you security grognards, go ahead and stick it on whatever port.  Hopefully though, security protects the build server externally of the server.  There is no real reason to have a build server like this wide open for small group development.  So better just to keep this server behind a firewall and just keep it setup with defaults.

[![](/images/adronhall.smugmug.com/photos/308267866_hESei-S.png)](http://adronhall.smugmug.com/gallery/5097270_6ynmt/4/308267866_hESei)

This screen I’m not 100% sure what the reason for it displaying at this point is.  These things are good defaults, so leave em’, hit save, and keep moving along.

[![](/images/adronhall.smugmug.com/photos/308267871_3XURD-S.png)](http://adronhall.smugmug.com/gallery/5097270_6ynmt/4/308267871_3XURD)

Starting the services will not require a reboot or anything like that.  Jetbrains did an A grade job of the installation process for this software.

[![](/images/adronhall.smugmug.com/photos/308267882_25Mtx-S.png)](http://adronhall.smugmug.com/gallery/5097270_6ynmt/4/308267882_25Mtx)

I always just leave the default check so that I can be sure the server and site are setup and running appropriately.

[![](/images/adronhall.smugmug.com/photos/308267889_QiigA-S.png)](http://adronhall.smugmug.com/gallery/5097270_6ynmt/4/308267889_QiigA)

After you agree to the license the initial, one time only, Administrator Account Creation screen appears.  So create your account and you’ll be sent straight to the functional administration site.

[![](/images/adronhall.smugmug.com/photos/308267893_QDkfD-S.png)](http://adronhall.smugmug.com/gallery/5097270_6ynmt/5/308267893_QDkfD)

Now it is time for the build process setup.  This is the good stuff.  If you’re working on this via the local server, after you click on Administration (red arrow below points to it), the path is usually [http://localhost/admin/admin.html](http://localhost/admin/admin.html "http://localhost/admin/admin.html") for local setups.  So it is handy to bookmark this URI.  The little red arrow below points to where the Create Project button/link/function is.  Click that and we’ll get rolling.

[![](/images/adronhall.smugmug.com/photos/308267896_Kpi8X-S.png)](http://adronhall.smugmug.com/gallery/5097270_6ynmt/5/308267896_Kpi8X)

I just
stuck this in here, because I don’t see things right in front of my face sometimes.  Once you have one project already, the Create Project button moves to center screen (at least in FireFox).  So don’t forget that and then not see it when you need it.

[![](/images/adronhall.smugmug.com/photos/307955348_woqG5-S.png)](http://adronhall.smugmug.com/gallery/5097270_6ynmt/3/307955348_woqG5)

Name the new project, no description necessary, but always good to have one anyway.

[![](/images/adronhall.smugmug.com/photos/307955353_eUJcY-S.png)](http://adronhall.smugmug.com/gallery/5097270_6ynmt/3/307955353_eUJcY)

If you don’t create a VCS root now, it will prompt during the build configuration setup.  Since I don’t want any extra steps, I always just setup the VCS root first.

[![](/images/adronhall.smugmug.com/photos/307955357_ZTH9t-S.png)](http://adronhall.smugmug.com/gallery/5097270_6ynmt/3/307955357_ZTH9t)

Enter the appropriate settings, check the screen shot below with the red tagged items for examples.

[![](/images/adronhall.smugmug.com/photos/307955363_mRrdU-L.png)](http://adronhall.smugmug.com/gallery/5097270_6ynmt/3/307955363_mRrdU)

Once the connection information is in place, hit the “Test Connection” button toward the bottom to verify.  A nifty little modal AJAX type dialog pops up to verify a good connection.

[![](/images/adronhall.smugmug.com/photos/307955374_yMSUb-S.png)](http://adronhall.smugmug.com/gallery/5097270_6ynmt/3/307955374_yMSUb)

Go back to the project screen and click on “Create build configuration”.  I found it somewhat confusing that the VCS root isn’t displayed below after creation, at least in the order I did the configuration.  Maybe this is actually a bug, but I think somehow I circumvented the process somehow.  Anyway…

[![](/images/adronhall.smugmug.com/photos/307955382_mKuDf-S.png)](http://adronhall.smugmug.com/gallery/5097270_6ynmt/3/307955382_mKuDf)

The rest is a pretty straight forward next, next, next type of browser/web based wizard.  First you’ll setup the general settings as below…

[![](/images/adronhall.smugmug.com/photos/307955390_TSioJ-S.png)](http://adronhall.smugmug.com/gallery/5097270_6ynmt/3/307955390_TSioJ)

…then link the build runner up to the version control system setup earlier…

[![](/images/adronhall.smugmug.com/photos/307955398_rGzYd-S.png)](http://adronhall.smugmug.com/gallery/5097270_6ynmt/3/307955398_rGzYd)

On the build configuration screen there is really isn’t much to fill out.  Select the sln2008 Build Runner option.  This will let you point this at a particular \*.sln file of a solution to get the entire solution to build.

![](/images/adronhall.smugmug.com/photos/307955342_WkgdV-S.png)

On the final screen hit done and you’re ready to go.  **Click on the upper right hand side on the run button.  Then click on the Projects tab at the upper left hand side.**  This doesn’t particularly seem intuitive at this point in the process, but it is how the app seems to work.  ( I highlighted this part as many seem to just scan over some key parts, namely this one )

![Smile [:)]](/emoticons/emotion-1.gif)  Cheers!

After my ramblings, if you want to read more there are dozens of other blog entries on the topic.  Each of these entries Some of these entries I’ve included, so read away…

- [Source Control and Continuous Integration on the Cheap](http://blog.wekeroad.com/2008/01/27/source-control-and-continuous-integration-on-the-cheap/) – Rob Conery- [Mass Code Auto – Team City](http://ultramagnus.org/post/2008/02/Mass-Code-Auto---Team-City.aspx)- [Setting Up a Continuous Integration Environment (Preface)](http://blog.briandicroce.com/2008/03/17/setting-up-a-continuous-integration-environment-preface/) – Brian on Software- [Setting up a basic continuous integration server with TeamCity](http://sebastienlachance.com/2008/02/06/setting-up-a-basic-continuous-integration-server-with-teamcity/) – Sebastian Lechance- [CruiseControl.NET is dead.  Long live Team City!](http://blog.eleutian.com/2007/12/22/CruiseControlNETIsDeadLongLiveTeamCity.aspx) – Eleutian Speak ENG- [VisualSVN + TeamCity + Nant + Sql Server = A  Great CI Solution](http://www.acceptedeclectic.com/2008/05/visualsvn-teamcity-nant-sql-server.html) – Pete Weissbrod- [Creating an XNA Build Agent for TeamCity](http://www.nuclex.org/articles/creating-an-xna-build-agent-for-teamcity) – Nuclex- [Set up a Build Computer using Visual SVN, Team City, MsTest, Nunit](http://weblogs.asp.net/lkempe/archive/2008/03/21/set-up-a-build-computer-using-visualsvn-team-city-mstest-nunit.aspx) – Laurent Kempe- [This is why you need TeamCity Build Server](http://www.codeodor.com/index.cfm/2008/3/12/This-is-why-you-need-TeamCity-build-server/2050) – Sammi Larbi

…and of course the actual product(s) and processes used.

- [Continuous Integration](http://en.wikipedia.org/wiki/Continuous_integration)- [Team City 3.1](http://www.jetbrains.com/teamcity/download/index.html) by [JetBrains](http://www.jetbrains.com/index.html) (the creators of [ReSharper](http://www.jetbrains.com/resharper/index.html))

[![kick it on DotNetKicks.com](http://www.dotnetkicks.com/Services/Images/KickItImageGenerator.ashx?url=http%3a%2f%2fadronbhall.com%2fblogs%2ftechnology__software_development%2fdefault.aspx&bgcolor=3333FF&cfgcolor=CC3300)](http://www.dotnetkicks.com/kick/?url=http%3a%2f%2fadronbhall.com%2fblogs%2ftechnology__software_development%2fdefault.aspx)

Technorati Tags: [ReSharper](http://technorati.com/tags/ReSharper),[TeamCity](http://technorati.com/tags/TeamCity),[Continuous Integration](http://technorati.com/tags/Continuous%20Integration),[CI](http://technorati.com/tags/CI),[Build](http://technorati.com/tags/Build),[Subversion](http://technorati.com/tags/Subversion),[VisualSVN](http://technorati.com/tags/VisualSVN),[Integration](http://technorati.com/tags/Integration),[Visual Studio](http://technorati.com/tags/Visual%20Studio)

del.icio.us Tags: [ReSharper](http://del.icio.us/popular/ReSharper),[TeamCity](http://del.icio.us/popular/TeamCity),[Continuous Integration](http://del.icio.us/popular/Continuous%20Integration),[CI](http://del.icio.us/popular/CI),[Build](http://del.icio.us/popular/Build),[Subversion](http://del.icio.us/popular/Subversion),[VisualSVN](http://del.icio.us/popular/VisualSVN),[Integration](http://del.icio.us/popular/Integration),[Visual Studio](http://del.icio.us/popul
ar/Visual%20Studio)
