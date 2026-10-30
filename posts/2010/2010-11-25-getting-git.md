---
title: Getting Git
date: 2010-11-25 14:19:53 -0800
last_modified_at: 2011-01-05 09:07:18 -0800
permalink: /2010/11/25/getting-git/
slug: getting-git
wp_id: 1832
original_url: https://compositecode.blog/2010/11/25/getting-git/
categories:
- How-to
tags:
- git
- source control
excerpt: I’ve been stumbling through getting familiar with Git over the last couple of weeks. It’s the source repository we use at work (thank goodness I’m rid of the damnable TFS nonsense!) and I have officially moved all of my Subversion & even Mercurial Repositories to Git. I really enjoy using Unfuddle, so have moved back to that after using Repositoryhosting for a while. The reason boils down to Open ID. Repositoryhosting didn’t support Open ID and Unfuddle does. Repositoryhosting supported Mercurial which I’ll admit is awesome. I really enjoyed that but wanted the combination of Git experience + Open Id that I get with Unfuddle. In addition, I actually like their management and project tools better. So back I’ve come to Unfuddle. Over the next few weeks I’ll probably be posting a few tidbits about Git. For this entry here’s a tidbit on ignoring certain files that don’t need committed or pushed into the repository. Based on that this is what my exclude file looks like.
---

I’ve been stumbling through getting familiar with Git over the last couple of weeks.  It’s the source repository we use at work (thank goodness I’m rid of the damnable TFS nonsense!) and I have officially moved all of my Subversion & even Mercurial Repositories to Git.  I really enjoy using Unfuddle, so have moved back to that after using Repositoryhosting for a while.  The reason boils down to Open ID.  Repositoryhosting didn’t support Open ID and Unfuddle does.  Repositoryhosting supported Mercurial which I’ll admit is awesome.  I really enjoyed that but wanted the combination of Git experience + Open Id that I get with Unfuddle.  In addition, I actually like their management and project tools better.  So back I’ve come to Unfuddle.

Over the next few weeks I’ll probably be posting a few tidbits about Git.  For this entry here’s a tidbit on ignoring certain files that don’t need committed or pushed into the repository.  Based on that this is what my exclude file looks like.

> - Resharper
> - obj
> - bin
> - \*.suo
> - \*.user
> - \*.vs10x

For more information on setting files to ignore, check out the [github man page](http://help.github.com/git-ignore/).

UPDATE (1/5/2011):  New post & updated file in [this post](/2011/01/05/git-updates/).
