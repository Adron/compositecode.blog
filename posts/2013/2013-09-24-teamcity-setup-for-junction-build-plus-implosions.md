---
title: TeamCity Setup for Junction Build, Plus Implosions
date: 2013-09-24 12:17:53 -0700
last_modified_at: 2013-09-24 12:17:53 -0700
permalink: /2013/09/24/teamcity-setup-for-junction-build-plus-implosions/
slug: teamcity-setup-for-junction-build-plus-implosions
wp_id: 8912
original_url: https://compositecode.blog/2013/09/24/teamcity-setup-for-junction-build-plus-implosions/
categories:
- .NET Bits
- How-to
- Junction Project
tags:
- cloud
- cloud computing
- continuous delivery
- continuous integration
- delivery lifecycle
- jetbrains
- lifecycle
- software
- software development
- software lifecycle
- team city
- teamcity
excerpt: I wanted to get a continuous delivery process setup for Junction that could help everybody involved get a clear and quick status of the project. The easiest way to do this for a Windows 8 .NET Project is to setup a Team City CI Server. This article covers what I went through to get the …
---

[![](https://photos.adron.me/Software/Software-Development/Estuary-Project/i-3Xxk8NH/0/O/Dashboard%20Goodness.jpg)](http://adron.github.io/junction/)I wanted to get a continuous delivery process setup for Junction that could help everybody involved get a clear and quick status of the project. The easiest way to do this for a Windows 8 .NET Project is to setup a [Team City CI Server](http://www.jetbrains.com/teamcity/).

This article covers what I went through to get the server up and running. In the ***next part I’ll cover troubleshooting*** that I went through to get a Visual Studio 2012 Window 8 C# Project building correctly on the server.

Finally, the ***last part is a small surprise***, but suffice it to say I’ll be getting a completely different language and tech stack up and running which you’ll likely not guess (or maybe you will).  😉

**Setting up Team City 8.0.3 (build 27540) using Tier 3 and a Windows 2008 Server, or not…**

Setting up a Windows 2008 Server with Tier 3 is super easy, as you’d expect with a cloud service provider. Log into your account, click on “Create Server” to bring up the create server dialog.

[![Create a New Server screen. Click for full size image.](https://photos.adron.me/Software/Software-Development/Estuary-Project/i-B3sDDgD/0/M/Tier%203%20CI%20Server-M.png)](https://photos.adron.me/Software/Software-Development/Estuary-Project/i-B3sDDgD/0/O/Tier%203%20CI%20Server.png)

*Create a New Server screen. Click for full size image.*

[![Click image for full size.](https://photos.adron.me/Software/Software-Development/Estuary-Project/i-zCFB5NJ/0/M/Tier%203%20CI%20Server%20001-M.png)](https://photos.adron.me/Software/Software-Development/Estuary-Project/i-zCFB5NJ/0/O/Tier%203%20CI%20Server%20001.png)

*Click image for full size.*

Next enter the information and select a *Standard* server.

[![Select how much horsepower you want the build server to have. Click for a full size image.](https://photos.adron.me/Software/Software-Development/Estuary-Project/i-cLcHgQW/0/M/Tier%203%20CI%20Server%20002-M.png)](https://photos.adron.me/Software/Software-Development/Estuary-Project/i-cLcHgQW/0/O/Tier%203%20CI%20Server%20002.png)

*Select how much horsepower you want the build server to have. Click for a full size image.*

Click next and then make the last few selections.

[![Server Tasks. No need to change the defaults here. Click for full size image.](https://photos.adron.me/Software/Software-Development/Estuary-Project/i-2N5B5zK/0/M/Tier%203%20CI%20Server%20003-M.png)](https://photos.adron.me/Software/Software-Development/Estuary-Project/i-2N5B5zK/0/O/Tier%203%20CI%20Server%20003.png)

*Server Tasks. No need to change the defaults here. Click for full size image.*

Click Create Server and then sit tight for a few while the server is created. Once the server is created navigate back to the server information screen (I’ll leave you to get back to this screen).

[![Server information screen. Click for full size image.](https://photos.adron.me/Software/Software-Development/Estuary-Project/i-9d3VvhB/0/M/Tier%203%20CI%20Server%20004-M.png)](https://photos.adron.me/Software/Software-Development/Estuary-Project/i-9d3VvhB/0/O/Tier%203%20CI%20Server%20004.png)

*Server information screen. Click for full size image.*

On this screen click on the add public ip button to bring up the IP & port selection screen.

[![Adding a public IP Address. Click for full size image.](https://photos.adron.me/Software/Software-Development/Estuary-Project/i-KjSMzRN/0/M/Tier%203%20CI%20Server%20005-M.png)](https://photos.adron.me/Software/Software-Development/Estuary-Project/i-KjSMzRN/0/O/Tier%203%20CI%20Server%20005.png)

*Adding a public IP Address. Click for full size image.*

On the public IP screen select the HTTP (80) and RDP (3389) ports to open up. Click the add ip address button and again sit tight for a few. Once the server has the IP set then we can log in using RDP ([Remote Desktop](http://www.microsoft.com/mac/remote-desktop-client) or on Mac try [CoRD](http://cord.sourceforge.net/)).

Next install the .NET 4.5 SDK. For the latest, it’s best to install the latest windows SDK that is available for Windows Server 2008 also.

## Team City install

In the instructions below, you’ll notice everything is now Windows Server 2012. That’s because after installing everything on a Windows 2008 Server I stumbled on a very important fact. I’m working to put a build together for a Windows 8 Store Application, which requires a Windows Server 2012 (or Windows 8) operating system to build on.

I got a sudden flashback to OS-X and iOS land there for a second, but leapt in and wiped out the image I’d just built. Since I’d built it in a cloud environment, it merely meant spending a few seconds to get a new OS instance built up. So after a few clicks, just like the instructions above for building a Windows 2008 Server I had a Windows 2012 Server instead. There are, however a few steps to follow once you have a good Windows Server 2012 install. Once you have a good Windows 2012 Server up and running it should have a public IP, some memory, compute and storage capabilities. In the image below I didn’t give it a huge amount of horsepower for a few reasons.

1. It’s just doing builds, not computing the singularity.
2. If it can build on this, I’m doing good keeping the project clean.
3. I want to keep the build fast, keeping it on a weak machine and still having it fast also reinforces that I have a clean project.
4. I don’t need a successful build every second, the server gets used only during pushes by devs. If we get up to dozens of devs hacking on this, I can easily spool up and get a faster, more hard core heavier horsepower option up and running.

[![Windows Server 2012 w/ Public IP, 1 Proc, 1 GB RAM and 40 GB Storage. Click for full size image.](https://photos.adron.me/Software/Software-Development/Estuary-Project/i-KCjCN72/0/M/TeamCity%20001-M.png)](https://photos.adron.me/Software/Software-Development/Estuary-Project/i-KCjCN72/0/O/TeamCity%20001.png)

*Windows Server 2012 w/ Public IP, 1 Proc, 1 GB RAM and 40 GB Storage. Click for full size image.*

When Windows Server 2012 boots up the first thing that will launch is the Server Manager. We don’t really need that yet, so just ignore it, close it or move it to the side.

[![Windows Server 2012 Server Manager. Click for full size image.](https://photos.adron.me/Software/Software-Development/Estuary-Project/i-8xwvM5W/0/M/TeamCity%20002-M.png)](https://photos.adron.me/Software/Software-Development/Estuary-Project/i-8xwvM5W/0/O/TeamCity%20002.png)

*Windows Server 2012 Server Manager. Click for full size image.*

The first thing we will need is Internet Explorer, so we can download [Chrome](https://www.google.com/intl/en/chrome/browser/) or [Firefox](http://www.mozilla.org/en-US/firefox/new/). Internet Explorer is wired up with high security so the first thing it will do is explode with messages about sites not being in the right zone. It is, hugely annoying. So add each site to the zone and head out to the web to pick up Chrome or Firefox.

[![Internet Explorer security configuration explosions. Click for full size.](https://photos.adron.me/Software/Software-Development/Estuary-Project/i-JL2H6HK/0/M/TeamCity%20003-M.png)](https://photos.adron.me/Software/Software-Development/Estuary-Project/i-JL2H6HK/0/O/TeamCity%20003.png)

*Internet Explorer security configuration explosions. Click for full size.*

In the following screenshots I didn’t actually download Chrome or Firefox first, but instead downloaded TeamCity. I advise getting Chrome or Firefox FIRST and then downloading TeamCity with one of those browsers. Life is dramatically simpler that way.

[![Team City - add another site to the site list for security clearance. Click for full size.](https://photos.adron.me/Software/Software-Development/Estuary-Project/i-J4trWf2/0/M/TeamCity%20008-M.png)](https://photos.adron.me/Software/Software-Development/Estuary-Project/i-J4trWf2/0/O/TeamCity%20008.png)

*Team City – add another site to the site list for security clearance. Click for full size.*

[![Team City downloading. Click for full size image.](https://photos.adron.me/Software/Software-Development/Estuary-Project/i-M7VC62t/0/M/TeamCity%20009-M.png)](https://photos.adron.me/Software/Software-Development/Estuary-Project/i-M7VC62t/0/O/TeamCity%20009.png)

*Team City downloading. Click for full size image.*

I know one can turn off the security settings in IE, but it’s just dramatically easier to go and use one of the other browsers. Just trust me on this one, if you want to turn off the security features in IE, be my guest, I’d however recommend just getting a different browser to work with.

Once you’ve got your browser of choice and Team City downloaded, run the installer executable.

[![Installer Downloaded w/ Security Scan in IE. Click for full size image.](https://photos.adron.me/Software/Software-Development/Estuary-Project/i-SrwXWsn/0/M/TeamCity%20010-M.png)](https://photos.adron.me/Software/Software-Development/Estuary-Project/i-SrwXWsn/0/O/TeamCity%20010.png)

*Installer Downloaded w/ Security Scan in IE. Click for full size image.*

![Executable downloaded.](https://photos.adron.me/Software/Software-Development/Estuary-Project/i-b6FNH3c/0/M/TeamCity%20011-M.png)

*Executable downloaded.*

![Installing Team City.](https://photos.adron.me/Software/Software-Development/Estuary-Project/i-nkZGpXN/0/O/TeamCity%20012.png)

*Installing Team City.*

Leave the components checked unless you have some specific goal for your server and build agents.

![Server & Build Agents Options.](https://photos.adron.me/Software/Software-Development/Estuary-Project/i-JX8479t/0/O/TeamCity%20013.png)

*Server & Build Agents Options.*

In one of the subsequent dialogs there is the option to run the server under the SYSTEM account or under a user account. Since this is a single purpose machine and I don’t really want to manage Windows users, I’m opting for the SYSTEM account.

![SYSTEM Account.](https://photos.adron.me/Software/Software-Development/Estuary-Project/i-PRzD2B2/0/O/TeamCity%20014.png)

*SYSTEM Account.*

After everything is installed navigate in a browser to <http://localhost>. This will automatically direct you to the TeamCity First Start page.

[![TeamCity First Start Page. Click for full size image.](https://photos.adron.me/Software/Software-Development/Estuary-Project/i-cqTXc3h/0/M/TeamCity%20015-M.png)](https://photos.adron.me/Software/Software-Development/Estuary-Project/i-cqTXc3h/0/O/TeamCity%20015.png)

*TeamCity First Start Page. Click for full size image.*

At this point you’ll be prompted to ok the EULA.

[![Signing one of those famous EULAs. Click for full size image.](https://photos.adron.me/Software/Software-Development/Estuary-Project/i-gBW4M7L/0/M/TeamCity%20016-M.png)](https://photos.adron.me/Software/Software-Development/Estuary-Project/i-gBW4M7L/0/O/TeamCity%20016.png)

*Signing one of those famous EULAs. Click for full size image.*

Then you’ll be prompted to create the first Administrator user.

![Creating the administrator user.](https://photos.adron.me/Software/Software-Development/Estuary-Project/i-TDhTwqV/0/O/TeamCity%20017.png)

*Creating the administrator user.*

From there you’ll be sent to the TeamCity interface, ready to create a new build project.

[![TeamCity Tools is marked by a giant pink arrow, Great ways to integrate TeamCity into your workflow. Click for full size clarity!](https://photos.adron.me/Software/Software-Development/Estuary-Project/i-6FN5329/0/M/TeamCity%20018-M.png)](https://photos.adron.me/Software/Software-Development/Estuary-Project/i-6FN5329/0/O/TeamCity%20018.png)

*TeamCity Tools is marked by a giant pink arrow, Great ways to integrate TeamCity into your workflow. Click for full size clarity!*

Click on Projects at the top left of the screen and you’ll navigate to the Create a Project dialog. Click on the Create a Project link to start the process.

[![Creating a project. Click for full size image.](https://photos.adron.me/Software/Software-Development/Estuary-Project/i-Hjn5cPb/0/M/TeamCity%20020-M.png)](https://photos.adron.me/Software/Software-Development/Estuary-Project/i-Hjn5cPb/0/O/TeamCity%20020.png)

*Creating a project. Click for full size image.*

Once you’ve entered the name, project ID and description click on Create. This will bring you to the next step, and to the general tab of the project. On this screen click on Create build configuration.

[![Project Setup. Click for full size image.](https://photos.adron.me/Software/Software-Development/Estuary-Project/i-m7TSLRG/0/M/TeamCity%20021-M.png)](https://photos.adron.me/Software/Software-Development/Estuary-Project/i-m7TSLRG/0/O/TeamCity%20021.png)

*Project Setup. Click for full size image.*

Now create a name, enter the config id, and click the VCS Settings >> button to move on to the next step of the process.

[![Build Configuration. Click for full size image.](https://photos.adron.me/Software/Software-Development/Estuary-Project/i-X8gHtkN/0/M/TeamCity%20022-M.png)](https://photos.adron.me/Software/Software-Development/Estuary-Project/i-X8gHtkN/0/O/TeamCity%20022.png)

*Build Configuration. Click for full size image.*

In VCS Settings leave everything as default and click on the Add Build Step >> button.

[![Click for full size image.](https://photos.adron.me/Software/Software-Development/Estuary-Project/i-KD4Q9HP/0/M/TeamCity%20023-M.png)](https://photos.adron.me/Software/Software-Development/Estuary-Project/i-KD4Q9HP/0/O/TeamCity%20023.png)

*Click for full size image.*

Now select the Visual Studio (sln) option from the Runner type and give the dialog a moment to render the options below that. They’ll appear and then enter the Step Name, Visual Studio type needs to be set to Microsoft Visual Studio 2012 and then click on Save.

[![Setting up the Build Type. Click for full size image.](https://photos.adron.me/Software/Software-Development/Estuary-Project/i-SwPsgQG/0/M/TeamCity%20024-M.png)](https://photos.adron.me/Software/Software-Development/Estuary-Project/i-SwPsgQG/0/O/TeamCity%20024.png)

*Setting up the Build Type. Click for full size image.*

From there you’ll be navigated back to the Project Build Steps screen. On that page you’ll see the build step listed. We’ll have one more we’ll need to add in a moment, but for now click on Version Control Settings again.

[![Build Step displaced, click on Version Control Settings Again. Click for full size image.](https://photos.adron.me/Software/Software-Development/Estuary-Project/i-2dcHb9x/0/M/TeamCity%20025-M.png)](https://photos.adron.me/Software/Software-Development/Estuary-Project/i-2dcHb9x/0/O/TeamCity%20025.png)

*Build Step displaced, click on Version Control Settings Again. Click for full size image.*

On this page click on the Create an attach a new VCS root.

[![Attach a new VCS root. Click for full size image.](https://photos.adron.me/Software/Software-Development/Estuary-Project/i-TK6pnNq/0/M/TeamCity%20026-M.png)](https://photos.adron.me/Software/Software-Development/Estuary-Project/i-TK6pnNq/0/O/TeamCity%20026.png)

*Attach a new VCS root. Click for full size image.*

Now select Git from the dialog and wait for the page to populate the form settings and options.

[![VCS Root Options. Click for full size image.](https://photos.adron.me/Software/Software-Development/Estuary-Project/i-6Q3P8PN/0/M/TeamCity%20027-M.png)](https://photos.adron.me/Software/Software-Development/Estuary-Project/i-6Q3P8PN/0/O/TeamCity%20027.png)

*VCS Root Options. Click for full size image.*

Now enter the correct Fetch URL to the Git repo (which on github looks something like <https://github.com/username/gitrepo.git> and is available to copy and paste from the right hand side of the repo page on github), enter the appropriate default branch to build and an appropriate VCS root name and VCS root ID. Once that is done click on the Test connection button.

[![Test Connection. Click for full size image.](https://photos.adron.me/Software/Software-Development/Estuary-Project/i-d2cVvCd/0/M/TeamCity%20028-M.png)](https://photos.adron.me/Software/Software-Development/Estuary-Project/i-d2cVvCd/0/O/TeamCity%20028.png)

*Test Connection. Click for full size image.*

Click save and now navigate back to the Build Triggers screen by click on the #5 option on the right hand side of the page. You’ll be navigated back to the magical Version Control Settings screen where you now have a few more options available and a VCS root available.

[![Version Control Settings. Click for full size.](https://photos.adron.me/Software/Software-Development/Estuary-Project/i-sWPxcDn/0/M/TeamCity%20029-M.png)](https://photos.adron.me/Software/Software-Development/Estuary-Project/i-sWPxcDn/0/O/TeamCity%20029.png)

*Version Control Settings. Click for full size.*

Now an Add New Build Trigger dialog appears to add the trigger. I set it to trigger a new build at each new check-in. The TeamCity server checks frequently to see if a commit has been made and will initiate a build. Another way however to setup this is to not add a trigger and instead go to Github (if you’re using Github) and setup a push trigger from Github itself. That way every commit will initiate a build instead of the TeamCity Server, which knows nothing about the actual status of the repo until it checks, giving a more timely build process to your commits & dev workflow.

[![Build Trigger. Click for full size image.](https://photos.adron.me/Software/Software-Development/Estuary-Project/i-RsH2Vhg/0/M/TeamCity%20030-M.png)](https://photos.adron.me/Software/Software-Development/Estuary-Project/i-RsH2Vhg/0/O/TeamCity%20030.png)

*Build Trigger. Click for full size image.*

[![The added build trigger. Click for full size image.](https://photos.adron.me/Software/Software-Development/Estuary-Project/i-jWJrMPw/0/M/TeamCity%20031-M.png)](https://photos.adron.me/Software/Software-Development/Estuary-Project/i-jWJrMPw/0/O/TeamCity%20031.png)

*The added build trigger. Click for full size image.*

Now, one more build step. Add the NuGet Installer (which is included with the TeamCity Build Server, check the docs for TeamCity 8.x for [NuGet Installer](http://confluence.jetbrains.com/display/TCD8/NuGet+Installer) and [NuGet](http://confluence.jetbrains.com/display/TCD8/NuGet) for more information). For our purposes once you’ve insured that the NuGet Installer you need is available add a new build step. Select from the Runner Type NuGet Installer and the respective form will populate below.

[![NuGet Installer. Click for full size image.](https://photos.adron.me/Software/Software-Development/Estuary-Project/i-WGbcwwN/0/M/TeamCityNugetInstaller%2001-M.png)](https://photos.adron.me/Software/Software-Development/Estuary-Project/i-WGbcwwN/0/O/TeamCityNugetInstaller%2001.png)

*NuGet Installer. Click for full size image.*

Once the step is added, click on Reorder Build Steps under the Build Steps list and a dialog, specifically for reordering the build steps will appear.

[![Reordered Build Steps.](https://photos.adron.me/Software/Software-Development/Estuary-Project/i-T96xPpF/0/M/TeamCityNugetInstaller%2003-M.png)](https://photos.adron.me/Software/Software-Development/Estuary-Project/i-T96xPpF/0/O/TeamCityNugetInstaller%2003.png)

*Reordered Build Steps. Click for full size image.*

Reorder the steps so that Getting NuGetty (the name I’ve give to it, click for a full size image) will be run first.

[![The NuGet Settings.  Under the NuGet.exe is where to add the Nuget executable if it isn't already installed and available. Click the NuGet settings for options. Click for full size image.](https://photos.adron.me/Software/Software-Development/Estuary-Project/i-CwdrwSp/0/M/TeamCityNugetInstaller%2002-M.png)](https://photos.adron.me/Software/Software-Development/Estuary-Project/i-CwdrwSp/0/O/TeamCityNugetInstaller%2002.png)

*The NuGet Settings. Under the NuGet.exe is where to add the Nuget executable if it isn’t already installed and available. Click the NuGet settings for options. Click for full size image.*

At this time you now have all of the steps you actually need. You’ll be able to go back to the main projects screen and built the project.

[![](https://photos.adron.me/Software/Software-Development/Estuary-Project/i-W3Q99Ws/0/M/TeamCity%20032-M.png)](https://photos.adron.me/Software/Software-Development/Estuary-Project/i-W3Q99Ws/0/O/TeamCity%20032.png)When you do this however, if you’ve actually set this up to build a Windows 8 Store Project you’ll get a build failure. Which is a total bummer, but that makes for a great follow up blog which I’ll have posted real soon! For now, these are great steps for getting a modern ASP.NET, Java, Maven and a whole host of other builds up and running. For the solution around the Windows 8 Store Project keep reading (subscribe on the top right hand side to the RSS!) and I’ll have that posted up real soon.

Until next entry, Cheers!  > Adron
