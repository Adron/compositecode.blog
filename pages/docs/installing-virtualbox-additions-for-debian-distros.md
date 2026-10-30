---
layout: page
title: Installing VirtualBox Additions for Debian Distros
date: 2019-01-18 19:26:20 -0800
last_modified_at: 2019-01-18 19:26:20 -0800
permalink: /docs/installing-virtualbox-additions-for-debian-distros/
slug: installing-virtualbox-additions-for-debian-distros
wp_id: 15229
original_url: https://compositecode.blog/docs/installing-virtualbox-additions-for-debian-distros/
---

Get all the latest updates and upgrade.

```bash
sudo apt update
sudo apt upgrade
```

Install build essentials and dkms for the ability to build the essentials.

```bash
sudo apt install build-essential dkms linux-headers-$(uname -r)
```
