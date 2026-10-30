---
title: OS-X and F# [Clone It, Build It, Install It, Hack It]
date: 2015-05-07 23:30:42 -0700
last_modified_at: 2015-05-07 23:43:27 -0700
permalink: /2015/05/07/os-x-and-f-clone-it-build-it-install-it-hack-it/
slug: os-x-and-f-clone-it-build-it-install-it-hack-it
wp_id: 10998
original_url: https://compositecode.blog/2015/05/07/os-x-and-f-clone-it-build-it-install-it-hack-it/
categories:
- Certifications
- How-to
tags:
- f#
- fp
- fsharp
- functional programming
- os-x
excerpt: 'Ok. Mission: Get F# running on OS-X and executing via repl.'
---

[![](/wp-content/uploads/2015/05/fsharp_logomark_october_2014-svg.png)](/wp-content/uploads/2015/05/fsharp_logomark_october_2014-svg.png)Ok.

Mission: Get F# running on OS-X and executing via repl.

There are a number of steps here, that if you don’t have everything covered things just won’t work. So let’s knock out the prerequisites first. This will include getting autoconf installed. There are some other tools that I’ve added below that are good to have installed too, so get autoconf, automake, and libtool installed.

```bash
export build=~/devtools # or wherever you'd like to build
mkdir -p $build

cd $build
curl -OL http://ftpmirror.gnu.org/autoconf/autoconf-2.68.tar.gz
tar xzf autoconf-2.68.tar.gz
cd autoconf-2.68
./configure --prefix=/usr/local
make
sudo make install
export PATH=/usr/local/bin

cd $build
curl -OL http://ftpmirror.gnu.org/automake/automake-1.11.tar.gz
tar xzf automake-1.11.tar.gz
cd automake-1.11
./configure --prefix=/usr/local
make
sudo make install

cd $build
curl -OL http://ftpmirror.gnu.org/libtool/libtool-2.4.tar.gz
tar xzf libtool-2.4.tar.gz
cd libtool-2.4
./configure --prefix=/usr/local
make
sudo make install
```

Now we’re ready to get some F# (64-bit flavors too) running on OS-X. This is very likely to take more than a few minutes because we’ve got two actual builds to do here.

First step is to get mono built and installed.

```bash
git clone https://github.com/mono/mono
cd mono
./autogen.sh --prefix=/mono64 --enable-nls=no
make
sudo make install
```

Now clone fsharp, build and install it.

```bash
git clone https://github.com/fsharp/fsharp
cd fsharp
./autogen.sh --prefix=/mono64
make
sudo make install
```

Finally get the binary executable paths added to the paths file.

```bash
vi /etc/paths
```

Add the following paths to the paths file.

```bash
/mono64/bin/mono
/mono64/bin
```

Once that’s done, run the tests to confirm everything has built right and is operable.

```bash
cd tests/fsharp/core
./run-all.sh
```

Now… that should all be ok.

## repl

What I wanted now is something to sling some code and execute it. The easiest way, is to use the ‘fsharpi’ repl. At the OS-X terminal launch the repl.
Enter this line…

```bash
let x = 5;;
```

Then let y to a value…

```bash
let y = 20;;
```

Then enter…

```bash
y + x;;
```

…and you should see the math calculated. Then you can quit out of the repl with the following command.

```bash
#quit;;
```

The overall repl should come out looking like this.

```bash
> let x = 5;;

val x : int = 5

> let y = 20;;

val y : int = 20

> y + x;;
val it : int = 25
> #quit;;

-- Exit...
```

Compilation – A Step Further

Just to show one more step. Let’s do a compile of a file with F# Code in it. Create a file called process.fs and enter the following code.

```fsharp
open System

[<EntryPoint>]
let main (argv :string[]) =
    printfn "Hello World"
    Console.ReadLine() |> ignore
    0
```

Now run the compiler ‘fsharpc’.

```bash
fsharpc process.fs
```

Now before you freak out screaming “OMG WTF am I supposed to do with a process.exe file…!!!” just calm down and execute the following command.

```bash
mono process.exe
```

There you’ll see the execution of “Hello World”. Welcome to F# on OS-X. More to come, Keep thrashing code!

Note: I’ve got a github repo for this and coming F# coding available at [sharpgrounds](https://github.com/Adron/sharpgrounds).
