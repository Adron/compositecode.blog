---
title: The Exasperating Topic of Database Indexes
date: 2023-09-06 22:29:55 -0700
last_modified_at: 2023-09-11 19:36:18 -0700
permalink: /2023/09/06/the-exasperating-topic-of-database-indexes/
slug: the-exasperating-topic-of-database-indexes
wp_id: 66690
original_url: https://compositecode.blog/2023/09/06/the-exasperating-topic-of-database-indexes/
categories:
- Databases
tags:
- building databases
- clustered index
- composite index
- database indexes
- databases
- full-text
- full-text index
- indexes
- non-clustered index
- primary index
- spatial index
- unique index
excerpt: 'The article delves into the intricacies of indexing in various relational databases: SQL Server, Oracle, MariaDB/MySQL, and PostgreSQL. Each database system’s section elucidates the creation and purpose of different index types, from primary and unique indexes to specialized ones like full-text and spatial indexes. The discussion culminates in a poignant analogy, likening database indexes to a book’s table of contents, underscoring their pivotal role in efficient data retrieval.'
image: /wp-content/uploads/2023/08/a-torn-paper-written-with-inscription-database-on-2022-11-11-21-07-02-utc.jpg
---

Previous posts on this theme, “[Designing a Relational Database – Data Modeling](/2023/08/22/designing-a-relational-database-data-modeling/)“ and “[Let’s Talk About Database Schema](/2023/08/29/lets-talk-about-database-schema/)“.

Indexes aren’t necessary right? Of course not, they’re just peripherally superficial things that sit like leaches on a database table’s column!

Ok, bad database satire aside, let’s get real. Indexes are extremely useful for a plethora of reasons. They play a crucial role in optimizing the speed of database operations, especially retrieval operations.

### Demystifying the Magic Behind Relational Database Indexes

Ever tried finding a specific recipe in a massive cookbook? Imagine if there wasn’t an index! Just as that cookbook index saves you hours of flipping through page after page, a relational database index works wonders by helping the system quickly locate rows within a table without the tedious process of examining each one.

**So, How Does This Magic Work?**

**1. Structure of the Craft:** Dive deep, and you’d find tree-like structures, be it the B-tree or its illustrious cousins – the B+ tree and B\* tree. These aren’t ordinary trees; they’re a labyrinth that efficiently guides the system to the row it seeks in a jiffy.
**2. Guiding Stars – Pointers:** Each entry in this labyrinth isn’t just a dead end. It carries a key value and – wait for it – a pointer. Think of it as a magical compass pointing directly to the treasure, or in this case, the row in the table.
**3. Supercharged Searches:** Now, imagine sifting through a library without a catalog – agonizingly slow, right? That’s how a database without an index feels. But bring in an index, and suddenly even the vastest of tables become a playground of swift searches.

**When Do You Need this Wizardry?**

- **Giant Libraries (or Tables):** The larger your table, the more glaring the need for an index.
- **Frequently Visited Aisles:** Those columns that always seem to be in the limelight during searches (`WHERE`) or parades (`ORDER BY`) – they’re your prime candidates.
- **Cross-Referencing Books:** If you’ve got columns that act like bridges (foreign keys) connecting various tables, indexing them is like adding express lanes for faster JOIN operations.

**But Magic Comes With Its Rules:**

- **Space – The Final Frontier:** Every index, while powerful, occupies its chunk of space. Sometimes a significant chunk of space!
- **Write Delays:** While reading becomes a breeze, writing can take a hit. Imagine each time you add a detail; the index, like a meticulous librarian, updates its records.
- **TLC Needed:** As data dances and shifts around, our magical index might need occasional tidying up to keep it efficient.
- **Too Much Magic?:** Just like too many cooks, having more indexes than necessary can actually backfire.
- **Pick Your Battles:** Remember, not every shelf or column needs an index. Be smart and base your decision on the needs and behavior of your visitors (queries).

**A Glimpse at Different Magical Indexes:**

