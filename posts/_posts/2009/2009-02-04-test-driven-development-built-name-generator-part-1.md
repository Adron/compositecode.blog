---
title: Test Driven Development Built Name Generator Part 1
date: 2009-02-04 02:20:52 -0800
last_modified_at: 2013-09-05 19:09:20 -0700
permalink: /2009/02/04/test-driven-development-built-name-generator-part-1/
slug: test-driven-development-built-name-generator-part-1
wp_id: 582
original_url: https://compositecode.blog/2009/02/04/test-driven-development-built-name-generator-part-1/
categories:
- .NET Bits
- How-to
- Testing
tags:
- .NET
- bdd
- behavior driven development
- c#
- csharp
- tdd
- test driven development
excerpt: Part 2, Part 3. This is going to be a multi-part series on building a straight forward database driven name generator. I’ve tried the random name generator thing and it generally isn’t so great. I’d tried in the past this idea with the database table of census names and it works great. So this is part …
---

[Part 2](/2009/02/05/test-driven-development-built-name-generator-part-2/), [Part 3](/2009/02/13/test-driven-development-built-name-generator-part-3/).

This is going to be a multi-part series on building a straight forward database driven name generator.  I’ve tried the random name generator thing and it generally isn’t so great.  I’d tried in the past this idea with the database table of census names and it works great.  So this is part 1.  I’ll post these entries consecutively over the next few days so stay tuned.

First I started a new clean solution and added a test project.  I figured I wasn’t even going to add the actual assembly project yet, just jump right in and start writing a test, get red, and go to the next step.

I added a test file and wrote the following test.

```csharp
[TestMethod]
public void VerifyFullNameObjectInstantiatesWithNames()
{
    FullName fullName = new FullName();
    Assert.IsTrue(fullName.FirstName.Length == 0);
    Assert.IsTrue(fullName.LastName.Length == 0);
}
```

After that I used ReSharper Alt+Enter Shortcut plus a little additional keying in myself to flesh out the skeletal class and get a green light.  I ended up with the class below.

```csharp
public class FullName
{
    public string FirstName { get; set; }
    public string LastName { get; set; }
}
```

Next I wanted to enforce a contract so I could create a factory to build my FullName objects with.  With that change the interface and class I had now looked like this.

```csharp
public interface IFullName
{
    string FirstName { get; set; }
    string LastName { get; set; }
}

public class FullName : IFullName
{
    public FullName()
    {
        FirstName = string.Empty;
        LastName = string.Empty;
    }

    public string FirstName { get; set; }
    public string LastName { get; set; }
}
```

That gave me a green light on my first test.  After that I built a test for the factory that could build the names.

```csharp
[TestMethod]
public void VerifyFullNameObjectReturnsFromFactory()
{
    IFullName name = NameFactory.Build();
    Assert.IsTrue(name.FirstName.Length > 0);
    Assert.IsTrue(name.LastName.Length > 0);
}
```

I then took the NameFactory object and fleshed it out so I could build, run the test, and get green lighted.  Below is the NameFactory Class.

```csharp
public class NameFactory
{
    public static IFullName Build()
    {
        return new FullName { FirstName = "TestFirst", LastName = "TestLast" };
    }
}
```

So now I have a green light on the name factory.  But even though I have a green light, it doesn’t exactly do what it needs to do, which is get some good unique and random names.  Next step, write a test for getting back some random names.

```csharp
[TestMethod]
public void VerifyFullNameIsRandom()
{
    IFullName nameOne = NameFactory.Build();
    IFullName nameTwo = NameFactory.Build();

    Assert.AreNotEqual(nameOne.FirstName, nameTwo.FirstName);
    Assert.AreNotEqual(nameOne.LastName, nameTwo.LastName);
}
```

After creating this test, I have to dive a little deeper.  First I grabbed the [census names](http://www.census.gov/genealogy/names/names_files.html) for first and last names off of the Internet.  After that I added two projects to my overall Visual Studio Solution.  One is a database project and one is Windows App to use to manipulate the text file data and get it into our database.

[![](/images/adronhall.smugmug.com/photos/464365893_HJUQx-S.png)](http://adronhall.smugmug.com/gallery/7227152_BavAD#464365893_HJUQx)

Next I created the *Generator* Database a table to store the names that are stored in the files.

The SQL create script is shown below.

```sql
 IF NOT EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'[dbo].[Names]') AND type in (N'U'))
 BEGIN
 CREATE TABLE [dbo].[Names](
     [NameId] [uniqueidentifier] NOT NULL,
     [Name] [nvarchar](50) NOT NULL,
     [Type] [smallint] NOT NULL,
  CONSTRAINT [PK_Names] PRIMARY KEY CLUSTERED
 (
     [NameId] ASC
 )WITH (PAD_INDEX  = OFF, STATISTICS_NORECOMPUTE  = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS  = ON, ALLOW_PAGE_LOCKS  = ON) ON [PRIMARY]
 ) ON [PRIMARY]
 END
```

I also added an extended property to outline how I intended to use the “Type” column.

```sql
IF NOT EXISTS (SELECT * FROM ::fn_listextendedproperty(N'MS_Description' , N'SCHEMA',N'dbo', N'TABLE',N'Names', N'COLUMN',N'Type'))
EXEC sys.sp_addextendedproperty @name=N'MS_Description', @value=N'1 = Male, 2 = Female, 3 = Last Name' , @level0type=N'SCHEMA',@level0name=N'dbo', @level1type=N'TABLE',@level1name=N'Names', @level2type=N'COLUMN',@level2name=N'Type'
```

My intention is for the “Type” column to have a 1 for the male first name, a 2 for a female first name, and a 3 for the last name.

I’ve covered creating the initial tests and objects to use.  Also the database table that is needed and the create scripts have been provided.  Next steps are to build a quick app to get the names imported into the database table.  Stay tuned and that will be posted tomorrow.
