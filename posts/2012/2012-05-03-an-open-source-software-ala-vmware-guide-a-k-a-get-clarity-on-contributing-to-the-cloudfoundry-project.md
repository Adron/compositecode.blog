---
title: 'An Open Source Software ala VMware Guide :: A.K.A. Get Clarity on Contributing to the CloudFoundry Project!'
date: 2012-05-03 15:06:06 -0700
last_modified_at: 2012-05-03 15:20:26 -0700
permalink: /2012/05/03/an-open-source-software-ala-vmware-guide-a-k-a-get-clarity-on-contributing-to-the-cloudfoundry-project/
slug: an-open-source-software-ala-vmware-guide-a-k-a-get-clarity-on-contributing-to-the-cloudfoundry-project
wp_id: 5547
original_url: https://compositecode.blog/2012/05/03/an-open-source-software-ala-vmware-guide-a-k-a-get-clarity-on-contributing-to-the-cloudfoundry-project/
categories:
- Cloud Foundry
tags:
- cloud foundry
- cloudfoundry
- open source
- open source software
- oss
excerpt: I’ve jumped into committing some source code to the Cloud Foundry Project and I wanted to document the process so far. The Cloud Foundry project is a little trickier than most open source projects, because there are a host of tools around the process. As that is the case, it isn’t a simple github repository …
---

I’ve jumped into committing some source code to the Cloud Foundry Project and I wanted to document the process so far. The Cloud Foundry project is a little trickier than most open source projects, because there are a host of tools around the process. As that is the case, it isn’t a simple github repository with easy to push pull requests and other flows. Instead, there’s a trick to it all and that’s what this blog entry is about. **These observations about getting a first pull request submitted:**

- The instructions, sort of, are located here for contributions: <http://cloudfoundry.org/contribute> There however seems to be some key parts missing from these (or I didn’t find them on any of the immediate links). The main one being any connection, information, or workflow around the internal git repository that they have setup. That should be more prominently displayed. Can I submit a pull request for the contributions page?  🙂
- The github repository. I won’t beat around the bush on this particular observation. The github repository is almost entirely *useless*. You can’t send pull requests to it, nobody communicates around it, and all the existing pull requests are dead. It is a read-only repo of the internal git repo. So don’t look there for any key pieces of information – check the Google Groups and other information I’ve linked in this blog entry.
- The real code base is in an internal git repository held by VMware that has a [gerrit (code review)](http://reviews.cloudfoundry.org/) + Jenkins (awesome build server). This is actually a pretty slick setup. Albeit I admit this is absolutely more work for contributors. But when you got a hot potato you gotta pass around the pain (is that even an colloquialism? Probably not, so I just made it up).
- There are some very useful google groups that you should sign up for if you intend to contribute code to Cloud Foundry.  This is where all the super smart and also friendly Cloud Foundry core team hang out. Even if you aren’t going to commit code, go sign up anyway. You’ll be able to get a lot of very useful information from these guys related to setting up, using, and deploying Cloud Foundry. <http://groups.google.com/a/cloudfoundry.org/groups/dir>
- They also ask you to sign a document related to contributions located here: <http://cloudfoundry.org/individualcontribution.pdf> basically promising you didn’t steal someone else’s code and that you won’t sue VMware for making this code public.
- The [JIRA site](https://cloudfoundry.atlassian.net) (another account login you’ll need to setup, it is worth it to, so get one if you intend to commit code. Otherwise if you just want to lurk then don’t really worry about the JIRA site too much.)
- Once you are logged in to the Google Groups you can hit this link: <https://groups.google.com/a/cloudfoundry.org/group/vcap-dev/browse_thread/thread/af205159a17ec358> which actually has the best instructions I’ve found on getting a good clone and submitting a pull request via the gerrit command line tool.
- Another more immediate way to get help is to bounce into IRC via freenode and join the #cloudfoundry channel. The core devs plus a number of other coders hang out in that room.

**Getting it Cloned**

Per the instructions above, the first thing you’ll need is the code base. You’ll need to make sure you have a gerrit account first and that you’ve submitted your SSH public keys to gain access. Then get the vcap code base via the gerrit CLI:

```bash
$ sudo gem install gerrit-cli
Password:
Successfully installed gerrit-cli-0.0.11 gem installed
Installing ri documentation for gerrit-cli-0.0.1...
Installing RDoc documentation for gerrit-cli-0.0.1...
$
```

I left the results of the command in just for familiarities sake. The next command is to clone the repo gerrit style.

```bash
$ gerrit clone ssh://adron@reviews.cloudfoundry.org:29418/vcap
Cloning into 'vcap'...remote:
Counting objects: 12253, doneremote: Finding sources: 100% (12253/12253)Receiving objects:  89% (10961/12253), Receiving objects:  89% (10961/12253), Receiving objects:  89% (10961/12253), Receiving objects:  89% (10961/12253), Receiving objects:  89% (10961/12253), Receiving objects:  89% (10961/12253), 247.05Receiving objects:  94% (11631/12
Receiving objects:  94% (11631/12253), Receiving objects:  94% (11631/12253), Receiving objects:  94% (11631/12253), Receiving objects:  94% (11631/12253), 548.27 MiB | 105
remote: Total 12253 (delta 6438), reused 11765 (delta 6438)
Receiving objects: 100% (12253/12253), 773.92 MiB | 311 KiB/s, done.

Resolving deltas: 100% (6438/6438), done.

Installing commit-msg hooks into 'vcap/.git/hooks'.commit-msg
100% 2331     2.3KB/s   00:00

Installing tracked git hooks:

$
```

> **NOTE:** This will likely take a long while for the vcap repo. It took me about 45 minutes to clone. That’s based on two seperate machines on two different fast internet connections with two different operating systems.  So just be patient.

Then just cd vcap into the working directory and create your changes. Once the changes are committed then pull the latest, merging again if needed, and then push the pull request via the following command.

```bash
$ gerrit push
```

Once that is done your pull request will be put into the continuous integration build queue. Then someone from the core team will up vote your code or deny it with reasons. You can check out the status:

- <http://reviews.cloudfoundry.org/#/q/status:open,n,z>  => open requests
- <https://cloudfoundry.atlassian.net/secure/Dashboard.jspa> => JIRA Board
- <http://support.cloudfoundry.com/home> => Support pages for Cloud Foundry

The OSS-Docs are located on Github, check those out here. They’re not super complete, but the information they do have in them is pretty solid. So check these out while hacking:  <https://github.com/cloudfoundry/oss-docs>.

In my next write up about my efforts with Cloud Foundry, I’ll dive into what I’m pushing and what for. So keep reading, I’ll be back with more good bits.
