---
title: 'Setting Sail with the Smuggling Pattern :: Part 1'
date: 2008-08-15 07:21:27 -0700
last_modified_at: 2008-08-15 07:21:27 -0700
permalink: /2008/08/15/setting-sail-with-the-smuggling-pattern-part-1/
slug: setting-sail-with-the-smuggling-pattern-part-1
wp_id: 252
original_url: https://compositecode.blog/2008/08/15/setting-sail-with-the-smuggling-pattern-part-1/
categories:
- Uncategorized Bits
tags: []
excerpt: Maybe because I’m often entertained by the geekiest of things, I’ve started usage of the Smuggling Pattern named after a fellow software architect Matt Davis’s terminology of smuggling data into and out of Excel. It is something that I’ve lately needed to do on a regular basis, get data into and out of Excel without …
---

Maybe because I’m often entertained by the geekiest of things, I’ve started usage of the Smuggling Pattern named after a fellow software architect Matt Davis’s terminology of smuggling data into and out of Excel.  It is something that I’ve lately needed to do on a regular basis, get data into and out of Excel without Excel, or at least the evil COM Interop Model, really knowing what is going on.  In other words, I want total programmatic control over data so I can trust it versus Excel mangling my poor data up.  This is what the Smuggling Pattern is going to do for me, and it is doing it well.

Now you might think, “WTF!”  But just to clarify, the Smuggling Pattern is really the Builder Pattern that we architects know and love with a cooler more fun more pirate like name!  So with that, here’s some of that code, and the TDD process I undertook to get this sucker built to set sail.

First I created a C# Class Project and created the following file folder structure and files.

