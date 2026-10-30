---
title: The Keys & Relationships of Relational Databases
date: 2023-09-18 15:46:47 -0700
last_modified_at: 2023-09-20 13:28:57 -0700
permalink: /2023/09/18/the-keys-relationships-of-relational-databases/
slug: the-keys-relationships-of-relational-databases
wp_id: 66733
original_url: https://compositecode.blog/2023/09/18/the-keys-relationships-of-relational-databases/
categories:
- Databases
tags:
- database
- database design
- database modeling
- database patterns
- design patterns
- keys
- rdbms
- relational databases
- relationships
- ruby
excerpt: Together, keys and relationships not only maintain data accuracy and consistency but also support meaningful and logical data retrieval and insights.
image: /wp-content/uploads/2023/08/alphabet-letters-and-icons-with-the-word-database-2023-08-19-06-29-47-utc.jpg
---

This is a continuation of my posts on relational databases, started [here](/2023/08/22/designing-a-relational-database-data-modeling/). Previous posts on this theme, “[Designing a Relational Database – Data Modeling](/2023/08/22/designing-a-relational-database-data-modeling/), “[Let’s Talk About Database Schema](/2023/08/29/lets-talk-about-database-schema/)“, and “[The Exasperating Topic of Database Indexes](/2023/09/06/the-exasperating-topic-of-database-indexes/)“.

In the context of relational databases, “keys” and “relationships” are fundamental concepts that help in ensuring data integrity, organizing data efficiently, and enabling meaningful data retrieval. Let’s break these down:

## 1. Keys

A key is an attribute (or a set of attributes) that uniquely identifies a record in a table. Various types of keys exist in relational databases:

- **Primary Key**: This uniquely identifies each record in a table. A primary key cannot have NULL values, and each value must be unique. A table can have only one primary key, which may consist of single or multiple columns.
- **Foreign Key**: This is an attribute or set of attributes in a table that refers to the primary key in another table. It establishes a relationship between two tables. A foreign key ensures records in one table correspond to records in another.
- **Unique Key**: Similar to a primary key, it uniquely identifies each record in the table. The difference is that a table can have more than one unique key, but only one primary key. Unique keys can have NULL values, but the values must be unique.
- **Composite Key**: When more than one attribute is used to uniquely identify a record in the table, such a key is called a composite key.
- **Candidate Key**: Any attribute or set of attributes that could serve as the primary key is a candidate key. It means it can uniquely identify records in the table.
- **Super Key**: It is a set of attributes that, when taken collectively, can be used to uniquely identify records. A super key can have additional attributes that are not strictly necessary for unique identification.

## 2. Relationships

Relationships in relational databases determine how tables connect to one another and how data correlates:

- **One-to-One (1:1) Relationship**: In this relationship, one record in a table is related to one and only one record in another table. For instance, each employee in a company might have one unique work ID.
- **One-to-Many (1:N) or Many-to-One (N:1) Relationship**: One record in a table can be related to one or more records in another table. For example, one customer can place many orders, but each order is made by one customer.
- **Many-to-Many (M:N) Relationship**: Multiple records in one table are related to multiple records in another table. For instance, students and courses. One student can enroll in many courses, and one course can have many students. This relationship is typically resolved in relational databases using a junction table (or bridge table).

Relationships are typically enforced using Foreign Keys. When a foreign key in one table refers to the primary key of another, it creates a linkage that ensures the validity of the data and maintains referential integrity.

## Purpose of Keys

1. **Uniqueness**: Keys, especially primary keys, ensure that each record in a table is uniquely identifiable. This uniqueness is crucial for precise data retrieval, ensuring that data isn’t duplicated, and for establishing relationships between tables.
2. **Data Integrity**: Through the use of keys, particularly foreign keys, the integrity of data across tables is maintained. For instance, a foreign key ensures that a reference from one table to another is always valid. It prevents orphan records or invalid references.
3. **Efficient Data Retrieval**: Keys, especially when indexed, can speed up data retrieval operations. When a database system knows that a key is unique or indexed, it can optimize search operations to quickly locate the associated record.
4. **Logical Framework**: Keys provide a framework for understanding the logical structure of a database. They often signify important attributes around which data is organized or retrieved.

