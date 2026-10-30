---
title: _____100 |> F# Some Troubleshooting Linux
date: 2015-06-28 15:59:56 -0700
last_modified_at: 2015-06-28 15:59:56 -0700
permalink: /2015/06/28/_____100-f-some-troubleshooting-linux/
slug: _____100-f-some-troubleshooting-linux
wp_id: 11118
original_url: https://compositecode.blog/2015/06/28/_____100-f-some-troubleshooting-linux/
categories:
- .NET Bits
- F#
tags:
- documentation
- f#
- fsharp
- Generator
- linux
- os-x
- project scaffold
- ProjectScaffold
excerpt: 'In the last article I wrote on writing a code kata with F# on OS-X or Windows, I had wanted to use Linux but things just weren’t cooperating with me. Well, since that article I have resolved some of the issues I ran into, and this is the log of those issues. Issue 1: “How …'
image: /wp-content/uploads/2015/06/ah_f_256.png
---

In the last article I wrote on writing a code kata with F# on OS-X or Windows, I had wanted to use Linux but things just weren’t cooperating with me. Well, since that article I have resolved some of the issues I ran into, and this is the log of those issues.

## Issue 1: “How can I resolve the “Could not fix timestamps in …” “…Error: The requested feature is not implemented.””

The first issue I ran into with running the ProjectScaffold build on Linux I wrote up and posted to Stack Overflow titled “[How can I resolve the “Could not fix timestamps in …” “…Error: The requested feature is not implemented.”](http://stackoverflow.com/questions/30972220/how-can-i-resolve-the-could-not-fix-timestamps-in-error-the-requested)“. You can read more about the errors I receiving on the StackOverflow Article, but below is the immediate fix. This fix should probably be added to any F# Installation instructions for Linux as part of the default.

First ensure that you have the latest version of mono. If you use the instructions to do a make and make install off of the fsharp.org site you may not actually have the latest version of mono. Instead, here’s a good way to get the latest version of mono using apt-get. More information can be found about this on the [mono page here](http://www.mono-project.com/docs/getting-started/install/linux/#usage).

```bash
apt-get install mono-devel
apt-get install mono-complete
```

## Issue 2: “ProjectScaffold Error on Linux Generating Documentation”

The second issue I ran into I also posted to Stack Overflow titled “[ProjectScaffold Error on Linux Generating Documentation](http://stackoverflow.com/questions/30992501/projectscaffold-error-on-linux-generating-documentation)“. This one took a lot more effort. It also spilled over from Stack Overflow to become an actual [Github Issue (323) on the project](https://github.com/tpetricek/FSharp.Formatting/issues/323). So check out those issues in case you run into any issues there.

In the next issue, to be published tomorrow, I’ll have some script tricks to use mono more efficiently to run \*.exe commands and get things done with paket and fake in F# running on any operating system.
