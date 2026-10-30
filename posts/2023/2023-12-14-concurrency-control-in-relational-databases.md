---
title: Concurrency Control in Relational Databases
date: 2023-12-14 12:01:15 -0800
last_modified_at: 2023-12-14 12:03:29 -0800
permalink: /2023/12/14/concurrency-control-in-relational-databases/
slug: concurrency-control-in-relational-databases
wp_id: 67382
original_url: https://compositecode.blog/2023/12/14/concurrency-control-in-relational-databases/
categories:
- Databases
tags:
- concurrency
- concurrency control
- database
- database locking
- database locks
- databases
- multiversion concurrency control
- optimistic concurrency control
- snapshot isolation
- timestamp ordering
excerpt: Concurrency control in relational databases ensures data integrity when multiple transactions happen concurrently. Various methods include locking, preventing conflicts by restricting data access; optimistic concurrency control, assuming rare conflicts and rolling back and retrying when they occur; and timestamp ordering, prioritizing transactions based on their start time. The method choice depends on the database needs and workload characteristics. Critical components of this process include proper testing, understanding, and knowledge of workloads and data interactions.
image: /wp-content/uploads/2023/12/CleanShot-2023-12-14-at-11.57.22.png
---

This is a continuation of my posts on relational databases, started [here](/2023/08/22/designing-a-relational-database-data-modeling/). Previous posts on this theme, “[Data Modeling](/2023/08/22/designing-a-relational-database-data-modeling/)“, “[Let’s Talk About Database Schema](/2023/08/29/lets-talk-about-database-schema/)“, “[The Exasperating Topic of Database Indexes](/2023/09/06/the-exasperating-topic-of-database-indexes/)“, “[The Keys & Relationships of Relational Databases](/2023/09/18/the-keys-relationships-of-relational-databases/)“, “[Relational Database Query Optimization](/2023/09/20/relational-database-query-optimization/)“, “[Normalization in Relational Databases](/2023/09/26/normalization-in-relational-databases/)“, “[Database (DB) Caching and DB Tertiary Caching](/2023/10/22/database-db-caching-and-db-tertiary-caching/)“, “[Security and Authentication in Relational Databases](/2023/12/07/security-and-authentication-in-relational-databases/)“, and [A Guide to Backup and Recovery Options for Relational Databases: Focusing on SQL Server, Oracle, MariaDB/MySQL, and PostgreSQL](/2023/12/11/a-guide-to-backup-and-recovery-options-for-relational-databases-focusing-on-sql-server-oracle-mariadb-mysql-and-postgresql/).

Concurrency control in relational databases is a fundamental concept that ensures the integrity and consistency of data when multiple transactions are occurring simultaneously.

## Real World Example

Imagine a bustling city where everyone is trying to get their tasks done efficiently and without stepping on each other’s toes. That’s what concurrency control is like in the world of relational databases. It’s all about managing the simultaneous operations on data in a way that ensures everyone gets their job done without causing chaos or data traffic jams.

In the realm of relational databases, transactions are like the citizens of our city. Each transaction wants to read, update, or delete data. Concurrency control is the set of traffic rules that governs how these transactions interact with each other. Without these rules, you’d have data inconsistencies, like two transactions trying to update the same piece of data at the same time, leading to conflicts and errors.

There are several methods to manage concurrency, each with its own pros and cons. Locking is like having traffic lights at intersections; it prevents conflicts by restricting access to data while a transaction is using it. However, just like traffic lights can cause delays, locking can lead to reduced database performance, especially if not managed well.

Another method is optimistic concurrency control. This is more like a roundabout, where transactions proceed assuming there won’t be conflicts, and if they do occur, the transactions are rolled back and retried. It’s efficient when conflicts are rare, but can be problematic when traffic is heavy.

Then there’s timestamp ordering, akin to giving each transaction a timestamp and ensuring they’re processed in that order. It’s like organizing our city’s tasks based on a schedule to avoid conflicts.

