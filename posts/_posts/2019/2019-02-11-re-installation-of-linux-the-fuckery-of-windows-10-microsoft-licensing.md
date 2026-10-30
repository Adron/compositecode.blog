---
title: Re-installation of Linux, The Fuckery of Windows 10 & Microsoft Licensing
date: 2019-02-11 10:12:42 -0800
last_modified_at: 2019-02-26 09:56:11 -0800
permalink: /2019/02/11/re-installation-of-linux-the-fuckery-of-windows-10-microsoft-licensing/
slug: re-installation-of-linux-the-fuckery-of-windows-10-microsoft-licensing
wp_id: 15364
original_url: https://compositecode.blog/2019/02/11/re-installation-of-linux-the-fuckery-of-windows-10-microsoft-licensing/
categories:
- Linux
- microsoft
- Reviews
tags: []
excerpt: 'Notice: TLDR is at the very bottom. Notice: This post may damage sensitive ears. At points it may be vulgar. Notice: If you want to get to just the Linux parts, scroll down to the “Patience and Linux Saves The Day” headline. The Beginning of Horror First a few positives for Windows 10. It runs …'
image: /wp-content/uploads/2019/02/wasntevensupposedtobe2.jpg
---

**Notice**: TLDR is at the very bottom.

**Notice**: This post may damage sensitive ears. At points it may be vulgar.

**Notice**: If you want to get to just the Linux parts, scroll down to the “**Patience and Linux Saves The Day**” headline.

## **The Beginning of Horror**

First a few positives for Windows 10. It runs a Bash system thingy on it now, that’s pretty cool. It loads much faster than Windows 7 (and Vista, LULz). It still plays and supports basically all the games first. It has active tiles, but I guess that’s an arguable positive.

Windows 10 isn’t that horrifyingly bad, it seems, at first glance. But it requires a bunch of unnecessary work to re-map in your brain how it works in relation to the web, to bash, to Linux and the whole \*nix POSIX world. You might say, but why does that even matter? Well, it matters because we’re in a web world, which is at it’s core a POSIX world of Linux and at worst MacOS, but it sure as hell isn’t a Windows world anymore. That’s just what consumers get that are powerless to do anything else about the fact they’re generally always going to be stuck with a purchase between Windows Device and Windows Device.

Now combine that with the fact in the last ~8-10 years almost every major change in the industry through the advent of a new technology, new platform, or otherwise has been released for several years on Linux or MacOS before it even attempts to come to Windows. Docker is a prime example, and it’s arguable that it still doesn’t *really* work on Windows. That’s the starting point of the horror for me.

## **The First Mistake of Mine and Microsoft’s**

The real horror however started with these next few facts. I was pondering keeping Windows 10 on the machine to play games, so I got a key to update Windows 10 from whatever it is to “Professional” so that I could use Docker and Hyper-V. Because Docker doesn’t really run natively on Windows it need Hyper-V to be able to do anything. I “purchased” an upgrade from the Windows Store to Professional so that I could work with Docker and Hyper-V. It went through a process and all seemed well.

## **The Second Mistake**

With Windows 10 upgraded, I also thought it’d be great to have a completely clean install. Windows 10 on this machine had all sorts of cruft on it. Trash games and other junk, I didn’t even realize at this time it was supposed to be the clean version from the Microsoft store. But being that it had so much cruft and other unknown settings, drivers, and configuration mess setup I figured I’d format the drive and reload. To do this I went out and downloaded a Windows 10 image. I *assumed* wrongly that it would give me the version pertinent to whatever the machine has on it, in this case Professional. It gave me “Enterprise” for whatever reason. This was the second mistake.

I then formatted the drive and reloaded Windows 10. I commenced to think everything was fine and dandy, you see, in the docs it says the machine should have the key bound to the hardware. Which I now know is utter bullshit, or simply software that just doesn’t work. I should have known better than to trust this stuff. But I made a mistake, I did, and now I was going to pay for it.

