---
title: Vue.js Studies Day 3 – More Ways to Get Started
date: 2023-01-12 17:20:55 -0800
last_modified_at: 2023-01-12 17:20:55 -0800
permalink: /2023/01/12/vue-js-studies-day-3-more-ways-to-get-started/
slug: vue-js-studies-day-3-more-ways-to-get-started
wp_id: 65733
original_url: https://compositecode.blog/2023/01/12/vue-js-studies-day-3-more-ways-to-get-started/
categories:
- Unknown Code Ramblings
tags: []
excerpt: For this next getting started I decided to give JetBrains WebStorm a go and see what it used, and what extras it would provide. I presumed correctly, that there is indeed lagniappe!
image: /wp-content/uploads/2023/01/vuejs-dailies-header.png
---

## Method 3 – JetBrains WebStorm

For this next method on getting started I decided to give [JetBrains](https://www.jetbrains.com/) [WebStorm](https://lp.jetbrains.com/webstorm-ide/) a go and see what it used, and what extras it would provide. I presumed correctly, that there is indeed lagniappe!

I opened up WebStorm – to note, I’ve got a full subscription to the entire line of JetBrains tools but you can go get a free trial version if you want to give it a try – and clicked on the *File* menu and *New*, then on *Project*.

[![](/wp-content/uploads/2023/01/CleanShot-2023-01-11-at-20.42.01.png)](/wp-content/uploads/2023/01/CleanShot-2023-01-11-at-20.42.01.png)
[![](/wp-content/uploads/2023/01/vuejs-webstorm-start3.png)](/wp-content/uploads/2023/01/vuejs-webstorm-start3.png)

That brings up another window with project and I clicked on *New Project* from there, which gives me a list of web projects to start and I chose Vue.js. After entering location and node interpreter, the Vue CLI – both of which I’ve already got installed but if they’re not, WebStorm can do that for you – and then click *Create*.

[![](/wp-content/uploads/2023/01/vuejs-webstorm-start2.png)](/wp-content/uploads/2023/01/vuejs-webstorm-start2.png)

That’ll spin up a project and open it in the IDE itself. You’ll see a prompt popup that’ll ask if you want to run `npm install` and if not, be sure to run that either view the embedded CLI, or via the run npm option in the IDE. The IDE’s display will show the familiar “Process finished with exit code 0”.

[![](/wp-content/uploads/2023/01/vuejs-webstorm1.png)](/wp-content/uploads/2023/01/vuejs-webstorm1.png)

Now there are a range of ways to run the application that was just generated for us. To note, WebStorm has used the same method that you can use if you execute `npx create-vue`. The big differences are there are now hooks, and the IDE itself is aware of a number of things that can help you do a number of things from debugging to application execution. For example, looking up at the top of the IDE (pending it’s a default install and you’ve not moved parts of the IDE around!) we now have a button to execute the application with npm, or to execute and debug the application.

[![](/wp-content/uploads/2023/01/vuejs-webstorm3.png)](/wp-content/uploads/2023/01/vuejs-webstorm3.png)

When you execute the application, the window at the bottom of the IDE will pop up with the familiar launch of vite, and you can even click on the local URI and it’ll launch your default browser. You can also setup the IDE to, by default, launch the browser if you’d like.

[![](/wp-content/uploads/2023/01/vuejs-webstorm4.png)](/wp-content/uploads/2023/01/vuejs-webstorm4.png)
