---
title: How I'm Using BlogEngine.NET Part 1
date: 2008-09-19 06:22:00 -0700
last_modified_at: 2008-09-19 06:22:00 -0700
permalink: /2008/09/19/how-im-using-blogengine-net-part-1/
slug: how-im-using-blogengine-net-part-1
wp_id: 227
original_url: https://compositecode.blog/2008/09/19/how-im-using-blogengine-net-part-1/
categories:
- Uncategorized Bits
tags: []
excerpt: BlogEngine.NET does not currently do multiple blogs per installation of the web application. I know this is supposed to change in the future, but I needed a solution now. The easiest fix really, and the previous Community Server Engine installation lent itself well to this, was to just create a web application for each blog …
---

BlogEngine.NET does not currently do multiple blogs per installation of the web application.  I know this is supposed to change in the future, but I needed a solution now.  The easiest fix really, and the previous Community Server Engine installation lent itself well to this, was to just create a web application for each blog I was going to have.

What I did was create a basic web application, which I planned to host at the root level of my domain, <http://www.adronbhall.com>.  I create that web application in my overall .NET Solution and then created two copied instances of the BlogEngine.NET Application in the same solution.  These would be copied into the existing directories, or paths of the current root application like; <http://adronbhall.com/blogs/technology__software_development/> and <http://adronbhall.com/blogs/my_transportation_obsession/>.

I then created a separate database for each.  This of course, IMHO, isn’t all that great since I’ll have redundant users and all that.  I’m just going to have to figure that problem out later.  For now, I just want to get the engines setup so I can have total control over my sites and code base.

I reconnected each respective BlogEngine.NET installation to their own database.  I got good connectivity, downloaded the appropriate skins that I wanted for each, and got to work on setting them up.

Then things got really fun when I began building out the ETL for each of the sites.  The Community Server database was of course in a single source, but the other two were going to need to be in separate locations.  Not really complicated, but not something one whips up in 5 minutes either.

The first thing I tried was creating a true to the ideal ETL project with SSIS, which turned out to be a complete waste of time and a PIA.  After that I just wrote some straight SQL that would take data from the originating database and insert the data via mappings directly into the database I wanted it to end up in.  The following are the first steps of this makeshift ETL effort.

First I setup each database, configured each of the blogengine.net databases so they were ready for import.  Then I added a database project to my overall solution.

**The Database Project “EtlCode”**

