---
title: 'Code Katas: Kicking off With a Little JavaScript'
date: 2011-09-27 08:27:04 -0700
last_modified_at: 2011-09-27 08:27:04 -0700
permalink: /2011/09/27/code-katas-kicking-off-with-a-little-javascript/
slug: code-katas-kicking-off-with-a-little-javascript
wp_id: 3922
original_url: https://compositecode.blog/2011/09/27/code-katas-kicking-off-with-a-little-javascript/
categories:
- Code Katas
- How-to
- Javascript
tags:
- arabic numeral
- javascript
- kata
- roman numeral
excerpt: A few days ago, my friend Aeden Jameson asks, “you want to work through a code kata this weekend?” I thought, well yeah, that’d be cool. So we met at Cafe Fiore and hacked out the beginning of a Kata based on the Roman to Arabic and Arabic to Roman Numerals. It was fun, which led me to working up an actual blog entry related to our kata session. This however, is just me working through a similar aspect of the numeral conversions with JavaScript. Enjoy. First things first, I’m using QUnit which is available on Github with documentation on the jQuery Site . So if you’re going to work through these, go get that first. Or use another unit testing framework. I also am using Webstorm , which is a pretty sweet IDE for editing HTML, CSS, and JavaScript available from Jetbrains . You can even do scary stuff like edit and write PHP! Oh yeah that’s right! It IS absolutely worth the money. 😀 With that out of the way, here’s what I started with. First I created a QUnit and Scripts Directory. In QUnit I placed the qunit.css and qunit.js files and in the Scripts Directory I added the jquery-1.5.1.min.js file. The later file isn’t that important at this point, but I’ve added as I intend to use it at some point later on. …click through to read and see more code.
---

> **BEWARE, this is a crazy long post. So before you jump in for a read, just know that it isn’t a two minute read. 😉**

