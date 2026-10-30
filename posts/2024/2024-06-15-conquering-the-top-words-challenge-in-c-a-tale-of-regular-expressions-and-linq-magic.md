---
title: 'Conquering the Top Words Challenge in C#: A Tale of Regular Expressions and LINQ Magic'
date: 2024-06-15 13:59:00 -0700
last_modified_at: 2024-06-18 19:07:49 -0700
permalink: /2024/06/15/conquering-the-top-words-challenge-in-c-a-tale-of-regular-expressions-and-linq-magic/
slug: conquering-the-top-words-challenge-in-c-a-tale-of-regular-expressions-and-linq-magic
wp_id: 68390
original_url: https://compositecode.blog/2024/06/15/conquering-the-top-words-challenge-in-c-a-tale-of-regular-expressions-and-linq-magic/
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
excerpt: This article discusses solving the “Top Words Challenge” in C# using regular expressions and LINQ. The author presents the challenge, assumptions, sample tests, and two solutions. The first solution uses regular expressions and LINQ, while the second solution refactors the code to be more concise using LINQ and regular expressions. The article concludes with a link to an additional video and references.
image: /wp-content/uploads/2024/05/csharp-coders.png
---

Programming Problems & Solutions : “Conquering the Top Words Challenge in C#: A Tale of Regular Expressions and LINQ Magic”. The introduction to this series is [here](/2024/05/29/coding-with-ai-a-comparative-series/) and includes all links to every post in the series. If you’d like to watch the video (see just below this), or the AI code up (it’s at the bottom of the post) they’re available! But if you just want to work through the problem keep reading, I cover most of what is in the video plus a slightly different path down below.

<iframe allowfullscreen="true" class="youtube-player" height="486" loading="lazy" sandbox="allow-scripts allow-same-origin allow-popups allow-presentation allow-popups-to-escape-sandbox" src="https://www.youtube.com/embed/Wr3T_SVR0Kg?version=3&amp;rel=1&amp;showsearch=0&amp;showinfo=1&amp;iv_load_policy=1&amp;fs=1&amp;hl=en-US&amp;autohide=2&amp;wmode=transparent" style="border:0;" width="863"></iframe>

*AI Refactoring & Work video at the bottom of the post.*

Today I’m diving into a fascinating coding challenge that had me scratching my head for a bit. But fear not, for I have emerged victorious with a solution that will make your C# heart sing!

## The Challenge

Imagine you’re given a string of text, filled with words, punctuation, and even the occasional line break. My mission, should I choose to accept it – obviously I will – is to write a function that returns an array of the top 3 most occurring words in descending order. Sounds simple enough, right? Well, let’s add a twist!

Here are the assumptions:

