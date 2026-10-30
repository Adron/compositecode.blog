---
title: DataLoader for GraphQL Implementations
date: 2023-06-20 07:55:00 -0700
last_modified_at: 2023-07-24 23:19:33 -0700
permalink: /2023/06/20/dataloader-for-graphql-implementations/
slug: dataloader-for-graphql-implementations
wp_id: 66263
original_url: https://compositecode.blog/2023/06/20/dataloader-for-graphql-implementations/
categories:
- .NET Bits
- graphql
- Java
- Javascript
tags:
- DataLoader
- graph
- graphql
- graphql api
- java
- javascript
- node
- node.js
- nodejs
- spring
- spring boot
excerpt: A popular library used in GraphQL implementations is called DataLoader, and in many ways the name is somewhat descriptive of its purpose. As described in the JavaScript repo for the Node.js implementation for GraphQL “DataLoader is a generic utility to be used as part of your application’s data fetching layer to provide a simplified and consistent API over various remote data sources such as databases or web services via batching and caching.” The DataLoader solvers the N+1 problem that otherwise requires a resolver to make multiple individual requests to a database (or data source, i.e. another API), resulting in inefficient and slow data retrieval. A DataLoader serves as a batching and caching layer for combining multiple requests int a single request. Grouping together identical
image: /wp-content/uploads/2023/06/CleanShot-2023-06-19-at-21.48.40.png
---

A popular library used in GraphQL implementations is called DataLoader, and in many ways the name is somewhat descriptive of its purpose. As described in the JavaScript repo for the Node.js implementation for GraphQL

> “DataLoader is a generic utility to be used as part of your application’s data fetching layer to provide a simplified and consistent API over various remote data sources such as databases or web services via batching and caching.”

The DataLoader solvers the N+1 problem that otherwise requires a resolver to make multiple individual requests to a database (or data source, i.e. another API), resulting in inefficient and slow data retrieval.

A DataLoader serves as a batching and caching layer for combining multiple requests int a single request. Grouping together identical requests and executing them more efficiently, thus minimizing the number of database or API round trips.

DataLoader Operation:

1. Create a new instance of DataLoader, specifying a batch loading function. This function would define how to load the data for a given set of keys.
2. The resolver iterates through the collection and instead of fetching the related data adds the keys for the data to be fetched to the DataLoader instance.
3. The DataLoader collects the keys and for multiple keys, deduplicates the request and executes.
4. Once the batch is executed DataLoader returns the results associating them with their respective keys.
5. The resolver can then access the response data and resolve the field or relationships as needed.

DataLoader also caches the results of the previous requests so if the same key is requested again DataLoader retrieves from cache instead of making another request. This caching further improves performance and reduces redundant fetching.

## DataLoader Implementation Examples

#### JavaScript & Node.js

The following is a basic implementation using Apollo Server of DataLoader for GraphQL.

```
const { ApolloServer, gql } = require("apollo-server");
const { DataLoader } = require("dataloader");

// Simulated data source
const db = {
  users: [
    { id: 1, name: "John" },
    { id: 2, name: "Jane" },
  ],
  posts: [
    { id: 1, userId: 1, title: "Post 1" },
    { id: 2, userId: 2, title: "Post 2" },
    { id: 3, userId: 1, title: "Post 3" },
  ],
};

// Simulated asynchronous data loader function
const batchPostsByUserIds = async (userIds) => {
  console.log("Fetching posts for user ids:", userIds);
  const posts = db.posts.filter((post) => userIds.includes(post.userId));
  return userIds.map((userId) => posts.filter((post) => post.userId === userId));
};

// Create a DataLoader instance
const postsLoader = new DataLoader(batchPostsByUserIds);

const resolvers = {
  Query: {
    getUserById: (_, { id }) => {
      return db.users.find((user) => user.id === id);
    },
  },
  User: {
    posts: (user) => {
      // Use DataLoader to load posts for the user
      return postsLoader.load(user.id);
    },
  },
};

// Define the GraphQL schema
const typeDefs = gql`
  type User {
    id: ID!
    name: String!
    posts: [Post]
  }

  type Post {
    id: ID!
    title: String!
  }

  type Query {
    getUserById(id: ID!): User
  }
