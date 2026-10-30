---
title: Learning Go Episode 1 – Environment, Go Workspace, GOPATH/GOROOT, Types, and more Introduction
date: 2019-01-19 14:34:34 -0800
last_modified_at: 2019-07-05 19:38:57 -0700
permalink: /2019/01/19/learning-go-episode-1/
slug: learning-go-episode-1
wp_id: 15219
original_url: https://compositecode.blog/2019/01/19/learning-go-episode-1/
categories:
- golang
- ThrashingCode
- Video
tags:
- coding
- go
- golang
- learning
- learning to code
- programming
excerpt: 'Episode Post & Video Links: 1 (this post), 2, 3, 4, 5, 6, 7, and 8. Non-linked are in the works! Videos available now on Youtube however, so check em’ out! This is episode one of a multi-part series on “The Go Programming Language“. Not necessary, but if you’d like to follow along you can …'
image: /wp-content/uploads/2018/10/thrashing-code-metal-gopher.png
---

Episode Post & Video Links:  1 (this post), [2](/2019/02/06/learning-go-episode-2-further-into-packages-dependencies-application-creation-and-ides/), [3](/2019/03/10/learning-go-episode-3-more-data-types-casting-rendering-an-svg-file-and-writing-to-files/), [4](/2019/05/27/learning-go-episode-4-composite-types-slices-arrays-etc/), [5](/2019/07/05/learning-go-episode-5-functions-and-methods-and-lots-of-other-things/), 6, 7, and 8. Non-linked are in the works! Videos [available now on Youtube](https://www.youtube.com/playlist?list=PL4f75Y6Ce5ssiDTjB0Y_D7a-13eeAepHn) however, so check em’ out!

This is episode one of a multi-part series on “[The Go Programming Language](http://www.informit.com/store/go-programming-language-9780134190440)“. Not necessary, but if you’d like to follow along you can also pick up the book “The Go Programming Language” by Alan A. A. Donovan and Brian W. Kernighan. At the bottom of the description I have a link to the book publisher’s website and the respective book. I’ll be using that as a guideline and using a number of examples from the book. However I’ll also be adding a lot of additional material around [Goland IDE](https://www.jetbrains.com/go/) from [Jetbrains](https://www.jetbrains.com/) and [Visual Studio Code](https://code.visualstudio.com/). The video link to this session is at the bottom of the post, scroll all the way down and it’s waiting for you there.

[3:28](https://youtu.be/lqIG0EBbRbQ/watch?v=lqIG0EBbRbQ&t=208s) – Getting started, introducing that the session I’m starting with a completely new Ubuntu Linux load so that I ensure we cover all of the steps to get up and running. These steps, even though they’re on Linux are reproducible on Windows 10 and MacOS, so any operating system is usable to follow along with, with only minor discrepancies.

[5:04](https://youtu.be/lqIG0EBbRbQ/watch?v=lqIG0EBbRbQ&t=304s) – Introducing the book that I’ll be using as a guideline reference so that viewers can also follow along with a physical book. I’m a big fan of multisensory learning, so between a book, the stream, being able to ask questions in the channel, it’ll give viewers a chance to learn and undertake their coding adventures in Go using all sorts of methods.

**Book Reference**: “[The Go Programming Language](http://www.informit.com/store/go-programming-language-9780134190440)” by Alan A. A. Donovan and Brian W. Kernighan

[6:58](https://youtu.be/lqIG0EBbRbQ/watch?v=lqIG0EBbRbQ&t=418s) – Discussing where Go is located on the web related to Github and the golang.org site that is useful in that one can even try out little snippets of Go code itself, on the site!
**Github**: <https://github.com/golang/go>
**Golang**: <https://golang.org>
[10:40](https://youtu.be/lqIG0EBbRbQ/watch?v=lqIG0EBbRbQ&t=640s) – Setting export in the .bashrc file (or .bash\_profile on MacOS or environment variables on Windows 10). Speaking of Windows 10 specifically, Linda Gregier wrote up a great blog post on getting Go setup on Windows specifically.
[14:50](https://youtu.be/lqIG0EBbRbQ/watch?v=lqIG0EBbRbQ&t=890s) – Setting up the Go workspace path for GOPATH using the standard Go convention. From here I get into the first “Hello World!” with Go.
[15:34](https://youtu.be/lqIG0EBbRbQ/watch?v=lqIG0EBbRbQ&t=934s) – Mention of setting up Go on a Docker container and how it is easier, but we’re staying focused on setting it up completely from scratch.
[18:20](https://youtu.be/lqIG0EBbRbQ/watch?v=lqIG0EBbRbQ&t=1100s) – Starting first code, a standard “Hello World” program.
[19:50](https://youtu.be/lqIG0EBbRbQ/watch?v=lqIG0EBbRbQ&t=1190s) – First build of that “Hello World” program.
[20:34](https://youtu.be/lqIG0EBbRbQ/watch?v=lqIG0EBbRbQ&t=1234s) – Here I introduce `go run` and how to execute a singular file instead of building an entire project.
[21:32](https://youtu.be/lqIG0EBbRbQ/watch?v=lqIG0EBbRbQ&t=1292s) – Installing some IDE’s to use for developing Go applications. The first two up for installation is Visual Studio Code and JetBrains Goland.
[29:00](https://youtu.be/lqIG0EBbRbQ/watch?v=lqIG0EBbRbQ&t=1740s) – A first variable, what is it, and how to declare one in Go in one of the ways one can declare a variable in Go!
[31:08](https://youtu.be/lqIG0EBbRbQ/watch?v=lqIG0EBbRbQ&t=1868s) – Introducing the terminal in Visual Studio Code.
[37:12](https://youtu.be/lqIG0EBbRbQ/watch?v=lqIG0EBbRbQ&t=2232s) – A little example of OBS, how I’m using it, and how I interact back and forth with chat and related tooling plus the virtual machine itself.
[42:36](https://youtu.be/lqIG0EBbRbQ/watch?v=lqIG0EBbRbQ&t=2556s) – Changing themes and adding plugins for Goland. In the plugins I also find the most epic of status bars, the Nyan Cat!
[59:00](https://youtu.be/lqIG0EBbRbQ/watch?v=lqIG0EBbRbQ&t=3540s) – Here I start to get back into some more specific Go details. Starting off with a Go command line parsing application. At this point I also cover several additional ways to declare variables, speak more about short declarations, and other ways to declare, assign, and use variables in Go.

At this point I also go through a number of examples to exemplify how to go about declaring variables, build, run, and explore the details of the code. Further along I also get into string formatting, concatenating, and related string manipulation with Go.

Other details include taking a look at extra ways to figure out Go code using autocomplete inside Goland and other exploratory features. Eventually before wrapping up I broach pointers, tuple declaration techniques, and how to declare additional functions beyond `func main()`.
[1:58:40](https://youtu.be/lqIG0EBbRbQ/watch?v=lqIG0EBbRbQ&t=7120s) – Adding dependencies and generating random data. At this point I bring in a dependency. But before pulling in the dependency, after introducing it, I show how to go about doing.
[2:00:10](https://youtu.be/lqIG0EBbRbQ/watch?v=lqIG0EBbRbQ&t=7210s) – New machine, and I run into git not being available. The `go get` command uses git to pull dependencies so I go about why this is needed and the steps to install on Ubuntu.
[2:09:20](https://youtu.be/lqIG0EBbRbQ/watch?v=lqIG0EBbRbQ&t=7760s) – Introduction to more concepts around dependencies, what `go get` does versus managing dependencies with Go Dep.
[2:10:00](https://youtu.be/lqIG0EBbRbQ/watch?v=lqIG0EBbRbQ&t=7800s) – Installing Go Dep; MacOS, using curl, Linux installation, and a question sort of remains to get it running on Windows. The easiest method is using chocolatey however, so check that out if you’re going the Windows route.
[2:15:20](https://youtu.be/lqIG0EBbRbQ/watch?v=lqIG0EBbRbQ&t=8120s) – Setting up Go Dep integration with Goland.
[2:23:55](https://youtu.be/lqIG0EBbRbQ/watch?v=lqIG0EBbRbQ&t=8635s) – Showing off Goland’s commit dialog and some of the respective options.

<iframe allowfullscreen="true" class="youtube-player" height="486" loading="lazy" sandbox="allow-scripts allow-same-origin allow-popups allow-presentation allow-popups-to-escape-sandbox" src="https://www.youtube.com/embed/lqIG0EBbRbQ?version=3&amp;rel=1&amp;showsearch=0&amp;showinfo=1&amp;iv_load_policy=1&amp;fs=1&amp;hl=en-US&amp;autohide=2&amp;wmode=transparent" style="border:0;" width="863"></iframe>
