---
title: GraphQL VS Code Extension Review && Simple Schema Build
date: 2022-03-24 09:25:13 -0700
last_modified_at: 2022-03-29 17:06:23 -0700
permalink: /2022/03/24/graphql-vs-code-extension-review-simple-schema-build/
slug: graphql-vs-code-extension-review-simple-schema-build
wp_id: 65108
original_url: https://compositecode.blog/2022/03/24/graphql-vs-code-extension-review-simple-schema-build/
categories:
- graphql
tags:
- code
- extension
- graphql
- graphql schema
- ide
- javascript
- schema
- visual studio code
- vs code
excerpt: Today I checked out the GraphQL extension – “VSCode GraphQL” – for Visual Studio Code. It’s available on the Marketplace @ VSCode GraphQL and of course you can navigate to plugging in VS Code and install it just like this.
image: /wp-content/uploads/2022/03/more-graphql.png
---

Today I checked out the GraphQL extension – “[VSCode GraphQL](https://github.com/graphql/vscode-graphql)” – for [Visual Studio Code](https://code.visualstudio.com/). It’s available on the Marketplace @ [VSCode GraphQL](https://marketplace.visualstudio.com/items?itemName=GraphQL.vscode-graphql) and of course you can navigate to plugging in VS Code and install it just like this.

[![](/wp-content/uploads/2022/03/extension-installation.gif.gif)](/wp-content/uploads/2022/03/extension-installation.gif.gif)

*Installing the Extension*

Once installed, setup a project by setting a simple configuration file in the root of the project. I’ve done a quick setup as follows.

[![](/wp-content/uploads/2022/03/starting-graphql-project.gif.gif)](/wp-content/uploads/2022/03/starting-graphql-project.gif.gif)

*Setting up the Project*

```
mkdir scheduling
cd scheduling
touch .gitignore
touch .graphqlrc.yml
mkdir src
cd src
touch schema.graphql
cd ..
code .
```

If you don’t like the config file named `.graphqlrc.yml` then you can change that to one of many different names, as outlined in [this doc](https://www.graphql-config.com/docs/user/user-usage).

With that done it’s now opened up in VS Code and ready for building our GraphQL Schema.

[![](/wp-content/uploads/2022/03/code-typing.gif)](/wp-content/uploads/2022/03/code-typing.gif)

*Adding the GraphQL Schema*

```
schema {
    query: Query
    mutation: Mutation
}
type Schedule {
    id: ID!
    trainName: String!
    location: String!
    order: String!
    direction: Boolean!
    arrival: String!
    departure: String!
}
type Query {
    singleSchdule(id: ID!): Schedule
}
type Mutation {
    putSchedule(id: ID!, trainName: String!, location: String!, order: String!, direction: Boolean!, arrival: String!, departure: String!): Schedule
}
```

As this code is typed out, you can see the extension providing autocomplete and the color coding. Let’s get into some of the specific features of this extension as of the latest release.

The general features involve loading up the extension upon detecting a configuration file at a root level of the project, or a parent level directory. This loads the extension so that it will work against any `.graphql` and `.gql` files. The extension also loads for any js, ts, jsx, tsx, or vue files and their respective `gql` sections, such as fenced code blocks in markdown files.

The core features include:

- syntax highlighting – type, query, mutation, interface, union, enum, scalar, fragments, and directives.
- autocomplete suggestions
- validation against schema
- snippets (interface, type, input, enum, and union)
- hover support
- go to definition support (input, enum, type)
- outline support

That’s a quick overview of that extension for Visual Studio Code, I’ll give a review of others in the near future as well as [WebStorm](https://www.jetbrains.com/webstorm/), other [JetBrains IDE](https://www.jetbrains.com/)s, and others.
