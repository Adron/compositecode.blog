---
title: The Oncoming Microsoft ASP.NET MVC with Some LINQ Tossed In – Part 2
date: 2008-01-31 13:57:00 -0800
last_modified_at: 2008-01-31 13:57:00 -0800
permalink: /2008/01/31/the-oncoming-microsoft-asp-net-mvc-with-some-linq-tossed-in-part-2/
slug: the-oncoming-microsoft-asp-net-mvc-with-some-linq-tossed-in-part-2
wp_id: 342
original_url: https://compositecode.blog/2008/01/31/the-oncoming-microsoft-asp-net-mvc-with-some-linq-tossed-in-part-2/
categories:
- Uncategorized Bits
tags: []
excerpt: In the first part of this series I went over how to create a basic skeleton of controllers and models so that we could create a mock test and get it green lighted along with some other tests for getting the basic navigation methods tested and green lighted. In this part of the series I'm …
---

In the [first part of this series](http://adronbhall.com/blogs/technology__software_development/archive/2007/12/25/6062.aspx) I went over how to create a basic skeleton of controllers and models so that we could create a mock test and get it green lighted along with some other tests for getting the basic navigation methods tested and green lighted.  In this part of the series I'm going to go over the model from a LINQ point of view.  After that in subsequent parts of this series I'll start building out the views, utilizing of course a test driven development process.  So no more blabbering, let's code.

LINQ is definitely going to change the world of development for a lot of people.  Maybe not so much for people who have been using generated OR/M software for a while.  The idea of actual business objects and linking business logic onto the actual data in a database isn't particularly new, but it is ridiculously useful when writing code.  In addition there are dozens of other benefits too; reduced ramp up time for developers on the data schema, less meddling by the coders in the DBA's space, and the list continues.

So what I'm going to go over now includes setting up some real model data, schema, and LINQing it to the actual model classes.  I won't really do everything in good practice right off as I am initially just going to get it to work.  I'm still unfamiliar enough using LINQ that I'm not even 100% sure yet what good practice is using this particular OR/M.  After that in some subsequent sections I will then apply additional good practice and probably add more unit tests.

First thing to do is setup a schema like the one I've displayed in the image below.  Click on the image to get a full size original of the image.

[![The Database Schema](https://adronhall.smugmug.com/photos/249447441-L.png)](http://adronhall.smugmug.com/gallery/4145533/1/249447441)

Once you've created that image then we'll setup a view that will be used for displaying the correlated data all together.  To do this I created a view based on the select statement below.

> SELECT       
>      Trip.TripId,
>      Purpose.Purpose,
>      [Type Of Trip].TripType,
>      Trip.Name,
>      Trip.Notes,
>      Trip.Mileage,
>      Trip.DateOfTrip,
>      Origination.FullName AS Origination,
>      Origination.AbbreviationCode AS OriginationAbbreviation,
>      Desination.FullName AS Destination,
>          Desination.AbbreviationCode AS DestinationAbbreviation
>  FROM            dbo.tt\_Trips AS Trip
>      INNER JOIN    dbo.tt\_TripPurpose AS Purpose ON Trip.PurposeId = Purpose.PurposeId
>      INNER JOIN    dbo.tt\_TripTypes AS [Type Of Trip] ON Trip.TypeId = [Type Of Trip].TypeId
>      LEFT OUTER JOIN    dbo.tt\_Locations AS Origination ON Trip.OriginationLocationId = Origination.LocationId
>      LEFT OUTER JOIN dbo.tt\_Locations AS Desination ON Trip.DestinationLocationId = Desination.LocationId

Once the view is created then add a new LINQ dbml file to your project.  The image below shows the LINQ to SQL file which I've named Transportation.dbml.

[![Adding a New LINQ to SQL Class File](https://adronhall.smugmug.com/photos/249447446-M.png)](http://adronhall.smugmug.com/gallery/4145533/1/249447446)

When the file is added click on the plus beside the file and you'll see we also have the Transportation.dbml.layout and Transportation.designer.cs files.  What you see displayed when you open the .dbml file is actually the .layout file.  The layout file is where you will drag and design you objects derived from the database.

Now open up the server explorer and the database you've created the schema in.  Now select all of the tables and views, then drag and drop them into the Transportation.dbml layout page.

[![Database Objects to Drag](https://adronhall.smugmug.com/photos/249515712-S.png)](http://adronhall.smugmug.com/gallery/4145533/1/249515712)[![Drag to This Point](https://adronhall.smugmug.com/photos/249515717-S.png)](http://adronhall.smugmug.com/gallery/4145533/1/249515717)

When you're done you should have a diagram representation as displayed below.  These are now the objects that you have for your model.

[![Model Objects](https://adronhall.smugmug.com/photos/249515722-L.png)](http://adronhall.smugmug.com/gallery/4145533/1/249515722)

Before moving on to the tests, do a quick rebuild all just to make sure all the pieces are still working.

[![Rebuild Context Menu](https://adronhall.smugmug.com/photos/249515728-S.png)](http://adronhall.smugmug.com/gallery/4145533/1/249515728)

If any errors pop up feel free leave a comment.  I ran into a few fiddling around with all of this and could easily help out.

Once you have your entities created we're ready to test these to make sure we have good in and out with the actual database.  The following example isn't using any of the fancy unit testing frameworks or mocking, what I'm going to do – since I too am still getting familiar with the LINQ technology pieces – is literally to write out some tests that do clean inserts, updates, and deletes.  With that said, lets get going.

First off for the testing project I had to add the following using statements to the test class.

> using System.Linq;
>  using MvcApplication;
>  using MvcApplication.Models;

I had to also add the linq reference also since it isn't included by default in the test framework.  The Models namespace I had to add also.   The MvcApplication part was added when I created the solution back in the first part of this series.

The first test I wrote is for testing the location, with a really straight forward get of a single item, if it doesn't exist I create the object and stick it in the database.  Finally the last part has an assertion to verify the proper objects are the same.

> [TestMethod]
>  public void CheckInsertAndDataForLocationEntity()
>  {
>      TransportationDataContext transportationDb = new TransportationDataContext(@"Data Source=ADRON-PC\SQLEXPRESS;Initial Catalog=transitTracker;Integrated Security=True;Pooling=False");
>
>     tt\_Location location = transportationDb.tt\_Locations.Single(l => l.FullName == "Portland");
>
>     if (location.FullName != "Portland")
>      {
>          location.FullName = "Portland";
>          location.AbbreviationCode = "PDX";
>          location.Note = "PDX is the airport and railroad station code for Portland, Oregon.";
>          location.LocationId = Guid.NewGuid();
>          transportationDb.tt\_Locations.InsertOnSubmit(
> location);
>          transportationDb.SubmitChanges();
>      }
>
>     tt\_Location getPortland = transportationDb.tt\_Locations.Single(l => l.FullName == "Portland");
>
>     Assert.AreEqual(location, getPortland);
>  }

Note that the context object (transportationDb) has the "SubmitChanges()" method on it.  The "InsertOnSubmit(entity)" is located on the static object of the entity type located on the context object.  This seems kind of illogical at first, but it works.  I've seen a few other ways that an insert like this is done, but I'm not sure which is truly a preferred way to do it.  I'm sure in the very near future though I'll either figure out the preferred way or find some material written up about it.

At this point I wrote a few more tests, but since they're crude as the one above, I'll leave them for the reader to build themselves.  I've downloaded mbUnit though to do some nice mocking tests and have started looking at some ways to unit test LINQ with mocks so it can be a really solid test layer.

So stay tuned for part three where I'll go over the creation of the views.  Once I'm done with the views it will then be time to head off into the integration world and get all this loosely coupled directly injected inversion of control stuff to work together.

[![kick it on DotNetKicks.com](http://www.dotnetkicks.com/Services/Images/KickItImageGenerator.ashx?url=http%3a%2f%2fadronbhall.com%2fblogs%2ftechnology__software_development%2farchive%2f2008%2f01%2f31%2f6182.aspx&bgcolor=3333FF&cfgcolor=CC3300)](http://www.dotnetkicks.com/kick/?url=http%3a%2f%2fadronbhall.com%2fblogs%2ftechnology__software_development%2farchive%2f2008%2f01%2f31%2f6182.aspx)
