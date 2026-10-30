---
title: 'TDD, Architecture and Testing Code in Isolation :: Part 2'
date: 2008-07-07 16:13:00 +0000
last_modified_at: 2008-07-07 16:13:00 +0000
permalink: /2008/07/07/tdd-architecture-and-testing-code-in-isolation-part-2/
slug: tdd-architecture-and-testing-code-in-isolation-part-2
wp_id: 271
original_url: https://compositecode.blog/2008/07/07/tdd-architecture-and-testing-code-in-isolation-part-2/
categories:
- Uncategorized Bits
tags: []
excerpt: Navigate back to Part 1 of this series of entries. The next steps I undertook are some of my various clean ups. Create respective test classes for each of the pieces of the database that will have respective entities, methods, or objects to test. I like to keep code clean, easy to read, and were …
---

[Navigate back to Part 1 of this series of entries](http://www.adronbhall.com/blogs/technology__software_development/post/2008/07/06/TDD-Architecture-and-Testing-Code-in-Isolation-Part-1.aspx).

The next steps I undertook are some of my various clean ups.  Create respective test classes for each of the pieces of the database that will have respective entities, methods, or objects to test.

[![](/images/adronhall.smugmug.com/photos/326404784_oTAM2-M.png)](http://adronhall.smugmug.com/gallery/5339404_Kav3S/2/326404784_oTAM2)

I like to keep code clean, easy to read, and were it needs to be.  I hate code bloat, misplaced code sections, and above all I can’t stand arbitrary pieces of using statements, random misuses of methods (such as ToString()) and other such things.  Luckily for me [JetBrains](http://www.jetbrains.com/) Software created [ReSharper](http://www.jetbrains.com/resharper/index.html).  So before going to far headlong into the tests I always run a few “Cleanup Code…” functions on my newly created files.

[![](/images/adronhall.smugmug.com/photos/326404789_boYQp-M.png)](http://adronhall.smugmug.com/gallery/5339404_Kav3S/2/326404789_boYQp)

I usually just leave the cleanup code settings on full and click run.

[![](/images/adronhall.smugmug.com/photos/326404773_hxTqU-M.png)](http://adronhall.smugmug.com/gallery/5339404_Kav3S/1/326404773_hxTqU)

The code already, with just the crude skeleton goes from this…

```
   1:  using System;
   2:  using System.Collections.Generic;
   3:  using System.Linq;
   4:  using System.Text;
   5:  using MbUnit.Framework;
   6:
   7:  namespace DataAccessLayer.Unit.mbUnitTests
   8:  {
   9:      [TestFixture]
  10:      public class Users
  11:      {
  12:          [Test]
  13:          public void Test()
  14:          {
  15:              //
  16:              // TODO: Add test logic here
  17:              //
  18:          }
  19:      }
  20:  }
```

…to this…

```
using MbUnit.Framework;
```

```
   1:  namespace DataAccessLayer.Unit.mbUnitTests
   2:  {
   3:      [TestFixture]
   4:      public class Users
   5:      {
   6:          [Test]
   7:          public void Test()
   8:          {
   9:              //
  10:              // TODO: Add test logic here
  11:              //
  12:          }
  13:      }
  14:  }
```

.csharpcode, .csharpcode pre
{
font-size: small;
color: black;
font-family: consolas, “Courier New”, courier, monospace;
background-color: #ffffff;
/\*white-space: pre;\*/
}
.csharpcode pre { margin: 0em; }
.csharpcode .rem { color: #008000; }
.csharpcode .kwrd { color: #0000ff; }
.csharpcode .str { color: #006080; }
.csharpcode .op { color: #0000c0; }
.csharpcode .preproc { color: #cc6633; }
.csharpcode .asp { background-color: #ffff00; }
.csharpcode .html { color: #800000; }
.csharpcode .attr { color: #ff0000; }
.csharpcode .alt
{
background-color: #f4f4f4;
width: 100%;
margin: 0em;
}
.csharpcode .lnum { color: #606060; }

Reason number eight gazillion that [ReSharper](http://www.jetbrains.com/resharper/index.html) RULEZ!  I almost forgot too, I need to have my [Rhino Mock Library](http://www.ayende.com/projects/rhino-mocks/downloads.aspx) References.  If you don’t have the [Rhino Mock Library](http://www.ayende.com/projects/rhino-mocks/downloads.aspx) you can [download it](http://www.ayende.com/projects/rhino-mocks/downloads.aspx).  Generally I just put a folder in the solution, stick the DLL in it, and then browse to make a reference.

[![](/images/adronhall.smugmug.com/photos/326404777_fWn5r-M.png)](http://adronhall.smugmug.com/gallery/5339404_Kav3S/1/326404777_fWn5r)

[![](/images/adronhall.smugmug.com/photos/326404778_JoRGq-M.png)](http://adronhall.smugmug.com/gallery/5339404_Kav3S/2/326404778_JoRGq)

Now that we have clean test fixtures I’m going to run some green lights.  Green light tests that is, which is not in true TDD fashion.  The reason though is because this layer will be tests against a generated layer (the LINQ to SQL).  The generated layer doesn’t really require a red light green light process, so I’m just going to write the bare minimum of green light tests against the layer.  Then when we go to the next layer, which WILL need to be red light green light I’ll already have this layer tested appropriately.

Before going any further and I forget another reference I’m grabbing the DAL Layer assembly.

[![](/images/adronhall.smugmug.com/photos/327105757_Y4dQs-M.png)](http://adronhall.smugmug.com/gallery/5339404_Kav3S/2/327105757_Y4dQs)

[![](/images/adronhall.smugmug.com/photos/327105768_oDjNq-M.png)](http://adronhall.smugmug.com/gallery/5339404_Kav3S/2/327105768_oDjNq)

Now that I’ve managed to not forget the references, which I’ve been working on doing, and I have the appropriate items in place.  The next step NOW is to get those green lights.  Off to the reckless abandon of TDD.  The first tests I write are simple, no frills, just to get and test the TsrUser and TmtUser Entities.

```
   1:  using System;
   2:  using MbUnit.Framework;
   3:  using Rhino.Mocks;
   4:
   5:  namespace DataAccessLayer.Unit.mbUnitTests
   6:  {
   7:      [TestFixture]
   8:      public class Users
   9:      {
  10:          [Test]
  11:          public void TestTsrUserEntity()
  12:          {
  13:              Guid newUserId = Guid.NewGuid();
  14:              TsrUser tsrUser = MockRepository.GenerateStub<TsrUser>();
  15:              tsrUser.UserId = newUserId;
  16:              Assert.AreEqual(tsrUser.UserId, newUserId);
  17:          }
  18:
  19:          [Test]
  20:          public void TestTmtUserEntity()
  21:          {
  22:              Guid newUserId = Guid.NewGuid();
  23:              TmtUser tmtUser = MockRepository.GenerateStub<TmtUser>();
  24:              tmtUser.UserId = newUserId;
  25:              Assert.AreEqual(tmtUser.UserId, newUserId);
  26:          }
  27:      }
  28:  }
```

.csharpcode, .csharpcode pre
{
font-size: small;
color: black;
font-family: consolas, “Courier New”, courier, monospace;
background-color: #ffffff;
/\*white-space: pre;\*/
}
.csharpcode pre { margin: 0em; }
.csharpcode .rem { color: #008000; }
.csharpcode .kwrd { color: #0000ff; }
.csharpcode .str { color: #006080; }
.csharpcode .op { color: #0000c0; }
.csharpcode .preproc { color: #cc6633; }
.csharpcode .asp { background-color: #ffff00; }
.csharpcode .html { color: #800000; }
.csharpcode .attr { color: #ff0000; }
.csharpcode .alt
{
background-color: #f4f4f4;
width: 100%;
margin: 0em;
}
.csharpcode .lnum { color: #606060; }

Next, hit up the User Lists derived from the views.  This is where the mocking gets truly interesting.  The above tests, while they help, really don’t do much of anything.  Next what I need is a way to mock out the DataContext Class, which doesn’t have an interface.  This is a slight issue, but just requires a little manual coding to get a good mock going.  Since I knew I’d be using this for multiple testing projects I’ve created a completely new project to reference.  Since I’m not always creative I’m naming it “UnitTest” and then will name the files respectively.

[![](/images/adronhall.smugmug.com/photos/327105730_FZ4vx-M.png)](http://adronhall.smugmug.com/gallery/5339404_Kav3S/2/327105730_FZ4vx)

I also found a bit of code specifically for mocking the DataContext over at Andrew Tokeley’s Blog on [Mocking LINQ to SQL DataContext](http://andrewtokeley.net/archive/2008/07/06/mocking-linq-to-sql-datacontext.aspx).  I’ve snagged it and have altered it for the particular project.  Make sure to give dibs to Andrew!  Below are the modified interfaces and the respective classes.  Make sure to add a reference to the DAL for the project too.  Then add the files listed below in the screen shot.

[![](/images/adronhall.smugmug.com/photos/327105757_Y4dQs-M.png)](http://adronhall.smugmug.com/gallery/5339404_Kav3S/2/327105757_Y4dQs)

![](/images/adronhall.smugmug.com/photos/327105743_E7Pxu-M.png)

**IDataContextWrapper Interface**

```
   1:  using System;
   2:  using System.Collections.Generic;
   3:
   4:  namespace UnitTest.Interfaces
   5:  {
   6:      public interface IDataContextWrapper : IDisposable
   7:      {
   8:          List<T> Table<T>() where T : class;
   9:          void DeleteAllOnSubmit<T>(IEnumerable<T> entities) where T : class;
  10:          void DeleteOnSubmit<T>(T entity) where T : class;
  11:          void InsertOnSubmit<T>(T entity) where T : class;
  12:          void SubmitChanges();
  13:      }
  14:  }
```

.csharpcode, .csharpcode pre
{
font-size: small;
color: black;
font-family: consolas, “Courier New”, courier, monospace;
background-color: #ffffff;
/\*white-space: pre;\*/
}
.csharpcode pre { margin: 0em; }
.csharpcode .rem { color: #008000; }
.csharpcode .kwrd { color: #0000ff; }
.csharpcode .str { color: #006080; }
.csharpcode .op { color: #0000c0; }
.csharpcode .preproc { color: #cc6633; }
.csharpcode .asp { background-color: #ffff00; }
.csharpcode .html { color: #800000; }
.csharpcode .attr { color: #ff0000; }
.csharpcode .alt
{
background-color: #f4f4f4;
width: 100%;
margin: 0em;
}
.csharpcode .lnum { color: #606060; }

**IMockDatabase Interface**

```
   1:  using System;
   2:  using System.Collections;
   3:  using System.Collections.Generic;
   4:
   5:  namespace UnitTest.Interfaces
   6:  {
   7:      public interface IMockDatabase
   8:      {
   9:          Dictionary<Type, IList> Tables { get; set; }
  10:      }
  11:  }
```

.csharpcode, .csharpcode pre
{
font-size: small;
color: black;
font-family: consolas, “Courier New”, courier, monospace;
background-color: #ffffff;
/\*white-space: pre;\*/
}
.csharpcode pre { margin: 0em; }
.csharpcode .rem { color: #008000; }
.csharpcode .kwrd { color: #0000ff; }
.csharpcode .str { color: #006080; }
.csharpcode .op { color: #0000c0; }
.csharpcode .preproc { color: #cc6633; }
.csharpcode .asp { background-color: #ffff00; }
.csharpcode .html { color: #800000; }
.csharpcode .attr { color: #ff0000; }
.csharpcode .alt
{
background-color: #f4f4f4;
width: 100%;
margin: 0em;
}
.csharpcode .lnum { color: #606060; }

**MockDatabase Class**

```
   1:  using System;
   2:  using System.Collections;
   3:  using System.Collections.Generic;
   4:
   5:  namespace UnitTest.Mocks
   6:  {
   7:      /// <summary>
   8:      /// Abstract Template class that represents our in memory database. We can create different implementations of this class that contain different
   9:      /// tables and data.
  10:      /// </summary>
  11:      public abstract class MockDatabase
  12:      {
  13:          protected MockDatabase()
  14:          {
  15:              InitializeDataBase();
  16:          }
  17:
  18:          public Dictionary<Type, IList> Tables { get; set; }
  19:
  20:          private void InitializeDataBase()
  21:          {
  22:              Tables = new Dictionary<Type, IList>();
  23:              CreateTables();
  24:              PopulateTables();
  25:          }
  26:
  27:          protected abstract void CreateTables();
  28:          protected abstract void PopulateTables();
  29:
  30:          protected void AddTable<T>()
  31:          {
  32:              var table = new List<T>();
  33:              Tables.Add(typeof (T), table);
  34:          }
  35:
  36:          protected List<T> GetTable<T>()
  37:          {
  38:              return (List<T>) Tables[typeof (T)];
  39:          }
  40:      }
  41:  }
```

.csharpcode, .csharpcode pre
{
font-size: small;
color: black;
font-family: consolas, “Courier New”, courier, monospace;
background-color: #ffffff;
/\*white-space: pre;\*/
}
.csharpcode pre { margin: 0em; }
.csharpcode .rem { color: #008000; }
.csharpcode .kwrd { color: #0000ff; }
.csharpcode .str { color: #006080; }
.csharpcode .op { color: #0000c0; }
.csharpcode .preproc { color: #cc6633; }
.csharpcode .asp { background-color: #ffff00; }
.csharpcode .html { color: #800000; }
.csharpcode .attr { color: #ff0000; }
.csharpcode .alt
{
background-color: #f4f4f4;
width: 100%;
margin: 0em;
}
.csharpcode .lnum { color: #606060; }

**MockDatabaseContextWrapper Wrapper Class**

```
   1:  using System.Collections.Generic;
   2:  using UnitTest.Interfaces;
   3:
   4:  namespace UnitTest.Mocks
   5:  {
   6:      /// <summary>
   7:      /// A linq to sql wrapper class. This is a mock implementation of IDataContextWrapper
   8:      /// that works directly with an in memory version of a database
   9:      /// </summary>
  10:      public class MockDataContextWrapper : IDataContextWrapper
  11:      {
  12:          private readonly MockDatabase _mockDatabase;
  13:
  14:          public MockDataContextWrapper(MockDatabase database)
  15:          {
  16:              _mockDatabase = database;
  17:          }
  18:
  19:          #region IDataContextWrapper Members
  20:
  21:          public List<T> Table<T>() where T : class
  22:          {
  23:              return (List<T>) _mockDatabase.Tables[typeof (T)];
  24:          }
  25:
  26:          public void DeleteAllOnSubmit<T>(IEnumerable<T> entities) where T : class
  27:          {
  28:              foreach (T entity in entities)
  29:              {
  30:                  Table<T>().Remove(entity);
  31:              }
  32:          }
  33:
  34:          public void DeleteOnSubmit<T>(T entity) where T : class
  35:          {
  36:              Table<T>().Remove(entity);
  37:          }
  38:
  39:          public void InsertOnSubmit<T>(T entity) where T : class
  40:          {
  41:              Table<T>().Add(entity);
  42:          }
  43:
  44:          public void SubmitChanges()
  45:          {
  46:          }
  47:
  48:          public void Dispose()
  49:          {
  50:          }
  51:
  52:          #endregion
  53:      }
  54:  }
```

.csharpcode, .csharpcode pre
{
font-size: small;
color: black;
font-family: consolas, “Courier New”, courier, monospace;
background-color: #ffffff;
/\*white-space: pre;\*/
}
.csharpcode pre { margin: 0em; }
.csharpcode .rem { color: #008000; }
.csharpcode .kwrd { color: #0000ff; }
.csharpcode .str { color: #006080; }
.csharpcode .op { color: #0000c0; }
.csharpcode .preproc { color: #cc6633; }
.csharpcode .asp { background-color: #ffff00; }
.csharpcode .html { color: #800000; }
.csharpcode .attr { color: #ff0000; }
.csharpcode .alt
{
background-color: #f4f4f4;
width: 100%;
margin: 0em;
}
.csharpcode .lnum { color: #606060; }

**DataContextWrapper Wrapper Class**

```
   1:  using System;
   2:  using System.Collections.Generic;
   3:  using System.Data.Linq;
   4:  using System.Linq;
   5:  using UnitTest.Interfaces;
   6:
   7:  namespace UnitTest
   8:  {
   9:      /// <summary>
  10:      /// A linq to sql wrapper class for the Datacontext object. This is the real implementation of IDataContextWrapper
  11:      /// that works directly with a database
  12:      /// </summary>
  13:      /// <typeparam name="T"></typeparam>
  14:      public class DataContextWrapper<T> : IDataContextWrapper where T : DataContext, new()
  15:      {
  16:          private readonly T db;
  17:          private bool _disposed;
  18:
  19:          public DataContextWrapper()
  20:          {
  21:              Type t = typeof (T);
  22:              db = (T) Activator.CreateInstance(t);
  23:          }
  24:
  25:          public DataContextWrapper(string connectionString)
  26:          {
  27:              Type t = typeof (T);
  28:              db = (T) Activator.CreateInstance(t, connectionString);
  29:          }
  30:
  31:          #region IDataContextWrapper Members
  32:
  33:          public List<TableName> Table<TableName>() where TableName : class
  34:          {
  35:              var table = (Table<TableName>) db.GetTable(typeof (TableName));
  36:
  37:              return table.ToList();
  38:          }
  39:
  40:          public void DeleteAllOnSubmit<Entity>(IEnumerable<Entity> entities) where Entity : class
  41:          {
  42:              db.GetTable(typeof (Entity)).DeleteAllOnSubmit(entities);
  43:          }
  44:
  45:          public void DeleteOnSubmit<Entity>(Entity entity) where Entity : class
  46:          {
  47:              db.GetTable(typeof (Entity)).DeleteOnSubmit(entity);
  48:          }
  49:
  50:          public void InsertOnSubmit<Entity>(Entity entity) where Entity : class
  51:          {
  52:              db.GetTable(typeof (Entity)).InsertOnSubmit(entity);
  53:          }
  54:
  55:          public void SubmitChanges()
  56:          {
  57:              db.SubmitChanges();
  58:          }
  59:
  60:          public void Dispose()
  61:          {
  62:              Dispose(true);
  63:              GC.SuppressFinalize(this);
  64:          }
  65:
  66:          #endregion
  67:
  68:          private void Dispose(bool disposing)
  69:          {
  70:              if (_disposed)
  71:                  return;
  72:
  73:              if (disposing)
  74:              {
  75:                  db.Dispose();
  76:              }
  77:
  78:              _disposed = true;
  79:          }
  80:      }
  81:  }
```

.csharpcode, .csharpcode pre
{
font-size: small;
color: black;
font-family: consolas, “Courier New”, courier, monospace;
background-color: #ffffff;
/\*white-space: pre;\*/
}
.csharpcode pre { margin: 0em; }
.csharpcode .rem { color: #008000; }
.csharpcode .kwrd { color: #0000ff; }
.csharpcode .str { color: #006080; }
.csharpcode .op { color: #0000c0; }
.csharpcode .preproc { color: #cc6633; }
.csharpcode .asp { background-color: #ffff00; }
.csharpcode .html { color: #800000; }
.csharpcode .attr { color: #ff0000; }
.csharpcode .alt
{
background-color: #f4f4f4;
width: 100%;
margin: 0em;
}
.csharpcode .lnum { color: #606060; }

**ExampleMockDatabase Class**

```
   1:  using System;
   2:  using DataAccessLayer;
   3:
   4:  namespace UnitTest.Mocks
   5:  {
   6:      /// <summary>
   7:      /// This is an actual implementation of our database containing specific tables and data.
   8:      /// </summary>
   9:      public class ExampleMockDatabase : MockDatabase
  10:      {
  11:          protected override void CreateTables()
  12:          {
  13:              AddTable<TsrUserListing>();
  14:          }
  15:
  16:          protected override void PopulateTables()
  17:          {
  18:              var testTsrUserListing1 =
  19:                  new TsrUserListing
  20:                      {
  21:                          UserId = Guid.NewGuid(),
  22:                          UserName = "Test User",
  23:                          LoweredUserName = "test user",
  24:                          IsAnonymous = false,
  25:                          LastActivityDate = DateTime.Now.AddDays(-4),
  26:                          MobileAlias = "test user"
  27:                      };
  28:              var testTsrUserListing2 =
  29:                  new TsrUserListing
  30:                      {
  31:                          UserId = Guid.NewGuid(),
  32:                          UserName = "User Test",
  33:                          LoweredUserName = "user test",
  34:                          IsAnonymous = true,
  35:                          LastActivityDate = DateTime.Now.AddMinutes(-23),
  36:                          MobileAlias = "user test"
  37:                      };
  38:              var testTsrUserListing3 =
  39:                  new TsrUserListing
  40:                      {
  41:                          UserId = Guid.NewGuid(),
  42:                          UserName = "John Doe",
  43:                          LoweredUserName = "john doe",
  44:                          IsAnonymous = true,
  45:                          LastActivityDate = DateTime.Now.AddHours(-22),
  46:                          MobileAlias = "john doe"
  47:                      };
  48:
  49:              GetTable<TsrUserListing>().Add(testTsrUserListing1);
  50:              GetTable<TsrUserListing>().Add(testTsrUserListing2);
  51:              GetTable<TsrUserListing>().Add(testTsrUserListing3);
  52:          }
  53:      }
  54:  }
```

.csharpcode, .csharpcode pre
{
font-size: small;
color: black;
font-family: consolas, “Courier New”, courier, monospace;
background-color: #ffffff;
/\*white-space: pre;\*/
}
.csharpcode pre { margin: 0em; }
.csharpcode .rem { color: #008000; }
.csharpcode .kwrd { color: #0000ff; }
.csharpcode .str { color: #006080; }
.csharpcode .op { color: #0000c0; }
.csharpcode .preproc { color: #cc6633; }
.csharpcode .asp { background-color: #ffff00; }
.csharpcode .html { color: #800000; }
.csharpcode .attr { color: #ff0000; }
.csharpcode .alt
{
background-color: #f4f4f4;
width: 100%;
margin: 0em;
}
.csharpcode .lnum { color: #606060; }

**CustomerController Class**

```
   1:  using System;
   2:  using System.Collections.Generic;
   3:  using System.Linq;
   4:  using DataAccessLayer;
   5:  using UnitTest.Interfaces;
   6:
   7:  namespace UnitTest.Controller
   8:  {
   9:      public class TsrUserListingController
  10:      {
  11:          public IDataContextWrapper DataContext { get; set; }
  12:
  13:          public IEnumerable<TsrUserListing> GetTsrUserListing(DateTime lastActivityDate)
  14:          {
  15:              IEnumerable<TsrUserListing> tsrUserListings = from tsrUserListing in DataContext.Table<TsrUserListing>()
  16:                                                            where tsrUserListing.LastActivityDate >= lastActivityDate
  17:                                                            select tsrUserListing;
  18:              return tsrUserListings;
  19:          }
  20:
  21:          public IEnumerable<TsrUserListing> GetTsrUserListing()
  22:          {
  23:              IEnumerable<TsrUserListing> tsrUserListings = from tsrUserListing in DataContext.Table<TsrUserListing>()
  24:                                                            select tsrUserListing;
  25:              return tsrUserListings;
  26:          }
  27:      }
  28:  }
```

.csharpcode, .csharpcode pre
{
font-size: small;
color: black;
font-family: consolas, “Courier New”, courier, monospace;
background-color: #ffffff;
/\*white-space: pre;\*/
}
.csharpcode pre { margin: 0em; }
.csharpcode .rem { color: #008000; }
.csharpcode .kwrd { color: #0000ff; }
.csharpcode .str { color: #006080; }
.csharpcode .op { color: #0000c0; }
.csharpcode .preproc { color: #cc6633; }
.csharpcode .asp { background-color: #ffff00; }
.csharpcode .html { color: #800000; }
.csharpcode .attr { color: #ff0000; }
.csharpcode .alt
{
background-color: #f4f4f4;
width: 100%;
margin: 0em;
}
.csharpcode .lnum { color: #606060; }

Now that we have the database fake/mock – whatever one wants to call it – we’re ready for some tests.  So stay tuned, I’ll have it up tomorrow.

[![kick it on DotNetKicks.com](http://www.dotnetkicks.com/Services/Images/KickItImageGenerator.ashx?url=http%3a%2f%2fadronbhall.com%2fblogs%2ftechnology__software_development%2farchive%2f2008%2f07%2f07%2f7390.aspx&bgcolor=3333FF&cfgcolor=CC3300)](http://www.dotnetkicks.com/kick/?url=http%3a%2f%2fadronbhall.com%2fblogs%2ftechnology__software_development%2farchive%2f2008%2f07%2f07%2f7390.aspx)

Technorati Tags: [TDD](http://technorati.com/tags/TDD),[Test](http://technorati.com/tags/Test),[Unit Tests](http://technorati.com/tags/Unit%20Tests),[LINQ](http://technorati.com/tags/LINQ),[SQL](http://technorati.com/tags/SQL),[DAL](http://technorati.com/tags/DAL),[DataAccessLayer](http://technorati.com/tags/DataAccessLayer),[Architecture](http://technorati.com/tags/Architecture),[Software](http://technorati.com/tags/Software),[mbUnit](http://technorati.com/tags/mbUnit),[Rhino](http://technorati.com/tags/Rhino),[Mock](http://technorati.com/tags/Mock),[Stub](http://technorati.com/tags/Stub),[ReSharper](http://technorati.com/tags/ReSharper),[Isolation](http://technorati.com/tags/Isolation)

del.icio.us Tags: [TDD](http://del.icio.us/popular/TDD),[Test](http://del.icio.us/popular/Test),[Unit Tests](http://del.icio.us/popular/Unit%20Tests),[LINQ](http://del.icio.us/popular/LINQ),[SQL](http://del.icio.us/popular/SQL),[DAL](http://del.icio.us/popular/DAL),[DataAccessLayer](http://del.icio.us/popular/DataAccessLayer),[Architecture](http://del.icio.us/popular/Architecture),[Software](http://del.icio.us/popular/Software),[mbUnit](http://del.icio.us/popular/mbUnit),[Rhino](http://del.icio.us/popular/Rhino),[Mock](http://del.icio.us/popular/Mock),[Stub](http://del.icio.us/popular/Stub),[ReSharper](http://del.icio.us/popular/ReSharper),[Isolation](http://del.icio.us/popular/Isolation)
