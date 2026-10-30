---
title: 'Excel Spreadsheet Tests :: Tip o'' The Day'
date: 2009-06-28 12:00:42 -0700
last_modified_at: 2009-06-28 12:00:42 -0700
permalink: /2009/06/28/excel-spreadsheet-tests-tip-o-the-day/
slug: excel-spreadsheet-tests-tip-o-the-day
wp_id: 647
original_url: https://compositecode.blog/2009/06/28/excel-spreadsheet-tests-tip-o-the-day/
categories:
- Uncategorized Bits
tags: []
excerpt: While working through some of the Excel scenarios lately I’ve come upon some more ways to test Excel. Create an Excel Application instance with the default workbook. Doing this will drastically speed up your tests. Do this in the fixture setup & assign it to a property of the test class. This way, no more …
---

While working through some of the Excel scenarios lately I’ve come upon some more ways to test Excel.

Create an Excel Application instance with the default workbook.  Doing this will drastically speed up your tests.  Do this in the fixture setup & assign it to a property of the test class.  This way, no more startup and tear down of the Excel object for each test.

```
public Application ExcelApplication { get; set; }

[TestFixtureSetUp]
public void CreateExcelAppAppropriately()
{
    ExcelApplication = new Application();
    ExcelApplication.Workbooks.Add(Type.Missing);
    ExcelApplication.Visible = true;
}
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

That will give you a good kick start when you end up with a few dozen or more tests.  Starting up and killing the Excel Instance on each test can be brutal in overall performance.  For the shutdown of the tests, as long as you have clean code and don?t have odd Excel threads or something running off everywhere, the fixture shutdown can be as simple as below.

```
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

One other thing I like to do is add a boolean value that sets the Excel instance to stay visible and not close after the tests.  I create a private bool and then set it in any test I?m currently working with.  When I?m done I just remove the assignment and let it default to false.  This way the Excel instance doesn?t stay open for the build & tests on the build server.

```
private bool reviewExcelPostTests;

[TestFixtureTearDown]
public void QuitExcelAppAppropriately()
{
    if (reviewExcelPostTests)
        return;

    foreach (Workbook workbook in ExcelApplication.Workbooks)
    {
        workbook.Close(false, false, Type.Missing);
    }
    ExcelApplication.Quit();
}
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

That’s it for my Excel tips today, I’ll have some more coming in the near future.
