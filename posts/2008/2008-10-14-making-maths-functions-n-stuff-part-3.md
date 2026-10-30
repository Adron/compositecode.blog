---
title: Making Maths Functions n' Stuff Part 3
date: 2008-10-14 01:05:31 +0000
last_modified_at: 2008-10-14 01:05:31 +0000
permalink: /2008/10/14/making-maths-functions-n-stuff-part-3/
slug: making-maths-functions-n-stuff-part-3
wp_id: 210
original_url: https://compositecode.blog/2008/10/14/making-maths-functions-n-stuff-part-3/
categories:
- Uncategorized Bits
tags: []
excerpt: 'I’ll just hit the code first thing on this entry. I first started, as usual, with a few tests. My goal for the next two methods were to convert radians to degrees and degrees to radians. If you want to review, check out part 2. First test for degrees to radians. 1: [Test] 2: public …'
---

I’ll just hit the code first thing on this entry.  I first started, as usual, with a few tests.  My goal for the next two methods were to convert radians to degrees and degrees to radians.  If you want to review, check out [part 2](http://www.adronbhall.com/blogs/technology__software_development/post/2008/10/10/Making-Maths-Functions-n-Stuff-Part-2.aspx).

First test for degrees to radians.

```
   1:          [Test]
   2:          public void TestDegreesToRadians()
   3:          {
   4:              const double radiansAnswer = 0.174532925199433;
   5:              const double degrees = 10;
   6:
   7:              Console.WriteLine("Entered Radians: " + degrees);
   8:              Console.WriteLine("The Returned Answer:" + radiansAnswer);
   9:              Console.WriteLine("The Known Answer:" + MathCookbook.Functions.ConvertDegreesToRadians(degrees));
  10:
  11:              Assert.AreEqual(radiansAnswer, MathCookbook.Functions.ConvertDegreesToRadians(degrees));
  12:          }
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

Then implement the method.  Since I know what the answers are, because one can simply use calc, I just make the test work by creating a working method.

```
   1:          /// <summary>
   2:          /// This method returns the radians for the passed degrees.
   3:          /// </summary>
   4:          /// <param name="degrees">Enter the degrees to convert.</param>
   5:          /// <returns>The radians.</returns>
   6:          public static double ConvertDegreesToRadians(double degrees)
   7:          {
   8:              return (Math.PI / 180) * degrees;
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

Second test for radians to degrees.

```
   1:          [Test]
   2:          public void TestRadiansToDegrees()
   3:          {
   4:              const double degreesAnswer = 572.957795130823;
   5:              const double radians = 10;
   6:
   7:              Console.WriteLine("Entered Radians: " + radians);
   8:              Console.WriteLine("The Returned Answer: " + degreesAnswer);
   9:              Console.WriteLine("The Known Answer: " + MathCookbook.Functions.ConvertRadiansToDegrees(radians));
  10:
  11:              Assert.AreEqual(degreesAnswer, MathCookbook.Functions.ConvertRadiansToDegrees(radians));
  12:          }
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

Then implement the method.  Again, just the working method is fine.

```
   1:          /// <summary>
   2:          /// This method returns the degrees for the passed radians.
   3:          /// </summary>
   4:          /// <param name="radians">Enter the radians to convert.</param>
   5:          /// <returns>The degrees</returns>
   6:          public static double ConvertRadiansToDegrees(double radians)
   7:          {
   8:              return (180 / Math.PI) * radians;
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

In the above tests, I added the Console.WriteLine() methods because in ReSharper’s testing VS.NET add in it presents a rather clean report below the tests.  Always nice, and offers good evidence of what might or might not be passing immediately.  Sure, one can write out in the string passing of the assertion method, but I prefer to see it cleanly written out before the test result.

[![](/images/adronhall.smugmug.com/photos/390647308_gE5AX-M.png)](http://adronhall.smugmug.com/gallery/6181616_zg5Ko/1/390647308_gE5AX)
