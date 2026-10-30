---
title: A TimePiece of C# and JavaScript
date: 2011-08-21 15:34:48 -0700
last_modified_at: 2011-08-21 15:34:48 -0700
permalink: /2011/08/21/a-timepiece-of-c-and-javascript/
slug: a-timepiece-of-c-and-javascript
wp_id: 3581
original_url: https://compositecode.blog/2011/08/21/a-timepiece-of-c-and-javascript/
categories:
- .NET Bits
- How-to
- Javascript
tags:
- .NET
- c#
- javascript
- qunit
- shouldly
- unit test
- unit testing
- unit tests
excerpt: I put together a little project on Github, partially because I’ve been making headway learning the intricacies of JavaScript, and partly because I wanted something that would parse a string that represents a time value. So here’s the TDD I went through. In the process I pulled in QUnit and used that as my testing framework for the JavaScript example. I’d love input on either of these, so feel free to gimme some heat, tell me what I’ve done wrong, and especially how I ought to be doing this. 🙂 …click through to read more…
---

I put together a little project on Github, partially because I’ve been making headway learning the intricacies of JavaScript, and partly because I wanted something that would parse a string that represents a time value. So here’s the TDD I went through. In the process I pulled in QUnit and used that as my testing framework for the JavaScript example. I’d love input on either of these, so feel free to gimme some heat, tell me what I’ve done wrong, and especially how I ought to be doing this.  🙂

The first thing I did was put together the C# Library. I started two projects, one for the tests and one for the actual library.  In the tests project I added a class file and removed the default using statements and replaced them with the following by way of [Nuget](http://nuget.org/):

```csharp
using NUnit.Framework;
using Shouldly;
```

After adding these references I jumped right into setting up the test fixture. Since I know I want to have something to parse the hour for military time also I’ve setup two test variables.

```csharp
[TestFixture]
public class with_static_parsing_of_time
{
    protected string sampleTimeOne = "10:12am";
    protected string sampleTimeTwo = "2:30pm";
```

The first test I then dived into was to test the hour.

```csharp
[Test]
public void should_return_a_time_piece_with_correct_hour()
{
    var timePiece = TimePiece.Parse(sampleTimeOne);
    timePiece.Hour.ShouldBe(10);
}
```

I then fleshed out the object and implemented enough to get this test to pass.

```csharp
namespace TimeSlicer
{
    public class TimePiece
    {
        public TimePiece(string time)
        {
            ParseTime(time);
        }

        private void ParseTime(string time)
        {
            SetHour(time);
        }

        private void SetHour(string time)
        {
            Hour = Convert.ToInt32(time.Split(Convert.ToChar(":"))[0]);
        }

        public int Hour { get; set; }
```

I then continued back and forth writing [tests](https://github.com/Adron/Time-Slice/tree/master/TimeSliceCsharp/TimeSlicer.Tests) and [implemented](https://github.com/Adron/Time-Slice/blob/master/TimeSliceCsharp/TimeSlicer/TimePiece.cs) each. For the complete code check out the [Github Repository](https://github.com/Adron/Time-Slice). This example is really simple. I’d love any thoughts on adding to it or what you might think is a better way to test the object.

For the JavaScript I [downloaded QUnit](https://github.com/jquery/qunit). Again I stepped into the testing, which is a whole different ballgame than in C#.

```javascript
<link rel="stylesheet" href="qunit/qunit.css" type="text/css" media="screen"/>
<script type="text/javascript" src="jquery-1.6.2.js"></script>
<script type="text/javascript" src="qunit/qunit.js"></script>
<script type="text/javascript" src="TimeSlicer/TimePiece.js"></script>
<script type="text/javascript">

var timeValueOne = "1:30am";
var timeValueTwo = "8:15pm";

$(document).ready(function() {

module("Parse hour from value.");

test("Should parse hour from value.", function() {
    TimePiece(timeValueOne);
    equal(TimePiece.Hour(), 1, "The appropriate hour value is returned for AM meridian value.");
});
```

For the full test file with other JavaScript libraries and CSS check out the [code file](https://github.com/Adron/Time-Slice/blob/master/TimeSliceJavaScript/TimePiece.Tests.html) on github.

…and directly into implementation. With the caveat that I’m extremely unfamiliar with actual psuedo/pretend/faux object creation in JavaScript. In this realm I’m still reading up on best ways to do this.

```javascript
TimePiece = function(time) {
    TimePiece.Hour = function () {
        return time.toString().split(":")[0];
    }
    return time;
};
```

I went on from here writing tests and implementing as I did with the C#. The JavaScript was interesting. I’ve also noticed that I get a lot of strings back versus the number values that I’d actually want, thus the addition of the “parseInt” in the final version.

Check out the overall project on Github at: <https://github.com/Adron/Time-Slice>
