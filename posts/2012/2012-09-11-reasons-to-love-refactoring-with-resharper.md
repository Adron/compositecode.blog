---
title: Reasons to Love Refactoring with ReSharper
date: 2012-09-11 17:14:45 -0700
last_modified_at: 2012-09-11 17:14:45 -0700
permalink: /2012/09/11/reasons-to-love-refactoring-with-resharper/
slug: reasons-to-love-refactoring-with-resharper
wp_id: 6549
original_url: https://compositecode.blog/2012/09/11/reasons-to-love-refactoring-with-resharper/
categories:
- .NET Bits
tags:
- c#
- refactor
- refactoring
- resharper
excerpt: 'It started like this. string responseValue; if (null == vcapResponse) { responseValue = message; } else { responseValue = vcapResponse.Description; } return responseValue; …and after a few alt+enter hits… return null == vcapResponse ? message : vcapResponse.Description; I ended up with that beauty. Oh yeah. 🙂 …and for today, …'
---

It started like this.

```csharp
string responseValue;

if (null == vcapResponse)
{
    responseValue = message;
}
else
{
    responseValue = vcapResponse.Description;
}

return responseValue;
```

…and after a few alt+enter hits…

```csharp
return null == vcapResponse ? message : vcapResponse.Description;
```

I ended up with that beauty. Oh yeah. 🙂

…and for today, that’s it. Whew!
