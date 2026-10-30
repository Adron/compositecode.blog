---
title: Ruby 1.9.3, Iron Foundry + Cloud Foundry and++
date: 2012-07-03 08:42:34 -0700
last_modified_at: 2012-07-03 08:48:49 -0700
permalink: /2012/07/03/ruby-1-9-3-iron-foundry-cloud-foundry-and/
slug: ruby-1-9-3-iron-foundry-cloud-foundry-and
wp_id: 5899
original_url: https://compositecode.blog/2012/07/03/ruby-1-9-3-iron-foundry-cloud-foundry-and/
categories:
- How-to
- Iron Foundry
- Platform (as a Service)
- Ruby on Rails Bits
tags:
- cloud foundry
- cloudfoundry
- iron foundry
- ironfoundry
excerpt: Installing the Latest Ruby, A Gotcha Generally, you’d just install rvm (Ruby Version Manager) and execute this command. rvm install 1.9.3 But alas, as happens sometimes, I ran into an issue related to the C compiler being found. Checking the log file for errors I found the message and went searching, finding …
---

## Installing the Latest Ruby, A Gotcha

Generally, you’d just install rvm (Ruby Version Manager) and execute this command.

```bash
rvm install 1.9.3
```

But alas, as happens sometimes, I ran into an [issue related to the C compiler being found](http://stackoverflow.com/questions/6848035/mac-os-x-lion-xcode-problems-using-rvm). Checking the log file for errors I found the message and went searching, finding an immediate solution thanks to good ole’ [Stack Overflow](http://stackoverflow.com). Simply executing the install with a specific C compiler will get things running smoothly.

```bash
rvm install 1.9.3 --with-gcc=clang
```

## Installing the Latest Ruby on Windows

This part is pretty stupidly simple. Just [download the installer](http://rubyinstaller.org/downloads/) and execute it. Once you’ve done this you’ve got all the gem bits and ruby bits you need to get the CLI for Cloud Foundry w/ the Iron Foundry .NET Additions!

## Installing the vmc-ironfoundry CLI App

Why am I installing Ruby 1.9.3 besides the obvious fact that it is Ruby, and awesome, and inherently great for getting shit done? I need the latest bits in order to install the latest Iron Foundry vmc client! You may ask, what’s wrong with the vmc client that Cloud Foundry has made? Well, the .NET bits aren’t included to appropriately identify when you have a .NET application. Basically, the vmc client is the exact same one that the core Cloud Foundry team puts together, but with the additions to know that there are Iron Foundry DEAs that can launch and run .NET Web Applications. To install this, execute the following command on OS-X.

```bash
gem install vmc-IronFoundry
```

If you ever run into the

> “Could not find a valid gem ‘vmc-ironfoundry’ (>= 0) in any repository”

a quick call to update will usually resolve the issue. You may need to run this command with sudo, to insure you have access to the gems directory.

```bash
sudo gem update --system
```

## Summary

At this point you can deploy a ton of languages and frameworks in addition to having .NET & SQL Server Support. I’ll be following up this with a how-to on deploying an ASP.NET 4.0 MVC Application, Node.js, and Ruby on Rails Application, scaling them to multiple instances, and best practices around that in the next month or three. In addition to that, I’ll have some great material coming up regarding some practices around getting these frameworks to work well together against data sources, across end points, via services and more.
