---
title: C# Array to Phone Number String Conversion & Testing with NUnit
date: 2024-06-01 14:10:00 -0700
last_modified_at: 2024-06-01 14:17:28 -0700
permalink: /2024/06/01/c-array-to-phone-number-string-conversion-testing-with-nunit/
slug: c-array-to-phone-number-string-conversion-testing-with-nunit
wp_id: 68365
original_url: https://compositecode.blog/2024/06/01/c-array-to-phone-number-string-conversion-testing-with-nunit/
categories:
- .NET Bits
- c#
- Code Katas
tags:
- c#
- code exercises
- coding
- csharp
- dotnet
- kata
excerpt: This article discusses a coding challenge to create a phone number from an array of integers in C#. The solution uses string formatting, robust testing with NUnit, and extends to include internationalization and encoding/decoding features for phone numbers. The article details the implementation, testing, and challenges faced, providing valuable insights for software developers.
image: /wp-content/uploads/2024/05/csharp-coders.png
---

Programming Problems & Solutions : “How to Format Arrays as Phone Numbers with NUnit Testing”. The introduction to this series is [here](/2024/05/29/coding-with-ai-a-comparative-series/) and includes all links to every post in the series. If you’d like to watch the video (see just below this), or the AI code up (it’s at the bottom of the post) they’re available! But if you just want to work through the problem keep reading, I cover most of what is in the video plus a slightly different path down below.

<iframe allowfullscreen="true" class="youtube-player" height="486" loading="lazy" sandbox="allow-scripts allow-same-origin allow-popups allow-presentation allow-popups-to-escape-sandbox" src="https://www.youtube.com/embed/AK60kogoQZA?version=3&amp;rel=1&amp;showsearch=0&amp;showinfo=1&amp;iv_load_policy=1&amp;fs=1&amp;hl=en-US&amp;autohide=2&amp;wmode=transparent" style="border:0;" width="863"></iframe>

*The AI continuation and lagniappe is at the bottom of this post.*

In the world of software development, sometimes a seemingly simple task has lessons to teach such as language features and problem-solving. Today, I’m diving into a fun coding challenge that does exactly that: writing a method in C# that takes an array of 10 integers and returns these numbers formatted as a phone number. This exercise is perfect for understanding array manipulation, string formatting, and how to effectively use testing frameworks like NUnit to verify our solution.

#### The Challenge

Imagine you are given an array of 10 integers, each between 0 and 9. My task is to write a function that converts this array into a string that represents these numbers in the format of a standard *North American* phone number. Here’s the format we’re aiming for: “(XXX) XXX-XXXX”.

#### The Setup

To start, I’ll structure our solution within a simple class called `Kata` with a static method `CreatePhoneNumber`:

```
public class Kata
{
  public static string CreatePhoneNumber(int[] numbers)
  {
    // This will be our implementation space.
  }
}
```

#### Crafting the Solution

Using C#’s `string.Format` method allows us to insert the elements of the array into a formatted string seamlessly. This method is not only straightforward but also ensures that the placement of each number is exactly where it needs to be within the phone number format. Here’s how you can implement it:

```
public static class Kata
{
  public static string CreatePhoneNumber(int[] numbers)
  {
    return string.Format("({0}{1}{2}) {3}{4}{5}-{6}{7}{8}{9}",
                         numbers[0], numbers[1], numbers[2], numbers[3], numbers[4],
                         numbers[5], numbers[6], numbers[7], numbers[8], numbers[9]);
  }
}
```

#### Why This Approach?

The `string.Format` method is incredibly powerful for a few reasons:

- **Clarity:** The format string clearly shows the structure of the output, making the code easy to understand at a glance.
- **Maintainability:** Changes in the format can be made simply by adjusting the format string.
- **Scalability:** This method can easily be adapted to different or more complex formatting requirements without changing the underlying logic.

#### Ensuring Code Reliability

To make sure our function behaves as expected, we use NUnit testing framework to create a set of test cases:

```
namespace Solution
{
  using NUnit.Framework;

  [TestFixture]
  public class Tests
  {
    [Test]
    [TestCase(new int[]{1,2,3,4,5,6,7,8,9,0}, ExpectedResult="(123) 456-7890")]
    [TestCase(new int[]{1,1,1,1,1,1,1,1,1,1}, ExpectedResult="(111) 111-1111")]
    public static string FixedTest(int[] numbers)
    {
      return Kata.CreatePhoneNumber(numbers);
    }
  }
}
```

The key takeaway is that understanding and utilizing the string formatting capabilities of your programming language can greatly simplify tasks involving data presentation. Moreover, integrating robust testing ensures that our code meets the requirements before it is deployed or integrated into a larger system.

## Expanding Functionality – Encoding & Decoding

At this point we’ve got the `CreatePhoneNumber` method and it does it’s job. But it does only it’s job, let’s add two things into the mix.

1. I’ll first add the capability to add an internationalized code.
2. I’ll also add a feature to take a phone number in the format displayed and encode it back into an array.