[![](/images/adronhall.smugmug.com/photos/375770880_NGhcV-M.png)](http://adronhall.smugmug.com/gallery/6009716_mwqwG/1/375770880_NGhcV)

**The Databases**

[![](/images/adronhall.smugmug.com/photos/375770890_WtNTx-M.png)](http://adronhall.smugmug.com/gallery/6009716_mwqwG/1/375770890_WtNTx)

I then started created the various extraction SQL that is needed for the views in the AdronsCommunity Database.  There were several views, with some code duplication (SQL isn’t exactly an OOP language), but specifically geared toward each database the data would eventually end up in.

Each of the views created had the following code, notice that I’ve used a lot of “as SomeColumn” so that the names would align easily and reduce prospective confusion.  If I want to extract the other entries not related to these two blogs later I wanted to make it easy on myself.

**Query for Categories**

```
SELECT  dbo.cs_Post_Categories.Name,
    dbo.cs_Post_Categories.Description,
    dbo.cs_Post_Categories.CategoryID AS CS_CategoryID,
    dbo.cs_Post_Categories.IdForBlogEngine AS CategoryId
FROM dbo.cs_Post_Categories INNER JOIN
    dbo.cs_Post_Categories_Parents ON
        dbo.cs_Post_Categories.CategoryID = dbo.cs_Post_Categories_Parents.CategoryID
WHERE (dbo.cs_Post_Categories.SectionID = 13)
```

**Query for Posts**

```
SELECT     TOP (100) PERCENT
    IdForBlogEngine AS PostID,
    Subject AS Title,
    Body AS Description,
    FormattedBody AS PostContent,
    PostDate AS DateCreated,
    NULL AS DateModified,
    'Adron' AS Author,
    IsApproved AS IsPublished,
    NULL AS IsCommentEnabled,
    NULL AS Raters,
    NULL AS Rating,
    NULL AS Slug,
    PostID AS CS_PostID
FROM dbo.cs_Posts
WHERE (PostAuthor = N'adron') AND
    (UserID = 2102) AND
    (SectionID = 13) AND
    (IsApproved = 1) AND
    (PostType = 0)
ORDER BY DateCreated DESC
```

**Query for Categories & Posts Many to Many Table**

```
SELECT TOP (100) PERCENT
    dbo.cs_Posts.Subject,
    dbo.cs_Post_Categories.Name,
    dbo.cs_Posts_InCategories.PostID,
    dbo.cs_Posts_InCategories.CategoryID,
    dbo.cs_Posts.IdForBlogEngine AS PostIDForBlogEngine,
    dbo.cs_Post_Categories.IdForBlogEngine AS CategoryIdForBlogEngine
FROM dbo.cs_Post_Categories
            INNER JOIN
    dbo.cs_Posts_InCategories ON
        dbo.cs_Post_Categories.CategoryID = dbo.cs_Posts_InCategories.CategoryID
            RIGHT OUTER JOIN
    dbo.cs_Posts ON
        dbo.cs_Posts_InCategories.PostID = dbo.cs_Posts.PostID
WHERE (dbo.cs_Post_Categories.Name IS NOT NULL) AND
    (dbo.cs_Post_Categories.SectionID = 13)
ORDER BY dbo.cs_Posts.PostDate DESC
```

**Query for Comments**

```
SELECT TOP (100) PERCENT
    dbo.cs_Posts.IdForBlogEngine AS PostCommentID,
    dbo.l_looselyPosts.PostID,
    dbo.cs_Posts.PostDate AS CommentDate,
    dbo.cs_Posts.PostAuthor AS Author,
    '' AS Email,
    '' AS Website,
    dbo.cs_Posts.FormattedBody AS Comment,
    dbo.cs_Posts.IPAddress AS IP,
    dbo.cs_Posts.IsApproved
FROM dbo.cs_Posts INNER JOIN
    dbo.l_looselyPosts ON
        dbo.cs_Posts.ParentID = dbo.l_looselyPosts.CS_PostID
WHERE (dbo.cs_Posts.PostType = 1)
ORDER BY CommentDate DESC
```

Notice in the queries above, I turned each one into a veiw.  Some of the above views have dependencies on each other to derive the new primary keys and other criteria for the process.  Also one thing I stumbled upon is that I had to make the Email and Website columns on the Query for Comments empty nvarchar types instead of null, because in code they break when they’re null but work fine when they just have empty strings.  This might be a bug, at some point, I’ll mention but doubt it is causing any harm at this point.

Once each of these were created I could then create my actual queries for the process.

**Get the Categories**

```
DELETE FROM [looselycoupled].[dbo].[be_PostCategory]
GO
INSERT INTO [looselycoupled].[dbo].[be_PostCategory]
           ([PostID]
           ,[CategoryID])
SELECT l_looselyPostsCategories.PostIDForBlogEngine,
    l_looselyPostsCategories.CategoryIdForBlogEngine
FROM l_looselyPostsCategories
            INNER JOIN
    l_looselyCategories ON
        l_looselyPostsCategories.CategoryID = l_looselyCategories.CS_CategoryID
            INNER JOIN
    l_looselyPosts ON
        l_looselyPostsCategories.PostID = l_looselyPosts.CS_PostID
```

**Get the Posts**

```
DELETE FROM [looselycoupled].[dbo].[be_Posts]
GO
INSERT INTO [looselycoupled].[dbo].[be_Posts]
           ([PostID]
           ,[Title]
           ,[Description]
           ,[PostContent]
           ,[DateCreated]
           ,[DateModified]
           ,[Author]
           ,[IsPublished]
           ,[IsCommentEnabled]
           ,[Raters]
           ,[Rating]
           ,[Slug])
SELECT [PostID]
      ,[Title]
      ,[Description]
      ,[PostContent]
      ,[DateCreated]
      ,[DateModified]
      ,[Author]
      ,[IsPublished]
      ,[IsCommentEnabled]
      ,[Raters]
      ,[Rating]
      ,[Slug]
FROM [AdronsCommunity].[dbo].[l_looselyPosts]
```

**Get the Many to Many Posts to Categories**

```
DELETE FROM [looselycoupled].[dbo].[be_Categories]
GO
INSERT INTO [looselycoupled].[dbo].[be_Categories]
           ([CategoryName]
            ,[Description]
            ,[CategoryID])
SELECT DISTINCT
    CAST(Name AS nvarchar(50)) AS Name,
    CAST(Description AS nvarchar(200)) AS Description,
    CategoryId
FROM         AdronsCommunity.dbo.l_looselyCategories
```

**Get the Comments**

```
DELETE FROM [looselycoupled].[dbo].[be_PostComment]
GO
INSERT INTO [looselycoupled].[dbo].[be_PostComment]
           ([PostCommentID]
           ,[PostID]
           ,[CommentDate]
           ,[Author]
           ,[Email]
           ,[Website]
           ,[Comment]
           ,[Ip]
           ,[IsApproved])
SELECT    [PostCommentID]
      ,[PostID]
      ,[CommentDate]
      ,[Author]
      ,[Email]
      ,[Website]
      ,[Comment]
      ,[IP]
      ,[IsApproved]
FROM    [AdronsCommunity].[dbo].[l_looselyComments]
```

That’s it for the ETL.  In the next part I’ll cover some other tasks I had to complete in order to get moved over onto BlogEngine.NET.

Just for fun I’ve added the Acronym Translation List for any newbies.

- ETL – **E**xtract, **T**ransform, and **L**oad.  Something that is generally used to refer to business intelligence data warehouses or other elaborate data processes.- PIA – **P**ain **I**n the **A**ss.  Self descriptive.- IMHO – **I**n **M**y **H**umble **O**pinion.  Exactly what is written.- SQL – This isn’t really an acronym, according to the original creators, it became an acronym, then un-became an acronym.  However, many people think that it means **S**tandard **Q**uery **L**anguage, when it reality it just means **S**e**q**ua**l**.