`;

// Create Apollo Server instance
const server = new ApolloServer({ typeDefs, resolvers });

// Start the server
server.listen().then(({ url }) => {
  console.log(`Server running at ${url}`);
});
```

This example I created a DataLoader instance `postsLoader` using the `DataLoader` class from the `dataloader` package. I define a batch loading function `batchPostsByUserIds` that takes an array of user IDs and retrieves the corresponding posts for each user from the `db.posts` array. The function returns an array of arrays, where each sub-array contains the posts for a specific user.

In the `User` resolver I user the `load` method of DataLoader to load the posts for a user. The `load` method handles batching and caching behind the scenes, ensuring that redundant requests are minimized and results are cached for subsequent requests.

When the GraphQL server receives a query for the `posts` field of a `User` the DataLoader automatically batches the requests for multiple users and executes the batch loading function to retrieve the posts.

This example demonstrates a very basic implementation of DataLoader in a GraphQL server. In a real-world scenario there would of course be a number of additional capabilities and implementation details that you’d need to work on for your particular situation.

#### Spring Boot Java Implementation

Just furthering the kinds of examples, the following is a Spring Boot example.

First add the dependencies.

```
<dependencies>
  <!-- GraphQL for Spring Boot -->
  <dependency>
    <groupId>com.graphql-java</groupId>
    <artifactId>graphql-spring-boot-starter</artifactId>
    <version>5.0.2</version>
  </dependency>

  <!-- DataLoader -->
  <dependency>
    <groupId>org.dataloader</groupId>
    <artifactId>dataloader</artifactId>
    <version>3.4.0</version>
  </dependency>
</dependencies>
```

Next create the components and configure DataLoader.

```
import com.graphql.spring.boot.context.GraphQLContext;
import graphql.servlet.context.DefaultGraphQLServletContext;
import org.dataloader.BatchLoader;
import org.dataloader.DataLoader;
import org.dataloader.DataLoaderRegistry;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.Bean;
import org.springframework.web.context.request.WebRequest;

import java.util.List;
import java.util.concurrent.CompletableFuture;
import java.util.concurrent.CompletionStage;
import java.util.stream.Collectors;

@SpringBootApplication
public class DataLoaderExampleApplication {

  // Simulated data source
  private static class Db {
    List<User> users = List.of(
        new User(1, "John"),
        new User(2, "Jane")
    );

    List<Post> posts = List.of(
        new Post(1, 1, "Post 1"),
        new Post(2, 2, "Post 2"),
        new Post(3, 1, "Post 3")
    );
  }

  // User class
  private static class User {
    private final int id;
    private final String name;

    User(int id, String name) {
      this.id = id;
      this.name = name;
    }

    int getId() {
      return id;
    }

    String getName() {
      return name;
    }
  }

  // Post class
  private static class Post {
    private final int id;
    private final int userId;
    private final String title;

    Post(int id, int userId, String title) {
      this.id = id;
      this.userId = userId;
      this.title = title;
    }

    int getId() {
      return id;
    }

    int getUserId() {
      return userId;
    }

    String getTitle() {
      return title;
    }
  }

  // DataLoader batch loading function
  private static class BatchPostsByUserIds implements BatchLoader<Integer, List<Post>> {
    private final Db db;

    BatchPostsByUserIds(Db db) {
      this.db = db;
    }

    @Override
    public CompletionStage<List<List<Post>>> load(List<Integer> userIds) {
      System.out.println("Fetching posts for user ids: " + userIds);
      List<List<Post>> result = userIds.stream()
          .map(userId -> db.posts.stream()
              .filter(post -> post.getUserId() == userId)
              .collect(Collectors.toList()))
          .collect(Collectors.toList());
      return CompletableFuture.completedFuture(result);
    }
  }

  // GraphQL resolver
  private static class UserResolver implements GraphQLResolver<User> {
    private final DataLoader<Integer, List<Post>> postsDataLoader;

    UserResolver(DataLoader<Integer, List<Post>> postsDataLoader) {
      this.postsDataLoader = postsDataLoader;
    }

    List<Post> getPosts(User user) {
      return postsDataLoader.load(user.getId()).join();
    }
  }

  // GraphQL configuration
  @Bean
  public GraphQLSchemaProvider graphQLSchemaProvider() {
    return (graphQLSchemaBuilder, environment) -> {
      // Define the GraphQL schema
      GraphQLObjectType userObjectType = GraphQLObjectType.newObject()
          .name("User")
          .field(field -> field.name("id").type(Scalars.GraphQLInt))
          .field(field -> field.name("name").type(Scalars.GraphQLString))
          .field(field -> field.name("posts").type(new GraphQLList(postObjectType)))
          .build();

      GraphQLObjectType postObjectType = GraphQLObjectType.newObject()
          .name("Post")
          .field(field -> field.name("id").type(Scalars.GraphQLInt))
          .field(field -> field.name("title").type(Scalars.GraphQLString))
          .build();

      GraphQLObjectType queryObjectType = GraphQLObjectType.newObject()
          .name("Query")
          .field(field -> field.name("getUserById")
              .type(userObjectType)
              .argument(arg -> arg.name("id").type(Scalars.GraphQLInt))
              .dataFetcher(environment -> {
                // Retrieve the requested user ID
                int userId = environment.getArgument("id");
                // Fetch the user by ID from the data source
                Db db = new Db();
                return db.users.stream()
                    .filter(user -> user.getId() == userId)
                    .findFirst()
                    .orElse(null);
              }))
          .build();

      return graphQLSchemaBuilder.query(queryObjectType).build();
    };
  }

  // DataLoader registry bean
  @Bean
  public DataLoaderRegistry dataLoaderRegistry() {
    DataLoaderRegistry dataLoaderRegistry = new DataLoaderRegistry();
    Db db = new Db();
    dataLoaderRegistry.register("postsDataLoader", DataLoader.newDataLoader(new BatchPostsByUserIds(db)));
    return dataLoaderRegistry;
  }

  // GraphQL context builder
  @Bean
  public GraphQLContext.Builder graphQLContextBuilder(DataLoaderRegistry dataLoaderRegistry) {
    return new GraphQLContext.Builder().dataLoaderRegistry(dataLoaderRegistry);
  }

  public static void main(String[] args) {
    SpringApplication.run(DataLoaderExampleApplication.class, args);
  }
}
```

