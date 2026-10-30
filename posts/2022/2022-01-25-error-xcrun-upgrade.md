---
title: Error “xcrun” @ Upgrade
date: 2022-01-25 09:55:26 -0800
last_modified_at: 2022-03-29 17:06:01 -0700
permalink: /2022/01/25/error-xcrun-upgrade/
slug: error-xcrun-upgrade
wp_id: 64819
original_url: https://compositecode.blog/2022/01/25/error-xcrun-upgrade/
categories:
- Unknown Code Ramblings
tags: []
excerpt: 'Got hit with this error recently during an upgrade. $ git xcrun: error: invalid active developer path (/Library/Developer/CommandLineTools), missing xcrun at: /Library/Developer/CommandLineTools/usr/bin/xcrun The quick fix is to issue the command xcode-select install then follow the steps prompted to get the latest tools installed.'
image: /wp-content/uploads/2022/01/the-error.png
---

Got hit with this error recently during an upgrade.

```
$ git
xcrun: error: invalid active developer path (/Library/Developer/CommandLineTools), missing xcrun at: /Library/Developer/CommandLineTools/usr/bin/xcrun
```

[![](/wp-content/uploads/2022/01/CleanShot-2022-01-25-at-09.46.31@2x.png)](/wp-content/uploads/2022/01/CleanShot-2022-01-25-at-09.46.31@2x.png)

*Software List*

The quick fix is to issue the command `xcode-select install` then follow the steps prompted to get the latest tools installed.

Another possible solution is to issue a reset like `sudo xcode-select --reset` so that xcode will reset and clean up the installed version.

If there is any problem completing these steps you can also just navigate to the [Apple Developer site](https://developer.apple.com/download/), log in, and issue a search for the developer tools. Searching specifically for “command line tools for xcode” should get the results and bubble the most recent version to the top. Downloading the \*.dmg will give you a downloaded installer to get the latest installed. This is of course what the above command pretty much does but just follows a more specific path without as many steps.

These steps \*should\* get everything back up and running after an upgrade of MacOS or other significant upgrades that need the command line tools upgraded to the latest.
