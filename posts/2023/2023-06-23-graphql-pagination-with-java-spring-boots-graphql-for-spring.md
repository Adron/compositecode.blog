---
title: GraphQL Pagination with Java Spring Boot’s “GraphQL for Spring”
date: 2023-06-23 22:43:00 -0700
last_modified_at: 2023-07-24 23:19:19 -0700
permalink: /2023/06/23/graphql-pagination-with-java-spring-boots-graphql-for-spring/
slug: graphql-pagination-with-java-spring-boots-graphql-for-spring
wp_id: 66393
original_url: https://compositecode.blog/2023/06/23/graphql-pagination-with-java-spring-boots-graphql-for-spring/
categories:
- graphql
tags:
- graphql
- java
- pagination
- spring boot
excerpt: There are several different approaches for implementing pagination in GraphQL, and specifically with Java Spring Boot. The type of pattern to use depends on numerous factors like the size of the dataset, ordering requirements, and related performance characteristics. This post doesn’t cover the logic or details needed to determine the type of paging to use, just the options that are available. With that time to get into paging! 👊🏻
image: /wp-content/uploads/2023/07/data6.jpg
---

There are several different approaches for implementing pagination in GraphQL, and specifically with Java Spring Boot. Here are these commonly used patterns for paging in APIs:

1. Offset Pagination:
   - This pattern uses an offset and limit approach, where you specify the starting offset (number of records to skip) and the maximum number of records to return.
   - Example parameters: `offset=0 and limit=10`
2. Cursor-based Pagination:
   - This pattern uses a cursor (typically an encoded value representing a record) to determine the position in the dataset.
   - The cursor can be an ID, a timestamp, or any other value that uniquely identifies a record.
   - Example parameters: `cursor=eyJpZCI6MX0= and limit=10`
3. Page-based Pagination:
   - This pattern divides the dataset into pages, each containing a fixed number of records.
   - It uses page numbers to navigate through the dataset, typically with links or metadata indicating the previous, next, and current pages.
   - Example parameters: `page=1 and size=10`
4. Time-based Pagination:
   - This pattern uses time-based boundaries, such as a start and end timestamps, to fetch records within a specific time range.
   - It is commonly used in scenarios where the dataset is time-ordered, such as logs or social media posts.
   - Example parameters: `start_time=1621234567 and end_time=1622345678`
5. Keyset Pagination:
   - This pattern relies on ordering the dataset by one or more columns and using the column values as the paging keys.
   - Each page request includes the last record’s key from the previous page, and the API returns records greater than that key.
   - It provides efficient pagination for large datasets with indexed columns.
   - Example parameters: `last_key=12345 and limit=10`
6. Combination of Patterns:
   - You can also combine different pagination patterns based on the requirements of your API and the nature of the data being paginated.
   - For example, you might use cursor-based pagination for real-time updates and keyset pagination for efficient retrieval of large datasets.

The type of pattern to use depends on numerous factors like the size of the dataset, ordering requirements, and related performance characteristics. This post doesn’t cover the logic or details needed to determine the type of paging to use, just the options that are available. With that time to get into paging! 👊🏻

Here’s an example of how you can write – generally – a Java Spring Boot GraphQL API with paging for a “Customer” object:

1. Set up the project:
   - Create a new Spring Boot project in your preferred IDE.
   - Add the necessary dependencies to your `pom.xml` file:
     - Spring Boot Starter Web
     - Spring Boot Starter Data JPA
     - GraphQL Java Tools
     - GraphQL Java Spring Boot Starter
2. Define the Customer entity:
   - Create a new class named `Customer` with the following fields:

```
import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;

@Entity
public class Customer {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long customerId;
    private String firstName;
    private String lastName;
    private String customerDetails;
    private Integer customerAccountId;
    private Integer customerSalesId;
    private Long engId;
    private Long forgoId;

    // Constructors, getters, and setters
}
```

3. Set up the Customer repository:

