---
title: Starting a New Project – Let’s Choose a Tech Stack!
date: 2024-02-15 11:20:07 -0800
last_modified_at: 2024-03-01 17:36:58 -0800
permalink: /2024/02/15/starting-a-new-project-lets-choose-a-tech-stack/
slug: starting-a-new-project-lets-choose-a-tech-stack
wp_id: 67767
original_url: https://compositecode.blog/2024/02/15/starting-a-new-project-lets-choose-a-tech-stack/
categories:
- App Building
- Architecture
- Coding Adventures
- graphql
- How-to
- Java
- Javascript
tags:
- application building
- application coding
- java
- javascript
- records
- vinyls
excerpt: The post outlines the initiation of a new project for a multi-tenant music collector’s database. The objectives include personal use and sharing with others, along with the selection of tech stacks. The project aims to provide a personalized, secure, and collaborative platform for enthusiasts to manage and appreciate their vinyl collections efficiently. Key decisions include PostgreSQL for the database, Java Spring Boot for services and middle tier, and React for the user interface.
image: /wp-content/uploads/2024/02/IMG_6251.jpeg
---

It’s time to start a new project. Because [one can never have enough side projects](https://adron.github.io/anotherfuckingsideproject/)! **/s**

This particular project I’ll be writing about in this post is derived from the [multi-tenant music collector’s database](/2023/10/23/building-a-multi-tenant-music-collectors-database/) I’ve already started working on. I’ve finally gotten back to it, during a slight break in collecting and music listening, to write up some of my thinking about this particular project.

## Stated Objectives For This Application

1. **Personal Reasons:** I always like to have side projects that I could make use of myself. Since I’ve recently started collecting music again, and in that am a [new collector of vinyl albums](https://viciousshred.com/2023/06/18/the-beginning-of-reactions-reviews-album-unboxing/), I wanted a better way to organize all that music and the extensive history, members, song, lyrics, and related information about the music and artists.
2. **For Everybody:** Beyond the desire to have a well built application to provide the capabilities I’ve described above, I also want to provide this capability to others. In light of that capability, I’ll be designing this application as a multi-tenant application so that you too dear reader, once I get it built can use the application for your own music collection.
3. **Choose The Tech Stack:** I’ll need to write this application in something, obviously, so this post is going to cover my reasoning for the tech stack I’m going to use. The application will be built in three core pieces: the database, the services and middle tier layer, and the user interface. I’ll detail each and cover the reasoning for the stack I’ll choose for each section.

## My Own Personal Collection

Building an application to organize my (or your) growing collection of music (vinyls, CDs, Cassettes, digital, or whatever) albums and the rich history surrounding the music and artists you’re passionate about is not just a practical endeavor; it’s a journey into the heart of what makes music collecting a deeply personal and rewarding hobby. For enthusiasts, music is not just about the sounds. It’s about the stories, the people behind the creations, and the cultural moments captured in each track. By developing an application tailored to your needs, you’re crafting a tool that not only enhances your enjoyment of the hobby but also deepens your connection to the music. This goes beyond mere organization; it’s about creating an immersive experience that lets you explore and appreciate the intricate web of influences, history, and creativity that music embodies.

Moreover, such a project reflects a broader trend towards personalized solutions for niche interests. In a world where mainstream platforms often overlook the depth and specificity of niche hobbies (or food or a million other things), building my own application stands as a testament to this decentralization of teh commoditization of people’s personal interest in music. It enables you to track down, record, reflect on and introspect about what makes collectors, such as detailed cataloging options, historical insights, and track-by-track analysis. This level of customization is not just about convenience; it’s about creating a space that respects and elevates the art of music collecting. It becomes a dynamic archive, a living history, and a personal museum of your musical journey. By investing in this project, I’m not just organizing a collection; I’m working toward preserving a legacy and contributing to the culture of music appreciation in a digital age.

## Available to All the Collectors

By adopting a multi-tenant architecture for this vinyl collection application, it becomes an accessible and scalable tool for a wide range of collectors, from novices to experts. This approach not only democratizes the management and appreciation of vinyl records but also fosters a vibrant community where users can exchange insights and experiences. The customizable nature of the platform ensures that each collector can tailor the application to the specifics of their collection, tracking everything from album history to personal anecdotes. This level of personalization enriches the collecting experience, allowing users to see their collections not just as music, but as a mosaic of cultural and historical significance.

The mostly decentralized aspect of the application offers enhanced security, reliability, and privacy, ensuring that users’ data and collections are safeguarded. This structure supports a more resilient platform with reduced risks of downtime or data loss, crucial for collectors who invest significant time in cataloging their albums. Moreover, the decentralized model promotes a collaborative environment, enabling collectors to contribute to and benefit from a collective pool of knowledge. This communal approach deepens the connection between collectors, transforming individual pursuits into a shared exploration of music history and culture.

In essence, this multi-tenant, decentralized application transcends mere organization of vinyl records, offering collectors a comprehensive tool that caters to the nuances of their hobby. It not only facilitates the management of collections but also enhances the overall experience of music collecting by fostering a sense of community and shared passion among enthusiasts. Through personalized features and collaborative opportunities, collectors are equipped with a dynamic platform that celebrates the art of music collection in the digital age.

## Choose The Language & Stack

**Caveat:** The initial choice of language and technology stack for building this application is provisional. It’s crucial to maintain flexibility, as the evolving needs and challenges of the project might necessitate a reassessment of the chosen technologies. While a change in the stack should not be made lightly—considering the progress made, existing work, and potential obstacles—it’s important to weigh these factors carefully. Ultimately, the decision to adjust the technology stack should be guided by its impact on the project’s success, keeping in mind the importance of this choice for various reasons.

The right language and technology stack for your application will influence its development, scalability, and maintenance. Here are my top considerations to guide my choice:

**Project Requirements:** Assess the specific needs of your vinyl collection application, including the need for real-time updates, scalability, multi-tenancy, and decentralized data management. The technology stack should align with these functional and technical requirements.

**Developer Expertise:** Consider the skills and expertise of my development team – i.e. starting with, that’s me and me alone. Choosing technologies that a prospective future team is familiar with can accelerate development and reduce the learning curve, though it’s also an opportunity to adopt new technologies if they offer significant benefits. In addition, it also may spell disaster if people can’t be found that use a particular technology. Memories of finding Erlang developers, something that is almost impossible, comes to mind. Another is Haskell, both languages are extremely powerful but if you must grow a larger team, hiring that team can be extremely difficult or impossible.

**Community Support and Ecosystem:** Opt for languages and technologies with strong community support and a rich ecosystem of libraries and tools. This can significantly ease development challenges and provide access to pre-built solutions for common problems. In some cases, it might take a little bit more examination to really understand what is grassroots community vs. forced corporate community. Is it really driven by people’s motivations (i.e. Go vs. Rust vs. .NET vs. Java) or is it some other drivers, and how much do you trust or want to be involved in that particular community.

**Security:** Given the application’s focus on personalized collections, security is important. As it should be with all applications really, since it’s not exactly impossible or that difficult to decently secure most website application. Choosing technologies with robust security features and a good track record of addressing vulnerabilities is a great starting point.

**Interoperability and Integration:** The ability to easily integrate with other services, APIs, and data sources is crucial. Select technologies that offer flexibility in integration and support for standard data exchange formats. Does the technology have ways to easily shim in other languages or stacks or binaries of other sorts? How well does the language itself, and its stack, work within the overall realm of technology as a whole?

**Deployment and Operational Considerations:** Some technologies are easier to deploy and manage than others, especially in a decentralized environment. Consider the ease of deployment, monitoring, and ongoing management as part of your technology stack decision. This, especially since I’m starting this one off as a singular developer could be the make or break. As at some point, my intent would be for the bulk of my effort to be focused around operational needs and focusing on my collection and not particularly worrying about building features or such.

Balancing these considerations will help me choose a technology stack that not only meets the current needs of my application but also positions it for future growth and success. It’s also beneficial to prototype or conduct a feasibility study with shortlisted technologies to validate my choice before committing to a full-scale development project.

## The Decisions

As I stated before, there are three key parts to this application. There is the database, the service(s) and middle tier, and the user interface. For the database I can easily go ahead and make that decision, as I’ll use a relational database and that database will be PostgreSQL for a billion and 1 reasons. For now though, I’m going to skip that and instead write a whole blog post about why I chose PostgreSQL.

### ***Decision: Database is PostgreSQL.***

Next up would be the services and middle tier. This part is probably the most difficult for the simple fact that there is the widest selection of options here. Every single language and stack can build whatever kind of services, APIs, middle tier, and the plethora of middleware one needs.

**Comprehensive Integration Support:** This framework supports both GraphQL and REST APIs right from the start, offering flexibility to cater to varied client data requirements. This inclusivity ensures developers can easily craft and manage diverse API endpoints, facilitating efficient data exchanges. The GraphQL integration aids in reducing data over-fetching and under-fetching, while REST API compatibility maintains simplicity and adherence to web standards.

**Robust Database Connectivity:** Known for its advanced ORM capabilities, it ensures seamless database interactions, particularly with PostgreSQL. This ORM layer simplifies complex queries and data operations, allowing developers to utilize PostgreSQL’s advanced features effectively without deep SQL knowledge. This comprehensive database support is crucial for applications requiring reliable and efficient data management.

**Performance Optimization Features:** It includes a suite of tools for enhancing API performance, such as asynchronous processing, caching, and efficient connection pooling. These features are vital for scaling applications and managing large volumes of requests smoothly. The framework’s design allows for easy performance tuning to meet specific application demands, ensuring optimized scalability and resource utilization.

**Vibrant Developer Community:** Beyond technical features, the framework boasts a vast and active developer community. This network is a rich resource for support, tutorials, and shared knowledge, significantly easing the learning curve and troubleshooting process. The availability of a large pool of skilled developers also bodes well for future application maintenance and enhancements. This community aspect ensures that new features, best practices, and updates are readily accessible, keeping applications up-to-date and secure.

**My Own Experience:** I’m actually choosing this language and stack not because it is what I’m most familiar with, but because I want to regain familiarity with the stack. Currently, it’s been more years than I’d like to admit since I regularly did work with this language and stack. Only recently have I delved back into it for some work related efforts, and now it’ll be the core of this project.

### ***Decision: Java Spring Boot***

Finally the user interface. I know I want it to be a web interface for many – what should be – obvious reasons. The choice basically comes down to two for me, React or Vuejs. I’ve spent some time learning Vuejs and some time developing with React.

I don’t like either. I don’t really like how the “web” and its “interface” works since its all janky and hacked together technologies. But it is the only “web” that we have and the most common way to build things for the web these days tends to be React. Thus…

### ***Decision: React***

So that’s that, in the coming days, weeks, and months as I build out this application, this is the starting point for which and why I’ve decided to use these particular pieces of tech.

[![](/wp-content/uploads/2024/02/Service-blueprint-with-swimlanes.png)](/wp-content/uploads/2024/02/Service-blueprint-with-swimlanes.png)

**References & Notes:**

- /s This is short for “sarcasm” to call out something that isn’t particularly obvious as sarcasm.
