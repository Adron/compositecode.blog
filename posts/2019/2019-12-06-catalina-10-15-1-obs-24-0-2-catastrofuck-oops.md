---
title: 'Catalina 10.15.1 & OBS 24.0.2 Catastrofuck “Oops” (UPDATE: 24.0.5 Release Fixes)'
date: 2019-12-06 12:31:31 -0800
last_modified_at: 2020-04-16 09:17:03 -0700
permalink: /2019/12/06/catalina-10-15-1-obs-24-0-2-catastrofuck-oops/
slug: catalina-10-15-1-obs-24-0-2-catastrofuck-oops
wp_id: 16593
original_url: https://compositecode.blog/2019/12/06/catalina-10-15-1-obs-24-0-2-catastrofuck-oops/
categories:
- A Bite o' Apple
- Video
tags:
- catalina
- macos
- macos catalina
- obs
- obs studio
- streaming
- twitch
excerpt: 'December 14th, 2019 UPDATE! Scroll to the end of the post for details and link to the latest version. Over the last few months I’ve started working a lot more with DAW’s (Digital Audio Workstation) Software. The main software I’ve been using and have taught myself includes: Logic Pro X, Superior Drummer 3, and EZMix …'
image: /wp-content/uploads/2019/12/obs-studio.jpg
---

***December 14th, 2019 UPDATE! Scroll to the end of the post for details and link to the latest version.***

![catalina](/wp-content/uploads/2019/12/catalina-1.jpg)Over the last few months I’ve started working a lot more with DAW’s (Digital Audio Workstation) Software. The main software I’ve been using and have taught myself includes: Logic Pro X, Superior Drummer 3, and EZMix 2. I’ve written and played music for more years than I’ll count, and have wanted to make Twitch streaming one of my outlets to produce, mix, write, and offer up music that I put together.

![obs-studio](/wp-content/uploads/2019/12/obs-studio.jpg)Since I’ve spent the time training up on Logic Pro X, that ties me somewhat to MacOS. I could switch to something else and there would be some familiarities. But whatever the case that would mean I’d need to retrain myself on those non-familiar nuances of the software. The other software I use is offered as either MacOS or Windows and considering I’ve seen how Windows behaves with many of these things, bloats up with other things, and overall gives me a general UX distaste I didn’t really want to move or shift to that OS.

That leaves me running MacOS to insure the software works and move forward. Honestly, it’s a slick package when they’re all rolled together. Don’t think I haven’t just abandoned Windows and Linux for other things, I haven’t. Linux is still basically my daily driver for almost every single things I do besides produce music. Coding is Linux, document and documentation writing is on Linux, building websites is on Linux, gaming ironically is on Linux, Docker runs better on Linux, Kubernetes basically runs on Linux, Go is just kind of easier on Linux, and even .NET, C#, F#, Python, and so much more is all over there running on Linux with less resistance. The Dell XPS 15 running Ubuntu is a solid platform for all of these things. Albeit I’m not sure what could happen because much of the IDE/platform software is easier and more feature reach and integrated on MacOS. So all that said, here I am, running MacOS to ensure I can produce and write music without resistance the other platforms cause.

## The Current Catalina Problem

All that said, the recent upgrade to Catalina has left me with a black eye square in the face! OBS simply is broken, for the most part, if one launches it or uses it in the traditional way one would use it. I’ve found myself continually launching it from the terminal, which appears to alter the way it starts and then it respectively demands access to the devices that it needs. To do that it’s just a single command;

```
/Applications/OBS.app/Contents/MacOS/OBS
```

i.e. I just run the app, from the executable. This, as I was writing seems to fix many of the permissions issues and allow OBS to run without hindrance. However it is one of many apps that cause issues.

That’s it for this post, just an update and a few notes + links about where I am with this effort. Eventually, music composition, production, and bouncing (recording and export to MP3/WAV/etc) will be my weekend Twitch schedule. For now however it’s an ongoing battle to get all the pieces working appropriately with MacOS Catalina. It is new, so I imagine most of these issues will be worked on the coming weeks. Stay tuned!

---

***UPDATE DETAILS:***

*New version of OBS released with tons of Catalina (and Linux) fixes! Release notes on all the updates, fixes, tweaks, and errata.*

- *Fixed macOS Catalina issues*
- *Fixed macOS Python scripting support*
- *Fixed a bug where audio bitrate would not be properly set to the specified value in simple output mode*
- *Fixed a bug where videos on loop could sometimes get frozen when switching scenes*
- *Fixed a bug with Linux Display Capture where the crop value would shift the cursor’s captured position incorrectly*
- *Fixed an issue where if the video drivers crashed on Windows for whatever reason, OBS would not recover from that properly and also crash (yes you heard that correctly)*
- *Fixed an issue where when connecting to your Twitch account fails because of Twitch’s two-factor authentication requirement, you would not be able to change to another Twitch account until authentication was fixed and the account was reconnected*
- *Fixed an issue where when connecting your Twitch account for the first time, the panels would not open up in dark mode*
- *Fixed an issue where preview projector stopped working when toggling studio mode*
- *Fixed an issue where multiple 0x0 windows would appear on Linux Window Capture*
- *Fixed an issue where certain windows would not be listed with Linux Window Capture*
- *Fixed a few rare crashes*
- *You can now use Twitch dashboard panel URLs as custom browser docks*
- *Added some additional graphics and audio diagnostic logging*
