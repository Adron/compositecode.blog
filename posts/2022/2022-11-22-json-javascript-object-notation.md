---
title: JSON – JavaScript Object Notation
date: 2022-11-22 22:21:51 -0800
last_modified_at: 2022-11-22 22:21:51 -0800
permalink: /2022/11/22/json-javascript-object-notation/
slug: json-javascript-object-notation
wp_id: 65622
original_url: https://compositecode.blog/2022/11/22/json-javascript-object-notation/
categories:
- References
tags:
- javascript
- javascript object notation
- json
excerpt: JSON (JavaScript Object Notation), a lightweight data-interchange format. It’s relatively easy to read for us humans, which is nice, and is a subset of the JavaScript Programming Language Standard (ECMA-262 3rd Edition – December 1999). JSON is a text format, and even though it’s a subset of JavaScript, is language independent. The conventions are of the C-family of languages like C, C++, C#, Java, JavaScript, and others.
image: /wp-content/uploads/2022/11/object.png
---

JSON (JavaScript Object Notation), a lightweight data-interchange format. It’s relatively easy to read for us humans, which is nice, and is a subset of the JavaScript Programming Language Standard ([ECMA-262 3rd Edition – December 1999](https://www.ecma-international.org/wp-content/uploads/ECMA-262_3rd_edition_december_1999.pdf)).

JSON is a text format, and even though it’s a subset of JavaScript, is language independent. The conventions are of the C-family of languages like C, C++, C#, Java, JavaScript, and others.

There are two structures to JSON; a collection of name value pairs and ordered lists of values. For more details check out the [organization](https://www.json.org/). A few examples for reference.

A simple JSON object.

```
{
    "name":"John",
    "age":30,
    "car":null
}
```

An array of JSON objects.

```
[
    {
        color: "red",
        value: "#f00"
    },
    {
        color: "green",
        value: "#0f0"
    },
    {
        color: "blue",
        value: "#00f"
    },
    {
        color: "cyan",
        value: "#0ff"
    },
    {
        color: "magenta",
        value: "#f0f"
    },
    {
        color: "yellow",
        value: "#ff0"
    },
    {
        color: "black",
        value: "#000"
    }
]
```

A JSON object using a list.

```
{
    "name":"John",
    "age":30,
    "cars":["Ford",&nbsp;"BMW",&nbsp;"Fiat"]
}
```
