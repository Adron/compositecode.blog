---
title: HighBall Part Duex (#4) Patterns
date: 2009-04-13 02:40:00 -0700
last_modified_at: 2014-01-08 17:17:25 -0800
permalink: /2009/04/13/highball-part-duex-4-patterns/
slug: highball-part-duex-4-patterns
wp_id: 618
original_url: https://compositecode.blog/2009/04/13/highball-part-duex-4-patterns/
categories:
- .NET Bits
- How-to
tags:
- c#
- csharp
- dependency injection
- silverlight
excerpt: 'Navigation of Highball Series Part #1 | Part #2 | Part #3 | Part #4 Here in part #4 I want to cover the final wire up I did to get the initial screens to show. The other primary focus of this blog entry is to cover some of the architectural patterns behind what I have so far. We haven’t …'
---

Navigation of Highball Series [Part #1](/2009/03/30/highball-part-duex-01/) | [Part #2](/2009/04/01/highball-part-duex-02-adding-the-composite-application-libraries/) | [Part #3](/2009/04/12/highball-part-duex-3-wiring-up-silverlight/) | [Part #4](/2009/04/13/highball-part-duex-4-patterns/)

Here in part #4 I want to cover the final wire up I did to get the initial screens to show.  The other primary focus of this blog entry is to cover some of the architectural patterns behind what I have so far.  We haven’t touched upon testing this yet, primarily because I’m stepping through wiring both Silverlight & WPF with these libraries for the first time.  I’ve done the WPF before, but not both.  Soon enough, I’ll get back to good standard practice and get some tests done first.  But for now, here’s the low down on wiring up Silverlight and the architectural patterns so far.

### Architectural Patterns & Ideas

**Dependency Injection**

This is one of interesting parts of the application, at least to me.  For many the dependency injection is endlessly confusing, but it comes in immensely helpful in getting things loosely coupled and all wired up.  Because even when you decouple things, they do have to get wired up again – it’s just the how that’s important.  Below is an example of a presenter in the schedule module that uses constructor based dependency injection.  Dig it?  I’ll have another follow up entry in the future about what and how Dependency Injection works, along with the respective Dependency Inversion, Inversion of Control, and all those other patterns.  For now, just now that this is how the view gets registered with the region that is responsible for displaying it when the application runs.

```csharp
public class ScheduleViewAllPresenter : IModule
{
    private readonly IRegionViewRegistry regionViewRegistry;

    public ScheduleViewAllPresenter(IRegionViewRegistry registry)
    {
        regionViewRegistry = registry;
    }

    public void Initialize()
    {
        regionViewRegistry.RegisterViewWithRegion("HighBallMainRegion", typeof(ScheduleViewAllView));
    }
}
```

In the code snippet above you’ll see in the initialize method that the view that is injected is registered to the particular region that it will be displayed in.  In the shell the view will be displayed in the region as shown below.

**Composite Modules**

I’ve added a single module to the solution so far.  This module has two views & their respective presenters, which I’ll cover in the section below.  The module is simply a project, loosely coupled, that will provide a view and the presentation logic for that view to be injected into the shell upon some application logic.

The module itself isn’t so much a pattern but more an architectural piece of the application.  As I move forward on this project I’ll add more modules to the solution as functionality is needed.  Each module will have an isolated, or mostly isolated, business use.  The first example that I have is the *HighBall.Interface.Modules.ScheduleModule*.  I’ll be adding more, probably along these lines;  mileage tracking, vehicle inventory, driver check-in, driver route choice, etc.  Each having a particular part of functionality that will primarily be isolated to itself.

When the CAL is used within a development team the modules would most likely be split off to individual pairs in the case of Agile, or even entire teams.  In Agile parlance each module would be a number of user stories, or in the most simple form, a single user story.

**View & Presenter**, with no **Model** yet.

The view and presenter are where you get to see the Model View Presenter (MVP) first start to appear.  Eventually as I move forward there will be the model, and more elaboration on the view and presenter.  For now all we have is the view, which is just the xaml markup and the presenter which is responsible for registering the view in the registry, and initializing the view with a region that it would be displayed in.  As you can see above in the Dependency Injection example the presenter is very thin at this point.

So that summarizes the cut off point for my first basic release of [HighBall](http://highball.codeplex.com).  Check out the [code release](http://highball.codeplex.com/Release/ProjectReleases.aspx?ReleaseId=26044), rant at me about deficiencies, and if you have any additional ideas or other elaborations you’d like to see please do comment.

Currently I’m researching how to put TDD into effect to build the presenters, views, and other composite pieces of this application.  My next entry will have several examples of unit tests that aren’t currently included in this release.  Until then, happy hacking (or coding).
