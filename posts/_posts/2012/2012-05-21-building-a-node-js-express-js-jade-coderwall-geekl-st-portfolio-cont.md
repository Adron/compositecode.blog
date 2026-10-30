---
title: Building a Node.js + Express.js + Jade CoderWall + Geekl.st Portfolio (cont…)
date: 2012-05-21 10:55:18 -0700
last_modified_at: 2012-09-10 22:48:33 -0700
permalink: /2012/05/21/building-a-node-js-express-js-jade-coderwall-geekl-st-portfolio-cont/
slug: building-a-node-js-express-js-jade-coderwall-geekl-st-portfolio-cont
wp_id: 5668
original_url: https://compositecode.blog/2012/05/21/building-a-node-js-express-js-jade-coderwall-geekl-st-portfolio-cont/
categories:
- How-to
- Javascript
- Node.js Things
tags: []
excerpt: In the previous blog entry I went thru the steps needed to get a Node.js site up and running with Express.js. Next I’m going to leap right into getting some mash ups going with Coder Wall. I’m currently waiting on Geekli.st to get me some beta API access, when that happens I’ll be adding some …
---

In the [previous blog](/2012/05/14/building-a-node-js-express-js-jade-coderwall-geekl-st-portfolio/) entry I went thru the steps needed to get a Node.js site up and running with Express.js. Next I’m going to leap right into getting some mash ups going with Coder Wall. I’m currently waiting on Geekli.st to get me some beta API access, when that happens I’ll be adding some of the geeky list to the portfolio. For now… on with the mash up.

[![Folder Structure](/images/adronhall.smugmug.com/Software/Software-Development/Nodejs-Bits/i-2hNd5tF/0/O/Screen-Shot-2012-05-14-at.png "Folder Structure")](https://github.com/Adron/codingwall)

*Folder Structure*

First things first, get the pertinent pieces you need from proudify.js (check it out here: <https://github.com/icebreaker/proudify> and on Mihail’s site here: <http://proudify.me>). My folder structure looked like this once I had pulled in the js & css files I needed. You may notice I have three image files too, I picked them up via <http://iconfinder.com>, but you can snag my github and they’re included in that.

If you just want to clone the code, I do have it available on [github](https://github.com) @ <https://github.com/Adron/codingwall>.

.
.
.
.
Next I setup the index.jade like this:

```vb
h1= title

div.splitter
    div.left
        div.navAlpha
          p Welcome to #{title}'s Portfolio Site

          a(href='http://www.linkedin/in/adron&#8217;)
            | <img alt="Linkedin" src="images/linkedin.png" style="border: 0px" />
          br
          a(href='http://twitter.com/adron&#8217;)
            | <img alt="Twitter @adron" src="images/twitter.png" style="border: 0px" />
          br
          a(href='http://www.facebook.com/adron&#8217;)
            | <img alt="Facebook" src="images/facebook.png" style="border: 0px" />

        div.navBeta
          p #{title}'s Other Web Presence

          ul
            li
              a(href='http://compositecode.com&#8217;)
                | Composite Code
            li
              a(href='https://github.com/Adron&#8217;)
                | Github
            li
              a(href='http://www.linkedin.com/in/adron&#8217;)
                | LinkedIn
            li
              a(href='http://www.facebook.com/adron&#8217;)
                | Facebook
            li
              a(href='http://twitter.com/adron&#8217;)
                | Twitter

    div.right
        div.crazy
          p the content
```

After I setup the index.jade I changed the layout.jade to have the following code.

```vb
doctype 5
html(lang="en")
  head
    title= title
    link(rel='stylesheet', href='/stylesheets/style.css')
    link(rel='stylesheet', href='/stylesheets/site.css')
    link(rel='stylesheet', href='/stylesheets/splitter.css')
    link(rel='stylesheet', href='/stylesheets/proudify.min.css')
    script(src='/javascripts/jquery-1.4.4.min.js')
    script(src='/javascripts/jquery-ui-1.8.7.custom.min.js')
    script(src='/javascripts/jquery-proudify.min.js')
  body!= body
```

Those are basically all the changes I made for the first push to github. Run the standard app:

```bash
node app.js
```

Once it runs you should see the basic display of information. The proudify.js pulls the CoderWall badges from the their site.

![Coding Wall](/images/adronhall.smugmug.com/Software/Software-Development/Nodejs-Bits/i-889wZxH/0/O/Screen-Shot-2012-05-21-at.png "Coding Wall")

*Coding Wall*

At this time I still haven’t had time to weave in the Geekli.st yet, but will work toward doing that in the future and making a post.

I’ll be adding other features to this, as an example, around database support, connecting to services and a host of other functionalities. So stay tuned to this blog and be sure to follow the github repository for the latest bits.

Until then, enjoy.
