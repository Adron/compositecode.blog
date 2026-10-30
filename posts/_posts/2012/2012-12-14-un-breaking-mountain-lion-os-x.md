---
title: Un-breaking OS-X Mountain Lion
date: 2012-12-14 16:49:18 -0800
last_modified_at: 2012-12-14 17:36:18 -0800
permalink: /2012/12/14/un-breaking-mountain-lion-os-x/
slug: un-breaking-mountain-lion-os-x
wp_id: 7228
original_url: https://compositecode.blog/2012/12/14/un-breaking-mountain-lion-os-x/
categories:
- A Bite o' Apple
- How-to
tags:
- apple
- c compiler
- compiler
- error
- exception
- gcc
- gcc 4.2
- mountain lion
- nodejs
- os-x
- os-x mountain lion
- ruby native extensions
- upgrade
excerpt: I posted a blog entry about my efforts last week, which included a rather frustrating experience with a freshly loaded OS-X Mountain Lion install. I had installed XCode and eventually got the Command Line Tools installed, which I outlined in the entry. Things seemed to be working ok, and for the most part in doing …
---

I posted a [blog entry about my efforts last week, which included a rather frustrating experience with a freshly loaded OS-X Mountain Lion install](/2012/12/09/basho-first-week-coding-research-adventures/). I had installed XCode and eventually got the Command Line Tools installed, which I outlined in the entry. Things seemed to be working ok, and for the most part in doing other things all is good, but when trying to install middleman and by reference blockenspiel I ran into an issue getting the C compiler (or any of the compilers I tried) to build the native extensions that were included in this gem. Here’s what I installed and did to finally – FINALLY – get things running right.

The first thing, since it kept coming up, was to get [Homebrew](http://mxcl.github.com/homebrew/) installed.

```bash
ruby -e "$(curl -fsSkL raw.github.com/mxcl/homebrew/go)"
```

I’d already installed RVM, which consists of either the [JewelryBox](http://unfiniti.com/software/mac/jewelrybox) or

```bash
$ \curl -L https://get.rvm.io | bash -s stable --ruby
```

After that I installed Ruby 1.9.3p327.

```bash
rvm install 1.9.3
```

You can check the RVM and Ruby versions by using the -v switch. Also to verify what ruby versions you actually have installed with RVM you can use the list command.

```bash
Adron$ ruby -v
ruby 1.9.3p327 (2012-11-10) [x86_64-darwin12.2.0]
Adrons-MacBook-Air-2:~ Adron$ rvm -v

rvm 1.17.2 (stable) by Wayne E. Seguin <wayneeseguin@gmail.com>, Michal Papis <mpapis@gmail.com> [https://rvm.io/]

papis@gmail.com> [https://rvm.io/]

Adron$ rvm list

rvm rubies

=* ruby-1.9.3-p327 [ x86_64 ]

# => -- current
# =* -- current && default
#  * -- default
```

When I ran ‘rvm requirements’ the current readme doc that is displayed covers a lot of the problems I’ve noticed. It seems there is all sorts of stupid issues between the GCC Compiler and XCode and blagh blagh blagh somebody didn’t even check our stuff before we shipped. This actually goes into detail about what the issues could be if you too have run into this problem.

```bash
To use an RVM installed Ruby as default, instead of the system ruby:

    rvm install 1.8.7 # installs patch 357: closest supported version
    rvm system ; rvm gemset export system.gems ; rvm 1.8.7 ; rvm gemset import system.gems # migrate your gems
    rvm alias create default 1.8.7

And reopen your terminal windows.

Xcode and gcc:

Right now Ruby requires gcc to compile, but Xcode 4.2 and later no longer ship with gcc. Instead they ship with llvm-gcc (to which gcc is a symlink) and clang, neither of which are supported for building Ruby. Xcode 4.1 was the last version to ship gcc, which was /usr/bin/gcc-4.2.

Xcode 4.1 and earlier:
-- Ruby will build fine.

Xcode 4.2 and later (including Command Line Tools for Xcode):
-- If you have gcc-4.2 (and friends) from an earlier Xcode version, Ruby will build fine.
-- If you don't have gcc-4.2, you have two options to get it:
 * Install apple-gcc42 from Homebrew
 * Install osx-gcc-installer

  Homebrew:

  If you are using Homebrew, you can install the apple-gcc42 and required libraries from homebrew/dupes:

      brew update
      brew tap homebrew/dupes
      brew install autoconf automake apple-gcc42
      rvm pkg install openssl

  Xcode 4.2+ install or/and Command Line Tools for Xcode is required to provide make and other tools.

  osx-gcc-installer:

  If you don't use Homebrew, you can download and install osx-gcc-installer: https://github.com/kennethreitz/osx-gcc-installer.

  Warning: Installing osx-gcc-installer on top of a recent Xcode is known to cause problems, so you must uninstall Xcode before installing osx-gcc-installer. Afterwards you may install Xcode 4.2+ or Command Line Tools for Xcode if you desire.

  ** NOTE: Currently, Node.js is having issues building with osx-gcc-installer. The only fix is to install Xcode over osx-gcc-installer.
```

If you need to uninstall XCode you’ll have to follow the directions for each specific version you may have. However for 4.5.2 the steps are as follows.

```bash
sudo <Xcode>/Library/uninstall-devtools --mode=all
```

I wrapped up the current changes and those listed above as follows to see if I could get a good build.

```bash
sudo chown -R `whoami` /usr/local
brew update
brew tap homebrew/dupes
brew install apple-gcc42
```

At the end of all this, still problems. Apple completely screwed the Ruby Community on this one. But really, at the end of the day, the message is don’t frikkin’ install XCode before you get an appropriate gcc installer on your machine. At this point…

I did the unthinkable. I gave up and nuked my machine, loading OS-X back on with a completely fresh installation that has now XCode on it. I went through all of these steps again, minus installing XCode out of order and guess what…

Everything worked.

Computers, ugh!

Until next time, good luck with your install.