- (1) **Primary Index:** It’s like the ID card given when a primary key is born.
- (2) **Unique Index:** The guardian ensuring each value remains one-of-a-kind.
- (3) **Clustered Index:** The meticulous sorter deciding the order of data in a table.
- (4) **Non-clustered Index:** The free spirit, indifferent to data order but still serving its purpose.
- (5) **Composite &** (6) **Full-text &** (7) **Spatial:** Specialized indexes for those unique needs, from multi-column data to searching words or even mapping geographical realms.

In essence, the world of relational database indexes is enchanting, turning tables into efficient havens of data retrieval. When wielded with care and understanding, this magic can make databases sing but remember to tend to them, just as a gardener would nurture their prized blooms.

Certainly! Let’s go through each index type for SQL Server and see how to implement them:

### 1. Primary Index

A primary index is automatically created when you define a primary key. The primary key enforces uniqueness for a column (or combination of columns) and ensures that no NULL values are allowed.

```
CREATE TABLE Employees (
    EmployeeID INT PRIMARY KEY,
    FirstName VARCHAR(50),
    LastName VARCHAR(50)
);
```

### 2. Unique Index

A unique index ensures that all values in the indexed column(s) are unique. While a primary key creates a unique index by default, you can also explicitly create a unique index on columns that aren’t the primary key.

```
CREATE UNIQUE INDEX idx_UniqueLastName
ON Employees (LastName);
```

### 3. Clustered Index

Each table can have only one clustered index. The data rows in the table are stored on disk in the order specified by the clustered index. If you define a primary key on a table, a clustered index is created by default (unless you specify otherwise).

```
CREATE CLUSTERED INDEX idx_ClusteredFirstName
ON Employees (FirstName);
```

### 4. Non-Clustered Index

A table can have multiple non-clustered indexes. They don’t affect the physical order of data, but rather create a separate data structure which holds the key values and pointers to the location of the data rows.

```
CREATE NONCLUSTERED INDEX idx_NonClusteredLastName
ON Employees (LastName);
```

### 5. Composite Index

A composite index includes more than one column. The order of columns in the index definition can influence performance, especially when the index is used in JOIN operations and WHERE clauses.

```
CREATE INDEX idx_Composite_FirstName_LastName
ON Employees (FirstName, LastName);
```

### 6. Full-Text Index

Full-text indexing provides capabilities for sophisticated word searches in character-based data. Before you can create a full-text index, you need to have a unique, single-column, non-null index on the table, and the table should have a full-text catalog.

First, enable and create a full-text catalog (if you haven’t already):

```
CREATE FULLTEXT CATALOG MyFullTextCatalog AS DEFAULT;
```

Then, create a full-text index:

```
CREATE FULLTEXT INDEX ON Employees(FirstName, LastName)
KEY INDEX idx_UniqueLastName
ON MyFullTextCatalog;
```

### 7. Spatial Index

Spatial indexes support spatial data types (`geometry` and `geography`). They optimize operations like spatial queries and help in quickly retrieving spatial objects based on their spatial location.

First, create a table with a spatial column:

```
CREATE TABLE SpatialTable (
    ID INT PRIMARY KEY,
    Location GEOGRAPHY
);
```

Then, create a spatial index:

```
CREATE SPATIAL INDEX idx_Spatial_Location
ON SpatialTable(Location);
```

Always remember that while indexes can significantly improve read performance, they can also slow down write operations. It’s essential to find a balance and create indexes based on the specific needs and usage patterns of your database.

Sure! Oracle databases support a variety of index types. Let’s go through each index type and see how to implement them in Oracle:

### 1. Primary Index

In Oracle, when you define a primary key constraint, a unique index is automatically created to enforce this constraint. This acts as a primary index.

```
CREATE TABLE Employees (
    EmployeeID NUMBER PRIMARY KEY,
    FirstName VARCHAR2(50),
    LastName VARCHAR2(50)
);
```

### 2. Unique Index

A unique index ensures that all values in the indexed column(s) are unique.

```
CREATE UNIQUE INDEX idx_UniqueLastName ON Employees (LastName);
```

### 3. Clustered Index

In Oracle, a clustered index is a bit different than in SQL Server. Oracle uses “index clusters” where rows of one or more tables are stored together based on key values. First, you define the cluster and then you create tables using that cluster.

