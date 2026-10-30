---
title: Oh, exFAT Doesn’t Work on Linux
date: 2018-07-24 13:59:06 -0700
last_modified_at: 2018-07-24 13:59:07 -0700
permalink: /2018/07/24/oh-exfat-doesnt-work-on-linux/
slug: oh-exfat-doesnt-work-on-linux
wp_id: 14446
original_url: https://compositecode.blog/2018/07/24/oh-exfat-doesnt-work-on-linux/
categories:
- How-to
- Linux
tags:
- exfat
- How-to
- linux
- ubuntu
excerpt: 'But to the rescue comes the search engine. I found some material on the matter and, as I’ve learned frequently, don’t count out Linux when it comes to support of nearly everything on Earth. Sure enough, there’s support for exFAT (really, why wouldn’t there be?) Check out this repo: https://github.com/relan/exfat There’s of course the git clone …'
image: /wp-content/uploads/2018/07/ssd-inside.jpg
---

But to the rescue comes the search engine. I found some material on the matter and, as I’ve learned frequently, don’t count out Linux when it comes to support of nearly everything on Earth. Sure enough, there’s support for exFAT (really, why wouldn’t there be?)

Check out this repo: https://github.com/relan/exfat

There’s of course the *git clone* and *make* and *make install* path or there’s also the *apt install* path.

```
git clone https://github.com/relan/exfat.git
cd exfat
autoreconf --install
./configure
make
```

Then make install.

```
make install
```

Of course, as with things on Linux, no reboot needed just use it now to mount a drive.

```
mount.exfat-fuse /dev/spec /mnt/exfat
```

To note, if you’re using Ubuntu 18.04 the support will just be available now so re-click on the attached drive or memory device you’ve just attached and it will now appear. Pretty sweet. If you want to use apt just run this command.

```
apt install exfat-fuse
```

That’s it. Now you’ve
