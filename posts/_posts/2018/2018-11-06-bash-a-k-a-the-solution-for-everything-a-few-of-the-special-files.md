---
title: ‘bash’ A.K.A. The Solution for Everything – A few of the *Special Files*!
date: 2018-11-06 16:00:51 -0800
last_modified_at: 2018-11-06 16:15:25 -0800
permalink: /2018/11/06/bash-a-k-a-the-solution-for-everything-a-few-of-the-special-files/
slug: bash-a-k-a-the-solution-for-everything-a-few-of-the-special-files
wp_id: 14735
original_url: https://compositecode.blog/2018/11/06/bash-a-k-a-the-solution-for-everything-a-few-of-the-special-files/
categories:
- bash
tags:
- bash
- file
- files
- linux
- linux boot
- linux startup
- os starup
- special files
- unix
- unix boot
- unix startup
excerpt: In bash, the shell reads one or more startup files. Here’s the details about what’s what and which is run when. /etc/profile is executed automatically at login. The file from the list of ~/.bash_profile, ~/.bash_login, or ~/.profile are then executed at login. ~/.bashrc is executed by every non-login shell, but if sh is used to …
image: /wp-content/uploads/2018/10/good-bash-logo.png
format: aside
---

In bash, the shell reads one or more startup files. Here’s the details about what’s what and which is run when.

1. /etc/profile is executed automatically at login.
2. The file from the list of ~/.bash\_profile, ~/.bash\_login, or ~/.profile are then executed at login.
3. ~/.bashrc is executed by every non-login shell, but if sh is used to invoke bash it reads the $ENV for POSIX compatability.

For reference, the ~ symbol is used in place of the user directory. One way to check this out yourself is to change directory to ~ with a `cd ~` in the shell, then type `pwd` which will give the current directory. You’ll find that it is something like `/Users/adron` where instead of my name it’d be your user name.

When invoking the shell, you can also skip the ~/.bashrc or otherwise change the way bash starts up with the following options.

- `bash --init-file theFileToUseInstead` or `--rcfile` instead of ~/.bashrc.
- `bash --norc` which is similar to invoking with `sh`, which will use $ENV.
- `bash --noprofile` will prevent /etc/profile or any other personal startup files. This will provide a pretty baseline bash shell for use.

Until next time, happy bash code thrashing!
