---
title: The Non-Microsoft Realm, Collecting Rubies Part II
date: 2011-04-21 00:07:42 -0700
last_modified_at: 2011-04-21 00:11:03 -0700
permalink: /2011/04/21/the-non-microsoft-realm-collecting-rubies-part-ii/
slug: the-non-microsoft-realm-collecting-rubies-part-ii
wp_id: 2634
original_url: https://compositecode.blog/2011/04/21/the-non-microsoft-realm-collecting-rubies-part-ii/
categories:
- How-to
- Linux
- Ruby on Rails Bits
tags:
- gems
- gemset
- git
- gitflow
- ruby
- ruby on rails
- rvm
- sql lite 3
- sqlite
- sqlite3
excerpt: 'A few steps when setting up Gemsets with RVM. With a few other commands that can often be helpful. Just a quick Friday night entry… cheers! Functionality by line: Get a list of the current available gemsets. Creates a gemset called theNameOfTheSiteToCreate. Lists the name of the current gemset. Delete the gemset named theNameOfTheSiteToCreate. This lists the current Ruby Version selected.'
---

Just a quick Friday night entry with helpful tidbits… cheers!

[Part I of the Collecting Rubies Series](/2011/04/09/the-non-microsoft-realm-collecting-rubies-part-i/).

### RVM Gemsets

A few steps when setting up Gemsets with [RVM](https://rvm.beginrescueend.com/). With a few other commands that can often be helpful.

**Functionality by line:**

1. Get a list of the current available gemsets.
2. Creates a gemset called theNameOfTheSiteToCreate.
3. Lists the name of the current gemset.
4. Delete the gemset named theNameOfTheSiteToCreate.
5. This lists the current Ruby Version selected.

```bash
rvm gemset list
rvm gemset create theNameOfTheSiteToCreate
rvm gemset name
rvm gemset delete theNameOfTheSiteToCreate
rvm list
```

### Git-flow

Check out the [git-flow github](https://github.com/nvie/gitflow) account.

To install:

```bash
wget --no-check-certificate -q -O -- https://github.com/nvie/gitflow/raw/develop/contrib/gitflow-installer.sh | sudo sh
```

…then just type git flow and you’ll see this prompt, which provides some functionality that is usable right away…

```bash
usage: git flow

Available subcommands are:
   init      Initialize a new git repo with support for the branching model.
   feature   Manage your feature branches.
   release   Manage your release branches.
   hotfix    Manage your hotfix branches.
   support   Manage your support branches.
   version   Shows version information.
```

### SQL Lite 3

Check out the [sqlite3](http://www.sqlite.org/) site.

To install:

```bash
sudo apt-get install sqlite3 libsqlite3-dev
```
