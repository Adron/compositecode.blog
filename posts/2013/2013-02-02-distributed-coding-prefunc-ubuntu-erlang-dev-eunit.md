---
title: 'Distributed Coding Prefunc: Ubuntu Erlang Dev & EUnit'
date: 2013-02-02 15:50:03 -0800
last_modified_at: 2013-02-02 15:50:03 -0800
permalink: /2013/02/02/distributed-coding-prefunc-ubuntu-erlang-dev-eunit/
slug: distributed-coding-prefunc-ubuntu-erlang-dev-eunit
wp_id: 7430
original_url: https://compositecode.blog/2013/02/02/distributed-coding-prefunc-ubuntu-erlang-dev-eunit/
categories:
- Distributed Things
- Erlang
- How-to
- Linux
tags:
- bdd
- Distributed Coding Prefunc
- erlang
- eunit
- linux
- quickcheck
- tdd
- ubuntu
- unit testing
- unit tests
excerpt: After installing Erlang on OS-X and then getting QuickCheck installing via Erlang, I wanted to expand the OS options I’m using to Ubuntu (i.e. Linux). So in this entry I’m going to cover the Erlang install, a quick eunit bit, and then a QuickCheck install and sample. The first step in geting Erlang installed is …
---

[![Erlang Logo](/images/adronhall.smugmug.com/Software/Misc-Images/Just-Icons-and-Bits/i-rnNZZNH/0/O/Erlang_logo.png)](http://www.erlang.org/)After installing [Erlang on OS-X](/2012/12/28/distributed-coding-prefunc-up-and-running-with-erlang/) and then getting [QuickCheck installing via Erlang](/2013/01/14/distributed-coding-prefunc-installing-quickcheck-for-great-testing/), I wanted to expand the OS options I’m using to Ubuntu (i.e. Linux). So in this entry I’m going to cover the Erlang install, a quick eunit bit, and then a QuickCheck install and sample. The first step in geting Erlang installed is deciding how you want to install it. So far, it isn’t like Rails where it is pretty important which method you pick to how well it will work for you on Ubuntu. For Erlang all methods get you started with a good version that is working. The method I used was simply to install with apt-get.

```bash
sudo apt-get install erlang erlang-doc
```

After installing, always a good idea to run things and make sure they’re all content and happy with your machine. Startup the erlang shell.

```bash
erl
```

Then run some of the commands. Some I’ve found that will present you with useful and interesting information ist he erlang:system\_info function with appropriate parameter passed. The otp\_release parameter will get the version of erlang, the cpu\_topology shows you the processor outlay for you machine (or in this case my virtual machine, with a single processor core allocated to it), and allocated\_areas shows a bit about system memory allocations.

```erlang
Eshell V5.9.1  (abort with ^G)
1> erlang:system_info(otp_release).
"R15B01"
2> erlang:system_info(cpu_topology).
[{processor,{logical,0}}]
3> erlang:system_info(allocated_areas).
[{sys_misc,80748},
 {static,1007616},
 {atom_space,98328,73387},
 {atom_table,95961},
 {module_table,9084},
 {export_table,50316},
 {export_list,240960},
 {register_table,180},
 {fun_table,3266},
 {module_refs,2048},
 {loaded_code,3437028},
 {dist_table,403},
 {node_table,227},
 {bits_bufs_size,0},
 {bif_timer,80200},
 {link_lh,0},
 {process_table,262144},
 {ets_misc,52504}]
[{processor,{logical,0}}]
```

Now that erlang is effectively installed we can write a little sample code. To do this I created a directory called “TestingErlang” and in it placed an Erlang code file called “eunit\_tests.erl”. Note: I’m using Sublime 2 on Ubuntu, so exchange that for whatever text editor you’re using for your Erlang coding.

```bash
adron@ubuntu:~/Codez$ mkdir TestingErlang
adron@ubuntu:~/Codez$ cd TestingErlang
adron@ubuntu:~/Codez/TestingErlang$ sublime eunit_tests.erl
```

Add the header file include.

```erlang
-define(NOTEST, true).
-include_lib("eunit/include/eunit.hrl").
```

Adding the header file include will cause all the function with \_test() or \_test\_() to automatically be exported. An exported function of test() is created that can be used for running all of the unit tests. This also will include the preprocessor macros of EUnit for writing tests. So now throw a super simple test into the file.

You may want to, amid the automatic export of the methods ending in \_test() or \_test\_() not name them this, and you’ll then need to add a line at the top of your code file like this.

```erlang
-export([reverse_test/0]).
```

After this, add the function test as shown below.

```erlang
reverse_test() -> lists:reverse([1,2,3]).
```

The complete code file should look like this.

```erlang
-module(eunit_test).
-define(NOTEST, true).
-include_lib("eunit/include/eunit.hrl").
-export([reverse_test/0]).

reverse_test() -> lists:reverse([1,2,3]).
```

Build it and call the function.

```bash
Eshell V5.9.1  (abort with ^G)
1> c(eunit_test).
{ok,eunit_test}
2> eunit_test:reverse_test().
[3,2,1]
3>
```

BOOM! Passing. So now we know we have a good Erlang install and eunit is setup and usable. In the following blog entries I have in the works, we’ll dive deeper into what and how Erlang works from an extremely basic level all the way to diving into some of the more complex features.
