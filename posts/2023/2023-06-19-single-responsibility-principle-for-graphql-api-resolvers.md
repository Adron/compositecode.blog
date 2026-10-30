---
title: Single Responsibility Principle for GraphQL API Resolvers
date: 2023-06-19 13:00:45 -0700
last_modified_at: 2023-07-24 23:20:00 -0700
permalink: /2023/06/19/single-responsibility-principle-for-graphql-api-resolvers/
slug: single-responsibility-principle-for-graphql-api-resolvers
wp_id: 66244
original_url: https://compositecode.blog/2023/06/19/single-responsibility-principle-for-graphql-api-resolvers/
categories:
- Coding Patterns & Practices
- graphql
tags:
- clean code
- graphql
- javascript
- node
- node.js
- nodejs
- single responsibility principle
- software patterns
excerpt: The Single Responsibility Principle (SRP) states that a class or module should have only one reason to change. It emphasizes the importance of keeping modules or components focused on a single task, reducing their complexity, and increasing maintainability. SRP defined. In GraphQL API development the importance, and need, of maintaining code quality and scalability is …
image: /wp-content/uploads/2023/06/supermassive-2-star-galaxy-cosmos-physical-scien-2022-11-09-16-26-21-utc.jpg
---

> The Single Responsibility Principle (SRP) states that a class or module should have only one reason to change. It emphasizes the importance of keeping modules or components focused on a single task, reducing their complexity, and increasing maintainability.
>
> SRP defined.

In GraphQL API development the importance, and need, of maintaining code quality and scalability is of utmost importance. A powerful principle that can help achieve these goals when developing your API’s resolvers is the Single Responsibility Principle (SRP). I’m not always a die hard when it comes to SRP – there are always situations that may need to skip out on some of the concept – but in general it helps tremendously over time.

By adhering the SRP coders can more easily avoid the pitfalls of large monolithic resolvers that end up doing spurious processing outside of their intended scope. Let’s explore some of the SRP and I’ll provide three practice examples of how to implement some simple SRP use with GraphQL.

When applying SRP in GraphQL the aim is to ensure that each resolver handles a specific data type or field, thereby avoiding scope bloat and convoluted resolvers that handle unrelated responsibilities.

1. User Resolvers:
   - Imagine a scenario where a GraphQL schema includes a User type with fields like id, name, email, and posts. Instead of writing a single resolver for the User type that fetches and processes all of the data we can adopt SRP by creating separate resolvers for each field. For instance we would have resolvers.getUserById to fetch user details, resolvers.getUserName to retrieve the respective user’s name, and a resolvers.getUserPosts to fetch the user’s posts. In doing so we keep each resolver focused on a specific field and in turn keep the codebase simplified.
2. Product Resolvers:
   - Another example might be a product object within an e-commerce application. It would contain fields like is, name, price, and reviews. With SRP we’d have resolvers for resolvers.getProductById, resolvers.getProductName, resolvers.getProductPrice, and resolvers.getProductReviews. The naming, by use of SRP, can be utilized to describe what each of these functions do and what one can expect in response. This again, makes the codebase dramatically easier to maintain over time.
3. Comment Resolvers:
   - Last example, imagine a blog, with a comment type consisting of id, content, and author. This would break out to resolvers.getCommentContent, resolvers.getCommentAuthor, and resolvers.getCommentById. This adheres to SRP and keeps things simple, just like the previous two examples.

**Prerequisite**: The examples below assume the `apollo-server` and `graphql` are installed and available.

## User Resolvers Example

A more thorough working example of the user resolvers described above would look something like this. I’ve included the data in a variable to act as the database, but the inferred premise there would be an underlying database should be obvious.

```
// Assuming you have a database or data source that provides user information
const db = {
  users: [
    { id: 1, name: "John Doe", email: "john@example.com", posts: [1, 2] },
    { id: 2, name: "Jane Smith", email: "jane@example.com", posts: [3] },
  ],
  posts: [
    { id: 1, title: "GraphQL Basics", content: "Introduction to GraphQL" },
    { id: 2, title: "GraphQL Advanced", content: "Advanced GraphQL techniques" },
    { id: 3, title: "GraphQL Best Practices", content: "Tips for GraphQL development" },
  ],
};

const resolvers = {
  Query: {
    getUserById: (_, { id }) => {
      return db.users.find((user) => user.id === id);
    },
  },
  User: {
    name: (user) => {
      return user.name;
    },
    posts: (user) => {
      return db.posts.filter((post) => user.posts.includes(post.id));
    },
  },
};

// Assuming you have a GraphQL server setup with Apollo Server
const { ApolloServer, gql } = require("apollo-server");

const typeDefs = gql`
  type User {
    id: ID!
    name: String!
    email: String!
    posts: [Post!]!
  }

  type Post {
    id: ID!
    title: String!
    content: String!
  }

  type Query {
    getUserById(id: ID!): User
  }
