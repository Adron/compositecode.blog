---
title: GraphQL Error Handling
date: 2023-06-17 23:11:24 -0700
last_modified_at: 2023-07-24 23:19:59 -0700
permalink: /2023/06/17/graphql-error-handling/
slug: graphql-error-handling
wp_id: 66406
original_url: https://compositecode.blog/2023/06/17/graphql-error-handling/
categories:
- graphql
tags:
- error handling
- graphql
- graphql api
- graphql error handling
- graphql patterns
- graphql practices
- graphql standards
excerpt: The following post is based on some of the common error handling techniques I’ve seen in use when implementing GraphQL APIs. The following examples include; Objects in the Response. Union Types. Middleware Custom Error Types Extensions Bubbling & Partial Results To elaborate, a basic definition of each of these follows with a slightly deeper dive into the details of each example.
image: /wp-content/uploads/2023/07/data4.jpg
---

The following post is based on some of the common error handling techniques I’ve seen in use when implementing GraphQL APIs. The following examples include;

1. Objects in the Response.
2. Union Types.
3. Middleware
4. Custom Error Types
5. Extensions
6. Bubbling & Partial Results

To elaborate, a basic definition of each of these follows with a slightly deeper dive into the details of each example.

## Error Objects in the Response

GraphQL allows you to define an error object structure within the response payload. When an error occurs during the execution of a GraphQL query, you can include relevant error information such as error codes, messages, and additional data in the response. This approach ensures that clients receive detailed error information and can handle errors appropriately.

It’s important to note that the approaches to error handling in GraphQL can vary depending on the specific GraphQL implementation or framework being used. These approaches are not mutually exclusive and can be combined to fit the needs of a particular application or organization. In JavaScript, an example of an error object in a GraphQL response might look like this:

```
{
  "data": null,
  "errors": [
    {
      "message": "Invalid argument value",
      "locations": [
        {
          "line": 3,
          "column": 7
        }
      ],
      "path": [
        "user",
        "name"
      ],
      "extensions": {
        "code": "INVALID_ARGUMENT",
        "details": {
          "minLength": 5,
          "maxLength": 20
        }
      }
    }
  ]
}
```

In this example, the response object has a `data` field set to `null` indicating that there was an error during the execution of the query. The `errors` field is an array containing an object representing the specific error that occurred.The error object includes the following properties:

- `message`: A human-readable error message describing the issue.
- `locations`: An array indicating the location of the error within the GraphQL query. Each location object contains the `line` and `column` where the error occurred.
- `path`: An array representing the field path that caused the error. It helps identify the specific field that generated the error.
- `extensions`: An optional field that can include additional information about the error. In this example, it includes the `code` field with a custom error code (`INVALID_ARGUMENT`) and a `details` object with specific details related to the error.

Please note that the structure and specific properties of error objects can vary depending on the GraphQL server implementation or framework being used. The example provided above showcases a common structure used to convey error information in a GraphQL response.

## Union Types for Errors

GraphQL supports union types, which allow you to define a type that can represent multiple possible types. You can leverage this feature to create a union type that includes both successful responses and error responses. By defining such a type, clients can anticipate and handle errors as part of the normal response flow.

In GraphQL, a union type allows you to define a type that can represent multiple possible types. It’s a way to indicate that a field in a response can have different types of values. This concept is useful for error handling when you want to include both successful responses and error responses in the same field.To create a union type for errors, you can define a new GraphQL type that represents an error and include it as one of the possible types within the union type. This allows the field to return either a successful response or an error response, depending on the situation.Here’s an example to illustrate this concept further:

```
union ResponseType = SuccessResponse | ErrorResponse

type SuccessResponse {
  data: String
}

type ErrorResponse {
  error: String
}
```

In this example, the `ResponseType` is a union type that can represent either a `SuccessResponse` or an `ErrorResponse`. The `SuccessResponse` type has a `data` field that holds the successful response data, while the `ErrorResponse` type has an `error` field that contains the error message. Now, let’s say you make a GraphQL query and receive a response in JavaScript using this union type:

```
{
  "data": {
    "responseField": {
      "__typename": "SuccessResponse",
      "data": "Some data"
    }
  }
}
```

