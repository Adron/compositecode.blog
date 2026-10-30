---
layout: page
title: Postgresql – Admin Commands Short List
date: 2015-06-03 11:07:19 -0700
last_modified_at: 2018-10-17 01:43:00 -0700
permalink: /docs/postgresql-admin-commands-short-list/
slug: postgresql-admin-commands-short-list
wp_id: 11136
original_url: https://compositecode.blog/docs/postgresql-admin-commands-short-list/
---

[Home](/) > [Docs](/docs/) >

## Determining if Postgres is Running

```bash
ps aux | grep postgres
```

The installation directory generally looks something like this.

```bash
/Library/PostgreSQL
```

However Postgres has and continues to have various disparate installation paths depending on the installation method. Maybe they’ve been synchronized, but I don’t hedge bets on it and just assume I’ll have to find it.

## Easy Installations

There is an actual [installer for Windows, OS-X, and other platforms](http://www.enterprisedb.com/products-services-training/pgdownload) available via EnterpriseDB. I’d however advise NOT to use this installer. The more generally accepted installation method is to use homebrew or other alternates on Linux. As for Windows, this is another situation I’d suggest just not running Windows as it would be easier and less frustrating.

With homebrew it’s easy to get a good installation following these steps. It is always good to kick off with a brew update and doctor to make sure things are ok on the system.

```bash
brew update
brew doctor
```

Then give it the ole’ brew install.

```bash
brew install postgresql
```

Now setup the initial database, which you’ll have to do.

```bash
initdb /usr/local/var/postgres -E utf8
```

Now let’s setup launch. Mind you, make sure to check what version of Postgres you’re install as the version below may be different than what I’ve used.

```bash
mkdir -p ~/Library/LaunchAgents
cp /usr/local/Cellar/postgresql/9.2.1/homebrew.mxcl.postgresql.plist ~/Library/LaunchAgents/
```

Now run Launch Control.

```bash
launchctl load -w ~/Library/LaunchAgents/homebrew.mxcl.postgresql.plist
```

…and that should get everything up and running.
