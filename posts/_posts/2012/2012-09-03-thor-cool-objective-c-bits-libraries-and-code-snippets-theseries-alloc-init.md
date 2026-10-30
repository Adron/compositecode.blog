---
title: Thor – Cool Objective-C Bits, Libraries and Code Snippets [[TheSeries alloc] init];
date: 2012-09-03 11:26:52 -0700
last_modified_at: 2012-09-04 01:05:59 -0700
permalink: /2012/09/03/thor-cool-objective-c-bits-libraries-and-code-snippets-theseries-alloc-init/
slug: thor-cool-objective-c-bits-libraries-and-code-snippets-theseries-alloc-init
wp_id: 6417
original_url: https://compositecode.blog/2012/09/03/thor-cool-objective-c-bits-libraries-and-code-snippets-theseries-alloc-init/
categories:
- Apple Programming
- Iron Foundry
- Thor Project
tags:
- cocoa
- objective-c
- reactive extensions
- thor
- thorproject
excerpt: Benjamin Van Der Veen (@bvanderveen) has been working with me to build out the Thor Application based on Nathan Young’s (@nathanyoung) awesome designs. We’ll be releasing open source real soon. I wanted to cover some of the cool libraries, specific code snippets and such. These are a few of the things that have come in …
---

[Benjamin Van Der Veen](http://bvanderveen.com/) ([@bvanderveen](http://twitter.com/bvanderveen)) has been working with me to build out the [Thor Application](http://www.ironfoundry.org/thor)  based on Nathan Young’s ([@nathanyoung](https://twitter.com/nathanyoung)) [awesome designs](http://cargocollective.com/nathanyoung). We’ll be releasing open source real soon. I wanted to cover some of the cool libraries, specific code snippets and such. These are a few of the things that have come in very useful as the coding deluge began.

## Reactive Cocoa (AKA Reactive Extensions)

When you need to compose and transform sequences of values (kind of like Reactive Extensions for .NET) this is your library when working in Objective-C land. [Reactive Cocoa](https://github.com/github/ReactiveCocoa) or “RAC” for short can observe on key values to provide a key value for compliant properties. RAC helps to keep mutability under wraps (which is really really needed in Objective-C), pulls together behaviors and relationships between properties, and helps tremendously with asynchronous actions. The last bit we have a good amount of occurring with Thor since it talks to the Cloud Foundry web service API end points.

An example I snagged from the github site is below. It watches for changes on the username property.

```objc
[RACAbleSelf(self.username) subscribeNext:^(NSString *newName) {
    NSLog(@"%@", newName);
}];
```

Which serves, as pointed out in the README.md (be sure to read it if you’re going to use the library), as a wrapper around KVO. It goes on to show further sequences on complex actions.

```objc
[[[[RACAbleSelf(self.username)
    distinctUntilChanged]
    take:3]
    where:^(NSString *newUsername) {
        return [newUsername isEqualToString:@"joshaber"];
    }]
    subscribeNext:^(id _) {
        NSLog(@"Hi me!");
    }];
```

For some that write C# all the time this might seem like a “meh” moment. But considering the work that would be needed in Objective-C usually this could take significantly more lines of code, such as setting an observer, using a property or something to watch the value, monitor the non-distinct changes, and then bounce the value of the property for every non-distinct value. Yeah, and it still isn’t done. But anyway, that’s just the icing, the cake is delicious. If you’re in Objective-C land much, it is worth checking out.

[Check it out on Github](https://github.com/github/ReactiveCocoa).
