---
title: 'Distributed Coding Prefunc: Up and Running With Erlang'
date: 2012-12-28 11:16:13 -0800
last_modified_at: 2013-02-02 15:47:04 -0800
permalink: /2012/12/28/distributed-coding-prefunc-up-and-running-with-erlang/
slug: distributed-coding-prefunc-up-and-running-with-erlang
wp_id: 7267
original_url: https://compositecode.blog/2012/12/28/distributed-coding-prefunc-up-and-running-with-erlang/
categories:
- Distributed Things
- How-to
tags:
- distributed
- Distributed Coding Prefunc
- distributed computing
- erlang
excerpt: Before diving into architecture, coding, descriptions and other things related to distributed computing over the coming months. It helps to become familiar with a language like Erlang. I’m going to dive immediately into getting Erlang up and running before any theory, description or otherwise, so following the most direct installation… Installing Erlang This is easy …
---

[![Erlang Logo](/images/adronhall.smugmug.com/Software/Misc-Images/Just-Icons-and-Bits/i-rnNZZNH/0/O/Erlang_logo.png)](http://www.erlang.org/)Before diving into architecture, coding, descriptions and other things related to distributed computing over the coming months. It helps to become familiar with a language like Erlang. I’m going to dive immediately into getting Erlang up and running before any theory, description or otherwise, so following the most direct installation…

## Installing Erlang

This is easy on OS-X. Pending of course you have the XCode and Developer Tools installed.

```bash
curl -O http://erlang.org/download/otp_src_R15B01.tar.gz
tar zxvf otp_src_R15B01.tar.gz
cd otp_src_R15B01
```

Then compile the latest XCode and tools you can use the LLVM Compiler.

```bash
CFLAGS=-O0 ./configure --disable-hipe --enable-smp-support --enable-threads \
--enable-kernel-poll --enable-darwin-64bit
```

```bash
make
sudo make install
```

For more information on building Erlang you can also check out the [Erlang Organization Site](http://www.erlang.org/). It’s that simple, so now that it is up and running you should be able to check that all is right with the install by pulling a version.

```bash
erl -version
```

In my follow up blog entry I’m going to take you through the Rebar Riak Core Templates. This will get you up and running with an Erlang Application. This application can then be used either as a stand alone Erlang App for whatever you want to build with it or as a great starting point to build against Riak.
