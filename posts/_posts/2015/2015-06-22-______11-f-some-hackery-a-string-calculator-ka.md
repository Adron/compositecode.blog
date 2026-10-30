---
title: ______11 |> F# – Some Hackery – A String Calculator Kata
date: 2015-06-22 22:40:30 -0700
last_modified_at: 2015-06-22 22:55:32 -0700
permalink: /2015/06/22/______11-f-some-hackery-a-string-calculator-ka/
slug: ______11-f-some-hackery-a-string-calculator-ka
wp_id: 11117
original_url: https://compositecode.blog/2015/06/22/______11-f-some-hackery-a-string-calculator-ka/
categories:
- .NET Bits
- F#
- How-to
tags:
- .NET
- code kata
- f#
- fsharp
- kata
- string calculator
excerpt: Now for some F# hacking. The first thing I did was actually go through a Code Kata, which I’ll present here. The first step I took was to get a project started. For that I used the ProjectScaffold to build a clean project via bash. First cloned… git clone git@github.com:fsprojects/ProjectScaffold.git sharpKataStringCalc …then I …
image: /wp-content/uploads/2015/06/ah_f_256.png
---

Now for some F# hacking. The first thing I did was actually go through a Code Kata, which I’ll present here.

The first step I took was to get a project started. For that I used the [ProjectScaffold](https://github.com/fsprojects/ProjectScaffold) to build a clean project via bash.

First cloned…

```fsharp
git clone git@github.com:fsprojects/ProjectScaffold.git sharpKataStringCalc
```

…then I navigated into the directory and executed the build.sh script…

```fsharp
cd sharpKataStringCalc/
./build.sh
```

…then I got prompted for some input.

```bash
  #####################################################

# Project Scaffold Init Script
# Please answer a few questions and we will generate
# two files:
#
# build.fsx               This will be your build script
# docs/tools/generate.fsx This script will generate your
#                         documentation
#
# NOTE: Aside from the Project Name, you may leave any
# of these blank, but you will need to change the defaults
# in the generated scripts.
#

  #####################################################

Project Name (used for solution/project files): sharpKataStringCalc
Summary (a short description): A code kata for the string calculator exercise.
Description (longer description used by NuGet): The code kata, kicked off my Roy Osherove, this is my iteration of it (at least my first iteration of it).
Author: Adron Hall
Tags (separated by spaces): fsharp f# code kata stringcalculator
Github User or Organization: adron
Github Project Name (leave blank to use Project Name):
```

Once I hit enter after entering the information I’ve gotten more than a few of these broken builds.

```bash
Time Elapsed 00:00:00.1609190
Running build failed.
Error:
Building /Users/adronhall/Coderz/sharpKataStringCalc/sharpKataStringCalc.sln failed with exitcode 1.

---------------------------------------------------------------------
Build Time Report
---------------------------------------------------------------------
Target         Duration
------         --------
Clean          00:00:00.0019508
AssemblyInfo   00:00:00.0107624
Total:         00:00:00.6460652
Status:        Failure
---------------------------------------------------------------------
  1) Building /Users/adronhall/Coderz/sharpKataStringCalc/sharpKataStringCalc.sln failed with exitcode 1.
  2) : /Users/adronhall/Coderz/sharpKataStringCalc/src/sharpKataStringCalc/sharpKataStringCalc.fsproj(0,0): Target named 'Rebuild' not found in the project.
  3) : /Users/adronhall/Coderz/sharpKataStringCalc/tests/sharpKataStringCalc.Tests/sharpKataStringCalc.Tests.fsproj(0,0): /Users/adronhall/Coderz/sharpKataStringCalc/tests/sharpKataStringCalc.Tests/sharpKataStringCalc.Tests.fsproj: The required attribute "Project" in Import is empty
---------------------------------------------------------------------
```

This problem I was able to solve once, based on what I did in a previous blog entry “[That Non-Windows Scaffolding for OS-X and Linux |> I Broke It! But…](/2015/06/14/fsharp-project-scaffolding/)“. Which seemed odd that I fixed it previously. To help with the build I actually opened it up in Xamarin Studio. Now, one of the problems with doing this, is that it’s only available on Windows & OS-X. I’m however interested in using this stuff on Linux too, but that’s looking a bit more difficult the more I work with the toolchain unfortunately.

After working through the issue I found that on one OS-X box I’d installed Mono via make and F# via make and that messes things up. Do one or the other and you should be ok. So on my other two OS-X boxes (I’ve a personal retina and a work retina) the build worked flawlessly, and when it works flawlessly it looks like this toward the end of the build execution.

```bash
Finished Target: GenerateReferenceDocs
Starting Target: GenerateDocs (==> GenerateReferenceDocs, GenerateReferenceDocs)
Finished Target: GenerateDocs
Starting Target: All (==> GenerateDocs)
Finished Target: All

---------------------------------------------------------------------
Build Time Report
---------------------------------------------------------------------
Target                  Duration
------                  --------
Clean                   00:00:00.0035253
AssemblyInfo            00:00:00.0103142
Build                   00:00:04.9369669
CopyBinaries            00:00:00.0052210
RunTests                00:00:00.6568475
CleanDocs               00:00:00.0025772
GenerateHelp            00:00:08.6989318
GenerateReferenceDocs   00:00:11.7627584
GenerateDocs            00:00:00.0003409
All                     00:00:00.0000324
Total:                  00:00:26.1162623
Status:                 Ok
---------------------------------------------------------------------
```

I’ve gotten this to work on OS-X and Windows just fine using the straight up ProjectScaffold and the ./build.sh. So all is good, I’m going to move forward with writing the kata based on that and loop back around to straighten out the Linux issues.

To run the tests, execute the following script after creating the project scaffold.

```bash
./build.sh RunTests
```

First off, what are the ideas behind the string calculator kata? Well here’s how Roy Osherove lays it out this particular code kata.

**Before you start:**

- Try not to read ahead.
- Do one task at a time. The trick is to learn to work incrementally.
- Make sure you only test for correct inputs. there is no need to test for invalid inputs for this kata.

**String Calculator**

1. Create a simple String calculator with a method int Add(string numbers)
   1. The method can take 0, 1 or 2 numbers, and will return their sum (for an empty string it will return 0) for example “” or “1” or “1 2”
   2. Start with the simplest test case of an empty string and move to 1 and two numbers
   3. Remember to solve things as simply as possible so that you force yourself to write tests you did not think about
   4. Remember to refactor after each passing test
2. Allow the Add method to handle an unknown amount of numbers.
3. Allow the Add method to handle new lines between numbers (instead of an empty space).
   1. the following input is ok: “1\n2 3” (will equal 6)
   2. the following input is NOT ok: “1 \n” (not need to prove it – just clarifying)
4. Support different delimiters
   1. to change a delimiter, the beginning of the string will contain a separate line that looks like this: “//[delimiter]\n[numbers…]” for example “//;\n1;2” should return three where the default delimiter is ‘;’ .
   2. the first line is optional. all existing scenarios should still be supported
5. Calling Add with a negative number will throw an exception “negatives not allowed” – and the negative that was passed.if there are multiple negatives, show all of them in the exception message
6. Numbers bigger than 1000 should be ignored, so adding 2 + 1001 = 2
7. Delimiters can be of any length with the following format: “//[delimiter]\n” for example: “//[\*\*\*]\n1\*\*\*2\*\*\*3” should return 6
8. Allow multiple delimiters like this: “//[delim1][delim2]\n” for example “//[\*][%]\n1\*2%3” should return 6.
9. Make sure you can also handle multiple delimiters with length longer than one char.

Ok, so now that we’re clear on the string calculator, I’m going to dig into knocking out the first item, “Create a simple string calculator with a method int Add (string numbers)”

But first, in TDD fashion let’s write the test and make it fail first. I changed the code in the Tests.fs file in the tests directory and tests project to read as follows.

```fsharp
module sharpKataStringCalc.Tests

open System
open sharpKataStringCalc
open NUnit.Framework

[<TestFixture>]
type CalculatorTests() =
  [<Test>]
  member x.add_empty_string() =
    let calculator = Calculator()
    let result = calculator.Add ""
    Assert.That(result, Is.EqualTo 0)
```

That gets us a failing test, since we don’t even have any implementation yet. So now I’ll add the first part of the implementation code. First I created a Calculator.fs file and deleted the other file that ProjectScaffold put in there in the first place.

```fsharp
namespace sharpKataStringCalc

open System

type Calculator() =
  member x.Add express =
    0
```

Ok, that gives me a passing test for the first phase of all this. Now since I’m a total F# newb still I’ve got to kind of dig around and read documentation while I’m working through this. So I’m taking a couple of hours while Roy’s suggestion is to use 30 minutes to do this kata. But I figured it is a good way to force myself to learn the syntax and start getting into an F# refactoring practice.

The first thing I started to do was write a test where I set the Calculator() again that looked something like this. I didn’t like that so I tried to pull it out of the test.

```fsharp
  [<TestCase("1", Result = 1)>]
  member x.Add_single_number_returns_that_number expression =
    let calculator = Calculator()
    calculator.Add expression
```

I ended up with something like this then.

```fsharp
let calculator = Calculator()

[<TestFixture>]
type CalculatorTests() =
  [<Test>]
  member x.add_empty_string() =
    let result = calculator.Add ""
    Assert.That(result, Is.EqualTo 0)

  [<TestCase("1", Result = 1)>]
  member x.Add_single_number_returns_that_number expression =
    calculator.Add expression
```

After adding that code with that little refactor I ran it, red light fail, so I then moved on to implementation for this test.

```fsharp
type Calculator() =
  member x.Add expression =
    match expression with
    | "" -> 0
    | _ -> 1
```

Everything passed. So now on to the next scenario other subsequent number strings. I add another test and result condition.

```fsharp
  [<TestCase("1", Result = 1)>]
  [<TestCase("2", Result = 2)>]
  member x.Add_single_number_returns_that_number expression =
    calculator.Add expression
```

It runs, gets a red light fail, I then implement with this minor addition.

```fsharp
type Calculator() =
  member x.Add expression =
    match expression with
    | "" -> 0
    | _ -> Int32.Parse expression
```

Before moving on, I’m just going to cover some of the syntax I’ve been using. The | delimits individual matches, individual discriminated union cases, and enumeration values. In this particular case I’m just using it to match the empty string or the
wildcard. Which speaking of, the \_ is a wildcard match or specifies a generic parameter. To learn more about these in detail check out [match expressions](https://msdn.microsoft.com/en-us/library/dd233242.aspx) or [generics](https://msdn.microsoft.com/en-us/library/dd233215.aspx). There are lots of good things in there.

The other syntax is somewhat more self-explanatory so I’m going to leave it as is for the moment. It is, in the end, when executing the tests evident what is going on at least. Alright, back to the kata. Let’s actually add two numbers. For the test I’m just going to add another TestCase with two actual numbers.

```fsharp
  [<TestCase("1", Result = 1)>]
  [<TestCase("2", Result = 2)>]
  [<TestCase("1 2", Result = 3)>]
  member x.Add_single_number_returns_that_number expression =
    calculator.Add expression
```

Fails, so on to implementation. I’m just going to do this the cheap “it works” way and do something dumb.

```fsharp
type Calculator() =
  member x.Add expression =
    match expression with
    | "" -> 0
    | _ when expression.Contains " " -> 3
    | _ -> Int32.Parse expression
```

That’ll give me a passing green light, but I’ll add another bit of attribute to the test and get another failing test.

```fsharp
  [<TestCase("1", Result = 1)>]
  [<TestCase("2", Result = 2)>]
  [<TestCase("1 2", Result = 3)>]
  [<TestCase("2 3", Result = 5)>]
  member x.Add_single_number_returns_that_number expression =
    calculator.Add expression
```

I’ll add the following code to implement and get a passing test.

```fsharp
type Calculator() =
  member x.Add expression =
    match expression with
    | "" -> 0
    | _ when expression.Contains " " ->
        let numbers = expression.Split [| ' ' |]
        (Int32.Parse numbers.[0]) + (Int32.Parse numbers.[1])
    | _ -> Int32.Parse expression
```

Ok. So that part of the match looks for an empty space, and then takes the two numbers opposite sides of that empty space (array item 0 and 1) and then parses them and adds them together. Keep in mind that ‘ ‘ signifies a single character, and not a string, even though for the contains method that executes on a string, passing in a string with ” ” is ok and the appropriate actions are taken by the compiler.

For the tests I’m going to do a refactor and break them apart just a bit and rename them using the “ xyz “ technique of methods. After the refactor the code looked like this. I got this idea from the “[Use F# to write unit tests with readable names](http://fsharpforfunandprofit.com/posts/low-risk-ways-to-use-fsharp-at-work-3/#test-nunit)” tip.

```fsharp
[<TestFixture>]
type CalculatorTests() =
  [<Test>]
  member x."should return zero if no string value is passed in."() =
    let result = calculator.Add ""
    Assert.That(result, Is.EqualTo 0)

  [<TestCase("1", Result = 1)>]
  [<TestCase("2", Result = 2)>]
  member x."take one number and return that number" expression =
    calculator.Add expression

  [<TestCase("1 2", Result = 3)>]
  [<TestCase("2 3", Result = 5)>]
  member x."add single number to single number and return sum" expression =
    calculator.Add expression
```

At this point I’m going to take a break, and wrap this up in a subsequent part of this series. It’s been a fun troubleshooting and getting started string calculator kata. So stay tuned and I’ll be slinging some F# math at ya real soon.

**Reference:**

- [Symbol and Operator References](https://msdn.microsoft.com/en-us/library/dd233228.aspx)
- [Generics](https://msdn.microsoft.com/en-us/library/dd233215.aspx)
- [Match Expressions](https://msdn.microsoft.com/en-us/library/dd233242.aspx)
- [F# Interactive](https://msdn.microsoft.com/en-us/library/dd233175.aspx) – Not specifically referenced in this article, but something good to read to know how the interactive repl works.
- [My Sharp String Calculator Kata repo on Github](https://github.com/Adron/sharpKataStringCalc)