```
-- Create the cluster
CREATE CLUSTER EmployeeCluster (EmployeeID NUMBER);

-- Create an index for the cluster
CREATE INDEX idx_ClusteredEmployee ON CLUSTER EmployeeCluster;

-- Create a table using the cluster
CREATE TABLE Employees (
    EmployeeID NUMBER,
    FirstName VARCHAR2(50),
    LastName VARCHAR2(50)
) CLUSTER EmployeeCluster (EmployeeID);
```

### 4. Non-Clustered Index

In Oracle, standard B-tree indexes are similar to non-clustered indexes in SQL Server.

```
CREATE INDEX idx_NonClusteredLastName ON Employees (LastName);
```

### 5. Composite Index

A composite index includes more than one column.

```
CREATE INDEX idx_Composite_FirstName_LastName ON Employees (FirstName, LastName);
```

### 6. Full-Text Index

Oracle provides the Oracle Text feature for text-based searches. To create a full-text index, you’d use the `CTX_DDL` package. But first, you’d define a standard table column of type `CLOB` or `VARCHAR2` to store the text.

```
-- Create a table with a CLOB column for text data
CREATE TABLE TextTable (
    ID NUMBER PRIMARY KEY,
    TextData CLOB
);

-- Create the full-text index
BEGIN
    CTX_DDL.CREATE_INDEX_SET('idx_TextData');
    CTX_DDL.ADD_INDEX('idx_TextData', 'TextTable', 'TextData');
END;
/
```

### 7. Spatial Index

Oracle provides spatial features through its spatial data types like `SDO_GEOMETRY`.

First, create a table with a spatial column:

```
CREATE TABLE SpatialTable (
    ID NUMBER PRIMARY KEY,
    Location SDO_GEOMETRY
);
```

Then, you’d typically insert spatial metadata for that column, and after that, you create a spatial index:

```
-- Insert metadata (This is a simplified example, actual requirements can vary)
INSERT INTO USER_SDO_GEOM_METADATA (TABLE_NAME, COLUMN_NAME, DIMINFO, SRID)
VALUES ('SpatialTable', 'Location', SDO_DIM_ARRAY(...), ...);

-- Create the spatial index
CREATE INDEX idx_Spatial_Location ON SpatialTable(Location) INDEXTYPE IS MDSYS.SPATIAL_INDEX;
```

(Note: The ellipses `...` in the spatial metadata insertion represent placeholders; you’d replace them with actual values specific to your spatial data.)

Always monitor the performance and make sure you have the right indexes for your workload. Over-indexing can have a negative impact on performance, especially during write operations.

Sure! MariaDB/MySQL supports various index types to enhance performance. Let’s explore each type:

### 1. Primary Index

When you define a primary key in MariaDB/MySQL, it automatically creates a unique index. If the storage engine is InnoDB (which is common and default in many setups), the primary key is also a clustered index.

```
CREATE TABLE Employees (
    EmployeeID INT PRIMARY KEY,
    FirstName VARCHAR(50),
    LastName VARCHAR(50)
);
```

### 2. Unique Index

A unique index ensures that all values in the indexed column(s) are unique.

```
CREATE UNIQUE INDEX idx_UniqueLastName ON Employees (LastName);
```

### 3. Clustered Index

In MariaDB/MySQL, with the InnoDB storage engine, the primary key also acts as a clustered index. Each InnoDB table has a clustered index; if you don’t define a primary key, MariaDB/MySQL creates an implicit clustered index named `GEN_CLUST_INDEX`. Thus, the clustered index is closely tied to the primary key in InnoDB.

### 4. Non-Clustered Index

This is a standard secondary index in MariaDB/MySQL.

```
CREATE INDEX idx_NonClusteredFirstName ON Employees (FirstName);
```

### 5. Composite Index

A composite index includes more than one column.

```
CREATE INDEX idx_Composite_FirstName_LastName ON Employees (FirstName, LastName);
```

### 6. Full-Text Index

MariaDB/MySQL supports full-text indexing for MyISAM tables by default, but as of MySQL 5.6 and MariaDB 10.0.5, InnoDB also supports full-text indexing.

