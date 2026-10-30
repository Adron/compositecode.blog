---
title: 'The Second Order Effects of AI Acceleration: 22 Predictions from Polyglot Conference Vancouver'
date: 2025-10-12 17:46:48 -0700
last_modified_at: 2025-10-12 17:46:48 -0700
permalink: /2025/10/12/the-second-ofrder-effects-of-ai-acceleration-22-predictions-from-polyglot-conference-vancouver/
slug: the-second-ofrder-effects-of-ai-acceleration-22-predictions-from-polyglot-conference-vancouver
wp_id: 73339
original_url: https://compositecode.blog/2025/10/12/the-second-ofrder-effects-of-ai-acceleration-22-predictions-from-polyglot-conference-vancouver/
categories:
- AI & AI Tooling
tags:
- coding
- polyglot
- polyglot coders
- polyglotconf
- programming
excerpt: The Polyglot Conference in Vancouver featured a debate on the “Second Order Effects of AI Acceleration,” tackling 22 predictions about AI’s impact on software development. Discussions focused on issues like “vibe coding,” the rise of customized tools, and the importance of critical thinking in management. Concerns included the potential decline in code quality and long-term sustainability, alongside optimism for AI’s role in augmenting human creativity.
---

I just wrapped up attending an absolutely fascinating session at the Polyglot Conference here in Vancouver, BC. The talk was titled “Second Order Effects of AI Acceleration” and it was thought-provoking discussions – surface level and a little into the meat – that gets the brain gears turning. A room full of developers, architects, product, thinkers, and tech leaders debating predictions about where this AI acceleration is actually taking us.

The format was brilliant with fpredictions followed by arguments for and against each one. No hand-waving, no corporate speak, just real people with real experience hashing out what they think is coming down the pipe. I took notes on all 22 predictions and my immediate gut reactions to each one.

## 1. Far More Vibe Coded Outages

**My Reaction: Simple. I concur with the prediction.**

This one hits close to home. We’re already seeing the early signs of this phenomenon. “Vibe coding” – that delightful term for AI-assisted development where developers rely heavily on LLM suggestions without fully understanding the underlying logic – is becoming the norm in many shops. The problem isn’t the AI assistance itself, but the lack of deep understanding that comes with it.

When you’re building on top of code you don’t fully comprehend, you’re essentially creating a house of cards. One small change, one edge case, one unexpected input, and the whole thing comes crashing down. The outages won’t be dramatic server failures necessarily, but subtle bugs that cascade through systems built on shaky foundations.

The real issue here is that debugging vibe-coded systems requires a level of understanding that the original developers may not possess. You can’t effectively troubleshoot what you don’t understand, and that’s going to lead to longer resolution times and more frequent failures.

## 2. Companies Will More Often Develop Their Own Custom Tools

**My Reaction: 100% agreed, as I’ve already seen it happening in places I am working, which is evident anecdotally. However I’ve also seen evidence of fairly extensive glue code being put together via “vibe” coding in other places from Microsoft to Amazon to other places. All for better or worse.**

This is already happening at scale, and I’ve witnessed it firsthand. The traditional model of buying off-the-shelf solutions and adapting them is being replaced by rapid prototyping and custom development. Why? Because AI makes it faster and cheaper to build something tailored to your specific needs than to integrate and customize existing solutions.

But here’s the catch – we’re seeing a lot of “glue code” being generated. Not the elegant, well-architected solutions we’d hope for, but rather quick-and-dirty integrations that work for now but create technical debt for later. I’ve seen this pattern at Microsoft, Amazon, and other major tech companies where teams are rapidly prototyping solutions that work in the short term but lack the architectural rigor of traditional enterprise software.

The upside is innovation and speed. The downside is maintenance nightmares and the potential for significant refactoring down the road.

## 3. We’re in the VC Subsidized Phase of AI; Will Get More Expensive Like Uber + En-shittification

**My Reaction: I concur with this point too, which it is kind of odd that there is a agree or disagree here, since it is just the reality of the matter at current time. Eventually the cost, even with reduction in costs from efficiences and such, will go up just from the magnitude of what is being done. Efficiencies will only get us so far. The cost, will eventually have to go up, just as time consumption will start to go up around the organization and coordination of said tooling usage even though what can be done will exponentially grow. This entire specific prediction topic could and needs to be extensively expanded on.**

