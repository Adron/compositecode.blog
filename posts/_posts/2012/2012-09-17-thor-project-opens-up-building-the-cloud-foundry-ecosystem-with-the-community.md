---
title: Thor Project Opens Up, Building the Cloud Foundry Ecosystem with the Community
date: 2012-09-17 06:15:15 -0700
last_modified_at: 2012-09-17 13:43:47 -0700
permalink: /2012/09/17/thor-project-opens-up-building-the-cloud-foundry-ecosystem-with-the-community/
slug: thor-project-opens-up-building-the-cloud-foundry-ecosystem-with-the-community
wp_id: 6258
original_url: https://compositecode.blog/2012/09/17/thor-project-opens-up-building-the-cloud-foundry-ecosystem-with-the-community/
categories:
- .NET Bits
- Apple Programming
- Awesome Coders
- Cloud Foundry
- Coding Adventures
- Iron Foundry
- Javascript
- Metro UI
- Platform (as a Service)
tags:
- .NET
- c#
- cocoa
- csharp
- design
- dotnet
- javascript
- obj-c
- objc
- objective-c
- open source
- open source software
- os-x
- oss
- thor
- thorproject
- ui
- ux
- windows
- windows 7
- windows 8
- winrt
excerpt: The Iron Foundry Team are big advocates of open source software. We write code across all sorts of languages, just like many of the development shops out there do. Sometimes we’re heavy on the .NET, other times we’re all up in some Java, Ruby on Rails, spooling up a Node.js Application or something else. So …
---

The Iron Foundry Team are big advocates of open source software. We write code across all sorts of languages, just like many of the development shops out there do. Sometimes we’re heavy on the .NET, other times we’re all up in some Java, Ruby on Rails, spooling up a Node.js Application or something else. So keeping with our love of open source and our polyglot nature we’ve created the Thor Project with three distinct apps.

![](/images/adronhall.smugmug.com/Software/Software-Development/Thor/i-jwLWNnb/0/S/VMW-LGO-CloudFoundry-217-S.png)Before jumping into the applications though, a little context for what and where Thor is in the grand scheme of things. We need to roll back to the [Cloud Foundry Project](http://www.cloudfoundry.org) to get into that. The Cloud Foundry Project is an open source project built around software for PaaS (Platform as a Service) which can be used to build your own PaaS internally or externally, in a cloud provider or directly on hardware. It’s your choice how, when and where you want to use it. For more context on PaaS check out my previous entry “[The Confusions of IaaS, PaaS and SaaS](/2011/01/04/the-confusions-of-iaas-paas-and-saas/)“.

# Thor Project

## Cocoa for OS-X

[![Thor Odinson](/images/adronhall.smugmug.com/Software/Software-Development/Thor/i-pwbG3VB/0/S/ThorOdinsonEarth-616008-S.jpg "Thor Odinson")](http://www.ironfoundry.org/thor)

*Thor Odinson, God of Thunder*

You know who Thor is right? He’s this mythic Norse God, also known as the God of Thunder. Since [we’re all about bringing the hamma](http://blog.ironfoundry.org/2012/02/have-you-brought-the-hamma/) we welcomed Thor into our team’s stable of applications. So starting immediately we’ve released Thor into the realms for contributions and fighting the good open source software battle! If you’d like to join the effort, check out the github project and feel free to join us!

Technically, what is the Thor Application? This is a Cocoa Application built for OS-X that is used for managing, deploying and publishing applications to Cloud Foundry enabled and or Iron Foundry extended PaaS Environments.

## .NET for Windows 7

The .NET Metro version of the Thor Application is also released via github with a provided installer. We’ve almost taken the same path, except of course for the very different UX and UI queues with Windows 7 and the Metro UX design guidelines.

## WinRT for Windows 8

I wasn’t really sure what to call this version. Is it Metro or WinRT or Windows 8 or something else? Anyway, there is a project, it is albeit empty at this point, but it is the project where the Windows 8 version of Thor will go! For now get the Windows 7 version and install it on Windows 8, it won’t have touch interface support and things, but should work just like a regular application on Windows 8.

# The Code

- [**Thor OS-X (Cocoa)**](http://bit.ly/UfGdXC)
- [**Thor .NET**](http://bit.ly/SugiK9)
- [**Thor WinRT**](http://bit.ly/QgjvgU)
- [**Thor Design**](http://bit.ly/U5vfbu) – This is all the design collateral created by [Nathan Young](http://cargocollective.com/nathanyoung) ([@nathanyoung](http://twitter.com/nathanyoung)) for each of the versions.

To get started with these, generally you’d just clone the repo and do a build, then get started checking out the code. There is one catch, for the OS-X version you’ll want to pull down the sub-modules with the following command.

```bash
git clone git@github.com:YourForkHere/Thor.git
git submodule update --init --recursive
```

Once you do that in XCode just make sure to then select the right project as the starting build project.

![](/images/adronhall.smugmug.com/Software/Software-Development/Thor/i-7nBDLbh/0/S/002-running-xcode-thor-S.png)

…then when the application is launched…

[![Thor Running in OS-X](/images/adronhall.smugmug.com/Software/Software-Development/Thor/i-4zj2p3n/1/L/004-Thor-Running-L.jpg "Thor Running in OS-X")](http://ironfoundry.org/Thor)

*Thor Running in OS-X*

I’ll have more in the coming days and weeks about Thor & Iron Foundry. For now, check out the [blog entry on the Iron Foundry Blog](http://blog.ironfoundry.org/2012/09/alpha-for-thor-download-try-get-involved/) and subscribe there for more information.
