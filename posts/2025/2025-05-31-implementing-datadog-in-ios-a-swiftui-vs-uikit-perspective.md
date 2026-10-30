---
title: 'Implementing Datadog in iOS: A SwiftUI vs UIKit Perspective'
date: 2025-05-31 13:03:29 -0700
last_modified_at: 2025-06-01 14:47:25 -0700
permalink: /2025/05/31/implementing-datadog-in-ios-a-swiftui-vs-uikit-perspective/
slug: implementing-datadog-in-ios-a-swiftui-vs-uikit-perspective
wp_id: 72211
original_url: https://compositecode.blog/2025/05/31/implementing-datadog-in-ios-a-swiftui-vs-uikit-perspective/
categories:
- Coding Adventures
- Coding Patterns & Practices
tags:
- coding
- datadog
- logging
- Observability
- programming
- rum
excerpt: This post discusses implementing Datadog in iOS applications using both SwiftUI and UIKit. It highlights the necessary SDK packages, key management challenges, and best practices for monitoring. The author prefers SwiftUI for its maintainability and automatic lifecycle handling, while noting UIKit’s explicit control and customization options. Pricing complexities are also addressed.
image: /wp-content/uploads/2025/05/datadog-log-dogging-the-rum.png
---

I’ve been diving deep into implementing Datadog in iOS applications and wanted to share my experience with both SwiftUI and UIKit approaches and the related elements of the work. Let’s break this down into what works, what doesn’t, and why you might choose various options when using Datadog (or deciding not to use Datadog).

## The Setup

First things first, you’ll need these Datadog SDK packages:

```
dependencies: [
    .package(url: "https://github.com/DataDog/dd-sdk-ios", from: "2.27.0")
]
```

The core packages we’re using:

- DatadogCore
- DatadogLogs
- DatadogRUM
- DatadogCrashReporting

## The Security Configuration Maze

One of the most frustrating experiences I’ve had with Datadog is managing all the different keys and tokens and the documentation surrounding where, which ones, and what is needed where. Here’s what you need to know:

### Required Credentials

1. **Client Token**
   - Used for sending data to Datadog
   - Found in: Organization Settings > API Keys
   - Different from API keys (confusing, I know)
2. **Application ID**
   - Used for RUM tracking
   - Found in: RUM > Applications
   - Not the same as your client token
3. **API Keys**
   - Used for programmatic access
   - Different from client tokens
   - Found in: Organization Settings > API Keys

With that break down, hopefully you won’t run into the problems I ran into. But just so you can identify the problems instantly, here are the confusion points that I stumbled with a few times.

### Common Confusion Points

- Client tokens vs API keys
- Application IDs vs Client tokens
- Organization vs User API keys
- Different keys for different environments
- Also the “Organization Settings” isn’t under “My Organizations” nor does it lead to the other. Note that tokens also aren’t listed under Organization Settings unless you click on Organization Settings and then it is an option on that screen. All rather disorganized and confusing to sort out, especially giving more than a few docs point incorrectly to just “Organizations” or “Organization” without specifying which. Image to point that out, 1 is very different than 2 in spite of the name “Organization” or “Organizations” being in both.

[![Screenshot showing Datadog Personal and Organization Settings menu with highlighted 'My Organizations' and 'Application Keys' sections.](/wp-content/uploads/2025/05/CleanShot-2025-05-30-at-21.02.52.png)](/wp-content/uploads/2025/05/CleanShot-2025-05-30-at-21.02.52.png)

If at any point these elements become confusing, stop what you’re doing, back up a step, regroup, recollect your thoughts, and review where you’re at. There is always a good chance you’ve swapped a key or a token or something somewhere in the process of wiring things up.

### Best Practices for Key Management

```
enum Config {
    enum Datadog {
        static let clientToken: String = {
            guard let token = ProcessInfo.processInfo.environment["DATADOG_CLIENT_TOKEN"] else {
                fatalError("DATADOG_CLIENT_TOKEN environment variable is not set")
            }
            return token
        }()

        static let applicationId: String = {
            guard let id = ProcessInfo.processInfo.environment["DATADOG_APPLICATION_ID"] else {
                fatalError("DATADOG_APPLICATION_ID environment variable is not set")
            }
            return id
        }()
    }
}
```

## The UX Experience

Let’s be honest: Datadog’s interface is powerful but not exactly user-friendly. Here’s what I’ve noticed, and have researched realizing I’m not the only one, there is a lot of community feedback too, and they generally think:

### The Good

- Comprehensive monitoring capabilities
- Powerful query language
- Extensive customization options
- Good documentation

### The Not-So-Good

1. **Interface Complexity**
   - Steep learning curve
   - Overwhelming number of options
   - Non-intuitive navigation
   - Too many clicks to get things done