This is the elephant in the room that everyone’s trying to ignore. Right now, we’re in the honeymoon phase where AI services are heavily subsidized by venture capital, similar to how Uber operated in its early days. The prices are artificially low to drive adoption and build market share.

But here’s the reality: the computational costs of running these models at scale are enormous. The energy consumption alone is staggering. As usage grows exponentially, the costs will have to follow. We’re already seeing early signs of this with API rate limits and pricing adjustments from major providers.

The “enshittification” aspect is particularly concerning. As these services become essential infrastructure, providers will have increasing leverage to extract more value. We’ll see feature degradation, increased lock-in, and pricing that reflects the true cost of the service rather than the subsidized rate.

This deserves its own deep dive post – the economics of AI infrastructure are going to fundamentally reshape how we think about software costs.

## 4. Junior Developers Will Become Senior Developers More Rapidly

**My Reaction: Disagree and agree. The ramifications in the software engineering industry around this specific space is extensive. So much so, I’ll write an entirely new post just on this topic. It’s in the cooker, it’ll be ready soon!**

This is a nuanced prediction that I have mixed feelings about. On one hand, AI tools are democratizing access to complex programming concepts. A junior developer can now generate sophisticated code patterns, implement complex algorithms, and work with technologies they might not have encountered before.

But here’s the critical distinction: there’s a difference between being able to generate code and being able to architect systems, debug complex issues, and make sound technical decisions under pressure. The latter requires experience, pattern recognition, and deep understanding that can’t be accelerated by AI alone.

I’m seeing a concerning trend where junior developers are being promoted based on their ability to produce working code quickly, but they lack the foundational knowledge to handle the inevitable problems that arise. This creates a dangerous gap in our industry.

The real question is: are we creating a generation of developers who can build but can’t maintain, debug, or evolve systems? This topic is so complex and important that it deserves its own dedicated post.

## 5. Existing Programming Languages Will Form a Hegemony

**My Reaction: I mostly agree with this point. There may be some new languages that come up, and languages that more specifically allow for agents to communicate across paths without the need for human based languages and their respective error prone inefficiences.**

The programming language landscape is consolidating around a few dominant players. Python, JavaScript, Java, and C# are becoming the de facto standards for most development work. This consolidation is driven by several factors: AI training data is heavily weighted toward these languages, tooling and ecosystem maturity, and the practical reality that most developers need to work with existing codebases.

However, I think we’ll see some interesting developments in agent-to-agent communication languages. As AI systems become more sophisticated, they may develop their own protocols and languages optimized for machine-to-machine communication rather than human readability. These won’t replace human programming languages, but they’ll exist alongside them for specific use cases.

The hegemony isn’t necessarily bad – it reduces fragmentation and makes it easier to find talent and resources. But it also risks stifling innovation and creating monocultures that are vulnerable to specific types of problems.

## 6. Value of Contrarian People Will Be Higher Than Yes Men

**My Reaction: Agreed. Then of course those with a healthy dose of questions have always found a more useful path in society over time than the “yes men” type cowards. Politics in the US of course being an exception right now.**

This prediction resonates deeply with me. In an environment where AI can generate code, documentation, and even architectural decisions at the click of a button, the ability to question, challenge, and think critically becomes exponentially more valuable.

The “yes men” who simply implement whatever is suggested without critical analysis are becoming obsolete. AI can do that job better and faster. What AI can’t do is ask the hard questions: “Is this the right approach?” “What are the long-term implications?” “How does this fit with our broader strategy?”

Contrarian thinking becomes a competitive advantage because it’s the one thing that AI can’t replicate – genuine skepticism and independent thought. The people who can look at AI-generated solutions and say “wait, this doesn’t make sense” or “we’re missing something important here” will become increasingly valuable.

This is especially true in technical leadership roles where the ability to make nuanced decisions and see around corners becomes critical.

## 7. Shienification of Software (Software Will Become More Like Fast Fashion)

**My Reaction: I agree that this will start to happen, as US led capitalism tends toward a race to the bottom, sadly, and with all the negatives of fast fashion (there are a lot) this will happen with AI led software development. Everything from enshittification to the environmental negatives, this is going to happen and many in the industry can only do their best to mitigate the negatives.**

