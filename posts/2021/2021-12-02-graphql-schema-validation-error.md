---
title: Apollo GraphQL Federation Schema Validation Error [Solved!]
date: 2021-12-02 11:47:17 -0800
last_modified_at: 2022-03-26 17:11:27 -0700
permalink: /2021/12/02/graphql-schema-validation-error/
slug: graphql-schema-validation-error
wp_id: 64574
original_url: https://compositecode.blog/2021/12/02/graphql-schema-validation-error/
categories:
- graphql
tags:
- apollo graphql
- error
- graphql
- javascript
- programming
- schema
- schema validation
excerpt: This is the error I’ve bumped into while working through the example for Apollo’s GraphQL Federation when setting up a subgraph API. I’ve tried several things to resolve this error including changing versions for the GraphQL library in use but that hasn’t fixed it. I’ve also got this now on MacOS, Linux, and Windows so …
image: /wp-content/uploads/2021/12/CleanShot-2021-12-02-at-11.46.08.png
---

This is the error I’ve bumped into while working through the [example for Apollo’s GraphQL Federation when setting up a subgraph API](https://www.apollographql.com/docs/federation/v2/subgraphs/). I’ve tried several things to resolve this error including changing versions for the GraphQL library in use but that hasn’t fixed it. I’ve also got this now on MacOS, Linux, and Windows so it isn’t something odd about the environment.

```
 ~/Codez/AppoloFederationCore-v2/ [main] node index.js
/Users/adronhall/Codez/AppoloFederationCore-v2/node_modules/apollo-graphql/lib/schema/buildSchemaFromSDL.js:50
        throw new GraphQLSchemaValidationError_1.GraphQLSchemaValidationError(errors);
        ^

GraphQLSchemaValidationError: Unknown directive "@entity".
    at buildSchemaFromSDL (/Users/adronhall/Codez/AppoloFederationCore-v2/node_modules/apollo-graphql/lib/schema/buildSchemaFromSDL.js:50:15)
    at buildSubgraphSchema (/Users/adronhall/Codez/AppoloFederationCore-v2/node_modules/@apollo/subgraph/dist/buildSubgraphSchema.js:26:58)
    at Object.<anonymous> (/Users/adronhall/Codez/AppoloFederationCore-v2/index.js:29:11)
    at Module._compile (node:internal/modules/cjs/loader:1095:14)
    at Object.Module._extensions..js (node:internal/modules/cjs/loader:1124:10)
    at Module.load (node:internal/modules/cjs/loader:975:32)
    at Function.Module._load (node:internal/modules/cjs/loader:816:12)
    at Function.executeUserEntryPoint [as runMain] (node:internal/modules/run_main:79:12)
    at node:internal/main/run_main_module:17:47 {
  errors: [
    GraphQLError [Object]: Unknown directive "@entity".
        at Object.Directive (/Users/adronhall/Codez/AppoloFederationCore-v2/node_modules/graphql/validation/rules/KnownDirectivesRule.js:56:29)
        at Object.enter (/Users/adronhall/Codez/AppoloFederationCore-v2/node_modules/graphql/language/visitor.js:323:29)
        at visit (/Users/adronhall/Codez/AppoloFederationCore-v2/node_modules/graphql/language/visitor.js:243:26)
        at Object.validateSDL (/Users/adronhall/Codez/AppoloFederationCore-v2/node_modules/graphql/validation/validate.js:92:22)
        at buildSchemaFromSDL (/Users/adronhall/Codez/AppoloFederationCore-v2/node_modules/apollo-graphql/lib/schema/buildSchemaFromSDL.js:48:31)
        at buildSubgraphSchema (/Users/adronhall/Codez/AppoloFederationCore-v2/node_modules/@apollo/subgraph/dist/buildSubgraphSchema.js:26:58)
        at Object.<anonymous> (/Users/adronhall/Codez/AppoloFederationCore-v2/index.js:29:11)
        at Module._compile (node:internal/modules/cjs/loader:1095:14)
        at Object.Module._extensions..js (node:internal/modules/cjs/loader:1124:10)
        at Module.load (node:internal/modules/cjs/loader:975:32)
  ]
}
```

The code I’m running is the happy path code offered in the docs.

```javascript
const { ApolloServer, gql } = require('apollo-server');
const { buildSubgraphSchema } = require('@apollo/subgraph');

const typeDefs = gql`
  type Query {
    me: User
  }

  type User @entity @key(fields: "id") {
    id: ID!
    username: String
  }
`;

const resolvers = {
  Query: {
    me() {
      return { id: "1", username: "@ava" }
    }
  },
  User: {
    __resolveReference(user, { fetchUserById }){
      return fetchUserById(user.id)
    }
  }
}

const server = new ApolloServer({
  schema: buildSubgraphSchema([{ typeDefs, resolvers }])
});

server.listen(4001).then(({ url }) => {
    console.log(`🚀 Server ready at ${url}`);
});
```

Anybody seen this? Got a fix? Do I need to add the @entity directive myself? Whatever the case the I think the documentation should point out the dependency needed if it’s just a dependency, but this reliably breaks just following the happy path.

Thoughts?

Will update this post with the resolution as I dig through troubleshooting. 👍🏻

[![](/wp-content/uploads/2021/12/image.png)](/wp-content/uploads/2021/12/image.png)

*Click to read a full size image of the response.*

**UPDATE: Dec 3rd, 2021.**

It looks like the docs were just updated incorrectly when posted and the entity directive isn’t ready for v2 just yet. Removing this directive resolves the error and we’ll need to wait until it’s added in a subsequent iteration for that capability.

Stephen Barlow ([@barlow\_vo](https://twitter.com/barlow_vo)) from Apollo responded via the Twitters, but also added a [link to the roadmap](https://github.com/apollographql/federation/blob/main/ROADMAP.md) for federation.
