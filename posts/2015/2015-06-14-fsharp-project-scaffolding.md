---
title: That Non-Windows Scaffolding for OS-X and Linux |> I Broke It! But…
date: 2015-06-14 16:35:40 -0700
last_modified_at: 2015-06-20 22:28:36 -0700
permalink: /2015/06/14/fsharp-project-scaffolding/
slug: fsharp-project-scaffolding
wp_id: 11133
original_url: https://compositecode.blog/2015/06/14/fsharp-project-scaffolding/
categories:
- .NET Bits
- F#
- How-to
tags:
- .NET
- broke build
- error
- f#
- fsharp
- issues
excerpt: I dove into the ProjectScaffold solution recently to see where I could get with this project. Just like in the instructions I first cloned the project. git clone Then executed the shell script to get an appropriate download of Paket and related tools. $ ./build.sh On OS-X my first attempt …
image: /wp-content/uploads/2015/06/ah_f_256.png
---

I dove into the [ProjectScaffold](http://fsprojects.github.io/ProjectScaffold/) solution recently to see where I could get with this project. Just like in the instructions I first cloned the project.

```bash
git clone
```

Then executed the shell script to get an appropriate download of [Paket](https://github.com/fsprojects/Paket) and related tools.

```bash
$ ./build.sh
```

On OS-X my first attempt I got scaffolding but a bad build right off. See the video below for that example.

Trying the same thing on Ubuntu gave me this issue. This issue seemed to be different from the OS-X issue so I’m working to resolve it separately.

```bash
adron@ubuntu ~/C/ProjectScaffold> ./build.sh
No version specified. Downloading latest stable.
Github download failed. Try downloading Paket directly from 'nuget.org'.
Error getting response stream (Write: The authentication or decryption has failed.): SendFailure
```

Then trying it on OS-X gave me this issue.  :-/

Grumble grumble, fuss, fuss, alright, going into debugging and troubleshooting mode. I made a video of the exact steps I went through.

<https://vimeo.com/130705740>

So if you have any ideas, let me know, I’m currently looking through the code and trying out some things. Once I get this working I’ll update this blog entry below the video with the updated resolution. Thanks!

UPDATED: Dammit, the dumbest things are what always punch me in the face the hardest. I fixed it, and it didn’t require a pull request after all! When naming a project be sure to use only string characters to be safe. As I wrote in the [github issue](https://github.com/fsprojects/ProjectScaffold/issues/189), the name “*sharp-kata-01*” breaks the build in a way that gives completely erroneous messages. Once I renamed it things moved forward.