The choice of concurrency control depends heavily on the specific needs and characteristics of the database and its workload. Testing, understanding, and knowing what workloads demand and how the data interacts inbound and outbound, as well as internally to the database is key to determining the concurrency control paradigms to use.

## Looking Further into Locking

Locking, in the context of concurrency control for relational databases, as mentioned is a bit like the traffic rules of a busy city. It’s a mechanism designed to maintain order and prevent chaos when multiple transactions are trying to access and modify the same data at the same time.

Let’s start with the basics: What is locking? Imagine you’re in a library with a bunch of other people. You all want to read or write in the same book. Locking is like saying, “Hey, I’m using this book right now, so you’ll have to wait your turn.” In database terms, a lock is a mechanism that prevents concurrent transactions from accessing the same data in conflicting ways.

How does it work? There are different types of locks, but let’s focus on two main ones: shared locks and exclusive locks. A shared lock is like a bunch of people reading the same book. They can all read it at the same time without any issues. In database terms, this means multiple transactions can read the same data simultaneously.

On the other hand, an exclusive lock is like saying, “I’m writing in this book, so no one else can use it until I’m done.” This is necessary when a transaction is modifying data. It ensures that no other transaction can read or write the data until the lock is released, preventing inconsistencies and data corruption.

Now, let’s look at an example. Imagine you’re running a ticket booking system for a concert. Two people, Alice and Bob, are trying to buy the last ticket at the same time. Alice’s transaction reads the number of tickets, sees one is available, and starts the process to buy it. At the same time, Bob’s transaction also reads that one ticket is available. Without locking, both transactions could proceed, and they would both think they’ve successfully bought the last ticket — a classic case of overbooking!

Here’s where locking comes into play. When Alice’s transaction starts, it places an exclusive lock on the ticket count. Now, when Bob’s transaction tries to read the ticket count, it can’t proceed because of Alice’s lock. It has to wait. Once Alice’s transaction is complete (and the ticket count is updated to show that there are no tickets left), the lock is released. Now Bob’s transaction can read the updated data and see that, unfortunately, the concert is sold out.

## Delving into Optimistic Concurrency Control (OCC)

OCC in relational databases is like a trust-but-verify approach to managing data transactions. It’s a bit like letting skateboarders freely do their tricks in a skate park, trusting they won’t collide, but having a plan in place just in case they do.

So, what exactly is Optimistic Concurrency Control? It’s a strategy used in database systems when you expect that conflicts between transactions are rare, but you still need a way to handle them when they occur. Instead of locking resources to prevent conflicts (like in pessimistic concurrency control), OCC takes a more laid-back approach. It allows transactions to proceed without locking resources, but it checks for conflicts before committing the transactions.

How does it work? Let’s walk through the steps:

1. **Read Phase**: In this phase, a transaction reads the data but doesn’t lock it. It’s like taking a mental snapshot of the current state of the data.
2. **Process Phase**: Here, the transaction does its work, like updating records, but it still doesn’t lock anything. It’s operating under the assumption that nothing has changed since it took its snapshot.
3. **Validation Phase**: This is where the magic happens. Before the transaction is committed, the system checks to see if the data it read and modified has been changed by another transaction in the meantime. If the data is unchanged, the transaction is committed. If the data has been altered, the transaction is rolled back, and it might be retried.

Now, let’s look at an example. Imagine you’re running a social media app, and two users, Alice and Bob, are simultaneously editing their profiles. Alice changes her profile picture, and Bob updates his bio. With OCC, both transactions read the current state of their profiles and proceed to make their updates independently.

When they’re done, the system checks if the profile data for each user has been changed by someone else during their updates. Since Alice and Bob are editing different parts of their profiles, their changes don’t conflict with each other. The system allows both transactions to commit successfully.

## Timestamp Ordering Control

Timestamp Ordering Control in relational databases is like organizing a busy kitchen where every chef (transaction) gets a timestamped ticket dictating when they can cook their dish (access and modify data).

