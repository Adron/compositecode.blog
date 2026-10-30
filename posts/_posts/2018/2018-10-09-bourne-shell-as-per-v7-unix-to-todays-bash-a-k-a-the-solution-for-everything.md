---
title: ‘bash’ A.K.A. The Solution for Everything – Bourne Shell as per v7 Unix to Today’s
date: 2018-10-09 08:00:53 -0700
last_modified_at: 2018-10-09 17:22:12 -0700
permalink: /2018/10/09/bourne-shell-as-per-v7-unix-to-todays-bash-a-k-a-the-solution-for-everything/
slug: bourne-shell-as-per-v7-unix-to-todays-bash-a-k-a-the-solution-for-everything
wp_id: 14638
original_url: https://compositecode.blog/2018/10/09/bourne-shell-as-per-v7-unix-to-todays-bash-a-k-a-the-solution-for-everything/
categories:
- bash
- Linux
- Unknown Code Ramblings
tags:
- born again shell
- bourne again shell
- bourne shell
- console
- linux
- posix
- shell
- terminal
- unix
excerpt: In 1979 Unix v7 started being distributed with the original Bourne Shell. Simply, it’s a program that sits at /bin/sh and runs in the terminal. You may ask, what’s the difference between a shell and the terminal?
image: /wp-content/uploads/2018/10/good-bash-logo.png
format: aside
---

In 1979 Unix v7 started being distributed with the original Bourne Shell. Simply, it’s a program that sits at /bin/sh and runs in the terminal. You may ask, “what’s the difference between a shell and the terminal?” Let’s cover that right now, because it’s something that routinely isn’t common knowledge, but it really ought to be as it sets the basis for understanding a lot of what is going on in Unix based systems (*that includes almost every practical system on a PC, Server, in the cloud, on your phones, and more. Probably easiest to explain it simply as everything that isn’t the Microsoft Windows OS*)

## A Shell and the Terminal

***Terminal*** – A terminal is the text input and output environment on the system.

***Shell*** – This is the command line interpreter that is run at the terminal.

Another point of context, is that a terminal, shell, and the word console are all used in various ways and sometimes interchangeably. However, these words do not mean the same thing at all. They are distinct individual parts of the system. For example, console, which is used in a strangely disingenuous way all over Microsoft phrasing, is the physical terminal of the system, which is where the system terminal, i.e. the thing I’ve described above, actually runs in so that we can type and interface with it as humans.

Albeit, as English does, these definitions aren’t always taken as the exact, appropriate, and pedantically correct definitions today. For example, many at Microsoft argue that the console is just the terminal, that the terminal is the console. Sure, ok, that’s fine I can still follow along in the conversation, and this adds context, for when someone steps out of line and uses the more historically specific definition in context of a conversation.

Alright, that’s all groovy, so now we can get back to just talking about the shell, all the power it gives the Unix/Linux/POSIX System user, and touch on the terminal or console as we need to with full context of what these things actually are!

## [Gnu-bash-logo.svg](https://en.wikipedia.org/wiki/Bash_(Unix_shell))Introducing Bash!

Alright, with that little bit of context around Bourne Shell, let’s talk about what we’ve actually got today running as our shell in our terminal on our console on the computers we work with! The Bourne Shell, years later had a replacement written for it by Brian Fox. He released it in 1989 and over the years it became a kind of defacto replacement of Bourne Shell. The term ‘BASH’ stands for ***B**ourne **A**gain **SH**ell*.

[![440px-Bash_screenshot](/wp-content/uploads/2018/10/440px-bash_screenshot.png)](https://en.wikipedia.org/wiki/Bash_(Unix_shell))The Bash command syntax is a superset of the Bourne Shell syntax. It provides a wide range of commands that includes ideas drawn from the Korn shell (ksh) and the C shell (csh) such as command line editing, command history, the directory stack, the $RANDOM and $PPID variables, and POSIX command substitution syntax. If many of those things make you think, “*WTF are these variables and such?*” have no worries, I’ll get to em’ soon enough in this series!

But with that, this is the beginning of many short entries on tips, tricks, tutorials, syntax, history, and context of bash so until next time, cheers!

## References & Collected Materials

- [What is the difference between the shell and terminal?](https://askubuntu.com/questions/506510/what-is-the-difference-between-terminal-console-shell-and-command-line)
- [Bourne Shell Wikipedia Page](https://en.wikipedia.org/wiki/Bourne_shell)
- [Bash (Unix Shell)](https://en.wikipedia.org/wiki/Bash_(Unix_shell))
