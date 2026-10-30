---
title: Data Generation, TDD Like
date: 2009-02-15 20:50:41 +0000
last_modified_at: 2014-12-30 12:13:55 -0800
permalink: /2009/02/15/data-generation-tdd-like/
slug: data-generation-tdd-like
wp_id: 589
original_url: https://compositecode.blog/2009/02/15/data-generation-tdd-like/
categories:
- Uncategorized Bits
tags: []
excerpt: On the tail of my recent additions to the data generator app I?ve been building I fell right into a need for the middle name to be generated along with standard names. Here?s how I went about fixing this situation up with a sling at TDD & such. The first thing I did was a …
---

On the tail of my recent additions to the data generator app I?ve been building I fell right into a need for the middle name to be generated along with standard names.  Here?s how I went about fixing this situation up with a sling at TDD & such.

The first thing I did was a quick refactor, to change the previous *FullName* class I had been using in my previous Part 1, Part 2, and Part 3 examples to *FirstLastAmericanName*.  Next I added the first test for the new class I?ll create right afterward.  The test looked like this.

```
   1:  [TestMethod]
   2:  public void VerifyFirstMiddleLastName()
   3:  {
   4:      var name = new FirstMiddleLastAmericanName();
   5:      Assert.IsTrue(name.FirstName.Length == 0);
   6:      Assert.IsTrue(name.LastName.Length == 0);
   7:      Assert.IsTrue(name.MiddleName.Length == 0);
   8:  }
```

The test, of course doesn?t build, let alone run.  So I jumped into this new class and created the following.

```
   1:  namespace Generator.Core.Model
   2:  {
   3:      public class FirstMiddleLastAmericanName : IFullName
   4:      {
   5:          public FirstMiddleLastAmericanName()
   6:          {
   7:              FirstName = string.Empty;
   8:              LastName = string.Empty;
   9:              MiddleName = string.Empty;
  10:          }
  11:
  12:          public string MiddleName;
  13:
  14:          #region IFullName Members
  15:
  16:          public string FirstName { get; set; }
  17:
  18:          public string LastName { get; set; }
  19:
  20:          #endregion
  21:      }
  22:  }
```

So now I get a green light and I head right into the next test.

```
   1:  [TestMethod]
   2:  public void VerifyFirstMiddleLastNameObjectReturnsFromFactory()
   3:  {
   4:      var factory = new NameFactory();
   5:      var name = factory.Build(NameFactory.NameCulture.AmericanFirstMiddleLast) as FirstMiddleLastAmericanName;
   6:      Assert.IsTrue(name.FirstName.Length > 0);
   7:      Assert.IsTrue(name.LastName.Length > 0);
   8:      Assert.IsTrue(name.MiddleName.Length > 0);
   9:  }
```

I needed to then add the NameCulture enumeration.  This I added directly inside of the NameFactory.  I reviewed the other classes and name spaces I had setup.  At this time it seemed like the best place to put the enumeration.

```
   1:  namespace Generator.Core.Factories
   2:  {
   3:      public class NameFactory
   4:      {
   5:          public enum NameCulture
   6:          {
   7:              American,
   8:              AmericanFirstMiddleLast,
   9:              British,
  10:              French,
  11:              Japanese
  12:          }
```

Make note that is a very partial code segment. Also make note, I?m not adding anything except functionality right now for that second value AmericanFirstMiddleLast. I left off the rest of the class as it will be changing a lot and I?ll copy in each part as I change it. In this entry I?ll be refactoring so that the enumeration is a legitimately used part of the code base and how it reverberates through. The next thing was to get at least a basic method to get a green light for the test listed. What I ended up with to get to that point is as follows.

```
   1:  public IFullName Build(NameCulture nameCulture)
   2:  {
   3:      var name =
   4:          new FirstMiddleLastAmericanName
   5:              {
   6:                  FirstName = "test",
   7:                  MiddleName = "test",
   8:                  LastName = "test"
   9:              };
  10:
  11:      return name;
  12:  }
```

Now it?s time to get some real randomness in the names.  I first wrote out a test.

```
   1:  [TestMethod]
   2:  public void VerifyFirstMiddleLastNameIsRandom()
   3:  {
   4:      var factory = new NameFactory();
   5:      var nameOne = factory.Build(NameFactory.NameCulture.AmericanFirstMiddleLast) as FirstMiddleLastAmericanName;
   6:      var nameTwo = factory.Build(NameFactory.NameCulture.AmericanFirstMiddleLast) as FirstMiddleLastAmericanName;
   7:
   8:      Assert.AreNotEqual(nameOne.FirstName, nameTwo.FirstName);
   9:      Assert.AreNotEqual(nameOne.MiddleName, nameTwo.MiddleName);
  10:      Assert.AreNotEqual(nameOne.LastName, nameTwo.LastName);
  11:  }
```

