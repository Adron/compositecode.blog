---
title: '_____101 |> F# Coding Ecosystem:  Paket && Atom w/ Paket'
date: 2015-08-23 15:55:10 -0700
last_modified_at: 2015-08-23 16:04:26 -0700
permalink: /2015/08/23/_____101-f-coding-ecosystem-paket-atom-w-paket/
slug: _____101-f-coding-ecosystem-paket-atom-w-paket
wp_id: 11119
original_url: https://compositecode.blog/2015/08/23/_____101-f-coding-ecosystem-paket-atom-w-paket/
categories:
- .NET Bits
- How-to
tags:
- build tools
- f#
- fsharp
- functional
- functional programming
- paket
- scaffold
- template
excerpt: One extremely useful tool to use with F# is Paket. Paket is a package manager that provides a super clean way to manage your dependencies. Paket can handle everything from Nuget dependencies to git or file dependencies. It really opens up your project capabilities to easily pull in and handle dependencies, whereever they are located. I cloned …
image: /wp-content/uploads/2015/06/ah_f_256.png
---

![](https://photos.adron.me/Software/Software-Development/Functional-Bits/i-DChJBd2/0/O/logo.png)One extremely useful tool to use with F# is Paket. Paket is a package manager that provides a super clean way to manage your dependencies. Paket can handle everything from Nuget dependencies to git or file dependencies. It really opens up your project capabilities to easily pull in and handle dependencies, whereever they are located.

I cloned the [Paket Project](https://github.com/fsprojects/Paket) first, since I would like to have the very latest and help out if anything came up. For [more information on Paket check out the about page](http://fsprojects.github.io/Paket/index.html).

```bash
git clone git@github.com:fsprojects/Paket.git
```

I built that project with the respective ./build.sh script and all went well.

```bash
./build.sh
```

## NOTE – Get That Command Line Action

One thing I didn’t notice immediately in the docs (I’m putting in a PR right after this blog entry) was anyway to actually get Paket setup for the command line. On bash, Windows, or whatever, it seemed a pretty fundamental missing piece so I’m going to doc that right here but also submit a PR based on the [issue I added here](https://github.com/fsprojects/Paket/issues/1011)). It could be I just missed it, but either way, here’s the next step that will get you setup the rest of the way.

```bash
./install.sh
```

Yeah, that’s all it was. Kind of silly eh? Maybe that’s why it isn’t documented that I could see? After the installation script is run, just execute paket and you’ll get the list of the various commands, as shown below.

```bash
$ paket
Paket version 1.31.1.0
Command was:
  /usr/local/lib/paket/paket.exe
available commands:

	add: Adds a new package to your paket.dependencies file.
	config: Allows to store global configuration values like NuGet credentials.
	convert-from-nuget: Converts from using NuGet to Paket.
	find-refs: Finds all project files that have the given NuGet packages installed.
	init: Creates an empty paket.dependencies file in the working directory.
	auto-restore: Enables or disables automatic Package Restore in Visual Studio during the build process.
	install: Download the dependencies specified by the paket.dependencies or paket.lock file into the `packages/` directory and update projects.
	outdated: Lists all dependencies that have newer versions available.
	remove: Removes a package from your paket.dependencies file and all paket.references files.
	restore: Download the dependencies specified by the paket.lock file into the `packages/` directory.
	simplify: Simplifies your paket.dependencies file by removing transitive dependencies.
	update: Update one or all dependencies to their latest version and update projects.
	find-packages: EXPERIMENTAL: Allows to search for packages.
	find-package-versions: EXPERIMENTAL: Allows to search for package versions.
	show-installed-packages: EXPERIMENTAL: Shows all installed top-level packages.
	pack: Packs all paket.template files within this repository
	push: Pushes all `.nupkg` files from the given directory.

	--help [-h|/h|/help|/?]: display this list of options.
```

## Paket Elsewhere && Atom

If you’re interested in Paket with Visual Studio I’ll let you dig into that on your own. Some resources are[Paket Visual Studio on Github](https://github.com/fsprojects/Paket.VisualStudio) and[Paket for Visual Studio](https://visualstudiogallery.msdn.microsoft.com/ce104917-e8b3-4365-9490-8432c6e75c36). What I was curious though was Paket integration with either Atom or Visual Studio Code.

Krzysztof Cieślak ([@k\_cieslak](http://twitter.com/k_cieslak)) and Stephen Forkmann ([@sforkmann](http://twitter.com/sforkmann)) maintain the [Paket.Atom Project](https://github.com/fsprojects/Paket.Atom) and Krzysztof Cieślak also handles the [atom-fsharp project](https://github.com/fsprojects/atom-fsharp) for Atom. Watch this gif for some of the awesome goodies that Atom gets with the Paket.Atom Plugin.

[![Click for fullsize image of the gif.](https://raw.githubusercontent.com/fsprojects/Paket.Atom/master/img/paket-add-atom.gif)](https://raw.githubusercontent.com/fsprojects/Paket.Atom/master/img/paket-add-atom.gif)

*Click for fullsize image of the gif.*

## Getting Started and Adding Dependencies

I’m hacking along and want to add some libraries, how do I do that with Paket? Let’s take a look. This is actually super easy, and doesn’t make the project dependentant on peripheral tooling like Visual Studio when using Paket.

The first thing to do, is inside the directory or project where I need the dependency I’ll intialize the it for paket.

```bash
paket init
```

The next step is to add the dependency or dependencies that I’ll need. I’ll add a Nuget package that I’ll need shortly. The first package I want to grab for this project is FsUnit, a testing framework project managed and maintained by Dan Mohl [@dmohl](https://twitter.com/dmohl) and Sergey Tihon [@sergey\_tihon](https://twitter.com/sergey_tihon).

```bash
paket add nuget FsUnit
```

When executing this dependency addition the results displayed show what other dependencies were installed and which versions were pegged for this particular dependency.

```bash
✔ ~/Codez/sharpPaketsExample
15:33 $ paket add nuget FsUnit
Paket version 1.33.0.0
Adding FsUnit to /Users/halla/Codez/sharpPaketsExample/paket.dependencies
Resolving packages:
 -- FsUnit 1.3.1
 -- NUnit 2.6.4
Locked version resolution written to /Users/halla/Codez/sharpPaketsExample/paket.lock
Dependencies files saved to /Users/halla/Codez/sharpPaketsExample/paket.dependencies
Downloading FsUnit 1.3.1 to /Users/halla/.local/share/NuGet/Cache/FsUnit.1.3.1.nupkg
NUnit 2.6.4 unzipped to /Users/halla/Codez/sharpPaketsExample/packages/NUnit
FsUnit 1.3.1 unzipped to /Users/halla/Codez/sharpPaketsExample/packages/FsUnit
3 seconds -- ready.
```

I took a look in the packet.dependencies and packet.lock file to see what were added for me with the paket add nuget command. The packet.dependencies file looked like this now.

```bash
source https://nuget.org/api/v2

nuget FsUnit
```

The packet.lock file looked like this.

```bash
NUGET
  remote: https://nuget.org/api/v2
  specs:
    FsUnit (1.3.1)
      NUnit (2.6.4)
    NUnit (2.6.4)
```

There are a few more dependencies that I want, so I went to work adding those. First of this batch that I added was [FAKE](http://fsharp.github.io/FAKE/) (more on this in a subsequent blog entry), which is a build tool based off of [RAKE](https://github.com/ruby/rake).

```bash
paket add nuget FAKE
```

Next up was [FsCheck](https://github.com/fscheck/FsCheck).

```bash
paket add nuget FsCheck
```

The paket.dependencies file now had the following content.

```bash
source https://nuget.org/api/v2

nuget FAKE
nuget FsCheck
nuget FsUnit
```

The paket.lock file had the following items added.

```bash
NUGET
  remote: https://nuget.org/api/v2
  specs:
    FAKE (4.1.4)
    FsCheck (2.0.7)
      FSharp.Core (>= 3.1.2.5)
    FSharp.Core (4.0.0.1)
    FsUnit (1.3.1)
      NUnit (2.6.4)
    NUnit (2.6.4)
```

Well, that got me started. The code repository at this state is located on this [branch here](https://github.com/Adron/sharpSystemExamples/tree/01-paket) of the [sharpSystemExamples repository](http://www.github.com/Adron/sharpSystemExamples). So on to some coding and the next topic. Keep reading, subsribe, or hit me up on twitter [@adron](https://twitter.com/adron).

## References

- [Paket Project on Github](https://github.com/fsprojects/Paket)
- [Paket for Visual Studio on Github](https://github.com/fsprojects/Paket.VisualStudio) and [Plugin for Visual Studio](https://visualstudiogallery.msdn.microsoft.com/ce104917-e8b3-4365-9490-8432c6e75c36)
- [Paket.Atom Project](https://github.com/fsprojects/Paket.Atom) and [atom-fsharp project](https://github.com/fsprojects/atom-fsharp) for [Atom](https://atom.io/)
- [Atom](https://atom.io/)
