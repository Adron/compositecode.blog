---
title: Development Machine Environment Build and Base OS Load
date: 2020-05-24 12:04:11 -0700
last_modified_at: 2020-05-26 10:47:10 -0700
permalink: /2020/05/24/development-machine-environment-build-and-base-os-load/
slug: development-machine-environment-build-and-base-os-load
wp_id: 16910
original_url: https://compositecode.blog/2020/05/24/development-machine-environment-build-and-base-os-load/
categories:
- Development Machine Environment
tags:
- beginner
- getting started
- initial setup
- software developers
- software development
- virtual machines
excerpt: When choosing an operating system to work with there are a number of factors to take into account. Some of these factors include; What language stack and tooling will you need to use? What focus beyond software development will the machine have? What apps and tooling do you already have?
image: /wp-content/uploads/2020/05/hacker-working-using-computer-with-codes.jpg
---

For the next post in this series building a development machine environment check out the [browser & IDEs post](/2020/05/26/development-machine-environment-build-language-stack-installations-browsers-ides/).

<iframe allowfullscreen="true" class="youtube-player" height="486" loading="lazy" sandbox="allow-scripts allow-same-origin allow-popups allow-presentation allow-popups-to-escape-sandbox" src="https://www.youtube.com/embed/syWt2fv5fXE?version=3&amp;rel=1&amp;showsearch=0&amp;showinfo=1&amp;iv_load_policy=1&amp;fs=1&amp;hl=en-US&amp;autohide=2&amp;wmode=transparent" style="border:0;" width="863"></iframe>

*Development Machine Environment Build & Language Stack Installations – Getting a Base OS Load*

## Operating System Notes

When choosing an operating system to work with there are a number of factors to take into account. Some of these factors include;

1. What language stack and tooling will you need to use?
2. What focus beyond software development will the machine have?
3. What apps and tooling do you already have?

There are many other questions, around costs and licensing, and other errata that you’ll need to take into account. One thing however, regardless of what you choose, the bulk of software development with most software languages, their respective tooling stacks work on almost any operating system you’d choose.

In this particular example and the following material I’ve chosen Ubuntu 20.04 LTS (Long Term Support) to use as my operating system. I’ll build a virtualization image of the operating system so that I can reuse time and time again. The virtualization software I’m using is VMWare’s VMWare Fusion software, but just like the operating system you can use most virtualization software and it will work just fine.

## Getting a Base OS Loaded

It is often important to load a ***new*** operating system installation onto a machine for use in application (re: web/software/IoT/mobile/etc) development. This can help us better understand what is installed and effecting various affects on the machine itself, it can insure that we have known assets that aren’t influencing server or other manipulations, and a long list of positives over taking whatever one is given from the various computer system manufacturers.

This post is the first in a series ([here on Dev.to](https://dev.to/adronhall) and on my core blog [https://compositecode.blog](/)). I’m going through precise steps, but I’m keeping it general enough with pointers and related tips for MacOS and Windows that the series will be useful for anyone building their first or tenth or twentieth development machine regardless of operating system or hardware.

## My Installation Specifics

I’m using a Macbook Pro 16″ w/ enough RAM and compute cores that I split off a solid 4-8GB of RAM dedicated to the VM that has the host OS. In addition, I set the compute

To do this, in VMWare Fusion pull up the settings for the Virtual Machine that was created. To note, when the virtual machine is shutdown you can change these settings to add or decrease memory, compute cores, etc. But do note, sometimes this will make an operating system unstable. The rule to follow is, set the resources at time of creation and leave them set.

Once the settings are open, click on the processors and memory option.

[![Settings Screen for the Virtual Machine](/wp-content/uploads/2020/05/Screen-Shot-2020-05-24-at-11.48.21-AM.png)](https://res.cloudinary.com/practicaldev/image/fetch/s--jHP0CJ5p--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https%3A//dev-to-uploads.s3.amazonaws.com/i/7ro2zkrqqddh74gvb0dh.png)

That will display this screen where the values can be set. I also show stepping through this process in the video.

[![Alt Text](/wp-content/uploads/2020/05/Screen-Shot-2020-05-24-at-11.48.38-AM-1.png)](https://res.cloudinary.com/practicaldev/image/fetch/s--IEHcGVKT--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https%3A//dev-to-uploads.s3.amazonaws.com/i/0eag2cbn0icqzdv7fogg.png)

That’s it for now. However, if you’re interested in joining me for next steps, language stack setup, and more in addition to writing some JavaScript, Go, Python, Terraform, and more infrastructure, web dev, and all sorts of coding I stream regularly on Twitch at <https://twitch.tv/adronhall>, post the VOD’s to YouTube along with entirely new tech and *metal* content at <https://youtube.com/c/ThrashingCode>. Feel free to check out a coding session, ask questions, interject, or just come and enjoy the tunes!

For more [Thrashing Code Newsletter](/thrashing-composite-code-newsletter/) for more details about open source projects and related efforts I work on, sign up for it [here](/thrashing-composite-code-newsletter/)!
