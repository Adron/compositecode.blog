---
title: Language Stack Installation for Python & Go
date: 2020-05-27 11:15:29 -0700
last_modified_at: 2020-05-27 11:15:29 -0700
permalink: /2020/05/27/language-stack-installation-for-python-go/
slug: language-stack-installation-for-python-go
wp_id: 16940
original_url: https://compositecode.blog/2020/05/27/language-stack-installation-for-python-go/
categories:
- Development Machine Environment
- golang
- python
tags:
- development
- development machine
- go
- golang
- python
- setup
- software development
excerpt: Previously I’ve gone through the steps I take to get a solid development machine setup. From the base operating system load, to the browser and basic IDEs I install. Now I’ve got more videos and the respective notes and details about what two language stacks I setup next; Python and Go.
image: /wp-content/uploads/2020/05/computer-hacker-coding-in-dark-TF6D3PB2.jpg
---

Previously I’ve gone through the steps I take to get a solid development machine setup. From the [base operating system load](/2020/05/24/development-machine-environment-build-and-base-os-load/), to the [browser and basic IDEs I install](/2020/05/26/development-machine-environment-build-language-stack-installations-browsers-ides/). Now I’ve got more videos and the respective notes and details about what two language stacks I setup next; Python and Go.

## Python

In regards to the Python stack, this one can often be somewhat confusing. Depending on the operating system I setup the stack a little differently.

### MacOS

For MacOS I’ve written two posts about this previously, one titled “[Getting Started with Python Right!](/2019/12/23/getting-started-with-python-right/)” and one “[Unbreaking Python Through Virtual Environments](/2019/12/25/unbreaking-python-through-virtual-environments/)“. Those two posts cover most of the nuance to getting a base Python stack installed on MacOS and then using virtual environments to manage project specific versions per repository.

### Linux

For the Linux OS, usually a debian variant, the systems tend to have Python 3 installed by default. I then take the next step of installing pip3 and work from there. The IDE, PyCharm from Jetbrains uses virtualenv to setup virtual environments per repository from that point forward.

## Python Setup && Reasons

For more details about the specific walk through, I’ve created this video to walk through setting up Python 3 on Ubuntu and verifying, and also by use of PyCharm to setup a small verification app it shows how the virtualenv sets up a specific environment for the new verification project.

The reasons for installing Python first are numerous. One of the first reasons is that Python is required for installing and using numerous Python related CLIs, such as AWS’s CLI, among many others. It pays off to just have a good install at the system level (i.e. not particular just in a virutal environment, but executable at the terminal on system) to ensure it is available for any and all CLIs that would need it. If you’re into data science work, that’s a huge second reason, because Python is used in about every aspect of data science work, machine learning, and related endeavors.

<iframe allowfullscreen="true" class="youtube-player" height="486" loading="lazy" sandbox="allow-scripts allow-same-origin allow-popups allow-presentation allow-popups-to-escape-sandbox" src="https://www.youtube.com/embed/4lLMDOFxgps?version=3&amp;rel=1&amp;showsearch=0&amp;showinfo=1&amp;iv_load_policy=1&amp;fs=1&amp;hl=en-US&amp;autohide=2&amp;wmode=transparent" style="border:0;" width="863"></iframe>

## Go Setup && Reasons

The reason I go for Go as my second language stack install is driven by two primary reasons:

1. I like writing Go and use it myself for a number of reasons. Such as, it is ridiculously quick and minimal work to build a CLI for use in systems that requires only a single binary executable for use.
2. I use Go for a lot of other work-related efforts, around Kubernetes, Docker, Terraform, and others.

With that, here’s the quick install and initial project for verification setup.

<iframe allowfullscreen="true" class="youtube-player" height="486" loading="lazy" sandbox="allow-scripts allow-same-origin allow-popups allow-presentation allow-popups-to-escape-sandbox" src="https://www.youtube.com/embed/El_rf1eInR4?version=3&amp;rel=1&amp;showsearch=0&amp;showinfo=1&amp;iv_load_policy=1&amp;fs=1&amp;hl=en-US&amp;autohide=2&amp;wmode=transparent" style="border:0;" width="863"></iframe>

If you’d like to take a few other quick tours of Go, here are some posts, with videos, putting together a [Go module project and writing an initial test in under 3 minutes](/2020/04/26/creating-a-go-module-writing-tests-in-less-than-3-minutes/) and setting up an [HTTP server in about 15 minutes](/2020/05/04/simple-http-server-starter-in-15-minutes/).

<iframe allowfullscreen="true" class="youtube-player" height="486" loading="lazy" sandbox="allow-scripts allow-same-origin allow-popups allow-presentation allow-popups-to-escape-sandbox" src="https://www.youtube.com/embed/Qs7vHHQPv18?version=3&amp;rel=1&amp;showsearch=0&amp;showinfo=1&amp;iv_load_policy=1&amp;fs=1&amp;hl=en-US&amp;autohide=2&amp;wmode=transparent" style="border:0;" width="863"></iframe>

<iframe allowfullscreen="true" class="youtube-player" height="486" loading="lazy" sandbox="allow-scripts allow-same-origin allow-popups allow-presentation allow-popups-to-escape-sandbox" src="https://www.youtube.com/embed/xQkJ7ZRA-BI?version=3&amp;rel=1&amp;showsearch=0&amp;showinfo=1&amp;iv_load_policy=1&amp;fs=1&amp;hl=en-US&amp;autohide=2&amp;wmode=transparent" style="border:0;" width="863"></iframe>

That’s it for now. However, if you’re interested in joining me for next steps, language stack setup, and more in addition to writing some JavaScript, Go, Python, Terraform, and more infrastructure, web dev, and all sorts of coding I stream regularly on Twitch at <https://twitch.tv/adronhall>, post the VOD’s to YouTube along with entirely new tech and *metal* content at <https://youtube.com/c/ThrashingCode>. Feel free to check out a coding session, ask questions, interject, or just come and enjoy the tunes!

For more on my open source efforts and related projects, sign up for the [Thrashing Code Newsletter](/thrashing-composite-code-newsletter/)!
