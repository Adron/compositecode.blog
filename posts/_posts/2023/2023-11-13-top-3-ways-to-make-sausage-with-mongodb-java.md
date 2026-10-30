---
title: Top 3 Ways to Make Sausage with MongoDB & Java
date: 2023-11-13 16:12:11 -0800
last_modified_at: 2023-11-14 12:50:42 -0800
permalink: /2023/11/13/top-3-ways-to-make-sausage-with-mongodb-java/
slug: top-3-ways-to-make-sausage-with-mongodb-java
wp_id: 67078
original_url: https://compositecode.blog/2023/11/13/top-3-ways-to-make-sausage-with-mongodb-java/
categories:
- Databases
- Java
tags:
- coding
- data access
- databases
- java
- mongo
- mongodb
- mongodb java driver
- morphia
- spring data
- spring data for mongodb
excerpt: 'The text presents a detailed comparison between 3 popular Java libraries for accessing MongoDB: MongoDB Java Driver, Morphia, and Spring Data MongoDB, offering insights into their usability and relevance. The MongoDB Java Driver provides direct access to MongoDB for native-like interaction. Morphia is an Object-Document Mapper designed for easy code readability and maintenance. For Spring ecosystem users, Spring Data MongoDB allows for a seamless integration with MongoDB. The choice of library is largely dependent on individual project requirements and comfort with Java and MongoDB.'
image: /wp-content/uploads/2023/11/specialist-coffee-shop-a-coffee-machine-making-co-2022-03-04-02-42-25-utc.jpg
---

I’ve been working with Java a ton this year, more so than the previous years, so I decided to put together the top three Java libraries for accessing MongoDB that I’ve been using. That top 3 list shapes up like this.

1. **MongoDB Java Driver**: This is the official Java driver provided by MongoDB. It allows Java applications to connect to MongoDB and work with data. The driver supports synchronous and asynchronous interaction with MongoDB and provides a rich set of features for database operations.
   - **Key Methods**:
     - `MongoClients.create()`: To create a new client connection to the database.
     - `MongoDatabase.getCollection()`: To access a collection from the database.
     - `MongoCollection.find()`: To find documents within a collection.
2. **Morphia**: Morphia is an Object-Document Mapper (ODM) for MongoDB and Java. It provides a higher-level, object-oriented API to interact with MongoDB, and maps Java objects to MongoDB documents.
   - **Key Methods**:
     - `Datastore.createQuery()`: To create a query for the type of entity you want to retrieve.
     - `Datastore.save()`: To save an entity to the database.
     - `Query.asList()`: To execute a query and get the results as a list.
3. **Spring Data MongoDB**: Part of the larger Spring Data project, Spring Data MongoDB provides integration with MongoDB to work with the data as easily as if it were a relational database. It’s a popular choice for Spring-based applications.
   - **Key Methods**:
     - `MongoRepository.findAll()`: To find all documents in a collection.
     - `MongoRepository.save()`: To save a given entity.
     - `MongoRepository.findById()`: To find a document by its ID.

These libraries offer comprehensive methods for connecting to and working with MongoDB from Java applications. They are widely used in the Java community and are supported by a large number of developers and organizations. Let’s dive deeper with each, and also more specifically talk about some of their respective query methods.

## A Guide to Using the MongoDB Java Driver

A simple diagram of the MongoDB Java Driver interactions.

[![](/wp-content/uploads/2023/11/image-1.png)](/wp-content/uploads/2023/11/image-1.png)

1. **MongoClient**: Represents the MongoClient instance, which is the entry point to interact with the database.
2. **MongoDatabase**: This is an instance of MongoDatabase, representing a specific database in MongoDB.
3. **MongoCollection**: Represents a collection within the database, where documents are stored.
4. **Operations**: This includes various operations that can be performed on the collections, such as:
   - CRUD Operations: Create, Read, Update, and Delete operations on documents.
   - Aggregation: Operations for aggregating data.
   - Index Management: Operations for managing indexes on collections.

The arrows indicate the flow of interaction, starting from the MongoClient instance to the database, then to the collections, and finally to the operations performed on these collections.

### Prerequisites

Before we start, ensure you have the following:

1. **Java Development Kit (JDK)**: Make sure Java is installed on your system.
2. **MongoDB Server**: Install and run MongoDB on your local machine or use a cloud-based MongoDB service.
3. **IDE for Java**: Any modern IDE like IntelliJ IDEA, Eclipse, or NetBeans.