2. **Dashboard Creation**
   - Tedious widget configuration
   - Complex query building
   - Limited drag-and-drop functionality
   - Time-consuming setup
3. **Common Pain Points**
   - Finding the right settings
   - Understanding the pricing
   - Managing multiple environments
   - Setting up alerts

### Suggested Workarounds

1. Create templates for common dashboards
2. Use the API for automation (throw some AI scripting in there to get shit done and you’ll be golden!)
3. Set up team training sessions

## The UIKit vs SwiftUI Implementation

When implementing Datadog in an iOS application, the choice between UIKit and SwiftUI significantly impacts how we approach monitoring and logging. Let’s explore both approaches in detail.

### UIKit Implementation: The Traditional Approach

UIKit’s imperative nature requires a more hands-on approach to view lifecycle management and event tracking. Here’s a detailed implementation:

```
class ViewController: UIViewController {
    // MARK: - Properties
    private let rum = RUMMonitor.shared()
    private let viewKey = "view_controller"

    // MARK: - Lifecycle Methods
    override func viewDidLoad() {
        super.viewDidLoad()
        // Initialize view and setup UI components
        setupUI()
    }

    override func viewWillAppear(_ animated: Bool) {
        super.viewWillAppear(animated)
        // Start tracking when view appears
        // This is crucial for accurate session tracking
        rum.startView(
            key: viewKey,
            name: "ViewController",
            attributes: [
                "screen_type": "main",
                "user_type": "standard"
            ] as [String: any Encodable]
        )
    }

    override func viewWillDisappear(_ animated: Bool) {
        super.viewWillDisappear(animated)
        // Stop tracking when view disappears
        // This ensures clean session boundaries
        rum.stopView(key: viewKey)
    }

    // MARK: - User Actions
    @IBAction func userActionTapped(_ sender: UIButton) {
        // Track user interactions with custom attributes
        rum.addUserAction(
            type: .custom,
            name: "button_tapped",
            attributes: [
                "button_id": sender.tag,
                "action_type": "tap"
            ] as [String: any Encodable]
        )
    }

    // MARK: - Error Handling
    private func handleError(_ error: Error) {
        // Track errors with detailed context
        rum.addError(
            error: error,
            source: .custom,
            attributes: [
                "error_type": "network",
                "retry_count": 3
            ] as [String: any Encodable]
        )
    }
}
```

This UIKit implementation demonstrates several key aspects:

- Explicit lifecycle management through view controller methods
- Manual tracking of view appearances and disappearances
- Direct access to the RUM monitor for custom event tracking
- Detailed error handling with contextual information
- Clear separation of concerns between UI setup and monitoring

### SwiftUI Implementation: The Modern Approach

SwiftUI’s declarative nature allows for a more elegant and maintainable implementation. Here’s how we can implement the same functionality:

```
// MARK: - RUM View Modifier
struct RUMViewModifier: ViewModifier {
    let name: String
    let attributes: [String: any Encodable]
    @StateObject private var loggingService = DatadogLoggingService.shared

    func body(content: Content) -> some View {
        content
            .onAppear {
                // Start tracking when view appears
                // The modifier handles all the tracking logic
                let rum = RUMMonitor.shared()
                rum.startView(
                    key: name,
                    name: name,
                    attributes: attributes
                )
            }
            .onDisappear {
                // Stop tracking when view disappears
                // Clean and automatic cleanup
                let rum = RUMMonitor.shared()
                rum.stopView(key: name)
            }
    }
}

// MARK: - View Extension
extension View {
    func trackRUMView(
        name: String,
        attributes: [String: any Encodable] = [:]
    ) -> some View {
        modifier(RUMViewModifier(name: name, attributes: attributes))
    }
}

// MARK: - Example View Implementation
struct ContentView: View {
    @StateObject private var viewModel = ContentViewModel()

    var body: some View {
        VStack {
            // View content
            Button("Perform Action") {
                handleUserAction()
            }
        }
        .trackRUMView(
            name: "ContentView",
            attributes: [
                "screen_type": "main",
                "user_type": "standard"
            ]
        )
    }

    private func handleUserAction() {
        // Track user actions with automatic view context
        let rum = RUMMonitor.shared()
        rum.addUserAction(
            type: .custom,
            name: "button_tapped",
            attributes: [
                "action_type": "tap",
                "timestamp": Date()
            ] as [String: any Encodable]
        )
    }
}
```

The SwiftUI implementation offers several advantages:

- Declarative tracking through view modifiers
- Automatic lifecycle management
- Reusable tracking components
- Cleaner, more maintainable code
- Better integration with SwiftUI’s state management

### Key Implementation Differences

