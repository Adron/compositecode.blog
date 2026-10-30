---
title: Windows Phone 7 Pt I
date: 2010-07-30 12:45:00 -0700
last_modified_at: 2010-07-30 13:34:38 -0700
permalink: /2010/07/30/windows-phone-7-pt-i/
slug: windows-phone-7-pt-i
wp_id: 806
original_url: https://compositecode.blog/2010/07/30/windows-phone-7-pt-i/
categories:
- How-to
- Phone n' Mobile Dev
tags: []
excerpt: I’ve got some Windows Phone 7 work lined up so thought I’d run through the most recent setup for SDK, Toolkit, and other such items needed for development. I’m working based on the assumption that Visual Studio 2010 is already installed. I’m also assuming the following items are installed, if not, install these before moving to the next items. I’m not 100% sure they’re needed, but I installed them first to make sure and for previous Silverlight 4 Development. Microsoft Silverlight 4 Tool for Visual Studio Silverlight 4 Toolkit Silverlight 4 SDK Next make sure uninstall any existing Windows Phone 7 SDK or other software you might have already installed previously. It is usually best, even if MS suggest no need to uninstall existing software, to do it anyway. Next check out the major download for Windows Phone 7 development; Windows Phone Developer Tools Beta Application Bar Icons for Windows Phone 7 Series Windows Phone 7 Training Kit for Developers – Beta Refresh Install each of these in order. To verify that you have installed them successfully you can check the Programs and Features. To do a final verification I always like to start a project with each of the templates installed and do a build of each. That way, without doubt the appropriate assemblies and other items have been installed and registered in the GAC.
---

