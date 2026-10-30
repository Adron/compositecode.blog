---
title: 'Converting Numbers into Roman Numerals with C#: A Classical Coding Exercise'
date: 2024-06-10 01:59:00 -0700
last_modified_at: 2024-06-10 13:12:49 -0700
permalink: /2024/06/10/converting-numbers-into-roman-numerals-with-c-a-classical-coding-exercise/
slug: converting-numbers-into-roman-numerals-with-c-a-classical-coding-exercise
wp_id: 68366
original_url: https://compositecode.blog/2024/06/10/converting-numbers-into-roman-numerals-with-c-a-classical-coding-exercise/
categories:
- .NET Bits
- c#
- Code Katas
tags:
- ai
- ai tooling
- c#
- code exercises
- coding
- copilot
- csharp
- dotnet
- kata
excerpt: This content outlines the process of converting modern numbers into ancient Roman numerals in C#. It describes the rules for conversion, provides a start-to-finish coding solution with testing, and explores the iterative process of refining the code for efficiency and readability. The final solution leverages recursion and LINQ, illustrating the elegance and power of C# programming.
image: /wp-content/uploads/2024/05/csharp-coders.png
---

Programming Problems & Solutions : “Conquering Roman Numerals in C#: An Exercise in Classical Coding”. The introduction to this series is [here](/2024/05/29/coding-with-ai-a-comparative-series/) and includes all links to every post in the series. If you’d like to watch the video (see just below this), or the AI code up (it’s at the bottom of the post) they’re available! But if you just want to work through the problem keep reading, I cover most of what is in the video plus a slightly different path down below.

<iframe allowfullscreen="true" class="youtube-player" height="486" loading="lazy" sandbox="allow-scripts allow-same-origin allow-popups allow-presentation allow-popups-to-escape-sandbox" src="https://www.youtube.com/embed/rAeUQBd6B24?version=3&amp;rel=1&amp;showsearch=0&amp;showinfo=1&amp;iv_load_policy=1&amp;fs=1&amp;hl=en-US&amp;autohide=2&amp;wmode=transparent" style="border:0;" width="863"></iframe>

*The continuation with CoPilot AI Tooling is at the end of the post.*

## The Challenge: Translating Numbers into a Language of Antiquity

Today, I’ll dive into a fascinating challenge: converting modern numbers into their ancient Roman numeral counterparts. The task is straightforward but intricate, involving a programming challenge that takes any positive integer from 1 to 3999 and converts it into the corresponding Roman numeral.

To convert regular decimal numbers into Roman numerals, one must follow a set of rules based on the values and combinations of specific Roman numeral characters. Here’s a brief summary of the conversion process:

### Roman Numerals and Their Values

- **I**: 1
- **V**: 5
- **X**: 10
- **L**: 50
- **C**: 100
- **D**: 500
- **M**: 1000

### Basic Rules

1. **Repetition**: Roman numerals are generally written from largest to smallest from left to right. For example, the number three is written as “III”.
2. **Subtraction**: There are specific instances where subtraction is used. For example:
   - **4** is written as **IV** (5 – 1)
   - **9** is written as **IX** (10 – 1)
   - **40** is written as **XL** (50 – 10)
   - **90** is written as **XC** (100 – 10)
   - **400** is written as **CD** (500 – 100)
   - **900** is written as **CM** (1000 – 100)

### Conversion Algorithm

1. Start with the largest numeral and work downwards.
2. Subtract the value of the numeral from the number and append the numeral to the result string.
3. Repeat until the number is reduced to zero.

### Example Conversion

For converting the number 1954:

- 1954 is 1000 (M) + 900 (CM) + 50 (L) + 4 (IV)
- The result is **MCMLIV**

## Tests First

I’ll start this exercise writing up some tests first just to think through what needs to be done. This suite of tests checks a variety of cases, from simple numbers like `1` or `2` to more complex ones like `1990` and `2008`:

```
using System;
using NUnit.Framework;

[TestFixture]
public class RomanConvertTests
{
	[TestCase(1, "I")]
	[TestCase(2, "II")]
	[TestCase(4, "IV")]
	[TestCase(500, "D")]
	[TestCase(1000, "M")]
	[TestCase(1954, "MCMLIV")]
	[TestCase(1990, "MCMXC")]
	[TestCase(2008, "MMVIII")]
	[TestCase(2014, "MMXIV")]
	public void Test(int value, string expected)
	{
		Assert.AreEqual(expected, RomanConvert.Solution(value));
	}
}
```

