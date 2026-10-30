---
title: 'Simplifying Time: Humanizing Duration in Programming'
date: 2024-06-11 22:34:00 -0700
last_modified_at: 2024-06-12 01:39:31 -0700
permalink: /2024/06/11/4-simplifying-time-humanizing-duration-in-programming/
slug: 4-simplifying-time-humanizing-duration-in-programming
wp_id: 68389
original_url: https://compositecode.blog/2024/06/11/4-simplifying-time-humanizing-duration-in-programming/
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
excerpt: The article discusses the challenge of converting seconds into a human-readable format for software development. It provides a C# solution and discusses the process of refining the solution for better readability and reusability. The final solution demonstrates the broader challenge of enhancing user interaction through well-tested code and can be adapted to various programming languages.
image: /wp-content/uploads/2024/05/csharp-coders.png
---

Programming Problems & Solutions : “Simplifying Time: Humanizing Duration in Programming”. The introduction to this series is [here](/2024/05/29/coding-with-ai-a-comparative-series/) and includes all links to every post in the series. If you’d like to watch the video (see just below this), or the AI code up (it’s at the bottom of the post) they’re available! But if you just want to work through the problem keep reading, I cover most of what is in the video plus a slightly different path down below.

<iframe allowfullscreen="true" class="youtube-player" height="486" loading="lazy" sandbox="allow-scripts allow-same-origin allow-popups allow-presentation allow-popups-to-escape-sandbox" src="https://www.youtube.com/embed/oIwApA7i52A?version=3&amp;rel=1&amp;showsearch=0&amp;showinfo=1&amp;iv_load_policy=1&amp;fs=1&amp;hl=en-US&amp;autohide=2&amp;wmode=transparent" style="border:0;" width="863"></iframe>

*To check out the AI refactoring and feature additions, that video is at the bottom of this post.*

In software development, seemingly simple tasks can unfold into complex challenges, especially when it involves outputs that must be human-centric, such as formatting time durations into a readable format. This is the case with the task of converting seconds into an easily digestible format for users.

#### The Challenge

The objective is straightforward: write a function that converts a given number of seconds into a format easy for humans to read. If it’s zero seconds, the function should return “now”. Otherwise, it should represent the duration as a combination of years, days, hours, minutes, and seconds, following specific formatting rules.

#### Why This Matters

Presenting users with raw seconds in applications where time durations are critical (like project timelines or cooking timers) is not helpful. Human-readable formats allow users to quickly and intuitively understand the information presented.

#### Testing and Validation

As usual, I like to write out some tests to get my thinking sorted out and do initial class and structure design this way. I start off here with now, because it’s always now.

```
using NUnit.Framework;

[TestFixture]
public class Tests {
  [Test]
  public void basicTests() {
    Assert.AreEqual("now", HumanTimeFormat.formatDuration(0));
    Assert.AreEqual("1 second", HumanTimeFormat.formatDuration(1));
    Assert.AreEqual("1 minute and 2 seconds", HumanTimeFormat.formatDuration(62));
    Assert.AreEqual("2 minutes", HumanTimeFormat.formatDuration(120));
    Assert.AreEqual("1 hour, 1 minute and 2 seconds", HumanTimeFormat.formatDuration(3662));
    Assert.AreEqual("182 days, 1 hour, 44 minutes and 40 seconds", HumanTimeFormat.formatDuration(15731080));
    Assert.AreEqual("4 years, 68 days, 3 hours and 4 minutes", HumanTimeFormat.formatDuration(132030240));
    Assert.AreEqual("6 years, 192 days, 13 hours, 3 minutes and 54 seconds", HumanTimeFormat.formatDuration(205851834));
    Assert.AreEqual("8 years, 12 days, 13 hours, 41 minutes and 1 second", HumanTimeFormat.formatDuration(253374061));
    Assert.AreEqual("7 years, 246 days, 15 hours, 32 minutes and 54 seconds", HumanTimeFormat.formatDuration(242062374));
    Assert.AreEqual("3 years, 85 days, 1 hour, 9 minutes and 26 seconds", HumanTimeFormat.formatDuration(101956166));
    Assert.AreEqual("1 year, 19 days, 18 hours, 19 minutes and 46 seconds", HumanTimeFormat.formatDuration(33243586));
  }
}
```

#### Starting Code

The task begins with a simple C# class structure:

```
public class HumanTimeFormat{
  public static string formatDuration(int seconds){
    // Enter Code here
  }
}
```