This example I define the `Db` class as a simulated data source with `users` and `posts` lists. I create a `BatchPostsByUserIds` class that implements the `BatchLoader` interface from DataLoader for batch loading of posts based on user IDs.

The `UserResolver` class is a GraphQL resolver that uses the `postsDataLoader` to load posts for a specific user.

For the configuration I define the schema using `GraphQLSchemaProvider` and create `GraphQLObjectType` for `User` and `Post`, and `Query` object type with a resolver for the `getUserById` field.

The `dataLoaderRegistry` bean registers the `postsDataLoader` with the DataLoader registry.

This implementation will efficiently batch and cache requests for loading posts based on user IDs.

## References

- Github Repository: [graphql/dataloader](https://github.com/graphql/dataloader)
- [Using DataLoader in GraphQL](https://oliha.dev/articles/using-dataloader-in-graphql/#0-what-is-dataloader)
- [GraphQL.NET’s implementation of DataLoader](https://graphql-dotnet.github.io/docs/guides/dataloader/)
- [Strawberry DataLoader (.NET)](https://strawberry.rocks/docs/guides/dataloaders)
- [GraphQL for Spring Java DataLoaders](https://docs.spring.io/spring-graphql/docs/current/reference/html/#execution.batching.dataloader)

## Other GraphQL Standards, Practices, Patterns, & Related Posts

- [GraphQL Pagination with Java Spring Boot’s “GraphQL for Spring”](/2023/06/23/graphql-pagination-with-java-spring-boots-graphql-for-spring/)
- [GraphQL Schema Standards, Patterns, & Practices](/2023/07/24/graphql-schema-standards/)
- [Single Responsibility Principle for GraphQL API Resolvers](/2023/06/19/single-responsibility-principle-for-graphql-api-resolvers/)
- [GraphQL Error Handling](/2023/06/17/graphql-error-handling/)
