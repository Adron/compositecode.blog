---
title: Creating Distributed Database Application Starter Kits
date: 2018-12-21 15:48:36 -0800
last_modified_at: 2018-12-21 15:59:41 -0800
permalink: /2018/12/21/creating-distributed-database-application-starter-kits/
slug: creating-distributed-database-application-starter-kits
wp_id: 15076
original_url: https://compositecode.blog/2018/12/21/creating-distributed-database-application-starter-kits/
categories:
- Architecture
- Coding Adventures
- Unknown Code Ramblings
tags:
- apache cassandra
- architecture
- cassandra
- coding
- datastax
- programming
- starter kits
excerpt: I’ve boarded a bus, and as always, when I board a bus I almost always code. Unless of course there are people I’m hanging out with then I chit chat, but right now this is the 212 and I don’t know anybody on this chariot anyway. So into the code I go. I’ve been re-reviewing the Docker …
---

I’ve boarded a bus, and as always, when I board a bus I almost always code. Unless of course there are people I’m hanging out with then I chit chat, but right now this is the [212](https://kingcounty.gov/depts/transportation/metro/schedules-maps/212.aspx) and I don’t know anybody on this chariot anyway. So into the code I go.

I’ve been re-reviewing the Docker and related collateral we offer at DataStax. In that review it seems like it would be worth having some starter kit applications along with these “default” Docker options. This post I’ve created to provide the first language & tech stack of several starter kits I’m going to create.

**Starter Kit – The Todo List Template**

This first set of starter kits will be based upon a todo list application. It’s really simple, minimal in features, and offers a complete top to bottom implementation of a service, and an application on top of that service all built on [Apache Cassandra](http://cassandra.apache.org/). In some places, and I’ll clearly mark these places, I might add a few [DataStax Enterprise](https://www.datastax.com/products/datastax-enterprise) features around search, analytics, or graph.

**The Todo List**

**Features:** The following detail the features, from the users perspective, that this application will provide. Each implementation will provide all of these features.

- A user wants to create a user account to create todo lists with.
- A user wants to be able to store a username, full name, email, and some simple notes with their account.
- A user wants to be able to create a todo list that is identified by a user defined name. (i.e. “Grocery List”, “Guitar List”, or “Stuff to do List”)
- A user want to be able to logout and return, then retrieve a list from a list of their lists.
- A user wants to be able to delete a todo list.
- A user wants to be able to update a todo list name.
- A user wants to be able to add items to a todo list.
- A user wants to be able to update items in the todo list.
- A user wants to be able to delete items in a todo list.

**Architecture:** The following is the architecture of the todo list starter kit application.

- Database: Apache Cassandra.
- Service: A small service to manage the data tier of the application.
- User Interface: A web interface using React/Vuejs ??

As you can see, some of the items are incomplete, but I’ll decide on them soon. My next review is to check out what I really want to use for the user interface, and also to get a user account system figured out. I don’t really want to create the entire user interface, but instead would like to use something like Auth0 or Okta.

**May I Ask?**

There are numerous things I’d love help with. Are there any user stories you think are missing? Should I add something? What would make these helpful to you? Leave a comment, or tweet at me [@Adron](https://twitter.com/Adron). I’d be happy to get some feedback and other’s thoughts on the matter so that I can ensure that these are simple, to the point, usable, and helpful to people. Cheers!
