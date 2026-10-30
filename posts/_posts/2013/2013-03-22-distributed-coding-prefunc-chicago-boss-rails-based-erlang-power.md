---
title: 'Distributed Coding Prefunc: Chicago Boss, Rails Based Erlang Power'
date: 2013-03-22 22:30:48 -0700
last_modified_at: 2013-03-22 22:30:48 -0700
permalink: /2013/03/22/distributed-coding-prefunc-chicago-boss-rails-based-erlang-power/
slug: distributed-coding-prefunc-chicago-boss-rails-based-erlang-power
wp_id: 7950
original_url: https://compositecode.blog/2013/03/22/distributed-coding-prefunc-chicago-boss-rails-based-erlang-power/
categories:
- Erlang
- How-to
tags: []
excerpt: Troy Howard and I sat down on a Friday night to do some straight up thrashing of Erlang and Chicago Boss. It seemed like a framework that has a lot of promise. Thus, we wanted to hack at it a bit and see what we could come up with. First things first, I running OS-X …
---

[![](/images/adronhall.smugmug.com/Software/Software-Development/Erlang-Chicago-Boss/i-V8z4hDD/0/O/ChicagoBoss.png)](http://www.chicagoboss.org/)Troy Howard and I sat down on a Friday night to do some straight up thrashing of Erlang and Chicago Boss. It seemed like a framework that has a lot of promise. Thus, we wanted to hack at it a bit and see what we could come up with.

First things first, I running OS-X and Troy hacking with the latest Ubuntu, we dove in. I first downloaded from the main [Chicago Boss Site](http://www.chicagoboss.org/), which I immediately decided not to use and went straight for a fork and cloning of the repo.

```bash
git clone git@github.com:Adron/ChicagoBoss.git
cd ChicagoBoss
make
make app PROJECT=bigonion
cd ../bigonion
./init-dev.sh
```

The ‘./init-dev.sh’ will launch the server to view whatever is available on the site. Now when I went to the localhost at port 8001, it shows some general mess which is kind of nondescript. But one can identify that the server is running if this works.

![Hitting http://localhost:8001](/images/adronhall.smugmug.com/Software/Software-Development/Erlang-Chicago-Boss/i-NsFQ4Hg/0/O/Screenshot_3_22_13_9_50_PM.png)

*Hitting <http://localhost:8001>*

![Boardwalk Explosion!](/images/adronhall.smugmug.com/Software/Software-Development/Erlang-Chicago-Boss/i-WgMRTn4/0/S/explosion_zps50e7f7d1-S.jpg)

*Boardwalk Explosion!*

**Oh dear, then the explosion…**

At this point Troy started running into a number of problems on Ubuntu. Ranch wasn’t building based on what was included. He went through fighting and attempting to manually install this dependency but no go. He had originally downloaded RB14 of Erlang which should have worked. However it did not. It caused all sorts of madness.

I spooled up my VM of Ubuntu and went through the same steps above, even did the quick intro to setup a hello world, and it worked. We then checked out Erlang versions and I was running with R15B01. Troy went with installing that version and lo’ n’ behold, magic of the druids! Mayor Daley kicked this thing and made it run. So if you are running anything besides R15B01 on Ubuntu, we can’t attest to this stuff working. Just sayin’.

**So Back to the Chicago Boss**

So go back to the bigonion project above that we created and throw in a controller file. Be sure to use the exact naming, because this is seriously like rails, follow the convention or you’ll spend the rest of your life in the jail of convention-less hell!

Add a file at /src/controller/bigonion\_greeting\_controller.erl and add the following code.

```erlang
-module(bigonion_greeting_controller, [Req]).
-compile(export_all).

hello('GET', []) ->
    {output, "<strong>Daley will tell you how to run the Big Onion!</strong>"}.
```

Now execute the code, or if you have the server running with ‘./init-dev.sh’ still then just navigate to ‘<http://localhost:8001/greeting/hello&#8217>; and you’ll get a hello world [reality check about Chicago history](http://en.wikipedia.org/wiki/Richard_J._Daley). 😉

On to next things, let’s get a conformance test in there. Add a file called ‘src/test/functional/bigonion\_test.erl’ with the following code snippet of a test in it.

```erlang
-module(bigonion_test).
-compile(export_all).

start() ->
    boss_web_test:get_request("/greeting/hello", [],
        [ fun boss_assert:http_ok/1,
            fun(Res) -> boss_assert:tag_with_text("strong",
                "Daley will tell you how to run the Big Onion!", Res) end ], []).
```

Now build the project to production.

```bash
./rebar compile
./rebar boss c=test_functional
```

…which left me with

```bash
$ ./rebar boss c=test_functional
==> bigonion (boss)
FATAL: Config file "boss.test.config" not found.
```

Joy, another completely random error. But hey, that’s software development right. So that’s coming later… for now, I’m out. Keep hacking the Erlang bits. If you know what happened with the last command to run the test above, please leave a comment and help out! 🙂
