---
title: 'Generics :: Tip O'' The Day'
date: 2007-06-10 13:03:48 +0000
last_modified_at: 2007-06-10 13:03:48 +0000
permalink: /2007/06/10/generics-tip-o-the-day/
slug: generics-tip-o-the-day
wp_id: 469
original_url: https://compositecode.blog/2007/06/10/generics-tip-o-the-day/
categories:
- Uncategorized Bits
tags: []
excerpt: Many people find Generics confusing. I hope that I can add to some confusion reduction with a quick demonstration of some standard Generics usages in the C# .NET 2.0 world. The type-safety of C# prevents potential errors by catching them at compile time. Every variable in C# has a defined type. When you give the …
---

Many people find Generics confusing.  I hope that I can add to some confusion reduction with a quick demonstration of some standard Generics usages in the C# .NET 2.0 world.

The type-safety of C# prevents potential errors by catching them at compile time.  Every variable in C# has a defined type.  When you give the object an assignment the compiler checks if it the action is a valid.  If the assignment isn’t valid, BOOM, you get a notification.

Now a major problem comes up when you try to use collections in pre-generics C#.  The collection objects in C# are typed to hold actual .NET Framework objects.  Since anything goes in, there is no way to provide type checking.  Compounding this situation is the fact that each object getting pulled out of the collection then needs to be cast.  This creates some nasty, bloated looking code, especially once you start churning out all the collections themselves.

So today’s tip is simply to remember that generics are your friend!  No more nasty ole’ pre-C# 2.0 collections.  Generics, generics, generics!  To check out more about Generics, get the low down, and see how generics are utilized in .NET Framework for reflection, arrays, collections, serialization, and even remoting check out [Microsoft](http://www.microsoft.com/en/us/default.aspx)‘s [MSDN](http://msdn2.microsoft.com/en-us/default.aspx) [Section on Generics](http://msdn2.microsoft.com/en-us/library/ms379564(vs.80).aspx).  For more information specifically on what a generic check out this particular [MSDN](http://msdn2.microsoft.com/en-us/default.aspx) [page](http://msdn2.microsoft.com/en-us/library/ms172193.aspx).

![Smile [:)]](/emoticons/emotion-1.gif)
