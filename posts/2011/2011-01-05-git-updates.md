---
title: Git Updates
date: 2011-01-05 09:06:23 -0800
last_modified_at: 2011-01-05 09:08:12 -0800
permalink: /2011/01/05/git-updates/
slug: git-updates
wp_id: 2056
original_url: https://compositecode.blog/2011/01/05/git-updates/
categories:
- How-to
tags:
- distributed source control
- git
- source control
excerpt: Here’s my latest Git Ignore file for .NET Development.
---

Here’s my latest Git Ignore file for .NET Development.

#Begin .ignore file
#OS junk files
[Tt]humbs.db
\*.DS\_Store

#Visual Studio files
\*.[Oo]bj
\*.dat
\*.crc
\*.exe
\*.pdb
\*.user
\*.aps
\*.pch
\*.vspscc
\*.vssscc
\*\_i.c
\*\_p.c
\*.ncb
\*.suo
\*.tlb
\*.tlh
\*.bak
\*.[Cc]ache
\*.ilk
\*.log
\*.lib
\*.sbr
\*.sdf
ipch/
obj/
[Bb]in
[Dd]ebug\*/
[Rr]elease\*/
Ankh.NoLoad

#Tooling
\_ReSharper\*/
\*.resharper
[Tt]est[Rr]esult\*

#Project files
[Bb]uild/

#Subversion files
.svn

# Office Temp Files
~$\*

#End .ignore file

I added a starting Git workflow on my domain here: <http://www.adronbhall.com/Home/GitWorkflow>
