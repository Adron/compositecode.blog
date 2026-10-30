---
title: ‘bash’ A.K.A. The Solution for Everything –  Passed Variables & The Script Filename
date: 2019-01-02 08:15:16 -0800
last_modified_at: 2019-03-04 10:54:55 -0800
permalink: /2019/01/02/bash-a-k-a-the-solution-for-everything-passed-variables-the-script-filename/
slug: bash-a-k-a-the-solution-for-everything-passed-variables-the-script-filename
wp_id: 15119
original_url: https://compositecode.blog/2019/01/02/bash-a-k-a-the-solution-for-everything-passed-variables-the-script-filename/
categories:
- bash
tags:
- bash
excerpt: When writing a script in bash you can pass parameters into that script to work with. For example, let’s say I have a script file called runme.sh and I want to pass in my name and today’s date. I could do that like this. ./runme.sh “Adron Hall” “12/27/2018” Inside the script I can get access to …
image: /wp-content/uploads/2018/10/good-bash-logo.png
format: aside
---

When writing a script in bash you can pass parameters into that script to work with. For example, let’s say I have a script file called `runme.sh` and I want to pass in my name and today’s date. I could do that like this.

`./runme.sh "Adron Hall" "12/27/2018"`

Inside the script I can get access to the parameters by using the bash param variables of $1, $2, and so on. With a little bash code written up like this.

```
echo "The first parameter $1"

echo "The second parameter is $2"

echo "The \$0 parametere returns the name of the file! This file is named $0."
```

[View the gist on GitHub](https://gist.github.com/Adron/ece3ebae47b87454291e18474d073a6a/039e24e2f05f76385079983935148b4c5f488eb0/bashParams.sh)

![dghubble:go-twitter- Go Twitter REST and Streaming API v1.1 2](/wp-content/uploads/2019/01/dghubblego-twitter-Go-Twitter-REST-and-Streaming-API-v1.1-2.png)