- Create a new interface named `CustomerRepository` that extends `JpaRepository<Customer, Long>`.

```
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface CustomerRepository extends JpaRepository<Customer, Long> {
}
```

4. Create the GraphQL schema:

- Create a new file named `schema.graphqls` under the `resources` directory.
- Define the GraphQL schema with the required types, queries, and mutations:

```
type Customer {
  customerId: ID!
  firstName: String!
  lastName: String!
  customerDetails: String!
  customerAccountId: Int!
  customerSalesId: Int!
  engId: ID!
  forgoId: ID!
}

type Query {
  getCustomers(page: Int!): [Customer!]!
}

schema {
  query: Query
}
```

5. Implement the GraphQL resolver:

- Create a new class named `GraphQLResolver` and define the resolver methods.

```
import com.coxautodev.graphql.tools.GraphQLQueryResolver;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;

import java.util.List;

@Component
public class GraphQLResolver implements GraphQLQueryResolver {
    private final CustomerRepository customerRepository;

    @Autowired
    public GraphQLResolver(CustomerRepository customerRepository) {
        this.customerRepository = customerRepository;
    }

    public List<Customer> getCustomers(int page) {
        int pageSize = 42;
        int offset = (page - 1) * pageSize;
        return customerRepository.findAll(PageRequest.of(offset, pageSize)).getContent();
    }
}
```

6. Run the application:
   - Run the Spring Boot application.
   - Navigate to `http://localhost:8080/graphql` to access the GraphQL Playground.
7. Testing the API:
   - Use the following query in the GraphQL Playground to fetch customers with pagination:

```
query {
  getCustomers(page: 1) {
    customerId
    firstName
    lastName
    customerDetails
    customerAccountId
    customerSalesId
    engId
    forgoId
  }
}
```

Replace `page: 1` with the desired page number to retrieve different sets of customers.

---

## Page-based + Caching

Previous Page, Next Page, and Current Page Model

1. Modify the GraphQL schema:
   - Update the `getCustomers` query in the `schema.graphqls` file to include the new pagination fields:

```
type CustomerConnection {
  pageInfo: PageInfo!
  edges: [CustomerEdge!]!
}

type CustomerEdge {
  cursor: ID!
  node: Customer!
}

type PageInfo {
  startCursor: ID
  endCursor: ID
  hasPreviousPage: Boolean!
  hasNextPage: Boolean!
}

type Query {
  getCustomers(page: Int!): CustomerConnection!
}

schema {
  query: Query
}
```

2. Update the GraphQL resolver:
   - Modify the `GraphQLResolver` class to include the new pagination logic and return the `CustomerConnection` type:

```
import com.coxautodev.graphql.tools.GraphQLQueryResolver;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.domain.PageRequest;
import org.springframework.stereotype.Component;

import java.util.List;
import java.util.stream.Collectors;

@Component
public class GraphQLResolver implements GraphQLQueryResolver {
    private final CustomerRepository customerRepository;

    @Autowired
    public GraphQLResolver(CustomerRepository customerRepository) {
        this.customerRepository = customerRepository;
    }

    public CustomerConnection getCustomers(int page) {
        int pageSize = 42;
        int offset = (page - 1) * pageSize;

        List<Customer> customers = customerRepository.findAll(PageRequest.of(offset, pageSize)).getContent();
        List<CustomerEdge> customerEdges = customers.stream()
                .map(customer -> new CustomerEdge(String.valueOf(customer.getCustomerId()), customer))
                .collect(Collectors.toList());

        boolean hasPreviousPage = page > 1;
        boolean hasNextPage = customers.size() == pageSize;

        String startCursor = customerEdges.isEmpty() ? null : customerEdges.get(0).getCursor();
        String endCursor = customerEdges.isEmpty() ? null : customerEdges.get(customerEdges.size() - 1).getCursor();

        PageInfo pageInfo = new PageInfo(startCursor, endCursor, hasPreviousPage, hasNextPage);
        return new CustomerConnection(pageInfo, customerEdges);
    }
}
```

