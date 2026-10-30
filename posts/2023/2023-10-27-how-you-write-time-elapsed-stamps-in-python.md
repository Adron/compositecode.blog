---
title: How you write time elapsed stamps in Python?
date: 2023-10-27 10:41:23 -0700
last_modified_at: 2023-10-27 10:41:23 -0700
permalink: /2023/10/27/how-you-write-time-elapsed-stamps-in-python/
slug: how-you-write-time-elapsed-stamps-in-python
wp_id: 66996
original_url: https://compositecode.blog/2023/10/27/how-you-write-time-elapsed-stamps-in-python/
categories:
- python
tags:
- code patterns
- coding patterns
- programming
- python
- python3
- time elapsed
- time stamps
excerpt: A common practice in any coding is to get a time stamp for the start and stop of a process, and probably calc the elapsed time since it started (ya know, because that means we don’t have to mentally calc it ourselves the zillion times the code will run!). The following is usually an example …
image: /wp-content/uploads/2023/10/CleanShot-2023-10-27-at-10.39.33.png
---

A common practice in any coding is to get a time stamp for the start and stop of a process, and probably calc the elapsed time since it started (ya know, because that means we don’t have to mentally calc it ourselves the zillion times the code will run!). The following is usually an example of how I do this particular activity:

```
start_time = datetime.datetime.now()
print(f"Process started at: {start_time.strftime('%Y-%m-%d %H:%M:%S')}")

# ...do the process and all here that is being timed...

end_time = datetime.datetime.now()
print(f"Process ended at: {end_time.strftime('%Y-%m-%d %H:%M:%S')}")
time_elapsed = end_time - start_time
print(f"Time elapsed: {time_elapsed}")
```

***Now, my question is, how do YOU do this in Python? Are there other tricks, cleaner ways to do it?***