The fundamental difference between these approaches lies in how they handle view lifecycle and state management. UIKit requires explicit tracking at each lifecycle point, while SwiftUI provides a more automated approach through its view modifier system.In UIKit, we must manually track view appearances and disappearances, which can lead to more boilerplate code but offers greater control over the tracking process. This is particularly useful in complex applications where you need fine-grained control over what gets tracked and when.SwiftUI, on the other hand, handles much of this automatically through its view modifier system. The RUMViewModifier encapsulates all the tracking logic, making it easy to add tracking to any view with a single line of code. This approach is more maintainable and less prone to errors, but it may be less flexible in certain edge cases.

### Performance and Debugging Considerations

When it comes to performance, UIKit’s explicit tracking can be more efficient in complex scenarios where you need to carefully manage what gets tracked. However, this comes at the cost of more boilerplate code and potential for errors.SwiftUI’s automated tracking is more convenient but may introduce some overhead in complex view hierarchies. The key is to use appropriate sampling rates and batch tracking when possible to minimize this impact.Debugging tracking issues in UIKit is generally more straightforward due to the explicit nature of the implementation. You can easily add breakpoints and inspect the tracking state at each lifecycle point. SwiftUI’s more automated approach can make debugging more challenging, but proper logging and error handling can help mitigate this.

### Migration and Hybrid Approaches

For teams transitioning from UIKit to SwiftUI, a hybrid approach is often the most practical solution. You can maintain the existing UIKit tracking while gradually introducing SwiftUI components with their own tracking implementation. This allows for a smooth transition while ensuring consistent monitoring throughout the application.The key to successful implementation in either framework is maintaining consistent tracking patterns and proper documentation. Whether you’re using UIKit, SwiftUI, or a combination of both, clear guidelines and best practices will help ensure effective monitoring and debugging capabilities.

## The Verdict

If you’re starting a new project, I’d recommend going with SwiftUI. The declarative nature makes implementing Datadog tracking much cleaner and less error-prone. However, if you’re working with an existing UIKit codebase, the UIKit approach is perfectly valid and gives you more granular control.

The key is to be consistent with whichever approach you choose. In my implementation, I’ve gone with SwiftUI because:

1. Less boilerplate code
2. Better state management
3. Automatic lifecycle handling
4. More maintainable in the long run

## A Few Best Practices

1. **Environment Variables**
   - Keep sensitive data out of the code
   - Use proper configuration management
   - Document your setup process
2. **Logging**
   - Use appropriate log levels
   - Include relevant context
   - Don’t log sensitive data
   - Batch when possible
3. **Performance**
   - Monitor memory usage
   - Use appropriate sampling
   - Keep an eye on network calls
4. **Maintenance**
   - Regular SDK updates
   - Monitor log volume
   - Review and adjust as needed

## The Cost Factor

Let’s talk about the elephant in the room: Datadog’s pricing structure. It’s… complicated. Here’s what you need to know:

### Base Pricing

- Free tier: Limited to 5 hosts, 1-day data retention
- Pro tier: Starts at $15/host/month
- Enterprise tier: Custom pricing

### What You’re Actually Paying For

I must add a caveat here. The following is based on quick RTFMing and Reddit reading, plus some other research. However some of this data I’m not sure if it is up to date, or what you might get in their Enterprise oriented options, or in some other scenarios. It’s all kind of confusing really, so YMMV based on your consumption of and relationship with Datadog. I’m not the price guy so some of this might be off by one or just wrong.

1. **Log Management**
   - $0.10 per million log events
   - Additional cost for longer retention periods
   - Indexed logs cost more than non-indexed
2. **RUM (Real User Monitoring)**
   - $1.50 per 1,000 sessions
   - Additional costs for custom events
   - Session replay features cost extra
3. **APM (Application Performance Monitoring)**
   - Included in host-based pricing
   - Additional costs for custom metrics
   - Trace ingestion costs extra

### Hidden Costs to Watch Out For

- Data transfer costs
- Storage costs for longer retention
- Custom metrics and events
- Team member seats
- Support level costs

### Cost Optimization Tips

- Implement log sampling
- Use appropriate log levels
- Set up log retention policies
- Monitor your usage regularly
- Consider using the free tier for development

## Wrapping Up

Whether you choose UIKit or SwiftUI, Datadog provides powerful monitoring capabilities for your iOS app. The key is to implement it in a way that makes sense for your project’s architecture and team’s expertise.

For my part, I’ve found the SwiftUI implementation to be more maintainable and less error-prone, but your mileage may vary depending on your specific needs and constraints.

Let me know if you’ve got any questions or want to dive deeper into any particular aspect!

## References

- [Datadog iOS SDK Documentation](https://docs.datadoghq.com/real_user_monitoring/ios/)
- [SwiftUI Documentation](https://developer.apple.com/documentation/swiftui)
- [Datadog Log Management](https://docs.datadoghq.com/logs/)

This implementation is part of my [simply-swiftly-logging](https://github.com/Adron/simply-swiftly-logging) project, where you can find the complete code and more detailed documentation.
