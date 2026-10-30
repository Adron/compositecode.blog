---
title: 'JavaScript Libraries Spilled EVERYWHERE! Series #002'
date: 2012-10-20 12:29:10 -0700
last_modified_at: 2012-10-21 22:54:37 -0700
permalink: /2012/10/20/javascript-libraries-spilled-everywhere-series-002/
slug: javascript-libraries-spilled-everywhere-series-002
wp_id: 6829
original_url: https://compositecode.blog/2012/10/20/javascript-libraries-spilled-everywhere-series-002/
categories:
- How-to
- Javascript
- Node.js Things
tags:
- bdd
- behavior de
- javascript
- js
- node
- node.js
- nodejs
- tdd
excerpt: In the last blog entry I wrote up vows.js for testing JavaScript, in this I’ve tried out another testing framework called mocha. This framework is pretty extensive as you can do the things you do with vows.js as well as a lot of other techniques. In addition to mocha I’ve added a few other things …
---

![](/images/adronhall.smugmug.com/Software/Misc-Images/Bad-Resume/i-s2d7HmT/0/S/javascript-S.png)In the last [blog entry I wrote up vows.js for testing JavaScript](/2012/10/14/js-libs-everywhere-001/), in this I’ve tried out another testing framework called [mocha](http://visionmedia.github.com/mocha/). This framework is pretty extensive as you can do the things you do with vows.js as well as a lot of other techniques. In addition to [mocha](http://visionmedia.github.com/mocha/) I’ve added a few other things to the mix. As well as a few obvious points where I need to RTFM still about how mocha works.

## mocha.js

Before falling off into a conversation about reading the manual, I’ll dive into a bit about [mocha](http://visionmedia.github.com/mocha/). Mocha is a project, [hosted on github](https://github.com/visionmedia/mocha) as you might expect, that aims to provide a very feature rich test framework that can run via node or the browser. It also enables asynchronous and synchronous testing with some pretty sweet reporting.

The installation is the standard simplicity of a beautiful and elegant package from npm for node.js.

```bash
$ npm install -g mocha
```

Of course, depending on the way you’ve setup your machine, you may need to hit that command with sudo. The sample test on the main documentation & project page is pretty straight forward, I’ve copied it below for easy reference.

```bash
$ npm install -g mocha
$ mkdir test
$ $EDITOR test/test.js
```

Note that above, where “$EDITOR” is whatever editor you’re using, such as Sublime 2, Textmate, Webstorm or whatever.

```javascript
var assert = require("assert")
describe('Array', function(){
  describe('#indexOf()', function(){
    it('should return -1 when the value is not present', function(){
      assert.equal(-1, [1,2,3].indexOf(5));
      assert.equal(-1, [1,2,3].indexOf(0));
    })
  })
})
```

Then run the test.

```bash
$  mocha

  .

  ✔ 1 test complete (1ms)
```

Overall, pretty sweet and simple. There are ways to setup mocha to do TDD or BDD style also. What I’ve done for my basic name generator I’m building has started of super simple. One of the other additions that I’ve added below is the [should.js](https://github.com/visionmedia/should.js/) library. I’ll add more about this library, and the intent behind using it in the next blog article I write up.

My first tests I’ve put together I’ve entered below.

```javascript
require('should');
var factory = require('./../lib/NameFactory').nameFactory;

describe('when working with names using NameFactory', function(){
  var generateThisManyNames = 3;

  describe('generating names', function(){
    it('should return a name between 3 and 20 characters', function(){
        factory.generate_names().length.should.be.approximately(3,20);
    });
    it('should return correct number of names', function(){
        factory.generate_names(generateThisManyNames).length.should.equal(generateThisManyNames);
    });
  })
});
```

…and then I’ve implemented the absolute basic to get those tests to pass. You JavaScripters that have been at it for a while can likely detect my massive newbism among this code. I’d love feedback btw. 🙂 So here’s my basic implementation so far.

```javascript
module.exports.nameFactory = {
    generate_names: function (count) {
        if (count > 1){
            return [",","];
        }
        else{
            return 'stuff';
        }
    }
};
```

I’m still sketch on best practices around a number of object uses and creation in JavaScript. For instance in my code above, I’m creating a module, and setting up properties with functions, which leads to a number of questions… (maybe it is stack overflow time)

- Is this an efficient way to create a JavaScript function for returning randomly created names?
- What would your first tests be when creating a name generator? Any suggestions on some tests to add?
- This shows some of my intent, such as returning a single result if no count is entered or it is less than 2, any suggestions on doing a kind of overloaded factory pattern method like that?
- Now that I’ve gotten what I do above, I need some more tests to add to confirm that the returned content isn’t [”,”,”] <- cuz’ obviously that’s useless and not random, just returns the 3 string array that would prospectively have generated (or randomly selected) names. Ideas?
- Is there another way to create a class or namespace that isn’t “module.export…” like I have above with “module.exports.nameFactory”? I’d love to just have a “NameFactory” or something. Not sure how or what way would be best in JavaScript land to put something like that together.

I’ve already moved past just this, but would love any feedback on the above questions and code snippets. I’ll post my results and the changes and additions from any body that posts feedback and suggestions in a subsequent post.  🙂

Cheers!