Both of those features added and I will also dramatically expand the test coverage of these capabilities. First, getting things added for an internationalized code. Refactoring the tests gives them a format like this.

```
[TestCase(new int[]{1,1,2,3,4,5,6,7,8,9,0}, ExpectedResult="+1 (123) 456-7890")]
[TestCase(new int[]{1,1,1,1,1,1,1,1,1,1,1}, ExpectedResult="+1 (111) 111-1111")]
```

Both of these tests continue on the happy path, just internationalizing the phone numbers solely for the US market (the US country code is 1). First I’ll go ahead and refactor the `CreatePhoneNumber` method to deal with this addition.

```
public static string CreatePhoneNumber(int[] numbers)
{
    return string.Format("+{0} ({1}{2}{3}) {4}{5}{6}-{7}{8}{9}{10}",
        numbers[0], numbers[1], numbers[2], numbers[3], numbers[4],
        numbers[5], numbers[6], numbers[7], numbers[8], numbers[9], numbers[10]);
}
```

There are lots of country codes beyond 1, after making this change I went ahead and added a few more for testing. For a list of country codes and the expansive nature of how many there are, check out the [Wikipedia page for a starter on the topic](https://en.wikipedia.org/wiki/List_of_country_calling_codes).

```
[TestCase(new int[]{30,1,2,3,4,5,6,7,8,9,0}, ExpectedResult="+30 (123) 456-7890")] // Greece
[TestCase(new int[]{31,1,2,3,4,5,6,7,8,9,0}, ExpectedResult="+31 (123) 456-7890")] // Netherlands
[TestCase(new int[]{380,1,1,1,1,1,1,1,1,1,1}, ExpectedResult="+380 (111) 111-1111")] // Ukraine
```

At this point I wanted to tackle some of the edge cases that would make an incorrect number. For example if a value larger than 9 was entered in as one of the digits for the phone number, it would make an invalid phone number.

```
[TestCase(new int[]{45,15,2,3,4,93,6,7,8,9,0}, ExpectedResult="+31 (123) 456-7890")] // Denmark
```

This number would fail, as shown below, based on the code that is currently implemented.

[![](/wp-content/uploads/2024/05/CleanShot-2024-05-14-at-12.09.25@2x.png)](/wp-content/uploads/2024/05/CleanShot-2024-05-14-at-12.09.25@2x.png)

Obviously something needs done, but the question is, should it throw an exception or return something like “Invalid phone number, digits 1 and 5 are out of range of 0 to 9.” I’ve thought about it a little bit, and am going to opt for the message instead. Since it isn’t really a *system* error, but simply a data error that might need to be pushed through to the client side, a message would be ideal in this situation. YMMV.

The following is my first take at a message, I’m going to add just the “Invalid phone number.” as the response. I’ll work on the related messaging after adding a few tests.

```
[TestCase(new int[]{45,15,2,3,4,93,6,7,8,9,0}, ExpectedResult="Invalid phone number.")] // Denmark
[TestCase(new int[]{46,1,2,3,63,9,6,7,8,9,0}, ExpectedResult="Invalid phone number.")] // Sweden
[TestCase(new int[]{47,1,55,3,4,9,6,7,8,9,0}, ExpectedResult="Invalid phone number.")] // Norway
```

My first implementation to implement this was pretty clean

```
foreach (int digit in numbers)
{
    if (digit < 0 || digit > 9)
        return "Invalid phone number.";
}
```

But, obviously I don’t want to check the first digit, because the international code could be 1 or it could be 300 or something. I wasn’t sure so I looked up specification E.123 and E.164 for international numbers. In those specifications I immediately learned a host of things, such as the fact the internationalization of the number, by adding the +1 or the +45, includes the + and also removes the parenthesis that I’ve got on the numbers above. For just national numbers the international code isn’t used and the parenthesis come back! Yikes, the complexities! For now, I’m just going to aim for the first digit being in the range of 0-9999, which appears to be the specification. I’ll read deeper into that in the future, but for now I’ll get these parts working correctly based on just adding the international number at the front and not dealing with removal or addition of the parenthesis. To ensure that the international number is covered, I changed the simple implemented code to the following.

```
int countryCode = numbers[0];

if (countryCode < 1 || countryCode > 9999)
{
    return "Invalid phone number.";
}

for (int digitIndex = 1; digitIndex < numbers.Length; digitIndex++)
{
    int digit = numbers[digitIndex];
    if (digit > 9)
        return "Invalid phone number.";
}
```

That’s more code, but as I add criteria it will get even bigger and more specific. But so far, this code passes the tests.

Now I’ll put together an encoding method I’ll call `EncodePhone` and have it take a string parameter of the number. The first test for this method I shaped up something like this, using the opposing of one of the previous tests.

```
[Test, TestCase("+1 (123) 456-7890", ExpectedResult = new int[] { 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0 })]
    public static int[] EncodeTest(string number)
    {
        return Kata.EncodePhone(number);
    }
```

My first draft of the method implemented came out like this.

```
public static int[] EncodePhone(string phoneNumber)
{
    string cleanedNumber = new string(phoneNumber.Where(char.IsDigit).ToArray());

    if (cleanedNumber.Length != 11)
    {
        throw new ArgumentException("Invalid phone number format.");
    }

    // Convert each character to an integer and store in an array
    int[] numbers = new int[cleanedNumber.Length];
    for (int i = 0; i < cleanedNumber.Length; i++)
    {
        numbers[i] = int.Parse(cleanedNumber[i].ToString());
    }

    return numbers;
}
```

That passed, but I’ll add some of the other tests now to work out the edge cases and refactor accordingly. As I worked through this, it would obviously, just as before, run into problems with the added country code and it’s variable number of digits. I went back to work on this issue so the parsing is handled differently for the country code.

```
public static int[] EncodePhone(string phoneNumber)
{
    string cleanedNumber = new string(phoneNumber.Where(char.IsDigit).ToArray());

    if (cleanedNumber.Length < 11 || cleanedNumber.Length > 13)
    {
        throw new ArgumentException("Invalid phone number format.");
    }

    // Identify the country code length (1 to 3 digits)
    int countryCodeLength = cleanedNumber.Length - 10;

    // Create an array for the result
    int[] numbers = new int[11];

    // Parse the country code and store it as a single element
    numbers[0] = int.Parse(cleanedNumber.Substring(0, countryCodeLength));

    // Parse the remaining phone number digits
    for (int i = 0; i < 10; i++)
    {
        numbers[i + 1] = int.Parse(cleanedNumber[countryCodeLength + i].ToString());
    }

    return numbers;
}
```

This finally got the tests to pass.

As we know at this point the `EncodePhone` method is designed to parse a formatted phone number string and return an array of integers representing the individual digits of the phone number, including the country code. Here’s a detailed breakdown of the code:

```
string cleanedNumber = new string(phoneNumber.Where(char.IsDigit).ToArray());
```

This line removes all non-digit characters from the input `phoneNumber` string. The `Where(char.IsDigit)` filters out only the digit characters, and `ToArray` converts the resulting sequence into a character array. Finally, a new string is created from this array, resulting in `cleanedNumber` containing only numeric digits.

```
if (cleanedNumber.Length < 11 || cleanedNumber.Length > 13)
{
    throw new ArgumentException("Invalid phone number format.");
}
```

The method checks if the length of `cleanedNumber` is between 11 and 13 characters. This range accommodates a country code of 1 to 3 digits and a phone number of 10 digits. If the length is outside this range, an `ArgumentException` is thrown, indicating an invalid phone number format.

```
int countryCodeLength = cleanedNumber.Length - 10;
```

The length of the country code is calculated by subtracting 10 (the length of the phone number part) from the total length of `cleanedNumber`. This calculation determines whether the country code is 1, 2, or 3 digits long.

```
int[] numbers = new int[11];
```

An array `numbers` of length 11 is created to store the final result. The first element will hold the country code, and the remaining 10 elements will hold the digits of the phone number.

```
numbers[0] = int.Parse(cleanedNumber.Substring(0, countryCodeLength));
```

The country code is extracted from the beginning of `cleanedNumber` using the `Substring` method, starting at index 0 and spanning `countryCodeLength` characters. This substring is then parsed into an integer and stored as the first element of the `numbers` array.

```
for (int i = 0; i < 10; i++)
{
    numbers[i + 1] = int.Parse(cleanedNumber[countryCodeLength + i].ToString());
}
```

A `for` loop iterates over the next 10 digits of `cleanedNumber`, starting after the country code. Each digit is converted to an integer and stored in the corresponding position in the `numbers` array, starting from index 1.

Then finally `return numbers;`. The method returns the `numbers` array, which contains the country code as the first element and the digits of the phone number as the subsequent elements.

```
string formattedPhoneNumber = "+123 (456) 789-0123";
int[] phoneNumberDigits = EncodePhone(formattedPhoneNumber);

foreach (int digit in phoneNumberDigits)
{
    Console.Write(digit + " ");
}
```

The output would be something like `Output: 123 4 5 6 7 8 9 0 1 2 3`.

With that I’m going to call this one a wrap, until next time, happy coding!

## Lagniappe – The AI Analysis

<iframe allowfullscreen="true" class="youtube-player" height="486" loading="lazy" sandbox="allow-scripts allow-same-origin allow-popups allow-presentation allow-popups-to-escape-sandbox" src="https://www.youtube.com/embed/MUJjkp2rg80?version=3&amp;rel=1&amp;showsearch=0&amp;showinfo=1&amp;iv_load_policy=1&amp;fs=1&amp;hl=en-US&amp;autohide=2&amp;wmode=transparent" style="border:0;" width="863"></iframe>

**Reference**

- Github: My [first draft](https://github.com/Adron/arrays-as-phone-numbers/commit/255e444d08df0573440f79c81f1c9864391583c4), and then the [final commit](https://github.com/Adron/arrays-as-phone-numbers/commit/aca5afb5403cc480862e2186d0b24d850c5eaf4c) all [here](https://github.com/Adron/arrays-as-phone-numbers).
