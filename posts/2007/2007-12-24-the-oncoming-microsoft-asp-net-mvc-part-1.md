---
title: The Oncoming Microsoft ASP.NET MVC – Part 1
date: 2007-12-24 20:11:00 +0000
last_modified_at: 2007-12-24 20:11:00 +0000
permalink: /2007/12/24/the-oncoming-microsoft-asp-net-mvc-part-1/
slug: the-oncoming-microsoft-asp-net-mvc-part-1
wp_id: 363
original_url: https://compositecode.blog/2007/12/24/the-oncoming-microsoft-asp-net-mvc-part-1/
categories:
- Uncategorized Bits
tags: []
excerpt: The ASP.NET MVC is officially released in the .NET 3.5 Extensions CTP. This is part one of a multi-part series I’m going to do on getting a basic application up and running with good practice and solid test driven development process. Enjoy. First we’ll go over a quick review. What is MVC? MVC stands for …
---

The [ASP.NET](http://www.asp.net) MVC is officially released in the [.NET 3.5 Extensions CTP](http://asp.net/downloads/3.5-extensions/).  This is part one of a multi-part series I’m going to do on getting a basic application up and running with good practice and solid test driven development process.  Enjoy.

First we’ll go over a quick review.  What is MVC?  MVC stands for the model view controller pattern.

- The **Model** in an MVC pattern are the components of the application that are responsible for maintaining state.- The **View** in this pattern are the parts responsible for displaying the application’s user interface.- The **Controller** in this pattern are responsible for handling end user interaction.  Manipulating the model and choosing a view to render for the UI is also part of the responsibilities of the controllers.

In each of the above parts of the pattern, you could have multiple models, views, or controllers depending on the need and setup of the application.

Some of the absolutely kick ass benefits of the MVC pattern include;

- To me, one of the largest benefits of the MVC pattern is the separation of concerns.  I’ve ranted and raved about the need for a separation of concerns in some of my other blog entries.  This is fundamental to maintainable, easy to understand, and easy to read code.  Without a clear separation of concerns it is easy to toss out all three; maintainability, understanding, and readability.- The new MVC does not use the post back model for server interactions.  What is used is interactions with a controller class which enables the above mentioned separation of concerns and testing.- Unit testing and test driven development are easily implemented with the MVC pattern.  Especially so with this particular implementation of the pattern.  All the contracts within the framework are interface declared and easily mock-able.  Unit testing the application can be done without needing to run the controllers within the ASP.NET process making them turbo fast.- Dependency injection and inversion of control container models can be integrated and used.  This could include Windsor, [Spring.NET](http://www.springframework.net/), [NHibernate](http://www.hibernate.org/), probably even StructureMap or others.

So with all this awesomeness released finally I’ve set out to build my first ASP.NET MVC How To.  Since I’ve been needing to rebuild my Transportation Tracker Application I decided that would be my first ASP.NET MVC Candidate for building.  This quick tutorial is going to assume that you have Visual Studio 2008 installed and the .NET 3.5 Extensions CTP mentioned above installed already.  In addition to these things I’m also assuming that we all have [Rhino Mocks](http://www.ayende.com/projects/rhino-mocks/downloads.aspx) installed.  If not, get it.

**Spring.NET Framework**

Go hit up the [Spring.net Framework](http://www.springframework.net/).  Download that and install it, making sure to have Visual Studio 2008 closed.  Once you’ve got that installed we’re ready to go.  Click on the images to see the full size versions.

[![](https://adronhall.smugmug.com/photos/234418133-Ti.png)](http://adronhall.smugmug.com/gallery/4027372/1/234418133)[![](https://adronhall.smugmug.com/photos/234418135-Ti.png)](http://adronhall.smugmug.com/gallery/4027372/1/234418135)[![](https://adronhall.smugmug.com/photos/234418143-Ti.png)](http://adronhall.smugmug.com/gallery/4027372/1/234418143)[![](https://adronhall.smugmug.com/photos/234418161-Ti.png)](http://adronhall.smugmug.com/gallery/4027372/1/234418161)[![](https://adronhall.smugmug.com/photos/234418165-Ti.png)](http://adronhall.smugmug.com/gallery/4027372/1/234418165)[![](https://adronhall.smugmug.com/photos/234418170-Ti.png)](http://adronhall.smugmug.com/gallery/4027372/1/234418170)[![](https://adronhall.smugmug.com/photos/234418131-Ti.png)](http://adronhall.smugmug.com/gallery/4027372/1/234418131)

**Creating the Project**

First step after all that installation mess is to get a project and the proper test project created!  Just open up Visual Studio 2008 and click on file, then new so the new project dialog appears.  Name the project whatever you’d like to at this point.  Same thing with these images, click em’ if you want to see the full size ones.

[![](https://adronhall.smugmug.com/photos/234418277-S.png)](http://adronhall.smugmug.com/gallery/4027372/1/234418277)[![](https://adronhall.smugmug.com/photos/234418279-S.png)](http://adronhall.smugmug.com/gallery/4027372/1/234418279)

Once you’ve created the project with the test project, then create some initial model, view, and controller files that will be the basis of the application.  The first few I created are the interfaces for the model classes;

[![](https://adronhall.smugmug.com/photos/234418368-S.png)](http://adronhall.smugmug.com/gallery/4027372/2/234418368)[![](https://adronhall.smugmug.com/photos/234418371-S.png)](http://adronhall.smugmug.com/gallery/4027372/2/234418371)

[![](https://adronhall.smugmug.com/photos/234955438-S.png)](http://adronhall.smugmug.com/gallery/4027372/1/234955438)

Following the interfaces I created the model class files.  At this point I have a Solution Explorer Tree that looks like the image below.

[![](https://adronhall.smugmug.com/photos/234955446-M.png)](http://adronhall.smugmug.com/gallery/4027372/1/234955446)

Next create the necessary controllers for the application.  I’m going to break this apart into each separate section of the application that I will have data manipulation.  Each of these sections is basically a separate page with specific flow and data characteristics on each page.

[![Creating new files and code 03](https://adronhall.smugmug.com/photos/234955442-S.png)](http://adronhall.smugmug.com/gallery/4027372/1/234955442 "Creating new files and code 03")

Note when you are creating the MVC Controller Classes that there is a template item specifically for creating these that cut out some of the work for you, albeit a small amount.  What you get is a few attributes marking the class and initial void that is put in place for you.

> public class TripController : Controller
> {
>
>     [ControllerAction]
>     public void Index()
>     {
>         //Add code action logic here
>     }
> }

After adding each of the controllers I’ve got; LocationController, TransitModeController, TripController, TripPurposeController, TripTypeController, and the HomeController that was already generated by the template for me.  Since I’m trying to maintain my test driven development methodologies these days, I’m going to add a quick few pieces of code so that I can get something building and add some tests.

I added the following tests for the HomeController to assure that the proper items where setup and displaying properly.  Of course since I’m doing TDD, and I have none of this implemented yet, none of the tests will pass.  The following is my t
est code;

> using System;
> using System.Text;
> using System.Collections.Generic;
> using System.Linq;
> using Microsoft.VisualStudio.TestTools.UnitTesting;
> using MvcApplication.Controllers;
>
> namespace MvcApplicationTest.Controllers
> {
>     [TestClass]
>     public class TransportationControllerTests
>     {
>         [TestMethod]
>         public void HomeControllerSelectsCorrectViewTripType()
>         {
>             HomeControllerDouble controller = new HomeControllerDouble();
>             controller.TripTypes();
>             Assert.AreEqual(“TripType”, controller.SelectedView);
>         }
>
>         [TestMethod]
>         public void HomeControllerSelectsCorrectViewTrip()
>         {
>             HomeControllerDouble controller = new HomeControllerDouble();
>             controller.Trips();
>             Assert.AreEqual(“Trip”, controller.SelectedView);
>         }
>
>         [TestMethod]
>         public void HomeControllerSelectsCorrectViewTripPurpose()
>         {
>             HomeControllerDouble controller = new HomeControllerDouble();
>             controller.TripPurpose();
>             Assert.AreEqual(“TripPurpose”, controller.SelectedView);
>         }
>
>         [TestMethod]
>         public void HomeControllerSelectsCorrectViewTransitModes()
>         {
>             HomeControllerDouble controller = new HomeControllerDouble();
>             controller.TransitModes();
>             Assert.AreEqual(“TransitMode”, controller.SelectedView);
>         }
>
>         [TestMethod]
>         public void HomeControllerSelectsCorrectViewHome()
>         {
>             HomeControllerDouble controller = new HomeControllerDouble();
>             controller.Index();
>             Assert.AreEqual(“Index”, controller.SelectedView);
>         }
>
>         [TestMethod]
>         public void HomeControllerSelectsCorrectViewAbout()
>         {
>             HomeControllerDouble controller = new HomeControllerDouble();
>             controller.About();
>             Assert.AreEqual(“About”, controller.SelectedView);
>         }
>
>         [TestMethod]
>         public void HomeControllerSelectsCorrectLocation()
>         {
>             HomeControllerDouble controller = new HomeControllerDouble();
>             controller.Location();
>             Assert.AreEqual(“Location”, controller.SelectedView);
>         }
>
>         private class HomeControllerDouble : HomeController
>         {
>             public HomeControllerDouble()
>                 : base()
>             { }
>
>             public string SelectedView { get; private set; }
>             public object RenderedViewData { get; private set; }
>
>             protected override void RenderView(string viewName
>               , string masterName
>               , object viewData)
>             {
>                 this.SelectedView = viewName;
>                 this.RenderedViewData = viewData;
>             }
>         }
>     }
> }

Now that there are some tests to verify each of the different areas I’m going to move on to wiring these sections up.  After editing the HomeController.cs the code looks like the following;

> using System;
> using System.Web;
> using System.Web.Mvc;
>
> namespace MvcApplication.Controllers
> {
>     public class HomeController : Controller
>     {
>         [ControllerAction]
>         public void Index()
>         {
>             RenderView(“Index”);
>         }
>
>         [ControllerAction]
>         public void About()
>         {
>             RenderView(“About”);
>         }
>
>         [ControllerAction]
>         public void TransitModes()
>         {
>             RenderView(“TransitMode”);
>         }
>
>         [ControllerAction]
>         public void Trips()
>         {
>             RenderView(“Trip”);
>         }
>
>         [ControllerAction]
>         public void TripPurpose()
>         {
>             RenderView(“TripPurpose”);
>         }
>
>         [ControllerAction]
>         public void TripTypes()
>         {
>             RenderView(“TripType”);
>         }
>
>         [ControllerAction]
>         public void Location()
>         {
>             RenderView(“Location”);
>         }
>     }
> }

Now we have a compiling, unit test executing, running application.  Albeit there isn’t a whole bunch of use to the thing yet.  Next thing we’ll do is setup some testing that will utilize the [Rhino Mocks](http://www.ayende.com/projects/rhino-mocks/downloads.aspx) framework.  Keep in mind while working through this that we’re doing test driven development.  We get a test written, it tosses a red light, we then fix it so that we get a green light.  On and on goes the process.  The first test I’m going to write is for the TransitMode section of the application.  Create a file in the unit tests project folder called TransitModeControllerTest.cs.  After you’ve completed the code for this file, change the create the TransitModeController.cs file in the Controllers Directory.

> using System;
> using System.Collections.Generic;
> using System.Web;
> using System.Web.Mvc;
> using MvcApplication.Models;
>
> namespace MvcApplication.Controllers
> {
>     public class TransitModeController : Controller
>     {
>         ITransitMode transitModeRepository;
>
>         public TransitModeController(ITransitMode repository)
>         {
>             this.transitModeRepository = repository;
>         }
>
>         [ControllerAction]
>         public void TransitModesView()
>         {
>             // TODO: Add functional code after test is created.
>         }
>     }
> }

Now that you have skeleton of the controller created we have to get a red light test.  Make before going on to the test that the interface is created.  The code for it should look like the listing below.

> using System.Collections.Generic;
>
> namespace MvcApplication.Models
> {
>     public interface ITransitMode
>     {
>         void Create(TransitMode transitMode);
>
>         IList ListTransitModes();
>     }
> }

Open that TransitModeControllerTest.cs file
back up and add the code listed below.  Once completed run the test, and accordingly it should fail.

> using System;
> using System.Text;
> using System.Collections.Generic;
> using System.Linq;
> using Microsoft.VisualStudio.TestTools.UnitTesting;
> using MvcApplication.Controllers;
> using MvcApplication.Models;
> using Rhino.Mocks;
>
> namespace MvcApplicationTest.Controllers
> {
>     [TestClass]
>     public class TransitModeControllerTest
>     {
>         [TestMethod]
>         public void TransitModeControllerPassesCorrectViewData()
>         {
>             MockRepository mocks = new MockRepository();
>             ITransitMode transitModeRepository = mocks.DynamicMock();
>             SetupResult
>               .For(transitModeRepository.ListTransitModes())
>               .IgnoreArguments()
>               .Return(new List(new TransitMode[] { new TransitMode(), new TransitMode(), new TransitMode() }));
>             mocks.ReplayAll();
>
>             TransitModeControllerDouble controller = new TransitModeControllerDouble(transitModeRepository);
>             controller.TransitModesView();
>             IList transitModes = (IList)controller.RenderedViewData;
>             Assert.AreEqual(3, transitModes.Count, “Expected three modes.”);
>         }
>
>         private class TransitModeControllerDouble : TransitModeController
>         {
>             public TransitModeControllerDouble(ITransitMode transitMode)
>                 : base(transitMode)
>             { }
>
>             public string SelectedView { get; private set; }
>             public object RenderedViewData { get; private set; }
>
>             protected override void RenderView(string viewName
>               , string masterName
>               , object viewData)
>             {
>                 SelectedView = viewName;
>                 RenderedViewData = viewData;
>             }
>         }
>     }
> }

That gives us our red light test.  Now for the green light.  Add the code in bold below to the TransitModeController.cs file.  Running the test again will give you a green light test.  For now that gives us a good start.

> using System.Collections.Generic;
> using System.Web.Mvc;
> using MvcApplication.Models;
>
> namespace MvcApplication.Controllers
> {
>     public class TransitModeController : Controller
>     {
>         ITransitMode transitModeRepository;
>
>         public TransitModeController(ITransitMode repository)
>         {
>             this.transitModeRepository = repository;
>         }
>
>         [ControllerAction]
>         public void TransitModesView()
>         {
>             IList transitModes = transitModeRepository.ListTransitModes();
>             RenderView(“TransitModes”, transitModes);
>         }
>     }
> }

That’s it for now.  Merry Christmas, enjoy the code, and I’ll take it from this point forward for my next entry!

Technorati Tags: [ASP.NET](http://technorati.com/tags/ASP.NET),[ASP](http://technorati.com/tags/ASP),[C#](http://technorati.com/tags/C#),[MVC](http://technorati.com/tags/MVC),[Model View Controller](http://technorati.com/tags/Model%20View%20Controller)

del.icio.us Tags: [ASP.NET](http://del.icio.us/popular/ASP.NET),[ASP](http://del.icio.us/popular/ASP),[C#](http://del.icio.us/popular/C#),[MVC](http://del.icio.us/popular/MVC),[Model View Controller](http://del.icio.us/popular/Model%20View%20Controller)

[![kick it on DotNetKicks.com](http://www.dotnetkicks.com/Services/Images/KickItImageGenerator.ashx?url=http%3a%2f%2fadronbhall.com%2fblogs%2ftechnology__software_development%2farchive%2f2007%2f12%2f25%2f6062.aspx&bgcolor=0033FF&cfgcolor=CC0033)](http://www.dotnetkicks.com/kick/?url=http%3a%2f%2fadronbhall.com%2fblogs%2ftechnology__software_development%2farchive%2f2007%2f12%2f25%2f6062.aspx)
