---
title: Java Time with Introspective GraphQL on Chaos Database AKA Pre- Refactor Prototype Mutating Database Spring Boot Java Hack App
date: 2023-12-01 17:06:11 -0800
last_modified_at: 2023-12-04 15:55:33 -0800
permalink: /2023/12/01/java-time-with-introspective-graphql-on-chaos-database-aka-pre-refactor-prototype-mutating-database-spring-boot-java-hack-app/
slug: java-time-with-introspective-graphql-on-chaos-database-aka-pre-refactor-prototype-mutating-database-spring-boot-java-hack-app
wp_id: 67033
original_url: https://compositecode.blog/2023/12/01/java-time-with-introspective-graphql-on-chaos-database-aka-pre-refactor-prototype-mutating-database-spring-boot-java-hack-app/
categories:
- Coding Adventures
- Databases
- Java
- Spring
tags:
- database
- databases
- java
- mongo
- mongodb
- spring boot
- spring data for mongo
- spring for graphql
excerpt: The developer discusses building a GraphQL API against a Mongo database in Java with a Spring stack. Starting with a prerequisite setup in Java 17 and Spring 3, they create a basic “Hello World” app for initialization. The API functionality is expanded by adding configurations for error handling and testing. The process includes adding application properties and a GraphQL schema. Code is then written for a basic QueryResolver class, before diving into more complex queries to retrieve available MongoDB collections. The post also highlights potential for future refactoring to improve scalability.
image: /wp-content/uploads/2023/11/CleanShot-2023-11-30-at-15.47.18.gif
---

With the [previous work to get a testing environment built and running done (in Python)](/2023/10/31/fruit-and-snakes-frequent-mutative-mongo-user-database-with-python/), I was ready to get started on the GraphQL API as previously described. As a refresher, this description,

> singular mission to build a GraphQL API against a Mongo database where the idea is, one could query the underlying collections, documents, and fields with the assumption that users would be adding or possibly removing said collections, documents, and fields as they needed.

