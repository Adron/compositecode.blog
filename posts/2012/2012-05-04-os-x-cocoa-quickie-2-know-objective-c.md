---
title: 'OS-X Cocoa Quickie #2 => Know Objective-C'
date: 2012-05-04 23:23:34 -0700
last_modified_at: 2012-07-22 15:10:37 -0700
permalink: /2012/05/04/os-x-cocoa-quickie-2-know-objective-c/
slug: os-x-cocoa-quickie-2-know-objective-c
wp_id: 5501
original_url: https://compositecode.blog/2012/05/04/os-x-cocoa-quickie-2-know-objective-c/
categories:
- How-to
tags: []
excerpt: When working with Objective-C one key thing to keep in mind is the differences between the other “C”s like C, C++, etc. One thing that crops up sometimes is the C char type. Normally, this isn’t the most ideal thing to use. The better type to use is NSString. // c string char …
---

When working with Objective-C one key thing to keep in mind is the differences between the other “C”s like C, C++, etc. One thing that crops up sometimes is the C char type. Normally, this isn’t the most ideal thing to use. The better type to use is NSString.

```objc
// c string
char *foo;
foo = "This is a c string.";

// NSString
NSString *bar;
bar = @"This is an NSString.";
```

The way to straighten this out is to give a little conversion if you do run into some C char types.

```objc
const char *footoo = "blah blah";
// Convert the NSString from a c string.
NSString *foobar;
foobar = [NSString stringWithUTF8String:footoo];

// Convert the c string to an NSString.
footoo = [foobar UTF8String];
```

One of the other things that is a little catchy is the isEqual method.

The result of this test is yes if the receiver and anObject are equal and no otherwise. Basically, both pointers must be to the same memory locations. This however is not always equal, which can cause a bit of confusion.

There are a host of other things to keep an eye out for. So be sure to check out the specifics of how Objective-C works versus the other “C”s.
