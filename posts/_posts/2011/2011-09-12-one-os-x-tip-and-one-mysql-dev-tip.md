---
title: One OS-X Tip and One MySQL Dev Tip
date: 2011-09-12 21:44:52 -0700
last_modified_at: 2011-09-12 21:44:52 -0700
permalink: /2011/09/12/one-os-x-tip-and-one-mysql-dev-tip/
slug: one-os-x-tip-and-one-mysql-dev-tip
wp_id: 3777
original_url: https://compositecode.blog/2011/09/12/one-os-x-tip-and-one-mysql-dev-tip/
categories:
- A Bite o' Apple
- How-to
tags:
- alias
- apple
- applescript
- bash
- file visibility
- mysql
excerpt: 'I’ve downloaded and installed MySQL recently. I was doing a few things to make it easier to work with and thought, “I ought to document this, it isn’t real intuitive without pages of documentation being read.” So here’s some tips. 1. Make sure you can view all of your files in OS-X, especially if you intend to do development. What I’ve found to be the easiest way to do this, is to setup a script application on the desktop. Open up the AppleScript Editor, quickest way is to press the ⌘ + Space Bar and type in applescript and hit enter. In the editor enter the following code: set dotVisible to do shell script “defaults read com.apple.Finder AppleShowAllFiles” if dotVisible = “0” then do shell script “defaults write com.apple.Finder AppleShowAllFiles 1” else do shell script “defaults write com.apple.Finder AppleShowAllFiles 0” end if tell application “Finder” to quit delay 1 tell application “Finder” to activate Then save the file with the following options in the save as dialog selected. AppleScript Editor Save As Dialog w/ Appropriate Settings The only thing you really need to set is the File Format to “Application” and be sure nothing is checked. Now whenever you double click the file on the desktop, the finder will automatically be restarted with all the files visible, and double clicking again will hide all of the files from view. 2. Setup MySQL and when done, make sure to add the appropriate aliases to the .bash_rc file for the bash shell. These include setting these two aliases: alias mysql=/usr/local/mysql/bin/mysql alias mysqladmin=/usr/local/mysql/bin/mysqladmin That’s it for now, more tidbits to come and a write up of my extended weekend PDX hacking sessions with Geoloqi.'
---

I’ve downloaded and installed MySQL recently. I was doing a few things to make it easier to work with and thought, “I ought to document this, it isn’t real intuitive without pages of documentation being read.” So here’s some tips.

1. Make sure you can view all of your files in OS-X, especially if you intend to do development. What I’ve found to be the easiest way to do this, is to setup a script application on the desktop. Open up the AppleScript Editor, quickest way is to press the ⌘ + Space Bar and type in applescript and hit enter. In the editor enter the following code:

```bash
set dotVisible to do shell script "defaults read com.apple.Finder AppleShowAllFiles"
if dotVisible = "0" then
	do shell script "defaults write com.apple.Finder AppleShowAllFiles 1"
else
	do shell script "defaults write com.apple.Finder AppleShowAllFiles 0"
end if
tell application "Finder" to quit
delay 1
tell application "Finder" to activate
```

Then save the file with the following options in the save as dialog selected.

[![AppleScript Editor Save As Dialog w/ Appropriate Settings](/images/adronhall.smugmug.com/Software/Misc-Images/Bad-Resume/i-BXMKH85/0/S/Screen-shot-2011-09-12-at-S.png "AppleScript Editor Save As Dialog w/ Appropriate Settings")](http://adronhall.smugmug.com/Software/Misc-Images/Bad-Resume/18598094_fwJncc#1476747878_BXMKH85-O-LB)

*AppleScript Editor Save As Dialog w/ Appropriate Settings*

The only thing you really need to set is the File Format to “Application” and be sure nothing is checked. Now whenever you double click the file on the desktop, the finder will automatically be restarted with all the files visible, and double clicking again will hide all of the files from view.

2. Setup MySQL and when done, make sure to add the appropriate aliases to the .bash\_rc file for the bash shell. These include setting these two aliases:

```bash
alias mysql=/usr/local/mysql/bin/mysql
alias mysqladmin=/usr/local/mysql/bin/mysqladmin
```

That’s it for now, more tidbits to come and a write up of my extended weekend PDX hacking sessions with Geoloqi.
