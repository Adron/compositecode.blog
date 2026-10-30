---
title: My Day @ Seattle Mobile Hackathon (#mobileappSEA) The Morning
date: 2011-04-16 16:48:14 -0700
last_modified_at: 2011-04-20 20:44:53 -0700
permalink: /2011/04/16/my-day-seattle-mobile-hackathon-mobileappsea-the-morning/
slug: my-day-seattle-mobile-hackathon-mobileappsea-the-morning
wp_id: 2660
original_url: https://compositecode.blog/2011/04/16/my-day-seattle-mobile-hackathon-mobileappsea-the-morning/
categories:
- Conferences
- How-to
- Linux
- Phone n' Mobile Dev
- Ruby on Rails Bits
tags:
- '#mobileappSEA'
- appdev
- application development
- f5
- jetbrain
- mobile
- ruby
- ruby on rails
- rubymine
- software development
- webstorm
excerpt: Arrived around 8:20am “ish”. @juliaferraioli & cohort were registering people. The @AWSstartups crew was there including @Jeffbarr, also @shanley, @Alex_donn, @JamesPearce, and others were already getting things put together. I decided to happily plunk down in a chair and get going. I had zero plan, but only a single goal. Make a web app that isn’t device proprietary, but is mobile centric, and get it live on the web. My initial dev machine load that I intended to get this accomplished with I posted yesterday. So here’s my first push into Ruby on Rails and Mobile Dev with jQuery…
---

I arrived around 8:20am “ish”. [@juliaferraioli](http://twitter.com/juliaferraioli) & cohort were registering people. The [@AWSstartups](http://twitter.com/awsstartups) crew was there including [@Jeffbarr](http://twitter.com/jeffbarr), also [@shanley](http://twitter.com/shanley), [@Alex\_donn](http://twitter.com/alex_donn), [@JamesPearce](http://twitter.com/JamesPearce), and others were already getting things put together. I decided to happily plunk down in a chair and get going. I had zero plan, but only a single goal. Make a web app that isn’t device proprietary, but is mobile centric, and get it live on the web.

My initial dev machine load that I intended to get this accomplished with [I posted yesterday](/2011/04/15/seattle-mobile-hackathon-mobileappsea-f5-networks/).  So here’s my first push…

First a quick run thru of WebStorm and RubyMine IDEs.

{Edited this part on Apr 20th to provider more information regarding Java Installation} If you’re on Ubuntu, open up the Synaptic Package Manager and search for java6, which should bring up the *sun-java6-jre*.  Mark it for installation and apply so that the JDK will install with the required components.  If the Java 6 isn’t available in the Synaptic Package Manager open up the *Settings -> Repositories*, and then the *Software Sources Dialog* will appear.  Click on the *Other Software* tab and select *Canonical Partners*.  Close the dialog and *Reload* the packages.  When a search is done now, the *sun-java6-jdk* should be available.

Next edit the profile at /etc/profile by entering the command:

```bash
sudo gedit /etc/profile
```

Add the following to the bottom of the file:

```bash
export JAVA_HOME=/usr/lib/jvm/java-6-sun
export JDK_HOME=$JAVA_HOME
export RUBYMINE_JDK=$JAVA_HOME
```

![](/images/adronhall.smugmug.com/Software/Software-Development/Ubuntu-Tekpub-and-Ruby-on/i-xWXGTDC/0/O/webide.png)![](/images/adronhall.smugmug.com/Software/Software-Development/Ubuntu-Tekpub-and-Ruby-on/i-6HVbwKb/0/O/rubymine.png)After this is done, restart your X-Windows/Gnome Instance or simply just reboot. I don’t really like to suggest rebooting since it usually isn’t needed with Linux. 😉

Unzip both packages downloaded from [Jetbrains](http://www.jetbrains.com/).

```bash
tar -xvzf WebStorm-2.0.1.tar.gz
tar -xvzf RubyMine-3.1.1.tar.gz
```

You may want to put your new applications into a specific directory. I placed mine in a folder I made within my user folder called apps. Just a little easier to keep up with things that way.

![Creating a Launcher](/images/adronhall.smugmug.com/Software/Software-Development/Ubuntu-Tekpub-and-Ruby-on/i-Sjk6WPG/0/S/creatinglauncher-S.png "Creating a Launcher")

*Creating a Launcher*

Once these are unzipped right click on your desktop and choose “Create Launcher…”. Click on the Browser to bring up a folder navigation dialog, find the bin directory of the app your creating a launcher for. In my case it is /home/adron/apps/WebStorm-103.243/bin/ which has the WebStorm App Files needed for the Launcher. Find the WebStorm.sh file and select it.

Once the app file is selected then check ok. For a more step by step, check out [Tomi’s Blog Entry](http://tomionrails.blogspot.com/2010/05/install-rubymine-on-ubuntu-1004.html).  Do the same for both apps.

With both of those apps, simply launch the IDE and enter your key (or select 30 day trial) and you’re up and running.

[![RubyMine Startup (click for full size image)](/images/adronhall.smugmug.com/Software/Software-Development/Ubuntu-Tekpub-and-Ruby-on/i-LBQ6Gzj/0/S/screenshot-S.png "RubyMine Startup (click for full size image)")](http://adronhall.smugmug.com/Software/Software-Development/Ubuntu-Tekpub-and-Ruby-on/16541687_96rYA#1254069538_LBQ6Gzj-O-LB)

*RubyMine Startup (click for full size image)*

With the awesome [Jetbrains IDEs](http://www.jetbrains.com/) installed I was really ready to dive into something.  Next I went straight for a new project in RubyMine.  File -> New or just click on the Create New Project on the main RubyMine Startup Screen.

![New Project Dialog](/images/adronhall.smugmug.com/Software/Software-Development/Ubuntu-Tekpub-and-Ruby-on/i-PqbwcwV/0/O/somesushi.png "New Project Dialog")

*New Project Dialog*

Pick your name, I’ve decided to go for *some sushi* with a project type of Rails application, and click enter.  The next dialog that comes up asks some standard settings information options.

![Rails Settings](/images/adronhall.smugmug.com/Software/Software-Development/Ubuntu-Tekpub-and-Ruby-on/i-hm87n5z/0/O/rails-application.png "Rails Settings")

*Rails Settings*

If you click on the ellipsis button to the right of the Rails Version, a prompt will come up to select which rails version you want to use.  Ruby Mine will then install that version if it isn’t installed already.

![Install Rails Version](/images/adronhall.smugmug.com/Software/Software-Development/Ubuntu-Tekpub-and-Ruby-on/i-vc8Fhs3/0/O/installrails.png "Install Rails Version")

*Install Rails Version*

I decided to check “Generate RDoc and ri documentation” also, and then clicked on Install.

[![Installing Rails Version](/images/adronhall.smugmug.com/Software/Software-Development/Ubuntu-Tekpub-and-Ruby-on/i-F3qw9kN/0/S/rubymineworking-S.png "Installing Rails Version")](http://adronhall.smugmug.com/Software/Software-Development/Ubuntu-Tekpub-and-Ruby-on/16541687_96rYA#1254081652_F3qw9kN-O-LB)

*Installing Rails Version*

Once the options and settings are made for the new project, click to create the project.  RubyMine will work for a few seconds, maybe 20 or 30 on slower machines, and eventually the IDE will display with the newly created project.  When I created it the first time I was informed I was missing some gems.

[![RubyMine Project (Click for larger image)](/images/adronhall.smugmug.com/Software/Software-Development/Ubuntu-Tekpub-and-Ruby-on/i-4q22wrw/0/S/rubymine-S.png "RubyMine Project (Click for larger image)")](http://adronhall.smugmug.com/Software/Software-Development/Ubuntu-Tekpub-and-Ruby-on/16541687_96rYA#1254115121_4q22wrw-O-LB)

*RubyMine Project (Click for larger image)*

I clicked on the *More…* option near the *Install and attach missing gems using bundler…* warning to get the additional gems I needed.  This brings up a dialog specific to maintaining the Ruby SDK and Gems.

[![Settings (Click for larger image)](/images/adronhall.smugmug.com/Software/Software-Development/Ubuntu-Tekpub-and-Ruby-on/i-LD6Lq8h/0/S/settings-S.png "Settings (Click for larger image)")](http://adronhall.smugmug.com/Software/Software-Development/Ubuntu-Tekpub-and-Ruby-on/16541687_96rYA#1254115120_LD6Lq8h-O-LB)

*Settings (Click for larger image)*

I clicked on Install Gems and found the the sqllite3 and sqllite3-ruby gems to install.  I clicked on install and then apply and OK (ok, old habit, not sure WHY apply gets put on these dialogs) on the settings screen.  Once done getting those last bits installed click on the Development: SomeSushi (or whatever you’ve named the project) and select Edit Configurations.

[![Development: SomeSushi](/images/adronhall.smugmug.com/Software/Software-Development/Ubuntu-Tekpub-and-Ruby-on/i-KDCW5FP/0/S/development-somesushi-S.png "Development: SomeSushi")](http://adronhall.smugmug.com/Software/Software-Development/Ubuntu-Tekpub-and-Ruby-on/16541687_96rYA#1254115102_KDCW5FP-O-LB)

*Development: SomeSushi*

On the Edit Configurations Dialog screen check Run Browser from the bottom of the options and click on OK.  Then click on run button (the green play button on the button bar) to run the Ruby on Rails Web Application.  Within a second or two you’ll see the default Ruby on Rails + RubyMine Run the site in the browser.

[![RubyMine Ruby on Rails Default Web App](/images/adronhall.smugmug.com/Software/Software-Development/Ubuntu-Tekpub-and-Ruby-on/i-gZjBKdn/0/S/website-S.png "RubyMine Ruby on Rails Default Web App")](http://adronhall.smugmug.com/Software/Software-Development/Ubuntu-Tekpub-and-Ruby-on/16541687_96rYA#1254115108_gZjBKdn-O-LB)

*RubyMine Ruby on Rails Default Web App*

At this point in the day I took a break, ate lunch, talked to [@AWSstartups](http://twitter.com/awsstartups) crew [@rodica](http://twitter.com/rodica) & [@Jeffbarr](http://twitter.com/Jeffbarr).  Introduced myself formally in person to [@shanley](http://twitter.com/shanley) and chit chatted about our respective efforts with [@lazycoder](http://twitter.com/lazycoder) and [@juliaferraioli](http://twitter.com/juliaferraioli).  The food was great, as in, it was actually really good.  Not some random junk.  Super tender chicken with spaghetti sauce and little round funny shaped pastas (I’m sure there is an appropriate name for em’).  I was honestly impressed by the food brought in.

After lunch I dived back in for the next phase of development.  For that though, I have another blog entry coming…  (stay tuned).
