---
layout: page
title: Spam Detection Project
date: 2024-07-03 12:44:43 -0700
last_modified_at: 2024-08-20 10:57:48 -0700
permalink: /spam-detection-project/
slug: spam-detection-project
wp_id: 69094
original_url: https://compositecode.blog/spam-detection-project/
---

Adron here, diving into the nitty-gritty of my latest project: building a robust SMS/MMS content filter leveraging Spring Boot and Proofpoint. This project was all about creating a seamless and efficient spam detection service. Let me take you through how the team and I put it all together.

#### The Objective

Our goal was to build a content filter service that could process and analyze SMS and MMS messages, utilizing Proofpoint for spam determinations. We needed to handle various message formats, reassemble multi-part messages, extract relevant features, and make real-time spam decisions. Here’s how we made it happen.

#### Architecture Overview

Our system is built with several key components:

1. **Message Ingestion Module**: Captures incoming messages.
2. **Message Preprocessing Module**: Decodes and reassembles multi-part messages.
3. **Feature Extraction Module**: Uses UDFs to extract message features.
4. **Spam Detection Module**: Integrates Proofpoint for spam analysis.
5. **Filtering and Logging Module**: Filters spam and logs results for further analysis.

#### Building the Spam Detection Module with Spring Boot and Proofpoint

The heart of our spam detection lies in the integration with Proofpoint. Here’s how we leveraged Spring Boot to build and deploy this service.

**1. Spring Boot Service Class**

We created a service class in Spring Boot, marking it as a service component to be managed by Spring. This class implements an interface to ensure consistency across different implementations.

**2. Asynchronous Processing**

To handle spam checks without blocking, we utilized asynchronous processing. This allows our service to process multiple requests concurrently, improving overall throughput.

**3. WebClient for HTTP Requests**

We used Spring’s WebClient to interact with Proofpoint’s API. This modern, non-blocking HTTP client simplifies the process of making API calls and handling responses. The client is configured to send the extracted message features to Proofpoint and receive spam determination results.

**4. Proofpoint Integration**

Proofpoint’s API plays a critical role in our spam determinations. We configured headers and message bodies as per Proofpoint’s requirements, ensuring accurate and efficient communication. The headers include information such as the source and destination of the message, and other policy-related variables.

**5. Handling Multi-part Messages**

Our service handles multi-part messages by decoding and reassembling them into a single coherent message. It also converts hexadecimal message content to a readable format, ensuring that the entire message is analyzed accurately.

**6. Metrics and Monitoring**

The team opted for Micrometer for monitoring and logging the performance of our spam detection service. This helps in keeping track of spam detection rates and system performance. We set up counters to track the number of messages identified as spam and other relevant metrics.

#### Containerization and Stateless Scaling

To ensure the application can handle high throughput, we containerized it using Docker with the intent of adding service nodes when throughput demands increase. Here’s how we set it up:

1. **Dockerization**: We created a Dockerfile to package the Spring Boot application into a container. This Dockerfile includes all necessary dependencies and configuration for running the application.
2. **Stateless Architecture**: The application is designed to be stateless, meaning it does not store any session data locally. This allows us to scale horizontally by simply adding more containers. Each instance of the application can handle incoming requests independently, ensuring high availability and reliability.
3. **Orchestration**: We made use of AWS Beanstalk for this application and deployment automation via Github actions. The entire process was automated via branching triggers for seamless deploy per desired environment.
4. **Auto-scaling**: AWS auto-scaling capabilities ensure that the number of running containers adjusts automatically based on the incoming traffic load. This means our spam detection service can seamlessly handle spikes in message volume without manual intervention.

#### Deployment

Deploying our Spring Boot application was straightforward. We packaged the application as a JAR file and deployed it to our AWS VPC environment via Github + Beanstalk Actions. Spring Boot’s embedded server made the deployment process seamless, allowing us to focus on refining the spam detection logic for pre and post processing needs.

#### Conclusion

By combining Spring Boot with Proofpoint’s advanced spam detection capabilities, and leveraging Docker and AWS resources for containerization and orchestration, we built a powerful, scalable, and reliable SMS/MMS content filter. This project is a textbook example of how leveraging robust third-party solutions within a well-architected Spring Boot application can lead to efficient and effective solution.

That’s all for now. Stay tuned for more insights into my projects, and as always, happy coding!

---

> P.S. If you have any questions or want to share your experiences with spam detection, drop a comment or reach out to me directly. Let’s keep the conversation going!

> P.S.S. Names and companies have been relabeled in some of these description to prevent associations and for security reasons. The work was done, but the company names might be slightly altered for these reasons.
