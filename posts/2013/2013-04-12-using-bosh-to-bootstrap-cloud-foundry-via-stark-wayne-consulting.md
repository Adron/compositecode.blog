---
title: Using Bosh to Bootstrap Cloud Foundry via Stark & Wayne Consulting
date: 2013-04-12 21:26:54 -0700
last_modified_at: 2013-06-12 19:57:45 -0700
permalink: /2013/04/12/using-bosh-to-bootstrap-cloud-foundry-via-stark-wayne-consulting/
slug: using-bosh-to-bootstrap-cloud-foundry-via-stark-wayne-consulting
wp_id: 8122
original_url: https://compositecode.blog/2013/04/12/using-bosh-to-bootstrap-cloud-foundry-via-stark-wayne-consulting/
categories:
- AWS
- Cloud Foundry
- How-to
tags:
- amazon web services
- aws
- bosh
- cloud
- cloud computing
- cloud deployment
- could foundry
- dr nic
- open stack
- openstack
- software
- technology
excerpt: I finally sat down and really started to take a stab at Cloud Foundry Bosh. Here’s the quick lowdown on installing the necessary bits and getting an initial environment built. Big thanks out to Dr Nic @drnic, Luke Bakken & Brain McClain @brianmmcclain for initial pointers to where the good content is. With their guidance …
---

I finally sat down and really started to take a stab at [Cloud Foundry Bosh](https://github.com/cloudfoundry/bosh). Here’s the quick lowdown on installing the necessary bits and getting an initial environment built. Big thanks out to Dr Nic **[@drnic](http://twitter.com/drnic)**, Luke Bakken & Brain McClain **[@brianmmcclain](http://twitter.com/brianmmcclain)** for initial pointers to where the good content is. With their guidance and help I’ve put together this how-to. Enjoy…  boshing.

![](/images/adronhall.smugmug.com/Software/Software-Development/Bosh-Bits/i-wGprTdd/0/S/tumblr_l1iotoYo541qbn8c7-S.jpg)**Prerequisites**

**Step: Get an instance/machine up and running.**

To make sure I had a totally clean starting point I started out with an AWS EC2 Instance to work from. I chose a micro instance loaded with Ubuntu. You can use your local workstation if you want to or whatever, it really doesn’t matter. The one catch, of course is you’ll have to have a supported \*nix based operating system.

**Step: Get things updated for Ubuntu.**

```bash
sudo apt-get update
```

**Step: Get cURL to make life easy.**

```bash
sudo apt-get install curl
```

**Step: Get Ruby, in a proper way.**

```bash
\curl -L https://get.rvm.io | bash -s stable
source ~/.rvm/scripts/rvm
rvm autolibs enable
rvm requirements
```

![](/images/adronhall.smugmug.com/Software/Software-Development/Bosh-Bits/i-6pQVLrj/0/S/bruce-wayne-the-dark-knight-2022974-1024-682-S.jpg)Enabling autolibs sets up so that rvm will install all the requirements with the ‘rvm requirements’ command. It used to just show you what you needed, then you’d have to go through and install them. This requirements phase includes some specifics, such as git, gcc, sqlite, and other tools needed to build, execute and work with Ruby via rvm. Really helpful things overall, which will come in handy later when using this instance for whatever purposes.

Finish up the Ruby install and set it as our default ruby to use.

```bash
rvm install 1.9.3
rvm use 1.9.3 --default
rvm rubygems current
```

**Step: Get bosh-bootstrap.**

bosh-bootstrap is the easiest way to get started with a sample bosh deployment. For more information check out [Dr Nic’s Stark and Wayne repo on Github](https://github.com/StarkAndWayne/bosh-bootstrap). (also check out [the Cloud Foundry Bosh repo](https://github.com/StarkAndWayne/bosh-cloudfoundry).)

```bash
gem install bosh-bootstrap
gem update --system
```

Git was installed a little earlier in the process, so now set the default user name and email so that when we use bosh it will know what to use for cloning repositories it uses.

```bash
git config --global user.name "Adron Hall"
git config --global user.email plzdont@spamme.bro
```

**Step: Launch a bosh deploy with the bootstrap.**

```bash
bosh-bootstrap deploy
```

You’ll receive a prompt, and here’s what to hit to get a good first deploy.

Stage 1: I select AWS, simply as I’ve no OpenStack environment. One day maybe I can try out the other option. Until then I went with the tried and true AWS. Here you’ll need to enter your access & secret key from the AWS security settings for your AWS account.

For the region, I selected #7, which is west 2. That translates to the data center in Oregon. Why did I select Oregon? Because I live in Portland and that data center is about 50 miles away. Otherwise it doesn’t matter which region you select, any region can spool up almost any type of bosh environment.

Stage 2: In this stage, select default by hitting enter. This will choose the default bosh settings. The default uses a medium instance to spool up a good default Cloud Foundry environment. It also sets up a security group specifically for Cloud Foundry.

Stage 3: At this point you’ll be prompted to select what to do, choose to create an inception virtual machine. After a while, sometimes a few minutes, sometimes an hour or two – depending on internal and external connections – you should receive the “Stage 6: Setup bosh” results.

> Stage 6: Setup bosh
>
> setup bosh user
> uploading /tmp/remote\_script\_setup\_bosh\_user to Inception VM
> Initially targeting micro-bosh…
> Target set to `microbosh-aws-us-west-2′
> Creating initial user adron…
> Logged in as `admin’
> User `adron’ has been created
> Login as adron…
> Logged in as `adron’
> Successfully setup bosh user
> cleanup permissions
> uploading /tmp/remote\_script\_cleanup\_permissions to Inception VM
> Successfully cleanup permissions
> Locally targeting and login to new BOSH…
> bosh -u adron -p cheesewhiz target 54.214.0.15
> Target set to `microbosh-aws-us-west-2′
> bosh login adron cheesewhiz
> Logged in as `adron’
> Confirming: You are now targeting and logged in to your BOSH
>
> ubuntu@ip-yz-xyz-xx-yy:~$

If you look in your AWS Console you should also see a box with a key pair named “inception” and one that is under the “microbosh-aws-us-west-2” name. The inception instance is a m1.small while the microbosh instance is an m1.medium.

That should get you going with bosh. In my next entry around bosh I’ll dive into some of Dr Nic & Brian McClain’s work before diving into what exactly Bosh actually is. As one may expect, from Stark & Wayne we can expect some pretty cool stuff, so keep an eye over there on [Stark & Wayne](http://starkandwayne.com/).