- A word is a string of letters (A to Z) optionally containing one or more apostrophes (‘) in ASCII.
- Apostrophes can appear at the start, middle, or end of a word (‘abc, abc’, ‘abc’, ab’c are all valid).
- Any other characters (e.g., #, , /, . …) are not part of a word and should be treated as whitespace.
- Matches should be case-insensitive, and the words in the result should be lowercased.
- Ties may be broken arbitrarily.
- If a text contains fewer than three unique words, then either the top-2 or top-1 words should be returned, or an empty array if a text contains no words.

The Tests Before we embark on this coding adventure, let’s take a look at some sample tests to guide our way:

```
[Test]
public void SampleTests()
{
    Assert.That(TopTrioWords.Top3("a a a b c c d d d d e e e e e"), Is.EqualTo(new List<string> { "e", "d", "a" }));
    Assert.That(TopTrioWords.Top3("e e e e DDD ddd DdD: ddd ddd aa aA Aa, bb cc cC e e e"), Is.EqualTo(new List<string> { "e", "ddd", "aa" }));
    Assert.That(TopTrioWords.Top3(" //wont won't won't "), Is.EqualTo(new List<string> { "won't", "wont" }));
    Assert.That(TopTrioWords.Top3(" , e .. "), Is.EqualTo(new List<string> { "e" }));
    Assert.That(TopTrioWords.Top3(" ... "), Is.EqualTo(new List<string>()));
    Assert.That(TopTrioWords.Top3(" ' "), Is.EqualTo(new List<string>()));
    Assert.That(TopTrioWords.Top3(" ''' "), Is.EqualTo(new List<string>()));
    Assert.That(TopTrioWords.Top3(
        string.Join("\n", [
            "In a village of La Mancha, the name of which I have no desire to call to",
            "mind, there lived not long since one of those gentlemen that keep a lance",
            "in the lance-rack, an old buckler, a lean hack, and a greyhound for",
            "coursing. An olla of rather more beef than mutton, a salad on most",
            "nights, scraps on Saturdays, lentils on Fridays, and a pigeon or so extra",
            "on Sundays, made away with three-quarters of his income."
        ])), Is.EqualTo(new List<string> { "a", "of", "on" }));
}
```

## The First Draft Solution

Alright, let’s dive into the solution! I’ll use the power of regular expressions and LINQ to conquer this challenge. Here’s the first draft code:

```
using System.Text.RegularExpressions;

namespace TopWords;

public static class TopWords
{
    public static List<string> Top3(string s)
    {
        var cleanedText = Regex.Replace(s, "[^a-zA-Z']", " ");

        var words = cleanedText.ToLower().Split(new[] { ' ' }, StringSplitOptions.RemoveEmptyEntries);

        var wordCounts = new Dictionary<string, int>();
        foreach (var word in words)
        {
            if (string.IsNullOrWhiteSpace(word) || Regex.IsMatch(word, "^'+$"))
            {
                continue;
            }

            if (!wordCounts.TryAdd(word, 1))
            {
                wordCounts[word]++;
            }
        }

        var topWords = wordCounts
            .OrderByDescending(x => x.Value)
            .ThenBy(x => x.Key)
            .Take(3)
            .Select(x => x.Key)
            .ToList();

        return topWords;
    }
}
```

Let’s break it down:

1. I start by using a regular expression to remove all non-letter characters except apostrophes from the input string. This ensures it only considers valid words according to the given assumptions.
2. I split the cleaned text into individual words using `ToLower()` to convert them to lowercase and `Split()` to separate them based on whitespace.
3. I create a dictionary called `wordCounts` to store the count of occurrences for each word. I iterate over each word in the `words` array and update the count in the dictionary accordingly. I then skip words that are null, whitespace, or consist only of apostrophes using a regular expression.
4. To get the top 3 words, I use some LINQ magic! I sort the dictionary entries in descending order based on the count of occurrences, then alphabetically in case of ties. We take the top 3 entries, select only the words (keys) from the dictionary entries, and convert the result to a list.
5. Finally, we return the list of top words and bask in the glory of our coding triumph!

And there you have it! A solution that passes all the tests and handles even the trickiest cases with aplomb. Remember, regular expressions and LINQ are your friends when it comes to text manipulation and data querying. But wait, as always there’s more! I’ve gotta refactor this and slim it up!

## Refactoring

Alright, let’s see how we can streamline the code and minimize the lines while still maintaining readability and functionality. Well ok, one could argue about the readability of this one. But in spite of arguments, I delved deeper into regular expressions to see what I could do here, what I came up with is this micro-beast of code.

```
public static string[] Top3(string s)
{
    return Regex.Matches(s.ToLower(), @"[a-z']+")
        .Cast<Match>()
        .Select(m => m.Value)
        .Where(word => !Regex.IsMatch(word, "^'+$"))
        .GroupBy(word => word)
        .OrderByDescending(g => g.Count())
        .ThenBy(g => g.Key)
        .Take(3)
        .Select(g => g.Key)
        .ToArray();
}
```

Let’s break down the changes:

1. I use `Regex.Matches()` to find all the valid words in the input string directly, instead of cleaning the string and splitting it into words separately. The regular expression `[a-z']+` matches one or more lowercase letters or apostrophes.
2. I use `Cast<Match>()` to cast the `MatchCollection` returned by `Regex.Matches()` to an `IEnumerable<Match>`, allowing us to use LINQ methods on it.
3. I use `Select(m => m.Value)` to extract the matched word from each `Match` object.
4. I use `Where(word => !Regex.IsMatch(word, "^'+$"))` to filter out words that consist only of apostrophes.
5. I use `GroupBy(word => word)` to group the words by their value, effectively counting the occurrences of each word.
6. I use `OrderByDescending(g => g.Count())` to sort the groups in descending order based on the count of occurrences.
7. I use `ThenBy(g => g.Key)` to sort the groups alphabetically in case of ties.
8. I use `Take(3)` to select the top 3 groups.
9. I use `Select(g => g.Key)` to extract the word from each group.
10. Finally, I use `ToArray()` to convert the result to an array of strings.
11. I changed the method signature has been changed to return an array of strings (`string[]`) instead of a list (`List<string>`). This is just a minor adjustment to further reduce the code.

This refactored code achieves the same functionality as the previous solution but in a more concise manner. It leverages the power of LINQ and regular expressions to minimize the lines of code while still handling all the necessary cases. If you’re not familiar with LINQ and regular expressions it’s an unreadable nightmare, but if you are, it’s a thing of beauty!

With that, hope you dug this challenge and the walk through. Cheers! 🍻

## AI Lagniappe

<iframe allowfullscreen="true" class="youtube-player" height="486" loading="lazy" sandbox="allow-scripts allow-same-origin allow-popups allow-presentation allow-popups-to-escape-sandbox" src="https://www.youtube.com/embed/J4qS2AvdHDE?version=3&amp;rel=1&amp;showsearch=0&amp;showinfo=1&amp;iv_load_policy=1&amp;fs=1&amp;hl=en-US&amp;autohide=2&amp;wmode=transparent" style="border:0;" width="863"></iframe>

## References

- Github [repo](https://github.com/Adron/TopWords).
