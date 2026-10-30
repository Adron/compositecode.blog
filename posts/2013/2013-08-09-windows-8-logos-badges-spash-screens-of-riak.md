---
title: Windows 8 Logos, Badges & Splash Screens of Riak
date: 2013-08-09 21:13:55 -0700
last_modified_at: 2013-09-06 11:13:13 -0700
permalink: /2013/08/09/windows-8-logos-badges-spash-screens-of-riak/
slug: windows-8-logos-badges-spash-screens-of-riak
wp_id: 8546
original_url: https://compositecode.blog/2013/08/09/windows-8-logos-badges-spash-screens-of-riak/
categories:
- .NET Bits
- How-to
- Junction Project
- Metro UI
- Riak
- Software Projects
tags:
- graphic design
- logo
- metro ui
- riak
- riak logo
- tablet
- tablet application
- user experience
- user interface
- windows 8
- windows 8 ui
excerpt: As I’ve started working on a Windows 8 project here at Basho, there are a few pieces of collateral that help out to bring some branding and appeal to the application appearance. The first two things to grab if you want build a good looking Riak + Windows 8 application are the assets for design. …
---

[![](https://photos.adron.me/Software/Software-Development/Estuary-Project/i-sBPcjJW/0/O/Dashboard%20Goodness.jpg)](http://adron.github.io/junction/)As I’ve started working on a Windows 8 project here at **[Basho](http://www.basho.com/)**, there are a few pieces of collateral that help out to bring some branding and appeal to the application appearance. The first two things to grab if you want build a good looking Riak + Windows 8 application are the assets for design.

- [Basho Design Assets](http://basho.com/design-assets-hub/) : This includes several transparent images for the Basho & Riak, Riak CS and Riak Enterprise logos. Toward the bottom of the page there are also a number of Bashomen that you can download.
- [Windows 8 Store Design Assets](http://msdn.microsoft.com/en-us/library/windows/apps/hh975421.aspx) : This page includes a lot of downloadable Photoshop & other design assets for putting together a Windows 8 user interface and experience.
- [Windows 8 Design Guidelines](http://msdn.microsoft.com/en-us/library/windows/apps/hh465424.aspx) : This page shows how the interactions on Windows 8 are supposed to be used, developed around and what their best use is.
- [Windows 8 UX Patterns](http://msdn.microsoft.com/en-us/library/windows/apps/hh770552.aspx) : A sampling of UX patterns for Windows 8.

**Design Assets**

To check out the design assets I’ve put together I’ve created a [github repository junction\_design\_assets](https://github.com/Adron/junction_design_assets). In this repository are all of the Adobe Photoshop \*.psd files for each logo, wide logo, small logo, store logo, badge logo and splash screen image for the upcoming application. I’ve also attached an [Apache 2.0 license](http://www.apache.org/licenses/LICENSE-2.0.html) to this for use by others. All of the images created had a transparent background, and are set to display against a black or other dark background.

Here’s a quick intro where all of these design assets go, via Visual Studio 2012. The first step was to create a good *splash screen*, as defined by the Windows 8 guidelines for images at sizes of 1116x540px, 868x420px and 620x300px.

[![Setting up the Splash Screen (Click for full size image)](https://photos.adron.me/Software/Software-Development/Estuary-Project/i-z3XP7Wc/0/M/design-M.png)](https://photos.adron.me/Software/Software-Development/Estuary-Project/i-z3XP7Wc/0/O/design.png)

*Setting up the Splash Screen (Click for full size image)*

A: Open the Package.appmanifest file and the designed that is displayed above will show a screen used for editing the file.

B: In this case I changed the background color to black since I created all of the images to display on a dark background. One can’t get any darker than the darkest black, and this is that black!

C: When you click on the elipsis to upload each of the images it will upload the image to the Assets folder within the project. With that in mind DO NOT manually put the images into the project. Use this screen or you’ll end up with all sorts of headaches.

Also important is the default SplashScreen.png that is put into the *Spash screen:* text box. Don’t fill this in first, instead click each ellipsis under each splash screen image size and select each image for each size. The odd thing is (*one of those completely non-intuitive things*) is that the *Assets\SplashScreen.png* file doesn’t actually exist in the Assets directory, but is instead created somehow through pixie dust magic and added to the project. This will be the same for other sections of the Package.appmanifest file settings and logo images that are to be added. So remember to NOT change this but to instead upload all of the other images required first.

The second step then was to get a good *logo* as defined by the guidelines at 270x270px, 210x210px, 150x150px and 120x120px. For this I went with the Riak Graphic Logo with images as shown at the different sizes.

[![Adding the Logo (Click for full size image)](https://photos.adron.me/Software/Software-Development/Estuary-Project/i-HMk9svh/0/M/design%2001-M.png)](https://photos.adron.me/Software/Software-Development/Estuary-Project/i-HMk9svh/0/O/design%2001.png)

*Adding the Logo (Click for full size image)*

Next up is the *Wide Logo*…

[![Wide Logo (Click for full size image)](https://photos.adron.me/Software/Software-Development/Estuary-Project/i-XkFNJGT/0/M/design%2004-M.png)](https://photos.adron.me/Software/Software-Development/Estuary-Project/i-XkFNJGT/0/O/design%2004.png)

*Wide Logo (Click for full size image)*

The *Small Logo*…

[![Small Logo (Click for full size image)](https://photos.adron.me/Software/Software-Development/Estuary-Project/i-3VKh33B/0/M/design%2003-M.png)](https://photos.adron.me/Software/Software-Development/Estuary-Project/i-3VKh33B/0/O/design%2003.png)

*Small Logo (Click for full size image)*

…and the *Store Logo*.

[![Store Logo (Click for full size image)](https://photos.adron.me/Software/Software-Development/Estuary-Project/i-bW69k52/0/M/design%2002-M.png)](https://photos.adron.me/Software/Software-Development/Estuary-Project/i-bW69k52/0/O/design%2002.png)

*Store Logo (Click for full size image)*

This is the first step, which is where I’m at so far with this application. The application is also available with an [Apache 2.0 license](http://www.apache.org/licenses/LICENSE-2.0.html) with the [code on github](https://github.com/Adron/junction). If you’d like to jump into the code and help me build this application please feel free to reach out to me twitter [@adron](https://twitter.com/adron) or hit me on [Github @adron](https://github.com/Adron).

[![](/images/adronhall.smugmug.com/Software/Misc-Images/Logo/i-5zk96td/0/O/AH---Logo-32x32.png)](http://adron.me)
