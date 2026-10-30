---
title: The Method I Use Setting Up a Dev Machine for Node.js
date: 2018-07-16 09:08:46 -0700
last_modified_at: 2024-11-18 21:43:20 -0800
permalink: /2018/07/16/setting-up-a-dev-machine-for-node-js/
slug: setting-up-a-dev-machine-for-node-js
wp_id: 14396
original_url: https://compositecode.blog/2018/07/16/setting-up-a-dev-machine-for-node-js/
categories:
- Javascript
- Node.js Things
- nodejs
tags:
- javascript
- node
- node.js
- nodejs
excerpt: 'UPDATED: April 4th, 2019, March 17th, 2022, and again on November 18th, 2024. It seems every few months setup of whatever tech stack is always tweaked a bit. This is a collection of information I used to setup my box recently. First off, for the development box I always use nvm as it is routine …'
image: /wp-content/uploads/2018/07/1200px-node-js_logo.png
---

###### *UPDATED: April 4th, 2019, March 17th, 2022*, and again on November 18th, 2024.

It seems every few months setup of whatever tech stack is always tweaked a bit. This is a collection of information I used to setup my box recently. First off, for the development box I always use nvm as it is routine to need a different version of Node.js installed for various repositories and such. The best article I’ve found that is super up to date for Ubuntu 18.04 is Digital Ocean’s [article](https://www.digitalocean.com/community/tutorials/how-to-install-node-js-on-ubuntu-18-04) (kind of typical for them to have the best article, as their blog is exceptionally good). In it the specific installation of nvm I’ve noticed has changed since I last worked with it some many months ago.

First curl download the installation script. I trust the script so I just install it from the repo! (*Albeit I HAVE read it multiple times*, remember, don’t just run scripts from random repos!)

curl -o- <https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.1/install.sh> | bash

UPDATE November 18, 2024 – `curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.1/install.sh | bash` to get the latest installed.

Now that I’ve gotten the script and run it, I can then `source ~/.profile` and nvm is now available. Check out the versions available for installation with `nvm ls-remote`. Next up, install a particular version, or a few, as in my case I’ll need a couple.

nvm install 6
nvm install 8.11.3
nvm install 10.15.3
nvm install node

![installing-nodejs](/wp-content/uploads/2018/07/installing-nodejs.png)

After this I ran a `nvm ls` command to see what was installed altogether. Note for my installation of version 6, with the `nvm install 6` command it chose version 6.14.3 as it will choose latest for any major release version specified.

Beyond the version manager installed version there’s also the package manager on Debian/Ubuntu that can be used, but requires a few additional steps but is good if the installation will be used to host a specific Node.js application at a particular version. More details on that installation method can be found [here](https://nodejs.org/en/download/package-manager/#debian-and-ubuntu-based-linux-distributions).

Next up I finalized my installation. After getting a list of the latest versions with `nvm ls-remote` I chose 10.15.3 with the `nvm use 10.15.3` command. For a list of the local versions of Node.js I can now use `nvm ls` and check the current version in use with `node -v`.

For the latest updates check out the repository for NVM [here](https://github.com/nvm-sh/nvm#installing-and-updating).
