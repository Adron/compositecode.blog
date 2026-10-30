---
title: 'How to Convert an IPv4 Address to a 32-bit Integer in C#: A Step-by-Step Guide'
date: 2024-06-21 12:09:00 -0700
last_modified_at: 2024-06-24 10:00:25 -0700
permalink: /2024/06/21/6-how-to-convert-an-ipv4-address-to-a-32-bit-integer-in-c-a-step-by-step-guide/
slug: 6-how-to-convert-an-ipv4-address-to-a-32-bit-integer-in-c-a-step-by-step-guide
wp_id: 68391
original_url: https://compositecode.blog/2024/06/21/6-how-to-convert-an-ipv4-address-to-a-32-bit-integer-in-c-a-step-by-step-guide/
categories:
- .NET Bits
- c#
- Code Katas
tags:
- c#
- code exercises
- code kata
- coding
- csharp
- dotnet
- kata
excerpt: In this programming article, the author presents a challenge of converting an IPv4 address into a 32-bit integer. The process involves splitting the IP address, converting octets to integers, performing bitwise shifting, and using bitwise OR to combine the values. A C# function is provided for this purpose, along with tests and a refactored solution.
image: /wp-content/uploads/2024/05/csharp-coders.png
---

Programming Problems & Solutions : “How to Convert an IPv4 Address to a 32-bit Integer in C#: A Step-by-Step Guide”. The introduction to this series is [here](/2024/05/29/coding-with-ai-a-comparative-series/) and includes all links to every post in the series. If you’d like to watch the video (see just below this), or the AI code up (it’s at the bottom of the post) they’re available! But if you just want to work through the problem keep reading, I cover most of what is in the video plus a slightly different path down below.

<iframe allowfullscreen="true" class="youtube-player" height="486" loading="lazy" sandbox="allow-scripts allow-same-origin allow-popups allow-presentation allow-popups-to-escape-sandbox" src="https://www.youtube.com/embed/uYwaJIfJQK0?version=3&amp;rel=1&amp;showsearch=0&amp;showinfo=1&amp;iv_load_policy=1&amp;fs=1&amp;hl=en-US&amp;autohide=2&amp;wmode=transparent" style="border:0;" width="863"></iframe>

Hey there, fellow code wranglers! Time to dive deep into the land of bits and bytes and IP addresses. Today, I’m tackling a neat little programming challenge: converting an IPv4 address into a 32-bit integer. A fun exercise that hones your bitwise operation skills and deepens your understanding of IP addresses.

Let’s kick things off with the essentials. An IPv4 address, such as `128.32.10.1`, consists of four octets. Each octet is a byte (8 bits), and together they form a 32-bit number. Here’s a quick breakdown:

- 1st octet: 128 -> `10000000`
- 2nd octet: 32 -> `00100000`
- 3rd octet: 10 -> `00001010`
- 4th octet: 1 -> `00000001`

When we line them up, we get: `10000000.00100000.00001010.00000001`

This binary sequence can be translated to the 32-bit number `2149583361`. Our task is to write a function `ToInt32` in C# that takes an IPv4 address as input and returns this 32-bit number.

Let’s break it down step-by-step:

1. **Split the IP Address**: We split the string representation of the IP address into its four octets.
2. **Convert to Integer**: Convert each octet from a string to an integer.
3. **Bitwise Shifting**: Shift each octet into its proper position within the 32-bit integer.
4. **Combine Using Bitwise OR**: Use the bitwise OR operation to combine these values into the final 32-bit integer.

Here’s how we do it in code:

```
namespace IpConverter;

public static class IpConvert
{
    public static uint ToInt32(string ip)
    {
        string[] octets = ip.Split('.');
        uint ipNumber = 0;

        ipNumber += Convert.ToUInt32(octets[0]) << 24; // Shift the first octet left by 24 bits
        ipNumber += Convert.ToUInt32(octets[1]) << 16; // Shift the second octet left by 16 bits
        ipNumber += Convert.ToUInt32(octets[2]) << 8;  // Shift the third octet left by 8 bits
        ipNumber += Convert.ToUInt32(octets[3]);       // Fourth octet stays as is

        return ipNumber;
    }
}
```

### Walking Through the Code:

```
using IpConverter;

namespace IpConverterTests;

public class Tests
{
    [SetUp]
    public void Setup()
    {
    }

    [Test]
    public void TestIPtoInt()
    {
        Assert.That(IpConvert.ToInt32("128.32.10.1"), Is.EqualTo(2149583361), "Incorrect answer for ip = \"128.32.10.1\"");
    }
}
```