This got me to a stage where I actually have a good test that will make sure I?m getting solid random names back.  After this test, with the red light received, I set out and applied these changes the Build method I created above.

```
   1:  public IFullName Build(NameCulture nameCulture)
   2:  {
   3:      var rand = new Random(DateTime.Now.Millisecond);
   4:      var entities = new GeneratorEntities();
   5:
   6:      List<Names> firstNames = (from name in entities.Names
   7:                                where name.Type == "Female First Names" || name.Type == "Male First Names"
   8:                                select name).ToList();
   9:      List<Names> lastNames = (from name in entities.Names
  10:                               where name.Type == "Last Names"
  11:                               select name).ToList();
  12:      List<Names> middleNames = new List<Names>();
  13:
  14:      middleNames.AddRange(firstNames);
  15:      middleNames.AddRange(lastNames);
  16:
  17:      var firstMiddleLastAmericanName =
  18:          new FirstMiddleLastAmericanName
  19:              {
  20:                  FirstName = firstNames[rand.Next(0, firstNames.Count)].Name,
  21:                  MiddleName = middleNames[rand.Next(0, middleNames.Count)].Name,
  22:                  LastName = lastNames[rand.Next(0, lastNames.Count)].Name
  23:              };
  24:
  25:      return firstMiddleLastAmericanName;
  26:  }
```

That should give me a full range of middle names.  Next step, that?s right, write a test.  After this test I noticed something though?

```
   1:  [TestMethod]
   2:  public void VerifyMultitudesFirstMiddleLastNameIsRandom()
   3:  {
   4:      var factory = new NameFactory();
   5:      var list =
   6:          factory.Build(NameFactory.NameCulture.AmericanFirstMiddleLast, 1000) as
   7:          List<FirstMiddleLastAmericanName>;
   8:
   9:      for (int i = 0; i < list.Count; i++)
  10:      {
  11:          int compareUp = i + 1;
  12:          if (compareUp == list.Count)
  13:          {
  14:              compareUp = 0;
  15:          }
  16:          Assert.AreNotEqual(
  17:              list[compareUp].FirstName + list[compareUp].MiddleName + list[compareUp].LastName,
  18:              list[i].FirstName + list[compareUp].MiddleName + list[i].LastName);
  19:      }
  20:  }
```

Yeah, I needed to do some serious refactoring.  With this test, not even building, I jumped into resolving the Build methods.  During each of these stages of the refactor I made a point to run all of my tests, except the one above.  This way I assured I didn?t break anything else.  My final NameFactory code looked like what is below.  Take a good look at the following code, and below I?ll have listed a few of the major refactor changes I made.

