---
title: Fixing Windows 10 Drives for Linux Mounting
date: 2019-02-05 22:40:25 -0800
last_modified_at: 2019-03-04 10:54:34 -0800
permalink: /2019/02/05/fixing-windows-10-drives-for-linux-mounting/
slug: fixing-windows-10-drives-for-linux-mounting
wp_id: 15317
original_url: https://compositecode.blog/2019/02/05/fixing-windows-10-drives-for-linux-mounting/
categories:
- Linux
tags:
- drive
- exfat
- linux
- mount
excerpt: I mentioned, since I’d run into this problem, a while back in my post “Oh, exFAT Doesn’t Work on Linux” which then includes a fix. Here’s a slightly more updated fix for the same and another fix for mounting just the Windows 10 partition if you have a Windows 10 System Drive (i.e. the drive …
---

I mentioned, since I’d run into this problem, a while back in my post “[Oh, exFAT Doesn’t Work on Linux](/2018/07/24/oh-exfat-doesnt-work-on-linux/)” which then includes a fix. Here’s a slightly more updated fix for the same and another fix for mounting just the Windows 10 partition if you have a Windows 10 System Drive (i.e. the drive with the OS on it). First, the exFAT install can simply be done with the following, no need to go get it with git via a clone.

```bash
sudo apt-get install exfat-fuse exfat-utils
```

The other trick is to get a Windows 10 System Drive mounted. To do that, open up the disks application and click the gears on the drive. Then make the following settings by clicking off for “User Session Defaults”. Then you can set “Mount at system startup” and add “remove\_hiberfile” to the end of the command parameters as shown. Now the drive can be mounted, just click the mount button and you should be set.

![drive-setup-for-mount-windows-10-drive.png](/wp-content/uploads/2019/02/drive-setup-for-mount-windows-10-drive.png)
