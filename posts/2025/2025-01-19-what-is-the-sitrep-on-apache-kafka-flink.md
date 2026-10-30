---
title: What is the SITREP on Apache Kafka & Flink?
date: 2025-01-19 00:50:40 -0800
last_modified_at: 2025-01-20 10:41:09 -0800
permalink: /2025/01/19/what-is-the-sitrep-on-apache-kafka-flink/
slug: what-is-the-sitrep-on-apache-kafka-flink
wp_id: 70978
original_url: https://compositecode.blog/2025/01/19/what-is-the-sitrep-on-apache-kafka-flink/
categories:
- Apache Flink
- Apache Kafka
- Apache Projects
- Industry
- Reviews
- Software Projects
- Thoughts
- Writing
tags:
- apache flink
- apache kafka
- apache projects
- apache software
excerpt: I’ve worked with (** references at end of article) a number of Apache projects over the years, often pretty closely; Apache Cassandra, Apache Flink, Apache Kafka, Apache Zookeeper and numerous others. But the last few years I’ve not been immediately hands on with the technology. A few questions popped up recently, that fortunately I was …
image: /wp-content/uploads/2025/01/kafka-flink.png
---

I’ve worked with (**\*\*** *references at end of article*) a number of Apache projects over the years, often pretty closely; Apache Cassandra, Apache Flink, Apache Kafka, Apache Zookeeper and numerous others. But the last few years I’ve not been immediately hands on with the technology. A few questions popped up recently, that fortunately I was able to answer based on existing knowledge, but it made me real curious about what the SITREP (Situational Report) is for the Apache Kafka and Flink Projects for TODAY, i.e. rolling into 2025! The following is a quick dive into the history and then the latest details (and drama?) with Apache Kafka, Flink, and tangentially some other projects (Zookeeper?).

## Apache Projects – Context & Quick Details

