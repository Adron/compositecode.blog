---
title: Getting Started with Swift, For NON-Apple Devs
date: 2014-06-23 11:08:21 -0700
last_modified_at: 2014-06-23 10:45:26 -0700
permalink: /2014/06/23/getting-started-with-swift-for-non-apple-devs/
slug: getting-started-with-swift-for-non-apple-devs
wp_id: 10024
original_url: https://compositecode.blog/2014/06/23/getting-started-with-swift-for-non-apple-devs/
categories:
- Apple Programming
- How-to
- Swift
tags:
- apple
- beta
- c#
- ios
- ios 8
- os-x
- os-x yosemite
- preview
- swift
- xamarin
- yosemite
excerpt: This past weekend I attempted to get started with Swift coding. Since I have not been an Apple Developer for a while, it wasn’t immediately obvious how to get started. But once I fumbled around a few minutes I realized I needed a developer account to get the latest XCode. Jeez, it really shows how …
---

[![](https://photos.adron.me/Software/Software-Development/Swift/i-39PcN77/0/O/swift-hero.png)](https://developer.apple.com/swift/)This past weekend I attempted to get started with Swift coding. Since I have not been an Apple Developer for a while, it wasn’t immediately obvious how to get started. But once I fumbled around a few minutes I realized I needed a developer account to get the latest XCode. Jeez, it really shows how much Apple loves to lock you in hard core to their development ecosystem. An unfortunate trait of a company that is actually extremely closed in much of its behavior, while taking advantage of so much of the open source community. But I digress, this isn’t a rant about the unethical behavior of Apple. I’ll reserve that for the novels worth of material it deserves.

One I signed up for the developer program, which costs $99 bucks, I immediately made my first huge mistake. This damnable mistake blew the entire weekend of hacking. I added under “Company” my simple DBA (Doing Business As) name. I already had an account, and because of this change for making this existing account become a developer account from a personal base level account, sprung a red flag. I checked back frequently over the weekend, but it wasn’t until Monday that somebody checked the app, realized the Company name I added was merely a DBA and ok’d my account. So far, 38 hours down the drain for getting started hacking on Swift! Dammit.

However, this morning I was happy to find everything was ok’d, and thus, the remaining bit of this blog entry is a bit more example and a little less story of my day.

[![Developer @ Apple](https://photos.adron.me/Software/Software-Development/Swift/i-cD6nt8R/0/L/Get_started_with_your_Safari_Developer_Program_-_Apple_Developer-L.png)](https://photos.adron.me/Software/Software-Development/Swift/i-cD6nt8R/0/O/Get_started_with_your_Safari_Developer_Program_-_Apple_Developer.png)

*Developer @ Apple*

## Getting XCode 6 beta

I wanted to do Swift hacking, the first step was to download XCode 6 beta. That’s available via download on the [iOS Developer page](https://developer.apple.com/devcenter/ios/index.action) (and I suppose the Mac Developer page). Scroll down on that page until you find the XCode Download button.

[![The Warnings and the Download XCode 6 beta page.](https://photos.adron.me/Software/Software-Development/Swift/i-7zLf2MN/0/L/iOS_Dev_Center_-_Apple_Developer2-L.png)](https://photos.adron.me/Software/Software-Development/Swift/i-7zLf2MN/0/O/iOS_Dev_Center_-_Apple_Developer2.png)

*The Warnings and the Download XCode 6 beta page.*

Also note, if you’re looking to do Swift hacking like I’m doing here, I’d actually advise against getting the iOS 8 beta or OS-X Yosemite Developer Previews right now. Best to keep as stable a machine while toying around with a new language. At least, that’s what the conversations have been so far…

[![OS-X Yosemite & iOS 8](https://photos.adron.me/Software/Software-Development/Swift/i-NNsdWTF/0/M/iOS_Dev_Center_-_Apple_Developer3-M.png)](https://photos.adron.me/Software/Software-Development/Swift/i-NNsdWTF/0/O/iOS_Dev_Center_-_Apple_Developer3.png)

*OS-X Yosemite & iOS 8*

Once I got Xcode 6 beta installed I dove right into creating a Swift Project. I created a simple new project that is empty to just check out what Xcode 6 provides out of box for the Swift Project.

[![Selecting an empty Xcode 6 beta project to use with Swift.](https://photos.adron.me/Software/Software-Development/Swift/i-xDbZbj2/0/L/swift1-L.png)](https://photos.adron.me/Software/Software-Development/Swift/i-xDbZbj2/0/O/swift1.png)

*Selecting an empty Xcode 6 beta project to use with Swift.*

The next dialog is where the Swift magic is selected.

[![Selecting Swift, entering a project name and other information dialog.](https://photos.adron.me/Software/Software-Development/Swift/i-G38PVhc/0/L/swift2-L.png)](https://photos.adron.me/Software/Software-Development/Swift/i-G38PVhc/0/O/swift2.png)

*Selecting Swift, entering a project name and other information dialog.*

After that I just clicked through on defaults until I got into the Xcode IDE with the project open.

[![Selecting the appropriate simulator.](https://photos.adron.me/Software/Software-Development/Swift/i-wwf5HMS/0/L/swift5-L.png)](https://photos.adron.me/Software/Software-Development/Swift/i-wwf5HMS/0/O/swift5.png)

*Selecting the appropriate simulator.*

Next I executed the project. Since I’d had my phone attached it wanted to run it there, but I have 7.1 iOS on it which won’t execute Swift code. I had to select the appropriate simulator then to run the application project. Once that ran, since I’d not done so on this particular computer, I needed to enable developer mode.

[![Enabling developer mode.](https://photos.adron.me/Software/Software-Development/Swift/i-vHMvkG8/0/L/swift4-L.png)](https://photos.adron.me/Software/Software-Development/Swift/i-vHMvkG8/0/O/swift4.png)

*Enabling developer mode.*

I did so and the empty application launched.

[![An empty iOS 8 iPad Retina Application.](https://photos.adron.me/Software/Software-Development/Swift/i-qjBq3zM/0/L/swift6-L.png)](https://photos.adron.me/Software/Software-Development/Swift/i-qjBq3zM/0/O/swift6.png)

*An empty iOS 8 iPad Retina Application.*

So that’s the basic getting started, no code actually slung. But rest assured I’ll have another post soon detailing some first code snippets. I also hope to get some comparisons written up between XCode with Swift and Xamarin Studio and C#. It’s cool that Apple finally has a modern feature rich language, so it’ll be interesting to see how each stacks up from a language and IDE perspective.

**References:**

- [Swift Docs](https://developer.apple.com/library/prerelease/ios/documentation/swift/conceptual/swift_programming_language/index.html)
- [Introducing Swift](https://developer.apple.com/swift/)
- [Apple Developer Site](https://developer.apple.com)
- [Swift Book on iBooks](https://itunes.apple.com/us/book/the-swift-programming-language/id881256329?mt=11)
