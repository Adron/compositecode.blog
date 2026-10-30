---
title: Documentation First w/ README.md && Project Tree Build
date: 2015-05-06 10:50:39 -0700
last_modified_at: 2015-05-06 10:50:39 -0700
permalink: /2015/05/06/documentation-first-w-readme-md-project-tree-build/
slug: documentation-first-w-readme-md-project-tree-build
wp_id: 10975
original_url: https://compositecode.blog/2015/05/06/documentation-first-w-readme-md-project-tree-build/
categories:
- How-to
- Software Projects
tags:
- bash
- command line
- folder structure
- project organization
- project structure
- tree
excerpt: I’m sitting here trying to get the folder structure for my project into a kind of ASCII Tree or something. I wasn’t going to manually do this, it would be insane. Especially on any decent size Enterprise Project with an endless supply of folders and nested content. I went digging to come up with a …
---

I’m sitting here trying to get the folder structure for my project into a kind of ASCII Tree or something. I wasn’t going to manually do this, it would be insane. Especially on any decent size Enterprise Project with an endless supply of folders and nested content. I went digging to come up with a better solution. On Linux I immediately found the [Tree Utility](http://mama.indstate.edu/users/ice/tree/) which was perfect.

***Except I was on OS-X.***

First option I gave a go to was to build the thing. Because I like to do things the hard way sometimes. First I needed to get the source, which is available [here](http://mama.indstate.edu/users/ice/tree/).

```bash
curl -O ftp://mama.indstate.edu/linux/tree/tree-1.7.0.tgz
```

Once downloaded, unzip the source into a directory and find the following section for the particular operating system you want to use the utility on. The section for OS settings looked like this when I finished editing it.

```bash
# Uncomment options below for your particular OS:

# Uncomment for OS X:
CC=cc
CFLAGS=-O2 -Wall -fomit-frame-pointer -no-cpp-precomp
LDFLAGS=
MANDIR=/usr/share/man/man1
OBJS+=strverscmp.o
```

Now get a good build of the command file.

```bash
./configure
make
```

Now let’s get tree into the executable path.

```bash
sudo mkdir -p /usr/local/bin
sudo cp tree /usr/local/bin/tree
```

Make sure your ~/.bash\_profile is setup right, include this.

```bash
export PATH="/usr/local/bin:$PATH"
```

Reload the shell and tree should be available as a command.

The other option which is really simple, if you don’t want to compile to code, is to just use brew to install it.

```bash
brew install tree
```

So now you can use tree, and do cool stuff like pipe it out to a file. If you’re running this against a Node.js Project you may want to delete the node\_modules directory and then just reinstall it after running the tree command.

```bash
tree > prof-tree.md
```

Then in your README.md file you can include the folder structure in the description of the project. Here’s a sample output!

```bash
.
├── README.md
├── client
│   └── README.md
├── package.json
├── proj-tree.md
├── server
│   ├── boot
│   │   ├── authentication.js
│   │   ├── explorer.js
│   │   ├── rest-api.js
│   │   └── root.js
│   ├── config.json
│   ├── datasources.json
│   ├── middleware.json
│   ├── model-config.json
│   └── server.js
└── test
    └── test_exists.js

4 directories, 14 files
```

That’s a super easy way to offer better documentation that provides some real insight into what various parts of the project structure are actually for.
