---
title: Learning “nools” Rules Engine
date: 2014-09-20 16:55:44 -0700
last_modified_at: 2014-12-23 16:21:44 -0800
permalink: /2014/09/20/learning-nools-rules-engine/
slug: learning-nools-rules-engine
wp_id: 10242
original_url: https://compositecode.blog/2014/09/20/learning-nools-rules-engine/
categories:
- How-to
- Javascript
- Node.js Things
- Testing
tags:
- action
- business rules
- business rules engine
- fact
- javascript
- node
- node.js
- nodejs
- nools
- rete
- rete algorithm
- rule
- rules
- rules engine
excerpt: Recently I sat down to work up a solution around a rules engine. There were a few things I noticed right off. When there is a request to implement or build a rules engine it is very often (I’m guessing a solid 40-60% of the time) reasoned that there is a need solely based on …
image: /wp-content/uploads/2014/01/javascript-logo.png
---

Recently I sat down to work up a solution around a rules engine. There were a few things I noticed right off.

1. When there is a request to implement or build a rules engine it is very often (I’m guessing a solid 40-60% of the time) reasoned that there is a need solely based on a lack of understanding around what the problem space is that actually needs a solution. The simple assumption, is 40-60% of the time somebody says “let’s implement a rules engine to solve these unknown problems” really translates to “we really don’t know much about this domain so let’s implement something arbitrary as a stop gap”.
2. Implementing a business rules engine can quickly become a “support the user” scenario for the developers that implement the rules engine. This is a situation in which the developers actually have to help the people writing the rules to be processed. This is not an ideal situation at all, generally developers supporting users writing rules is a quick way to ensure burn out, misappropriation of skills and turnover.
3. Many developers will, without hesitation, spout out “are you sure you want to implement a rules engine?” and then follow that up with “let’s discuss your actual problem” with that leading to “are you sure you want to implement a rules engine?”. Other developers upon hearing that one will implement a rules engine immediately respond with, “shit, I’m out.”

At this point I realized I had X, Y and Z reason to use it and would just have to persevere with all of the threats that are inclusive of implementing a rules engine. Sometimes one just has to step into the realm of scary and get it done.

So here’s what I dug up. I’m really not sure about the name of this project, as it appears to be some sort of [odd usage](https://twitter.com/hashtag/nools), so whatever, but it is indeed called [nools](http://c2fo.github.io/nools/) ([github repo](https://github.com/C2FO/nools)). Nools is a business rules engine based on the [Rete Algorithm](http://en.wikipedia.org/wiki/Rete_algorithm), something that is helpful to read up on when implementing. The main deployment for nools is to a Node.js server, but I’ve read that it is prospectively deployable in most browsers too.

[![The Browsers That Have Known Support, ya know, if you want to use nools in a broswer.](https://photos.adron.me/Software/Software-Development/Nooling/i-Z9xj2Q9/0/O/68747470733a2f2f63692e746573746c696e672e636f6d2f4332464f2f6e6f6f6c732e706e67.png)](https://ci.testling.com/C2FO/nools)

*The Browsers That Have Known Support, ya know, if you want to use nools in a broswer.*

There are a few other things that need definitions. So before moving on here are a few key words.

- **rule** – A collection of constraints that must be satisfied for in order for a action to occur.
- **action** – The code that will execute when a all of a rule’s constraints have been satisfied.
- **fact** – An object/item inserted into a session that the rule’s constraints match against.
- **flow** – This is container for rules that will be executed, you can think of it as a rule book.
- **session** – This is an “instance” of a flow used to match facts. Sessions are obtained from a flow.

## Working With the Examples

The first thing I tried to run was a simple little sample of a nools rule file using the DSL. The nools file I named helloworld.nools and put in a directory called *rules*. The file looked like the example available in the README.md of the nools repo, but I immediately hit a bump.

***The nools Rules***

```javascript
define Message {
    text : ",
        constructor : function(message){
        this.text = message;
    }
}

//find any message that starts with hello
rule Hello {
    when {
        m : Message m.text =~ /^hello(\s*world)?$/;
    }
    then {
        modify(m, function(){this.text += &quot; goodbye&quot;;});
    }
}

//find all messages then end in goodbye
rule Goodbye {
    when {
        m : Message m.text =~ /.*goodbye$/;
    }
    then {
        console.log(m.text);
    }
}
```

I created a server.js file with a simple bit of code just to see the results.

```javascript
var nools = require(&quot;nools&quot;);
var ruleFilePath = __dirname + &quot;rules/helloworld.nools&quot;;
var flow = nools.compile();
var Message = flow.getDefined(&quot;message&quot;);

console.log(&quot;Rules executed @ &quot; + ruleFilePath);
console.log(Message);
```

I tried running this with a simple *node server.js* command. The result, unfortunately was just an error dumped into the bash.

```bash
16:29 $ node server.js

/Users/adron/Codez/testing-nools/node_modules/nools/lib/index.js:61
throw new Error(&quot;Name required when compiling nools source&quot;);
^
Error: Name required when compiling nools source
at Object.exports.compile (/Users/adron/Codez/testing-nools/node_modules/nools/lib/index.js:61:15)
at Object.&amp;amp;amp;lt;anonymous&amp;amp;amp;gt; (/Users/adron/Codez/testing-nools/server.js:3:18)
at Module._compile (module.js:456:26)
at Object.Module._extensions..js (module.js:474:10)
at Module.load (module.js:356:32)
at Function.Module._load (module.js:312:12)
at Function.Module.runMain (module.js:497:10)
at startup (node.js:119:16)
at node.js:906:3
```

Ugh, I suppose some things just don’t work on the first try. Based on that error message I dove into the actual nools code, to line 61 to get some insight into what the error messages actually means. The function the error is actually located in looks like this.

```javascript
exports.compile = function (file, options, cb) {
    if (extd.isFunction(options)) {
        cb = options;
        options = {};
    } else {
        options = options || {};
        cb = null;
    }
    if (extd.isString(file)) {
        options.name = options.name || (isNoolsFile(file) ? path.basename(file, path.extname(file)) : null);
        file = parse(file);
    }
    if (!options.name) {
        throw new Error(&quot;Name required when compiling nools source&quot;);
    }
    return  compile.compile(file, options, cb, FlowContainer);
};
```

Line 61 is the line that reads *throw new Error(“Name required when compiling nools source”);*, which I suppose is a bit obvious. I did a little search on the README.md for the word options, which brought up the way to complie a nools rule and how to name it in the function call. I then looked back at my code and realized I’d not passed in the actual file to the compile function! Doh! I made that minor change of

```javascript
var flow = nools.compile();
```

to this

```javascript
var flow = nools.compile(ruleFilePath);
```

Before running I noticed I’d have one more little path problem and changed this

```javascript
var ruleFilePath = __dirname + &quot;rules/helloworld.nools&quot;;
```

to this

```javascript
var ruleFilePath = __dirname + &quot;/rules/helloworld.nools&quot;;
```

Now when I ran *node server.js* the result displayed as expected.

```bash
22:10 $ node server.js
Rules executed @ /Users/adron/Codez/testing-nools/rules/helloworld.nools
[Function]
```

At this point the individual parts of this code are in need of explanation. But those explanations will be coming in a subsequent blog post. So keep reading, subscribe, and that post will be coming Sunday (that’s tomorrow)*at 8:00am*!
