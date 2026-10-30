---
title: Making Maths Functions n' Stuff Part 5
date: 2008-10-16 02:02:30 +0000
last_modified_at: 2008-10-16 02:02:30 +0000
permalink: /2008/10/16/making-maths-functions-n-stuff-part-5/
slug: making-maths-functions-n-stuff-part-5
wp_id: 207
original_url: https://compositecode.blog/2008/10/16/making-maths-functions-n-stuff-part-5/
categories:
- Uncategorized Bits
tags: []
excerpt: There are a few more math functions and such that I wanted to add to the math application before calling it finished. If anyone out in the ole’ blogosphere has any other math functions they’d like to have added to the application please shoot me an e-mail or two on which ones to add. Neil? …
---

There are a few more math functions and such that I wanted to add to the math application before calling it finished.  If anyone out in the ole’ *blogosphere* has any other math functions they’d like to have added to the application please shoot me an e-mail or two on which ones to add.  Neil?  Any mathematicians out there?

First of the final additions.  Let’s throw an even or odd method in there.  As always, got to have a test or two.

```
   1:          [Test]
   2:          public void TestIsEvenYesLong()
   3:          {
   4:              // Just to prove the point.
   5:              const long evenNumber = 9223372036854775806;
   6:              Console.WriteLine("Test Number: " + evenNumber);
   7:              Console.WriteLine("Is Even? " + MathCookbook.Functions.IsEven(evenNumber));
   8:              Assert.IsTrue(MathCookbook.Functions.IsEven(evenNumber));
   9:          }
  10:
  11:          [Test]
  12:          public void TestIsEvenNoLong()
  13:          {
  14:              // Just to prove the point.
  15:              const long oddNumber = 9223372036854775807;
  16:              Console.WriteLine("Test Number: " + oddNumber);
  17:              Console.WriteLine("Is Even? " + MathCookbook.Functions.IsEven(oddNumber));
  18:              Assert.IsFalse(MathCookbook.Functions.IsEven(oddNumber));
  19:          }
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

Then toss the method in.

```
   1:          /// <summary>
   2:          /// This method returns true for an even number and false for an odd number.
   3:          /// </summary>
   4:          /// <param name="number">Enter the number to check for even or odd value.</param>
   5:          /// <returns>This method returns true for an even number and false for an odd number.</returns>
   6:          public static bool IsEven(long number)
   7:          {
   8:              return ((number & 1)==0);
   9:          }
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

Next of the final additions is a method to obtain rounding based on rounding up, down, or following the IEEE Standard 754, section 4, which rounds to the even number regardless of up or down.  Kind of odd, but here’s the tests.

```
   1:          [RowTest]
   2:          [Row(3.5, 4)]
   3:          [Row(3.3, 3)]
   4:          [Row(3.7, 4)]
   5:          [Row(2.5, 3)]
   6:          public void TestRoundUp(double roundThis, long answer)
   7:          {
   8:              Assert.AreEqual(
   9:                  MathCookbook.Functions.Round(
  10:                      MathCookbook.Functions.RoundDirection.Up, roundThis),
  11:                  answer);
  12:          }
  13:
  14:          [RowTest]
  15:          [Row(3.5, 3)]
  16:          [Row(3.3, 3)]
  17:          [Row(3.7, 4)]
  18:          [Row(2.5, 2)]
  19:          public void TestRoundDown(double roundThis, long answer)
  20:          {
  21:              Assert.AreEqual(
  22:                  MathCookbook.Functions.Round(
  23:                      MathCookbook.Functions.RoundDirection.Down, roundThis),
  24:                  answer);
  25:          }
  26:
  27:          [RowTest]
  28:          [Row(3.5, 4)]
  29:          [Row(3.3, 3)]
  30:          [Row(3.7, 4)]
  31:          [Row(2.5, 2)]
  32:          public void TestRoundIeeeStyle(double roundThis, long answer)
  33:          {
  34:              Assert.AreEqual(
  35:                  MathCookbook.Functions.Round(
  36:                      MathCookbook.Functions.RoundDirection.IeeeStandard, roundThis),
  37:                  answer);
  38:          }
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

Here’s the method.

```
   1:          /// <summary>
   2:          /// This method rounds up using the up, down, or IEEE standard rounding direction.
   3:          /// </summary>
   4:          /// <param name="direction">Enter the direction of rounding to use.</param>
   5:          /// <param name="roundThis">Enter the number in which to round.</param>
   6:          /// <returns>A double type rounded to the nearest number based on the round direction.</returns>
   7:          public static double Round(RoundDirection direction, double roundThis)
   8:          {
   9:              switch (direction)
  10:              {
  11:                  case RoundDirection.Up:
  12:                      return Math.Floor(roundThis + .5);
  13:                  case RoundDirection.Down:
  14:                      double floorValue = Math.Floor(roundThis);
  15:                      return (roundThis - floorValue) > .5 ? floorValue + 1 : floorValue;
  16:                  case RoundDirection.IeeeStandard:
  17:                      return Math.Round(roundThis);
  18:              }
  19:              return 0;
  20:          }
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

The final addition is the temperature measurement conversions.  Test first.

```
   1:          [RowTest]
   2:          [Row(0, 32)]
   3:          [Row(29.444444444444446, 85)]
   4:          [Row(7.5, 45.5)]
   5:          public void TestCelsiusToFehrenheit(double celsius, double fahrenheit)
   6:          {
   7:              Assert.AreEqual(MathCookbook.Functions.GetCelsiusToFahrenheit(celsius), fahrenheit);
   8:          }
   9:
  10:          [RowTest]
  11:          [Row(0, 32)]
  12:          [Row(29.444444444444446, 85)]
  13:          [Row(7.5, 45.5)]
  14:          public void TestFehrenheitToCelsius(double fahrenheit, double celsius)
  15:          {
  16:              Assert.AreEqual(MathCookbook.Functions.GetFahrenheitToCelsius(celsius), fahrenheit);
  17:          }
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

The method.

```
   1:          /// <summary>
   2:          /// This method converts fahrenheit to celsius.
   3:          /// </summary>
   4:          /// <param name="fahrenheit">Enter the fahrenheit temperature to convert.</param>
   5:          /// <returns>A double type of the celsius temperature.</returns>
   6:          public static double GetFahrenheitToCelsius(double fahrenheit)
   7:          {
   8:              return ((.5 / .9) * (fahrenheit - 32));
   9:          }
  10:
  11:          /// <summary>
  12:          /// This method converts celsius to fahrenheit.
  13:          /// </summary>
  14:          /// <param name="celsius">Enter the celsius temperature to convert.</param>
  15:          /// <returns>A double type of the fahrenheit temperature.</returns>
  16:          public static double GetCelsiusToFahrenheit(double celsius)
  17:          {
  18:              return (((.9 / .5) * celsius) + 32);
  19:          }
```
