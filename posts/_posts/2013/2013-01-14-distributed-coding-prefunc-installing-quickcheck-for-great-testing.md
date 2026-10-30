---
title: 'Distributed Coding Prefunc: Installing QuickCheck for Great Testing'
date: 2013-01-14 10:54:03 -0800
last_modified_at: 2013-02-02 15:47:15 -0800
permalink: /2013/01/14/distributed-coding-prefunc-installing-quickcheck-for-great-testing/
slug: distributed-coding-prefunc-installing-quickcheck-for-great-testing
wp_id: 7381
original_url: https://compositecode.blog/2013/01/14/distributed-coding-prefunc-installing-quickcheck-for-great-testing/
categories:
- Distributed Things
- Erlang
- How-to
tags:
- bdd
- behavior driven development
- Distributed Coding Prefunc
- erlang
- generated tests
- generating tests
- quickcheck
- tdd
- test driven development
- testing
- unit testing
excerpt: 'A few weeks ago I kicked off this series of “Distributed Coding Prefunc: Up and Running with Erlang” and had wanted to keep up the momentum, but as life goes I had to tackle a few other things first. But now, it’s time to get back on track with some distributed computing. I intend to …'
---

[![Erlang Logo](/images/adronhall.smugmug.com/Software/Misc-Images/Just-Icons-and-Bits/i-rnNZZNH/0/O/Erlang_logo.png)](http://www.erlang.org/)A few weeks ago I kicked off this series of “[Distributed Coding Prefunc: Up and Running with Erlang](/2012/12/28/distributed-coding-prefunc-up-and-running-with-erlang/)” and had wanted to keep up the momentum, but as life goes I had to tackle a few other things first. But now, it’s time to get back on track with some distributed computing. I intend to write tests with my samples, as I often do, I decided to take a stab at .

Before going forward, note that there is [QuickCheck for Haskell](http://www.cse.chalmers.se/~rjmh/QuickCheck/) and there is a [QuickCheck for Erlang](http://www.quviq.com/). Since the point of this “Distributed Coding Prefunc” is to get started coding with Erlang from zero, I’ll be talking about the Erlang version here. This version is created by John Hughes and Koen Claessen, starting the Quviq Company in 2006.

To download QuickCheck choose the version you intend to use, I’ve chosen the commercial license version from the [download page](http://www.quviq.com/downloads.html).

At the command prompt, install QuickCheck by running Erlang and then run the install with these commands.

Launch Erlang:

```bash
$ erl
Erlang R15B01 (erts-5.9.1) [source] [smp:4:4] [async-threads:0] [hipe] [kernel-poll:false]

Eshell V5.9.1  (abort with ^G)
1>
```

Then execute the install:

```erlang
1> eqc_install:install().
```

If the execution of the install displays this error, you’ll need to use sudo.

```bash
Installing ["pulse-1.27.7","eqc-1.27.7","eqc_mcerlang-1.27.7"].
Failed to copy pulse-1.27.7--copy returned {error,eacces}??
** exception exit: {{error,eacces},"pulse-1.27.7"}
     in function  eqc_install:'-copy_quickcheck/3-lc$^0/1-0-'/3 (../src/eqc_install.erl, line 63)
     in call from eqc_install:install2/4 (../src/eqc_install.erl, line 44)
```

Kill Erlang with a ctrl+c and restart Erlang with the sudo command.

```bash
$ sudo erl
```

Now when you install you should see the following result or something similar. You’ll be asked to continue, select lowercase ‘y’ to continue. It may be different for some, but when I hit uppercase ‘Y’ (I suppose I got overzealous to install QuickCheck) it finished as if I’d hit no or something else.

```bash
1> eqc_install:install().
Installation program for "Quviq QuickCheck" version 1.27.7.
Installing in directory /usr/local/lib/erlang/lib.
This will delete conflicting versions of QuickCheck, namely
    []
Proceed? y
Installing ["pulse-1.27.7","eqc-1.27.7","eqc_mcerlang-1.27.7"].
Quviq QuickCheck is installed successfully.
Looking in "/Users/adronhall"...   .emacs not found
Could not find your .emacs file!
Try install("path-to-emacs-file") or install(new_emacs).
Bookmark the documentation at /usr/local/lib/erlang/lib/eqc-1.27.7/doc/index.html.
ok
```

You’ll note above, I don’t currently have emacs installed. The reason it looks for emacs is because QuickCheck has templates/ops mode for emacs. So if you use emacs you’re in luck. I on the other hand, don’t, so I’ll just be using this from wherever I’m using it.

In addition to the lack of emacs, another important thing to note from the message is the link to documentation. Once you get this link open it up and check out the docs. They’re broken out into easily readily topic spaces and are a good place to do initial reference checking while you’re writing up your specs.

If you have a license, it is important to note, that if you’ve used sudo with your installation you’ll need to kill your running Erlang session and start it anew without sudo. Otherwise you’ll run into issue down the road trying to use the libs (unless of course you want to go hack on your permissions manually). Once you’re ready to register the software it’s simply one command, where xxxxx is your license key.

```bash
eqc:registration("xxxxxxxxxxxx").
```

Alright, next time we’re on to next steps…