## Purpose of Relationships

1. **Data Organization**: Relationships give structure to the data across different tables. Instead of keeping all data in a single, monolithic table, which could be inefficient and redundant, relationships allow data to be distributed across multiple tables while maintaining logical connections.
2. **Data Redundancy Reduction**: By establishing relationships, especially many-to-one or one-to-many, it’s possible to reduce data redundancy. For instance, instead of repeating address information for every order a customer makes, you can have a separate ‘Customers’ table and an ‘Orders’ table. Each order can then simply reference the customer, ensuring that address data isn’t repeatedly stored with every order.
3. **Referential Integrity**: Relationships, especially when enforced using foreign keys, ensure that the database’s data remains consistent and valid. For instance, if there’s a relationship between ‘Students’ and ‘Courses’, the database can prevent a situation where a course enrollment record references a non-existent student.
4. **Meaningful Data Retrieval**: Relationships enable complex and meaningful queries. For instance, you could retrieve all orders made by customers from a particular city by joining an ‘Orders’ table and a ‘Customers’ table on a shared key, and then filtering based on city.
5. **Data Insights**: The capability to relate tables and create complex queries can lead to deeper insights from the data. It becomes feasible to derive meaningful reports, analytics, and patterns when data from various tables can be logically interrelated.

In essence, keys and relationships are the backbone of a relational database, facilitating the organization of data in a structured, consistent, and efficient manner. They provide the foundation upon which complex operations, analytics, and applications are built.

Creating keys and relationships in ANSI SQL is primarily done through the use of constraints during the table creation or modification processes. Let’s delve into how to create these keys and relationships, accompanied by examples.

## 1. Keys in ANSI SQL

### Primary Key

A primary key uniquely identifies each record in a table.

```
CREATE TABLE Students (
    StudentID INT NOT NULL,
    FirstName VARCHAR(255),
    LastName VARCHAR(255),
    PRIMARY KEY (StudentID)
);
```

### Composite Key

A primary key consisting of more than one column.

```
CREATE TABLE StudentCourses (
    StudentID INT,
    CourseID INT,
    EnrollmentDate DATE,
    PRIMARY KEY (StudentID, CourseID)
);
```

### Unique Key

It ensures that all values in a column are different.

```
CREATE TABLE Users (
    UserID INT NOT NULL,
    Username VARCHAR(255) NOT NULL UNIQUE,
    Email VARCHAR(255),
    PRIMARY KEY (UserID)
);
```

## 2. Relationships in ANSI SQL

### Foreign Key

A foreign key establishes a relationship between two tables.

```
CREATE TABLE Orders (
    OrderID INT NOT NULL,
    CustomerID INT,
    OrderDate DATE,
    PRIMARY KEY (OrderID),
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID)
);
```

## Esoteric Usages of Keys and Relationships

While the above examples provide the fundamentals, there are some unique and less commonly discussed relationships and patterns in database design:

### Elephant Ear Relationship (Self-referencing relationship)

This is essentially a table that has a foreign key relationship with itself. A classic example is an Employee table where you want to capture the manager for each employee.

```
CREATE TABLE Employees (
    EmployeeID INT NOT NULL,
    FirstName VARCHAR(255),
    ManagerID INT,
    PRIMARY KEY (EmployeeID),
    FOREIGN KEY (ManagerID) REFERENCES Employees(EmployeeID)
);
```

Here, the `ManagerID` is a foreign key that references the `EmployeeID` from the same table.

### Many-to-Many Relationship

A many-to-many relationship can exist between two entities, say, Students and Courses. A student can register for many courses, and a course can have many students. This is usually resolved using a junction table.

