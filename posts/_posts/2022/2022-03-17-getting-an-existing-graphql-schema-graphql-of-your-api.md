---
title: Getting an Existing GraphQL `schema.graphql` of Your API
date: 2022-03-17 23:35:17 -0700
last_modified_at: 2022-03-29 17:07:02 -0700
permalink: /2022/03/17/getting-an-existing-graphql-schema-graphql-of-your-api/
slug: getting-an-existing-graphql-schema-graphql-of-your-api
wp_id: 65068
original_url: https://compositecode.blog/2022/03/17/getting-an-existing-graphql-schema-graphql-of-your-api/
categories:
- graphql
tags:
- graphql
- javascript
- json
- schema
- schema.graphql
excerpt: reason you don’t have your repo or for some reason it’s not immediately available. What to do? Here are two tools to get a quick schema of your GraphQL API by pointing them at your API and letting them introspect against it!
image: /wp-content/uploads/2022/03/haxx.png
---

Let’s say you’ve built out your GraphQL API. Now let’s say you want a schema.graphql file but for some reason you don’t have your repo or for some reason it’s not immediately available. What to do? Here are two tools to get a quick schema of your GraphQL API by pointing them at your API and letting them introspect against it!

**Prerequisite**

For both of these you’ll need to have NPM installed, which I’ll just assume you do if you’re dealing with GraphQL. If you don’t, head on out and get NPM and Node.js installed for good measure, and per my suggestion do yourself a favor and pick a version manager. I generally use nvm, check out details on install [NVM here](/2018/07/16/setting-up-a-dev-machine-for-node-js/).

**graphqurl**

Install with the following command.

```
npm install -g graphqurl
```

Now introspect!

```
gq https://some-cool-api.com/v1/graphql --introspect > schema.graphql
```

Now most, or at least many, APIs will have some type of header auth or token or something that needs passed. To do that with this issue the following.

```
gq https://some-cool-api.com/v1/graphql -H "X-Super-Secret-Secret: reallysecretAdminKeyOfSecrecy" --introspect > schema.graphql
```

**Apollo CLI**

If you’d like – or already have installed the Apollo CLI – it also has this ability. First install with this command.

```
npm install -g apollo
```

Now issue this command.

```
apollo schema:download --endpoint https://another-coolass-graphql-api.com/v1/graphql
```

Since it is all so common, throwing in a header option with this command.

```
apollo schema:download --endpoint https://another-coolass-graphql-api/v1/graphql --header "X-Secret-Is-Secret: theSecretBit"
```

Just Query It!

If you’ve got something to easily submit a GraphQL query with, you can also just submit a query like this to get all that introspected goodness!

```
query {
  __schema {
    types {
      name
      description
    }
    queryType {
      name
      description
    }
    mutationType {
      name
      description
    }
    subscriptionType {
      name
      description
      kind
    }
    directives {
      name
      description
      locations
      args {
        name
        description
        type {
          name
          description
        }
        defaultValue
      }
    }
  }
}
```

Of course this and the results you’ll have to determine yourself, adding addition fields for the different input parameters and all sorts of things, but this is a good starting point for a moderately readable response. If you want the whole thing, it’s easier to get a full dump from one of the above CLIs.

If you know of any other CLIs or apps that will pull down the schema for a GraphQL API let me know, and I’ll throw in another edit with that tool added. 👍🏻