[![](/images/adronhall.smugmug.com/photos/352400008_4k2eh-M.png)](http://adronhall.smugmug.com/gallery/5711024_NKtkk/1/352400008_4k2eh)

Once I completed that I jumped right into testing.  Of course with ReSharper it makes life so much friggin simpler, in addition to TDD making life simpler.  I do still admit, that if you’re not practiced at TDD, then doing tests in whatever order you are comfortable with still keeps you at peak performance.  But eventually you should work toward TDD and toss in a great tool like ReSharper.  The difference in speed and quality is almost like getting 2 of the 3 engineering axioms instead of just 1 (i.e. speed, quality, & cost).

The first tests I started on where the individual builder tests, or in my case the Smuggler Object.  I always create a check for null just to make sure that I named the file correctly, kind of a double check, and it gives me the attribute, category, and other parts that I can copy to the other tests easily.

```
using Production.Smugglers.Builders;
using NUnit.Framework;

namespace Production.Tests
{
    [TestFixture]
    public class SmugglerTests
    {
        [Test, Category("Builder Tests")]
        public void TestsSmugglerIsNotNull()
        {
            var smuggler = new Smuggler();
            Assert.IsNotNull(smuggler);
        }
    }
}
```

This test I ran and it proved that the smuggler does instantiate appropriately, albeit not doing a single useful thing yet.  Next test…

```
[Test, Category("Builder Tests")]
public void TestsSmugglerOrderCompletionResult()
{
    var smuggler = new Smuggler();
    smuggler.CompleteOrder();
    SmuggledClassForTest smuggled = smuggler.GetSmuggledSwag();
    Assert.AreEqual(smuggled.StuffTestValue, Resources.ValueForTestingSmugglerSmuggled);
}
```

Now this test, if you view the picture, didn’t color code so well.  ReSharper points out that the instantiated class smuggler doesn’t have a CompleteOrder or GetSmuggledSwag method.

image 2[![](/images/adronhall.smugmug.com/photos/352400018_9ktuM-M.png)](http://adronhall.smugmug.com/gallery/5711024_NKtkk/1/352400018_9ktuM)

Move the curser (and new character marker over the red method) and hit Alt+Enter (IntelliJ Keymapping) and select the Create method ‘Smuggler.CompleteOrder’.

[![](/images/adronhall.smugmug.com/photos/352399968_NAGur-M.png)](http://adronhall.smugmug.com/gallery/5711024_NKtkk/1/352399968_NAGur)

Now we have no more red, and the class Smuggler now has the method CompleteOrder.  The same code that is displayed in the image is directly below it so it can be copied and pasted easily.  Also note, I went ahead and added the IBuilder interface to the class since it will need to meet the contractual obligations of the builder interface.

[![](/images/adronhall.smugmug.com/photos/352399974_7DNNS-M.png)](http://adronhall.smugmug.com/gallery/5711024_NKtkk/1/352399974_7DNNS)

```
namespace Production.Smugglers.Builders
{
    public class Smuggler : IBuilder
    {
        public void CompleteOrder()
        {
            throw new NotImplementedException();
        }
    }
}
```

I then wrote the following additional test, below is the additional test and the ones I already completed in total.

```
[TestFixture]
public class SmugglerTests
{
    [Test, Category("Builder Tests")]
    public void TestsSmugglerIsNotNull()
    {
        var smuggler = new Smuggler();
        Assert.IsNotNull(smuggler);
    }

    [Test, Category("Builder Tests")]
    public void TestsSmugglerSmuggledIsNotNull()
    {
        Smuggler smuggler = new Smuggler();
        smuggler.CompleteOrder();
        SmuggledClassForTest smuggled = smuggler.GetSmuggledSwag();
        Assert.IsNotNull(smuggled);
    }

    [Test, Category("Builder Tests")]
    public void TestsSmugglerOrderCompletionResult()
    {
        Smuggler smuggler = new Smuggler();
        smuggler.CompleteOrder();
        SmuggledClassForTest smuggled = smuggler.GetSmuggledSwag();
        Assert.AreEqual(smuggled.StuffTestValue, Properties.Resources.ValueForTestingSmugglerSmuggled);
    }
}
```

After that I went ahead and fleshed out the following classes to get the smuggler tests to green light.  First I stuck a resource variable in for my “test variable value”.  One could do this another million ways but I figured this quick n’ easy.

[![](/images/adronhall.smugmug.com/photos/352399982_yMtSd-M.png)](http://adronhall.smugmug.com/gallery/5711024_NKtkk/1/352399982_yMtSd)

This resource file is located in the Properties of the project.

|  |  |
| --- | --- |
|  | Find the resources by clicking the tab… |

Then finished the interface (for now of course).

```
namespace Production.Smugglers.Builders
{
    public interface IBuilder
    {
        void CompleteOrder();
        SmuggledClassForTest GetSmuggledSwag();
    }
}
```

Then finished the Smuggler Class (i.e. Builder).

```
namespace Production.Smugglers.Builders
{
    public class Smuggler : IBuilder
    {
        private readonly SmuggledClassForTest smuggledClassForTest = new SmuggledClassForTest();

        public void CompleteOrder()
        {
            smuggledClassForTest.StuffTestValue = Resources.ValueForTestingSmugglerSmuggled;
        }

        public SmuggledClassForTest GetSmuggledSwag()
        {
            return smuggledClassForTest;
        }
    }
}
```

Then the little SmuggledClassForTests class, which is basically the product of the builder.

```
namespace Production.Smugglers.Smuggled
{
    public class SmuggledClassForTest
    {
        public string StuffTestValue { get; set; }
    }
}
```

Note the namespaces, I make a point to follow the standard of maintaining folder and namespace integrity.  I promise keeping the integrity makes getting to and finding code way faster than getting those things out of sync.

I then ran the tests again…

[![](/images/adronhall.smugmug.com/photos/352399998_TZpff-M.png)](http://adronhall.smugmug.com/gallery/5711024_NKtkk/1/352399998_TZpff)

…green lights!

[![kick it on DotNetKicks.com](http://www.dotnetkicks.com/Services/Images/KickItImageGenerator.ashx?url=http%3a%2f%2fadronbhall.com%2fblogs%2ftechnology__software_development%2farchive%2f2008%2f08%2f15%2f7547.aspx&bgcolor=3333FF&cfgcolor=CC3300)](http://www.dotnetkicks.com/kick/?url=http%3a%2f%2fadronbhall.com%2fblogs%2ftechnology__software_development%2farchive%2f2008%2f08%2f15%2f7547.aspx)

Technorati Tags: [Builder](http://technorati.com/tags/Builder),[Pattern](http://technorati.com/tags/Pattern),[Design](http://technorati.com/tags/Design),[Architecture](http://technorati.com/tags/Architecture),[Resharper](http://technorati.com/tags/Resharper),[Visual Studio](http://technorati.com/tags/Visual%20Studio),[.NET](http://technorati.com/tags/.NET),[dotnet](http://technorati.com/tags/dotnet),[unit Tests](http://technorati.com/tags/unit%20Tests),[testing](http://technorati.com/tags/testing),[TDD](http://technorati.com/tags/TDD)

del.icio.us Tags: [Builder](http://del.icio.us/popular/Builder),[Pattern](http://del.icio.us/popular/Pattern),[Design](http://del.icio.us/popular/Design),[Architecture](http://del.icio.us/popular/Architecture),[Resharper](http://del.icio.us/popular/Resharper),[Visual Studio](http://del.icio.us/popular/Visual%20Studio),[.NET](http://del.icio.us/popular/.NET),[dotnet](http://del.icio.us/popular/dotnet),[unit Tests](http://del.icio.us/popular/unit%20Tests),[testing](http://del.icio.us/popular/testing),[TDD](http://del.icio.us/popular/TDD)
