---
title: Philadelphia Riak Training & Presentations
date: 2013-08-08 09:04:58 -0700
last_modified_at: 2013-08-08 12:45:29 -0700
permalink: /2013/08/08/philadelphia-riak-training-presentations/
slug: philadelphia-riak-training-presentations
wp_id: 8684
original_url: https://compositecode.blog/2013/08/08/philadelphia-riak-training-presentations/
categories:
- Databases
- How-to
- Riak
tags:
- basho
- basho_bench
- benchmark
- benchmarking
- config
- configuration
- riak
excerpt: 'This week I’ve traveled to Philadelphia to meet with a number of the Basho team to work together and receive training with the trainers or the best ways to approach content on Riak and more generally the best ways we can all brainstorm up to approach specific topics. Some of those topics include things like: …'
---

[![R Graphs](/images/adronhall.smugmug.com/Software/Misc-Images/Bad-Resume/i-TbGC2Tt/0/S/R-graphs-S.png)](http://www.r-project.org/)

*R Graphs*

This week I’ve traveled to Philadelphia to meet with a number of the Basho team to work together and receive training with the trainers or the best ways to approach content on Riak and more generally the best ways we can all brainstorm up to approach specific topics. Some of those topics include things like:

- Access Patterns around Log Storage & Analysis
- Bloom Filters
- CRDTs
- Consensus Protocols
- Erasure Coding
- LevelDB and Bitcask Backends
- MDC Repl

Out of the options we discussed in training today I ran with benchmarking. It is always near and dear to many of the customers’, clients’ and curious’ that I talk to. I dove in to see what exactly we offer with basho\_bench ([docs info](http://docs.basho.com/riak/latest/ops/building/benchmarking/), [github repo](https://github.com/basho/basho_bench)) in detail and functionality, but also dove into other benchmarks are out there that others may have run in the past.

## basho\_bench

What exactly is basho\_bench? The basho\_bench project is a [code repo](https://github.com/basho/basho_bench) on Github that offers a set of benchmarking tests that are run against a Riak cluster. There are a few prerequisites to the quick steps below, the prerequisites are:

1. Make sure you have a [cluster](http://docs.basho.com/riak/latest/ops/building/basic-cluster-setup/) or a [devrel](/2013/05/24/an-ubuntu-riak-devrel/) ([Basho docs on devrel](http://docs.basho.com/riak/latest/quickstart/)) setup that you can point basho\_bench at.
2. [Erlang R15B03 should be installed](/2013/06/27/erlang-r15b01-what-you-need-for-building-some-riak-and-shredding-code/) ([OS-X Compiler battles and fixes](http://compositecode.com/coding-community/documentation-for/os-x-docs/erlang-r15b01-on-os-x/)).
3. Make sure [R is installed](http://www.cran.r-project.org/doc/manuals/R-admin.html).

Now to get basho\_bench setup.

```bash
git clone git://github.com/basho/basho_bench.git
cd basho_bench
make all
```

Once that is done building, review the directory structure that is in the basho\_bench directory. The following should be available in the directory.

```bash
$ ls
FAQ		deps		rebar
LICENSE		ebin		rebar.config
Makefile	examples	src
README.org	include		tests
basho_bench	priv
```

The examples directory has several default config files available to run with basho\_bench for testing. If there is a devrel setup with the default 127.0.0.1 IP usage, just run the following command to begin generating stats. If the cluster being tested is not a devrel with 127.0.0.1 then give the [configuration section of the docs](http://docs.basho.com/riak/latest/ops/building/benchmarking/#Configuration) a read for information on how to point basho\_bench at an alternative cluster.

```bash
./basho_bench examples/http.config
```

You’ll see something akin to this spit out onto the screen.

```bash
$ ./basho_bench examples/http.config
10:34:41.736 [debug] Lager installed handler lager_console_backend into lager_event
10:34:41.752 [debug] Lager installed handler {lager_file_backend,"/Users/adronhall/Codez/basho_bench/tests/20130808_103441/error.log"} into lager_event
10:34:41.752 [debug] Lager installed handler {lager_file_backend,"/Users/adronhall/Codez/basho_bench/tests/20130808_103441/console.log"} into lager_event
10:34:41.757 [debug] Lager installed handler error_logger_lager_h into error_logger
10:34:41.758 [info] Application lager started on node nonode@nohost
10:34:41.767 [info] Est. data size: 488.28 KB
10:34:41.807 [debug] Supervisor sasl_safe_sup started alarm_handler:start_link() at pid
10:34:41.808 [debug] Supervisor sasl_safe_sup started overload:start_link() at pid
10:34:41.809 [debug] Supervisor sasl_sup started supervisor:start_link({local,sasl_safe_sup}, sasl, safe) at pid
10:34:41.810 [debug] Supervisor sasl_sup started release_handler:start_link() at pid
10:34:41.811 [info] Application sasl started on node nonode@nohost

....AND A WHOLE LOT MORE HERE....

10:35:42.954 [info]   {{{put_re,{"localhost",4567,"/","{\"this\":\"is_json_%%V\"}"},[{'Content-Type','application/json'}]},{put_re,{"localhost",4567,"/","{\"this\":\"is_json_%%V\"}"},[{'Content-Type','application/json'}]}},{put,{conn_failed,{error,econnrefused}}}}: 1701
10:35:42.955 [info] Application basho_bench exited with reason: stopped
10:35:42.955 [info] Test completed after 1 mins.
$
```

After letting the test run for it’s designated minute, run the following command to get some pretty graphs with R.

```bash
make results
```

…or maybe run…

```bash
priv/summary.r -i tests/current
```

The reason I post both is that ‘*make results*‘ doesn’t seem to always work to build the results and the manual execution will actually get the results built. With the results built, check the tests directory in the basho\_bench directory for the summary.png file. If you open the file it should look something like this.

[![Default empty http.config results from basho_bench. (Click for full size image)](https://photos.adron.me/Software/Misc-Images/Bad-Resume/i-3W8GNtn/0/M/summary-M.png)](https://photos.adron.me/Software/Misc-Images/Bad-Resume/i-3W8GNtn/0/O/summary.png)

*Default empty http.config results from basho\_bench. (Click for full size image)*

From here you can now run basho\_bench and get the results that are specific to basho\_bench. However, this now leads me to a higher abstract topic of why do benchmarking in the first place.

## Why Benchmark? How to Benchmark!

The definition for benchmark,

> ## bench·mark
>
> [bench-mahrk] 
> **noun**
> 1.a standard of excellence, achievement, etc., against which similar things must be measured or judged: The new hotel is a benchmark in opulence and comfort.
> 2.any standard or reference by which others can be measured or judged: The current price for crude oil may become the benchmark.
> 3.Computers. an established point of reference against which computers or programs can be measured in tests comparing their performance, reliability, etc.
> 4.Surveying. Usually, bench mark. a marked point of known or assumed elevation from which other elevations may be established. Abbreviation:  BM
> **adjective**
> 5.of, pertaining to, or resulting in a benchmark: benchmark test,benchmark study.

While basho\_bench provides an interesting baseline test that shows various pieces of data to work with, it shows nothing by default that is specific to *YOUR* use case. The basho\_bench is not ideal for your production environment, it is not your dev or user acceptance testing or test criteria, it is an example. To truly get effective numbers that really encompass your needs for your project you will need to provide custom configuration for basho\_bench or write your own specific benchmark.

The reason behind this is, with Riak as with other NoSQL solutions, is that you’re working toward a goal that is very data specific and unknown. It has specific domain logic and criteria that is specific to the use case, a custom benchmark can provide real data related to that domain logic and criteria.

In the end, even though basho\_bench is a great tool to get started, do basic tests, and a great project to get ideas from it is not the panacea benchmark. You’ll need to create the specific benchmark for your use case yourself.

Happy hacking (and benchmarking).

[![](/images/adronhall.smugmug.com/Software/Misc-Images/Logo/i-5zk96td/0/O/AH---Logo-32x32.png)](http://adron.me)
