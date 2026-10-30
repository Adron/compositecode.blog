---
title: Kata Kickin’ Some Prime Numbers
date: 2010-06-16 13:46:00 -0700
last_modified_at: 2010-07-01 21:49:49 -0700
permalink: /2010/06/16/kata-kickin-some-prime-numbers/
slug: kata-kickin-some-prime-numbers
wp_id: 31
original_url: https://compositecode.blog/2010/06/16/kata-kickin-some-prime-numbers/
categories:
- Code Katas
- How-to
tags:
- kata
excerpt: Lately I have been interviewing people for prospective positions in the company I work for. In the various questions that I and others pose during these interviews one popped up as a prospective Kata. The challenge is really quit simple, “Write a method that would take a int and check if it is a prime number.” The following snippet is what I came up with.
---

Lately I have been interviewing people for prospective positions in the company I work for.  In the various questions that I and others pose during these interviews one popped up as a prospective Kata.  The challenge is really quit simple, “Write a method that would take a int and check if it is a prime number.”  The following snippet is what I came up with.

```csharp
protected bool IsPrime(int theNumber)
{
    bool isPrime = true;

    int theHalf = theNumber / 2;

    for (int i = 2; i < theHalf; i++)
    {
        var remainder = theNumber % i;
        if (remainder == 0)
        {
            isPrime = false;
            break;
        }
    }

    return isPrime;
}
```

The next idea that popped up was to find X prime number in order.  As the answer a question like, “What is the 6th prime number?”  I came up with the following method for that.

```csharp
protected int GetPrimeByPosition(int position)
{
    int counter = 1;
    int thePosition = 0;
    while (true)
    {
        if(IsPrime(counter))
        {
            if(thePosition == position)
                return counter;
            thePosition++;
        }

        counter++;
    }
}
```

In the end the Kata is a simple 2 step problem.

1. Write a method that determines if an int is a prime number.  i.e. “Is 5 a prime number?”
2. Write a method that determines the prime number based on X order.  i.e. “What is the 3rd prime number?”

So based on these two steps, what would be some other steps to add to this Kata?  What are some other good interview questions that are short and simple for prospective employees to code through?