In this example response, the `responseField` returns a `SuccessResponse` object. The `__typename` field indicates the specific type of the returned value. Here, it is set to `"SuccessResponse"`. Along with the `data` field containing the successful response data.Now, let’s consider an example where an error occurs:

```
{
  "data": {
    "responseField": {
      "__typename": "ErrorResponse",
      "error": "An error occurred"
    }
  }
}
```

In this case, the `responseField` returns an `ErrorResponse` object. The `__typename` field is set to `"ErrorResponse"`, and the `error` field contains the error message. By utilizing a union type for errors, the client can anticipate the possible response types and handle both successful responses and error responses accordingly. It provides a unified way to structure and handle different types of responses within the same field.

## Error Middleware

Middleware functions can be used in GraphQL servers to intercept and handle errors before they reach the resolver functions. Error middleware can perform tasks such as logging errors, transforming error messages, or enriching error data. It provides a centralized way to handle errors and can be customized based on specific application requirements.

Error middleware in the context of GraphQL refers to a mechanism where middleware functions are used to intercept and handle errors before they reach the resolver functions. It allows you to centralize error handling logic and perform tasks such as logging errors, transforming error messages, or enriching error data. Error middleware sits between the incoming request and the execution of the resolver functions, providing an opportunity to handle errors at a higher level.

In JavaScript, when implementing error middleware for a GraphQL server, you can use middleware functions provided by frameworks such as Express or Apollo Server. These middleware functions are executed in the order they are registered, allowing you to define custom error handling logic.Here’s an example of how error middleware could be implemented in JavaScript using Express:

```
const express = require('express');
const { ApolloServer, gql } = require('apollo-server-express');

// Define your GraphQL schema
const typeDefs = gql`
  type Query {
    hello: String
  }
`;

// Define your resolvers
const resolvers = {
  Query: {
    hello: () => {
      throw new Error('Something went wrong!');
    },
  },
};

// Create an ApolloServer instance
const server = new ApolloServer({ typeDefs, resolvers });

// Create an Express application
const app = express();

// Register error middleware
app.use((err, req, res, next) => {
  // Handle the error and send a custom error response
  res.status(500).json({ message: 'Internal Server Error' });
});

// Apply the Apollo Server middleware to the Express app
server.applyMiddleware({ app });

// Start the server
app.listen({ port: 4000 }, () => {
  console.log(`Server running at http://localhost:4000${server.graphqlPath}`);
});
```

In this example, we define a simple GraphQL schema with a single `hello` query that always throws an error. The error middleware function is registered using `app.use()` in Express. It takes four parameters: `err`, `req`, `res`, and `next`. When an error occurs during the execution of a resolver, the error middleware is invoked with the error object (`err`), the request object (`req`), the response object (`res`), and the `next` function.Inside the error middleware function, you can handle the error as per your requirements. In this example, we simply send a custom error response with a status code of 500 and a JSON payload containing an error message. By using error middleware, you can implement custom error handling logic, such as logging errors to a central system, translating error messages based on the client’s preferred language, or modifying the error response structure. This approach helps centralize error handling and keeps the resolver functions focused on their core responsibilities.

## Custom Error Types

GraphQL allows you to define custom scalar types, object types, and enum types. Similarly, you can define custom error types that encapsulate specific error scenarios in your application. By utilizing custom error types, you can provide more structured error responses, including standardized fields like error codes, error messages, and additional metadata.

Custom error types in GraphQL refer to defining your own error-specific types that encapsulate specific error scenarios in your application. By creating custom error types, you can provide more structured error responses, including standardized fields like error codes, error messages, and additional metadata.To define a custom error type in GraphQL, you can extend the built-in `Error` type or create a new object type specifically for handling errors. By extending the `Error` type, you inherit its fields and can add custom fields and metadata specific to your application’s error handling needs. Here is an example to illustrate the concept of custom error types in GraphQL:

```
type CustomError implements Error {
  code: String!
  message: String!
  additionalData: JSON
}

type Query {
  getUser(id: ID!): User
}

