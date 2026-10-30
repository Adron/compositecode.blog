---
title: Simplifying bash & repl Use With F#
date: 2015-05-15 22:27:49 -0700
last_modified_at: 2015-05-15 22:27:45 -0700
permalink: /2015/05/15/simplifying-bash-repl-use-with-f/
slug: simplifying-bash-repl-use-with-f
wp_id: 11026
original_url: https://compositecode.blog/2015/05/15/simplifying-bash-repl-use-with-f/
categories:
- Unknown Code Ramblings
tags: []
excerpt: That prompt… let’s get F# so that we can compile and run a file in about a zillionth of a second from the repl. First I setup a bash script that would be used to compile and then run the file. I created the file and simply named it “fs”. Inside the file I wrote …
---

That prompt… let’s get F# so that we can compile and run a file in about a zillionth of a second from the [repl](http://en.wikipedia.org/wiki/Read%E2%80%93eval%E2%80%93print_loop).

First I setup a bash script that would be used to compile and then run the file. I created the file and simply named it “fs”. Inside the file I wrote the following script.

```bash
echo "Compiling F#" + $1
fsharpc "$1.fs"
mono "$1.exe"
echo "Running Executable" + $1
```

I put that in my scripts folder that I have added to my path in my ~/.bash\_profile (or bashrc depending on what you’re rolling with).

```bash
export PATH="$PATH:~/Codez/scripts"
```

So now I have the ability to type in the following command and filename and the compile and the executable will be run. It makes for much easier repl usage.

```bash
fs theFileNameGoesHere
```

Got any tips or tricks to running F# somewhere besides Windows? Let me know and I’ll be sure to give you a shout out on Twitter and whenever I’m giving a presentation on hacking F# without Windows.
