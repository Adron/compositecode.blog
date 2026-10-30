---
layout: page
title: Because I Always Forget, VI Commands!
date: 2013-03-05 18:15:24 -0800
last_modified_at: 2015-08-12 22:20:25 -0700
permalink: /because-i-always-forget-vi-commands/
slug: because-i-always-forget-vi-commands
wp_id: 7799
original_url: https://compositecode.blog/because-i-always-forget-vi-commands/
---

[Home](http://compositecode.com/) > [Docs](/docs/) >

## Starting vi

You may use vi to open an already existing file by typing

```bash
vi filename
```

where “filename” is the name of the existing file. Also create a new file by typing

```bash
vi newname
```

where “newname” is the name you wish to give the new file.

To open a new file called “testvi,” enter

```bash
vi testvi
```

At this point you can either exit out of the file or save it (see below for more commands on this).

## vi’s two modes:

- command mode
- insert mode

In command mode, the letters of the keyboard perform editing functions (like moving the cursor, deleting text, etc.). To enter command mode, press the escape key.

In insert mode, the letters you type form words and sentences. Unlike many word processors, vi starts up in command mode.

**Entering Text**
In order to begin entering text in this empty file, you must change from command mode to insert mode. To do this, type

```bash
i
```

Nothing appears to change, but you are now in insert mode and can begin typing text.

## Basic Editing

Editing commands require that you be command mode. Many of the editing commands have a different function depending on whether they are typed as upper- or lowercase. Often, editing commands can be preceded by a number to indicate a repetition of the command.

**Deleting Characters**
To delete a character from a file, move the cursor until it is on the incorrect letter, then type

```bash
x
```

The character under the cursor disappears. To remove four characters (the one under the cursor and the next three) type

```bash
4x
```

To delete the character before the cursor, type

```bash
X
```

**Deleting Words**
To delete a word, move the cursor to the first letter of the word, and type

```bash
dw
```

This command deletes the word and the space following it.

To delete three words type

```bash
3dw
```

**Deleting Lines**

To delete a whole line, type

```bash
dd
```

The cursor does not have to be at the beginning of the line. Typing dd deletes the entire line containing the cursor and places the cursor at the start of the next line. To delete two lines, type

```bash
2dd
```

To delete from the cursor position to the end of the line, type

```bash
D
```

**Replacing Characters**
To replace one character with another:

Move the cursor to the character to be replaced.

```bash
r
```

Type the replacement character.
The new character will appear, and you will still be in command mode.

Replacing Words
To replace one word with another, move to the start of the incorrect word and type

```bash
cw
```

The last letter of the word to be replaced will turn into a $. You are now in insert mode and may type the replacement. The new text does not need to be the same length as the original. Press to get back to command mode. To replace three words, type

```bash
3cw
```

Replacing Lines
To change text from the cursor position to the end of the line:

```bash
C
```

Type the replacement text.
Press .
Inserting Text
To insert text in a line:

Position the cursor where the new text should go.

```bash
i
```

Enter the new text.

**Undoing**
To undo your most recent edit, type

```bash
u
```

To undo all the edits on a single line, type

```bash
U
```

Undoing all edits on a single line only works as long as the cursor stays on that line. Once you move the cursor off a line, you cannot use U to restore the line.

Moving Around in a File
There are shortcuts to move more quickly though a file. All these work in command mode.

Key Movement
— ——–
w forward word by word
b backward word by word
$ to end of line
0 (zero) to beginning of line
H to top line of screen
M to middle line of screen
L to last line of screen
G to last line of file
1G to first line of file
f scroll forward one screen
b scroll backward one screen
d scroll down one-half screen
u scroll up one-half screen
Moving by Searching
To move quickly by searching for text, while in command mode:

```bash
/
```

Enter the text to search for.

```bash
.
```

The cursor moves to the first occurrence of that text.

To repeat the search in a forward direction, type

```bash
n
```

To repeat the search in a backward direction, type

```bash
N
```

**Closing and Saving a File**
With vi, you edit a copy of the file, rather than the original file. Changes are made to the original only when you save your edits.

:w

To quit vi, and discard any changes your have made since last saving:

```bash
:q!
```