This test checks whether the function `ToInt32` correctly converts `"128.32.10.1"` to `2149583361`. When the test passes, we can confidently say our function works for this input. At this point, this seems to be a working solution, but I’m going to add a few more tests regardless, just to have them cover more of the cases to make sure my refactoring doesn’t get off in the weeds.

### Refactoring

First up, the tests I added.

```
public class Tests
{
    [Test]
    public void TestIPtoInt_ValidIP()
    {
        Assert.That(IpConvert.ToInt32("128.32.10.1"), Is.EqualTo(2149583361), "Incorrect answer for ip = \"128.32.10.1\"");
    }

    [Test]
    public void TestIPtoInt_AllZeros()
    {
        Assert.That(IpConvert.ToInt32("0.0.0.0"), Is.EqualTo(0), "Incorrect answer for ip = \"0.0.0.0\"");
    }

    [Test]
    public void TestIPtoInt_AllOnes()
    {
        Assert.That(IpConvert.ToInt32("255.255.255.255"), Is.EqualTo(4294967295), "Incorrect answer for ip = \"255.255.255.255\"");
    }

    [Test]
    public void TestIPtoInt_LeadingZeros()
    {
        Assert.That(IpConvert.ToInt32("001.002.003.004"), Is.EqualTo(16909060), "Incorrect answer for ip = \"001.002.003.004\"");
    }

    [Test]
    public void TestIPtoInt_RandomIP()
    {
        Assert.That(IpConvert.ToInt32("192.168.0.1"), Is.EqualTo(3232235521), "Incorrect answer for ip = \"192.168.0.1\"");
    }

    [Test]
    public void TestIPtoInt_RandomIP2()
    {
        Assert.That(IpConvert.ToInt32("10.0.0.1"), Is.EqualTo(167772161), "Incorrect answer for ip = \"10.0.0.1\"");
    }
}
```

- `TestIPtoInt_AllZeros`: Tests the conversion of an IP address with all octets being zero.
- `TestIPtoInt_AllOnes`: Tests the conversion of an IP address with all octets being 255.
- `TestIPtoInt_LeadingZeros`: Tests the conversion of an IP address with leading zeros in theoctets.
- `TestIPtoInt_RandomIP` and `TestIPtoInt_RandomIP2`: Test the conversion of random IP addresses to ensure the function works correctly for different inputs.

With that done I delved into a refactor of the method. After a few minutes I kind of just realized, using IDE refactoring options and thinking it through, I came up with the following:

I split the IP address string into an array of octets using `Split('.')`. Then I used `Select` to convert each octet from a string to an unsigned 32-bit integer using `Convert.ToUInt32`. I then used `Aggregate` to iterate over the octets and combine them into a single 32-bit integer:

- The `result` parameter accumulates the result of bitwise shifting and adding the octets.
- For each octet, we left-shift the `result` by 8 bits (`<< 8`) and then add the current octet to it.
- The final result is the 32-bit integer representation of the IP address.

```
namespace IpConverter;

public static class IpConvert
{
    public static uint ToInt32(string ip)
    {
        return ip.Split('.')
                 .Select(octet => Convert.ToUInt32(octet))
                 .Aggregate((result, octet) => (result << 8) + octet);
    }
}
```

With that another problem solved and code refactored. Happy thrashing code, catch ya next installment!

## AI Tooling Lagniappe!

<iframe allowfullscreen="true" class="youtube-player" height="486" loading="lazy" sandbox="allow-scripts allow-same-origin allow-popups allow-presentation allow-popups-to-escape-sandbox" src="https://www.youtube.com/embed/Qc6bJCCw8Zk?version=3&amp;rel=1&amp;showsearch=0&amp;showinfo=1&amp;iv_load_policy=1&amp;fs=1&amp;hl=en-US&amp;autohide=2&amp;wmode=transparent" style="border:0;" width="863"></iframe>

**Reference**

- [Github](https://github.com/Adron/ipv4-to-32bit-int) with [first draft](https://github.com/Adron/ipv4-to-32bit-int/commit/cd46307522a39164fae264570b4875706be29c8a) and the [refactoring](https://github.com/Adron/ipv4-to-32bit-int/commit/4c0aef0cf01478b323e70de16156603ed75dc3a5). Then finally, [the AI lagniappe](https://github.com/Adron/ipv4-to-32bit-int/commit/8bf8a79ee2048211871547da65376180e2e35b67)!