After re-installing Creative Cloud from Adobe, all my JetBrains software, and tons of other things I noticed a whole host of annoyances. Like the fact that the software cruft was still everywhere. I didn’t want this garbage shit, what gives. This was supposed to be a *clean* install. I kept digging about and installing things. I got OBS configured again specifically for Windows 10, because ya see, the folders still disagree on “\” vs “/” and Windows attaches every storage medium to an anchor letter. So all the sources were broken, and the list goes on. I spent hours upon hours getting Windows 10 setup under the notion I’d be able to use it.

Then it happened. Windows reports that it is not activated. So I began the process of activated, I click on updates and such and clicked try again. I went through the loops of help documentation. Nothing was happening. After trying every loop in the help docs that Microsoft provides I was getting frustrated. Then I noticed what the fatal issue was. I somehow now had “Enterprise” loaded and a key for “Professional”. I didn’t know, being what I suspect is a mere “consumer” now, how to actually choose which version of Windows to download. I had no MSDN, didn’t really need or want one, I thought. I also didn’t want to call in any *favors* because I wouldn’t want others to have to do that. Whenever I show or teach, or record things, I want to be able to tell people exactly what I’m using and why. Not that I “*got the hookup*” from inside Microsoft.

I continued, at this point, over 24 hours into the loading, setup, and configuration of this machine and I realize that I don’t even actually have a key, the fucking Microsoft site didn’t save the damned key, and I’m fighting with licensing to recover the OS and make sure that I can use it ongoing. This vain hope of using Windows, of catering and shaping much of my workflow around Windows just so that I could have it for games came from the initially reported (from Dell support itself) that Linux just simply wouldn’t work on the XPS 15 after I had spent 2 hours flailing around trying to install Ubuntu Linux on the machine. For reference, here’s the basic process I went through to get Linux on, but it appeared to fail by freezing up, throwing a bunch of kernel panics, and other miscellaneous nonsense. Either way I had given up and thought Windows 10 would be easier and had invested the time in it to get going.

I even recorded this effort, which is moderately useful and has some good bits of information. But mostly just the installation failure and freeze ups.  🙁

<iframe allowfullscreen="true" class="youtube-player" height="486" loading="lazy" sandbox="allow-scripts allow-same-origin allow-popups allow-presentation allow-popups-to-escape-sandbox" src="https://www.youtube.com/embed/LUQH4K_YsBs?version=3&amp;rel=1&amp;showsearch=0&amp;showinfo=1&amp;iv_load_policy=1&amp;fs=1&amp;hl=en-US&amp;autohide=2&amp;wmode=transparent" style="border:0;" width="863"></iframe>

It was now the end of the weekend, I’d sunk all my time in this, and Windows 10 was now in the late evening of Sunday telling me I didn’t have a legit copy of Windows. I was furious, enraged, and thought I now had a $2k+ dollar brick. I couldn’t get a legit copy of Windows without going some secret back door deal, shelling out even more money for a full copy of Windows, or so I thought. I felt screwed, shorted, and simply fucked over by Microsoft and their misleading notions of how their own software works around Windows. Honestly though, it wasn’t the first time, and I hadn’t felt this enraged with computers and software since the last time – almost a decade ago – when I used Windows and wrote primarily in Visual Studio (not Visual Studio Code).

**End State Condition 1**: Windows 10 loaded and not activated.

![giphy](/wp-content/uploads/2019/02/giphy.gif)

**End State Condition 2:** The wrong version is installed, Enterprise, instead of Professional. Based on the download from the automated consumer download option from Microsoft.

![giphy (3)](/wp-content/uploads/2019/02/giphy-3.gif)

**End State Condition 3:** I was now stuck in a support loop with the docs. No option led to a resolution.

![giphy (1)](/wp-content/uploads/2019/02/giphy-1.gif)

**End State Condition 4:** There was no contact information or way to submit a ticket without paying more money. Consumer support failure.

![giphy (2)](/wp-content/uploads/2019/02/giphy-2.gif)

**Conclusion:** I wasn’t even supposed to be here today.

![wasntevensupposedtobe](/wp-content/uploads/2019/02/wasntevensupposedtobe.jpg)

I was done, even if the laptop became a very expensive paper weight I was done, screw it.

## The Light At the End of the Tunnel Shines!

