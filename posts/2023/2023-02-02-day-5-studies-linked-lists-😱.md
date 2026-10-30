---
title: Day 5 Studies – Linked Lists 😱
date: 2023-02-02 00:35:06 -0800
last_modified_at: 2023-02-02 00:35:06 -0800
permalink: /2023/02/02/day-5-studies-linked-lists-%f0%9f%98%b1/
slug: day-5-studies-linked-lists-😱
wp_id: 65822
original_url: https://compositecode.blog/2023/02/02/day-5-studies-linked-lists-%f0%9f%98%b1/
categories:
- Javascript
tags: []
excerpt: I needed a refresher, as I’m at the point in my career I tend to just implement the things and not remember what they’re called anymore. Whether a refresher or you’re new to coding, maybe my refresher will be a good stroll through linked lists. First off, what exactly is a linked list? The name …
image: /wp-content/uploads/2020/04/wordpress-smaller-programming.jpg
---

I needed a refresher, as I’m at the point in my career I tend to just implement the things and not remember what they’re called anymore. Whether a refresher or you’re new to coding, maybe my refresher will be a good stroll through linked lists.

First off, what exactly is a linked list? The name sort of defines what we’re talking about, but a definition would definitely help. From an actual dictionary, I dug up the following definition.

> “A simple linear data structure, each of whose nodes includes a pointer to the next (and sometimes previous) node in the list, enabling traversal of the structure in at least one direction from any starting point.”
>
> via [Wordnick](https://www.wordnik.com/)

The parenthesis above overloads the definition a bit in describing both a simple linked list and a doubly linked list. Let’s define further to differentiate those two and throw in a circular one to boot.

## Singly Linked Lists

Each node contains a pointer to the next node. The code for a singly linked list would look something like this, if you put it together in JavaScript.

```
class ListNode {
    constructor(data) {
        this.data = data
        this.next = null
    }
}

class LinkedList {
    constructor(head = null) {
        this.head = head
    }
}
```

Note however, in this example, the pointer is really the next inferred object. You’d need to use a language like C, or C++, to build a linked list with an actual pointer. that would look something like this.

```
struct Node {
    int data;
    struct Node* next;
};

#include <bits/stdc++.h>
using namespace std;

class Node {
public:
    int data;
    Node* next;
};

void printList(Node* n)
{
    while (n != NULL) {
        cout << n->data << " ";
        n = n->next;
    }
}
```

Here you can see the \* used to set a pointer and then the reference to move between the nodes below. It’s a bit more complicated using a language like this, but I wanted to – because I’m often complicated – point out how it would be done with C++. This introduces additional capabilities, but I won’t go on about the nuances of using actual pointers here and am instead going to focus on the linked list concepts themselves. However it doesn’t hurt to know this and along with pointers themselves, this is a great topic for another post another time, so back to linked lists!

Referring back to the JavaScript example above, if you were to build out several nodes like this.

```
let node1 = new ListNode("a singular node.")
let node2 = new ListNode("some other node.")
let node3 = new ListNode("and another rando node.")
```

Then put together the nodes, and instantiate a linked list like this.

```
node1.next = node2
node2.next = node3

let list = new LinkedList(node1)
```

You can then request various nodes of the linked list or get the linked list object itself like this.

```
console.log(list.head)
console.log(list.head.next.data)
console.log(list.head.next.next.data)
```

The first console log would print out the entire list.head object, which means all of the nested objects too. That would look like this.

```
ListNode {
  data: 'a singular node.',
  next: ListNode {
    data: 'some other node.',
    next: ListNode { data: 'and another rando node.', next: null }
  }
}
```

The second and third console logs would print out `"some other node."` and `"and another rando node."` respectively.

## Double Linked Lists

Each node contains a pointer to the next and previous nodes. That turns the above example into this.

```
class ListNode {
    constructor(data) {
        this.data = data
        this.next = null
        this.prev = null
    }
}

class LinkedList {
    constructor(head = null) {
        this.head = head
    }
}
```

## Summary

That’s the short SITREP on LinkedLists. There’s a lot more to cover, the functions that work on the list, the traversals, the addition and removal of nodes, etc. But this post is just intended for a quick review of the structure of linked lists at their core. On to next topics, cheers!