#### Implementing the Solution

My first draft function, `formatDuration`, handles the conversion of seconds into a structured and readable string.

```
public class HumanTimeFormat
{
    public static string formatDuration(int seconds)
    {
        if (seconds == 0) return "now";

        int secondsPerMinute = 60;
        int secondsPerHour = 60 * secondsPerMinute;
        int secondsPerDay = 24 * secondsPerHour;
        int secondsPerYear = 365 * secondsPerDay;

        int years = seconds / secondsPerYear;
        seconds %= secondsPerYear;
        int days = seconds / secondsPerDay;
        seconds %= secondsPerDay;
        int hours = seconds / secondsPerHour;
        seconds %= secondsPerHour;
        int minutes = seconds / secondsPerMinute;
        seconds %= secondsPerMinute;

        List<string> parts = new List<string>();
        if (years > 0) parts.Add($"{years} year{(years > 1 ? "s" : "")}");
        if (days > 0) parts.Add($"{days} day{(days > 1 ? "s" : "")}");
        if (hours > 0) parts.Add($"{hours} hour{(hours > 1 ? "s" : "")}");
        if (minutes > 0) parts.Add($"{minutes} minute{(minutes > 1 ? "s" : "")}");
        if (seconds > 0) parts.Add($"{seconds} second{(seconds > 1 ? "s" : "")}");

        return parts.Count > 1
            ? string.Join(", ", parts.Take(parts.Count - 1)) + " and " + parts.Last()
            : parts.FirstOrDefault();
    }
}
```

The `formatDuration` function not only meets the practical needs of converting seconds into a user-friendly format but also illustrates the broader challenge in software development of enhancing user interaction through thoughtful, well-tested code. The solution, specific to C#, demonstrates a methodology that can be adapted across various programming languages, embodying a universal challenge and its resolution.

## Refactoring Time (No Pun’ Intended)

Immediately I stepped into a few key changes.

1. Introduced constants `TimeUnits` and `TimeUnitValues` to store the time unit names and their corresponding values in seconds. This makes the code more readable and avoids hard-coding the values multiple times.
2. Renamed the method to `FormatDuration` to follow the C# naming convention.
3. Used a `for` loop to iterate over the time units and their values. This eliminates the repetitive code for each time unit.
4. Extracted the logic for formatting a single part (e.g., “1 year” or “2 days”) into a separate method `FormatPart`. This improves readability and reusability.
5. Extracted the logic for combining the parts into a separate method `CombineParts`. This makes the main method `FormatDuration` more focused and easier to understand.

```
public class HumanTimeFormat
{
    private static readonly string[] TimeUnits = { "year", "day", "hour", "minute", "second" };
    private static readonly int[] TimeUnitValues = { 365 * 24 * 60 * 60, 24 * 60 * 60, 60 * 60, 60, 1 };

    public static string FormatDuration(int seconds)
    {
        if (seconds == 0)
            return "now";

        var parts = new List<string>();

        for (int i = 0; i < TimeUnitValues.Length; i++)
        {
            int count = seconds / TimeUnitValues[i];
            if (count > 0)
            {
                parts.Add(FormatPart(count, TimeUnits[i]));
                seconds %= TimeUnitValues[i];
            }
        }

        return CombineParts(parts);
    }

    private static string FormatPart(int count, string unit)
    {
        return $"{count} {unit}{(count > 1 ? "s" : "")}";
    }

    private static string CombineParts(List<string> parts)
    {
        return parts.Count > 1
            ? string.Join(", ", parts.Take(parts.Count - 1)) + " and " + parts.Last()
            : parts.FirstOrDefault();
    }
}
```

Ran the tests and they passed. All looked good, and I’m happy with this string of refactors, so I’m going to call this one a day! Happy thrashing coding. 🤘🏻

<iframe allowfullscreen="true" class="youtube-player" height="486" loading="lazy" sandbox="allow-scripts allow-same-origin allow-popups allow-presentation allow-popups-to-escape-sandbox" src="https://www.youtube.com/embed/keh_nqkTgvM?version=3&amp;rel=1&amp;showsearch=0&amp;showinfo=1&amp;iv_load_policy=1&amp;fs=1&amp;hl=en-US&amp;autohide=2&amp;wmode=transparent" style="border:0;" width="863"></iframe>

**Reference**

- [Github repo](https://github.com/Adron/humanizing-duration).