This exercise is a bridge to a time when these numerals were the cutting edge of numerical representation. By solving this problem, we not only enhance our coding skills but also pay homage to the ingenuity of Romans, and gives you a chance to meet your daily requirement of thinking about the Roman Civilization (see [meme](https://knowyourmeme.com/memes/how-often-do-you-think-about-the-roman-empire))!

## Setting the Scene with C#

To embark on this journey, I’ll start with a simple C# class setup. I’m tasked with filling in the `BuildRomanNumeral` function in the `RomanConvert` class, which is scaffolded as follows:

```
using System;

public class RomanConvert
{
	public static string BuildRomanNumeral(int n)
	{
		throw new NotImplementedException();
	}
}
```

My goal? Implement the `BuildRomanNumeral` function so that it accurately transforms an integer into its Roman numeral string.

## Crafting the Solution

My first draft solution involves a mapping of integers to their Roman numeral symbols. Here’s a neat trick: by using arrays for the numeral values and their corresponding symbols, and then iterating from the largest to the smallest, we can efficiently construct the numeral string:

```
using System;
using System.Text;

public class RomanConvert
{
	public static string BuildRomanNumeral(int n)
	{
        StringBuilder result = new StringBuilder();

        int[] values = {1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1};
        string[] symbols = {"M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"};

        for (int i = 0; i < values.Length; i++)
        {
            while (n >= values[i])
            {
                result.Append(symbols[i]);
                n -= values[i];
            }
        }

        return result.ToString();
	}
}
```

### Breakdown of the Method

1. **Array Initialization**: We start by defining two arrays—one for the Roman numeral values and another for their corresponding symbols. This setup ensures that we always try to subtract the largest possible values first, which is key to correctly forming Roman numerals.
2. **StringBuilder Efficiency**: A `StringBuilder` is utilized to build the numeral string efficiently. This is crucial as it avoids the overhead associated with frequent string concatenation.
3. **Iterative Construction**: The core of the function iterates over the values, subtracting from `n` and appending the appropriate Roman symbol until `n` is whittled down to zero.

## Refactoring

As I usually do before refactoring, when I’ve got tests, I like to make sure more edge cases – or just in general – tests cover more of the possible results. For this I’ve added the following to the tests.

```
[TestCase(3, "III")]
[TestCase(9, "IX")]
[TestCase(14, "XIV")]
[TestCase(44, "XLIV")]
[TestCase(99, "XCIX")]
[TestCase(399, "CCCXCIX")]
[TestCase(444, "CDXLIV")]
[TestCase(944, "CMXLIV")]
[TestCase(999, "CMXCIX")]
[TestCase(1066, "MLXVI")]
[TestCase(1987, "MCMLXXXVII")]
[TestCase(2021, "MMXXI")]
[TestCase(3999, "MMMCMXCIX")]
```

The first refactor I thought might work out, was an if for each of the increments 1000, 900, 500, 400, and so on downward. What I came up with is below, albeit no matter what I can’t seem to like how this code turned out. The fact it also sort of necessitates the exceptions, and sort of blobs up it feels messy and inelegant, like I just sort of crammed through the logic.

```
if ((n < 0) || (n > 3999)) throw new ArgumentOutOfRangeException("insert value betwheen 1 and 3999");
if (n < 1) return string.Empty;
if (n >= 1000) return "M" + BuildRomanNumeral(n - 1000);
if (n >= 900) return "CM" + BuildRomanNumeral(n - 900);
if (n >= 500) return "D" + BuildRomanNumeral(n - 500);
if (n >= 400) return "CD" + BuildRomanNumeral(n - 400);
if (n >= 100) return "C" + BuildRomanNumeral(n - 100);
if (n >= 90) return "XC" + BuildRomanNumeral(n - 90);
if (n >= 50) return "L" + BuildRomanNumeral(n - 50);
if (n >= 40) return "XL" + BuildRomanNumeral(n - 40);
if (n >= 10) return "X" + BuildRomanNumeral(n - 10);
if (n >= 9) return "IX" + BuildRomanNumeral(n - 9);
if (n >= 5) return "V" + BuildRomanNumeral(n - 5);
if (n >= 4) return "IV" + BuildRomanNumeral(n - 4);
if (n >= 1) return "I" + BuildRomanNumeral(n - 1);
throw new ArgumentOutOfRangeException("something bad happened");
```

I went about another refactor, and started thinking through ways to use more of C#’s features. Here is a breakdown of what I did for this refactor.

### Breakdown:

1. **Base Case Handling**: Right off the bat, we handle the simplest case: `if (n == 0) return string.Empty;`. This is our guard clause that ensures we stop the recursion when there’s nothing left to convert. It’s crucial for preventing those pesky `NullReferenceException` errors.
2. **Dictionary Initialization**: We initialize a `Dictionary<int, string>` that maps integer values to their corresponding Roman numeral symbols. This dictionary is our key to deciphering integers into the Roman numeral system.
3. **LINQ Wizardry**: I don’t always use LINQ out of concern that it isn’t easy or immediately readable by many developers, especially that aren’t familiar to C#. But it often makes things wildly simpler from a code perspective.
   - **`Where` Clause**: Filters the dictionary entries to those where `n` is greater than or equal to the key. This ensures we’re only working with valid numeral values.
   - **`Select` Statement**: This is where the recursive magic happens. For each valid dictionary entry, we append the Roman numeral symbol to the result of a recursive call to `Solution(n - p.Key)`. This effectively breaks down the integer and builds the Roman numeral string bit by bit.
   - **`FirstOrDefault`**: Fetches the first valid result from our selection, ensuring the method returns the correct Roman numeral as soon as it’s fully built.

### Why This Rocks:

- **Resilient and Robust**: The addition of the base case for `n == 0` makes this solution more resilient, preventing null references and ensuring smooth execution.
- **Elegant Recursion**: The recursion elegantly handles the conversion by breaking down the problem into smaller chunks, each of which is straightforward to solve.
- **Concise and Readable**: Despite packing powerful logic, the method remains concise and easy to follow, thanks to the clean use of LINQ and a dictionary for symbol mapping.

In essence, this refactored method exemplifies how a blend of recursion and LINQ can yield a highly efficient and readable solution for converting integers to Roman numerals. It’s a prime example of how elegant C# code can be when you leverage the language’s powerful features to their fullest!

```
if (n == 0) return string.Empty;

return new Dictionary<int, string>
{
    {1000, "M"}, {900, "CM"}, {500, "D"}, {400, "CD"},
    {100, "C"}, {90, "XC"}, {50, "L"}, {40, "XL"},
    {10, "X"}, {9, "IX"}, {5, "V"}, {4, "IV"}, {1, "I"}
}.Where(p => n >= p.Key).Select(p => p.Value + BuildRomanNumeral(n - p.Key)).FirstOrDefault()!;
```

With that, I’ll call this problem solved and post complete. I’ve detailed a refined solution for converting integers to Roman numerals using C#. The method begins with a base case to handle zero, preventing null references and ensuring smooth execution. It utilizes a dictionary to map integer values to Roman numeral symbols, and employs LINQ to filter and select the appropriate symbols recursively. The `Where` clause ensures only valid numeral values are processed, while the `Select` statement builds the Roman numeral string piece by piece through recursion. Finally, `FirstOrDefault` returns the fully constructed numeral. This approach is resilient, robust, and elegant, showcasing the power of recursion and LINQ for creating efficient and readable code.

<iframe allowfullscreen="true" class="youtube-player" height="486" loading="lazy" sandbox="allow-scripts allow-same-origin allow-popups allow-presentation allow-popups-to-escape-sandbox" src="https://www.youtube.com/embed/v4ivzRW0pZU?version=3&amp;rel=1&amp;showsearch=0&amp;showinfo=1&amp;iv_load_policy=1&amp;fs=1&amp;hl=en-US&amp;autohide=2&amp;wmode=transparent" style="border:0;" width="863"></iframe>

**Reference**

- [Github](https://github.com/Adron/roman-numerals): [First draft](https://github.com/Adron/roman-numerals/commit/c8571b9e871e1ce57be20320b7e4d3aa8989cece) of the code and [final refactor](https://github.com/Adron/roman-numerals/commit/4d7e5ef4a88624fafadcc363192e1787e86058ee).
