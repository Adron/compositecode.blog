---
title: Day 4 Studies – Web Related Things
date: 2023-01-13 18:49:52 -0800
last_modified_at: 2023-01-13 18:49:52 -0800
permalink: /2023/01/13/day-4-studies-web-related-things/
slug: day-4-studies-web-related-things
wp_id: 65774
original_url: https://compositecode.blog/2023/01/13/day-4-studies-web-related-things/
categories:
- Unknown Code Ramblings
tags: []
excerpt: Today I got into some studying Vue.js, but realized I wanted to cover some of the basics around things that Vue.js uses but I’d not really covered in the posts. Also before I got into some of the other core topics as outlined on Day 1 there were a number of things that just needed …
---

Today I got into some studying Vue.js, but realized I wanted to cover some of the basics around things that Vue.js uses but I’d not really covered in the posts. Also before I got into some of the other core topics as outlined on [Day 1](/2023/01/03/vue-js-day-1-studies/) there were a number of things that just needed defined. This post, is about those things.

**Virtual DOM** – this is something you hear about that isn’t specifically Vue.js related. React uses a virtual DOM as do other frameworks. The DOM part stands for **D**ocument **O**bject **M**odel, and the Virtual DOM is a lightweight JavaScript representation of this model. This Virtual DOM is what is updated instead of the actual DOM, and when the Virtual DOM is ready for rendering to the actual DOM, a diff is done of the two and only the changes are rendered in the actual DOM. This generally makes changes render much faster than attempting to make the changes in the actual DOM only.

The frameworks that use a Virtual DOM include; React, Vue.js, and Elm. Other frameworks like Svelte created by Rich Harris does not, and Rich is also quoted as saying a Virtual DOM is pure overhead. A valid point, yet arguable whether this is an advantage or disadvantage, as it appears to depend entirely on the situation and type of page(s) being rendered.

There are other techniques like Angular or Ember.js’s incremental DOM that offer an alternate approach to DOM rendering.

Digging more closely into the Document Object Model, it is a cross-platform language independent interface that uses a tree structure to represent XML or HTML. Each branch of the DOM ends in a node, each node containing objects. This provides a way to programmatically traverse the model and gain access to various parts of the tree. The nodes within the DOM can also have event handlers attached to them, which provides a programmatic way to fire off events for execution.

The DOM technology is currently managed by WHATWG – Web Hypertext Application Technology Working Group.

---

**Rendering Mechanism** – This is the way, process, and flow of Vue.js’s rendering of a page for a Vue Application.

This all starts in Vue.js, with the above defined Virtual DOM, as defined in the docs as the VDOM. Remembering from above, that each branch ends in a node, a constant of the VDOM could be written up as shown.

```
const vnode = {
  type: 'div',
  props: {
    id: 'anIdentifierOfSorts'
  },
  children: [
    /* all the other nodes on down the tree. */
  ]
}
```

The Render Pipeline, at a high level compiles, mounts, and patches the VDOM. Vue templates are compiled into render functions that return VDOM trees. The mount function then invokes the render function which walks the returned virtual DOM tree, creates actual DOM nodes based on it and renders. This is performed as a reactive effect to apply changes to the actual DOM. Finally during mount changes, the effect reruns during patch, which creates a new VDOM, the runtime renderer walks the tree, does a diff, and applies updates to the actual DOM.

---

## Templates & Render Functions

It’s important to know that Vue templates are compiled into VDOM render functions. Render functions can also be authored and called programmatically, bypassing a need to create a template. Even though vue recommends, and many if not most tutorials will show templates versus render functions, it’s important to know that render functions are available to use for more flexibility when dealing with dynamic logic or just odd business rules and such.