A few days ago, my friend [Aeden Jameson](http://www.facebook.com/aeden.jameson) ([@daliful](http://twitter.com/#!/daliful)) asks, “you want to work through a code kata this weekend?” I thought, well yeah, that’d be cool. So we met at Cafe Fiore and hacked out the beginning of a Kata based on the Roman to Arabic and Arabic to Roman Numerals. It was fun, which led me to working up an actual blog entry related to our kata session. This however, is just me working through a similar aspect of the numeral conversions with JavaScript. Enjoy.

First things first, I’m using [QUnit](https://github.com/jquery/qunit) which is available on [Github](http://www.github.com) with [documentation on the jQuery Site](http://docs.jquery.com/Qunit). So if you’re going to work through these, go get that first. Or use another unit testing framework. I also am using [Webstorm](http://www.jetbrains.com/webstorm/), which is a pretty sweet IDE for editing HTML, CSS, and JavaScript available from [Jetbrains](http://www.jetbrains.com/). You can even do scary stuff like edit and write PHP! Oh yeah that’s right! It ***IS*** absolutely worth the money. 😀

With that out of the way, here’s what I started with. First I created a QUnit and Scripts Directory. In QUnit I placed the qunit.css and qunit.js files and in the Scripts Directory I added the jquery-1.5.1.min.js file. The later file isn’t that important at this point, but I’ve added it since I intend to use it at some point later on.

There are a few main ideas behind doing a Code Kata:

- Keep the implementation code to the absolute minimum needed to pass the test.
- Use a steady TDD/BDD Style testing first approach to think through each step.

```html
<!DOCTYPE HTML>
<html>
<head>
    <title>TimePiece Object Unit Tests</title>
    <link rel="stylesheet"
          href="../QUnit/qunit.css"
          type="text/css"
          media="screen"/>
    <script type="text/javascript"
            src="../Scripts/jquery-1.5.1.min.js"></script>
    <script type="text/javascript"
            src="../QUnit/qunit.js"></script>
    <script type="text/javascript">
      // All the code bits go here!
    </script>
<body>
    <p>Roman to Arabic, Arabic to Roman...</p>
    <span>QUnit Test Results...</span>

    <h1 id="qunit-header">Numeral Conversions</h1>

    <h2 id="qunit-banner"></h2>

    <div id="qunit-testrunner-toolbar"></div>
    <h2 id="qunit-userAgent"></h2>
    <ol id="qunit-tests"></ol>
    <div id="qunit-fixture">hidden text</div>
</body>
</html>
```

Which gets me to the point that I have a rendering of an empty test results page, as shown below.

[![QUnit Test Results Page](/images/adronhall.smugmug.com/Software/Software-Development/Code-Katas/i-fdhHrH2/0/S/Screen-shot-2011-09-23-at-S.png "QUnit Test Results Page")](http://adronhall.smugmug.com/Software/Software-Development/Code-Katas/19173277_Xg84w3#1494179217_fdhHrH2-O-LB)

*QUnit Test Results Page*

The next step was to get started. So jumping right in I got some code put in place for a failing test.

```javascript
module("When converting an integer into a roman numeral");

test("should receive I when passing a 1", function() {
    equal(NumeralConverter.get_arabic_numeral("I"), 1, "I was returned when 1 was passed as a parameter.");
});
```

Red light received, code committed, implementing for green.

```javascript
var NumeralConverter = {
    get_arabic_numeral : function ( romanNumeral ){
        return 1;
    }
}
```

Code committed. Sticking with the idea to implement the bare minimum needed, one can see pretty obviously that this isn’t much of a converter. So going forward I added the next test, for our second numeral.

```javascript
test("should receive 2 when passing a 'II'", function() {
    equal(NumeralConverter.get_arabic_numeral("II"), 2, "2 was returned when 'II' was passed as a parameter.");
});
```

Again, nothing really specific here, nor is any defined logic really visible in what the method is needing to do. So after the commit I implemented the logic to pass this and committed this also.

```javascript
var NumeralConverter = {
    get_arabic_numeral : function ( romanNumeral ){
        var result = romanNumeral == "I" ? 1 : 2;
        return result;
    }
}
```

That gets those bits passing. With a nice little JavaScript Ternary Operator. Still not hitting on the big picture of converting between the roman to arabic numerals yet, but we’re getting a little closer. Stepping up to the next test, pretty much more of the same.

```javascript
test("should receive 3 when passing a 'III'", function() {
    equal(NumeralConverter.get_arabic_numeral("III"), 3, "3 was returned when 'III' was passed as a parameter.");
});
```

With the failing test committed, I did what seems like the easiest solution, yet so much like it is cheating. But hey! It works! That’s what is is about and one ever knows what kind of alternate solutions will crop up! Think small steps and things will lay out for you in interesting ways. Discipline!

```javascript
var NumeralConverter = {
    get_arabic_numeral : function ( romanNumeral ){
        return romanNumeral.length;
    }
}
```

So now the first tricky one comes up, the IV. The test continues to repeat. I pondered a rowset style test, but wasn’t really happy with any of the prospective solutions I saw with a quick search on the net for qunit. So on with tests as I’ve been going.

```javascript
test("should receive 4 when passing a 'IV'", function() {
    equal(NumeralConverter.get_arabic_numeral("IV"), 4, "4 was returned when 'IV' was passed as a parameter.");
});
```

Red light received, code committed. The implementation for this, still feels like cheating. Simplest code to get the test passing possible.

```javascript
var NumeralConverter = {
    get_arabic_numeral : function ( romanNumeral ){
        if(romanNumeral == "IV"){
            return 4;
        }
        return romanNumeral.length;
    }
}
```

Green light, code committed. Again, straight into a test.

```javascript
test("should receive 5 when passing a 'V'", function() {
    equal(NumeralConverter.get_arabic_numeral("V"), 5, "5 was returned when 'V' was passed as a parameter.");
});
```

Red light, code committed.

```javascript
var NumeralConverter = {
    get_arabic_numeral : function ( romanNumeral ){
        if(romanNumeral == "IV"){
            return 4;
        }
        else if(romanNumeral == "V"){
            return 5;
        }
        return romanNumeral.length;
    }
}
```

Green light. Code committed. It seems like something is starting to brew up out of the method.

```javascript
test("should receive 6 when passing a 'VI'", function() {
    equal(NumeralConverter.get_arabic_numeral("VI"), 6, "6 was returned when 'VI' was passed as a parameter.");
});
```

Red light. Code committed.

```javascript
var NumeralConverter = {
    get_arabic_numeral : function ( romanNumeral ){
        if(romanNumeral == "IV"){
            return 4;
        }
        else if(romanNumeral == "V"){
            return 5;
        }
        else if(romanNumeral == "VI"){
            return 6;
        }
        return romanNumeral.length;
    }
}
```

Green light, code committed. I implemented the next bits, but at testing that VIII returns 8 I began a refactoring. If I were to split the one Roman Numerals ‘I’ off I could then just count their length and add them to the five Roman Numeral V. I didn’t really think about how that would work past 8, but it seemed like a valid refactoring. After that, these two additional tests were completed and passing.

```javascript
test("should receive 7 when passing a 'VII'", function() {
    equal(NumeralConverter.get_arabic_numeral("VII"), 7, "7 was returned when 'VII' was passed as a parameter.");
});

test("should receive 8 when passing a 'VIII'", function() {
    equal(NumeralConverter.get_arabic_numeral("VIII"), 8, "8 was returned when 'VIII' was passed as a parameter.");
});
```

The actual method implementation looked like this now.

```javascript
var NumeralConverter = {
    get_arabic_numeral : function ( romanNumeral ){
        var ones = 0;
        var five = 0;
        var result = 0;
        var vCount = romanNumeral.split(/V/g).length -1;
        var iCount = romanNumeral.split(/I/g).length -- 1;

        if(romanNumeral == "IV"){
            return 4;
        }
        else if(vCount > 0){
            five = vCount * 5;
        }

        ones = iCount;
        result = five + ones;

        return result;
    }
}
```

Now we’re actually getting some logic in there. If one breaks the rules, there is even a bit of foreshadowing to where the logic and looping will eventually end up. But I’m going to keep going with the KISS idea and doing a minimal implement for each failing test! Moving right along…

```javascript
test("should receive 9 when passing a 'IX'", function() {
    equal(NumeralConverter.get_arabic_numeral("IX"), 9, "9 was returned when 'IX' was passed as a parameter.");
});
```

Ok, ok, now at this point I’m thinking, “oh jeez, this list of tests looks like a mess. These need refactored now.” I did look for a rowtest earlier, and that didn’t exist really. So something else ought to work though, but the question is what? So I looked around and just took a few minutes to think. Take a look at the tests at this point all listed together.

```javascript
module("When converting a roman numeral into an arabic numeral");

test("should receive 1 when passing a 'I'", function() {
    equal(NumeralConverter.get_arabic_numeral("I"), 1, "1 was returned when 'I' was passed as a parameter.");
});

test("should receive 2 when passing a 'II'", function() {
    equal(NumeralConverter.get_arabic_numeral("II"), 2, "2 was returned when 'II' was passed as a parameter.");
});

test("should receive 3 when passing a 'III'", function() {
    equal(NumeralConverter.get_arabic_numeral("III"), 3, "3 was returned when 'III' was passed as a parameter.");
});

test("should receive 4 when passing a 'IV'", function() {
    equal(NumeralConverter.get_arabic_numeral("IV"), 4, "4 was returned when 'IV' was passed as a parameter.");
});

test("should receive 5 when passing a 'V'", function() {
    equal(NumeralConverter.get_arabic_numeral("V"), 5, "5 was returned when 'V' was passed as a parameter.");
});

test("should receive 6 when passing a 'VI'", function() {
    equal(NumeralConverter.get_arabic_numeral("VI"), 6, "6 was returned when 'VI' was passed as a parameter.");
});

test("should receive 7 when passing a 'VII'", function() {
    equal(NumeralConverter.get_arabic_numeral("VII"), 7, "7 was returned when 'VII' was passed as a parameter.");
});

test("should receive 8 when passing a 'VIII'", function() {
    equal(NumeralConverter.get_arabic_numeral("VIII"), 8, "8 was returned when 'VIII' was passed as a parameter.");
});

test("should receive 9 when passing a 'IX'", function() {
    equal(NumeralConverter.get_arabic_numeral("IX"), 9, "9 was returned when 'IX' was passed as a parameter.");
});
```

That’s a lot of tests. Well, I looked through the documentation a little bit, and realized that I could just do this. Is it more readable? It almost comes off as rowset tests in junit/nunit.

```javascript
module("When converting a roman numeral into an arabic numeral");

test("should receive arabic numeral", function() {
    equal(NumeralConverter.get_arabic_numeral("I"), 1, "1 when 'I' was passed as a parameter.");
    equal(NumeralConverter.get_arabic_numeral("II"), 2, "2 when 'II' was passed as a parameter.");
    equal(NumeralConverter.get_arabic_numeral("III"), 3, "3 when 'III' was passed as a parameter.");
    equal(NumeralConverter.get_arabic_numeral("IV"), 4, "4 when 'IV' was passed as a parameter.");
    equal(NumeralConverter.get_arabic_numeral("V"), 5, "5 when 'V' was passed as a parameter.");
    equal(NumeralConverter.get_arabic_numeral("VI"), 6, "6 when 'VI' was passed as a parameter.");
    equal(NumeralConverter.get_arabic_numeral("VII"), 7, "7 when 'VII' was passed as a parameter.");
    equal(NumeralConverter.get_arabic_numeral("VIII"), 8, "8 when 'VIII' was passed as a parameter.");
    equal(NumeralConverter.get_arabic_numeral("IX"), 9, "9 when 'IX' was passed as a parameter.");
});
```

Either way, I’m sticking to it for now. I added the test for X.

```javascript
equal(NumeralConverter.get_arabic_numeral("X"), 10, "10 when 'X' is passed in.");
```

Then implemented it following a similar pattern that I had already started.

```javascript
get_arabic_numeral : function (romanNumeral) {
    var ones = 0, fives = 0, tens = 0;
    var result = 0;
    var vCount = romanNumeral.split(/V/g).length -- 1;
    var iCount = romanNumeral.split(/I/g).length -- 1;
    var xCount = romanNumeral.split(/X/g).length -- 1;

    if (romanNumeral == "IV") {
        return 4;
    }
    else if (romanNumeral == "IX") {
        return 9;
    }
    else if (vCount > 0) {
        fives = vCount * 5;
    }
    else if (xCount > 0) {
        tens = xCount * 10;
    }

    ones = iCount;
    result = fives + ones + tens;

    return result;
}
```

That was easy enough. Also note, when the pattern that is now evident among the logic, the next two tests automatically pass. Now some real progress has been made.

```javascript
equal(NumeralConverter.get_arabic_numeral("XI"), 11, "11 when 'XI' is passed in.");
equal(NumeralConverter.get_arabic_numeral("XII"), 12, "12 when 'XII' is passed in.");
equal(NumeralConverter.get_arabic_numeral("XIII"), 13, "13 when 'XIII' is passed in.");
```

Now however, things get a bit tricky. Add a test for ‘VX’.

```javascript
equal(NumeralConverter.get_arabic_numeral("VX"), 14, "14 when 'VX' is passed in.");
```

So adding another simple exception, pretty much takes care of that.

```javascript
get_arabic_numeral : function (romanNumeral) {
    var ones = 0, fives = 0, tens = 0;
    var result = 0;
    var vCount = romanNumeral.split(/V/g).length -- 1;
    var iCount = romanNumeral.split(/I/g).length -- 1;
    var xCount = romanNumeral.split(/X/g).length -- 1;

    if (romanNumeral == "IV") {
        return 4;
    }
    else if (romanNumeral == "IX") {
        return 9;
    }
    else if(romanNumeral == "VX") {
        return 14;
    }
    else if (vCount > 0) {
        fives = vCount * 5;
    }
    else if (xCount > 0) {
        tens = xCount * 10;
    }

    ones = iCount;
    result = fives + ones + tens;

    return result;
}
```

Now that trickiness comes up when adding the test for ‘XV’.

```javascript
equal(NumeralConverter.get_arabic_numeral("XV"), 15, "15 when 'XV' is passed in.");
```

Red light, code commit. Now to implement. An actual reduction of code gets us back in action here.

```javascript
get_arabic_numeral : function (romanNumeral) {
    var ones = 0, fives = 0, tens = 0;
    var result = 0;
    var vCount = romanNumeral.split(/V/g).length -- 1;
    var iCount = romanNumeral.split(/I/g).length -- 1;
    var xCount = romanNumeral.split(/X/g).length -- 1;

    if (romanNumeral == "IV") {
        return 4;
    }
    else if (romanNumeral == "IX") {
        return 9;
    }
    else if (romanNumeral == "VX") {
        return 14;
    }
    else if (vCount > 0 || xCount > 0) {
        fives = vCount * 5;
        tens = xCount * 10;
    }

    ones = iCount;
    result = fives + ones + tens;

    return result;
}
```

Green light. Code Commit. Now for the next three tests, they’ll all pass. The next test that we run into that gives us a failing test is for 19, or ‘XIX’. For the tests below I went ahead and added XVI, XVII, and XVIII.

```javascript
equal(NumeralConverter.get_arabic_numeral("XVI"), 16, "16 when 'XVI' is passed in.");
equal(NumeralConverter.get_arabic_numeral("XVII"), 17, "17 when 'XVII' is passed in.");
equal(NumeralConverter.get_arabic_numeral("XVIII"), 18, "18 when 'XVIII' is passed in.");
equal(NumeralConverter.get_arabic_numeral("XVIII"), 19, "19 when 'XIX' is passed in.");
```

Red light, code commit.

```javascript
get_arabic_numeral : function (romanNumeral) {
    var ones = 0, fives = 0, tens = 0;
    var result = 0;
    var vCount = romanNumeral.split(/V/g).length -- 1;
    var iCount = romanNumeral.split(/I/g).length -- 1;
    var xCount = romanNumeral.split(/X/g).length -- 1;

    if (romanNumeral == "IV") {
        return 4;
    }
    else if (romanNumeral == "IX") {
        return 9;
    }
    else if (romanNumeral == "VX") {
        return 14;
    }
    else if (romanNumeral == "XIX") {
        return 19;
    }
    else if (vCount > 0 || xCount > 0) {
        fives = vCount * 5;
        tens = xCount * 10;
    }

    ones = iCount;
    result = fives + ones + tens;

    return result;
}
```

Green light, code commit. Add the test for ‘XX’ and you’ll find that this test automatically passes also. There’s still soemthing to be done about the odd else if assigned values above! But onward. After the test for ‘XX’, I’ll jump right in and see how far I can get. Not until 24 do I run into an issue.

```javascript
equal(NumeralConverter.get_arabic_numeral("XXI"), 21, "21 when 'XXI' is passed in.");
equal(NumeralConverter.get_arabic_numeral("XXII"), 22, "22 when 'XXII' is passed in.");
equal(NumeralConverter.get_arabic_numeral("XXIII"), 23, "23 when 'XXIII' is passed in.");
equal(NumeralConverter.get_arabic_numeral("XXIV"), 24, "24 when 'XXIV' is passed in.");
```

It seems like there is some type of logic happening, some repeatable logic. So I started giving it a good look over. I will admit, I went ahead and worked through several more of the tests and implementation details just to force more of the if else statements to be apparent. I added tests for 25-30 and implemented passing tests with the following code.

```javascript
get_arabic_numeral : function (romanNumeral) {
    var ones = 0, fives = 0, tens = 0;
    var result = 0;
    var vCount = romanNumeral.split(/V/g).length -- 1;
    var iCount = romanNumeral.split(/I/g).length -- 1;
    var xCount = romanNumeral.split(/X/g).length -- 1;

    if (romanNumeral == "IV") {
        return 4;
    }
    else if (romanNumeral == "IX") {
        return 9;
    }
    else if (romanNumeral == "XIV") {
        return 14;
    }
    else if (romanNumeral == "XIX") {
        return 19;
    }
    else if (romanNumeral == "XXIV") {
        return 24;
    }
    else if (romanNumeral == "XXIX") {
        return 29;
    }
    else if (vCount > 0 || xCount > 0) {
        fives = vCount * 5;
        tens = xCount * 10;
    }

    ones = iCount;
    result = fives + ones + tens;

    return result;
}
```

I started to stop and do research, look up some other functions that already do this. I wanted to bad, but I stuck with the original idea behind the Kata. Just implement the bare minimum code and go through the red, green, refactor approach. In the end I stuck with that approach and came up with this mess.

```javascript
get_arabic_numeral : function (romanNumeral) {
    var ones = 0, fives = 0, tens = 0;
    var result = 0;
    var vCount = romanNumeral.split(/V/g).length -- 1;
    var iCount = romanNumeral.split(/I/g).length -- 1;
    var xCount = romanNumeral.split(/X/g).length -- 1;

    if (vCount > 0 || xCount > 0) {
        fives = vCount * 5;
        tens = xCount * 10;
    }

    if (romanNumeral.length > 1) {
        if (romanNumeral == "IV" || romanNumeral == "IX") {
            var workingNumber = fives + tens -- iCount;
            return workingNumber;
        }
        else if (romanNumeral == "XIV") {
            return 14;
        }
        else if (romanNumeral == "XIX") {
            return 19;
        }
        else if (romanNumeral == "XXIV") {
            return 24;
        }
        else if (romanNumeral == "XXIX") {
            return 29;
        }
    }

    ones = iCount;
    result = fives + ones + tens;

    return result;
}
```

From here, I had to get the IV or IX off of the larger roman numerals. I needed some string capabilties, so I pulled in some libraries for string manipulation, namely the [Underscore.js + Underscore.string libraries](/2011/09/24/underscore-js-and-underscore-js-m-lib-series-issue-001/). After that refactor, I knocked out all the code (yup, deleting code!) around the extra else if statements.

```javascript
get_arabic_numeral : function (romanNumeral) {
    var ones = 0, fives = 0, tens = 0;
    var result = 0;
    var vCount = romanNumeral.split(/V/g).length -- 1;
    var iCount = romanNumeral.split(/I/g).length -- 1;
    var xCount = romanNumeral.split(/X/g).length -- 1;

    if (vCount > 0 || xCount > 0) {
        fives = vCount * 5;
        tens = xCount * 10;
    }

    if (romanNumeral.length > 1) {
        if (_(romanNumeral).endsWith("IV") || _(romanNumeral).endsWith("IX")) {
            var workingNumber = fives + tens -- iCount;
            return workingNumber;
        }
    }

    ones = iCount;
    result = fives + ones + tens;

    return result;
}
```

At this point I was fairly confident that I had a huge number of effective conversions. So I decided to skip a few tests and head into the other numbers and other exception criteria. I did a commit for the refactor that I just finished and then jumped into a test for L, the Roman Numeral which represents 50, and the other numbers M, D, and C. I did write these individually, and then added the code, but I’ve added them altogether here to conserve space in this already long blog entry. 😉

```javascript
equal(NumeralConverter.get_arabic_numeral("L"), 50, "50 when 'L' is passed in.");
equal(NumeralConverter.get_arabic_numeral("M"), 1000, "1000 when 'M' is passed in.");
equal(NumeralConverter.get_arabic_numeral("D"), 500, "500 when 'D' is passed in.");
equal(NumeralConverter.get_arabic_numeral("C"), 100, "100 when 'C' is passed in.");
```

Red light, committed code. Implement.

```javascript
get_arabic_numeral : function (romanNumeral) {
    var ones = 0, fives = 0, tens = 0, fifties = 0;
    var hundreds = 0, fiveHundreds = 0, thousands = 0;
    var result = 0;
    var vCount = romanNumeral.split(/V/g).length -- 1;
    var iCount = romanNumeral.split(/I/g).length -- 1;
    var xCount = romanNumeral.split(/X/g).length -- 1;
    var lCount = romanNumeral.split(/L/g).length -- 1;
    var cCount = romanNumeral.split(/C/g).length -- 1;
    var dCount = romanNumeral.split(/D/g).length -- 1;
    var mCount = romanNumeral.split(/M/g).length -- 1;

    if (vCount > 0 || xCount > 0 || lCount > 0 || cCount > 0 || dCount > 0 || mCount > 0) {
        fives = vCount * 5;
        tens = xCount * 10;
        fifties = lCount * 50;
        hundreds = cCount * 100;
        fiveHundreds = dCount * 500;
        thousands = mCount * 1000;
    }

    if (romanNumeral.length > 1) {
        if (_(romanNumeral).endsWith("IV") || _(romanNumeral).endsWith("IX")) {
            var workingNumber = fives + tens -- iCount;
            return workingNumber;
        }
    }

    ones = iCount;
    result = ones + fives + tens + fifties + hundreds + fiveHundreds + thousands;

    return result;
}
```

At this point, one can see some of the changes from refactoring, and the practice of TDD for this specific kata. It is a great way to become more efficient at thinking in a TDD way, or a touch of how one might do BDD. I hope to have more blog entries about BDD vs. TDD, how to do this, and how to get better at it. Of course, I can only write about what I know or am learning myself, and with this particular occupation I’m always learning. 😉

Hopefully this was useful, as material and as an idea. I’m not 100% finished with this kata, and I will post the code in its completed form once I’m done. For now, enjoy, and practice that TDD/BDD awesomeness!
