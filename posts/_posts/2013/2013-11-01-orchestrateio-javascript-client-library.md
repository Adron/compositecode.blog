---
title: Orchestrate.io JavaScript Client Library
date: 2013-11-01 09:31:53 -0700
last_modified_at: 2014-01-23 10:36:03 -0800
permalink: /2013/11/01/orchestrateio-javascript-client-library/
slug: orchestrateio-javascript-client-library
wp_id: 9073
original_url: https://compositecode.blog/2013/11/01/orchestrateio-javascript-client-library/
categories:
- Databases
- Javascript
- My Updates
- Node.js Things
- Orchestrate.io
- Software Projects
tags:
- blog
- client
- client library
- database
- distributed
- distributed database
- feedly
- go
- golang
- graph
- key value
- library
- orchestrate
- orchestrate.io
excerpt: Today I’m starting a project working with Orchestrate.io’s API & open source software collaborations. More about the project in a moment, let’s get up to speed on what I’ll be including in this project. My main focus is to build a client library to access Orchestrate.io. During building this I’ll dive into the key value, …
image: /wp-content/uploads/2014/01/javascript-logo.png
---

Today I’m starting a project working with Orchestrate.io’s API & open source software collaborations. More about the project in a moment, let’s get up to speed on what I’ll be including in this project. My main focus is to build a client library to access Orchestrate.io. During building this I’ll dive into the key value, graph and other storage mechanisms that the client library will provide. Beyond that, I’ll take a stroll through building an NPM library and the pertinent JavaScript the library. So buckle up, we’re going on a code slinging hash writing hacking session.

Over the course of putting together this material, I’ll be posting most of the core material on Orchestrate.io’s blog, so subscribe for updates as they come out. [Feedly](http://cloud.feedly.com/) is a good option, connect via searching for “*orchestrate.io*” or navigate over to the [Orchestrate.io blog](http://blog.orchestrate.io/) itself. 😉

![Orchestrate.io](/wp-content/uploads/2013/11/orchestrate-io.gif)

![JavaScript](/wp-content/uploads/2013/11/js260x260.png)

## Project Effort Context

During building the client I’ll take a dive into who, what, where, when, why and how to interact with the various data structures. I’ll aim for the client to follow the model of the existing Go Client Library that is available at [Orchestrate Go Client on Github](https://github.com/orchestrate-io/orchestrate-go-client). It follows a basic model as shown below in Go language.

```cpp
    c := client.NewClient("Your API Key")
    // Get a value
    value, _ := c.Get("collection", "key")
    // Put a value
    c.Put("collection", "key", strings.NewReader("Some JSON"))
    // Search
    results, _ := c.Search("collection", "A Lucene Query")
    // Get Events
    events, _ := c.GetEvents("collection", "key", "kind")
    // Put Event
    c.PutEvent("collection", "key", "kind", strings.NewReader("Some JSON"))
    // Get Relations
    relations, _ := c.GetRelations("collection", "key", []string{"kind", "kind"})
    // Put Relation
    c.PutRelation("sourceCollection", "sourceKey", "kind", "sinkCollection", "sinkKey")
```

I’ll be working on this client, but don’t hold back on me, feel free to jump in with some of your own code or telling me I wrote some code wrong or whatever. I’d gladly accept any committers jumping in to help out. The more we all work together the more useful information I can provide during this project.

Once this project has produced a workable client pending interest from the community I’ll put together some material about where, how and some best uses around using the client in your Node.js Application. Even prospectively build a JavaScript client side library prospectively for use with Angular or other popular client side libraries.

## References

- <https://github.com/orchestrate-io/orchestrate-go-client>
- <http://blog.orchestrate.io>
- <http://docs.orchestrate.io>