```
   1:  using System;
   2:  using System.Collections.Generic;
   3:  using System.Linq;
   4:  using Generator.Core.Model;
   5:
   6:  namespace Generator.Core.Factories
   7:  {
   8:      public class NameFactory
   9:      {
  10:          public NameFactory()
  11:          {
  12:              entities = new GeneratorEntities();
  13:              random = new Random(DateTime.Now.Millisecond);
  14:              firstNames = new List<Names>();
  15:              lastNames = new List<Names>();
  16:              middleNames = new List<Names>();
  17:              namesList = (from name in entities.Names select name).ToList();
  18:          }
  19:
  20:          private readonly GeneratorEntities entities;
  21:          private readonly Random random;
  22:          private List<Names> firstNames;
  23:          private List<Names> lastNames;
  24:          private readonly List<Names> middleNames;
  25:          private readonly List<Names> namesList;
  26:
  27:          public enum NameCulture
  28:          {
  29:              American,
  30:              AmericanFirstMiddleLast,
  31:              British,
  32:              French,
  33:              Japanese
  34:          }
  35:
  36:          public IFullName Build(NameCulture nameCulture)
  37:          {
  38:              return CreateNames(nameCulture, 1)[0];
  39:          }
  40:
  41:          public IFullName Build()
  42:          {
  43:              return CreateNames(NameCulture.American, 1)[0];
  44:          }
  45:
  46:          public List<IFullName> Build(NameCulture nameCulture, int numberOfNames)
  47:          {
  48:              return CreateNames(nameCulture, numberOfNames);
  49:          }
  50:
  51:          private List<IFullName> CreateNames(NameCulture nameCulture, int numberOfNames)
  52:          {
  53:              firstNames = GetFirstNames();
  54:              lastNames = GetLastNames();
  55:
  56:              switch (nameCulture)
  57:              {
  58:                  case NameCulture.American:
  59:                      var firstLastAmericanName = new List<IFullName>();
  60:
  61:                      for (int i = 0; i < numberOfNames; i++)
  62:                      {
  63:                          firstLastAmericanName.Add(MapName(new FirstLastAmericanName()));
  64:                      }
  65:
  66:                      return firstLastAmericanName;
  67:
  68:                  case NameCulture.AmericanFirstMiddleLast:
  69:                      middleNames.AddRange(firstNames);
  70:                      middleNames.AddRange(lastNames);
  71:
  72:                      var americanFirstMiddleLastNames = new List<IFullName>();
  73:
  74:                      for (int i = 0; i < numberOfNames; i++)
  75:                      {
  76:                          var fullName = new FirstMiddleLastAmericanName();
  77:                          fullName = MapName(fullName) as FirstMiddleLastAmericanName;
  78:                          fullName.MiddleName = middleNames[random.Next(0, middleNames.Count)].Name;
  79:                          americanFirstMiddleLastNames.Add(fullName);
  80:                      }
  81:
  82:                      return americanFirstMiddleLastNames;
  83:
  84:                  default:
  85:                      throw new ArgumentOutOfRangeException("nameCulture");
  86:              }
  87:          }
  88:
  89:          private IFullName MapName(IFullName name)
  90:          {
  91:              name.FirstName = firstNames[random.Next(0, firstNames.Count)].Name;
  92:              name.LastName = lastNames[random.Next(0, lastNames.Count)].Name;
  93:              return name;
  94:          }
  95:
  96:          private List<Names> GetFirstNames()
  97:          {
  98:              return (from name in namesList
  99:                      where name.Type == "Female First Names" || name.Type == "Male First Names"
 100:                      select name).ToList();
 101:          }
 102:
 103:          private List<Names> GetLastNames()
 104:          {
 105:              return (from name in namesList
 106:                      where name.Type == "Last Names"
 107:                      select name).ToList();
 108:          }
 109:      }
 110:  }
```

The first thing I did was create the GetFirstNames & GetLastNames methods to clean up some of the junk that was in the Build methods.  Immediately I realized that I could make it even more performing by removing the actual queries against the database by simple returning the whole table into memory ? take a look at the last line of the constructor for that.  I completed that clean up, with appropriate lists being created.  Another thing I added was the mapper method.  I?m not 100% sure I like that method, but it sort of cleaned up things a little, but in turn it just doesn?t seem as elegant as it should be.

Overall I got it down to a single hit against the database & more in memory movements of the lists.  Also setup several private properties.  After a minute I thought, ?I?ll toss those setup some readonly members and save a bit of memory??  So I tried that and it worked out well.  I went through a number of other refactor steps and ended up with what I have listed above.  Next task was to see if my test would work.  So I uncommented my test and tried to run it.  It blew up with exceptions, so I dug in.

I immediately realized I had to do a little last minute refactor of my test also.  My final test ended up list this, which it appears to be, a bit more readable.  I might follow up though, with an entry cleaning this up even more.

```
   1:  [TestMethod]
   2:  public void VerifyMultitudesFirstMiddleLastNameIsRandom()
   3:  {
   4:      var factory = new NameFactory();
   5:      List<IFullName> list = factory.Build(NameFactory.NameCulture.AmericanFirstMiddleLast, 100);
   6:
   7:      for (int i = 0; i < list.Count; i++)
   8:      {
   9:          int compareUp = i + 1;
  10:          if (compareUp == list.Count)
  11:          {
  12:              compareUp = 0;
  13:          }
  14:
  15:          var fullName = list[compareUp] as FirstMiddleLastAmericanName;
  16:          var fullNameBase = list[i] as FirstMiddleLastAmericanName;
  17:
  18:          Assert.AreNotEqual(fullName.FirstName + fullName.MiddleName + fullName.LastName,
  19:              fullNameBase.FirstName + fullNameBase.MiddleName + fullNameBase.LastName);
  20:      }
  21:  }
```

Hope that was useful and happy Presidents day at ya.  Fini.
