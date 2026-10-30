---
title: Excel Helper Utilities Library Part Three
date: 2009-08-27 12:06:21 -0700
last_modified_at: 2009-08-27 12:06:21 -0700
permalink: /2009/08/27/excel-helper-utilities-library-part-three/
slug: excel-helper-utilities-library-part-three
wp_id: 662
original_url: https://compositecode.blog/2009/08/27/excel-helper-utilities-library-part-three/
categories:
- Uncategorized Bits
tags: []
excerpt: Obviously I’ve missed my self made time schedule of Monday, Wednesday, and Friday for these entries, so bare with me while I get em’ published as fast as possible. With that written . . . Welcome to part three of the Excel Helper Utilities Library series. In this entry I will cover the extension of …
---

Obviously I’ve missed my self made time schedule of Monday, Wednesday, and Friday for these entries, so bare with me while I get em’ published as fast as possible.  With that written . . .

Welcome to part three of the Excel Helper Utilities Library series.  In this entry I will cover the extension of the ExcelHelper class created in [Part Two](http://www.adronbhall.com/blogs/technology__software_development/post/2009/08/19/Excel-Helper-Utilities-Library-Part-Two.aspx).  The first method is one I wrote ages ago for VB.NET, but I’ve added here for the C# helper.  As always, tests first.

```
[Test]
public void GetColumnLetterA()
{
    string twentySeventColumn = ExcelHelper.GetExcelColumnLetter(1);
    Assert.AreEqual(twentySeventColumn, "A");
}

[Test]
public void GetColumnLetterB()
{
    string twentySeventColumn = ExcelHelper.GetExcelColumnLetter(2);
    Assert.AreEqual(twentySeventColumn, "B");
}

[Test]
public void GetColumnLetterAa()
{
    string twentySeventColumn = ExcelHelper.GetExcelColumnLetter(703);
    Assert.AreEqual(twentySeventColumn, "AAA");
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

. . . and the implemented code . . .

```
/// <summary>
/// This method gets the appropriate "A" thru "ZZZ" column header for Excel based
/// on a passed in long data type.
/// </summary>
/// <param name="columnIndex">Pass in a long type to derive the appropriate column header letter.</param>
/// <returns>A string of the appropriate "A" thru "ZZZ" header letter.</returns>
public static string GetExcelColumnLetter(int columnIndex)
{
    int dividend = columnIndex;
    string columnName = String.Empty;

    while (dividend > 0)
    {
        int mod = (dividend - 1)%26;
        columnName = Convert.ToChar(65 + mod) + columnName;
        dividend = ((dividend - mod)/26);
    }
    return columnName;
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

The next thing I wanted was a column range set, basically something that would return "A:A" if I passed it the start column index and ending column index.  Easy enough, again, tests first.

```
[Test]
public void GetColumnLetterSetAandA()
{
    const string columnStart = "1";
    const string columnEnd = "4";
    const string expectedValue = "A:D";
    string returnedValue = ExcelHelper.GetExcelColumnSet(columnStart, columnEnd);
    Assert.AreEqual(expectedValue, returnedValue);
}

[Test]
public void GetColumnLetterSetAandAaa()
{
    const string columnStart = "1";
    const string columnEnd = "703";
    const string expectedValue = "A:AAA";
    string returnedValue = ExcelHelper.GetExcelColumnSet(columnStart, columnEnd);
    Assert.AreEqual(expectedValue, returnedValue);
}

[Test]
public void GetColumnLetterSetAandZ()
{
    const string columnStart = "1";
    const string columnEnd = "26";
    const string expectedValue = "A:Z";
    string returnedValue = ExcelHelper.GetExcelColumnSet(columnStart, columnEnd);
    Assert.AreEqual(expectedValue, returnedValue);
}
```

. . . and the implementation . . .

```
/// <summary>
/// This method returns the ("A:ZZZ") part of the Range("A:ZZZ") column interface.
/// </summary>
/// <param name="firstColumn">Enter the first column to start the range with.</param>
/// <param name="secondColumn">Enter the second column to end the range with.</param>
/// <returns>A string formatted as A:ZZZ is returned from this method.</returns>
public static string GetExcelColumnSet(string firstColumn, string secondColumn)
{
    int firstColumnValue = Convert.ToInt32(firstColumn);
    int secondColumnValue = Convert.ToInt32(secondColumn);
    return GetExcelColumnLetter(firstColumnValue) + ":" + GetExcelColumnLetter(secondColumnValue);
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

That is the short and sweet of this entry.  I have to catch a bus and get a move on, but the next entry will be a few cell manipulations to simplify capturing and putting things in the cells in Excel.

If you visit, please give this entry a kick over at [![kick it on DotNetKicks.com](http://www.dotnetkicks.com/Services/Images/KickItImageGenerator.ashx?url=http%3a%2f%2fwww.adronbhall.com%2fblogs%2ftechnology__software_development%2fpost%2f2009%2f08%2f27%2fExcel-Helper-Utilities-Library-Part-Three.aspx&bgcolor=3333FF&cfgcolor=CC3300)](http://www.dotnetkicks.com/kick/?url=http%3a%2f%2fwww.adronbhall.com%2fblogs%2ftechnology__software_development%2fpost%2f2009%2f08%2f27%2fExcel-Helper-Utilities-Library-Part-Three.aspx)