So I had a beer (huge shout out to [North Coast Brewing](https://northcoastbrewing.com/beers/year-round-beers/old-rasputin-russian-imperial-stout/), [Old Rasputin](https://www.beeradvocate.com/beer/profile/112/412/) **ROCKS!**) and settled myself down into a stupor. Kind of a technology depression I’d fallen into for this Windows garbage again. I knew better I told myself over and over again, “*I knew better*“! At some point about halfway through this wonderful beer, I had another thought, “*I do know better and there’s obviously a way to get Linux installed on this machine!*” Seriously, I’ve fought harder installations than this! I’d tried installing Red Hat 3.2 back in the day and was successful! Ok, I’m going to calmly pick up this Mac here and start researching. I started finding lots of material about how the 9750 XPS 15 basically is plagued with poor driver support for Linux, but then with a few tweaks of keywords and Google-fu coming into play, I hit a few winners! That’s when I started to climb out of this pit of despair and tweeted this.

<blockquote class="twitter-tweet" data-dnt="true" data-width="550">
<p dir="ltr" lang="en">Alright. I'm live tweeting the reinstallation of Linux on this XPS 15. I've just spent the last couple hours figuring out a way to get this done. Here's the first details, in glorious twitter threaded form.</p>
<p>— Adron (@Adron) <a href="https://twitter.com/Adron/status/1092652999925587969?ref_src=twsrc%5Etfw">February 5, 2019</a></p></blockquote>

<script async="" charset="utf-8" src="https://platform.twitter.com/widgets.js"></script>

I thought, even if it takes until 4am no better way for success after this complete debacle with Windows 10 then to just say I’m going to live tweet my efforts via all the hacks and tweaks on websites I’d just found right! Right. But alas, I did, and into the installation I went!

## **Patience and Linux Saves The Day**

With the USB Stick loaded (same as I had done before in the video posted above in which the installation failed) I began. First step forward was to reboot and get into the BIOS (v1.7.0) and turn AHCI mode on under SATA options. I’m honestly not even sure why RAID On was set since there isn’t multiple drives, what even is this black magic in modern BIOS’s I do not know.

![2](/wp-content/uploads/2019/02/2.jpg)

I booted using the F12 key for the boot options menu of the BIOS.

![1](/wp-content/uploads/2019/02/1.jpg)

This process, because of some oddity in the Dell keyboard it’s easier to just press a bunch instead of holding down F12. I show an example in this short video in the tweet below, then selecting the right boot option once at the boot screen.

<blockquote class="twitter-tweet" data-dnt="true" data-width="550">
<p dir="ltr" lang="en">…then select the USB Linux boot stick. Then… <a href="https://t.co/AlMiuYWxfF">pic.twitter.com/AlMiuYWxfF</a></p>
<p>— Adron (@Adron) <a href="https://twitter.com/Adron/status/1092654359895101441?ref_src=twsrc%5Etfw">February 5, 2019</a></p></blockquote>

<script async="" charset="utf-8" src="https://platform.twitter.com/widgets.js"></script>

That gets us to the boot and install Linux screen. Did I mention Ubuntu looks crazy nice on this 4K screen? No? Well it does. Real glossy!

![3](/wp-content/uploads/2019/02/3.jpg)

This is where things are kind of tricky. I need to “*Try Ubuntu without installing*” screen and it flashes by too fast. So a lot of fast button pushing ensues. Click, click, click, click, click, click. Like this, then hit “shift” real fast, then hit “e”! It’s like those console game secret codes practically!! ![😬](https://abs.twimg.com/emoji/v2/72x72/1f62c.png "Grimacing face")  Shown in the tweets below, the button pressing maneuver and the subsequent screen where the next setting needs to be made.

<blockquote class="twitter-tweet" data-dnt="true" data-width="550">
<p dir="ltr" lang="en">Ok, now set 'nomodeset' after the words 'quiet spash'. Which on the XPS 15 is nearly impossible cuz seriously see that little blur of white characters, yeah, those white characters, that's where the change needs made. <a href="https://t.co/qBBGSx7F0U">pic.twitter.com/qBBGSx7F0U</a></p>
<p>— Adron (@Adron) <a href="https://twitter.com/Adron/status/1092658929878818816?ref_src=twsrc%5Etfw">February 5, 2019</a></p></blockquote>

<script async="" charset="utf-8" src="https://platform.twitter.com/widgets.js"></script>

Set `nomodeset` after the words `quiet splash`.

![4](/wp-content/uploads/2019/02/4.jpg)

Next up save that and continue. Then press F10 and the installation screen will appear. Start the installation by clicking that icon up there in the left hand corner that reads “Install Ubuntu 18.04.1 LTS”! Continue through the steps choosing the standard things you’d want. Connect to your WiFi. Then on Updates and Other Software do NOT choose the 3rd part option.

![5](/wp-content/uploads/2019/02/5.jpg)

Then boot into partially busted Ubuntu. A few more steps tho. `sudo gedit /etc/default/grub` and set `nouveau.modeset=0` and then `sudo shutdown -r now`. Then `sudo apt install mokutil`.

![6](/wp-content/uploads/2019/02/6.jpg)

Then it’s the tricky Nvidia Drivers. Gotta use the “*Software & Updates*” option. Don’t use the ppa, so goes the word. Select the “Using NVIDIA driver…” and Apply Changes. Reboot after. ![😑](https://abs.twimg.com/emoji/v2/72x72/1f611.png "Expressionless face")

![7](/wp-content/uploads/2019/02/7.jpg)

![8](/wp-content/uploads/2019/02/8.jpg)

Then this will probably happen. ![👩🏻‍🔧](https://abs.twimg.com/emoji/v2/72x72/1f469-1f3fb-200d-1f527.png "Female mechanic (light skin tone)") So make a password and all, *then* reboot. Note, it’ll show on this screen in plain text. This isn’t 100% sure to happen at this point, based on some things I read, but it likely ****should**** happen. I’d like to hear from you if you’re going through this and it doesn’t popup at this point.

![9](/wp-content/uploads/2019/02/9.jpg)

Then after you enter a password. Do enter a password. Don’t forget it either, even though you’ll rarely enter this one. Then this on reboot will happen, continue.

![11](/wp-content/uploads/2019/02/11.jpg)

Then on reboot check the driver. Check the driver via command line with `nvidea-smi`. If it failed, do another full `sudo apt-get update`.

![12](/wp-content/uploads/2019/02/12.jpg)

Then go and unselect the driver, apply, and select the driver again and apply.

![13](/wp-content/uploads/2019/02/13.jpg)

Then I did some battery tune ups too, even though I’ve also read they’re all there already in the latest Ubuntu. Thus, it doesn’t hurt to run these to make sure.

```bash
sudo apt update
sudo apt install tlp tlp-rdw powertop
sudo tlp start
sudo powertop --auto-tune sudo reboot
```

That was it. I rebooted again, just to make sure all the services were restarted, no kernel panics, no machine freak outs and all that jazz. I then immediately went into installing all the things I wanted on the machine. But more on that later, for now, success had been achieved and the horrors of a $2k+ dollar paperweight had been avoided!

## **TLDR;**

If you’re a coder, use Linux for the sake of us all. Throw Windows 10 in the trash bin, Microsoft already has too, note that everything is going CLI first, container based, and cloud focused Azure ***WHICH IS AWESOME, KEEP DOING IT MICROSOFT***!! Using Windows 10 and attempting to get/keep/verify it upon an error or two is an insult to consumers of the system. It really does seem like the OS is kept around out of pity or something. Final word, Dell and all y’all gotta get that hardware support for Linux going, otherwise what are you even doing as a hardware manufacturer. Push that stuff out there, make it a priority. Dell was one of the preeminent machine options and a king among those that survived the 90’s, a company with amazing support, and a solid coder’s platform. The company is still largely there, but Linux should be an even higher priority. Take another 10-20 people and unleash and enable them on that problem space! Then we all win.

## TLDR; Notice:

It also seems, just in case, always have at least one absolutely wonderful, premium, and spectacularly tasty beer handy to come out of the horrors of technology depression and calm down. It helps. I suppose one could alternate the “beer” for you’re preferred calming beverage like tea or such though.

I wish all vastly better luck in all their installations and interactions with their devices than I had, but rest assured, this XPS 15 is now a beast and beautifully runs Linux (Ubuntu so far)!

On that note, happy thrashing code all, and best of luck and skill in your endeavors!
