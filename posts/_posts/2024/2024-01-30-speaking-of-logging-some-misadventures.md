---
title: Speaking of Spring Boot Java Logging, Some Misadventures
date: 2024-01-30 14:26:54 -0800
last_modified_at: 2024-01-31 13:29:33 -0800
permalink: /2024/01/30/speaking-of-logging-some-misadventures/
slug: speaking-of-logging-some-misadventures
wp_id: 67634
original_url: https://compositecode.blog/2024/01/30/speaking-of-logging-some-misadventures/
categories:
- Java
tags:
- java
- java logging
- java spring boot
- logging
- logging PII
- logging redaction
- personally identifiable information
- redaction
- spring
- spring boot
- spring boot logging
- spring logging
excerpt: The content discusses implementing log masking for Personally Identifying Information (PII) in Java Spring Boot applications. It covers creating custom Logback converters with regular expressions, using Log4j2 configuration with properties, and suggests additional logging strategies like AOP, custom annotations, MDC, custom Logback filters, integrating with external logging systems, JSON log format, and custom log levels for thorough log data management and security.
image: /wp-content/uploads/2020/04/java.jpg
---

Preface: I set out upon a task to incorporate some masking, redaction, or filtering of some sort on PII (Personally Identifying Information) for the log files and log data an application service is producing. The application pre-exists, so this isn’t entirely a green field situation, but the application generally fits a Spring Boot Service style application. The one key thing I wasn’t sure about when starting, was what kind of logging was already incorporated into the operational service.

## Log Masking for Different Logging Libraries

The first solution I came up with was to incorporate a converter or appender of some sort that would mask PII with a string of some sort, like “\*\*\*\*” or “—–“. This solution that I came up with, upon checking, looked like it would work out ok with or for a number of the top logging libraries for Java, specially libraries that run with or as a Spring Boot service like LogBack or Log4j.

## Solution: Extend ClassicConverter & Write Up a Classic Converter

