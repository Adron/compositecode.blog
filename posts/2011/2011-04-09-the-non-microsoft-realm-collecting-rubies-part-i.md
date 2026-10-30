---
title: The Non-Microsoft Realm, Collecting Rubies Part I
date: 2011-04-09 21:54:30 -0700
last_modified_at: 2011-04-16 17:49:58 -0700
permalink: /2011/04/09/the-non-microsoft-realm-collecting-rubies-part-i/
slug: the-non-microsoft-realm-collecting-rubies-part-i
wp_id: 2580
original_url: https://compositecode.blog/2011/04/09/the-non-microsoft-realm-collecting-rubies-part-i/
categories:
- How-to
- Linux
- Ruby on Rails Bits
tags:
- curl
- gems
- git
- linux
- ruby
- ruby on rails
- rvm
- tekpub
excerpt: Years ago I worked with Linux (Redhat 3.2, SUSE, Gentoo, and Slackware among others) and also played around with PHP. I’ve never really gotten too keen in PHP, mainly because it just seemed sort of a mess. But when I needed something to get the job done and didn’t want to wait on the bureaucratic …
---

Years ago I worked with Linux (Redhat 3.2, SUSE, Gentoo, and Slackware among others) and also played around with PHP.  I’ve never really gotten too keen in PHP, mainly because it just seemed sort of a mess.  But when I needed something to get the job done and didn’t want to wait on the bureaucratic nonsense of corporate governance, PHP was there for me, albeit with a headache to follow.

However my interest in Linux and alternate development stacks, being in Southern Mississippi left me pretty much one option if I wanted to get into software development:  Microsoft’s .NET Framework.

So I learned that, and work with it regularly, and I dig it.  Most of the time.  It serves its purpose.  I have however wanted more, so I’ve started digging into other things again.  This is something I do frequently, and in my not so humble opinion think any serious developer should also dive into regularly.  Step outside of your comfort zone and try other things out, often this helps expand both options (such as .NET and Java, or Ruby on Rails, or whatever).

Recently I’ve decided I’m diving head long straight into Ruby on Rails.  I’m working on a new personal project and have determined I’m not going to use one lick of Microsoft Software (you can read in other motivations if you want to).  This project will be 100% Linux (maybe some Apple Gear & Bits) and Ruby on Rails.  I’ve not determined much beyond that.  Database or data store, TBD, graphics, TBD, and other such are all TBD.