This is perhaps the most concerning prediction on the list. The “Shienification” of software refers to the trend toward disposable, quickly-produced software that follows the fast fashion model: cheap, trendy, and designed to be replaced rather than maintained.

We’re already seeing signs of this. AI makes it incredibly easy to generate new applications, features, and even entire systems. The barrier to entry is lower than ever, which means more software is being produced with less thought given to long-term sustainability.

The environmental impact is particularly troubling. The computational resources required to train and run AI models are enormous, and if we’re producing more disposable software, we’re essentially burning through resources for short-term gains.

The challenge for the industry is to resist this trend and maintain focus on building software that’s designed to last, evolve, and provide long-term value rather than quick wins.

## 8. Relative Value of Fostering Talent to Name Things Well Will Be More Important

**My Reaction: Under-reported prediction and NEED among skillsets. Using the right words at the right times for the right things in the right way are going to exponentially grow as a skillset need.**

This is a subtle but profound prediction that I think is being overlooked. In an AI-driven development environment, the ability to name things well becomes critical because it directly impacts how effectively AI can understand and work with your code.

Good naming conventions, clear abstractions, and well-defined interfaces become the difference between AI that can effectively assist and AI that generates confusing, unmaintainable code. The people who can create clear, semantic naming schemes and architectural patterns will become incredibly valuable.

This extends beyond just variable names and function names. It includes the ability to create clear APIs, well-defined data models, and intuitive system architectures that both humans and AI can understand and work with effectively.

The irony is that as AI becomes more capable, the human skills around communication, clarity, and semantic design become more important, not less.

## 9. Optimize LLM for Specific Use Cases

**My Reaction: Not sure this is a prediction, it’s already happening.**

This is already well underway. We’re seeing specialized models for coding (GitHub Copilot, Cursor), for specific domains (legal, medical, financial), and for particular tasks (code review, documentation generation, testing).

The trend toward specialization makes sense from both a performance and cost perspective. A general-purpose model trying to be good at everything will inevitably be mediocre at most things. Specialized models can be optimized for specific use cases, leading to better results and more efficient resource usage.

We’re also seeing the emergence of model composition, where different specialized models work together to handle complex tasks. This is likely to continue and accelerate as the technology matures.

## 10. Companies Will Die Faster Because We Can Replicate Functionality Faster

**My Reaction: Agreed.**

This is a natural consequence of lowered barriers to entry. If AI makes it easier and faster to build software, then it also makes it easier and faster to replicate existing functionality. This creates a more competitive landscape where companies need to move faster and innovate more aggressively to maintain their competitive advantage.

The traditional moats around software companies – technical complexity, development time, specialized knowledge – are being eroded by AI. What used to take months or years to build can now be prototyped in days or weeks.

This isn’t necessarily bad for consumers, who will benefit from more competition and faster innovation. But it’s challenging for companies that rely on technical barriers to entry as their primary competitive advantage.

The companies that survive will be those that can move fastest, adapt most quickly, and find new ways to create value beyond just technical implementation.

## 11. Existence of Non-Technical Managers Will Decrease

**My Reaction: I’m doubtful of this. If anything the use of AI will lower overall technical ability and will cause some significant issues around troubleshooting from lack of depth of those using the tooling to gloss over deep knowledge.**

I’m skeptical of this prediction. While AI might make it easier for non-technical people to generate code, it doesn’t necessarily make them better at managing technical teams or making technical decisions.

In fact, I think we might see the opposite trend. As AI tools become more accessible, we might see more people in management roles who can generate code but lack the deep technical understanding needed to make sound architectural decisions or troubleshoot complex issues.

The real challenge will be ensuring that technical managers have both the AI-assisted productivity tools and the foundational knowledge needed to make good decisions. Simply being able to generate code doesn’t make someone a good technical leader.

## 12. Vibe Code Will Cause a Return to Small Teams with Microservices

**My Reaction: Agree and disagree, in that order.**

I agree that vibe coding will drive architectural changes, but I’m not sure microservices is the inevitable result. The challenge with vibe-coded systems is that they’re often built without a clear understanding of the underlying architecture, which can lead to tightly coupled, monolithic systems that are hard to maintain.

