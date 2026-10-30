---
title: Excel Helper Utilities Library Part One
date: 2009-08-19 02:14:00 +0000
last_modified_at: 2009-08-19 02:14:00 +0000
permalink: /2009/08/19/excel-helper-utilities-library-part-one/
slug: excel-helper-utilities-library-part-one
wp_id: 659
original_url: https://compositecode.blog/2009/08/19/excel-helper-utilities-library-part-one/
categories:
- Uncategorized Bits
tags: []
excerpt: I’m kicking off a series that is a long time in the making. The series is 99% complete at this point, and will be published every couple days. Right now I?m aiming for a Monday, Wednesday, Friday type of frequency, but might throw in an extra one here or there. When completed the code will …
---

I’m kicking off a series that is a long time in the making.  The series is 99% complete at this point, and will be published every couple days.  Right now I?m aiming for a Monday, Wednesday, Friday type of frequency, but might throw in an extra one here or there.  When completed the code will be posted to [CodePlex](http://www.codeplex.com/) for easy download & an additions that someone might want to contribute.  Just hit me up at *adron [at@] adronbhall [dot.] com*.

Here?s a code file I’ve put together to help project using Excel 2007.  These are just some small helper methods, etc., that remove some of the redundant Type.Missing and other insidious things one has to go through when developing with Excel.

This first class is a pure and simple utility class to help clean up strings for use in certain situations that come up with Excel.  Some examples might be when trying to clean up a string for a worksheet name.

Of course, as usual, the first thing I hit where the unit tests.  Since these methods are relatively simple, I just went ahead and wrote tests for each.

```
[TestFixture]
public class StringParsingTests
{
    [Test]
    public void IsNumberTrue()
    {
        const string isNumber = "234";
        Assert.IsTrue(StringParsing.IsNumeric(isNumber));
    }

    [Test]
    public void IsNumberFalse()
    {
        const string notNumber = "noNumberHere";
        Assert.IsFalse(StringParsing.IsNumeric(notNumber));
    }

    [Test]
    public void IsNumberFloat()
    {
        const string isNumber = "232.4419";
        Assert.IsTrue(StringParsing.IsNumeric(isNumber));
    }

    [Test]
    public void IsAlphaNumericTrue()
    {
        const string isAlphaNumeric = "asdf1234";
        Assert.IsTrue(StringParsing.IsValidAlphaNumeric(isAlphaNumeric));
    }

    [Test]
    public void IsAlphaNumericFalse()
    {
        const string notAlphaNumeric = "asdf.!~1234";
        Assert.IsFalse(StringParsing.IsValidAlphaNumeric(notAlphaNumeric));
    }

    [Test]
    public void RemoveSpecialCharactersRemoval()
    {
        const string notAlphaNumeric = "asdf!@#$";
        string isAlphaNumeric = StringParsing.RemoveSpecialCharacters(notAlphaNumeric);
        Assert.IsFalse(StringParsing.IsValidAlphaNumeric(isAlphaNumeric));
    }

    [Test]
    public void RemoveSpecialCharactersCheckOriginalString()
    {
        const string notAlphaNumeric = "asdf!@#$";
        const string expectedResult = "asdf    ";
        string isAlphaNumeric = StringParsing.RemoveSpecialCharacters(notAlphaNumeric);
        Assert.AreEqual(expectedResult, isAlphaNumeric);
    }

    [Test]
    public void TrimAndRemoveSpecialCharacters()
    {
        const string notAlphaNumeric = "asdf!@#$";
        string isAlphaNumeric = StringParsing.TrimAndRemoveSpecialCharacters(notAlphaNumeric);
        Assert.IsTrue(StringParsing.IsValidAlphaNumeric(isAlphaNumeric));
    }

    [Test]
    public void TrimAndRemoveSpecialCharactersCheckOriginalString()
    {
        const string notAlphaNumeric = "asdf!@#$";
        const string expectedResult = "asdf";
        string isAlphaNumeric = StringParsing.TrimAndRemoveSpecialCharacters(notAlphaNumeric);
        Assert.AreEqual(expectedResult, isAlphaNumeric);
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

The class I created is named StringParsing within a namespace of Abh.Core.Excel2k7.Utilities.  I?ve left the comments in place in case you want to copy & paste the code for use.

```
using System;
using System.Text.RegularExpressions;

namespace Abh.Core.Excel2k7.Utilities
{
    /// <summary>
    /// This class provides static methods for parsing and manipulating strings to provide
    /// Excel compliant, or other cleaning methods to trim, check for alphanumeric, and numeric
    /// data types within a string.  These methods are in addition to most existing methods
    /// already available on existing objects in the .NET Framework.
    /// </summary>
    public class StringParsing
    {
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

Within the class are four methods:

The first method is RemoveSpecialCharacters(string stringToClean).  This method does exactly what the name implies, it removes a selection of special characters from a passed in string.

```
/// <summary>
/// This method removes special characters from a string.
/// </summary>
/// <param name="stringToClean">Pass in the string to remove the special characters from.</param>
/// <returns>A string based on the passed in string without special characters is returned.</returns>
public static string RemoveSpecialCharacters(string stringToClean)
{
    return stringToClean.Replace("!", " ").
        Replace("@", " ").
        Replace("#", " ").
        Replace("$", " ").
        Replace("%", " ").
        Replace("^", " ").
        Replace("&", " ").
        Replace("*", " ").
        Replace("(", " ").
        Replace(")", " ").
        Replace("_", "").
        Replace("+", "").
        Replace("-", "").
        Replace("=", "").
        Replace("`", "").
        Replace("~", "").
        Replace("<", "").
        Replace(">", "").
        Replace("?", "").
        Replace(":", "").
        Replace(@"\", "").
        Replace("{", "").
        Replace("}", "").
        Replace("|", "").
        Replace("[", "").
        Replace("]", "").
        Replace(";", "").
        Replace("'", "").
        Replace(",", "").
        Replace(".", "").
        Replace("/", "").
        Replace("'", "");
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

The second method is TrimAndRemoveSpecialCharacters(string stringToClean).  Again, this method name describes exactly what the method does.  The string passed in has the edges trimmed of whitespace and then executes the previous method to remove special characters.

```
/// <summary>
/// This method removes special characters and trims any white space from the left and right of the
/// string.
/// </summary>
/// <param name="stringToClean">Pass in the string to remove the special characters from.</param>
/// <returns>A string based on the passed in string without special characters and trimmed
/// of white space is returned.</returns>
public static string TrimAndRemoveSpecialCharacters(string stringToClean)
{
    RemoveSpecialCharacters(stringToClean);
    return stringToClean.Trim();
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

The third method, again with the theme of self describing method names, is IsValidAlphaNumeric(string verifyThis).

```
/// <summary>
/// This method takes a string as input and return a boolean value representing
/// if the string is or is not alphanumeric.
/// </summary>
/// <param name="verifyThis">Pass the string to verify if it is or is not alphanumeric.</param>
/// <returns>True is returned if alphanumeric, false if not.</returns>
public static bool IsValidAlphaNumeric(string verifyThis)
{
    if (String.IsNullOrEmpty(verifyThis))
        return false;
    for (int i = 0; i < verifyThis.Length; i++)
    {
        if (!(Char.IsLetter(verifyThis[i])) && (!(Char.IsNumber(verifyThis[i]))))
            return false;
    }
    return true;
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

The last method is one of the most needed of all, the IsNumeric(string verifyThis) method.  Again, self explanatory.

```
/// <summary>
/// This method takes a string as input and returns a boolean value representing
/// if the string is numeric or not.
/// </summary>
/// <param name="verifyThis">Pass the string to verify if it is or is not numeric.</param>
/// <returns>True is returned if numeric, false if not.</returns>
public static bool IsNumeric(string verifyThis)
{
    verifyThis = verifyThis.Trim();
    var m = regex.Match(verifyThis);
    return !string.IsNullOrEmpty(m.Value);
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

That covers the string parsing utility file.  More to come later ? stay tuned.  The next few entries I’ll cover the ExcelHelper Class I’ve written that simplifies creation & retrieval of Excel Worksheets, and more.

[![kick it on DotNetKicks.com](http://www.dotnetkicks.com/Services/Images/KickItImageGenerator.ashx?url=http%3a%2f%2fwww.adronbhall.com%2fblogs%2ftechnology__software_development%2fpost%2f2009%2f08%2f19%2fExcel-Helper-Utilities-Library-Part-One.aspx&bgcolor=3333FF&cfgcolor=CC3300)](http://www.dotnetkicks.com/kick/?url=http%3a%2f%2fwww.adronbhall.com%2fblogs%2ftechnology__software_development%2fpost%2f2009%2f08%2f19%2fExcel-Helper-Utilities-Library-Part-One.aspx)
