---
layout: page
title: 'Vertical Application Stacks with Horizontal Infrastructure as Code: Java Spring Boot, Docker/K8s, and Continuous Deployment Prototype (i.e. Reference applications)'
date: 2024-07-22 15:13:32 -0700
last_modified_at: 2024-07-22 15:18:14 -0700
permalink: /vertical-application-stacks-with-horizontal-infrastructure-as-code-a-journey-into-java-spring-boot-docker-k8s-and-continuous-deployment/
slug: vertical-application-stacks-with-horizontal-infrastructure-as-code-a-journey-into-java-spring-boot-docker-k8s-and-continuous-deployment
wp_id: 69389
original_url: https://compositecode.blog/vertical-application-stacks-with-horizontal-infrastructure-as-code-a-journey-into-java-spring-boot-docker-k8s-and-continuous-deployment/
---

When I’m building out a prototype for a financial app—whether it’s for credit card processing or home loan management—I’m not just thinking about the immediate functionality. I’m considering the whole lifecycle, from development to deployment to long-term maintenance.

Here’s where the horizontal infrastructure as code (IaC) assets come into play. I’ve found that using tools like Terraform or Pulumi to define my infrastructure gives me a huge advantage. It’s not just about spinning up some EC2 instances or Kubernetes clusters. It’s about creating a repeatable, scalable foundation that can grow with the application.

For example, when I was prototyping a credit card payment API using Spring Boot, I set up a Kubernetes cluster using Terraform. This gave me the flexibility to easily deploy and scale my containerized Spring Boot app. But more importantly, it allowed me to version control my infrastructure alongside my application code. This is crucial for maintaining consistency across environments and for quickly spinning up new instances for testing or disaster recovery.

## Spring Boot Prototypes for Financial Applications

I’ve implemented both GraphQL and RESTful APIs for various financial applications. Here’s the quick list of a few:

1. **Credit Card Payment API (RESTful)**: I built this using Spring Boot with JPA for data persistence. The API handled payment processing, card validation, and transaction history. I used Spring Security for OAuth2 authentication to ensure secure transactions.
2. **Home Loan Processing API (GraphQL)**: This was an interesting one. I used Spring Boot with Spring for GraphQL to create a flexible API for loan applications. The GraphQL schema allowed clients to request exactly the data they needed, which was particularly useful for the complex data structures involved in loan processing.
3. **Financial Account Management API (RESTful)**: This was a hybrid approach. I used Spring Boot to create a RESTful API for basic CRUD operations on accounts, but I also integrated Apache Kafka for real-time event streaming. This allowed for immediate updates across the system when account changes occurred.
4. **API Templating Application**: I built a templating application, basically give it the basic information about data from a Kafka stream and a Spring Boot Java project template would be generated for a GraphQL API using subscriptions for streaming. This gave an immediate kick start to any developers aiming to create a GraphQL API for their respective services or application related to a stream they wanted to utilize.

In all these cases, containerization was key. I used Docker to package these Spring Boot applications along with their dependencies. This made deployment a breeze, especially when combined with Kubernetes for orchestration.

For continuous deployment, I set up some Jenkins CI/CD pipelines. These pipelines would build the Docker images, run tests, and deploy to the Kubernetes cluster automatically on each commit. This setup allowed for rapid iteration and easy rollbacks if needed.

Almost like a trip down memory lane, one of the teams I was supporting also brought up Jetbrains TeamCity which I also built out a few prototype pipelines on.

## Logging and Tracking with Spring Boot

One of the critical aspects of building and maintaining financial applications is logging and tracking. Using Spring Boot’s built-in libraries, I implemented a comprehensive logging and tracking system to monitor application behavior and diagnose issues.

### Logging Configuration

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

## Development Patterns for Long-Term Financial Applications

Financial applications often involve long-running processes, which can span days or even weeks. Implementing development patterns that support these extended workflows is crucial.

### Saga Pattern

The Saga pattern helps manage long-running transactions by breaking them into smaller, manageable steps with compensating actions to handle failures.

```
public class LoanProcessingSaga {
    public void applyForLoan(LoanApplication application) {
        try {
            // Step 1: Validate application
            validateApplication(application);

            // Step 2: Process application
            processApplication(application);

            // Step 3: Approve loan
            approveLoan(application);
        } catch (Exception e) {
            // Compensating action
            rollbackApplication(application);
        }
    }

    private void validateApplication(LoanApplication application) {
        // Validation logic
    }

    private void processApplication(LoanApplication application) {
        // Processing logic
    }

    private void approveLoan(LoanApplication application) {
        // Approval logic
    }

    private void rollbackApplication(LoanApplication application) {
        // Rollback logic
    }
}
```

### Event-Driven Architecture

Using an event-driven architecture with Apache Kafka, we can handle long-running processes by decoupling services and using events to trigger actions.

```
@Service
public class LoanApplicationService {
    @Autowired
    private KafkaTemplate<String, LoanApplicationEvent> kafkaTemplate;

    public void applyForLoan(LoanApplication application) {
        // Publish loan application event
        kafkaTemplate.send("loan-application-events", new LoanApplicationEvent(application));
    }
}

@Component
public class LoanApplicationEventListener {
    @KafkaListener(topics = "loan-application-events", groupId = "loan-processing")
    public void handleLoanApplicationEvent(LoanApplicationEvent event) {
        // Handled events here.
        processLoanApplication(event.getApplication());
    }

    private void processLoanApplication(LoanApplication application) {
        // All our fancy processing logic
    }
}
```

For further elaboration on this work I’ve added two additional addendum pages describing various aspects of the application prototypes and work.

- [Development Patterns for Long-Term Financial Applications](/development-patterns-for-long-term-financial-applications/)
- [Logging, Tracking, and more with Spring Boot](/logging-tracking-and-more-with-spring-boot/)
