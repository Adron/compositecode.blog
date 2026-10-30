---
title: My Lousy Example :( …and a Much Better Example :)
date: 2007-08-29 17:25:00 -0700
last_modified_at: 2007-08-29 17:25:00 -0700
permalink: /2007/08/29/my-lousy-example-and-a-much-better-example/
slug: my-lousy-example-and-a-much-better-example
wp_id: 432
original_url: https://compositecode.blog/2007/08/29/my-lousy-example-and-a-much-better-example/
categories:
- Uncategorized Bits
tags: []
excerpt: I posted an example a few days ago regarding ‘ref’ and ‘out’ parameter keywords. My main purpose was to present a “tip o’ the day” via a code example of ref and out parameters similar to some questions I had been posed earlier in the week. One of my stellar coworkers pointed out that the examples …
---

I posted an example a few days ago regarding ‘ref’ and ‘out’ parameter keywords.  My main purpose was to present a “tip o’ the day” via a code example of ref and out parameters similar to some questions I had been posed earlier in the week.  One of my stellar coworkers pointed out that the examples are fine and all, but really don’t point out what really occurs when trying to assign objects versus base value types, and properties of those objects etc.  With that he threw together some great examples that I nabbed from him (with permission of course).  Thanks Shane for the snippets.  ![Smile [:)]](/emoticons/emotion-1.gif)

So check out these examples…

1 using System.Diagnostics;

    2 using System.Reflection;

    3

    4 namespace ConsoleInterface

    5 {

    6     public class TestParam

    7     {

    8         private int \_TestProp;

    9

   10         public int TestProp

   11         {

   12             get { return \_TestProp; }

   13             set { \_TestProp = value; }

   14         }

   15     }

   16

   17     public class TestingRefAndOutParameters

   18     {

   19         public void CallingMethodChangeProp()

   20         {

   21             TestParam testParam = new TestParam();

   22

   23             testParam.TestProp = 2;

   24             Debug.WriteLine(MethodInfo.GetCurrentMethod().Name + ” Start testParam.TestProp=” + testParam.TestProp);

   25

   26             TestMethod(testParam);

   27             Debug.WriteLine(MethodInfo.GetCurrentMethod().Name + ” End testParam.TestProp=” + testParam.TestProp);

   28         }

   29

   30         public void TestMethod(TestParam testParam)

   31         {

   32             testParam.TestProp = 4;

   33         }

   34

   35         //\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

   36

   37         public void CallingMethodChangePropChangeObj()

   38         {

   39             TestParam testParam = new TestParam();

   40

   41             testParam.TestProp = 2;

   42             Debug.WriteLine(MethodInfo.GetCurrentMethod().Name + ” Start testParam.TestProp=” + testParam.TestProp);

   43

   44             TestMethodSetObj(testParam);

   45             Debug.WriteLine(MethodInfo.GetCurrentMethod().Name + ” End testParam.TestProp=” + testParam.TestProp);

   46         }

   47

   48         public void TestMethodSetObj(TestParam testParam)

   49         {

   50             testParam.TestProp = 4;

   51

   52             TestParam testParam2 = new TestParam();

   53

   54             testParam2.TestProp = 3;

   55             testParam = testParam2;

   56         }

   57

   58         //\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

   59

   60         public void CallingMethodChangePropChangeObjByRef()

   61         {

   62             TestParam testParam = new TestParam();

   63

   64             testParam.TestProp = 2;

   65             Debug.WriteLine(MethodInfo.GetCurrentMethod().Name + ” Start testParam.TestProp=” + testParam.TestProp);

   66

   67             TestMethodS
etObjByRef(ref testParam);

   68             Debug.WriteLine(MethodInfo.GetCurrentMethod().Name + ” End testParam.TestProp=” + testParam.TestProp);

   69         }

   70

   71

   72         public void TestMethodSetObjByRef(ref TestParam testParam)

   73

   74         {

   75             testParam.TestProp = 4;

   76

   77             TestParam testParam2 = new TestParam();

   78             testParam2.TestProp = 3;

   79             testParam = testParam2;

   80         }

   81

   82         //\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

   83

   84         public void CallingMethodChangePropChangeObjByOut()

   85         {

   86             TestParam testParam = new TestParam();

   87

   88             testParam.TestProp = 2;

   89             Debug.WriteLine(MethodInfo.GetCurrentMethod().Name + ” Start testParam.TestProp=” + testParam.TestProp);

   90

   91             TestMethodSetObjOut(out testParam);

   92             Debug.WriteLine(MethodInfo.GetCurrentMethod().Name + ” End testParam.TestProp=” + testParam.TestProp);

   93         }

   94

   95         public void TestMethodSetObjOut(out TestParam testParam)

   96         {

   97             testParam = new TestParam();

   98             testParam.TestProp = 4;

   99

  100             TestParam testParam2 = new TestParam();

  101             testParam2.TestProp = 3;

  102

  103             testParam = testParam2;

  104         }

  105     }

  106 }

As you work through each of these methods, realize what is going on with the object, value type, or other parameter manipulations as the method executes.  You’ll notice that even though something is set to another value, outside of the method it is not particularly going to have the value changed.  Take the following method for example:

   48         public void TestMethodSetObj(TestParam testParam)

   49         {

   50             testParam.TestProp = 4;

   51

   52             TestParam testParam2 = new TestParam();

   53

   54             testParam2.TestProp = 3;

   55             testParam = testParam2;

   56         }

In the code, when reading it directly, it would seem that based on the second assignment of testParam = testParam2, that the TestProp property would be assigned the value of 3.  But because of the way parameters are passed in C# one actually ends up with 4 instead of 3.  One must know the differences between value and reference type passing, for more information check out this [great write up](http://www.yoda.arachsys.com/csharp/parameters.html) or check out the [MSDN](http://msdn2.microsoft.com/en-us/default.aspx) article on “[Passing Parameters](http://msdn2.microsoft.com/en-us/library/0f66670z%28vs.71%29.aspx)” to really dig into what is going on.  Another [great write up](http://www.yoda.arachsys.com/csharp/memory.html) on what is getting put where in memory.

I hope these examples worked to display more effectively what is functionally happening with ‘ref’, ‘out’ and general parameter passing in C#.
