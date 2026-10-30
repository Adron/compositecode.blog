---
title: My Bespoke JetBrains Toolbox Configuration
date: 2021-10-29 13:49:09 -0700
last_modified_at: 2021-11-26 11:19:06 -0800
permalink: /2021/10/29/jetbrains-toolbox-configuration/
slug: jetbrains-toolbox-configuration
wp_id: 64407
original_url: https://compositecode.blog/2021/10/29/jetbrains-toolbox-configuration/
categories:
- Unknown Code Ramblings
tags:
- coding productivity
- intellij
- jetbrains
- jetbrains toolbox
excerpt: One thing I do just enough to remember I need to do, but not frequently enough to remember which settings are which, is installing the JetBrains Toolbox app to get the other JetBrains’ software installed. The following is the quick list of the key things that I setup to get the most out of Toolbox. …
image: /wp-content/uploads/2021/10/CleanShot-2021-10-29-at-13.29.29.png
---

One thing I do just enough to remember I need to do, but not frequently enough to remember which settings are which, is installing the JetBrains Toolbox app to get the other JetBrains’ software installed.

[![](/wp-content/uploads/2021/10/jetbrains_toolbox_00001.png)](/wp-content/uploads/2021/10/jetbrains_toolbox_00001.png)

The following is the quick list of the key things that I setup to get the most out of Toolbox. This is a quick process and I’ve detailed it here, one for memory, but also to detail what some of the features provide so this might be of more use to others.

The Toolbox *Settings* options are located by clicking on the gear icon when the application is opened up. This is the same across operating systems; Windows, Ubuntu, MacOS, or others. Find the gear, click it!

[![](/wp-content/uploads/2021/10/jetbrains_toolbox_00002.png)](/wp-content/uploads/2021/10/jetbrains_toolbox_00002.png)

Once *Settings* are opened up the core 4 configurations include:

[![](/wp-content/uploads/2021/10/jetbrains_toolbox_00003.png)](/wp-content/uploads/2021/10/jetbrains_toolbox_00003.png)

1. If you’ve got an account, login. Everything is easier if you’re logged into your account.
2. This second option around the theme is great on MacOS and Ubuntu. I’m not sure what it does on Windows exactly, but presume a similar effect. I myself set this to *Auto* since I always set the OS level theme to dark and love that almost all the apps that I use shift to that theme.

[![](/wp-content/uploads/2021/10/jetbrains_toolbox_00005.png)](/wp-content/uploads/2021/10/jetbrains_toolbox_00005.png)

4. I don’t set a shortcut for the toolbox, I simply use the Ctrl+Space to launch it from the spotlight on MacOS and use whatever option to issue apps from command on Windows and Linux OS installations of Toolbox.
5. This section, I’ll detail further down, has a host of additional settings around the tools use itself.

When logging into the app, the Toolbox will launch a browser to complete the process. The ! is what I do, log in with a regular JetBrains username and password based account versus using one of the Oauth options like Github. I feel like, however, maybe I should check if I can switch it or add the Github auth to use that, I am a fan of using it as my general dev auth across systems.

[![](/wp-content/uploads/2021/10/jetbrains_toolbox_00004.png)](/wp-content/uploads/2021/10/jetbrains_toolbox_00004.png)

Upon logging in and clicking *Approve* the prompt to open and then match the Toolbox extension for opening to the Toolbox application in the browser.

[![](/wp-content/uploads/2021/10/jetbrains_toolbox_00006.png)](/wp-content/uploads/2021/10/jetbrains_toolbox_00006.png)
[![](/wp-content/uploads/2021/10/jetbrains_toolbox_00007.png)](/wp-content/uploads/2021/10/jetbrains_toolbox_00007.png)
[![](/wp-content/uploads/2021/10/jetbrains_toolbox_00008.png)](/wp-content/uploads/2021/10/jetbrains_toolbox_00008.png)

Once all that is setup, my next move is to get the Tools section updated and setup the update behaviors, reload setting, and shell scripts.

[![](/wp-content/uploads/2021/10/jetbrains_toolbox_00009.png)](/wp-content/uploads/2021/10/jetbrains_toolbox_00009.png)

1. I toggle the *Update Toolbox App automatically* option on.
2. I also, cuz I’m such a nice person, send the anonymous usage statistics to JetBrains.
3. For the *Update all tools automatically* I often toggle this on. As in the vast majority of scenarios I’m working in, I need to ensure I have the latest patches and updates.
4. The *Keep only the latest version* is similar to #3 where as, I generally only want one version of the particular IDE, I don’t particularly need the EAP or previous versions, and I toggle this to keep only the latest version that is currently available.
5. I leave the *Reload Dock after update* option toggled on.
6. This last feature is one of the most important for me. I launch most of the IDEs, JetBrains or others, vai the terminal. My most used method is to issue the `ide .` so that the IDE opens the particular directory that the prompt is located in. This section, the *Generate shell scripts* enables this for all of the respective IDEs that are installed per the Toolbox App.

[![](/wp-content/uploads/2021/10/jetbrains_toolbox_00010.png)](/wp-content/uploads/2021/10/jetbrains_toolbox_00010.png)

1. This is diving into, once the *Generate shell scripts* is toggled on.
2. The *Shell scripts location*, I’d argue, should be set to your /usr/local or some system directory so that it’s available specifically for you, or if multiple users use the machine that use all the apps, it’s available prospectively for everybody. The fact is you can set it to whatever path you want, I’ve had some issues managing that autonomously of a directory like /usr/local that one just tends to end up with as part of one’s path on a machine. With that, I’d wrap this up with a strong suggestion to set it to /usr/local and call it a day.

An important thing to note about this path, whatever is selected has to be the path and the permissions must allow the creation of the actual files once apply is clicked. Whichever IDEs are installed should show like this. If permissions or or something else prevents these from being created then another directory needs to be selected or the permissions changed or problems resolved.

[![](/wp-content/uploads/2021/11/image.png)](/wp-content/uploads/2021/11/image.png)

At this point navigate to any directory and open the respective IDE by command or open the directory you’re located with `ideaCmd .` and the specific IDE will launch and open that particular directory.

That’s it for the Toolbox settings. I’ll end this article with a few suggestions on IDEs to install, pending you’re using an account that has the entire suite or you have multiple IDE subscriptions purchased. I would recommend, to install IntelliJ IDEA Ultimate regardless of what other IDEs you install. It’s a good option that has a little bit of every other IDE and has been the one (my understanding here) that was the original and thus, longest developed of all the options.

[![](/wp-content/uploads/2021/10/jetbrains_toolbox_00011.png)](/wp-content/uploads/2021/10/jetbrains_toolbox_00011.png)

Then, if you’re focused on a particular language stack, then install the IDE that is available for that particular language. GoLand for Go, PyCharm for Python, Rider for .NET, and WebStorm for web related development. There are others, so choose as you develop. Of course, any of these can all be developed in the IntelliJ IDEA IDE but your mileage may vary if you go that route, I’d highly recommend using the IDE specific to the language stack.

Cheers, enjoy your thrashing code! 🤘🏻
