---
title: 'The #TypeScript Bomb Went off With a BANG Today!'
date: 2012-10-01 18:02:24 -0700
last_modified_at: 2012-10-02 15:05:39 -0700
permalink: /2012/10/01/the-typescript-bomb-went-off-with-a-bang-today/
slug: the-typescript-bomb-went-off-with-a-bang-today
wp_id: 6679
original_url: https://compositecode.blog/2012/10/01/the-typescript-bomb-went-off-with-a-bang-today/
categories:
- How-to
- Javascript
- Reviews
tags:
- javascript
- typescript
excerpt: 'First thing in the morning today the east coast was talking about Mary Jo Foley’s article about the TypeScript release. Later in the day Matt Baxter-Reynolds (@mbrit) released a bit of write up titled “Microsoft TypeScript: Can the father of C# save us from the tyranny of JavaScript?“. My first reactions went something like this: TypeScript sounds …'
---

First thing in the morning today the east coast was talking about [Mary Jo Foley’s article about the TypeScript release](http://www.zdnet.com/microsoft-takes-the-wraps-off-typescript-a-superset-of-javascript-7000004993/). Later in the day Matt Baxter-Reynolds ([@mbrit](https://twitter.com/mbrit)) released a bit of write up titled “[Microsoft TypeScript: Can the father of C# save us from the tyranny of JavaScript?](http://www.zdnet.com/microsoft-typescript-can-the-father-of-c-save-us-from-the-tyranny-of-javascript-7000005054/)“. My first reactions went something like this:

> 1. TypeScript sounds interesting. Anders is on it, so that’s a big plus. It’s a “superset” & “syntactic sugar” which is also interesting.
> 2. TypeScript is a lousy name. I wish MS could find people to name things with something entertaining. It just seems disconnected.

After a little bit more review and an explosion on twitter I came to a few other conclusions.

- The whole large applications notion just doesn’t cut it for me. Writing big applications well is about a good team, not about your language taking up the slack of a bad team.
- I get that this makes things easier in Visual Studio and other IDEs to do certain “easy button” and F5 type development for coders that use those tools. There’s big plusses and really big negatives to this.
- If you check out the site <http://www.typescriptlang.org/> you’ll see open source with the [code available](http://typescript.codeplex.com/SourceControl/changeset/view/d397c54a55db). I’m stoked to see that Microsoft isn’t just playing lip service to this. They’re walking the walk these days, there’s even a [pull requests section](http://typescript.codeplex.com/sourcecontrol/list/contributions) albeit no requests yet, and it is indeed using Git.  Just (**git clone https://git01.codeplex.com/typescript)**
- A huge cool factor too, are the tons of [plugins available already](http://blogs.msdn.com/b/interoperability/archive/2012/10/01/sublime-text-vi-emacs-typescript-enabled.aspx).
  - [Sublime 2](http://blogs.msdn.com/b/interoperability/archive/2012/10/01/sublime-text-vi-emacs-typescript-enabled.aspx) [[download](http://www.interoperabilitybridges.com/media/155452/typescript_support_for_sublime_text.zip)] (which I hear from my buddy Jerry Sievert ([@jerrysievert](https://twitter.com/jerrysievert)) will work with TextMate)
  - [Emacs](http://blogs.msdn.com/b/interoperability/archive/2012/10/01/sublime-text-vi-emacs-typescript-enabled.aspx) [[download](http://www.interoperabilitybridges.com/media/155449/typescript_support_for_emacs.zip)]
  - [Vi](http://blogs.msdn.com/b/interoperability/archive/2012/10/01/sublime-text-vi-emacs-typescript-enabled.aspx) [[download](http://www.interoperabilitybridges.com/media/155446/typescript_support_for_vim.zip)]
  - [Visual Studio](http://www.microsoft.com/en-us/download/details.aspx?id=34790) [[download](http://www.microsoft.com/en-us/download/details.aspx?id=34790)]
- There’s a [tutorial](http://www.typescriptlang.org/tutorial/), which I plundered through real quick at lunch amid the plethora of pictures I took. Working through this tutorial I found the thing I’m happiest about, more so than the plugins, is that there is indeed an npm package (**npm install -g typescript**). Remember when installing, you’ll probably need to do a sudo.
- The [TypeScript Playground](http://www.typescriptlang.org/Playground/) is a cool feature. Kind of like jsbin, except for toying around with TypeScript. However change the following snippet of code:

```javascript
class Greeter {
	greeting: string;
	constructor (message: string) {
		this.greeting = message;
	}
	greet() {
		return "Hello, " + this.greeting;
	}
}

var greeter = new Greeter("world");

var button = document.createElement('button')
button.innerText = "Say Hello"
button.onclick = function() {
    alert(greeter.greet())
}

document.body.appendChild(button)
```

…and change the instantiation of…

```javascript
var greeter = new Greeter("world", 123);
```

…or change it to…

```javascript
var greeter = new Greeter("world", "WTF");
```

…and then think about it for a second. I thought the point was to do strong typing, but it seems that isn’t strong typing the bits in the parameter list of the object instantiation. Beyond little nuances like that, I’m generally ok with the enhancements they’ve added with TypeScript. Not sure people that know how to write JavaScript really need to have this. It seems there is a strong case that this is created to make it easier for C# (and by proxy Java) coders to grok and write JavaScript code. That’s fine by me too. The sooner people can stop whining about how horrible the language is (which I also will admit I’m totally fine with the language, just learn it, it isn’t hard).

## Summary

In the end, I’m fine with TypeScript. I think Anders & team have put this together in a responsible, positive way and inclusive of prospective community feedback and interaction. After so many years of the opposite, I’m still always impressed when things are done in good faith with the community. Do I think they need to work on how they put these efforts together? Yes. Do I think the approach of bombing the community with this new thing with a whole pre-built MS community around it pre-existing? Yes. But I digress, overall all looks good, and nothing truly negative about it (unless one is personally perturbed). So I’d suggest to try it out, it can definitely make things easier in a number of ways. I might even have some examples cropped up over the next few days.
