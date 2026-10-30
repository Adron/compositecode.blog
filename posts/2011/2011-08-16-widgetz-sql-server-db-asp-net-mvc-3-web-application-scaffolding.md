---
title: Widgetz SQL Server DB + ASP.NET MVC 3 Web Application Scaffolding
date: 2011-08-16 05:30:27 -0700
last_modified_at: 2011-08-15 18:12:01 -0700
permalink: /2011/08/16/widgetz-sql-server-db-asp-net-mvc-3-web-application-scaffolding/
slug: widgetz-sql-server-db-asp-net-mvc-3-web-application-scaffolding
wp_id: 3554
original_url: https://compositecode.blog/2011/08/16/widgetz-sql-server-db-asp-net-mvc-3-web-application-scaffolding/
categories:
- .NET Bits
- How-to
tags:
- asp.net mvc
- controller
- model
- mvc
- scaffolding
- sql
- sql server
- sql server 2008
- view
- visual studio 2010
excerpt: 'This is a quick walk through of how to setup a database, create some model objects, and build a scaffold for CRUD (Create, Read, Update, and Delete) all using ASP.NET MVC 3 and Visual Studio 2010. Open Visual Studio 2010 and start a database project as shown. SQL Server 2008 Database Project in Visual Studio 2010 (Click for full size image) Next create an ASP.NET MVC 3 Web Application in this solution. ASP.NET MVC 3 Web Application (Click for full size image) Now open the Server Explorer in Visual Studio 2010 (You might have to click on View to find it if it isn’t already available in the main IDE). Right click on the Data Connections node in the Service Explorer Tree. Select Create Database and provide a name for the database. Create a New SQL 2008 Database New Database Dialog Next in the Server Explorer, right click on the newly created database and select New Query. Then in the query window paste this SQL create script in and run it by right clicking and selecting execute. CREATE TABLE [dbo].[Widgetz] ( [Id] UNIQUEIDENTIFIER NOT NULL, [Name] NVARCHAR (50) NOT NULL, [Description] NTEXT NULL, [Created] DATETIME NOT NULL, [Terminated] DATETIME NULL, [Addon] BIT NOT NULL, [Active] BIT NOT NULL, [Cost] MONEY NULL, [ChildWidgetz] INT NULL ); ALTER TABLE [dbo].[Widgetz] ADD CONSTRAINT [PK_Widgetz] PRIMARY KEY CLUSTERED ([Name] ASC) WITH (ALLOW_PAGE_LOCKS = ON, ALLOW_ROW_LOCKS = ON, PAD_INDEX = OFF, IGNORE_DUP_KEY = OFF, STATISTICS_NORECOMPUTE = OFF); ALTER TABLE [dbo].[Widgetz] ADD CONSTRAINT [DF_Widgetz_Created] DEFAULT (getdate()) FOR [Created]; ALTER TABLE [dbo].[Widgetz] ADD CONSTRAINT [DF_Widgetz_Active] DEFAULT ((1)) FOR [Active]; ALTER TABLE [dbo].[Widgetz] ADD CONSTRAINT [DF_Widgetz_Addon] DEFAULT ((0)) FOR [Addon]; Once the table is created bring to focus the Solution Explorer and right click on the Database Project, selecting the Import Database Objects and Settings. Import Database Objects and Settings… Next select the correct database connection, and leave everything else as it is set. Selecting the appropriate database, options, and click next… (Click for the full size image) Next the wizard will finish importing the database objects. Finished (Click for full size image) If you look through the folder tree of the project you’ll find individual files for the table, defaults, and other object settings. Now right click on the Models directory of the ASP.NET MVC 3 Project that was created earlier. Select add and then new item. In that dialog add a new ADO.NET Entity Data Model. Yup, just when you think it had gone away… ADO.NET (Click for full size image) A dialog will appear, select the option to Generate from database and click next. Entity Data Model Wizard (Click for full size image) Next select the correct database connection again, then click on Yes to save the sensitive data (which if you’re using windows authentication it isn’t really going to save anything dangerous). Make sure the entities are named appropriately and click Next. Options for Creating the ADO.NET Entity Model The next screen, which may take a moment or two to display the list of tables and objects, will appear. Select the table that has been created and click on Entity Data Model Wizard (Click for full size image) Once done and finish is clicked, the entity model file will show the display view of the entity that was just created. Entity Model Now right click on the controller folder and select to create a new controller. Add Controller (Click for full size image) Be sure to click the advanced options and select the layout page. Advanced Options (Click for full size image) Now click on Ok and then Add. Visual Studio 2010 will not generate the scaffolding for the controller and views around CRUD operations. The Scaffolding in ASP.NET MVC 3 This might seem like an absurdly easy thing to do, and you’d be right. There are however many steps to turn this into a feasible, well design user interface, and provide a solid and intelligent user experience (UX) to the end user. Also, this is arguably a not so maintainable bit of work. If the end user ONLY wants to operate on the data with CRUD, then this is great. But the minute something else is needed a very different, testable, and maintainable architecture should be utilized instead of this generated scaffolding. Which in coming blog entries I will be covering some of the ways to create testable, maintainable, and better designed architecture around more than CRUD. 🙂 CODE: All the code for this project is available in the Lesson 1 – ScaffoldGeneratedWidgetz.'
---