```
CREATE TABLE StudentCourses (
    StudentID INT,
    CourseID INT,
    PRIMARY KEY (StudentID, CourseID),
    FOREIGN KEY (StudentID) REFERENCES Students(StudentID),
    FOREIGN KEY (CourseID) REFERENCES Courses(CourseID)
);
```

### Recursive Relationships

While the elephant ear relationship is a simple self-referencing table, recursive relationships can be more complex. For example, in a table capturing a hierarchical organizational structure, you might have multiple levels of self-referencing to capture the entire hierarchy.

### Polymorphic Associations

This is not a native concept in relational databases, but it’s sometimes used in application development. Polymorphic associations are a design pattern often seen in database systems, especially in the context of ORMs (Object-Relational Mapping) and certain application frameworks like Ruby on Rails. This pattern allows a model or table to belong to more than one type of related model on a single association.

The primary motivation behind polymorphic associations is to allow an entity to relate to multiple entities without requiring a separate join table for each relationship.

### Example:

Imagine you have a system where both `Articles` and `Products` can have `Comments`. Without polymorphic associations, you might need two separate tables to store comments for each: `ArticleComments` and `ProductComments`.

Using a polymorphic association, you’d have a single `Comments` table that can store comments for both `Articles` and `Products`.

The `Comments` table might look like:

| id | content | commentable\_id | commentable\_type |
| --- | --- | --- | --- |
| 1 | “Nice post!” | 5 | Article |
| 2 | “Great buy!” | 3 | Product |

In this table:

- `commentable_id` is the ID of the item being commented on (could be an `Article` ID or a `Product` ID).
- `commentable_type` specifies the type of item being commented on.

The combination of `commentable_id` and `commentable_type` gives us the context for each comment, allowing us to determine what entity the comment is related to.

### Advantages:

- \***Flexibility**: A single table (e.g., `Comments`) can be associated with multiple other tables, reducing the number of tables and relationships you need to manage.
- \***Extensibility**: If in the future you want another model (e.g., `Videos`) to also have comments, you can do so without changing the database schema. You’d simply start creating comments with `commentable_type` set to “Video”.

### Disadvantages:

- \***Complexity**: Polymorphic relationships can be harder to understand, especially for those new to the concept or the particular codebase.
- \***Loss of Foreign Key Constraints**: Traditional RDBMSs do not allow you to enforce foreign key constraints on polymorphic associations. This can lead to potential data integrity issues.
- \***Query Complexity**: Queries can become more complicated since you can’t just perform a straightforward join against a single table. Depending on the specific query, you might need conditional logic based on the `commentable_type`.

### Implementation in ORMs:

ORMs like Ruby on Rails make it easy to set up and work with polymorphic associations:class Comment < ApplicationRecord belongs\_to :commentable, polymorphic: true end class Article < ApplicationRecord has\_many :comments, as: :commentable end class Product < ApplicationRecord has\_many :comments, as: :commentable end

While polymorphic associations can be powerful and provide a clean solution for certain challenges, they should be used judiciously. Always weigh the advantages against the potential complications, especially if you’re working in an environment where database integrity and query performance are critical.

### Closure Table

This pattern is used to store hierarchical data, like a tree or a graph, in a relational database. For every ancestor-descendant relationship, an entry is made. This pattern makes certain types of queries faster but can be more complex to maintain.

These are just a few examples of the many design patterns and relationships available. Properly using these patterns can dramatically affect performance, maintainability, and scalability of a database system.

## Summary

Keys and relationships are foundational concepts in relational databases, underpinning the structure and integrity of stored data. Keys, which include primary, foreign, and unique keys, ensure each record’s uniqueness and enable efficient data retrieval. Relationships, on the other hand, define how tables connect to one another, allowing for organized data distribution and minimized redundancy. Establishing these connections involves mechanisms like one-to-one, one-to-many, and many-to-many associations, with some advanced patterns like polymorphic associations extending this foundational system. Together, keys and relationships not only maintain data accuracy and consistency but also support meaningful and logical data retrieval and insights.
