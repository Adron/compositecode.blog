---
layout: page
title: Get ‘wget’ from ‘curl’
date: 2013-06-03 22:48:02 -0700
last_modified_at: 2015-09-02 19:16:37 -0700
permalink: /docs/get-wget-from-curl/
slug: get-wget-from-curl
wp_id: 8410
original_url: https://compositecode.blog/docs/get-wget-from-curl/
---

[Home](http://compositecode.com/) > [Docs](/docs/) >

First, use curl to download the latest wget source:

```bash
curl -O http://ftp.gnu.org/gnu/wget/wget-1.13.4.tar.gz%5B/sourcecode%5D

Next we use tar to uncompress the files you just downloaded:
[sourcecode language="bash"]tar -xzf wget-1.13.4.tar.gz
```

Use cd to change to the directory:

```bash
cd wget-1.13.4
```

Configure with the appropriate –with-ssl flag to prevent a “GNUTLS not available” error:

```bash
./configure --with-ssl=openssl
```

Build the source:

```bash
make
```

Install wget, it ends up in /usr/local/bin/:

```bash
sudo make install
```

Confirm everything worked by running wget:

```bash
wget --help
```

Clean up by removing wget source files when finished:

```bash
cd .. && rm -rf wget*
```
