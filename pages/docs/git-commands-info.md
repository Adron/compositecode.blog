---
layout: page
title: Git Commands & Info
date: 2012-12-06 15:04:44 -0800
last_modified_at: 2020-11-04 20:20:46 -0800
permalink: /docs/git-commands-info/
slug: git-commands-info
wp_id: 7139
original_url: https://compositecode.blog/docs/git-commands-info/
---

The latest of my forgetful commands. A few chmods for running npm and cutting back on arbitrary sudo needs.

```
sudo chown -R $USER /usr/local/bin
sudo chown -R $USER /usr/local/lib/node_modules
```

…and every once in a while the stupid npm directory will get hosed up, which can often be fixed with.

```
sudo chown -R $USER /Users/adron/.npm/*
```

One command I always forget is what the switches are for creating an ssh key.

```
ssh-keygen -t rsa -C "your_email@youremail.com"
```

There is also the case of making the directory with appropriate permissions to then create the ssh key.

```
mkdir ~/.ssh
chmod 700 ~/.ssh/
ssh-keygen -t rsa
```

More information, specific to [github](http://www.github.com/), can be found in [this documentation](https://help.github.com/articles/generating-ssh-keys).

Brian McClain ([@BrianMMcClain](http://twitter.com/BrianMMcClain)) added from the comments below:

> If there’s ever a file you need to remove from git history for whatever reason (accidentally included a password or API Key, removing large files, etc), the below will remove it from the history of every branch and every tag. For example, to remove a file named “config.yml”

```
git filter-branch -index-filter 'git rm –cached –ignore-unmatch config.yml' –prune-empty –tag-name-filter cat – –all
```

For more info on this command, check out the link to the [github doc](https://help.github.com/articles/remove-sensitive-data).

**Branch Management**

Delete Local Branch

```
git branch -d the_local_branch
```

Delete Remote Branch

```
git push origin --delete
```

or

```
git push origin :
```

To synchronize your branches once a delete has occurred you sometimes may need to issue the following fetch command.

```
git fetch -p
```

Getting a Remote Branch

```
git checkout -b new_local_branch origin/existing_remote_branch
```

…and last but not least, the forgotten remote branch delete command.

```
git push origin --delete serverfix
```

**Keygen on Windows for Powershell with OpenSSH.**

Ensure OpenSSH is installed. First open up DOS or the PowerShell terminal (NOT ISE) with “As an administrator”.

[![](/wp-content/uploads/2020/11/2020-11-04_20-12-43.png)](/wp-content/uploads/2020/11/2020-11-04_20-12-43.png)

*“Run as adminstrator”*

Now just issue the keygen command listed above in the other example!