So, what is Timestamp Ordering Control? It’s a method of concurrency control in databases that uses timestamps to maintain the order of transactions. Each transaction is assigned a unique timestamp when it starts. This timestamp determines the transaction’s priority in accessing and modifying data.

How does it work? Let’s break it down:

1. **Timestamp Assignment**: When a transaction begins, it’s given a timestamp. This could be the current time or a sequence number, but the key is that it’s unique and ordered.
2. **Ordering Rules**: The database system uses these timestamps to decide the order in which transactions should access data. If one transaction has an earlier timestamp than another, it gets priority in reading and writing data.
3. **Conflict Resolution**: If a transaction tries to perform an operation that conflicts with the timestamp ordering rules (like trying to write data that has been read or written by a transaction with a newer timestamp), it’s either rolled back or made to wait, depending on the system’s design.

Here’s an example to illustrate this: Imagine a flight booking system where two customers, Alice and Bob, are trying to book the last seat on a flight. Alice starts her transaction, which gets timestamped at 10:00 AM. A moment later, Bob starts his transaction, which gets timestamped at 10:01 AM.

Alice’s transaction reads the number of seats available (finding one seat left) and proceeds to book it. Meanwhile, Bob’s transaction also reads the seat availability. However, before Bob’s transaction can book the seat, the system checks the timestamps. It sees that Alice’s earlier timestamped transaction is already booking the last seat. Therefore, Bob’s transaction is either rolled back or made to wait, depending on how the system handles such conflicts.

## Multiversion Concurrency Control (MVCC)

MVCC in relational databases is like a time machine for data. It’s a sophisticated way of handling transactions that allows multiple versions of data to coexist, enabling users to access data from different points in time.

So, what is MVCC? Imagine you’re in a museum where historical artifacts are continuously being updated and restored. MVCC allows each visitor (transaction) to see the museum (database) as it was at the time they entered, regardless of ongoing restorations (other transactions). This is achieved by maintaining different versions of data for different transactions.

How does it work? Let’s break it down:

1. **Version Creation**: When a transaction modifies data, instead of overwriting the existing data, MVCC creates a new version of that data. Each version is tagged with a timestamp or transaction ID.
2. **Non-Blocking Reads**: One of the key benefits of MVCC is that it allows read operations to occur without being blocked by write operations. When a transaction wants to read data, it gets the version of the data that was current at the time the transaction started.
3. **Consistency without Concurrency Issues**: Since each transaction sees its own consistent view of the database, MVCC effectively handles concurrency issues. Transactions can operate independently without interfering with each other.

Now, let’s consider an example. Imagine you’re running an online bookstore. Two customers, Alice and Bob, are interacting with the store at the same time. Alice is purchasing a book, while Bob is browsing the book catalog.

With MVCC, when Alice starts her transaction to purchase a book, the database creates a new version of the inventory data reflecting the reduced stock. However, Bob, who started browsing before Alice made her purchase, still sees the version of the inventory as it was when he started his browsing session. He won’t see the updated inventory until he starts a new transaction after Alice’s purchase is complete.

MVCC is particularly effective in read-heavy environments. It allows for high concurrency and performance, as readers don’t have to wait for writers and vice versa. However, he would also note that MVCC can require more storage space, as multiple versions of data need to be maintained. Additionally, there’s the overhead of cleaning up old data versions once they’re no longer needed.

In summary, Multiversion Concurrency Control is like giving each user their own personal snapshot of the database, tailored to the moment they started their transaction. It’s a powerful way to manage data in a dynamic environment, allowing for high levels of concurrency and consistent views of data, all while minimizing the conflicts and bottlenecks that can arise in traditional locking mechanisms.

## Snapshot Isolation

Snapshot Isolation in relational databases is akin to giving each user a camera to capture a moment in time, allowing them to work with that frozen moment even as the world around them continues to change.