### Step 1: Setting Up Your Project

First, create a new Java project in your IDE. You’ll need to add the MongoDB Java Driver to your project. If you’re using Maven, add the following dependency to your `pom.xml`:

```xml
<dependency>
    <groupId>org.mongodb</groupId>
    <artifactId>mongodb-driver-sync</artifactId>
    <version>YOUR_DESIRED_VERSION</version>
</dependency>
```

Replace `YOUR_DESIRED_VERSION` with the latest version of the MongoDB Java Driver.

### Step 2: Establishing a Connection to MongoDB

Create a new Java class and set up a connection to MongoDB:

```java
import com.mongodb.client.MongoClients;
import com.mongodb.client.MongoClient;
import com.mongodb.client.MongoDatabase;

public class MongoDBExample {
    public static void main(String[] args) {
        MongoClient mongoClient = MongoClients.create("mongodb://localhost:27017");
        MongoDatabase database = mongoClient.getDatabase("yourDatabaseName");
        // Rest of the code goes here
    }
}
```

Replace `yourDatabaseName` with the name of your database.

### Step 3: Querying for a List of Collections

To retrieve a list of collections from the database:

```java
import com.mongodb.client.MongoIterable;

// Inside the main method
MongoIterable<String> collections = database.listCollectionNames();
for (String collectionName : collections) {
    System.out.println(collectionName);
}
```

### Step 4: Retrieving Documents from a Collection

To fetch documents from a specific collection:

```java
import com.mongodb.client.MongoCollection;
import org.bson.Document;

// Inside the main method
MongoCollection<Document> collection = database.getCollection("yourCollectionName");
MongoIterable<Document> documents = collection.find();
for (Document doc : documents) {
    System.out.println(doc.toJson());
}
```

Replace `yourCollectionName` with the name of your collection.

### Step 5: Filtering Documents Based on Field Values

To filter documents based on specific field values:

```java
import com.mongodb.client.model.Filters;

// Inside the main method
MongoIterable<Document> filteredDocuments = collection.find(Filters.eq("fieldName", "value"));
for (Document doc : filteredDocuments) {
    System.out.println(doc.toJson());
}
```

Replace `fieldName` and `value` with the field you want to filter by and its corresponding value.

## A Guide to Using Morphia for MongoDB in Java

[![](/wp-content/uploads/2023/11/image-2.png)](/wp-content/uploads/2023/11/image-2.png)

1. **Datastore (Datastore Instance)**: This is the central part of the Morphia driver, managing the connection to the MongoDB database and providing the API for accessing and manipulating data.
2. **Entity (Entity Classes)**: These are Java classes that represent the documents stored in MongoDB. They are annotated to map the class fields to document fields.
3. **Mapper (Mapper)**: Responsible for converting the Java objects (entities) to MongoDB documents and vice versa. It interprets the annotations in the entity classes to perform this mapping.
4. **Query (Query Operations)**: This represents the operations available for querying the database, such as finding documents, filtering, and sorting.
5. **Update Operations**: These are operations that modify existing documents in the database, including updating fields, adding new data, or removing existing data.

The arrows indicate the interaction flow, with the Datastore instance being the central component that interacts with entity classes and the mapper. The entity classes are then used in query and update operations.

### Prerequisites

Before diving in, ensure you have:

1. **Java Development Kit (JDK)**: Java should be installed on your system.
2. **MongoDB Server**: Install MongoDB locally or use a cloud-based service.
3. **IDE for Java**: Use an IDE like IntelliJ IDEA, Eclipse, or NetBeans.
4. **Maven**: For managing project dependencies.

### Step 1: Setting Up Your Project

Create a new Java project in your IDE. Add Morphia and MongoDB Java Driver dependencies to your `pom.xml`:

```xml
<dependencies>
    <dependency>
        <groupId>dev.morphia.morphia</groupId>
        <artifactId>core</artifactId>
        <version>LATEST_VERSION</version>
    </dependency>
    <dependency>
        <groupId>org.mongodb</groupId>
        <artifactId>mongodb-driver-sync</artifactId>
        <version>MONGODB_DRIVER_VERSION</version>
    </dependency>
</dependencies>
```

