---
title: Consistency and Null Coalescing Operators
date: 2007-08-28 18:21:18 +0000
last_modified_at: 2007-08-28 18:21:18 +0000
permalink: /2007/08/28/consistency-and-null-coalescing-operators/
slug: consistency-and-null-coalescing-operators
wp_id: 433
original_url: https://compositecode.blog/2007/08/28/consistency-and-null-coalescing-operators/
categories:
- Uncategorized Bits
tags: []
excerpt: I’ve been trying to be more consistent lately with my blog entries, making at least one a day during the Monday through Friday work week. Well, that has sort of kind of maybe not really worked out too hot yet. But as I sat and thought, while reading through some blogs, I stumbled on Stuart …
---

I’ve been trying to be more consistent lately with my blog entries, making at least one a day during the Monday through Friday work week.  Well, that has sort of kind of maybe not really worked out too hot yet.  But as I sat and thought, while reading through some blogs, I stumbled on [Stuart Thompson’s blog](http://blogs.sftsrc.com/stuart/Default.aspx) where he mentions [Null-Coalescing Operators](http://blogs.sftsrc.com/stuart/archive/2007/08/10/46.aspx).  These suckers are great!

Per the example on his site, what we used to type when checking for nulls appeared something like this:

1 namespace SomeNamespace

    2 {

    3     public class Coalescing

    4     {

    5         private string emailAddress = string.Empty;

    6         private string parsedValue = string.Empty;

    7

    8         public string CheckForParsedValue()

    9         {

   10             if (parsedValue != null)

   11             {

   12                 emailAddress = parsedValue;

   13             }

   14             else

   15             {

   16                 emailAddress = “(Not provided)”;

   17             }

   18

   19             return emailAddress;

   20         }

   21     }

   22 }

but now will be coded in a super awesome elite looking way of:

10 string emailAddress = parsedValue ?? “(Not provided)”;

I’m stoked personally, and I think this makes a great tip o’ the day!  Of course it is kind of a “future” tip o’ the day.  Thanks Stuart pointing out this interesting tidbit of future C# coolness.

![Smile [:)]](/emoticons/emotion-1.gif)
