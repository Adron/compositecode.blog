---
title: Getting in Some Code Stylings, Looking Good for the Code Dance
date: 2014-10-07 09:15:00 -0700
last_modified_at: 2015-01-18 22:51:59 -0800
permalink: /2014/10/07/getting-in-some-code-stylings-looking-good-for-the-code-dance/
slug: getting-in-some-code-stylings-looking-good-for-the-code-dance
wp_id: 10304
original_url: https://compositecode.blog/2014/10/07/getting-in-some-code-stylings-looking-good-for-the-code-dance/
categories:
- Javascript
- Node.js Things
tags:
- code
- code format
- code style
- javascript
- jscs
- node
- node.js
- nodejs
excerpt: In every language there are opinions about how to format code. With JavaScript, the community abounds with opinions about how the code should look, how variables are declared, whether there should be semi-colons to end each statement, spaces before or after parenthesis, and more than I care to list in a simply worded paragraph like …
image: /wp-content/uploads/2014/01/javascript-logo.png
---

In every language there are opinions about how to format code. With JavaScript, the community abounds with opinions about how the code should look, how variables are declared, whether there should be semi-colons to end each statement, spaces before or after parenthesis, and more than I care to list in a simply worded paragraph like this. Recently the team at Deconstructed sat down to determine what our ongoing code style format would be and how we can enforce it.

The first thing we did was figure out what we could use for enforcement of the coding style. Milan ([@milanloveless](https://twitter.com/milanloveless)) quickly discovered node-jscs per suggestion from Adam Ulvi ([@s5fs](https://twitter.com/s5fs)). He implemented that code as follows.

First install node-jscs.

```bash
npm install jscs -g
```

After installing jscs we added a file called .jscsrc to the main path of the project. In that file we set the following settings for jscs.

```javascript
{
 "preset": "jquery",
 "excludeFiles": [
 "node_modules/**",
 ".gitignore",
 "LICENSE",
 "README.md"
 ]
}
```

Now let’s talk about the [jquery code style preset](https://contribute.jquery.org/style-guide/js/). We decided to go with the jQuery preset for a couple of specific reasons; naming and spacing. Some of the other styles are interesting but didn’t really matter in the decision making process.

Sublime has a way to add a linter to check for all the code style present but one beauty of WebStorm is that it picks up the .jscsrc file automatically and prompts to turn on a linter to check for the code formatting.

All in all, does code style make that much of a difference? In some ways yes, in some ways no. But it sets a standard to maintain a discipline around the code, a familiarity to the code, and allows one to adapt to reading the code in a particular way.