Replace `LATEST_VERSION` and `MONGODB_DRIVER_VERSION` with the latest versions of Morphia and MongoDB Java Driver, respectively.

### Step 2: Configuring Morphia

Create a new Java class for your application. First, set up Morphia and connect it to your MongoDB instance:

```java
import dev.morphia.Datastore;
import dev.morphia.Morphia;
import com.mongodb.client.MongoClients;

public class MorphiaExample {
    public static void main(String[] args) {
        var morphia = new Morphia();
        morphia.mapPackage("your.entity.package"); // Replace with your package name

        Datastore datastore = morphia.createDatastore(MongoClients.create(), "yourDatabaseName");
        datastore.ensureIndexes();
        // Rest of the code goes here
    }
}
```

Replace `your.entity.package` with the package containing your entity classes and `yourDatabaseName` with the name of your database.

### Step 3: Querying for a List of Collections

Morphia doesn’t provide a direct method to list collections. You can use the underlying MongoDB Java Driver:

```java
// Inside the main method
for (String collectionName : datastore.getDatabase().listCollectionNames()) {
    System.out.println(collectionName);
}
```

### Step 4: Retrieving Documents from a Collection

Assuming you have a mapped entity class, you can retrieve documents as follows:

```java
import dev.morphia.query.Query;

// Inside the main method
Query<YourEntityClass> query = datastore.find(YourEntityClass.class);
for (YourEntityClass entity : query.iterator()) {
    System.out.println(entity);
}
```

Replace `YourEntityClass` with your Morphia entity class.

### Step 5: Filtering Documents Based on Field Values

To filter documents based on field values:

```java
// Inside the main method
Query<YourEntityClass> filteredQuery = datastore.find(YourEntityClass.class)
                                                 .filter(Filters.eq("fieldName", "value"));
for (YourEntityClass entity : filteredQuery.iterator()) {
    System.out.println(entity);
}
```

Replace `fieldName` and `value` with the field you want to filter by and its corresponding value.

## A Guide to Spring Data for MongoDB

[![](/wp-content/uploads/2023/11/image-4.png)](/wp-content/uploads/2023/11/image-4.png)

1. **Repository (Repository Interface)**: This is the interface layer where data access and manipulation methods are defined. It abstracts the underlying data access technology.
2. **MongoTemplate**: This is the central class of the Spring Data MongoDB module. It simplifies the use of MongoDB operations like save, query, update, and delete.
3. **Converter (Converters)**: These are used to convert objects to MongoDB documents and vice versa. They handle the mapping of Java objects to MongoDB’s BSON format.
4. **Entity (Entity Classes)**: These are domain model classes that represent the data in the MongoDB database. They are typically annotated with Spring Data annotations to map them to MongoDB documents.
5. **Query (Query Methods)**: These methods are part of the repository interface and are used to define queries for accessing the data. They can be custom methods or derived from the method names.

The arrows indicate the interaction flow. The MongoTemplate interacts with both the repository interface and converters. The repository interface uses entity classes and defines query methods, while converters are used to map entity classes to MongoDB documents.

### Prerequisites

Before starting, ensure you have:

1. **Java Development Kit (JDK)**: Java should be installed on your system.
2. **MongoDB Server**: Install MongoDB locally or use a cloud-based service.
3. **Spring Boot**: Familiarity with Spring Boot is helpful.
4. **Maven or Gradle**: For managing project dependencies.

### Step 1: Setting Up Your Spring Boot Project