However, the trend toward microservices might be driven more by the need to isolate failures and limit the blast radius of bugs in vibe-coded systems. If you can’t trust the code quality, you need to architect around that uncertainty.

The disagreement comes from the fact that microservices also require significant architectural discipline and understanding, which might be at odds with the vibe coding approach. We might see a different architectural pattern emerge that’s better suited to AI-assisted development.

## 13. Software Will Become a Living Conversation, Not a Static Thing

**My Reaction: Agree, more dynamic conversations form the speed increase will occur in many projects for some products and some services.**

This is already happening in many development environments. The traditional model of writing code, testing it, and deploying it is being replaced by a more iterative, conversational approach where developers work with AI to continuously refine and improve their systems.

The speed of iteration is increasing dramatically. What used to take days or weeks can now happen in hours or minutes. This allows for more experimentation, faster feedback loops, and more responsive development processes.

However, this also creates challenges around version control, testing, and deployment. If software is constantly evolving, how do you ensure stability and reliability? How do you manage the complexity of systems that are always changing?

## 14. Website Search Will No Longer Be Relevant in ~3 Years

**My Reaction: Is it now?**

This prediction seems to assume that website search is currently highly relevant, which I’m not sure is the case. Traditional web search has been declining in relevance for years as content has moved to social media, apps, and other platforms.

The rise of AI-powered search and information retrieval might accelerate this trend, but I think the real question is whether website search was ever as relevant as we thought it was. The future of information discovery is likely to be more conversational and contextual, driven by AI rather than traditional keyword-based search.

## 15. LLMs Will Be Software and Replace Stacks

**My Reaction: I’m not sure this isn’t the way it is already. The context and case and specificity isn’t really clear here.**

This prediction is a bit vague, but I think it’s referring to the idea that LLMs might become the primary interface for interacting with software systems, potentially replacing traditional APIs and user interfaces.

We’re already seeing early signs of this with AI-powered interfaces that can understand natural language and translate it into system actions. The question is whether this will extend to the point where traditional software stacks become obsolete.

I’m skeptical that this will happen completely, but I do think we’ll see more AI-native interfaces and interactions that make traditional software feel more conversational and intuitive.

## 16. (Software) Libraries Will Become Less Relevant

**My Reaction: Agreed.**

As AI becomes more capable of generating code from scratch, the need for pre-built libraries and frameworks may decrease. Why use a library when you can have AI generate exactly what you need, tailored to your specific use case?

This trend is already visible in some areas where developers are using AI to generate custom implementations rather than pulling in external dependencies. The benefits include reduced dependency management, smaller bundle sizes, and more control over the implementation.

However, this also means losing the benefits of community-maintained, battle-tested code. The challenge will be finding the right balance between custom generation and proven libraries.

## 17. In the Future Ads Will Become Even More Precise; LLMs Will Have More Info for Targeting

**My Reaction: Agreed. I hate this.**

This is perhaps the most dystopian prediction on the list. As LLMs become more sophisticated and have access to more personal data, they’ll be able to create incredibly targeted and persuasive advertising that’s tailored to individual users’ psychology, preferences, and vulnerabilities.

The privacy implications are enormous. We’re already seeing early signs of this with AI-powered ad targeting that can analyze user behavior and create personalized content. As the technology improves, this will become even more sophisticated and invasive.

This is a trend that I find deeply concerning from both a privacy and societal perspective. The ability to manipulate individuals through highly targeted, AI-generated content represents a significant threat to autonomy and informed decision-making.

## 18. There Will Be a Standardization of Information Architecture Which Will Allow Faster Iteration of Tooling

**My Reaction: Doubtful. If humanity and industry hasn’t done this already I see no reason we’ll do it now.**

This prediction assumes that we’ll finally achieve the standardization that we’ve been trying to implement for decades. While AI might make it easier to work with standardized formats and protocols, I’m skeptical that it will drive the kind of widespread adoption needed for true standardization.

The history of technology is full of failed standardization attempts. Even when standards exist, they’re often ignored or implemented inconsistently. AI might make it easier to work with existing standards, but it won’t necessarily create the political and economic incentives needed for widespread adoption.

## 19. LLMs Will Cause a Dearth of New Innovation