type User {
  id: ID!
  name: String!
}
```

In this example, we define a custom error type called `CustomError`, which implements the built-in `Error` interface. The `CustomError` type includes fields such as `code`, `message`, and `additionalData`. These fields provide standardized information about the error, such as an error code, an error message, and any additional data that might be relevant to the error.Now, let’s consider an example of implementing a custom error type in JavaScript using a resolver function:

```
const { ApolloServer, gql, ApolloError } = require('apollo-server');

// Define your GraphQL schema
const typeDefs = gql`
  type Query {
    getUser(id: ID!): User
  }

  type User {
    id: ID!
    name: String!
  }
`;

// Define your resolvers
const resolvers = {
  Query: {
    getUser: (_, { id }) => {
      if (id !== '1') {
        throw new ApolloError('User not found', 'USER_NOT_FOUND', {
          invalidId: id,
        });
      }

      return { id: '1', name: 'John Doe' };
    },
  },
};

// Create an ApolloServer instance
const server = new ApolloServer({ typeDefs, resolvers });

// Start the server
server.listen().then(({ url }) => {
  console.log(`Server running at ${url}`);
});
```

In this example, we define a resolver for the `getUser` query. If the provided `id` is not `'1'`, we throw an `ApolloError` with a custom error message and additional metadata (`invalidId`). The `ApolloError` is a pre-defined error class provided by Apollo Server that allows you to create custom errors.By throwing a custom error, we can leverage the error handling mechanisms in GraphQL and ensure that the client receives structured error responses. The client can then handle these errors based on the provided error code, message, and additional data. Using custom error types helps maintain consistency in error responses, allows for better error categorization, and provides a clear structure for conveying error information to clients consuming your GraphQL API.

## Error Extensions

GraphQL allows extensions to be added to the response payload. You can leverage this feature to include additional information with error responses. For example, you can include debugging information, stack traces, or links to relevant documentation within the response extensions. This approach enhances the debugging experience and provides developers with valuable context when troubleshooting issues.

In the context of GraphQL, error extensions refer to a mechanism that allows you to include additional information or metadata with error responses. It extends the standard error response by providing a way to attach custom fields or data to the error object. Error extensions are particularly useful for enriching the error response with debugging information, stack traces, or links to relevant documentation.When an error occurs during the execution of a GraphQL query, you can include an `extensions` field within the error object to provide additional data specific to that error. This field can contain any JSON-serializable data, allowing you to customize the error response with relevant information for debugging or error handling purposes.Here’s an example to illustrate the concept of error extensions in GraphQL:

```
{
  "data": null,
  "errors": [
    {
      "message": "Invalid argument value",
      "locations": [
        {
          "line": 3,
          "column": 7
        }
      ],
      "path": [
        "user",
        "name"
      ],
      "extensions": {
        "code": "INVALID_ARGUMENT",
        "details": {
          "minLength": 5,
          "maxLength": 20
        }
      }
    }
  ]
}
```

In this example, the error response includes an `extensions` field within the error object. The `extensions` field contains custom data related to the error, such as an error code (`code`) and specific details (`details`) about the error, such as the minimum and maximum length allowed for the argument value.Now, let’s consider an example of implementing error extensions in JavaScript:

```
// Define your GraphQL schema
const typeDefs = gql`
  type Query {
    getUser(id: ID!): User
  }

  type User {
    id: ID!
    name: String!
  }
`;

// Define your resolvers
const resolvers = {
  Query: {
    getUser: (_, { id }) => {
      if (id !== '1') {
        const error = new Error('User not found');
        error.extensions = {
          code: 'USER_NOT_FOUND',
          invalidId: id,
        };
        throw error;
      }

      return { id: '1', name: 'John Doe' };
    },
  },
};

// Create an ApolloServer instance
const server = new ApolloServer({ typeDefs, resolvers });

