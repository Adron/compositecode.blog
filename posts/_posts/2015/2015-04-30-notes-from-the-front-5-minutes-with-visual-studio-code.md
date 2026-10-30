---
title: 'Notes From the Front: 5 Minutes With Visual Studio #Code'
date: 2015-04-30 17:21:21 -0700
last_modified_at: 2015-04-30 17:21:22 -0700
permalink: /2015/04/30/notes-from-the-front-5-minutes-with-visual-studio-code/
slug: notes-from-the-front-5-minutes-with-visual-studio-code
wp_id: 10954
original_url: https://compositecode.blog/2015/04/30/notes-from-the-front-5-minutes-with-visual-studio-code/
categories:
- Unknown Code Ramblings
tags: []
excerpt: Ok, so Microsoft released a Visual Studio version on Linux and OS-X called Visual Studio Code. It’s also available for Windows but it’s so minimalistic compared to Visual Studio one might not want to use it on Windows. There is however potential for this new IDE that Microsoft has released. It’s minimal and super fast …
image: /wp-content/uploads/2014/01/photodune-4658016-computer-problem-m.jpg
---

Ok, so Microsoft released a Visual Studio version on Linux and OS-X called [Visual Studio Code](https://code.visualstudio.com/). It’s also available for Windows but it’s so minimalistic compared to Visual Studio one might not want to use it on Windows.

[![Getting Setup on Ubuntu](https://photos.adron.me/Software/Software-Development/Visual-Studio-Things/i-PFvQZnv/0/O/VSC_01.png)](https://photos.adron.me/Software/Software-Development/Visual-Studio-Things/i-PFvQZnv/0/O/VSC_01.png)

*Getting Setup on Ubuntu*

There is however potential for this new IDE that Microsoft has released. It’s minimal and super fast at this point. On OS-X you can set it to launch as many of us OS-X users use Sublime (or your favorite editor here) to open entire projects.

### Starting

Add this to the end of your bash startup script and you’ll have the magic sauce available via the command line.

```bash
code () {
    if [[ $# = 0 ]]
    then
        open -a "Visual Studio Code"
    else
        [[ $1 = /* ]] && F="$1" || F="$PWD/${1#./}"
        open -a "Visual Studio Code" --args "$F"
    fi
}
```

You’ll then be able to open projects with the standard command notation as shown.

```bash
✔ ~/Codez/React-Studies [master|...9]
16:28 $ code .
```

That pulls up a project in the editor just like this.

[![Visual Studio Code in Action](https://photos.adron.me/Software/Software-Development/Visual-Studio-Things/i-TCrX4sm/0/O/VSC_02.png)](https://photos.adron.me/Software/Software-Development/Visual-Studio-Things/i-TCrX4sm/0/O/VSC_02.png)

*Visual Studio Code in Action*

From there, just do what ya do and sling some code. There’s other features that are detailed on the Visual Studio Code site, but I’ll let you read up on those there.

### Git Integration

The next thing I thought was pretty cool was the git integration, if for any reason because it just kind of looks nice. Nothing revolutionary here, but it’s nice to easily see without diving out to the bash to see what’s up.

[![Git Integration](https://photos.adron.me/Software/Software-Development/Visual-Studio-Things/i-LLW7WcD/0/O/VSC_03.png)](https://photos.adron.me/Software/Software-Development/Visual-Studio-Things/i-LLW7WcD/0/O/VSC_03.png)

*Git Integration*

…and the commit screen…

![Committing and Commit Messages](https://photos.adron.me/Software/Software-Development/Visual-Studio-Things/i-9kbMq4b/0/O/VSC_04.png)

*Committing and Commit Messages*

Now mind you, you can commit but not attach to any remotes and actually work with those. That’s kind of… disconnected? It’s fine though, whatever.

## Quick Summary

So that’s my 5 minutes review. My main takeaway from all of this though, is that Visual Studio Code is not ready for prime time usage. It’s sorely missing a ton of features or capabilities that other editors, like Sublime or Atom, already have. I’m sure in the coming versions there will be more features and capabilities added, but currently I’ll be sticking to my WebStorm, Atom, Sublime, or Brackets usage for development needs still. For existing or future C#/F# Development I’ll just be using Xamarin’s tools most likely or diving into a Windows VM with full fledged Visual Studio. Until the future, I’ll just have to keep an eye on Visual Studio Code.
