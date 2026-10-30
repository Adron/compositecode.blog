---
title: Bash, Ruby, and Such Console Installation Version Management Bits for OS-X
date: 2011-09-05 11:42:13 -0700
last_modified_at: 2011-09-05 11:42:13 -0700
permalink: /2011/09/05/bash-ruby-and-such-console-installation-version-management-bits-for-os-x/
slug: bash-ruby-and-such-console-installation-version-management-bits-for-os-x
wp_id: 3652
original_url: https://compositecode.blog/2011/09/05/bash-ruby-and-such-console-installation-version-management-bits-for-os-x/
categories:
- How-to
- Ruby on Rails Bits
tags:
- bash
- bash console
- console
- rails
- ruby
- ruby on rails
- ruby version manager
- rvm
- terminal
excerpt: I went to reinstall RVM (Ruby Version Manager) and got a message that the command wasn’t available. I realized, after fiddling around for a while that I didn’t have bash setup, and I had tried to run the standard quick install… just go to the blog entry. 😛 You can see all the bash & snippets there, they however won’t display here well at all.
---

I went to reinstall RVM (Ruby Version Manager) and got a message that the command wasn’t available. I realized, after fiddling around for a while that I didn’t have bash setup, and I had tried to run the [standard quick install](http://beginrescueend.com/) of:

```bash
bash <
```

…I had not setup bash shell as my shell on this Mac?! Oops. So since I’m a virtual noob sometimes, and I have no idea how to setup bash, I did some searching and came up with this solution.

First, [switch to bash](http://macdevcenter.com/pub/a/mac/2004/02/24/bash.html).

```bash
chsh -s bash
```

Then create yourself a .bash\_profile so that you’ll be able to initiate variables and such that you’ll need in the shell. These are used when working with Ruby, Rails, and a whole host of other things. To create a .bash\_profile you can follow these commands.  (Snagged from this [find](http://redfinsolutions.com/blog/creating-bashprofile-your-mac))

```bash
cd ~/
touch .bash_profile
open -e .bash_profile
```

Then add this to the bash file.

```bash
# place in ~/.bash_profile as the very last line
[[ -s "$HOME/.rvm/scripts/rvm" ]] && . "$HOME/.rvm/scripts/rvm"
```

Now run the install (usually you’re told to setup this bash file afterwards, but figured we might as well get it done).

```bash
bash <
```

Next exit (or whatever your restart of bash technique is) and open your bash terminal back up. Type this command to be sure we’re on the right path.

```bash
type rvm | head -n1
```

Now to install the latest Ruby on Rails bits you can issue a command like this.

```bash
rvm install 1.8.7
```

However, OS-X already comes with 1.8.7, so you’d probably want to install 1.9.2. I issued the 1.8.7 install since I knew, previously, I’d dorked up the install a few days ago. So it is also a good way to make sure your install is cleaned up. I’m sure though, it could possibly mess things up if you’ve tweaked things the wrong way – but it sure seems to be the case that Ruby, Rails + RVM just works. 🙂

```bash
rvm install 1.9.2
```

Once those are installed you’ll want to set one as default. I’m went with 1.9.2 for now. This can be changed later if need be.

```bash
rvm use 1.9.2 --default
```

Anyway, that’ll get you started on OS-X if you’ve run into the “I’m only running the Terminal in its default setup, I need some bash” situation. 🙂

Happy coding, hacking, and gem installing!

> **References:**
>
> Some references are included above as links, but these below didn’t fit exactly in context at any point, I however used them none the less.
>
> - [Installing and Using RVM on Mac OS-X Creating Gemsets and Reverting to Original Environment](http://seanbehan.com/mac-os-x/installing-and-using-rvm-on-mac-os-x-creating-gemsets-and-reverting-to-original-environment/)
