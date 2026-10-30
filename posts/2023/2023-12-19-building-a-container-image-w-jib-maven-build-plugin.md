---
title: Building a Container Image w/ jib-maven Build Plugin
date: 2023-12-19 12:36:43 -0800
last_modified_at: 2023-12-19 20:15:41 -0800
permalink: /2023/12/19/building-a-container-image-w-jib-maven-build-plugin/
slug: building-a-container-image-w-jib-maven-build-plugin
wp_id: 67421
original_url: https://compositecode.blog/2023/12/19/building-a-container-image-w-jib-maven-build-plugin/
categories:
- Java
tags:
- container image
- docker
- docker container
- docker image
- java docker image
- jib-maven
- maven
- maven build
excerpt: The content is a tutorial on how to set up a GraphQL API project with Maven, using the jib-maven plugin. The process involves initial project setup using Spring Initializr and specific dependency additions. Standard property settings were added to the application.properties file. A simple GraphQL schema and a query mapping and controller were created. Lastly, the jib-maven plugin was added to the pom.xml, and a Docker image was set up. Authentication settings required further work due to errors experienced while setting up permissions for Docker Hub.
image: /wp-content/uploads/2023/12/maven.png
---

First I’ve setup a project, similar to the [Hello World GraphQL API I setup here](/2023/12/01/java-time-with-introspective-graphql-on-chaos-database-aka-pre-refactor-prototype-mutating-database-spring-boot-java-hack-app/). I’ll setup another project that specifically uses Maven, to use the jib-maven plugin.

### Setting Up the Project

I’ve used the standard [Spring Initializr](https://start.spring.io/) in Intellij.

- **Project**: Maven Project
- **Language**: Java
- **Spring Boot**: Choose the latest stable version
- **Project Metadata**: Fill in as per your requirement
- **Packaging**: Jar
- **Java Version**: Choose your Java version (e.g., 11)
- **Dependencies**: Add ‘Spring Web’, ‘Spring Boot DevTools’, and ‘Spring for GraphQL’

[![](/wp-content/uploads/2023/12/CleanShot-2023-12-18-at-16.05.08.png)](/wp-content/uploads/2023/12/CleanShot-2023-12-18-at-16.05.08.png)

[![](/wp-content/uploads/2023/12/CleanShot-2023-12-18-at-16.07.10.png)](/wp-content/uploads/2023/12/CleanShot-2023-12-18-at-16.07.10.png)

Next up I added the standard properties I always do when starting a new GraphQL API in the application.properties file (located in src/resources/application.properties).

```yaml
server.error.whitelabel.enabled=false
server.error.include-stacktrace=always
server.error.include-message=always
server.error.include-binding-errors=always

spring.graphql.graphiql.enabled=true
spring.graphql.graphiql.path=graphiql
```

Next up a quick mini-schema for GraphQL.

```
type Query {
    hello: String
}
```

Finally a short and concise query mapping and controller.

```java
package org.example.dockerimageexample;

import graphql.kickstart.tools.GraphQLQueryResolver;
import org.springframework.graphql.data.method.annotation.QueryMapping;
import org.springframework.stereotype.Controller;

@Controller
public class QueryResolver implements GraphQLQueryResolver {

    @QueryMapping
    public String hello() {
        return "Hello, World!";
    }
}
```

jib-maven

First step, add the jib-maven plugin to the `pom.xml`.

```xml
<!-- Jib Maven Plugin -->
<plugin>
    <groupId>com.google.cloud.tools</groupId>
    <artifactId>jib-maven-plugin</artifactId>
    <version>3.4.0</version>
    <configuration>
        <to>
            <image>adrons-cool-graphql-docker-image</image>
        </to>
        <dockerClient>
            <executable>/usr/local/bin/docker</executable>
        </dockerClient>
    </configuration>
</plugin>
```

In this configuration I’ve got the image name for the docker image set to `adrons-cool-graphql-docker-image` and set it to my local Docker executable at `/usr/local/bin/docker`. I had previously tried to run this without designating the local executable, but it didn’t seem to work, as the location default seemed to be off for the plugin. Thus, I might have a unique setup in this particular scenario, which I’ll eventually sort out but for the purpose of this post, I’ve left it in there.

In some scenarios, reading the docs that exist, this seems like all of the steps that I would have to take. But I still kept getting authentication build errors whenever I ran this. I needed to set the auth for Docker hub into a configuration file in spite of the fact I was deploying nothing – theoretically – to Docker hub. Which, this is one more specificity that I’ll have to probably sort out at some point. But for now, what I did to get authentication setup was set the auth account information in the `settings.xml` file located – not in the project, but at the user level in `/~.m2`.

In the m2 folder I simply did a quick `touch settings.xml`, opened up that file and added the following content, where I’ve obviously changed the username and password to something internet usable. So everything besides the username, password, and id are exactly the same as what would be needed for a new project. I don’t have any other settings added and no other servers, just this for starters. In addition, I mapped the id to the project name `docker-image-example` just so it maps. I’ve done a few experiments and it seems that I could set it to anything, as its a designator (it appears) of the particular build server, nothing more.

```xml
<settings>

    <!-- ... other settings ... -->

    <servers>
        <server>
            <id>docker-image-example</id>
            <username>adron@mydomain.com</username>
            <password>superSecretPassword!</password>
        </server>

        <!-- Add more servers here if needed -->

    </servers>
</settings>
```

That’s my first setup with jib-maven, with initial thoughts and discoveries. Until next time, cheers! 🤘🏻
