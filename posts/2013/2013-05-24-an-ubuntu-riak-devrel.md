---
title: 'An Ubuntu Riak #devrel'
date: 2013-05-24 20:54:15 -0700
last_modified_at: 2013-05-24 20:54:15 -0700
permalink: /2013/05/24/an-ubuntu-riak-devrel/
slug: an-ubuntu-riak-devrel
wp_id: 8372
original_url: https://compositecode.blog/2013/05/24/an-ubuntu-riak-devrel/
categories:
- Databases
- Distributed Things
- How-to
- Riak
tags:
- developer environment
- devrel
- distributed
- distributed databases
- distributed systems
- install
- installation
- riak
excerpt: Setting up Riak to test out, prototype against, develop and use in a general way is extremely easy. Just setup a devrel on your local development machine. This is however limited to certain *nix based operating systems, so Windows as a dev platform is out – but not completely. Get a virtual machine running on …
---

Setting up Riak to test out, prototype against, develop and use in a general way is extremely easy. Just setup a devrel on your local development machine. This is however limited to certain \*nix based operating systems, so Windows as a dev platform is out – but not completely. Get a virtual machine running on Ubuntu, RHEL or some other Linux instance and you’re ready to go. What I’ve put together here is an example of getting a devrel up and running with an Ubuntu Virtual Machine.

Step 1: Get the basic reqs installed.

- Install Erlang R15B01.

  ```bash
  	sudo apt-get install build-essential libncurses5-dev openssl libssl-dev git
  	wget http://erlang.org/download/otp_src_R15B01.tar.gz
  	tar zxvf otp_src_R15B01.tar.gz
  	cd otp_src_R15B01
  	./configure && make && sudo make install
  ```
- Install Riak from source.

  ```bash
  curl -O http://downloads.basho.com.s3-website-us-east-1.amazonaws.com/riak/1.3/1.3.1/riak-1.3.1.tar.gz
  tar zxvf riak-1.3.1.tar.gz
  cd riak-1.3.1
  make rel
  ```
- Install 4 Riak nodes to #devrel.

  ```bash
  make all
  make devrel DEVNODES=4
  cd dev
  ```

Step 2: With each of the nodes, now join and build the Riak cluster.

- Start each node.

  ```bash
  dev1/bin/riak start
  dev2/bin/riak start
  dev3/bin/riak start
  dev4/bin/riak start
  ```
- Check to determine that the riak services are running.

  ```bash
  ps aux | grep beam
  ```
- Add each node to a single node.

  ```bash
  dev2/bin/riak-admin cluster join dev1@127.0.0.1
  dev3/bin/riak-admin cluster join dev1@127.0.0.1
  dev4/bin/riak-admin cluster join dev1@127.0.0.1
  ```
- Set and get the cluster plan.

  ```bash
  dev2/bin/riak-admin cluster plan
  ```

  NOTE: This plan can be run from any of the instances.
- Last, commit the cluster plan.

  ```bash
  dev2/bin/riak-admin cluster commit
  ```

  NOTE: The commit can also be run from any of the instances.