3. Define additional classes:
   - Create the following additional classes to support the new pagination model:

```
public class CustomerConnection {
    private final PageInfo pageInfo;
    private final List<CustomerEdge> edges;

    public CustomerConnection(PageInfo pageInfo, List<CustomerEdge> edges) {
        this.pageInfo = pageInfo;
        this.edges = edges;
    }

    public PageInfo getPageInfo() {
        return pageInfo;
    }

    public List<CustomerEdge> getEdges() {
        return edges;
    }
}

public class CustomerEdge {
    private final String cursor;
    private final Customer node;

    public CustomerEdge(String cursor, Customer node) {
        this.cursor = cursor;
        this.node = node;
    }

    public String getCursor() {
        return cursor;
    }

    public Customer getNode() {
        return node;
    }
}

public class PageInfo {
    private final String startCursor;
    private final String endCursor;
    private final boolean hasPreviousPage;
    private final boolean hasNextPage;

    public PageInfo(String startCursor, String endCursor, boolean hasPreviousPage, boolean hasNextPage) {
        this.startCursor = startCursor;
        this.endCursor = endCursor;
        this.hasPreviousPage = hasPreviousPage;
        this.hasNextPage = hasNextPage;
    }

    public String getStartCursor() {
        return startCursor;
    }

    public String getEndCursor() {
        return endCursor;
    }

    public boolean isHasPreviousPage() {
        return hasPreviousPage;
    }

    public boolean isHasNextPage() {
        return hasNextPage;
    }
}
```

- Inspect the `pageInfo` field to access the pagination information.
- The `edges` field contains the list of customers with their respective cursors.

---

## Offset Pagination

1. Modify the GraphQL resolver:

- Update the `getCustomers` method in the `GraphQLResolver` class to accept an additional parameter for the page size and offset:

```
import com.coxautodev.graphql.tools.GraphQLQueryResolver;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;

import java.util.List;

@Component
public class GraphQLResolver implements GraphQLQueryResolver {
    private final CustomerRepository customerRepository;

    @Autowired
    public GraphQLResolver(CustomerRepository customerRepository) {
        this.customerRepository = customerRepository;
    }

    public List<Customer> getCustomers(int pageSize, int offset) {
        return customerRepository.findAll(PageRequest.of(offset, pageSize)).getContent();
    }
}
```

2. Update the GraphQL schema:

- Modify the `getCustomers` query in the `schema.graphqls` file to include the additional parameters for page size and offset:

```
type Query {
  getCustomers(pageSize: Int!, offset: Int!): [Customer!]!
}

schema {
  query: Query
}
```

3. Run the application and test the API:

- Run the Spring Boot application.
- Use the following query in the GraphQL Playground to fetch customers with offset pagination:

```
query {
  getCustomers(pageSize: 42, offset: 0) {
    customerId
    firstName
    lastName
    customerDetails
    customerAccountId
    customerSalesId
    engId
    forgoId
  }
}
```

- Adjust the values of `pageSize` and `offset` as needed to navigate through the dataset.
- For example, to retrieve the next page, set `offset` to `42` (assuming `pageSize` is `42`).

---

## Page-based Pagination

1. Modify the GraphQL resolver:

- Update the `getCustomers` method in the `GraphQLResolver` class to accept an additional parameter for the page number and page size:

```
import com.coxautodev.graphql.tools.GraphQLQueryResolver;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.PageRequest;
import org.springframework.stereotype.Component;

@Component
public class GraphQLResolver implements GraphQLQueryResolver {
    private final CustomerRepository customerRepository;

    @Autowired
    public GraphQLResolver(CustomerRepository customerRepository) {
        this.customerRepository = customerRepository;
    }

    public Page<Customer> getCustomers(int pageNumber, int pageSize) {
        return customerRepository.findAll(PageRequest.of(pageNumber - 1, pageSize));
    }
}
```

