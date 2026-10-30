---
title: Gotta Get Git
date: 2011-09-09 01:53:43 -0700
last_modified_at: 2011-09-18 07:13:16 -0700
permalink: /2011/09/09/gotta-get-git/
slug: gotta-get-git
wp_id: 3711
original_url: https://compositecode.blog/2011/09/09/gotta-get-git/
categories:
- How-to
tags:
- git
excerpt: Using .NET, PHP, or Ruby you probably should have your code somewhere nice and safe. These days there is no better place than Github. It is the place to start, maintain, and contribute to software projects or to even run your own private repositories or even setup some private repositories for a business. But enough about Github. In this blog entry I’m going to take a quick tour through getting Git and setting it up for basic use. For Windows go check out msysgit. For Ubuntu go check out git site. For OS-X go check out these downloads. This link also has information regarding how to setup and use the SSH keys. For Windows that will be extra work, since it doesn’t speak SSH very well. For Ubuntu, the instructions are pretty much exactly the same. I also had a few tidbits about git in the past here and here. Simple apt-get installation instructions. Once you have Git installed, there are a few things one should do right away. A few things, once Git is installed that should be done include setting up your user name and e-mail address for commits. To do this follow these commands. …read more…
---

Using .NET, PHP, or Ruby you probably should have your code somewhere nice and safe. These days there is no better place than [Github](http://www.github.com). It is the place to start, maintain, and contribute to software projects or to even run your own private repositories or even setup some private repositories for a business. But enough about [Github](http://www.github.com). In this blog entry I’m going to take a quick tour through getting Git and setting it up for basic use.

For Windows go check out [msysgit](http://code.google.com/p/msysgit/).

For Ubuntu go check out [git site](https://help.ubuntu.com/community/Git).

For OS-X go check out these [downloads](http://help.github.com/mac-set-up-git/).  This link also has information regarding how to setup and use the SSH keys. For Windows that will be extra work, since it doesn’t speak SSH very well. For Ubuntu, the instructions are pretty much exactly the same.

I also had a few tidbits about git in the past [here](/2011/04/09/the-non-microsoft-realm-collecting-rubies-part-i/) and [here](/2011/04/21/the-non-microsoft-realm-collecting-rubies-part-ii/). Simple apt-get installation instructions.

Once you have Git installed, there are a few things one should do right away.

A few things, once Git is installed that should be done include setting up your user name and e-mail address for commits. To do this follow these commands.

```bash
git config --global user.name "Your Name"
git config --global user.e-mail "blaghDblagh@yourdomain.com"
```

You can also setup some aliases to commands that you’ll use a lot. I usually setup the following.

```bash
git config --global alias.co checkout
git config --global alias.c commit
git config --global alias.p push
git config --global alias.u pull
git config --global alias.a add
git config --global alias.s status
```

Now that Git is setup and when a web project is ready we can commit and push. Navigate to the root of the folder structure where the project is and issue the initialization and following commands for Git.

```bash
git init
git add .gitignore
git commit -m 'Adding the ignore file first.'
git add -A
git commit -m 'Adding all subsequent files and the Ruby on Rails Project itself. In other words, first commit.'
git remote add origin git@github.com:Adron/somewhereOrAnother.git
git push origin master
```

Note also this .gitignore file included in the overall project. This file is really important to pay attention to before any commits are made to the repository. If it doesn’t exist, and doesn’t have all of the files, directories, and other things that should be ignored, ignoring them after the fact is rather difficult. So make sure it is included and always has everything you want ignored. With Rails Projects this is placed by default, some Visual Studio tools will also add this, and other tools will too. However, it is safe to assume that it is not there and check.

The standard .gitignore included with Rails Projects looks like this.

```bash
.bundle
db/*.sqlite3
log/*.log
tmp/**/*
```

For Rubymine and other exclusions I always add the following, and often times even more. It is easier to take something out and add it later, than it is to remove something after added.

```bash
#OS junk files
[Tt]humbs.db
*.DS_Store

#Webstorm & Rubymine files
*.idea
.idea
.idea/

#Rails Heroku and other bits to ignore
*.sqlite3
db/*.sqlite3
public/system/*
.bundle
log/*.log
tmp/**/*
tmp/*
doc/api
doc/app
*.swp
*~
.DS_Store
```

Well, that’s all I got for now. 🙂 Cheers!