`;

const server = new ApolloServer({ typeDefs, resolvers });

server.listen().then(({ url }) => {
  console.log(`Server running at ${url}`);
});
```

In this code we have the `db` object acting as our database that we’ll interact with. Then the `resolvers` and the GraphQL schema is included inline to show the relationship of the data and how it would love per GraphQL. For this example I’m also, for simplicity, using Apollo server to build this example.

## Product Resolvers Example

I’ve also included an example of the product resolvers. Very similar, but has some minor nuance to show how it would coded up. For this example however, to draw more context I’ve added an authors table/entity, and respective fields for authors, as per related to reviews.

```
// Assuming you have a database or data source that provides product, review, and author information
const db = {
  products: [
    { id: 1, name: "Product 1", price: 19.99, reviews: [1, 2] },
    { id: 2, name: "Product 2", price: 29.99, reviews: [3] },
  ],
  reviews: [
    { id: 1, rating: 4, comment: "Great product!", authorId: 1 },
    { id: 2, rating: 5, comment: "Excellent quality!", authorId: 2 },
    { id: 3, rating: 3, comment: "Average product.", authorId: 1 },
  ],
  authors: [
    { id: 1, name: "John Doe", karmaPoints: 100, details: "Product enthusiast" },
    { id: 2, name: "Jane Smith", karmaPoints: 150, details: "Tech lover" },
  ],
};

const resolvers = {
  Query: {
    getProductById: (_, { id }) => {
      return db.products.find((product) => product.id === id);
    },
  },
  Product: {
    name: (product) => {
      return product.name;
    },
    price: (product) => {
      return product.price;
    },
    reviews: (product) => {
      return db.reviews.filter((review) => product.reviews.includes(review.id));
    },
  },
  Review: {
    author: (review) => {
      return db.authors.find((author) => author.id === review.authorId);
    },
  },
};

// Assuming you have a GraphQL server setup with Apollo Server
const { ApolloServer, gql } = require("apollo-server");

const typeDefs = gql`
  type Product {
    id: ID!
    name: String!
    price: Float!
    reviews: [Review!]!
  }

  type Review {
    id: ID!
    rating: Int!
    comment: String!
    author: Author!
  }

  type Author {
    id: ID!
    name: String!
    karmaPoints: Int!
    details: String!
  }

  type Query {
    getProductById(id: ID!): Product
  }
`;

const server = new ApolloServer({ typeDefs, resolvers });

server.listen().then(({ url }) => {
  console.log(`Server running at ${url}`);
});
```

## Comment Resolvers Example

Starting right off with this example, here’s what the code would look like.

```
// Assuming you have a database or data source that provides comment and author information
const db = {
  comments: [
    { id: 1, content: "Great post!", authorId: 1 },
    { id: 2, content: "Nice article!", authorId: 2 },
  ],
  authors: [
    { id: 1, name: "John Doe", karmaPoints: 100, details: "Product enthusiast" },
    { id: 2, name: "Jane Smith", karmaPoints: 150, details: "Tech lover" },
  ],
};

const resolvers = {
  Query: {
    getCommentById: (_, { id }) => {
      return db.comments.find((comment) => comment.id === id);
    },
  },
  Comment: {
    content: (comment) => {
      return comment.content;
    },
    author: (comment) => {
      return db.authors.find((author) => author.id === comment.authorId);
    },
  },
};

// Assuming you have a GraphQL server setup with Apollo Server
const { ApolloServer, gql } = require("apollo-server");

const typeDefs = gql`
  type Comment {
    id: ID!
    content: String!
    author: Author!
  }

  type Author {
    id: ID!
    name: String!
    karmaPoints: Int!
    details: String!
  }

  type Query {
    getCommentById(id: ID!): Comment
  }
`;

const server = new ApolloServer({ typeDefs, resolvers });

server.listen().then(({ url }) => {
  console.log(`Server running at ${url}`);
});
```

The concept of the Single Responsibility Principle (SRP) and provided code examples using JavaScript demonstrate its application in GraphQL resolvers. The SRP advocates for keeping code modules focused on a specific data type or field, avoiding large and monolithic resolvers that handle multiple unrelated responsibilities. By adhering to the SRP, software developers can build better software that is modular, maintainable, and easier to understand. By dividing functionality into smaller, well-defined units, developers can enhance code reusability, improve testability, and promote better collaboration among team members. Embracing the SRP helps create codebases that are more scalable, extensible, and adaptable to changing requirements, ultimately leading to higher-quality software solutions.

## Other GraphQL Standards, Practices, Patterns, & Related Posts

- [GraphQL Pagination with Java Spring Boot’s “GraphQL for Spring”](/2023/06/23/graphql-pagination-with-java-spring-boots-graphql-for-spring/)
- [DataLoader for GraphQL Implementations](/2023/06/20/dataloader-for-graphql-implementations/)
- [GraphQL Schema Standards, Patterns, & Practices](/2023/07/24/graphql-schema-standards/)
- [GraphQL Error Handling](/2023/06/17/graphql-error-handling/)