I’ve got some [Windows Phone 7](http://www.microsoft.com/windowsmobile/) work lined up so thought I’d run through the most recent setup for SDK, Toolkit, and other such items needed for development.

I’m working based on the assumption  that [Visual Studio 2010](http://www.microsoft.com/visualstudio/en-us/visual-studio-2010-launch?WT.mc_id=SEARCH&WT.srch=1) is already installed.  I’m also assuming the following items are installed, if not, install these before moving to the next items.  I’m not 100% sure they’re needed, but I installed them first to make sure and for previous [Silverlight](http://www.microsoft.com/silverlight) 4 Development.

- [Microsoft Silverlight 4 Tool for Visual Studio](http://www.microsoft.com/downloads/details.aspx?FamilyID=40ef0f31-cb95-426d-9ce0-00dcfabf3df5&displaylang=en)
- [Silverlight 4 Toolkit](http://silverlight.codeplex.com/)
- [Silverlight 4 SDK](http://www.microsoft.com/downloads/details.aspx?familyid=55B44DA3-E5DE-4D2A-8EAF-1155CA6B3207&displaylang=en)

Next make sure uninstall any existing Windows Phone 7 SDK or other software you might have already installed previously.  It is usually best, even if MS suggest no need to uninstall existing software, to do it anyway.

Next check out the major download for [Windows Phone 7](http://www.microsoft.com/windowsmobile/) development;

- [Windows Phone Developer Tools Beta](http://www.microsoft.com/downloads/details.aspx?FamilyID=c8496c2a-54d9-4b11-9491-a1bfaf32f2e3&displaylang=en)
- [Application Bar Icons for Windows Phone 7 Series](http://www.microsoft.com/downloads/details.aspx?familyid=369B20F7-9D30-4CFF-8A1B-F80901B2DA93&displaylang=en)
- [Windows Phone 7 Training Kit for Developers – Beta Refresh](http://www.microsoft.com/downloads/details.aspx?familyid=CA23285F-BAB8-47FA-B364-11553E076A9A&displaylang=en)

Install each of these in order.  To verify that you have installed them successfully you can check the Programs and Features.  To do a final verification I always like to start a project with each of the templates installed and do a build of each.  That way, without doubt the appropriate assemblies and other items have been installed and registered in the GAC.

[![Windows Phone 7 Project Templates](/images/adronhall.smugmug.com/Software/Software-Development/windowsphone7gettingstarted/Capture/952697499_HXRrG-S.png "Windows Phone 7 Project Templates")](http://adronhall.smugmug.com/Software/Software-Development/windowsphone7gettingstarted/)

*Windows Phone 7 Project Templates*

Open up Visual Studio 2010 and verify that these project templates are available (Click on the image for a full size screenshot).  Click on new project from the menus and look at the template on the left hand side.  Under the Silverlight for Windows Phone there should be three new templates:

- Windows Phone Application
- Windows Phone List Application
- Windows Phone Class Library

Under the XNA Game Studio 4.0 there should be the following project templates:

- Windows Phone Game (4.0)
- Windows Phone Game Library (4.0)
- Windows Game (4.0)
- Windows Game Library (4.0)
- Xbox 360 Game (4.0)
- Xbox 360 Game Library (4.0)
- Content Pipeline Extension Library (4.0)
- Empty Content Project (4.0)

[![Windows Phone 7 XNA](/images/adronhall.smugmug.com/Software/Software-Development/windowsphone7gettingstarted/Windows-Phone-XNA/952714306_8Lw8k-S.png "Windows Phone 7 XNA")](http://adronhall.smugmug.com/Software/Software-Development/windowsphone7gettingstarted/Windows-Phone-XNA/)

*Windows Phone 7 XNA*

Out of all of these XNA templates, the only truly phone related items are the first two.  But the others come along with the installation.

To get a feel for what is installed, select the Widnows Phone List Application.  This is a great starter just to get an idea of how the IDE works.

[![Windows Phone 7 List Application](/images/adronhall.smugmug.com/Software/Software-Development/windowsphone7gettingstarted/CutThisAppropriately/952697458_btvhh-S.png "Windows Phone 7 List Application")](http://adronhall.smugmug.com/Software/Software-Development/windowsphone7gettingstarted/CutThisAppropriately/)

*Windows Phone 7 List Application*

Once you’ve entered you project name and everything take a look at the solution explorer.  Inside the project you will see that there is a break out of the ViewModels, Images, and SampleData into folders.  Below that is the standard Silvelight File App.xaml.  By default this project template also lays out a MainPage.xaml and a DetailsPage.xaml.  To the far left hand side of the screen you can see the actual list application interface, and in the center the xaml code or C# is displayed.

Once you’ve checked that out give it a run, click on F5.  You’ll see the following application starting come up.

[![Windows Phone 7 Application Starting](/images/adronhall.smugmug.com/Software/Software-Development/windowsphone7gettingstarted/Loading/952697478_E5FvC-S.png "Windows Phone 7 Application Starting")](/images/adronhall.smugmug.com/Software/Software-Development/windowsphone7gettingstarted/Loading/952697478_E5FvC-S.png)

*Windows Phone 7 Application Starting*

[![Windows Phone 7 Application List Screen](/images/adronhall.smugmug.com/Software/Software-Development/windowsphone7gettingstarted/WindowsPhoneApp2/952697494_pSBDo-S.png "Windows Phone 7 Application List Screen")](http://adronhall.smugmug.com/Software/Software-Development/windowsphone7gettingstarted/WindowsPhoneApp2/)

*Application List Main Screen*

The first screen on the phone to popup should be the list application itself.  If you click on the windows button at the bottom of the phone screen emulator you’ll get back to the startup screen with the IE browser prominently displayed.  If you click on the arrow to the right of the screen you will see an application list.  There you can click on the application list to return to your list application.  Check out the screen shots below, as always, click on em’ to get the full size screenshot.

[![Windows Phone 7 List Application Screens](/images/adronhall.smugmug.com/Software/Software-Development/windowsphone7gettingstarted/Startup-Screen/952697484_45ZZK-M.png "Windows Phone 7 List Application Screens")](http://adronhall.smugmug.com/Software/Software-Development/windowsphone7gettingstarted/Startup-Screen/)

*Windows Phone 7 Main Screen*

[![Windows Phone 7 Application Screen](/images/adronhall.smugmug.com/Software/Software-Development/windowsphone7gettingstarted/WindowsPhoneApp/952697485_stgBC-Th.png "Windows Phone 7 Application Screen")](http://adronhall.smugmug.com/Software/Software-Development/windowsphone7gettingstarted/WindowsPhoneApp/)

*Windows Phone 7 Application Screen*

That’s it for this entry.  I’ll be adding some more Windows Phone 7 development how-to, random blurbs, and my 2 cents in the coming weeks.