Create a new Spring Boot project. You can use [Spring Initializr](https://start.spring.io/) to generate a project with the necessary dependencies. Select Web, MongoDB, and Lombok (optional for reducing boilerplate code).

### Step 2: Adding Dependencies

Ensure your `pom.xml` (if using Maven) includes Spring Data MongoDB dependency:

```xml
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-data-mongodb</artifactId>
</dependency>
```

If you’re using Gradle, add the equivalent dependency in your `build.gradle`.

### Step 3: Configuring Application Properties

In your `application.properties` or `application.yml`, add the MongoDB connection details:

```properties
spring.data.mongodb.uri=mongodb://localhost:27017/yourDatabaseName
```

Replace `yourDatabaseName` with the name of your MongoDB database.

### Step 4: Creating a Document Class

Create a class that represents a document in your MongoDB collection:

```java
import org.springframework.data.annotation.Id;
import org.springframework.data.mongodb.core.mapping.Document;

@Document
public class YourEntity {
    @Id
    private String id;

    // other fields, getters, and setters
}
```

Replace `YourEntity` with the name of your entity class.

### Step 5: Creating a Repository Interface

Spring Data MongoDB uses the repository pattern. Create an interface for your entity:

```java
import org.springframework.data.mongodb.repository.MongoRepository;

public interface YourEntityRepository extends MongoRepository<YourEntity, String> {
    // Custom query methods can be defined here
}
```

Replace `YourEntity` with your entity class.

### Step 6: Querying for a List of Collections

Spring Data MongoDB doesn’t provide a direct method to list collections from the `MongoRepository`. You can use `MongoTemplate` for this purpose:

```java
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.mongodb.core.MongoTemplate;

public class YourService {

    @Autowired
    private MongoTemplate mongoTemplate;

    public List<String> getCollections() {
        return mongoTemplate.getCollectionNames();
    }
}
```

### Step 7: Retrieving Documents from a Collection

Use the repository to fetch documents:

```java
@Autowired
private YourEntityRepository repository;

public List<YourEntity> getAllDocuments() {
    return repository.findAll();
}
```

### Step 8: Filtering Documents Based on Field Values

Spring Data allows defining query methods in the repository interface:

```java
List<YourEntity> findByYourFieldName(String value);
```

Replace `YourFieldName` with the field name and `value` with the value you’re filtering by.

# Review: MongoDB Access Methods – Java Driver, Morphia, and Spring Data MongoDB

In the realm of Java development, accessing MongoDB can be achieved through various methods, each with its unique flavor and capabilities. Let’s dive into a comparative review of three popular methods: the MongoDB Java Driver, Morphia, and Spring Data MongoDB, channeling the insightful and pragmatic style of Adron Hall.

## MongoDB Java Driver

**Direct and Unabashed:** The MongoDB Java Driver is the official, straight-from-the-source solution. It’s akin to speaking the native tongue of MongoDB, offering the most direct interaction with the database. This driver is for those who appreciate the unvarnished truth of working directly with MongoDB’s core features.

**Flexibility and Control:** It offers synchronous and asynchronous interactions, catering to a wide range of application needs. This level of control is a double-edged sword; it’s powerful but demands a deeper understanding of MongoDB’s workings.

**Verdict:** Ideal for purists and those who need fine-grained control over their MongoDB interactions. However, it can be verbose and complex, especially for newcomers.

## Morphia

**The Object-Oriented Comfort:** Morphia steps in as an Object-Document Mapper (ODM), bringing a familiar, object-oriented feel to MongoDB operations. It’s like having a translator who smoothly converts your Java objects into MongoDB documents and vice versa.

**Simplicity and Efficiency:** Morphia simplifies the code, making it more readable and maintainable. It’s particularly effective for those who think in terms of objects rather than database documents.

**Verdict:** Morphia is a great choice for developers who prefer a higher-level abstraction without straying too far from MongoDB’s native behavior. It’s less verbose than the Java Driver but still requires a good grasp of MongoDB’s principles.

## Spring Data MongoDB

**The Spring Ecosystem Harmony:** Spring Data MongoDB is the belle of the ball in the Spring ecosystem. It integrates MongoDB operations into the Spring framework, offering a consistent and familiar approach for those already versed in Spring.

**Abstraction and Convenience:** It abstracts much of the boilerplate code needed for MongoDB interactions. The repository pattern, in particular, is a boon for rapid development and clean code.

**Verdict:** For developers entrenched in the Spring ecosystem, this is a no-brainer. It offers the most streamlined experience, especially for CRUD operations. However, this comes at the cost of being a step removed from the direct MongoDB interactions, which might not appeal to those who prefer a hands-on approach.

## Conclusion

Choosing between the MongoDB Java Driver, Morphia, and Spring Data MongoDB depends largely on your project’s needs and your comfort level with MongoDB and Java.

- **Go with the Java Driver** if you need the full power and flexibility of MongoDB and don’t mind the complexity.
- **Choose Morphia** for a balanced approach, retaining much of MongoDB’s character while simplifying object-document mapping.
- **Opt for Spring Data MongoDB** if you’re already in the Spring ecosystem and prefer a more abstracted, convention-over-configuration approach.

Each method has its strengths and trade-offs, and the best choice varies with the specific context and requirements of your project.
