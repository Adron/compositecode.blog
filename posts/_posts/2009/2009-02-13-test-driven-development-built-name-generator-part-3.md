---
title: Test Driven Development Built Name Generator Part 3
date: 2009-02-13 02:47:00 -0800
last_modified_at: 2013-09-05 19:08:11 -0700
permalink: /2009/02/13/test-driven-development-built-name-generator-part-3/
slug: test-driven-development-built-name-generator-part-3
wp_id: 587
original_url: https://compositecode.blog/2009/02/13/test-driven-development-built-name-generator-part-3/
categories:
- .NET Bits
- How-to
tags:
- .NET
- bdd
- c#
- tdd
- test
- test driven development
- testing
excerpt: Part 1, Part 2. Now it is time finally for the random name generation. I’ve gotten everything into place, so it’s just a matter of grabbing the names and randomizing among them. Just as a check, after Part 2 was finished I had a total of 98,572 rows of data, or simply 98,572 names. Many …
---

[Part 1](/2009/02/04/test-driven-development-built-name-generator-part-1/), [Part 2](/2009/02/05/test-driven-development-built-name-generator-part-2/).

Now it is time finally for the random name generation.  I’ve gotten everything into place, so it’s just a matter of grabbing the names and randomizing among them.  Just as a check, after [Part 2](/2009/02/05/test-driven-development-built-name-generator-part-2/) was finished I had a total of 98,572 rows of data, or simply 98,572 names.

Many times I would not write actual unit tests against the database as it breaks isolation.  This time though, I’m making an exception.  First I added a reference to *Generator.Core, System.Data,* and *System.Data.Entity*.  I then created a new unit test class called *DatabaseTests* and added the following test to get things rolling.  Keep in mind, since these tests break isolation, I don’t write them in the *red light green light* idea of TDD.  My assumption is that they only prove the database is setup, running, the connection string is correct, and other minor configuration based and server based components.  In addition, yes, these are somewhat silly tests, such as the RetrieveFirstName() test has a bit of redundancy to it, but the point is to have an automated test to assure that the data has been moved into the database and is returning appropriately.

```csharp
[TestClass]
public class DatabaseTests
{
    [TestMethod]
    public void RetrieveFirstFemaleName()
    {
        var entities = new GeneratorEntities();
        var returnName = (from name in entities.Names
                          where name.Type == "Female First Names"
                           select name).FirstOrDefault();
         Assert.IsNotNull(returnName);
         Assert.IsTrue(returnName.Name != string.Empty);
     }

     [TestMethod]
     public void RetrieveLastName()
     {
         var entities = new GeneratorEntities();
         var returnName = (from name in entities.Names
                           where name.Type == "Last Names"
                           select name).FirstOrDefault();
         Assert.IsNotNull(returnName);
         Assert.IsTrue(returnName.Name != string.Empty);
     }

     [TestMethod]
     public void RetrieveFirstMaleName()
     {
         var entities = new GeneratorEntities();
         var returnName = (from name in entities.Names
                           where name.Type == "Male First Names"
                           select name).FirstOrDefault();
         Assert.IsNotNull(returnName);
         Assert.IsTrue(returnName.Name != string.Empty);
     }

     [TestMethod]
     public void RetrieveFirstName()
     {
         var entities = new GeneratorEntities();
         var returnName = (from name in entities.Names
                           where name.Type == "Female First Names" || name.Type == "Male First Names"
                           select name).FirstOrDefault();
         Assert.IsNotNull(returnName);
         Assert.IsTrue(returnName.Name != string.Empty && returnName.Type == "Female First Names" ||
                       returnName.Type == "Male First Names");
    }
}
```

The next step now was to refactor the existing tests to prove the assembly of the name data transfer objects that would hold the first name and last name derived from the returned entity objects.

The first thing I did was break out the actual name objects into their respective files.  I did this using ReSharper, because it’s super insanely simple with ReSharper.  After that I put the class files in the project that has the model.  Next I fixed the namespaces to *Generator.Core.Model*.  The class files after these changes looked like the code below.

IFullName.c

```csharp
namespace Generator.Core.Model
{
    public interface IFullName
    {
        string FirstName { get; set; }
        string LastName { get; set; }
    }
}
```

FullName.cs

