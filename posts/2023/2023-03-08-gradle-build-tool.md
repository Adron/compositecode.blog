---
title: Gradle Build Tool
date: 2023-03-08 22:48:37 -0800
last_modified_at: 2023-03-09 08:56:17 -0800
permalink: /2023/03/08/gradle-build-tool/
slug: gradle-build-tool
wp_id: 65978
original_url: https://compositecode.blog/2023/03/08/gradle-build-tool/
categories:
- How-to
- Java
- Spring
tags:
- api
- build
- gradle
- gradle build
- java
- java api
- javadocs
- spring
excerpt: A few helpful links and details to where information is on the Gradle Build Tool. Installation Via SDKMAN sdk install gradle x.y.z where x.y.z is the version, like 8.0.2. Via Brew with brew install gradle. Manually check out the instructions here. Building a Java Library (or application, Gradle plugin, etc) Using the init task. From …
image: /wp-content/uploads/2023/03/gradle-1-logo-png-transparent-784658437.png
---

A few helpful links and details to where information is on the Gradle Build Tool.

## Installation

Via SDKMAN `sdk install gradle x.y.z` where x.y.z is the version, like 8.0.2.

Via Brew with `brew install gradle`.

Manually check out the instructions [here](https://gradle.org/install/).

## Building a Java Library (or application, Gradle plugin, etc)

Using the init task. From inside a directory with the pertinent project.

`gradle init`

You’ll be prompted for options.

[![](/wp-content/uploads/2023/03/CleanShot-2023-03-08-at-11.12.53.png)](/wp-content/uploads/2023/03/CleanShot-2023-03-08-at-11.12.53.png)

With the project initialized this is what that initialized folder structure looks like.

[![](/wp-content/uploads/2023/03/CleanShot-2023-03-08-at-11.15.03.png)](/wp-content/uploads/2023/03/CleanShot-2023-03-08-at-11.15.03.png)

At this point add the Java code for the library, similar to this example, and execute a build like this.

`./gradlew build`

## Build Collateral

View the test report via the HTML output file at `lib/build/reports/tests/test/index.htm`l.

The JAR file is available in `lib/build/libs` with the name `lib.jar`. Verify the archive is valid with `jar tf lib/build/libs/lib.jar`.

Add the version by setting the `version = '0.1.1'` in the `build.gradle` file.

Run the jar task `./gradlew jar` and the build will create a `lib/build/libs/lib-0.1.1.jar` with the expected version.

Add all this to the build by adding the following to the `build.gradle` file:

```
tasks.named('jar') {
    manifest {
        attributes('Implementation-Title': project.name,
                   'Implementation-Version': project.version)
    }
}
```

Verifying this all works, execute a `./gradlew jar` and then extract the MANIFEST.MF via `jar xf lib/build/libs/lib-0.1.0.jar META-INF/MANIFEST.MF`.

## Adding API Docs

In the \*/Library.java file, replace the / in the comment by / \* so that we get *javadoc* markup.

Run the `./gradlew javadoc` task. The generated javadoc files are located at `lib/build/docs/javadoc/index.html`.

To add this as a build task, in `build.gradle` add a section with the following:

```
java {
    withJavadocJar()
}
```

## Publish a Build Scan

Execute a build scan with `./gradlew build --scan`.

## Common Issues + Tips n’ Tricks

#### gradlew – Permission Denied issue

Let’s say you execute Gradle with `./gradlew` with whatever parameter and immediately get a response of “Permission Denied”. The most common solution, especially for included `gradlew` executables included in repositories, is to just give the executable permission to execute. This is done with a simple addition `chmod +x gradelw` and you should now be ready to execute!
