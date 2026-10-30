---
title: 'Unit Testing Microsoft''s Way? :: Tip o'' The Day'
date: 2008-12-14 05:25:31 -0800
last_modified_at: 2008-12-14 05:25:31 -0800
permalink: /2008/12/14/unit-testing-microsofts-way-tip-o-the-day/
slug: unit-testing-microsofts-way-tip-o-the-day
wp_id: 571
original_url: https://compositecode.blog/2008/12/14/unit-testing-microsofts-way-tip-o-the-day/
categories:
- Uncategorized Bits
tags: []
excerpt: 'I really don’t get the complexity Microsoft has put into their testing framework. The basic testing class that one gets looks like this. 1: using System; 2: using System.Text; 3: using System.Collections.Generic; 4: using System.Linq; 5: using Microsoft.VisualStudio.TestTools.UnitTesting; 6: 7: namespace PipServices.Tests 8: { 9: /// 10: /// Summary description for UnitTest1 11: …'
---

I really don’t get the complexity Microsoft has put into their testing framework.  The basic testing class that one gets looks like this.

```
   1:  using System;
   2:  using System.Text;
   3:  using System.Collections.Generic;
   4:  using System.Linq;
   5:  using Microsoft.VisualStudio.TestTools.UnitTesting;
   6:
   7:  namespace PipServices.Tests
   8:  {
   9:      /// <summary>
  10:      /// Summary description for UnitTest1
  11:      /// </summary>
  12:      [TestClass]
  13:      public class UnitTest1
  14:      {
  15:          public UnitTest1()
  16:          {
  17:              //
  18:              // TODO: Add constructor logic here
  19:              //
  20:          }
  21:
  22:          private TestContext testContextInstance;
  23:
  24:          /// <summary>
  25:          ///Gets or sets the test context which provides
  26:          ///information about and functionality for the current test run.
  27:          ///</summary>
  28:          public TestContext TestContext
  29:          {
  30:              get
  31:              {
  32:                  return testContextInstance;
  33:              }
  34:              set
  35:              {
  36:                  testContextInstance = value;
  37:              }
  38:          }
  39:
  40:          #region Additional test attributes
  41:          //
  42:          // You can use the following additional attributes as you write your tests:
  43:          //
  44:          // Use ClassInitialize to run code before running the first test in the class
  45:          // [ClassInitialize()]
  46:          // public static void MyClassInitialize(TestContext testContext) { }
  47:          //
  48:          // Use ClassCleanup to run code after all tests in a class have run
  49:          // [ClassCleanup()]
  50:          // public static void MyClassCleanup() { }
  51:          //
  52:          // Use TestInitialize to run code before running each test
  53:          // [TestInitialize()]
  54:          // public void MyTestInitialize() { }
  55:          //
  56:          // Use TestCleanup to run code after each test has run
  57:          // [TestCleanup()]
  58:          // public void MyTestCleanup() { }
  59:          //
  60:          #endregion
  61:
  62:          [TestMethod]
  63:          public void TestMethod1()
  64:          {
  65:              //
  66:              // TODO: Add test logic    here
  67:              //
  68:          }
  69:      }
  70:  }
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

After clean up and removal of all the using statements and such that one does not need to start writing test, the class looks like this.

```
   1:  using Microsoft.VisualStudio.TestTools.UnitTesting;
   2:
   3:  namespace PipServices.Tests
   4:  {
   5:      [TestClass]
   6:      public class UnitTest1
   7:      {
   8:          [TestMethod]
   9:          public void TestMethod1()
  10:          {
  11:          }
  12:      }
  13:  }
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

I’d love to know what the mentality was behind all that other stuff being added.

After the cleanup there is 13 lines of code versus 70.  The intention of unit tests is to be simple, straight forward, and effectively explain via code what the functional code does.  So why all the extra deluge of mess?  Also the excessive comments are not needed, the test itself needs to provide the description of the code functionality.  If the test doesn’t do this it isn’t a very good test.  If there is a bunch of documentation describing what the test does it absolutely isn’t that useful of a test.  The likelihood that the test is not done in isolation increases exponentially when there is comments and such, and every time I see them I just shrug at what usually is a useless test.  I don’t quit get that, but would be happy if anyone could add to the reasoning (or know of any good links that might explain).