[![Ubuntu Download](/images/adronhall.smugmug.com/Software/Software-Development/Ubuntu-Tekpub-and-Ruby-on/Ubuntu/1245476025_mbNjK-S.png "Ubuntu Download")](http://www.ubuntu.com/desktop/get-ubuntu/download)

*Ubuntu Download*

With that, this is how & where I started from the ground up.

1. I snagged Ubuntu and loaded it (yes, it does dual boot on my machine that runs Windows 7).  <http://www.ubuntu.com/>
2. Next I went straight to [TekPub](http://tekpub.com/) and started downloading some of the Ruby on Rails Video Tutorials the crew over there has put together.  I purchased a membership because they’ve put out a lot of great material on everything from .NET, Entity Framework, NHibernate, Good SOLID Code, to Linux and Ruby on Rails.  I like the efforts, the teaching style, and they’re rather entertaining.  If you really don’t want to shell out any cash, there are other videos available on the [Ruby on Rails Site](http://rubyonrails.org/screencasts).
3. I hit a few snags on working with Ubuntu, mainly because I had not touched a Linux UI System in years.  The first two issues were;  1) [How do I change the screen settings to not duplicate my dual monitors](http://www.thegeekstuff.com/2009/08/ubuntu-tips-how-to-setup-dual-monitor/) and 2) [How do I take screenshots](http://tips.webdesign10.com/how-to-take-a-screenshot-with-ubuntu-linux).  < Click on the respective issue to see what page I found to resolve the issue.  Yes, they were both that easy to resolve.  Literally first click links of Google results.  Very cool.  🙂
4. ![](/images/adronhall.smugmug.com/Software/Software-Development/Ubuntu-Tekpub-and-Ruby-on/WatchingTekPubVideos/1245865897_6NQsQ-S.png)The next issue I ran into was related to playing the TekPub Videos.  Using the Synaptic Package Manager however I was able to download all the additional codecs I needed.  I have to say, since the UX was vastly superior to Microsoft’s Windows Media Player (or whatever it’s called these days) I was able to get the codecs without much manual searching.  I just clicked ok, the package manager popped up, found what I needed, and I clicked OK.  This experience reminds me more of Apple’s OS-X than Windows strangely enough.
5. With the [TekPub](http://tekpub.com/) Videos now viewable I downloaded the first [Rails 3 Video](http://tekpub.com/view/rails3/1).

While watching the video, which includes great coverage of what Rails 3 is all about, I worked through the following bits.  For these I also left the GUI Synaptic Package Manager and went with the command line, simply, it is just easier and faster.

### Git

> This was stupid simple.
>
> ```bash
> sudo apt-get install git git-gui git-doc gitk
> ```

### Build Bits

> Some important parts for building Ruby.  Yeah, this is kind of a kicker, super long, crazy command, best to copy and paste.  😉
>
> ```bash
> sudo apt-get install build-essential bison openssl libreadline6 libreadline6-dev curl git-core zlib1g zlib1g-dev libssl-dev libyaml-dev libsqlite3-0 libsqlite3-dev sqlite3 libxml2-dev libxslt-dev autoconf libc6-dev ncurses-dev
> ```

### Curl

> Reached out and got some curl.
>
> ```bash
> sudo apt-get install curl git-core
> ```

### RVM (Ruby Version Manager)

> Bash some [Ruby Version Manager](https://rvm.beginrescueend.com/).  Note I put in “cd~” just as a reminder to get to your user directory.  Most likely, after installing RVM you’d already be in that directory.
>
> ```bash
> bash < <(curl -s https://rvm.beginrescueend.com/install/rvm)
> cd ~
> gedit .bashrc
> ```
>
> At the very bottom of the .bashrc file add the following text.
>
> ```bash
> [[ -s "$HOME/.rvm/scripts/rvm" ]] && . "$HOME/.rvm/scripts/rvm"
> ```

> Once you’ve done that, close the terminal down and then reopen it so that all the paths and such can load.
>
> ```bash
> sudo apt-get install libruby1.9 zlib1g-dev libssl-dev libreadline5-dev build-essential
> ```

### Ruby 1.9.2 Bits

> Now comes the exciting part, getting Ruby loaded up good and proper.
>
> ```bash
> rvm install 1.9.2 --with-zlib-dir=~/.rvm/usr
> rvm use 1.9.2 --default
> ```
>
> Now if you check with “ruby -v” the ruby 1.9.2p0 version will be default.
>
> [![Setting Ruby 1.9.2 as Default](/images/adronhall.smugmug.com/Software/Software-Development/Ubuntu-Tekpub-and-Ruby-on/ruby-installed/1245953024_bazwY-S.png "Setting Ruby 1.9.2 as Default")](http://adronhall.smugmug.com/Software/Software-Development/Ubuntu-Tekpub-and-Ruby-on/16541687_96rYA#1245953024_bazwY-O-LB)
>
> *Setting Ruby 1.9.2 as Default*

### Collecting Gems

> Now you’ll need some bits, in this case, called gems.  This is one of the very powerful parts of Ruby on Rails.  Beware, these bits have glorious AWESOME all over em’.
>
> ```bash
> gem list
> gem install rails
> ```
>
> The gem list command should list what is currently installed. Initially, only the rake gem is installed.  Once you execute gem install rails, then do another gem list, you’ll have a whole set of gems installed.

### Checkup On Your Software

> These are just a few of the commands that are helpful in identifying what is installed now. Try em’ out to get a view of what is available.
>
> ```bash
> rvm gemset name
> gem list
> ```
