---
title: 'Excel Programming :: Tip o'' The Day'
date: 2009-06-14 14:11:48 +0000
last_modified_at: 2009-06-14 14:11:48 +0000
permalink: /2009/06/14/excel-programming-tip-o-the-day/
slug: excel-programming-tip-o-the-day
wp_id: 643
original_url: https://compositecode.blog/2009/06/14/excel-programming-tip-o-the-day/
categories:
- Uncategorized Bits
tags: []
excerpt: When creating an Excel Application there are some things to keep in mind. Recently I was creating some tests, which I’m not sure if they’d be "unit test", but they do test Excel. I created a fixture setup and a fixture tear down that would create my Excel Application object that I?d want to test …
---

When creating an Excel Application there are some things to keep in mind.  Recently I was creating some tests, which I’m not sure if they’d be "unit test", but they do test Excel.  I created a fixture setup and a fixture tear down that would create my Excel Application object that I?d want to test again.  The code I ended up with is shown below.

```
[TestFixture]
public class ConnectionManagement
{
    public Application ExcelApplication { get; set; }

    [TestFixtureSetUp]
    public void CreateExcelAppAppropriately()
    {
        ExcelApplication = new Application();
        ExcelApplication.Workbooks.Add(Type.Missing);
    }

    [TestFixtureTearDown]
    public void QuitExcelAppAppropriately()
    {
        foreach(Workbook workbook in ExcelApplication.Workbooks)
        {
            workbook.Close(false, false, Type.Missing);
        }

        ExcelApplication.Quit();
    }
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

Now if anyone has a better idea on how to test Excel and knowing the code will work against the actual Excel Application, PLEASE, let me know as this doesn’t feel like the best way to do this.  I keep getting the sinking suspicion that there should be a better way to test Excel Application Addins, Spreadsheet code and such.
