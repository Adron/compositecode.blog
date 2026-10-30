---
title: Starting an Ubuntu Dev Tools List
date: 2014-12-24 00:16:54 -0800
last_modified_at: 2016-01-18 10:56:35 -0800
permalink: /2014/12/24/starting-an-ubuntu-dev-tools-list/
slug: starting-an-ubuntu-dev-tools-list
wp_id: 10584
original_url: https://compositecode.blog/2014/12/24/starting-an-ubuntu-dev-tools-list/
categories:
- How-to
- Linux
tags:
- dev tools
- idea intellij
- intellij
- java
- linux
- oracle
- sublime
- tools list
- ubutnu
- webstorm
excerpt: I’ve recently setup a completely clean virtual machine for doing web, system, and related development on Ubuntu. Here’s the shortlist of what I’ve installed after a default installation. The ongoing list of tools and related items I have installed on my Linux dev box I’m keeping here, and it will be kept as a living doc, …
image: /wp-content/uploads/2014/12/logo-ubuntu_st_noc2ae-black-hex.png
---

I’ve recently setup a completely clean virtual machine for doing web, system, and related development on Ubuntu. Here’s the shortlist of what I’ve installed after a default installation. The ongoing list of tools and related items I have installed on my Linux dev box I’m keeping [here](http://compositecode.com/docs/ubuntu-dev-tools/), and it will be kept as a living doc, so I’ll change it as I add new tools, apps and related changes. *So lemme know what I ought to add to that list and I’ll add it to my [docs page here](http://compositecode.com/docs/ubuntu-dev-tools/).* Here’s what I have so far…

- [Java](#java) / [Oracle Java](#oraclejava)
- [WebStorm](#webstorm)
- [IntelliJ Community Edition](#intellij)
- [Sublime 3](#sublime)

**Other To-dos**

- Always run sudo apt-get update once the system is installed. It never hurts to have the latest updates.
- I always install [Chrome](https://www.google.com/chrome/) as my first app. Sometimes the Ubuntu Software Center flakes out on this, but just try again and it’ll work. I use the 64-bit Chrome btw, as I’ve noticed that the 32-bit often flakes out when attempting installation on my virtual machines. Your mileage may vary.

***What this enables…***

At this point I can launch into about any language; Java, JavaScript, and a few others with a minimal amount of headache. Since it’s a Linux instance it gives me a full range of Linuxy things at my disposal.

**Default Java Installation**

1. Run a ‘sudo apt-get update’.
2. To install the default Java JRE and the JDK run the following commands.

   ```bash
   sudo apt-get install default-jre
   sudo apt-get install default-jdk
   ```

**Oracle Java v8 Installation**

1. ```bash
   sudo add-apt-repository ppa:webupd8team/java
   sudo apt-get update
   sudo apt-get install oracle-java8-installer
   ```

**WebStorm Installation**

1. I download the application zip from JetBrains and then run

   ```bash
   tar xfz WebStorm-*.tar.gz
   ```
2. Next I always move the unzipped content to the directory in which I’d like to have the application stored. It’s good practice to not keep things in the download directory, just sayin’. Generally I put these in my usr/bin directory.

   ```bash
   mv /downloads/WebStorm-* your/desired/spot
   ```
3. Now at your terminal, navigate to the path where the application is stored and run the WebStorm.sh executable.

   ```bash
   ./bin/webstorm.sh
   ```
4. To add WebStorm to the Quicklaunch, just right click on the icon and select to Lock to Launcher.

**IDEA IntelliJ Installation**

1. Follow all the steps listed under WebStorm, it’s the exact same process.

**Sublime 3**

1. Go to download the latest [v3](http://www.sublimetext.com/3).
2. Run the package and it should launch the actual Ubuntu installer, setup Sublime for bash use and get it installed.

(NOTE UPDATED 1/18/2016 > The installer doesn’t seem to get it installed, so I went with this link <http://olivierlacan.com/posts/launch-sublime-text-3-from-the-command-line/> which has a good solution.)