```csharp
namespace Generator.Core.Model
{
    public class FullName : IFullName
    {
        public FullName()
        {
            FirstName = string.Empty;
            LastName = string.Empty;
        }

         #region IFullName Members

         public string FirstName { get; set; }
         public string LastName { get; set; }

         #endregion
     }
}
```

NameFactory.cs

```csharp
namespace Generator.Core.Model
{
    public class NameFactory
    {
        public static IFullName Build()
        {
            return new FullName {FirstName = "TestFirst", LastName = "TestLast"};
        }
    }
}
```

Now that we have these files moved out to the project where all the munging will happen, I’m going to start the actual refactor of the tests.  What I’ve come up with for the test refactor is as follows.

```csharp
using Generator.Core.Model;
using Microsoft.VisualStudio.TestTools.UnitTesting;

namespace Factory.Tests
{
    [TestClass]
    public class FactoryNameBuilder
    {
        [TestMethod]
        public void VerifyFullNameObjectInstantiatesWithNames()
        {
            var name = new FullName();
            Assert.IsTrue(name.FirstName.Length == 0);
            Assert.IsTrue(name.LastName.Length == 0);
        }

        [TestMethod]
        public void VerifyFullNameObjectReturnsFromFactory()
        {
            var factory = new NameFactory();
            IFullName name = factory.Build();
            Assert.IsTrue(name.FirstName.Length > 0);
            Assert.IsTrue(name.LastName.Length > 0);
        }

        [TestMethod]
        public void VerifyFullNameIsRandom()
        {
            var factory = new NameFactory();
            IFullName nameOne = factory.Build();
            IFullName nameTwo = factory.Build();

            Assert.AreNotEqual(nameOne.FirstName, nameTwo.FirstName);
            Assert.AreNotEqual(nameOne.LastName, nameTwo.LastName);
        }
    }
}
```

In the factory I removed the fake return and fleshed out the appropriate build method.

```csharp
using System;
using System.Collections.Generic;
using System.Linq;

namespace Generator.Core.Model
{
    public class NameFactory
    {
        public IFullName Build()
        {
            Random rand = new Random(DateTime.Now.Millisecond);

            GeneratorEntities entities = new GeneratorEntities();

            List FirstNames = (from name in entities.Names
                                      where name.Type == "Female First Names" || name.Type == "Male First Names"
                                      select name).ToList();
            List LastNames = (from name in entities.Names
                                     where name.Type == "Last Names"
                                     select name).ToList();

            FullName fullName = new FullName();
            fullName.FirstName = FirstNames[rand.Next(0, FirstNames.Count)].Name;
            fullName.LastName = LastNames[rand.Next(0, LastNames.Count)].Name;

            return fullName;
        }
    }
}
```

Run the tests now and you have a random name gold mine.  However, I wanted a bit more than that.  With another test added…

```csharp
[TestMethod]
public void VerifyMultipleNameReturn()
{
    var factory = new NameFactory();
    List<IFullName> list = factory.Build(1000);

    for (int i = 0; i < list.Count; i++)
    {
        int compareUp = i + 1;
        if (compareUp == list.Count)
        {
            compareUp = 0;
        }
        Assert.AreNotEqual(list[compareUp].FirstName + list[compareUp].LastName, list[i].FirstName + list[i].LastName);
    }
}
```

…then the extra *Build* method.

```csharp
public List<IFullName> Build(int numberOfNames)
{
    var rand = new Random(DateTime.Now.Millisecond);
    var entities = new GeneratorEntities();

    List<Names> FirstNames = (from name in entities.Names
                              where name.Type == "Female First Names" || name.Type == "Male First Names"
                              select name).ToList();
    List<Names> LastNames = (from name in entities.Names
                             where name.Type == "Last Names"
                             select name).ToList();

    var names = new List<IFullName>();

    for (int i = 0; i < numberOfNames; i++)
    {
        var fullName = new FullName();
        fullName.FirstName = FirstNames[rand.Next(0, FirstNames.Count)].Name;
        fullName.LastName = LastNames[rand.Next(0, LastNames.Count)].Name;
        names.Add(fullName);
    }

    return names;
}
```

and now I have a strong verification that I get solid randoms for 1000 name pairs.  I bumped it up to 2000 too just for fun, and didn’t hit duplicates until I put it up to 200,000.