So, what is Snapshot Isolation? It’s a concurrency control technique where each transaction works with a “snapshot” of the data as it existed at a specific point in time. This snapshot reflects the state of the database at the moment the transaction began, regardless of subsequent changes made by other transactions.

How does it work? Let’s delve into the steps:

1. **Snapshot Creation**: When a transaction starts, the database takes a snapshot of the current state of the data. This snapshot is what the transaction interacts with, rather than the live database.
2. **Independent Operations**: Transactions operate on their snapshots independently of each other. This means that a transaction does not see the changes made by other concurrent transactions.
3. **Commit Check**: When a transaction is ready to commit, the database checks to ensure that the changes it wants to make have not been made by another transaction since its snapshot was taken. If there’s a conflict, the committing transaction may be rolled back.

Consider this example: Imagine a library system where two librarians, Alice and Bob, are updating records at the same time. Alice is updating the catalog to add new books, while Bob is modifying the borrower records.

With Snapshot Isolation, when Alice starts her transaction, she gets a snapshot of the current state of the library database. She adds the new books to this snapshot. Concurrently, Bob starts his transaction and gets his own snapshot, which doesn’t include Alice’s new books since they were added after his snapshot was taken.

Alice and Bob work independently on their tasks. When they’re done, the system checks if the records they modified have been changed by other transactions since their snapshots were taken. If not, their changes are committed. If there are conflicts, one of the transactions might have to be retried.

Snapshot Isolation is great for improving performance in read-heavy databases, as it allows many readers to access data without waiting for writers. However, he would also caution that it’s not a silver bullet. Snapshot Isolation can lead to “write skew,” a type of anomaly where two transactions may make changes based on the same data, leading to inconsistent results.

In essence, Snapshot Isolation is like giving each user a personal, unchanging view of the database, allowing them to work without interference from others. It’s a powerful tool for managing concurrency, particularly in scenarios where the database is read more often than it’s written to, ensuring smooth and efficient operations.

## Summarized Concurrency Control

In the dynamic world of relational databases, managing the concurrent access of multiple transactions is akin to orchestrating a symphony with numerous musicians, each playing their own instrument. Concurrency control like the conductor’s baton, ensuring harmony and preventing discordant notes in an orchestra is how we manage our flow of data in and out of a database. It’s about striking the right balance between data integrity and system performance, much like a maestro ensuring each musician plays at the right moment. The choice of concurrency control strategy is crucial, as it can significantly impact the efficiency and reliability of database operations. It’s not just about keeping the data in tune; it’s about making the entire system perform its best.

Here’s a rundown of the specific options around concurrency control in relational databases:

- **Locking**:
  - *Shared Locks*: Allow multiple transactions to read a resource but prevent writing.
  - *Exclusive Locks*: Prevent other transactions from reading or writing a resource.
  - *Two-Phase Locking*: Expands and contracts locks in two phases to ensure serializability.
- **Optimistic Concurrency Control**:
  - *Read Phase*: Transactions read data without acquiring locks.
  - *Validation Phase*: Checks for conflicts before committing.
- **Timestamp Ordering**:
  - *Assigns Timestamps*: Each transaction gets a unique timestamp.
  - *Conflict Resolution*: Transactions are ordered and executed based on timestamps.
- **Multiversion Concurrency Control (MVCC)**:
  - *Versioning*: Maintains multiple versions of data for different transactions.
  - *Non-blocking Reads*: Allows read operations without waiting for write locks.
- **Snapshot Isolation**:
  - *Snapshot of Data*: Transactions work with a snapshot of data at a point in time.
  - *Reduced Locking Needs*: Minimizes the need for locks by working on snapshots.
- **Deadlock Detection and Resolution**:
  - *Detection Mechanisms*: Identifies deadlocks when they occur.
  - *Resolution Strategies*: Includes rolling back transactions or waiting.

Each of these methods has its unique strengths and is suited to different scenarios. The art of concurrency control lies in choosing and fine-tuning these strategies to ensure that the database performs harmoniously, efficiently handling the concurrent demands placed upon it.
