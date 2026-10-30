---
layout: page
title: Logging, Tracking, and more with Spring Boot
date: 2024-07-22 15:11:46 -0700
last_modified_at: 2024-07-22 15:18:12 -0700
permalink: /logging-tracking-and-more-with-spring-boot/
slug: logging-tracking-and-more-with-spring-boot
wp_id: 69390
original_url: https://compositecode.blog/logging-tracking-and-more-with-spring-boot/
---

One of the critical aspects of building and maintaining financial applications is logging and tracking. Using Spring Boot’s built-in libraries, I implemented a comprehensive logging and tracking system to monitor application behavior and diagnose issues.

### Logback Configuration

I used `Logback` as the logging framework, which is the default in Spring Boot. Here’s a sample configuration:

```
<configuration>
    <appender name="FILE" class="ch.qos.logback.core.rolling.RollingFileAppender">
        <file>logs/app.log</file>
        <rollingPolicy class="ch.qos.logback.core.rolling.TimeBasedRollingPolicy">
            <fileNamePattern>logs/app.%d{yyyy-MM-dd}.log</fileNamePattern>
            <maxHistory>30</maxHistory>
        </rollingPolicy>
        <encoder>
            <pattern>%d{yyyy-MM-dd HH:mm:ss} - %msg%n</pattern>
        </encoder>
    </appender>

    <root level="info">
        <appender-ref ref="FILE" />
    </root>
</configuration>
```

### Custom Logback Customizations

To extend the functionality of Logback for our financial application prototypes, I implemented several customizations to meet specific needs, such as filtering sensitive information, integrating with external logging services, and enhancing log readability.

#### Filtering Sensitive Information

Given the sensitivity of financial data, it was crucial to ensure that no sensitive information (e.g., credit card numbers, personal identification information) was logged. I implemented a custom `TurboFilter` to scrub logs of any sensitive data.

```
import ch.qos.logback.classic.spi.ILoggingEvent;
import ch.qos.logback.core.filter.Filter;
import ch.qos.logback.core.spi.FilterReply;
import java.util.regex.Pattern;

public class SensitiveDataFilter extends Filter<ILoggingEvent> {
    private static final Pattern SENSITIVE_DATA_PATTERN = Pattern.compile("(\\d{4}-?\\d{4}-?\\d{4}-?\\d{4})");

    @Override
    public FilterReply decide(ILoggingEvent event) {
        if (SENSITIVE_DATA_PATTERN.matcher(event.getFormattedMessage()).find()) {
            return FilterReply.DENY;
        }
        return FilterReply.NEUTRAL;
    }
}
```

#### Integration with External Logging Services

To enhance monitoring and alerting, we integrated our logging system with an external logging service like ELK (Elasticsearch, Logstash, Kibana) stack. This required customizing the Logback configuration to use a Logstash appender.

```
<configuration>
    <!-- Other appenders and configuration -->

    <appender name="LOGSTASH" class="net.logstash.logback.appender.LogstashTcpSocketAppender">
        <destination>logstash.example.com:5000</destination>
        <encoder class="net.logstash.logback.encoder.LogstashEncoder" />
    </appender>

    <root level="info">
        <appender-ref ref="FILE" />
        <appender-ref ref="LOGSTASH" />
    </root>
</configuration>
```

#### Enhancing Log Readability

To make logs more readable and easier to parse, I implemented a custom log format that includes additional context information such as request IDs, user IDs, and timestamps.

```
import ch.qos.logback.classic.PatternLayout;
import ch.qos.logback.classic.encoder.PatternLayoutEncoder;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

@Configuration
public class LoggingConfiguration {

    @Bean
    public PatternLayoutEncoder patternLayoutEncoder() {
        PatternLayoutEncoder encoder = new PatternLayoutEncoder();
        encoder.setPattern("%d{yyyy-MM-dd HH:mm:ss.SSS} [%thread] %-5level %logger{36} - %msg%n");
        return encoder;
    }
}
```

### Tracking Requests

To track requests, I used Spring Boot’s `HandlerInterceptor` to log incoming requests and responses.

```
@Component
public class RequestInterceptor implements HandlerInterceptor {
    private static final Logger logger = LoggerFactory.getLogger(RequestInterceptor.class);

    @Override
    public boolean preHandle(HttpServletRequest request, HttpServletResponse response, Object handler) throws Exception {
        logger.info("Incoming request: {} {}", request.getMethod(), request.getRequestURI());
        return true;
    }

    @Override
    public void afterCompletion(HttpServletRequest request, HttpServletResponse response, Object handler, Exception ex) throws Exception {
        logger.info("Outgoing response: {}", response.getStatus());
    }
}
```

### Custom Exception Handling

Custom exception handling was implemented using `@ControllerAdvice` to provide meaningful error messages and log exceptions.

```
@ControllerAdvice
public class GlobalExceptionHandler {
    private static final Logger logger = LoggerFactory.getLogger(GlobalExceptionHandler.class);

    @ExceptionHandler(Exception.class)
    public ResponseEntity<String> handleException(Exception ex) {
        logger.error("An error occurred: {}", ex.getMessage());
        return new ResponseEntity<>("An error occurred: " + ex.getMessage(), HttpStatus.INTERNAL_SERVER_ERROR);
    }
}
```

For details, related to these prototyping projects, check out [Development Patterns for Long-Term Financial Applications](/development-patterns-for-long-term-financial-applications/).
