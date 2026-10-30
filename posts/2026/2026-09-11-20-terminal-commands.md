---
title: Twenty-ish Terminal Commands for Getting Around the File System
date: 2026-09-11 09:49:05 -0700
last_modified_at: 2026-09-23 14:09:34 -0700
permalink: /2026/09/11/20-terminal-commands/
slug: 20-terminal-commands
wp_id: 75296
original_url: https://compositecode.blog/2026/09/11/20-terminal-commands/
categories:
- cli
tags:
- bash
- cli
- command line
- file system
- terminal
- zsh
excerpt: This content provides a comprehensive guide to terminal commands, focusing on file navigation and management in macOS and Linux. It highlights essential commands like ls, pwd, cd, tree, find, and others, detailing their functionalities and useful options. The guide aims to enhance user efficiency in file-system navigation through command-line tools.
image: /wp-content/uploads/2026/09/hero-20-terminal-commands.jpg
---

Recently I was digging around in the terminal and wanted an `ls` command that behaved like a fully opened tree view. That led me back through a bunch of the file-system commands I use all the time, along with a few switches that make them far more useful.

This is the resulting quick reference. I’m writing this on macOS with `zsh`, but most of it applies directly to Linux too. A few tools—particularly `tree` and `fd`—may need to be installed first.

## First, the Many Faces of `ls`

The plain command lists the current directory.

```bash
ls
```

Add `-l` for the vertical, long-listing format. This shows permissions, link count, owner, group, size, modified date, and name.

```bash
ls -l
```

Add `-a` to include hidden entries—names beginning with a dot—and `-h` to make sizes human-readable. The switches can be combined.

```bash
ls -lah
```

To descend through every directory and list its contents, add `-R` for recursive.

```bash
ls -laRh
```

That gets us the fully opened contents, although the output is grouped by directory rather than drawn as a visual tree.

## Navigation

### 1. `pwd` — Where Am I?

When I’ve wandered six directories deep and forgotten where I am, `pwd` prints the full path to the working directory.

```bash
pwd
```

### 2. `cd` — Change Directory

Move into a directory, up one level, back to the previous directory, or straight home.

```bash
cd projects
cd ..
cd -
cd ~
```

Paths containing spaces need quotes, as in `cd "My Projects"`.

### 3. `pushd` and `popd` — Directory Bookmarks, Sort Of

`pushd` changes directories while saving the current location on a stack. `popd` takes me back. This is excellent when bouncing between two distant parts of a repository.

```bash
pushd ~/Code/my-project/docs
popd
```

### 4. `tree` — The Actual Tree View

Unlike recursive `ls`, `tree` draws the hierarchy. `-a` includes hidden entries, `-L 2` limits output to two levels, and `-h` prints readable sizes.

```bash
tree -a -h -L 2
```

On macOS, install it with `brew install tree` if it is not already available.

## Finding and Inspecting Things

### 5. `find` — Search the Directory Tree

Find every Markdown file below the current directory. Here `.` means “start here,” `-type f` limits results to files, and `-name` supplies the filename pattern.

```bash
find . -type f -name "*.md"
```

Use `-type d` to find directories instead.

### 6. `fd` — A Friendlier Find

`fd` provides a concise, fast alternative when installed. This finds Markdown files while including hidden paths but excluding `.git`.

```bash
fd --hidden --exclude .git '\.md$'
```

Install it on macOS with `brew install fd`.

### 7. `stat` — All the File Details

`stat` reports metadata such as size, permissions, timestamps, and inode information.

```bash
stat quick-article.md
```

The exact output differs between macOS and Linux, but the intent is the same.

### 8. `file` — What Is This Thing?

Extensions can lie. `file` inspects the contents and reports what it believes the file actually is.

```bash
file mysterious-download
```

### 9. `du` — What Is Using the Space?

`du` measures disk usage. `-s` summarizes instead of listing everything below the target, and `-h` makes the result readable.

```bash
du -sh .
du -sh ./*
```

### 10. `df` — How Much Disk Is Left?

Where `du` examines files and directories, `df` reports free and used space on mounted file systems. Again, `-h` keeps the numbers readable.

```bash
df -h
```

### 11. `less` — Read Without Flooding the Terminal

For a file longer than one screen, use `less`. Search with `/text`, advance with the space bar, move backward with `b`, and quit with `q`.

```bash
less application.log
```

### 12. `head` and `tail` — Inspect the Edges

These show the beginning or end of a file. `-n 20` asks for twenty lines. `tail -f` keeps watching as new lines arrive, which is particularly handy for logs.

```bash
head -n 20 application.log
tail -n 20 application.log
tail -f application.log
```

## Creating and Managing Files

### 13. `mkdir` — Create Directories

The useful switch here is `-p`: it creates missing parent directories and does not complain if the path already exists.

```bash
mkdir -p notes/terminal/examples
```

### 14. `touch` — Create an Empty File

If the file does not exist, `touch` creates it. If it does exist, `touch` updates its timestamps without changing the contents.

```bash
touch notes.md
```

### 15. `cp` — Copy

Copy a file with plain `cp`. Use `-R` to copy a directory recursively and `-i` to ask before overwriting something.

```bash
cp -i notes.md notes-backup.md
cp -Ri source-folder destination-folder
```

### 16. `mv` — Move or Rename

`mv` handles both jobs. I often include `-i` for an overwrite prompt.

```bash
mv -i draft.md published.md
mv -i published.md archive/
```

### 17. `ln` — Create a Link

`ln -s` creates a symbolic link. The first path is the existing target; the second is the new link.

```bash
ln -s ~/Code/my-project/current-config.json config.json
```

### 18. `rmdir` — Remove an Empty Directory

`rmdir` only removes empty directories. That limitation makes it useful when I want the command to refuse anything containing files.

```bash
rmdir old-empty-folder
```

### 19. `rm` — Remove Files Carefully

Plain `rm` removes files. `-i` asks before each removal. Recursive `-R` removes directories and their contents, so double-check the path before pressing Return.

```bash
rm -i unwanted.txt
rm -Ri unwanted-folder
```

There generally is no built-in undo. On macOS, moving something to the Trash in Finder is often a better choice when I’m not absolutely sure.

### 20. `open` — Hand It to macOS

`open` opens a file in its default application. Give it a directory and Finder opens there; use `-a` to choose an application.

```bash
open README.md
open .
open -a "Visual Studio Code" .
```

On Linux, the closest general equivalent is usually `xdg-open`.

## A Few Combinations I Actually Use

Here are the quick combinations I tend to reach for most often.

```bash
# Everything here, including hidden entries, with readable details.
ls -lah

# Everything below here, recursively, in long format.
ls -laRh

# A manageable visual overview, two levels deep.
tree -a -L 2

# Find the biggest immediate entries in the current directory.
du -sh ./* | sort -h

# Jump somewhere temporarily, inspect it, and jump back.
pushd ~/Code/some-project
ls -lah
popd
```

That’s the lot: twenty-ish commands and a pile of switches that turn the terminal into a quick file-system navigator. The commands themselves are only half of the story. Run `man ls`, `man find`, or `man` followed by any of the built-in commands above to spelunk through everything else they can do.