2. Update the GraphQL schema:

- Modify the `getCustomers` query in the `schema.graphqls` file to include the additional parameters for page number and page size:

```
type CustomerConnection {
  pageInfo: PageInfo!
  edges: [CustomerEdge!]!
}

type CustomerEdge {
  cursor: ID!
  node: Customer!
}

type PageInfo {
  startCursor: ID
  endCursor: ID
  hasPreviousPage: Boolean!
  hasNextPage: Boolean!
}

type Query {
  getCustomers(pageNumber: Int!, pageSize: Int!): CustomerConnection!
}

schema {
  query: Query
}
```

3. Update the CustomerConnection and PageInfo classes:

- Modify the `CustomerConnection` and `PageInfo` classes to match the updated schema:

```
import java.util.List;

public class CustomerConnection {
    private final PageInfo pageInfo;
    private final List<CustomerEdge> edges;

    public CustomerConnection(PageInfo pageInfo, List<CustomerEdge> edges) {
        this.pageInfo = pageInfo;
        this.edges = edges;
    }

    public PageInfo getPageInfo() {
        return pageInfo;
    }

    public List<CustomerEdge> getEdges() {
        return edges;
    }
}

public class PageInfo {
    private final String startCursor;
    private final String endCursor;
    private final boolean hasPreviousPage;
    private final boolean hasNextPage;

    public PageInfo(String startCursor, String endCursor, boolean hasPreviousPage, boolean hasNextPage) {
        this.startCursor = startCursor;
        this.endCursor = endCursor;
        this.hasPreviousPage = hasPreviousPage;
        this.hasNextPage = hasNextPage;
    }

    public String getStartCursor() {
        return startCursor;
    }

    public String getEndCursor() {
        return endCursor;
    }

    public boolean isHasPreviousPage() {
        return hasPreviousPage;
    }

    public boolean isHasNextPage() {
        return hasNextPage;
    }
}
```

4. Run the application and test the API:

- Run the Spring Boot application.
- Use the following query in the GraphQL Playground to fetch customers with page-based pagination:

```
query {
  getCustomers(pageNumber: 1, pageSize: 42) {
    pageInfo {
      startCursor
      endCursor
      hasPreviousPage
      hasNextPage
    }
    edges {
      cursor
      node {
        customerId
        firstName
        lastName
        customerDetails
        customerAccountId
        customerSalesId
        engId
        forgoId
      }
    }
  }
}
```

- Adjust the values of `pageNumber` and `pageSize` as needed to navigate through the dataset.
- The response includes the `pageInfo` object, which provides information about the current page and pagination state.
- The `edges` field contains the list of customers with their respective cursors.

---

## Time-based Pagination

1. Modify the GraphQL resolver:

- Update the `getCustomers` method in the `GraphQLResolver` class to accept additional parameters for the start time, end time, and page size:

```
import com.coxautodev.graphql.tools.GraphQLQueryResolver;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;

import java.time.LocalDateTime;
import java.util.List;

@Component
public class GraphQLResolver implements GraphQLQueryResolver {
    private final CustomerRepository customerRepository;

    @Autowired
    public GraphQLResolver(CustomerRepository customerRepository) {
        this.customerRepository = customerRepository;
    }

    public List<Customer> getCustomers(LocalDateTime startTime, LocalDateTime endTime, int pageSize) {
        return customerRepository.findByTimeRange(startTime, endTime, PageRequest.of(0, pageSize));
    }
}
```

2. Update the GraphQL schema:

- Modify the `getCustomers` query in the `schema.graphqls` file to include the additional parameters for the start time, end time, and page size:

```
type Query {
  getCustomers(startTime: String!, endTime: String!, pageSize: Int!): [Customer!]!
}

schema {
  query: Query
}
```

3. Update the CustomerRepository:

