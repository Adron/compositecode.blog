---
title: Getting Started with Twitch | Twitch Thrashing Code Stream
date: 2018-07-08 17:45:32 -0700
last_modified_at: 2018-07-08 17:50:13 -0700
permalink: /2018/07/08/getting-started-with-twitch-twitch-thrashing-code-stream/
slug: getting-started-with-twitch-twitch-thrashing-code-stream
wp_id: 14298
original_url: https://compositecode.blog/2018/07/08/getting-started-with-twitch-twitch-thrashing-code-stream/
categories:
- Coding Adventures
- How-to
- Video
tags:
- coding
- streaming
- thrashing code
- tv
- twitch
- video
- video streaming
excerpt: I’d been meaning to get started for some time. I even tweeted, just trying to get further insight into what and why people watch Twitch streams and of course why and who produces their own Twitch streams. 📺What do you watch on Twitch? 👀Why do you watch it? 📹Why do you make your twitch stream? …
image: /wp-content/uploads/2018/07/combologo_474x356.png
---

I’d been meaning to get started for some time. I even tweeted, just trying to get further insight into what and why people watch [Twitch](https://www.twitch.tv/) streams and of course why and who produces their own [Twitch](https://www.twitch.tv/) streams.

<blockquote class="twitter-tweet" data-dnt="true" data-width="550">
<p dir="ltr" lang="en">📺What do you watch on Twitch?</p>
<p>👀Why do you watch it?</p>
<p>📹Why do you make your twitch stream?</p>
<p>— Adron (@Adron) <a href="https://twitter.com/Adron/status/1014199767742623744?ref_src=twsrc%5Etfw">July 3, 2018</a></p></blockquote>

<script async="" charset="utf-8" src="https://platform.twitter.com/widgets.js"></script>

With that I set out to figure out how to get the right tooling setup for Twitch streaming on Linux and MacOS. Here’s what I managed to dig up.

First things first, and somewhat obviously, go create a Twitch account. The sign up link is up in the top right corner.

<https://www.twitch.tv/>

## MacOS Setup

1. There’s the [MacOS Application to download](https://app.twitch.tv/download).
2. Next I downloaded the [Open Broadcast Software](https://obsproject.com/).
3. Then I followed the [Quickstart for OBS](https://obsproject.com/wiki/OBS-Studio-Quickstart).
4. For MacOS I also had to [download and install audio capture](https://support.shinywhitebox.com/hc/en-us/articles/204161459-Installing-iShowU-Audio-Capture). There were very specific instructions on [setting this up here](https://obsproject.com/forum/resources/os-x-capture-audio-with-ishowu-audio-capture.505/).

Once all of this is setup, then I had to get OBS to actually take some type of video stream of some sort. I could set the webcam, video, or other means by selecting it.

![obs-video-selection.png](/wp-content/uploads/2018/07/obs-video-selection.png)

One arrow points to the plus arrow that pops the option list up. Each of those settings pointed at then include:

- Display Capture – grabs the entire screen of the computer.
- Media Source – lets you select certain options like webcam or other video elements.
- Game Capture (Syphon) – I didn’t get to work just yet, but it appears that’ll capture specifically the game screen.
- Video Capture Device – This is also the webcam.
- Window Capture – This captures a singular window.

## Linux Setup

With the Linux setup I’m using Ubuntu 18.04 on a [Dell XPS 13](/2018/07/04/dell-xps-13-re-review-of-existing-laptop/) (click for my [review](/2018/07/04/dell-xps-13-re-review-of-existing-laptop/)) and the [System 76 Leopard Workstation](/2017/01/19/buying-a-leopard/) (click for my [review](/2017/01/19/buying-a-leopard/)) I have. For both I went ahead and went the route I went on the MacOS Laptops I have and installed [OBS](https://obsproject.com/).

1. For Ubuntu I just used apt-get to install everything, starting with FFmpeg.

   ```bash
   sudo apt-get install ffmpeg
   ```
2. Next step is to setup the repository ppa.

   ```bash
   sudo add-apt-repository ppa:obsproject/obs-studio
   ```
3. Now update and install OBS for Linux.

   ```bash
   sudo apt-get update
   sudo apt-get install obs-studio
   ```
4. When I open the app for the first time, just like on the MacOS version, I went ahead and selected the auto-configuration wizard to start. After stepping through that OBS was pretty much ready to go. Fewer steps than the MacOS.

## Curiosities, Experiments, and Things

My next step is to test out the streaming options, make some videos, and also figure out how this is going to fit into my Thrashing Code Show/VLOGing. But also to see what happens when I try variable number of machines streaming and related things. These experiments could be super fascinating depending on how or if certain things are possible. So as always, subscribe to whichever things you’d like, my blog subscription is over on the left of the blog (*I’ve no idea how to subscribe on the mobile site, lemme know if you figure it out*) or of course just [follow me on Twitch](https://www.twitch.tv/adronhall/).
