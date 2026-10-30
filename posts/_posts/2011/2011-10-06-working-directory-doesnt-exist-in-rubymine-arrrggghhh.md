---
title: “Working Directory doesn’t exist” in Rubymine!  ARRRGGGHHH!!
date: 2011-10-06 18:52:42 -0700
last_modified_at: 2011-10-06 20:21:48 -0700
permalink: /2011/10/06/working-directory-doesnt-exist-in-rubymine-arrrggghhh/
slug: working-directory-doesnt-exist-in-rubymine-arrrggghhh
wp_id: 4042
original_url: https://compositecode.blog/2011/10/06/working-directory-doesnt-exist-in-rubymine-arrrggghhh/
categories:
- How-to
- Ruby on Rails Bits
tags:
- jetbrains
- rails
- ruby
- rubymine
excerpt: So a few weeks back I created a Rubymine Ruby on Rails Project I was kicking off. I got it running, did some scaffolding, started customizing that for what I needed. I had created this project on Windows 7 and did not realize the implications of this. I did a clone via github of the code on a Mac via bash. I then opened Rubymine and opened the project. That’s when I got this error message, “Working Directory doesn’t exist”. I thought, well what the… no reason for this. I’ve barely edited the project. I checked out the Jetbrains Forums and didn’t find an answer at the time, but did find others having the problem. Just today, Tyler Williams posted what had happened. Being that I don’t delete my projects, even slightly broken, for many days I went back to look at the .idea files as Tyler Williams suggested. Sure enough, my setting was hard coded (I suppose by the IDE??). Which leads me to my recent thought that maybe I’ll be using TextMate more and Rubymine a little less. Even though, I do love the refactorings, code completion, and all that. But since I’m in the learning stage, and I’m doing hard core TDD (best I can with Ruby 🙂 ) I ought to not use the IDE as a crutch and instead force myself to learn the language well & the Rails Technology Framework! I’m getting there, but the battle still exists for me. At this point, I do my Ruby & Rails work about 1/2 in TextMate and 1/2 in Rubymine. Anyway, if you run into “Working Directory doesn’t exist” in Rubymine, now you have a good lead on what to do.
---

![](/images/adronhall.smugmug.com/Software/Software-Development/Technology-Company-Logos/i-cmzD2wP/0/O/rubymine.png)So a few weeks back I created a Rubymine Ruby on Rails Project I was kicking off. I got it running, did some scaffolding, started customizing that for what I needed. I had created this project on Windows 7 and did not realize the implications of this. I did a clone via github of the code on a Mac via bash. I then opened Rubymine and opened the project. That’s when I got this error message, “Working Directory doesn’t exist”. I thought, well what the…   no reason for this. I’ve barely edited the project!!

I checked out the Jetbrains Forums and didn’t find an answer at the time, but did find [others having the problem](http://devnet.jetbrains.net/message/5285770#5285770). Just today, [Tyler Williams posted what had happened](http://devnet.jetbrains.net/message/5321538#5321538). Being that I don’t delete my projects, even slightly broken, for many days I went back to look at the .idea files as Tyler Williams suggested. Sure enough, my setting was hard coded (I suppose by the IDE??).

Which leads me to my recent thought that maybe I’ll be using TextMate more and Rubymine a little less. Even though, I do love the refactorings, code completion, and all that. But since I’m in the learning stage, and I’m doing hard core TDD (best I can with Ruby 🙂 ) I ought to not use the IDE as a crutch and instead force myself to learn the language well & the Rails Technology Framework! I’m getting there, but the battle still exists for me. At this point, I do my Ruby & Rails work about 1/2 in TextMate and 1/2 in Rubymine. Anyway, if you run into “Working Directory doesn’t exist” in Rubymine, now you have a good lead on what to do.
