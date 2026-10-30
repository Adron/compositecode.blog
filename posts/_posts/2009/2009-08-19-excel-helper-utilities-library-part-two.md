---
title: Excel Helper Utilities Library Part Two
date: 2009-08-19 02:35:00 -0700
last_modified_at: 2010-10-31 11:34:57 -0700
permalink: /2009/08/19/excel-helper-utilities-library-part-two/
slug: excel-helper-utilities-library-part-two
wp_id: 660
original_url: https://compositecode.blog/2009/08/19/excel-helper-utilities-library-part-two/
categories:
- Software Projects
tags:
- excel
- unit test
excerpt: In the last entry I covered a range of utility class methods including appropriate unit tests. Today I want to cover the first steps into the twisted world of Excel Development with C#. Note, there are many things I probably will not mention that are pivotal to this code working. Namely the order in which …
---

In the last entry I covered a range of utility class methods including appropriate [unit tests](http://www.adronbhall.com/blogs/technology__software_development/post/2007/06/20/Software-Development-Testing-Tip-O-The-Day.aspx).  Today I want to cover the first steps into the twisted world of Excel Development with C#.  Note, there are many things I probably will not mention that are pivotal to this code working.  Namely the order in which Excel objects & framework interfaces and components are instantiated are of massive importance within managed code.  So if you are following along, first do the exact example here and then step on to changes.  That way you will have working code before arbitrarily having non-working code.

As always, [tests are first](http://www.adronbhall.com/blogs/technology__software_development/post/2007/06/20/Software-Development-Testing-Tip-O-The-Day.aspx).  In this entry I will actually step from test, to code, then green light the test for each part versus writing all the tests and then working through the methods.  That way I can cover each method and the purpose of the method.[![](/images/adronhall.smugmug.com/photos/624708491_LUTtZ-S.png)](http://adronhall.smugmug.com/gallery/9339220_UAfqA#624708491_LUTtZ)![](/images/adronhall.smugmug.com/photos/624708493_EBQiT-Ti.png)![](/images/adronhall.smugmug.com/photos/624708490_9WCw2-Ti.png)

Before even jumping straight into tests we will need to add two specific assemblies that are needed to test Excel appropriately;  Microsoft.Office.Interop.Excel and Microsoft.Office.Tools.Excel.v9.0.  (Click the images to see larger images)

Now to get started with Excel unit tests, we really do need to use the Excel Assemblies we’ve added because mocking just doesn’t cut it.  Because of the legacy code & other such droves of complexities, it is extremely hard to really mock accurately.  One really needs to know when the actual application is behaving appropriately under load & use from software written to use it.  With that said, here’s my first few tests & setup code.

I start out by creating the test class and creating a public property to act for all tests as the actual Excel Application under test.

```csharp
[TestFixture]
public class ExcelHelperTests
{
    public Application ExcelApplication { get; set; }
```

Next I create two tests for setup and teardown of the Excel Application object.  In addition to the basic Excel Application object, one thing I have learned about Excel from experience, is that one needs to go ahead and immediately add a workbook.  If there is no workbook, Excel can throw all sorts of odd errors that provide very little insight into what is going on.  So just remove that possibility by adding that default workbook.

```csharp
[TestFixtureSetUp]
public void CreateExcelAppAppropriately()
{
    ExcelApplication = new Application();
    ExcelApplication.Workbooks.Add(Type.Missing);
    ExcelApplication.Visible = true;
}
[TestFixtureTearDown]
public void QuitExcelAppAppropriately()
{
    foreach (Workbook workbook in ExcelApplication.Workbooks)
    {
        workbook.Close(false, false, Type.Missing);
    }
    ExcelApplication.Quit();
}
```

Now that this is setup I can really test how the class will react and behave under test with Excel.  Just to make sure, I verify that the appropriate Excel Application object is created and has a single workbook that was added in the fixture setup.

```csharp
[Test]
public void InitializeDefaultWorkbook()
{
    Assert.GreaterOrEqual(1, ExcelApplication.Workbooks.Count);
}
```

Next on the list is finally getting to the real nitty gritty of the Excel Helper class I’m creating.  My first test to begin this class is as follows.

```csharp
[Test]
public void ExcelHelperInstantiation()
{
    var excelHelper = new ExcelHelper(ExcelApplication);
    Assert.IsNotNull(excelHelper);
    Assert.IsNotNull(excelHelper.ExcelApplication);
}
```

With these tests throwing errors I’m now ready to add my initial class skeleton.

```csharp
/// <summary>
/// This class provides helper utility methods for Excel 2007 that cover common
/// needs such as creating a new worksheet, or getting an insantiated instance
/// of an existing worksheet.
/// </summary>
public class ExcelHelper
{
    /// <summary>
    /// This class has a single constructor used to
    /// setup the needed Microsoft.Office.Interop.Excel.Application
    /// object for use.
    /// </summary>
    /// <param name="excelApplication">Pass the active Excel Application
    /// object.</param>
    public ExcelHelper(Application excelApplication)
    {
        ExcelApplication = excelApplication;
    }
    /// <summary>
    /// This property is set to the active application the class
    /// executes methods against.
    /// </summary>
    public Application ExcelApplication { get; set; }
}
```

Run the test now and you should get a green light.  Moving along I added a test for the first method I want, a way to retrieve a Worksheet that already exists in Excel.  First my test looks something like this.

```csharp
[Test]
public void GetWorksheet()
{
    var newWorksheet = ExcelApplication.Worksheets.Add(Type.Missing, Type.Missing, Type.Missing,
                                                             Type.Missing) as Worksheet;
    const string newWorksheetName = "UniqueName";
    newWorksheet.Name = newWorksheetName;
    Worksheet foundNewWorksheet = new ExcelHelper(ExcelApplication).GetWorksheet(newWorksheetName);
    Assert.IsNotNull(foundNewWorksheet);
    Assert.AreEqual(foundNewWorksheet.Name, newWorksheet.Name);
}
```

I get a red light and then implement the code to return a Worksheet Object based on the passed in worksheet name.  It fails, since the method isn’t created, so I create the method.

```csharp
/// <summary>
/// This method retrieves a specific worksheet by name.
/// </summary>
/// <param name="worksheetName">Pass the name of the
/// worksheet to retrieve.</param>
/// <returns>The Worksheet Object of the requested
/// worksheet, or if not found null.</returns>
public Worksheet GetWorksheet(string worksheetName)
{
    Worksheet foundSheet = null;
    foreach (Worksheet sheet in ExcelApplication.Worksheets)
    {
        if (sheet.Name == worksheetName)
            foundSheet = sheet;
    }
    return foundSheet;
}
```

Next test is for creating a new Worksheet, and adding it to the Excel Workbook.

```csharp
[Test]
public void NewWorksheet()
{
    const string newWorksheetName = "UniqueName";
    new ExcelHelper(ExcelApplication).NewWorksheet(newWorksheetName);
    bool foundWorksheet = false;
    foreach (Worksheet worksheet in ExcelApplication.Worksheets)
    {
        if(worksheet.Name == newWorksheetName)
            foundWorksheet = true;
    }
    Assert.IsTrue(foundWorksheet);
}
```

Red lighted, so I add the method.

```csharp
/// <summary>
/// This method creates a new worksheet with the name
/// specified.
/// </summary>
/// <param name="name">Pass the name you want the new
/// worksheet to have.</param>
/// <returns>Returns the new Worksheet object.</returns>
public Worksheet NewWorksheet(string name)
{
    var returnToThisWorksheet = ExcelApplication.ActiveSheet as _Worksheet;
    var returnSheet = ExcelApplication.Worksheets.Add(
                          Type.Missing,
                          Type.Missing,
                          Type.Missing,
                          Type.Missing) as Worksheet;
    returnSheet.Name = name;
    if (returnToThisWorksheet != null) returnToThisWorksheet.Activate();
    return returnSheet;
}
```

Now that I’ve simplified the methods to create and retrieve a worksheet from Excel, I want to add some functionality around determining if a Worksheet already exists within a workbook.  This is usually a common need within Excel and I find many examples are simply a foreach loop stepping through each Worksheet until it found or did not find the Worksheet it is looking for.  This is a perfect example of something that would be better as a method.

First the test, which I’ll make a static method in case one wants to call this method without instantiating?

```csharp
[Test]
public void IsExistingWorksheetName()
{
    var newWorksheet = ExcelApplication.Worksheets.Add(Type.Missing, Type.Missing, Type.Missing,
                                                                         Type.Missing) as Worksheet;
    const string newWorksheetName = "UniqueName";
    newWorksheet.Name = newWorksheetName;
    ExcelHelper.IsExistingWorksheetName(newWorksheetName, ExcelApplication.Worksheets);
}
```

and a test for a static method?

```csharp
[Test]
public void IsExistingWorksheetNameInstantiatedMethod()
{
    var newWorksheet = ExcelApplication.Worksheets.Add(Type.Missing, Type.Missing, Type.Missing,
                                                              Type.Missing) as Worksheet;
    const string newWorksheetName = "UniqueName";
    newWorksheet.Name = newWorksheetName;
    ExcelHelper helper = new ExcelHelper(ExcelApplication);
    Assert.IsTrue(helper.IsExistingWorksheetName(newWorksheetName));
    foreach (Worksheet sheet in ExcelApplication.Worksheets)
    {
        if (sheet.Name == newWorksheetName)
            sheet.Delete();
    }
    Assert.IsFalse(helper.IsExistingWorksheetName(newWorksheetName));
}
```

As I finished this test and got a red light I realized, I needed to assure the other tests cleaned up after themselves like this one does with the deletion of the Worksheet.  I then went back and add the snippet

```csharp
foreach (Worksheet sheet in ExcelApplication.Worksheets)
{
    if (sheet.Name == newWorksheetName)
        sheet.Delete();
}
```

to each of the tests that needed it.  After the tests where appropriately refactored I ran the tests to assure they still where all green lights except for the one I just created.  I then jumped back into my ExcelHelper Class and created the methods I just wrote tests for.

```csharp
/// <summary>
/// This method checks for existing names to prevent identical name collisions within the
/// worksheet collection.
/// </summary>
/// <param name="worksheetName">Pass in the worksheet name to check for.</param>
/// <param name="existingWorksheets">Pass in the Excel worksheets collection to search in.</param>
/// <returns>Return true if existing worksheet name is found, false if no existing worksheet names.</returns>
public static bool IsExistingWorksheetName(string worksheetName, Sheets existingWorksheets)
{
    foreach (_Worksheet worksheet in existingWorksheets)
    {
        string existingWorksheet = worksheet.Name;
        if (worksheetName == existingWorksheet)
            return true;
    }
    return false;
}
/// <summary>
/// This method checks for existing names to prevent identical name collisions within the
/// worksheet collection.
/// </summary>
/// <param name="worksheetName">Pass in the worksheet name to check for.</param>
/// <returns>Return true if existing worksheet name is found, false if no existing worksheet names.</returns>
public bool IsExistingWorksheetName(string worksheetName)
{
    return IsExistingWorksheetName(worksheetName, ExcelApplication.Worksheets);
}
```

For this entry we’ve covered appropriate tests and methods for getting an Excel Worksheet, creating a new Excel Worksheet, and finding out if a Excel Worksheet Name is already taken.  In my next entry on this topic I’ll keep adding more Excel Helper Methods that will help make Excel Addin Development easier.

[![kick it on DotNetKicks.com](http://www.dotnetkicks.com/Services/Images/KickItImageGenerator.ashx?url=http%3a%2f%2fwww.adronbhall.com%2fblogs%2ftechnology__software_development%2fpost%2f2009%2f08%2f19%2fExcel-Helper-Utilities-Library-Part-Two.aspx&bgcolor=3333FF&cfgcolor=CC3300)](http://www.dotnetkicks.com/kick/?url=http%3a%2f%2fwww.adronbhall.com%2fblogs%2ftechnology__software_development%2fpost%2f2009%2f08%2f19%2fExcel-Helper-Utilities-Library-Part-Two.aspx)