My intent is to build with with a [Java](https://www.java.com/en/) + [Spring](https://spring.io/) stack. Just like with the Python app in the previous post, the first thing I like to do is just get the baseline GraphQL API “Hello World” app up and running.

At the end of this post I’ll include/link the Github repository.

## Phase 1: Getting the Initial GraphQL API Compiling & Running with a “Hello World”.

[![](/wp-content/uploads/2023/11/image.png)](/wp-content/uploads/2023/11/image.png)

### Prerequisites & Setup

- The post previous to this “[Fruit and Snakes: Frequent Mutative Mongo User Database with Python](/2023/10/31/fruit-and-snakes-frequent-mutative-mongo-user-database-with-python/)” I created the Mongo Database and setup the app that would create, every few seconds, new collections, documents, and other collateral to put into a Mongo database for the sole purpose of creating this GraphQL API.
- I’ll be using Java 17 for this work, so to ensure the least risk of versioning issues, get Java 17. The same goes for Spring 3. I’ve shown my selections from the Spring Initializr (not using Intellij? Cool, get a start with the [Spring Initializr Site](https://start.spring.io/;)) in the screenshots that follow.

[![](/wp-content/uploads/2023/11/CleanShot-2023-11-16-at-19.54.15.png)](/wp-content/uploads/2023/11/CleanShot-2023-11-16-at-19.54.15.png)

[![](/wp-content/uploads/2023/11/CleanShot-2023-11-30-at-11.36.54.png)](/wp-content/uploads/2023/11/CleanShot-2023-11-30-at-11.36.54.png)

At the end of this post I’ll include/link the Github repository.

Next I add the configuration and schema. The GraphQL schema goes in the /src/main/java/resources/graphql directory. I named the file specifically `schema.graphqls` and added the following. NOTE: The file, by convention of GraphQL for Spring is named schema.graphqls.

```graphql
type Query {
    hello: String
}
```

Next up I want to add two configuration sections to the `application.properties` file. First I always, add a section to turn off the white labeling as a precursor to setting up proper error handling but also so that any errors that pop up don’t start off as covered up white label pages. Second is the GraphiQL interface to make it easy to test out the API once it is up and running.

```yaml
server.error.whitelabel.enabled=false
server.error.include-stacktrace=always
server.error.include-message=always
server.error.include-binding-errors=always

spring.graphql.graphiql.enabled=true
spring.graphql.graphiql.path=graphiql
```

If you’re familiar with Spring Boot and the convention based approach combined with attribute based annotations, dependency injection, and all of that then a lot of this and the respective \*magic\* that happens makes sense. For example, the above two file; the *schema.graphqls* and the *application.properties* files are used to spin up the respective configuration and other dependency injected elements of the application without any need to codify their inception. It is all happening and connected behind the scenes. As I move through this material I’ll make a point to describe some of those inner workings – but if anything isn’t clear, leave a comment and I’ll elaborate and update the post with further details. In some cases, I may write up a whole additional post just to make sure I’ve covered all the details to understand all that Spring Boot \*magic\*.

### Writing the First Code

The first code that I have in the project is the *FruitCollectorApplication* class, annotated with *@SpringBootApplication* as the main method starting point. This won’t need changed and can be left as the starting point of the API. Upon this initial setup that code looks like this.

```java
package com.orchard.fruitcollector;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class FruitcollectorApplication {

    public static void main(String[] args) {
        SpringApplication.run(FruitcollectorApplication.class, args);
    }

}
```

To get the most basic of things running, next I’ll get a QueryResolver class written up. This class will get annotated with @Controller to designate it will be the core controller of the API, and I’ll add a hello() method annotated with the @QueryMapping attribute. This will map this method to the hello query in the GraphQL Schema.

```java
package com.orchard.fruitcollector;

import org.springframework.graphql.data.method.annotation.QueryMapping;
import org.springframework.stereotype.Controller;

@Controller
public class QueryResolver {

    @QueryMapping
    public String hello() {
        return "Hello World!";
    }
}
```

With that, I can now execute the API and everything should build, and I can spin up GraphiQL via [http://localhost:8080/graphiql](http://localhost:8080/graphiql?path=/graphql).

[![](/wp-content/uploads/2023/11/CleanShot-2023-11-30-at-12.31.20-1.png)](/wp-content/uploads/2023/11/CleanShot-2023-11-30-at-12.31.20-1.png)

## Phase 2: Writing Up Basic GraphQL Queries for Mongo with Spring

At the end of this post I’ll include/link the Github repository.

The first query that I want is a query that will return a list of the available collections. It’ll connect to the particular database Mongo and return the collections in that particular database. So no need for any parameters passed in or other criteria, just a clean “up “*give me everything*” query. The first addition I’ll make before any code, is to add the query type in the GraphQL schema. The full schema for the app now looks like this:

```json
type Query {
    hello: String
    collections: [String]
}
```

Implementing the query map will then follow this flow. First, add the @QueryMapping annotated method of `public List<String> collections() {}` and add the appropriate import `import java.util.List;` for that method. Next add an `Iterable<String>` object to receive the Mongo Template `getCollectionNames();` results.

[![](/wp-content/uploads/2023/11/CleanShot-2023-11-30-at-15.47.18.gif)](/wp-content/uploads/2023/11/CleanShot-2023-11-30-at-15.47.18.gif)

In the animated video I use the refactoring and code generation options in Intellj to put together the `MongoTemplate` field, constructor code that builds the field all from the collections method implementation. Intellij is super useful like that. Altogether the additional code in the QueryResolve looks like this, with the hello method included for completeness.

```
package com.orchard.fruitcollector;

import org.springframework.data.mongodb.core.MongoTemplate;
import org.springframework.graphql.data.method.annotation.QueryMapping;
import org.springframework.stereotype.Controller;

import java.util.ArrayList;
import java.util.List;

@Controller
public class QueryResolver {

    private MongoTemplate mongoTemplate;

    public QueryResolver(MongoTemplate mongoTemplate) {
        this.mongoTemplate = mongoTemplate;
    }

    @QueryMapping
    public String hello() {
        return "Hello World!";
    }

    @QueryMapping
    public List<String> collections() {
        Iterable<String> mongoCollection = mongoTemplate.getCollectionNames();

        List<String> collections = new ArrayList<>();
        for (String collectionName : mongoCollection) {
            collections.add(collectionName);
        }
        return collections;
    }
}
```

The last addition, is to add the connection string to the properties file of the project. In the application.properties file add the following line for the Mongo Database. Of course, replace “root” and “examplepass” and “test” with your respective user, password, and database to access in Mongo.

```yaml
spring.data.mongodb.uri=mongodb://root:examplepass@localhost:27017/test
```

That is all that is needed for implementation. However, know full well a solid refactor and abstraction of this code into various layers to keep the code manageable, scalable for ongoing implementation, and related criteria needs to be done. This is, an \*example\* at most that I’m building out to get started with this API. More on refactoring to something that is better ready for deployment as I move on – so keep reading.

With the implementation in place, the collections query and results against the database available via the [Fruit and Snakes: Frequent Mutative Mongo User Database with Python](/2023/10/31/fruit-and-snakes-frequent-mutative-mongo-user-database-with-python/) looks something like this.

[![](/wp-content/uploads/2023/11/CleanShot-2023-11-30-at-16.23.33.gif)](/wp-content/uploads/2023/11/CleanShot-2023-11-30-at-16.23.33.gif)

The next query I want is something that will just give the the document results of a collection. No paging just the full results. A simple enough request, the schema addition would look like `docsByCollectionName(collectionName: String!): [String]` for the GraphQL Schema. The complete schema now looks like this.

```json
type Query {
    hello: String
    collections: [String]
    docsByCollectionName(collectionName: String!): [String]
}
```

For the Java implementation there is a new element I need to add for this method, a parameter! This is easily done with marking the parameter with an `@Argument` attribute. The method would then follow the flow that the previous method I wrote did.

```java
@QueryMapping
public List<String> docsByCollectionName(@Argument String collectionName) {
    List<String> documents = new ArrayList<>();

    MongoCollection<Document> collection = mongoTemplate.getCollection(collectionName);
    FindIterable<Document> docs = collection.find();

    for (Document doc : docs) {
        documents.add(doc.toString());
    }

    return documents;
}
```

In this method, I’ve used the MongoCollection<Document> to store documents, but then still copy that, by toString, over to the documents object to return.

[![](/wp-content/uploads/2023/12/CleanShot-2023-12-01-at-01.03.46.gif)](/wp-content/uploads/2023/12/CleanShot-2023-12-01-at-01.03.46.gif)

As you can see in the short vid, the query now grabs the document results and you get the raw strings returned for processing via the API call.

### Thoughts & Strategy

At this point I’ll add a few more query calls just to provide a few options on how to query and what ways to use Spring to get these queries. However, I want to dive into some of the concepts and issues around querying against a Mongo DB instance like this.

1. ***Data Query Execution Time***: As you might have noticed in some of the queries already created, they lazy execute. You initiate the “query” but then setup the criteria of the query and then it executes. Because of the convention based approach to Spring for GraphQL and Spring Data for Mongo it isn’t immediately clear when the query is going to be executed. It’s however safe to assume that the query is generally executing upon the beginning of the manipulation of the results. It isn’t always the case, but it is often the case that this initiates the query to get the results. This specific tenant of operation for the particular libraries is important to note for troubleshooting purposes and also reasoning about building criteria and executing the queries within the code itself.
2. REGEX Efficiency in Mongo: Regular expressions in Mongo are a special and very powerful tool. Regular express / REGEX are very powerful to start with, albeit often considered cryptic and difficult to deal with. However with Mongo, since there isn’t particularly a schema or where clauses to work with for queries, it is often desirable to use something like regex to query against cumbersome – or disparate Mongo Documents. The documents themselves, being they don’t hold to a schema could hold any number of elements and using Regex to query agains the full document itself can be a life saver when one doesn’t know a specific field or element of a document to query for. Implementation details on regex a little later in the post.
3. One very significant problem with querying a Mongo database as I am doing in this particular scenario is that GraphQL’s features and specification capabilities aren’t really used. The data consumer must know the collection, field, or other part fo the document to query against and its exact spelling. Where as, GraphQL per specification should have objects, nested objects, types, and related elements one would query against defined in the schema. In this particular API however that isn’t available. Ideally the API system would be able to dynamically update the schema but that is cumbersome and shifts functionality to an infrastructure level, breaching separation of concerns and introducing difficulty that often isn’t easily overcome in organizations. i.e. the skills aren’t always available or time available to the team to design around this complexity and build a respective solution.

Alright, just a few thoughts at this point, onward to the last few method/query implementations and I’ll wrap up this post.

## Phase 3: The final Query Methods: Search String, Regex, & By Field

At the end of this post I’ll include/link the Github repository.

Next query is the `docsBySearchString` query. I’ll add the query to the GraphQL Schema, which gives me a complete schema that looks like this.

```json
type Query {
    hello: String
    collections: [String]
    docsByCollectionName(collectionName: String!): [String]
    docsBySearchString(collectionName: String!, fieldToSearch: String!, searchString: String!): [String]
}
```

Implementing that back on the Java side would then look like this. This method will now return results based on a string being found in a particular field.

```java
@QueryMapping
public List<String> docsBySearchString(@Argument String searchString, @Argument String collectionName, @Argument String fieldToSearch) {

    MongoCollection<Document> collection = mongoTemplate.getCollection(collectionName);

    Document query = new Document("$or", Arrays.asList(new Document(fieldToSearch, searchString)));

    FindIterable<Document> result = collection.find(query);

    List<String> documents = new ArrayList<>();
    for (Document doc : result) {
        documents.add(doc.toString());
    }

    return documents;
}
```

Next up is the regular expressions. This is a powerful query as regex can cover a wide range of functionality for the query. The GraphQL Schema with this addition would now look like this.

```json
type Query {
    hello: String
    collections: [String]
    docsByCollectionName(collectionName: String!): [String]
    docsBySearchString(collectionName: String!, fieldToSearch: String!, searchString: String!): [String]
    docsByRegex(collectionName: String!, fieldToSearch: String!, regex: String!): [String]
}
```

The Java side would look like this.

```java
@QueryMapping
public List<String> docsByRegex(@Argument String regex, @Argument String collectionName, @Argument String fieldToSearch) {

    MongoCollection<Document> collection = mongoTemplate.getCollection(collectionName);

    Document query = new Document("$or", Arrays.asList(regex(fieldToSearch, regex, "i")));

    FindIterable<Document> result = collection.find(query);

    List<String> documents = new ArrayList<>();
    for (Document doc : result) {
        documents.add(doc.toString());
    }

    return documents;
}
```

Finally, I’ll wrap this up with a query by field. The completed schema now includes all of these queries.

```java
type Query {
    hello: String
    collections: [String]
    docsByCollectionName(collectionName: String!): [String]
    docsBySearchString(collectionName: String!, fieldToSearch: String!, searchString: String!): [String]
    docsByRegex(collectionName: String!, fieldToSearch: String!, regex: String!): [String]
    docsFindByField(collectionName: String!, fieldToFind: String!): [String]
}
```

Flipping over to the Java side I’ve got this for implementation.

```java
@QueryMapping
public List<String> docsFindByField(@Argument String collectionName, @Argument String fieldToFind) {
    List<String> documents = new ArrayList<>();

    MongoCollection<Document> collection = mongoTemplate.getCollection(collectionName);

    Document query = new Document(fieldToFind, new Document("$exists", true));

    FindIterable<Document> result = collection.find(query);

    for (Document doc : result ) {
        documents.add(doc.toString());
    }

    return documents;
}
```

## Summary

In summary I’ve now got a GraphQL API that queries against this Mongo database. As the database collections change or new collections are added I can easily query against those and get new documents. In addition, in regular Mongo fashion if the document schemas change I can simply query against them in whatever particular way they’ve changed and get results.

## Coming Soon!

The next steps in this project will be to clean up, appropriately refactor with abstractions to help move the project to the next stage. For example, refactoring the singular controller class. Possibly adding a service class that handles the database connection and retrieval of things from the database, to make it database independent at the API controller level could be a good refactoring. There are many other things I could do, and many I should do. But for now, this is a functional API of basic capability and I’ll work up the refactor and additional GraphQL API additions in another post.

The Repo [dyna-fruity-collector Github Repository](https://github.com/Adron/dyna-fruity-collector)