```
-- Assuming Employees table uses the InnoDB storage engine
CREATE FULLTEXT INDEX idx_FullText_Name ON Employees (FirstName, LastName);
```

### 7. Spatial Index

MariaDB/MySQL supports spatial indexing on spatial columns for MyISAM, InnoDB (from MySQL 5.7.5), and MEMORY storage engines.

First, you need a table with a spatial column:

```
CREATE TABLE SpatialTable (
    ID INT PRIMARY KEY,
    Location GEOMETRY
);
```

Then, create the spatial index:

```
CREATE SPATIAL INDEX idx_Spatial_Location ON SpatialTable(Location);
```

When working with indexes in MariaDB/MySQL, always remember to periodically check their performance and usefulness. While they can greatly accelerate read operations, they might also add overhead to write operations. The `EXPLAIN` keyword can be handy in analyzing query execution plans and ensuring that your indexes are used effectively.

Certainly! PostgreSQL offers a variety of index types, each catering to specific use-cases. Let’s explore how to implement each type:

### 1. Primary Index

When you define a primary key in PostgreSQL, it automatically creates a unique B-tree index (which acts like a non-clustered index in some other databases).

```
CREATE TABLE Employees (
    EmployeeID SERIAL PRIMARY KEY,
    FirstName TEXT,
    LastName TEXT
);
```

### 2. Unique Index

A unique index ensures that all values in the indexed column(s) are unique.

```
CREATE UNIQUE INDEX idx_UniqueLastName ON Employees (LastName);
```

### 3. Clustered Index

In PostgreSQL, any B-tree index can be set as a clustered index. However, unlike some other RDBMSs, “clustering” in PostgreSQL doesn’t dictate the permanent physical ordering of the table. Instead, the `CLUSTER` command reorders the table’s current data; over time, as data is modified, the order will degrade. To maintain order, you would need to re-run the `CLUSTER` command periodically.

```
-- Create an index first
CREATE INDEX idx_ClusteredFirstName ON Employees (FirstName);

-- Then, set it as the clustered index
CLUSTER Employees USING idx_ClusteredFirstName;
```

### 4. Non-Clustered Index

The most common index type in PostgreSQL is the B-tree index, which acts as a non-clustered index in PostgreSQL.

```
CREATE INDEX idx_NonClusteredFirstName ON Employees (FirstName);
```

### 5. Composite Index

A composite index includes more than one column.

```
CREATE INDEX idx_Composite_FirstName_LastName ON Employees (FirstName, LastName);
```

### 6. Full-Text Index

PostgreSQL provides powerful text search capabilities using its vector space model. To enhance the performance of full-text searches, you can create an index on the `tsvector` representation of your text data.

```
-- Assuming you've a tsvector column storing the vector representation of text
ALTER TABLE Employees ADD COLUMN ts_vector_column tsvector
    GENERATED ALWAYS AS (to_tsvector('english', FirstName || ' ' || LastName)) STORED;

-- Now, create the index
CREATE INDEX idx_FullText_Name ON Employees USING gin(ts_vector_column);
```

### 7. Spatial Index

For spatial data, PostgreSQL offers the PostGIS extension which provides spatial data types and indexes.

First, ensure PostGIS is installed and enabled:

```
CREATE EXTENSION postgis;
```

Then, create a table with a spatial column:

```
CREATE TABLE SpatialTable (
    ID SERIAL PRIMARY KEY,
    Location GEOMETRY(Point, 4326)
);
```

After that, create a spatial index:

```
CREATE INDEX idx_Spatial_Location ON SpatialTable USING gist(Location);
```

Always remember that while indexes can improve query performance, they come with a cost in terms of disk space and write/update operation overhead. Regular maintenance using tools like `VACUUM` (for cleaning up and recovering space) and `REINDEX` (for rebuilding indexes) can be beneficial in PostgreSQL.

### Summary

Indexes in databases are like the table of contents in a massive book, guiding you precisely to the information you need without flipping through every page. Without them, every query would be like a tedious hunt in a dense forest, slowing down even the simplest data retrieval tasks. Leveraging indexes, databases become agile, efficient, and performance-optimized, turning potential data quagmires into smooth operations. Make your life easier in the land of databases, use indexes!
