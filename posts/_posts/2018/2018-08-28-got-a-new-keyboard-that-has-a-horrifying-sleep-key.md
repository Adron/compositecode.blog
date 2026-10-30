---
title: Got a New Keyboard That Has a Horrifying Sleep Key! @#$%^&@!
date: 2018-08-28 14:06:18 -0700
last_modified_at: 2022-03-30 15:41:47 -0700
permalink: /2018/08/28/got-a-new-keyboard-that-has-a-horrifying-sleep-key/
slug: got-a-new-keyboard-that-has-a-horrifying-sleep-key
wp_id: 14560
original_url: https://compositecode.blog/2018/08/28/got-a-new-keyboard-that-has-a-horrifying-sleep-key/
categories:
- Reviews
tags:
- hardware
- keyboard
- mouse
- review
excerpt: I picked up a Logitech keyboard recently, the MK850 with mouse combo. It was on sale for 80% off, which ran me a mighty $20 bucks. I needed a new keyboard as my Apple keyboard I’ve been using just really doesn’t cut it for a Linux machine. I wanted the function keys and placement of …
image: /wp-content/uploads/2018/08/thatkey1.jpg
---

I picked up a Logitech keyboard recently, the MK850 with mouse combo. It was on sale for 80% off, which ran me a mighty $20 bucks. I needed a new keyboard as my Apple keyboard I’ve been using just really doesn’t cut it for a Linux machine. I wanted the function keys and placement of the extra alt, ctrl, and related keys to be in a more traditional placement. This keyboard is a win. However…![Image from iOS (2)](/wp-content/uploads/2018/08/image-from-ios-2.jpg)

![Image from iOS (1)](/wp-content/uploads/2018/08/image-from-ios-1.jpg)

## Observations

My first observation as I plugged it in to try out, was my attempt to turn up the music, turned into a going to sleep phase for the computer. A few seconds and it was entirely off. This is a full on computer, not a laptop, so I don’t need it to be going to sleep ever. It either needs to be on, completely, or off completely. Let me show you, this key, right here is a damned curse!

![thatkey](/wp-content/uploads/2018/08/thatkey.jpg)

The F11 key, right beside the sound up and down function keys, is the sleep and lock key. Completely unacceptable location. I went into emergency mode on this matter.

## EMERGENCY

A little research and I went full off mode on *sleep*, *hibernate*, and *suspend*! The commands are as follows.

```
gsettings set org.gnome.settings-daemon.plugins.power button-hibernate "nothing"
gsettings set org.gnome.settings-daemon.plugins.power button-sleep "nothing"
gsettings set org.gnome.settings-daemon.plugins.power button-suspend "nothing"
```

Now, if you want those back on however, the commands are specific to the function, as shown below.

```
gsettings set org.gnome.settings-daemon.plugins.power button-hibernate "hibernate"
gsettings set org.gnome.settings-daemon.plugins.power button-sleep "hibernate"
gsettings set org.gnome.settings-daemon.plugins.power button-suspend "suspend"
```

Ok, whew. Errr well, maybe not.

I rebooted and that didn’t actually take effect. I did a little more research and found dconf-tools. So I installed that.

```
sudo apt-get install dconf-tools
```

Opened up dconf and navigated to`org` `gnome` `settings-daemon` `plugins` and then `power`.

![dangerous](/wp-content/uploads/2018/08/dangerous.png)

This editor then showed me what I had technically just set. So that was confirmed, but got me no where. Onward to troubleshooting.

Next research led me to this [option](https://ubuntuforums.org/showthread.php?t=1317325). But then I couldn’t actually get the command to pair to it as it seems the fn or function key plus the F11 key doesn’t actually show up when setting the shortcut keys. Thoughts? If you’ve got any ideas I’m out of ideas for now, do comment or tweet [@Adron](https://twitter.com/Adron).

On with the observations.

Alright, with that fixed I could refocus on the plusses of the keyboard. It’s paired very nicely with the silent mouse, similar to the mouse I reviewed a while back, the [M331 Silent Mouse](/2018/01/29/logitech-m331-silent-mouse/). The keyboard is also extremely silent, with barely any utterance of noise coming from the keyboard. If you like the loud mechanical style, this is not your keyboard. If you want to focus on music or something else while typing then, this is your keyboard.

With that, my quick review and emergency is done. This might be helpful so typed it up but now it’s time to get back to work on some Go prototyping and some solid tunes from Eastern High. For reference, here’s one of their good ones.

<iframe allowfullscreen="true" class="youtube-player" height="486" loading="lazy" sandbox="allow-scripts allow-same-origin allow-popups allow-presentation allow-popups-to-escape-sandbox" src="https://www.youtube.com/embed/o-IYjQvzbkI?version=3&amp;rel=1&amp;showsearch=0&amp;showinfo=1&amp;iv_load_policy=1&amp;fs=1&amp;hl=en-US&amp;autohide=2&amp;wmode=transparent" style="border:0;" width="863"></iframe>