- Update the `CustomerRepository` interface to include a method that queries customers within a specified time range:

```
import org.springframework.data.domain.Pageable;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;

import java.time.LocalDateTime;
import java.util.List;

public interface CustomerRepository extends JpaRepository<Customer, Long> {

    @Query("SELECT c FROM Customer c WHERE c.timestamp >= :startTime AND c.timestamp <= :endTime")
    List<Customer> findByTimeRange(LocalDateTime startTime, LocalDateTime endTime, Pageable pageable);
}
```

4. Run the application and test the API:

- Run the Spring Boot application.
- Use the following query in the GraphQL Playground to fetch customers with time-based pagination:

```
query {
  getCustomers(startTime: "2023-05-01T00:00:00", endTime: "2023-05-17T23:59:59", pageSize: 42) {
    customerId
    firstName
    lastName
    customerDetails
    customerAccountId
    customerSalesId
    engId
    forgoId
  }
}
```

- Adjust the values of `startTime`, `endTime`, and `pageSize` as needed to fetch customers within the desired time range.
- Make sure to provide valid time range values in ISO 8601 format.

---

## Keyset Pagination

1. Modify the GraphQL resolver:

- Update the `getCustomers` method in the `GraphQLResolver` class to accept additional parameters for the last key and page size:

```
import com.coxautodev.graphql.tools.GraphQLQueryResolver;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;

import java.util.List;

@Component
public class GraphQLResolver implements GraphQLQueryResolver {
    private final CustomerRepository customerRepository;

    @Autowired
    public GraphQLResolver(CustomerRepository customerRepository) {
        this.customerRepository = customerRepository;
    }

    public List<Customer> getCustomers(String lastKey, int pageSize) {
        return customerRepository.findNextCustomers(lastKey, pageSize);
    }
}
```

2. Update the GraphQL schema:

- Modify the `getCustomers` query in the `schema.graphqls` file to include the additional parameters for the last key and page size:

```
type Query {
  getCustomers(lastKey: String, pageSize: Int!): [Customer!]!
}

schema {
  query: Query
}
```

3. Update the CustomerRepository:

- Update the `CustomerRepository` interface to include a method that queries the next set of customers based on the last key:

```
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;

import java.util.List;

public interface CustomerRepository extends JpaRepository<Customer, Long> {

    @Query("SELECT c FROM Customer c WHERE c.key > :lastKey ORDER BY c.key ASC")
    List<Customer> findNextCustomers(String lastKey, int pageSize);
}
```

4. Run the application and test the API:

- Run the Spring Boot application.
- Use the following query in the GraphQL Playground to fetch customers with keyset pagination:

```
query {
  getCustomers(lastKey: "", pageSize: 42) {
    customerId
    firstName
    lastName
    customerDetails
    customerAccountId
    customerSalesId
    engId
    forgoId
  }
}
```

- Adjust the value of `pageSize` as needed to control the number of records per page.
- The `lastKey` parameter is used to retrieve the next set of customers based on the provided key. Initially, use an empty string as the `lastKey`.
- Subsequent requests can use the last key value received from the previous response to fetch the next set of customers.

Alright, with all those covered – which I mostly just put together as quickly as possible as examples – I had little time to research any of the latest or greatest ways to put these pagniation patterns together specifically with Java Spring Boot. If you’ve got pointers, suggestions, or otherwise, I’d love a critique of my general code slinging in this post. Cheers!

## Other GraphQL Standards, Practices, Patterns, & Related Posts

- [GraphQL Schema Standards, Patterns, & Practices](/2023/07/24/graphql-schema-standards/)
- [DataLoader for GraphQL Implementations](/2023/06/20/dataloader-for-graphql-implementations/)
- [Single Responsibility Principle for GraphQL API Resolvers](/2023/06/19/single-responsibility-principle-for-graphql-api-resolvers/)
- [GraphQL Error Handling](/2023/06/17/graphql-error-handling/)