**My Reaction: I fear that this could happen, in some ways. But in other ways I think humanity can and will be forced – with the culmination of AI, the toxic immolation of democracies, and other horrors facing the world right now – we’ll innovate, change, and hopefully for the better in ways we don’t even grasp with these massive triggers effecting us.**

This is a complex prediction that touches on fundamental questions about human creativity and innovation. On one hand, if AI can generate solutions to most problems, there might be less incentive for humans to engage in the kind of deep, creative thinking that leads to breakthrough innovations.

On the other hand, the challenges we’re facing as a society – climate change, political instability, economic inequality – are so profound that they might force innovation in ways we can’t currently imagine. The combination of AI capabilities and existential threats might actually accelerate innovation rather than stifle it.

The key question is whether AI will augment human creativity or replace it. I’m optimistic that it will be the former, but it’s not guaranteed.

## 20. AIs Will Invent Own Programming Language

**My Reaction: Agreed. I believe to some degree they already have.**

This is already happening in subtle ways. AI systems are developing their own internal representations and communication protocols that are optimized for machine-to-machine interaction rather than human readability.

As AI systems become more sophisticated and need to work together, they’ll likely develop more formal languages and protocols for communication. These won’t replace human programming languages, but they’ll exist alongside them for specific use cases.

The interesting question is whether these AI-invented languages will be more efficient or expressive than human-designed languages, and whether humans will eventually adopt them for certain types of programming tasks.

## 21. Some Countries Will Make AI Access a Universal Right

**My Reaction: Agreed. While others will block it, ban it, and control it and shape it to further attack and rewrite known narratives the world accepts as positives.**

This prediction reflects the growing recognition that AI access is becoming a fundamental requirement for participation in modern society. Just as internet access has become essential for education, employment, and civic participation, AI access is following the same trajectory.

Some countries will embrace this and provide universal access to AI tools and services, recognizing it as a public good. Others will restrict access, either for political reasons or to maintain control over information and communication.

The geopolitical implications are significant. Countries that provide universal AI access will have a competitive advantage in education, innovation, and economic development. Those that restrict it will fall behind.

## 22. Languages Used for Strengths More Than as a Panacea

**My Reaction: “Languages used for strengths more than as a panacea.” I added this one. It’s more a hope than a prediction. For example, I hope Go is used for its strengths, Rust for its strengths, Java, C#, etc. Instead of trying to make C# or Rust the panacea across all platforms and all needs. One can hope!**

This is my addition to the list, and it’s more of a hope than a prediction. In an AI-driven development environment, there’s a risk that we’ll default to whatever language the AI is most comfortable with, rather than choosing the right tool for the job.

I hope that AI will actually help empower us to make better language choices by understanding the strengths and weaknesses of different languages and recommending the most appropriate one for each use case. Go for its concurrency and simplicity, Rust for its safety and performance, Java for its enterprise ecosystem, C# for its Microsoft integration, and so on.

The goal should be to use each language for what it does best, rather than trying to make one language solve every problem. AI could actually help us achieve this by providing better guidance on language selection and architecture decisions.

## The Big Picture

These 22 predictions all of us participants conjured up paint a picture of an industry in rapid transformation. Some trends are already visible, others are still emerging. The common thread is that AI is fundamentally changing how we think about software development, from the tools we use to the way we organize teams and make decisions – all for better or worse.f

The challenge for the industry is to navigate these changes thoughtfully, preserving what’s valuable about traditional software development while embracing the opportunities that AI presents. The predictions that concern me most are those that suggest a race to the bottom in terms of quality, sustainability, and long-term thinking.

The predictions that excite me most are those that suggest AI will augment human capabilities rather than replace them, enabling us to be more creative and experimental in our solutions while preserving the critical thinking and problem-solving skills that make good developers valuable.

As we move forward, the key will be maintaining our focus on building software that’s not just functional, but sustainable, maintainable, and valuable in the long term. AI can help us build faster, but it can’t replace the judgment and wisdom needed to build well.

---

*What are your thoughts on these predictions? Which ones resonate with your experience, and which ones seem off-base? I’d love to hear your perspective on where you think AI is taking our industry.*

I’m @ Mastadon <https://metalhead.club/@adron>, Threads <https://www.threads.com/@adron>, and Blue Sky <https://bsky.app/profile/adron.bsky.social> – hit me up with your thoughts!
