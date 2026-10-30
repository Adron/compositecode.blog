---
title: Just Some Excel Helpers and Respective Unit Tests
date: 2008-07-31 06:20:26 +0000
last_modified_at: 2008-07-31 06:20:26 +0000
permalink: /2008/07/31/just-some-excel-helpers-and-respective-unit-tests/
slug: just-some-excel-helpers-and-respective-unit-tests
wp_id: 257
original_url: https://compositecode.blog/2008/07/31/just-some-excel-helpers-and-respective-unit-tests/
categories:
- Uncategorized Bits
tags: []
excerpt: Just some semi-elegant stuff I’ve conjured up recently to get column names in Excel and do some other functional things. I wrote this code in a true TDD fashion. It still, for some reason, seems odd to me to write tests in VB, since it was always a language that encouraged dirtiness. But alas, this …
---

Just some semi-elegant stuff I’ve conjured up recently to get column names in Excel and do some other functional things.  I wrote this code in a true TDD fashion.  It still, for some reason, seems odd to me to write tests in VB, since it was always a language that encouraged dirtiness.  But alas, this is fairly solid stuff.

```
Imports NUnit.Framework

<TestFixture()> _
Public Class HelperTests
    <Test()> <Category("Presenter Helper Tests")> _
    Public Sub TestHelperGetExcelColumnLetterSingleLetter()
        Dim theLetter As String = Helper.GetExcelColumnLetter(3)
        Assert.AreEqual(theLetter, "C")
    End Sub

    <Test()> <Category("Presenter Helper Tests")> _
    Public Sub TestHelperGetExcelColumnLetterDoubleLetter()
        Dim theLetter As String = Helper.GetExcelColumnLetter(29)
        Assert.AreEqual(theLetter, "AC")
    End Sub

    <Test()> <Category("Presenter Helper Tests")> _
    Public Sub TestHelperGetExcelColumnDoubleLetterThirdAlphabet()
        Dim theLetter As String = Helper.GetExcelColumnLetter(56)
        Assert.AreEqual(theLetter, "BD")
    End Sub

    <Test()> <Category("Presenter Helper Tests")> _
   Public Sub TestHelperGetExcelColumnTripleLetter()
        Dim theLetter As String = Helper.GetExcelColumnLetter(2356)
        Assert.AreEqual(theLetter, "CLP")
    End Sub

    <Test()> <Category("Presenter Helper Tests")> _
    Public Sub TestHelperGetExcelColumnTripleLetterSomething()
        Dim theLetter As String = Helper.GetExcelColumnLetter(14999)
        Assert.AreEqual(theLetter, "VDW")
    End Sub

    <Test()> <Category("Presenter Helper Tests")> _
        Public Sub TestHelperGetExcelColumnTripleLetterTheEndOfZzz()
        Dim theLetter As String = Helper.GetExcelColumnLetter(18278)
        Assert.AreEqual(theLetter, "ZZZ")
    End Sub

    <Test()> <Category("Presenter Helper Tests")> _
    Public Sub TestHelperGetExcelColumnF1C1()
        Dim theColumnF1C1 As String = Helper.GetExcelColumnF1C1(3, 6)
        Assert.AreEqual("C:F", theColumnF1C1)
    End Sub

End Class
```

I churned out each of these tests, the first few I did at one time, counting out where the column “letters” would be derived at various column numbers.  It almost got confusing a few times.  All tests of course went red and I began coding the innards of the method.

What I came up with, after a few gotchas here and there is this.

```
Public Class Helper
    ''' <summary>
    ''' This method gets the appropriate "A" thru "ZZZ" column header for Excel based
    ''' on a passed in long data type.
    ''' </summary>
    ''' <param name="colNum">Pass in a long type to derive the appropriate column header letter.</param>
    ''' <returns>A string of the appropriate "A" thru "ZZZ" header letter.</returns>
    Public Shared Function GetExcelColumnLetter(ByVal colNum As Long) As String
        Do
            GetExcelColumnLetter = Chr(65 + (colNum - 1) Mod 26) & GetExcelColumnLetter
            colNum = (colNum - 1) \ 26
        Loop While colNum > 0
    End Function

    ''' <summary>
    ''' This method returns the ("A:ZZZ") part of the Range("A:ZZZ") column interface.
    ''' </summary>
    ''' <param name="firstColumn">Enter the first column to start the range with.</param>
    ''' <param name="secondColumn">Enter the second column to end the range with.</param>
    ''' <returns>A string formatted as A:ZZZ is returned from this method.</returns>
    Public Shared Function GetExcelColumnF1C1(ByVal firstColumn As String, ByVal secondColumn As String) As String
        Return GetExcelColumnLetter(firstColumn) + ":" + GetExcelColumnLetter(secondColumn)
    End Function
End Class
```

If you work with Excel frequently you know all about F1C1, which I decided to stick on the end of the GetExcelColumnF1C1.  Not sure if it really makes sense, but since so much of Excel is kind of just mess, I figured it might conjure the right thought in a coder’s mind.

[![kick it on DotNetKicks.com](http://www.dotnetkicks.com/Services/Images/KickItImageGenerator.ashx?url=http%3a%2f%2fadronbhall.com%2fblogs%2ftechnology__software_development%2farchive%2f2008%2f07%2f31%2f7493.aspx&bgcolor=3333FF&cfgcolor=CC3300)](http://www.dotnetkicks.com/kick/?url=http%3a%2f%2fadronbhall.com%2fblogs%2ftechnology__software_development%2farchive%2f2008%2f07%2f31%2f7493.aspx)

Technorati Tags: [Office 2007](http://technorati.com/tags/Office%202007),[Office](http://technorati.com/tags/Office),[Excel](http://technorati.com/tags/Excel),[VB](http://technorati.com/tags/VB),[TDD](http://technorati.com/tags/TDD),[Unit Test](http://technorati.com/tags/Unit%20Test)

del.icio.us Tags: [Office 2007](http://del.icio.us/popular/Office%202007),[Office](http://del.icio.us/popular/Office),[Excel](http://del.icio.us/popular/Excel),[VB](http://del.icio.us/popular/VB),[TDD](http://del.icio.us/popular/TDD),[Unit Test](http://del.icio.us/popular/Unit%20Test)