The way I implemented that involved the following implementation, I’ll dub this one the the log-mask-example, and have the repo available [here](https://github.com/adronkaleyra/log-mask-example). There are several key pieces of collateral that make this work, the first being the logback-spring.xml configuration, added to the resources directory. The file looks like this, including the template for the log message, and the converterClass class path.

```
<configuration>
    <conversionRule conversionWord="piiMask" converterClass="org.skidrow.logmaskexample.PiiMaskingConverter"/>
    <appender name="STDOUT" class="ch.qos.logback.core.ConsoleAppender">
        <encoder>
            <pattern>%d{yyyy-MM-dd HH:mm:ss} [%thread] %-5level %logger{36}- %piiMask %n</pattern>
        </encoder>
    </appender>
    <root level="info">
        <appender-ref ref="STDOUT"/>
    </root>
</configuration>
```

Then there is the PiiMasking Converter class itself. It shapes up like this, to which, note I’ve removed the imports for brevity. Check out the file [here](https://github.com/adronkaleyra/log-mask-example/blob/main/src/main/java/org/skidrow/logmaskexample/PiiMaskingConverter.java) for the full imports and all.

```
public class PiiMaskingConverter extends ClassicConverter {

    private List<PiiRegexPattern> patterns;

    public PiiMaskingConverter() throws IOException {
        try {
            ObjectMapper mapper = new ObjectMapper();
            InputStream is = getClass().getResourceAsStream("/regexMasks.json");
            patterns = mapper.readValue(is, new TypeReference<>() {
            });
        } catch (IOException e) {
            throw new IOException("Error reading regex_patterns.json", e);
        }
    }

    @Override
    public String convert(ILoggingEvent event) {
        return maskMessage(event.getFormattedMessage());
    }

    private String maskMessage(String message) {

        boolean turnOn = getMaskingEnabled() {
        if (!turnOn)
            return message;
        for (PiiRegexPattern pattern : patterns) {
            message = message.replaceAll(pattern.getRegex().toString(), "****");
        }

        return message;
    }

    private boolean getMaskingEnabled() {

        Environment env = ApplicationContextProvider.getApplicationContext().getBean(Environment.class);
        return env.getProperty("masking.enabled", Boolean.class, true);
    }
}
```

The PiiRegexPattern I setup, which inflates from the values in the regexMasks.json file, looks like this.

```
public class PiiRegexPattern {

    private String title;
    private String regex;
    private String mask;

    public String getTitle() {
        return title;
    }

    public String getRegex() {
        return regex;
    }

    public String getMask() {return mask;}
}
```

Finally the regexMasks.json file shapes up with a few examples like this.

```
[
  {
    "title": "emailMask",
    "regex": "\\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\\.[A-Z|a-z]{2,}\\b"
  },
  {
    "title": "ipAddress",
    "regex": "\\b(?:[0-9]{1,3}\\.){3}[0-9]{1,3}\\b"
  },
  {
    "title": "phoneMask",
    "regex": "\\b(1[-+]?\\s?)?(\\(\\d{3}\\)\\s?\\d{3}[-.]?\\d{4}|\\d{3}[-.]?\\d{3}[-.]?\\d{4})\\b"
  },
  {
    "title": "internationalPhoneMask",
    "regex": "\\b\\+?\\d{1,3}?[-.\\s]?\\d{1,4}?[-.\\s]?\\d{1,4}?[-.\\s]?\\d{1,4}(?:\\s*x\\d{1,5})?\\b"
  }
]
```

This way it’s easy to just add additional regular expressions to the mix without adding them in code. Just add them to the JSON file and it’ll pull them in and run each of them.

The example repository I’ve linked also generates some kind of arbitrary log messages and examples just to have something to work with, if you want to clone it and give it a try. If you’ve got any questions, scroll on down the page and pop a comment in there. Happy to answer questions and elaborate on the approach.

## Solutions: Log4j2 Multi-Regular Expression Configuration Option

After further work I became aware of another option that eliminates the programmatic nature of this implementation and puts everything in configuration, requiring a shift to Log4j2, which is kind of ideal anyway considering the performance and other characteristics of Log4j2.

This option includes setting up some regular expressions via the properties section of a Log4j2.xml default configuration. You could use a custom configuration too, it doesn’t need to be a default configuration file. The properties shape up like this.

```
<Property name="phoneRegex">\b(1[-+]?\s)?(\(\d{3}\)\s?\d{3}[-.]?\d{4}|\d{3}[-.]?\d{3}[-.]?\d{4})\b</Property>
<Property name="emailRegex">\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b</Property>
<Property name="passwordFieldRegex">\bpassword\b\s+\[([^]]+)]</Property>
<Property name="redactText">RDCTD</Property>
```

My pattern layout, in the same configuration file, almost matching the default Spring Boot convention based configuration, shapes up like this.

```
<PatternLayout pattern="%d{yyyy-MM-dd'T'HH:mm:ss.SSSXXX} %5p ${sys:PID:-1} --- [%-15.15t] %-41.41logger : %replace{%replace{%replace{%msg}{${phoneRegex}}{${redactedText}}}{${emailRegex}}{${redactedText}}}{${fullPasswordEntryRegex}}{${redactedText}}%n"/>
```

Let’s break down the components of this pattern:

1. **`%d{yyyy-MM-dd'T'HH:mm:ss.SSSXXX}`**: This is the date and time format. `%d` specifies that the timestamp of the log event should be included. The `{}` contains the format of the timestamp. In this case, it’s a standard ISO 8601 format, including the year, month, day, hour, minute, second, millisecond, and timezone.
2. **`%5p`**: This represents the log level (like INFO, DEBUG, ERROR) in a 5-character wide field, right-aligned.
3. **`${sys:PID:-1}`**: This is a system property placeholder. It attempts to include the Process ID (PID) of the running application. If the PID is not available, it defaults to `-1`.
4. **`---`**: This is just a separator for readability.
5. **`[%-15.15t]`**: This includes the name of the thread that generated the log message. The `-15.15` formatting means the thread name will be truncated or padded to exactly 15 characters.
6. **`%-41.41logger`**: This is the logger’s name, usually the class name where the log statement is written. Similar to the thread name, it’s truncated or padded to 41 characters.
7. **`%replace{...}%n`**: This is a complex replace operation nested within the log message (`%msg`). It’s designed to redact sensitive information. Each `%replace{}` function takes three arguments: the input, a regex pattern to search for, and the replacement text. In this sequence, it redacts phone numbers, email addresses, and full password entries with `${redactedText}`. The `${phoneRegex}`, `${emailRegex}`, and `${fullPasswordEntryRegex}` are placeholders that should be defined elsewhere in the configuration to match their respective patterns.
8. **`%n`**: This is a newline character, ensuring each log message is printed on a new line.

There is also a need to ensure the dependency for Log4j2 is present in your dependencies file (i.e. your Maven file or whatever you’d want to use).

## Solutions Discussion

Below are additional ways to set up custom logging in a Spring Boot application, aside from the two already mentioned. I offer these to extend the brainstorming options when I, or you, are trying to get it sorted out what we need for logging in our applications. I hope it’s useful, and if you dear reader, know of any I’ve missed please add a comment with the additional option and I’ll add it to this list for completeness!

### Aspect-Oriented Programming (AOP) for Logging

- **Description**: Use AOP to intercept method calls and log relevant information. This is particularly useful for logging at the service or controller layer.
- **Advantages**: Provides centralized control over logging, can easily add or remove logging without modifying the actual service or controller code.
- **Example**: Using Spring AOP, create an aspect that logs method entry and exit, along with parameters and return values, optionally adding masking for sensitive data.

### Custom Annotation for Logging

- **Description**: Create a custom annotation that can be used to mark methods or parameters that need logging.
- **Advantages**: Offers fine-grained control over what gets logged, as developers can choose which methods or parameters to annotate.
- **Example**: Implement an annotation like `@Loggable` and use AOP or an interceptor to handle the logging logic whenever this annotation is encountered.

### SLF4J MDC (Mapped Diagnostic Context) for Advanced Logging

- **Description**: MDC allows for storing key-value pairs in the log context, which can then be included in the log messages.
- **Advantages**: Useful for adding contextual information to logs, like user IDs or transaction IDs, which helps in tracing and debugging.
- **Example**: In a web application, use a servlet filter or Spring interceptor to put a unique request ID into MDC at the beginning of a request and clear it at the end.

### Custom Logback Filters

- **Description**: Create custom filters in Logback for more control over what gets logged.
- **Advantages**: Allows for complex logic to determine if a log line should be printed, which is useful for dynamic log levels or redacting specific information.
- **Example**: Implement a filter that checks the content of each log message and decides whether to log it based on certain criteria, such as the presence of PII.

### Integration with External Logging Systems

- **Description**: Integrate with external logging systems or services like ELK (Elasticsearch, Logstash, Kibana) for more robust log management.
- **Advantages**: Offers powerful search, visualization, and analysis capabilities for logs.
- **Example**: Configure Spring Boot to send logs to Logstash, which then forwards them to Elasticsearch. Use Kibana for visualization and analysis.

### Using JSON Log Format

- **Description**: Configure loggers to output logs in JSON format, which is more structured and easier for parsing and analysis by log management tools.
- **Advantages**: Facilitates the integration with log analysis tools and improves the readability and structure of log data.
- **Example**: Set up Logback or Log4j2 to output logs in JSON format, including custom fields like method names, response times, etc.

### Custom Log Levels

- **Description**: Define custom log levels to categorize log messages more granely than the standard levels (INFO, DEBUG, etc.).
- **Advantages**: Provides more control and flexibility in how log messages are categorized and filtered.
- **Example**: Create custom log levels like AUDIT for logging user activities or METRIC for performance measurements.

## Summary i.e. the TLDR

In this conversation, I’ve discussed custom logging solutions in Java Spring Boot applications, with a focus on redacting Personally Identifying Information (PII) from logs. The initial approach involved creating a custom Logback converter to mask PII using regular expressions based on the default dependencies included in Spring Boot, configured via `logback-spring.xml` and an external JSON file. We also explored a Log4j2 configuration that uses properties for regular expressions to redact sensitive information directly in the pattern layout. Additional custom logging strategies were suggested, including using Aspect-Oriented Programming (AOP), custom annotations, SLF4J’s Mapped Diagnostic Context (MDC), custom Logback filters, integration with external logging systems like ELK, outputting logs in JSON format, and defining custom log levels. These methods provide a comprehensive framework for effectively managing and securing log data in Spring Boot applications, ensuring sensitive information is adequately protected.
