---
title: Fun Adobe Reader Installation Error
date: 2007-05-03 08:20:16 +0000
last_modified_at: 2007-05-03 08:20:16 +0000
permalink: /2007/05/03/fun-adobe-reader-installation-error/
slug: fun-adobe-reader-installation-error
wp_id: 487
original_url: https://compositecode.blog/2007/05/03/fun-adobe-reader-installation-error/
categories:
- Uncategorized Bits
tags: []
excerpt: “The Temp folder is on a drive that is full or is inaccessible. Free up space on the drive or verify that you have write permission on the Temp folder.” This is dumb… but, Adobe Acrobat is designed to install with UAC enabled and will fail if it is disabled. Run the download from Adobe.When …
---

“***The Temp folder is on a drive that is full or is inaccessible. Free up space on the drive or verify that you have write permission on the Temp folder.***”

This is dumb… but, Adobe Acrobat is designed to install with UAC enabled and will fail if it is disabled.

Run the download from Adobe.
When you get the message to run the second file, do nothing.
Go to c:\users\USERNAME\AppData\LocalLow\Netopsystems
Run the setup.exe as administrator.

If that still flakes out as it did for me, then copy the contents of that directory to somewhere that you have total access to, such as a new folder on the desktop.  Then just double click setup.  You won’t even need to run the file as administrator if you do it this way.
