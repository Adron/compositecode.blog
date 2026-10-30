---
layout: page
title: Ubuntu – Adding / Editing Users
date: 2014-12-28 00:12:03 -0800
last_modified_at: 2018-04-19 16:41:30 -0700
permalink: /docs/ubuntu-adding-editing-users/
slug: ubuntu-adding-editing-users
wp_id: 10653
original_url: https://compositecode.blog/docs/ubuntu-adding-editing-users/
---

```bash
sudo adduser newuser
```

You can create the sudo user by opening the sudoers file with this command:

```bash
sudo /usr/sbin/visudo
```

File looks like this

```bash
# User privilege specification
root    ALL=(ALL:ALL) ALL
newuser	ALL=(ALL:ALL) ALL
```

Delete a user

```bash
sudo userdel newuser
sudo rm -rf /home/newuser
```