If you’re unfamiliar with the Apache Projects in a general sense, I highly suggest going and checking out the [Apache Project Directory](https://projects.apache.org/) and [Apache Projects List](https://projects.apache.org/projects.html). There you will find all sorts of fascinating information about the organization itself, how the projects are organized, and the trend of committees and related details. For example, I always love checking out the initial charts on retired and active that show on the directory page, as I’ve snapshotted below.

[![](/wp-content/uploads/2025/01/CleanShot-2025-01-17-at-11.23.03.png)](/wp-content/uploads/2025/01/CleanShot-2025-01-17-at-11.23.03.png)

Another favorite chart is this one, which I’ll write some thoughts on in the very near future.

[![](/wp-content/uploads/2025/01/CleanShot-2025-01-17-at-11.28.55.png)](/wp-content/uploads/2025/01/CleanShot-2025-01-17-at-11.28.55.png)

## Tangential Projects

When checking up on Kafka & Flink and getting back up to speed, I’d be remiss if I didn’t include some of the key tangential projects, here is a list with links to important projects. These are related in the sense they either are used directly with or tangentially with Kafka or Flink. (*Note: If I missed any, please leave a comment on the post and I’ll add it to this list!*)

### **Projects Related to Apache Kafka**

1. [**Apache Zookeeper**](https://zookeeper.apache.org/)

   - Role: Originally used for managing Kafka’s metadata and ensuring distributed consensus.
   - Relationship: Kafka is moving toward a Zookeeper-less architecture with the KRaft protocol, but Zookeeper remains important for legacy deployments.
2. [**Apache Kafka Connect**](https://kafka.apache.org/documentation/#connect)

   - Role: A framework for integrating Kafka with external systems (databases, cloud services, etc.).
   - Relationship: Extends Kafka’s usability by enabling easy ingestion and egress of data.
3. [**Apache Avro**](https://avro.apache.org/)

   - Role: A data serialization system often used with Kafka for schema management.
   - Relationship: Enables efficient serialization and deserialization of messages sent over Kafka topics.
4. [**Apache Camel**](https://camel.apache.org/)

   - Role: An integration framework that provides numerous connectors.
   - Relationship: Used for integrating Kafka with diverse endpoints and implementing routing logic.
5. [**Apache Storm**](https://storm.apache.org/)

   - Role: A stream processing system.
   - Relationship: While Flink has overtaken Storm in many scenarios, Storm can still work alongside Kafka in legacy pipelines.
6. [**Apache Samza**](https://samza.apache.org/)

   - Role: A stream processing framework developed by LinkedIn.
   - Relationship: Like Flink, Samza can process Kafka streams but has a more niche adoption.
7. [**Apache NiFi**](https://nifi.apache.org/)

   - Role: A data flow management system.
   - Relationship: Frequently used with Kafka to design, schedule, and monitor complex data flows.

### **Projects Related to Apache Flink**

1. [**Apache Hadoop**](https://hadoop.apache.org/)

   - Role: A distributed storage and processing framework.
   - Relationship: Flink can read and write data from/to Hadoop Distributed File System (HDFS) for batch and stream processing.
2. [**Apache Beam**](https://beam.apache.org/)

   - Role: A unified programming model for defining batch and stream processing pipelines.
   - Relationship: Flink serves as one of Beam’s execution engines, enabling portability across environments.
3. [**Apache Pulsar**](https://pulsar.apache.org/)

   - Role: A distributed messaging system and Kafka alternative.
   - Relationship: Pulsar can act as an event source for Flink, much like Kafka, and supports Flink’s connectors.
4. [**Apache Cassandra**](https://cassandra.apache.org/)

   - Role: A distributed NoSQL database.
   - Relationship: Frequently used as a sink for Flink’s stream processing jobs or as part of a pipeline originating in Kafka.
5. [**Apache Hudi**](https://hudi.apache.org/)

   - Role: A data lake framework for managing datasets stored in HDFS or cloud storage.
   - Relationship: Works well with Flink for streaming updates and incremental processing in a data lake.
6. [**Apache Iceberg**](https://iceberg.apache.org/)

   - Role: A table format for large-scale, petabyte-scale analytics.
   - Relationship: Flink integrates with Iceberg for performing stream processing on large datasets.
7. [**Apache Druid**](https://druid.apache.org/)

   - Role: A real-time analytics database.
   - Relationship: Often paired with Flink for real-time ingestion and with Kafka for data streaming into analytics workloads.
8. [**Apache Kafka Streams**](https://kafka.apache.org/documentation/streams/)

   - Role: A stream processing library for Kafka.
   - Relationship: While Flink is more powerful for complex use cases, Kafka Streams is a simpler alternative for stream processing, often compared to Flink.

### **Projects Bridging Kafka and Flink**

1. [**Apache Kafka Connectors for Flink**](https://nightlies.apache.org/flink/flink-docs-stable/docs/connectors/datastream/kafka/)

   - Flink provides native connectors for reading from and writing to Kafka, enabling seamless integration between the two systems.
2. [**Apache Flink Stateful Functions (StateFun)**](https://statefun.apache.org/)

   - A framework for building stateful applications with event-driven functions.
   - Relationship: Integrates well with Kafka for triggering stateful computations and workflows.
3. [**Apache Pinot**](https://pinot.apache.org/)

   - Role: A real-time distributed OLAP datastore.
   - Relationship: Kafka provides real-time ingestion, while Flink processes and transforms data before storing it in Pinot for analytics.

### **Complementary Tools**

1. **Schema Management:**

   - [**Apache Avro**](https://avro.apache.org/), [**Apache Parquet**](https://parquet.apache.org/), and [**Apache Arrow**](https://arrow.apache.org/) for defining and sharing schemas for Kafka and Flink pipelines.
2. **Orchestration and Management:**

   - [**Apache Airflow**](https://airflow.apache.org/) for orchestrating workflows that include Kafka and Flink jobs.
   - [**Apache Oozie**](https://oozie.apache.org/) for managing workflows, especially in Hadoop environments.
3. **Observability:**

   - [**Apache SkyWalking**](https://skywalking.apache.org/) for monitoring and analyzing the performance of distributed systems, including Kafka and Flink.

## The Latest News & History of Apache Kafka & Apache Flink

Now for getting up to speed with the latest news of where Apache Flink and Apache Kafka are. Hopefully this section of my article will provide some insight for those looking to get into or get back into using or developing for or against these technologies. The idea, this will give you some context of where the tools have been in their development path and where they are now, and where they’re headed.

- 2010
  - **Apache Flink:** Initiated as the “Stratosphere” research project, a collaboration between Technische Universität Berlin, Humboldt-Universität zu Berlin, and Hasso-Plattner-Institut Potsdam.
- 2011
  - **Apache Kafka:** Developed at LinkedIn to address scalability issues with real-time data feeds and open-sourced.
- 2012
  - **Apache Kafka:** Graduated from the Apache Incubator on October 23 and became a top-level project.
- 2014
  - **Apache Flink:** Forked from Stratosphere’s distributed execution engine and entered the Apache Incubator in March.
  - **Apache Flink:** Graduated as a top-level Apache project in December.
- 2015
  - **Apache Flink:** Released version 0.9.0 on June 24 and version 0.10.0 on November 16.
- 2016
  - **Apache Flink:** Released version 1.0.0 on March 8, introducing backward compatibility for APIs. Released version 1.1.0 on August 8.
- 2017
  - **Apache Flink:** Released versions 1.2.0 (February 6), 1.3.0 (June 1), and 1.4.0 (December 12).
  - **Apache Kafka:** Released version 1.0.0, marking its maturity as a platform.
- 2018
  - **Apache Flink:** Released versions 1.5.0 (May 25), 1.6.0 (August 8), and 1.7.0 (November 30).
- 2019
  - **Apache Flink:** Released versions 1.8.0 (April 9) and 1.9.0 (August 22).
- 20\* 20
  - **Apache Flink:** Released versions 1.10.0 (February 11), 1.11.0 (July 6), and 1.12.0 (December 10).
- 2021
  - **Apache Flink:** Released versions 1.13.0 (May 3) and 1.14.0 (September 29).
- 2022
  - **Apache Flink:** Released versions 1.15.0 (May 5) and 1.16.0 (October 28).
- 2023
  - **Apache Flink:** Released versions 1.17.0 (March 23) and 1.18.0 (October 24).
- 2024
  - **Apache Flink:** Plans for version 1.19.0 in March \* 2024 and Flink 2.0 with a disaggregated storage architecture for cloud-native capabilities.
  - **Apache Kafka:** The community continues development toward Kafka 4.0, with plans to make KRaft mode the default and remove ZooKeeper dependencies.

## 2024 Highlights

In 2024, the data streaming ecosystem witnessed significant advancements, particularly surrounding Apache Flink and Apache Kafka. These developments encompassed major software releases, influential conferences, emerging trends, and notable industry movements.

### Major Software Releases

- **Apache Flink 2.0 Preview**: Marking its first major version change in eight years, the Apache Flink community unveiled a preview of Flink 2.0 in October 2024. This release introduced innovative features and improvements, setting the stage for the future of stream processing.
- **Confluent’s Integration of Flink and Iceberg**: In March 2024, Confluent enhanced its hosted Kafka service by integrating Apache Flink and Apache Iceberg. This integration aimed to provide developers with robust tools for real-time data processing and analytics.

### Conferences and Events

- **Flink Forward Berlin 2024**: Celebrating the 10-year anniversary of Apache Flink, this conference took place from October 21-24, 2024. It featured speakers from industry leaders such as Apple, Alibaba, Mercedes-Benz, and Uber, highlighting Flink’s impact across various sectors.
- **Kafka Summit London 2024**: Held in March 2024, this summit attracted over 3,500 attendees, both in-person and online. The event showcased the latest developments in Apache Kafka, with discussions on its integration with Apache Flink and the evolving data streaming landscape.
- **Current 2024**: On September 17-18, 2024, Austin, Texas, hosted Current 2024, bringing together the data streaming community to discuss advancements in Apache Kafka and Apache Flink. The event featured insights from tech leaders and industry giants on real-time event streaming.

### Emerging Trends

The year saw several key trends shaping the data streaming domain:

- **Data Sharing and Data Contracts**: Emphasis on data sharing across business units and the implementation of data contracts became prevalent, aiming to enhance data governance and policy enforcement.
- **Serverless Stream Processing**: The adoption of serverless architectures for stream processing gained traction, offering scalability and ease of deployment for real-time applications.
- **Integration with Generative AI**: The convergence of data streaming platforms with Generative AI technologies, such as large language models, opened new avenues for intelligent data processing and analytics.

### Industry Movements

- **Confluent’s Growth**: Confluent, a key player in the data streaming industry, reported a 400% earnings growth in Q3 2024, with sales rising to $250.2 million. The company’s partnerships with tech giants like Amazon, Microsoft, and Google underscored its pivotal role in facilitating real-time data streaming and AI applications.

## Stable and Development Versions

- Apache Flink:
  - Latest Stable Version:\*\* 1.\* 20.0, released August 2, \* 2024.
  - Development Version:\*\* Flink 2.0 (preview release announced October 23, \* 2024).
- Apache Kafka:
  - Latest Stable Version:\*\* 3.8.1, released November \* 2024.
  - Development Version:\*\* Kafka 4.0 (under active development).

## References & Article Addendums

1. [Apache Flink History](https://flink.apache.org/history.html)
2. [Wikipedia: Apache Flink](https://en.wikipedia.org/wiki/Apache_Flink)
3. [The Evolution of Kafka](https://www.rtinsights.com/the-technical-evolution-of-apache-kafka-from-linkedins-need-to-a-global-standard/)
4. [Confluent’s History of Kafka](https://www.confluent.io/blog/introducing-apache-kafka/)
5. [Wikipedia: Apache Kafka](https://en.wikipedia.org/wiki/Apache_Kafka)
6. [Apache Kafka Incubator Graduation](https://blogs.apache.org/kafka/entry/apache_kafka_graduates_to_a)
7. [Flink in the Apache Incubator](https://incubator.apache.org/projects/flink.html)
8. [Apache Flink Graduation Announcement](https://blogs.apache.org/foundation/entry/apache-flink-a-graduated-project)
9. [Apache Flink 0.9.0 Release Notes](https://flink.apache.org/news/2015/06/24/release-0.9.0.html)
10. [Apache Flink 0.10.0 Release Notes](https://flink.apache.org/news/2015/11/16/release-0.10.0.html)
11. [Apache Flink 1.0.0 Announcement](https://flink.apache.org/news/2016/03/08/release-1.0.0.html)
12. [Apache Flink 1.1.0 Announcement](https://flink.apache.org/news/2016/08/08/release-1.1.0.html)
13. [Apache Flink 1.2.0 Release Notes](https://flink.apache.org/news/2017/02/06/release-1.2.0.html)
14. [Apache Flink 1.3.0 Release Notes](https://flink.apache.org/news/2017/06/01/release-1.3.0.html)
15. [Apache Flink 1.4.0 Release Notes](https://flink.apache.org/news/2017/12/12/release-1.4.0.html)
16. [Kafka 1.0.0 Release Blog](https://www.confluent.io/blog/apache-kafka-goes-1-0/)
17. [Apache Kafka Release Notes](https://kafka.apache.org/10/documentation.html)
18. [Apache Flink 1.5.0 Release Notes](https://flink.apache.org/news/2018/05/25/release-1.5.0.html)
19. [Apache Flink 1.6.0 Release Notes](https://flink.apache.org/news/2018/08/08/release-1.6.0.html)
20. [Apache Flink 1.7.0 Release Notes](https://flink.apache.org/news/2018/11/30/release-1.7.0.html)
21. [Apache Flink 1.8.0 Release Notes](https://flink.apache.org/news/2019/04/09/release-1.8.0.html)
22. [Apache Flink 1.9.0 Release Notes](https://flink.apache.org/news/2019/08/22/release-1.9.0.html)
23. [Apache Flink 1.10.0 Announcement](https://flink.apache.org/news/2020/02/11/release-1.10.0.html)
24. [Apache Flink 1.11.0 Announcement](https://flink.apache.org/news/2020/07/06/release-1.11.0.html)
25. [Apache Flink 1.12.0 Announcement](https://flink.apache.org/news/2020/12/10/release-1.12.0.html)
26. [Apache Flink 1.13.0 Announcement](https://flink.apache.org/news/2021/05/03/release-1.13.0.html)
27. [Apache Flink 1.14.0 Announcement](https://flink.apache.org/news/2021/09/29/release-1.14.0.html)
28. [Apache Flink 1.15.0 Announcement](https://flink.apache.org/news/2022/05/05/release-1.15.0.html)
29. [Apache Flink 1.16.0 Announcement](https://flink.apache.org/news/2022/10/28/release-1.16.0.html)
30. [Apache Flink 1.17.0 Announcement](https://flink.apache.org/news/2023/03/23/release-1.17.0.html)
31. [Apache Flink 1.18.0 Announcement](https://flink.apache.org/news/2023/10/24/release-1.18.0.html)
32. [Apache Flink 2.0 Preview Announcement](https://flink.apache.org/news/2024/10/23/preview-release-of-apache-flink-2.0.html)
33. [Apache Kafka Downloads](https://kafka.apache.org/downloads)
34. [Apache Kafka Blog](https://kafka.apache.org/blog)
35. [Apache Flink History on Wikipedia](https://en.wikipedia.org/wiki/Apache_Flink)
36. [Apache Kafka History on Wikipedia](https://en.wikipedia.org/wiki/Apache_Kafka)
37. [Preview Release of Apache Flink 2.0](https://flink.apache.org/2024/10/23/preview-release-of-apache-flink-2.0/)
38. [Confluent Adds Flink, Iceberg to Hosted Kafka Service](https://www.datanami.com/2024/03/19/confluent-adds-flink-iceberg-to-hosted-kafka-service/)
39. [Highlights from Flink Forward Berlin 2024](https://www.ververica.com/blog/highlights-from-flink-forward-berlin)
40. [Data Streaming Platforms, Gen AI, and Apache Flink at Kafka Summit London 2024](https://www.confluent.io/blog/kafka-summit-london-2024-recap/)
41. [Current 2024: What’s on Tap in Data Streaming](https://www.confluent.io/blog/current-2024-whats-on-tap-in-data-streaming/)
42. [Top 5 Trends for Data Streaming with Kafka and Flink in 2024](https://www.kai-waehner.de/blog/2023/12/02/top-5-trends-for-data-streaming-with-apache-kafka-and-flink-in-2024/)
43. [The Top Five Trends for Data Streaming in 2024](https://www.confluent.io/resources/online-talk/the-top-five-trends-for-data-streaming-in-2024/)
44. [AI Nerve Center – And 400% Growth – Fuel This Google, Amazon, Microsoft Partner](https://www.investors.com/research/ibd-stock-analysis/confluent-stock-ai-stocks/)

The \*\* at the beginning of this article I added, as to be specific. I have not directly, emphasis on directly contributed to the open source code bases of these Apache projects. I have however used, deployed, and even consulted on and discussed architecture and design of the projects over the years. One of these days I may sling some code into a repository or two!
