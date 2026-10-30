---
title: Why Clean Code Seriously Matters!
date: 2011-12-09 11:45:56 -0800
last_modified_at: 2011-12-09 11:32:28 -0800
permalink: /2011/12/09/why-clean-code-seriously-matters/
slug: why-clean-code-seriously-matters
wp_id: 4521
original_url: https://compositecode.blog/2011/12/09/why-clean-code-seriously-matters/
categories:
- .NET Bits
- Rants
tags:
- c#
- clean code
- code
excerpt: The first example is some working code, that determines if a date value is a weekend day and returns true or false based on that. bool firstSecondNulls = false; var dayOfWeek = (DateTime) zeros.ElementAtOrDefault(i).BalanceDate; if (dayOfWeek.DayOfWeek == DayOfWeek.Sunday || dayOfWeek.DayOfWeek == DayOfWeek.Saturday) firstSecondNulls = true; return firstSecondNulls; This second example also provides the same result, except in a more readable, cleaner, and more efficient way. Matter of fact, I’d say in some circumstances it is exponentially more efficient! Do you see why? var dayOfWeek = (DateTime) zeros.ElementAtOrDefault(i).BalanceDate; return dayOfWeek.DayOfWeek == DayOfWeek.Sunday || dayOfWeek.DayOfWeek == DayOfWeek.Saturday; This is an insanely simple example. But just imagine some of the nightmarish methods and functions, with hundreds of lines of code. Keep in mind, that those nightmares are minimal compared to the Enterprise Scale 1000+ plus line methods! Yes, those exist and they are beyond nightmares but holocausts of thought and design! So the next time you think “meh, I’ll refactor it later.” just take that extra minute or two and do it now! The pay off, you know full well when you think about it, is massive in the end. Cheers!
---

The first example is some working code, that determines if a date value is a weekend day and returns true or false based on that.

```csharp
bool firstSecondNulls = false;
var dayOfWeek = (DateTime) zeros.ElementAtOrDefault(i).BalanceDate;
if (dayOfWeek.DayOfWeek == DayOfWeek.Sunday || dayOfWeek.DayOfWeek == DayOfWeek.Saturday)
    firstSecondNulls = true;
return firstSecondNulls;
```

This second example also provides the same result, except in a more readable, cleaner, and more efficient way. Matter of fact, I’d say in some circumstances it is exponentially more efficient! Do you see why?

```csharp
var dayOfWeek = (DateTime) zeros.ElementAtOrDefault(i).BalanceDate;
return dayOfWeek.DayOfWeek == DayOfWeek.Sunday || dayOfWeek.DayOfWeek == DayOfWeek.Saturday;
```

This is an insanely simple example. But just imagine some of the nightmarish methods and functions, with hundreds of lines of code. Keep in mind, that those nightmares are minimal compared to the Enterprise Scale 1000+ plus line methods! Yes, those exist and they are beyond nightmares but holocausts of thought and design!

So the next time you think “meh, I’ll refactor it later.” just take that extra minute or two and do it now! The pay off, you know full well when you think about it, is massive in the end. Cheers!