This is a quick walk through of how to setup a database, create some model objects, and build a scaffold for CRUD (Create, Read, Update, and Delete) all using ASP.NET MVC 3 and Visual Studio 2010.

Open Visual Studio 2010 and start a database project as shown.

[![SQL Server 2008 Database Project in Visual Studio 2010 (Click for full size image)](/images/adronhall.smugmug.com/Software/Software-Development/Scaffold-Generated-Widgetz/i-X8m9NDW/0/S/windgetz-database-01-S.png "SQL Server 2008 Database Project in Visual Studio 2010 (Click for full size image)")](http://adronhall.smugmug.com/Software/Software-Development/Scaffold-Generated-Widgetz/18539616_wbnrBx#1431299225_X8m9NDW-O-LB)

*SQL Server 2008 Database Project in Visual Studio 2010 (Click for full size image)*

Next create an ASP.NET MVC 3 Web Application in this solution.

[![ASP.NET MVC 3 Web Application (Click for full size image)](/images/adronhall.smugmug.com/Software/Software-Development/Scaffold-Generated-Widgetz/i-q8RGQQN/0/S/windgetz-database-02-S.png "ASP.NET MVC 3 Web Application (Click for full size image)")](http://adronhall.smugmug.com/Software/Software-Development/Scaffold-Generated-Widgetz/18539616_wbnrBx#1431299220_q8RGQQN-O-LB)

*ASP.NET MVC 3 Web Application (Click for full size image)*

Now open the Server Explorer in Visual Studio 2010 (You might have to click on View to find it if it isn’t already available in the main IDE). Right click on the Data Connections node in the Service Explorer Tree. Select Create Database and provide a name for the database.

![Create a New SQL 2008 Database](/images/adronhall.smugmug.com/Software/Software-Development/Scaffold-Generated-Widgetz/i-8F8vCQ9/0/O/windgetz-database-03.png "Create a New SQL 2008 Database")

*Create a New SQL 2008 Database*

![New Database Dialog](/images/adronhall.smugmug.com/Software/Software-Development/Scaffold-Generated-Widgetz/i-L5c967p/0/O/windgetz-database-04.png "New Database Dialog")

*New Database Dialog*

Next in the Server Explorer, right click on the newly created database and select New Query. Then in the query window paste this SQL create script in and run it by right clicking and selecting execute.

```sql
CREATE TABLE [dbo].[Widgetz] (
    [Id]           UNIQUEIDENTIFIER NOT NULL,
    [Name]         NVARCHAR (50)    NOT NULL,
    [Description]  NTEXT            NULL,
    [Created]      DATETIME         NOT NULL,
    [Terminated]   DATETIME         NULL,
    [Addon]        BIT              NOT NULL,
    [Active]       BIT              NOT NULL,
    [Cost]         MONEY            NULL,
    [ChildWidgetz] INT              NULL
);

ALTER TABLE [dbo].[Widgetz]
    ADD CONSTRAINT [PK_Widgetz] PRIMARY KEY CLUSTERED ([Name] ASC) WITH (ALLOW_PAGE_LOCKS = ON, ALLOW_ROW_LOCKS = ON, PAD_INDEX = OFF, IGNORE_DUP_KEY = OFF, STATISTICS_NORECOMPUTE = OFF);

ALTER TABLE [dbo].[Widgetz]
    ADD CONSTRAINT [DF_Widgetz_Created] DEFAULT (getdate()) FOR [Created];

ALTER TABLE [dbo].[Widgetz]
    ADD CONSTRAINT [DF_Widgetz_Active] DEFAULT ((1)) FOR [Active];

ALTER TABLE [dbo].[Widgetz]
    ADD CONSTRAINT [DF_Widgetz_Addon] DEFAULT ((0)) FOR [Addon];
```

Once the table is created bring to focus the Solution Explorer and right click on the Database Project, selecting the Import Database Objects and Settings.

![Import Database Objects and Settings...](/images/adronhall.smugmug.com/Software/Software-Development/Scaffold-Generated-Widgetz/i-QkNGPRf/0/O/windgetz-database-05.png "Import Database Objects and Settings...")

*Import Database Objects and Settings...*

Next select the correct database connection, and leave everything else as it is set.

[![Selecting the appropriate database, options, and click next... (Click for the full size image)](/images/adronhall.smugmug.com/Software/Software-Development/Scaffold-Generated-Widgetz/i-9H9RznV/0/S/windgetz-database-06-S.png "Selecting the appropriate database, options, and click next... (Click for the full size image)")](http://adronhall.smugmug.com/Software/Software-Development/Scaffold-Generated-Widgetz/18539616_wbnrBx#1431303228_9H9RznV-O-LB)

*Selecting the appropriate database, options, and click next... (Click for the full size image)*

Next the wizard will finish importing the database objects.

[![Finished (Click for full size image)](/images/adronhall.smugmug.com/Software/Software-Development/Scaffold-Generated-Widgetz/i-PGCkQ9H/0/S/windgetz-database-07-S.png "Finished (Click for full size image)")](http://adronhall.smugmug.com/Software/Software-Development/Scaffold-Generated-Widgetz/18539616_wbnrBx#1431305092_PGCkQ9H-O-LB)

*Finished (Click for full size image)*

If you look through the folder tree of the project you’ll find individual files for the table, defaults, and other object settings.

Now right click on the Models directory of the ASP.NET MVC 3 Project that was created earlier. Select add and then new item. In that dialog add a new ADO.NET Entity Data Model.

[![Yup, just when you think it had gone away...  ADO.NET (Click for full size image)](/images/adronhall.smugmug.com/Software/Software-Development/Scaffold-Generated-Widgetz/i-3JcNhZX/0/S/windgetz-database-08-S.png "Yup, just when you think it had gone away...  ADO.NET (Click for full size image)")](http://adronhall.smugmug.com/Software/Software-Development/Scaffold-Generated-Widgetz/18539616_wbnrBx#1431305082_3JcNhZX-O-LB)

*Yup, just when you think it had gone away... ADO.NET (Click for full size image)*

A dialog will appear, select the option to Generate from database and click next.

[![Entity Data Model Wizard (Click for full size image)](/images/adronhall.smugmug.com/Software/Software-Development/Scaffold-Generated-Widgetz/i-7zkLcCT/0/S/windgetz-database-09-S.png "Entity Data Model Wizard (Click for full size image)")](http://adronhall.smugmug.com/Software/Software-Development/Scaffold-Generated-Widgetz/18539616_wbnrBx#1431307145_7zkLcCT-O-LB)

*Entity Data Model Wizard (Click for full size image)*

Next select the correct database connection again, then click on Yes to save the sensitive data (which if you’re using *windows authentication* it isn’t *really* going to save anything dangerous). Make sure the entities are named appropriately and click Next.

[![Options for Creating the ADO.NET Entity Model](/images/adronhall.smugmug.com/Software/Software-Development/Scaffold-Generated-Widgetz/i-S37c8pC/0/S/windgetz-database-10-S.png "Options for Creating the ADO.NET Entity Model")](http://adronhall.smugmug.com/Software/Software-Development/Scaffold-Generated-Widgetz/18539616_wbnrBx#1431307149_S37c8pC-O-LB)

*Options for Creating the ADO.NET Entity Model*

The next screen, which may take a moment or two to display the list of tables and objects, will appear. Select the table that has been created and click on

[![Entity Data Model Wizard (Click for full size image)](/images/adronhall.smugmug.com/Software/Software-Development/Scaffold-Generated-Widgetz/i-hqGsxwg/0/S/windgetz-database-11-S.png "Entity Data Model Wizard (Click for full size image)")](http://adronhall.smugmug.com/Software/Software-Development/Scaffold-Generated-Widgetz/18539616_wbnrBx#1431307175_hqGsxwg-O-LB)

*Entity Data Model Wizard (Click for full size image)*

Once done and finish is clicked, the entity model file will show the display view of the entity that was just created.

![Entity Model](/images/adronhall.smugmug.com/Software/Software-Development/Scaffold-Generated-Widgetz/i-q4DVFHG/0/O/windgetz-database-12.png "Entity Model")

*Entity Model*

Now right click on the controller folder and select to create a new controller.

[![Add Controller (Click for full size image)](/images/adronhall.smugmug.com/Software/Software-Development/Scaffold-Generated-Widgetz/i-N4HxXQK/0/S/windgetz-database-13-S.png "Add Controller (Click for full size image)")](http://adronhall.smugmug.com/Software/Software-Development/Scaffold-Generated-Widgetz/18539616_wbnrBx#1431307636_N4HxXQK-O-LB)

*Add Controller (Click for full size image)*

Be sure to click the advanced options and select the layout page.

[![Advanced Options (Click for full size image)](/images/adronhall.smugmug.com/Software/Software-Development/Scaffold-Generated-Widgetz/i-hWrKCjj/0/S/windgetz-database-14-S.png "Advanced Options (Click for full size image)")](http://adronhall.smugmug.com/Software/Software-Development/Scaffold-Generated-Widgetz/18539616_wbnrBx#1431307643_hWrKCjj-O-LB)

*Advanced Options (Click for full size image)*

Now click on Ok and then Add. Visual Studio 2010 will not generate the scaffolding for the controller and views around CRUD operations.

![The Scaffolding in ASP.NET MVC 3](/images/adronhall.smugmug.com/Software/Software-Development/Scaffold-Generated-Widgetz/i-3JRSgnC/0/O/windgetz-database-15.png "The Scaffolding in ASP.NET MVC 3")

*The Scaffolding in ASP.NET MVC 3*

This might seem like an absurdly easy thing to do, and you’d be right. There are however many steps to turn this into a feasible, well design user interface, and provide a solid and intelligent user experience (UX) to the end user. Also, this is arguably a not so maintainable bit of work. If the end user ONLY wants to operate on the data with CRUD, then this is great. But the minute something else is needed a very different, testable, and maintainable architecture should be utilized instead of this generated scaffolding. Which in coming blog entries I will be covering some of the ways to create testable, maintainable, and better designed architecture around *more than CRUD*.  🙂

**CODE:** All the code for this project is available in the [Lesson 1 – ScaffoldGeneratedWidgetz](https://github.com/Adron/aspnetmvckickstarter).
