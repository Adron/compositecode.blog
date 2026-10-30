---
title: Name Casing Conventions, The Quick Comparison
date: 2020-11-27 09:28:38 -0800
last_modified_at: 2020-11-27 09:28:38 -0800
permalink: /2020/11/27/name-casing-conventions/
slug: name-casing-conventions
wp_id: 40117
original_url: https://compositecode.blog/2020/11/27/name-casing-conventions/
categories:
- Coding Patterns & Practices
tags:
- coding
- name casing
- naming
- naming conventions
- programming
- software developer
- software development
excerpt: There are a number of name casing practices, which I’ll cover in quick fashion here, for variables and other objects when programming.
image: /wp-content/uploads/2020/11/1nMsRdlFAbXWaP3XMBNpd9A.jpeg
---

There are a number of name casing practices, which I’ll cover in quick fashion here, for variables and other objects when programming.

## The Quickie Synopsis

- camelCaseLikeThis
- PascalCaseLikeThis
- snake\_case\_like\_this
- kebab-case-like-this
- MixAnd-match\_like-this

## Camel Case

With Camel Case the first letter of the first word is lower case, then every subsequent first letter of each word is upper cased. For example, `thisIsCamelCased`, `something` if a singular word, or `somethingElse`.

> My 2 ¢ – I’m a big fan of this case when I’m name private variables or related objects. I’m also a fan of using Camel Casing for certain types of functions, especially in JavaScript such as `this.doesStuff()` or `somethingAnother.doesOtherStuff()`.

## Pascal Case

In usage of Pascal Case, the first letter of each word within the name is upper cased. Examples include `ThisOject`, `ThatThing`, or `WhateverElse()`.

> My 2 ¢ – This is something I like to use for class declaracters (i.e. public class ThisClassThing) and then for functions or methods on that class, or respectively similarly for functions on functions in JavaScript, or the like. Basically, anything that will be used similar to `MyThing.DoesThisThing()`.

## Snake Case

Using Snake Case has the empty spaces replaced with underscores. So a file name like `this is my filename.md` would become `this_is_my_filename.md`.

> My 2 ¢ – Snake case is great when I need to have variables that would otherwise have spaces, but also wouldn’t be displayed regularly with anything that might obfuscate the underscore, such as an HTML.

## Kebab Case

Kebabs are tasty, the case however is similar to Snake Case, except instead of underscores dashes are used. Each space in the name is replaced with a `-` character. Such as `my-table-name-is-this` or `this-is-a-variable`.

> My 2 ¢ – Kebab case is excellent for filenames, URIs, or something of that sort where spacing between the words of a file or path are important to read, but an underscore would be obfuscated by the font rendering such as with a URI.
