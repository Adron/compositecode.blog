---
layout: page
title: Erlang R15B01 on OS-X
date: 2013-06-03 23:06:30 -0700
last_modified_at: 2013-07-26 08:18:50 -0700
permalink: /os-x-docs/erlang-r15b01-on-os-x/
slug: erlang-r15b01-on-os-x
wp_id: 8414
original_url: https://compositecode.blog/os-x-docs/erlang-r15b01-on-os-x/
---

## Installing on Mac OS X

You can install Erlang in several ways on OS X: from source, with Homebrew, or with MacPorts.

### Source

To build from source, you must have Xcode tools installed from the CD that came with your Mac or from the Apple [Developer website](http://developer.apple.com/).

First, download and unpack the source:

```bash
curl -O http://erlang.org/download/otp_src_R15B01.tar.gz
tar zxvf otp_src_R15B01.tar.gz
cd otp_src_R15B01
```

Next, configure Erlang.

Mountain Lion (OS X 10.8) and Lion (OS X 10.7) If you’re on Mountain Lion (OS X 10.8) or Lion (OS X 10.7) you can use LLVM (the default) or GCC to compile Erlang.

Using LLVM:

```bash
CFLAGS=-O0 ./configure --disable-hipe --enable-smp-support --enable-threads \
--enable-kernel-poll --enable-darwin-64bit
```

If you prefer GCC:

```bash
CC=gcc-4.2 CPPFLAGS='-DNDEBUG' MAKEFLAGS='-j 3' \
./configure --disable-hipe --enable-smp-support --enable-threads \
--enable-kernel-poll --enable-darwin-64bit
```

Ubuntu Installation

```bash
sudo apt-get install build-essential libncurses5-dev openssl libssl-dev fop xsltproc unixodbc-dev
sudo apt-get install libwxbase2.8 libwxgtk2.8-dev libqt4-opengl-dev
```

Then…

```bash
wget http://erlang.org/download/otp_src_R15B01.tar.gz
tar zxvf otp_src_R15B01.tar.gz
cd otp_src_R15B01
./configure && make && sudo make install
```

…and a video…

<iframe allowfullscreen="" frameborder="0" height="413" loading="lazy" mozallowfullscreen="" src="https://player.vimeo.com/video/69221604" webkitallowfullscreen="" width="550"></iframe>