// Start the server
server.listen().then(({ url }) => {
  console.log(`Server running at ${url}`);
});
```

In this example, within the resolver function for the `getUser` query, we create a custom error using the `Error` class. We then attach the error extensions by assigning a custom `extensions` object to the `error.extensions` property. In this case, the extensions include an error code (`code`) and the `invalidId` that caused the error. By utilizing error extensions, you can enrich the error response with custom fields or metadata that provides additional context to clients consuming your GraphQL API. Clients can access and utilize these extensions to enhance error handling, error logging, or for implementing specific error-related behaviors in their applications.

## Error Bubbling and Partial Results

GraphQL supports error bubbling, which means that even if errors occur during the execution of a query, the server can continue executing the remaining parts of the query and return a partial result. This allows clients to receive as much data as possible while still being aware of the occurred errors. By leveraging this behavior, clients can handle partial results gracefully and make informed decisions based on the available data.

Error bubbling refers to the propagation of errors through the GraphQL resolver chain. When an error occurs in a resolver, it can be propagated up to higher-level resolvers or the root resolver. This allows for a hierarchical error handling approach, where errors can be caught and processed at different levels of the resolver hierarchy. By bubbling up errors, you can handle and modify the error response based on the specific context or requirements of each resolver.

Partial results, in the context of GraphQL, refer to the concept of returning a mixture of successfully resolved data and errors in a single response. When executing a GraphQL query, if an error occurs during the resolution of a field, it doesn’t necessarily mean the entire query execution should fail. Partial results allow you to still return the successfully resolved data while indicating the presence of errors in the response. This enables clients to process and display the available data while being aware of any errors that occurred during the query execution.Here’s an example in JavaScript to demonstrate error bubbling and partial results in GraphQL:

```
// Define your GraphQL schema
const typeDefs = gql`
  type Query {
    user(id: ID!): User
  }

  type User {
    id: ID!
    name: String!
    email: String!
    posts: [Post]
  }

  type Post {
    id: ID!
    title: String!
    content: String!
  }
`;

// Define your resolvers
const resolvers = {
  Query: {
    user: (_, { id }) => {
      if (id !== '1') {
        throw new Error('User not found');
      }

      return {
        id: '1',
        name: 'John Doe',
        email: 'john@example.com',
        posts: [
          { id: '1', title: 'First Post', content: 'This is the first post' },
          { id: '2', title: 'Second Post', content: 'This is the second post' },
        ],
      };
    },
  },
  User: {
    posts: (user) => {
      if (user.id !== '1') {
        throw new Error('User ID not found');
      }

      return user.posts;
    },
  },
};

// Create an ApolloServer instance
const server = new ApolloServer({ typeDefs, resolvers });

// Start the server
server.listen().then(({ url }) => {
  console.log(`Server running at ${url}`);
});
```

In this example, we have a GraphQL schema with a `user` query that retrieves user information and their associated posts. The `user` resolver throws an error if the provided `id` is not `'1'`. Similarly, the `posts` resolver for the `User` type throws an error if the user ID is not `'1'`. When executing a query like this:

```
query {
  user(id: "1") {
    id
    name
    email
    posts {
      id
      title
      content
    }
  }
}
```

The `user` resolver executes successfully and returns the user data along with the associated posts. However, if the `id` provided is not `'1'`, an error is thrown and propagated up the resolver chain. The error is then included in the response, indicating the specific error that occurred during the resolution of the field.This demonstrates error bubbling, as the error from the inner resolver propagates up to the parent resolver and eventually to the root resolver. It allows for handling errors at different levels and providing a response that includes both successfully resolved data and error information.Partial results come into play when an error occurs during the resolution of a specific field. In the example, if the user ID is not found, the `user` resolver throws an error, but the response still contains the successfully resolved fields (`id`, `name`, and `email`), indicating a partial result. Clients can handle the available data while being aware of the error in the response.

## Other GraphQL Standards, Practices, Patterns, & Related Posts

- [GraphQL Pagination with Java Spring Boot’s “GraphQL for Spring”](/2023/06/23/graphql-pagination-with-java-spring-boots-graphql-for-spring/)
- [DataLoader for GraphQL Implementations](/2023/06/20/dataloader-for-graphql-implementations/)
- [Single Responsibility Principle for GraphQL API Resolvers](/2023/06/19/single-responsibility-principle-for-graphql-api-resolvers/)
- [GraphQL Schema Standards, Patterns, & Practices](/2023/07/24/graphql-schema-standards/)
