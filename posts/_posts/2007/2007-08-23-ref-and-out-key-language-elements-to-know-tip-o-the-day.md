---
title: '''ref'' and ''out'', Key Language Elements to Know :: Tip O'' The Day'
date: 2007-08-23 13:14:00 -0700
last_modified_at: 2007-08-23 13:14:00 -0700
permalink: /2007/08/23/ref-and-out-key-language-elements-to-know-tip-o-the-day/
slug: ref-and-out-key-language-elements-to-know-tip-o-the-day
wp_id: 435
original_url: https://compositecode.blog/2007/08/23/ref-and-out-key-language-elements-to-know-tip-o-the-day/
categories:
- Uncategorized Bits
tags: []
excerpt: The ‘ref’ and ‘out’ keywords for parameters are rarely used, so I thought they’d make a great tip o’ the day. Enjoy, and take it easy on the ‘ref’ and ‘out’ keywords. The ‘out’ keyword on a parameter basically is like making that variable an additional return type value. However, if the ‘out’ keyword is …
---

The ‘ref’ and ‘out’ keywords for parameters are rarely used, so I thought they’d make a great tip o’ the day.  Enjoy, and take it easy on the ‘ref’ and ‘out’ keywords.

The ‘out’ keyword on a parameter basically is like making that variable an additional return type value.  However, if the ‘out’ keyword is commonly used, you are probably in need of some code refactoring.

‘ref’ parameters on the other hand are passed into and out of a method, and are not required to be assigned prior to use in a method.  This is also one of the primary differences in the usage between ‘out’ and ‘ref’.

Check out the samples below that I nabbed from MSDN, they clarify well.  ![Smile [:)]](/emoticons/emotion-1.gif)

From [MSDN Sample](http://msdn2.microsoft.com/en-us/vcsharp/aa336814.aspx):

From the [MSDN Sample](http://msdn2.microsoft.com/en-us/vcsharp/aa336814.aspx) code:

‘ref’ Example

1 using System;

    2

    3 namespace ConsoleInterface

    4 {

    5     internal class RefExample

    6     {

    7         private static object FindNext(object value, object[] data, ref int index)

    8         {

    9             // NOTE: index can be used here because it is a ref parameter

   10             while (index < data.Length)

   11             {

   12                 if (data[index].Equals(value))

   13                 {

   14                     return data[index];

   15                 }

   16                 index += 1;

   17             }

   18             return null;

   19         }

   20

   21         private static void Main()

   22         {

   23             object[] data = new object[] {1, 2, 3, 4, 2, 3, 4, 5, 3};

   24

   25             int index = 0;

   26             // NOTE: must assign to index before passing it as a ref parameter

   27             while (FindNext(3, data, ref index) != null)

   28             {

   29                 // NOTE: that FindNext may have modified the value of index

   30                 Console.WriteLine(“Found at index {0}”, index);

   31                 index += 1;

   32             }

   33

   34             Console.WriteLine(“Done Find”);

   35         }

   36     }

   37 }

---

‘out’ Example

---

1 using System;

    2

    3 namespace ConsoleInterface

    4 {

    5     internal class OutExample

    6     {

    7         // Splits a string containing a first and last name separated

    8         // by a space into two distinct strings, one containing the first name and one containing the last name

    9

   10         private static void SplitName(string fullName, out string firstName, out string lastName)

   11         {

   12             // NOTE: firstName and lastName have not been assigned to yet.  Their values cannot be used.

   13             int spaceIndex = fullName.IndexOf(‘ ‘);

   14             firstName = fullName.Substring(0, spaceIndex).Trim();

   15             lastName = fullName.Substring(spaceIndex).Trim();

   16         }

   17

   18         private static void Main()

   19         {

   20             string fullName = “Yuan Sha”;

   21             string firstName;

   22             string lastName;

   23

   24             // NOTE: firstName and lastName have not been assigned yet.  Their values may not be used.

   25             SplitName(fullName, out firstName, out lastName);

   26             // NOTE: firstName and lastName have been assigned, because the out parameter passing mode guarantees it.

   27

   28             Console.WriteLine(“First Name ‘{0}’. Last Name ‘{1}'”, firstName, lastName);

   29         }

   30     }

   31 }
