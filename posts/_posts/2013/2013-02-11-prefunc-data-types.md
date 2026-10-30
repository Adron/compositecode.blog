---
title: 'Distributed Coding Prefunc: Some Basic Erlang & Erlang Shell Basics'
date: 2013-02-11 16:56:07 -0800
last_modified_at: 2013-02-11 16:56:07 -0800
permalink: /2013/02/11/prefunc-data-types/
slug: prefunc-data-types
wp_id: 7713
original_url: https://compositecode.blog/2013/02/11/prefunc-data-types/
categories:
- Erlang
- How-to
tags:
- code
- Distributed Coding Prefunc
- erlang
- programming
excerpt: 'The first few parts of this series include: Up and Running With Erlang Installing QuickCheck for Great Testing Ubuntu Erlang Dev & EUnit This continues the series, with the intent of getting to “Distributed Coding” with this all ramping up around Erlang and distributed programing in general. In this entry we’ll jump into some of …'
---

[![Erlang Logo](/images/adronhall.smugmug.com/Software/Misc-Images/Just-Icons-and-Bits/i-rnNZZNH/0/O/Erlang_logo.png)](http://www.erlang.org/)The first few parts of this series include:

- [Up and Running With Erlang](/2012/12/28/distributed-coding-prefunc-up-and-running-with-erlang/)
- [Installing QuickCheck for Great Testing](/2013/01/14/distributed-coding-prefunc-installing-quickcheck-for-great-testing/)
- [Ubuntu Erlang Dev & EUnit](/2013/02/02/distributed-coding-prefunc-ubuntu-erlang-dev-eunit/)

This continues the series, with the intent of getting to “Distributed Coding” with this all ramping up around Erlang and distributed programing in general. In this entry we’ll jump into some of the basics of Erlang and the shell that we can use to test and write some code.

## Erlang Basics : The Shell & Some Integers

Before getting to deep into things, here’s some basic shell usage commands and integers to get a feel for the Erlang shell. To start the shell just type erl, which will present the following in the terminal.

```erlang
$ erl
Erlang R15B01 (erts-5.9.1) [source] [smp:4:4] [async-threads:0] [hipe] [kernel-poll:false]

Eshell V5.9.1  (abort with ^G)
1>
```

To exit the shell just type “q().” and hit enter like this.

```erlang
$ erl
Erlang R15B01 (erts-5.9.1) [source] [smp:4:4] [async-threads:0] [hipe] [kernel-poll:false]

Eshell V5.9.1  (abort with ^G)
1> q().
ok
2> $
```

It’ll execute a second line that will dump you back out to the terminal. One thing to note, is that when you execute “q().” it drops to a second line numbered two above. If we start the shell back up again and type in some actual code we’ll see that the numbers increment. The idea is similar to each line of code in a code file.

Start up the shell again and type the following.

```erlang
$ erl
Erlang R15B01 (erts-5.9.1) [source] [smp:4:4] [async-threads:0] [hipe] [kernel-poll:false]

Eshell V5.9.1  (abort with ^G)
1> q().
ok
2> Adrons-MacBook-Air-2:erlangMagic adronhall$ clear
Adrons-MacBook-Air-2:erlangMagic adronhall$ erl
Erlang R15B01 (erts-5.9.1) [source] [smp:4:4] [async-threads:0] [hipe] [kernel-poll:false]

Eshell V5.9.1  (abort with ^G)
1> -69.
-69
2> 2#1212
2> 2#1212.
* 1: syntax error before: 212
2> 2#1010.
10
3> $A.
65
4> $B.
66
5> $a.
97
6> 2*2+100.
104
7>
```

What I’ve done here is enter some values, primarily all integers. These integers, on the first line is a negative integer. By entering a “.” at the end, the lines executes and returns the value. In this case, the value is “-69”.

The second line, I entered “2#1212” without entering a period to finish the line of code. Thus, nothing executes.

The third line I entered the same thing as the second, “2#1212” which is not valid, giving us a syntax error. On the next line I tweak my value just a bit, entering a valid hexadecimal number “2#1010” with the appropriate period at the end. The line executes and it displays the decimal integer “10”.

So far at this point, this shows us several things:

- Every line must end with a period to execute.
- We’ve seen a negative integer, a positive hexadecimal integer and an invalid integer and the error that throws “\* 1: syntax error before: 212”.
- We’ve seen that when the line in the shell successfully executes we get the next incremental line, such as “-69.” was on the first line, the first successful second line was the “2#1010.” value and as we move through each line above the code line increases.
- A valid integer includes -69, but also includes a hexadecimal representation of an integer such as “#2#1010”.

Moving beyond these values the “$A”, “$B” and “$a” are all ASCII representations and return their numeral values.

On line six I actually perform a basic calculator type multiplication and addition of integer values, which returns the integer value 104.

Now that we have the shell start and stop figured out, that gives us a platform in which to start stepping through some of the basics of Erlang.

## Erlang Floats

Above we’ve seen how regular integers are represented such as 2, 100 or -69 along with hexadecimal and ASCII numeric representations. For floats, we’re looking at similar uses. Spool up the shell again and try out these examples.

```erlang
1> 21.21.
21.21
2> -1234.1234.
-1234.1234
3> 3042.1.
3042.1
4> 650.21
4> 650.21.
* 2: syntax error before: 650.21
4> 650.21
4> 650.21.
* 2: syntax error before: 650.21
4> 650.21.
650.21
```

Lines 1-3 show some standard floats. On the first part of line four I left off the period to show that it won’t accept the line, even with a period in it, because of the numbers after that period. In that second line number four I’ve added the period, but it throws a syntax error.

Then note I did the exact same thing again, to show that entering a float and then adding the period, will still leave the float broken because of the way the Erlang compiler is waiting to execute the code. It’s almost like the compiler sees “650.21650.21” which of course doesn’t mean anything. However on the fifth line of the number four lines, I finally get a good execution and it displays the float I’ve entered “650.21”. Be sure when you’re fixing values like this, the compiler could be stuck in mid execution, because without the period at the very end, being the last character on the line, the compiler is still waiting for the period to actually start the execution.

## Mathematical Operators, You Know Those Things That Help Math Explain the Universe!

Erlang has the standard operators that you’re used to, especially if you’ve done anything with a language based around C syntax such as JavaScript, Java, C#, C++, Objective-C… well, pretty much every regularly used static typed language and more. In functional languages these operators are pretty common too. If any don’t look familiar, be sure to get intimate with them. You’ll find them all over Erlang code.

The + and – characters act as addition and subtraction, but also as unary operators. In order of precedence, the unary operations of the + and – have the highest precedence and the addition and subtraction usage of the + and – have the lowest precedence.

The \* and / signify multiplication and division. They’re precedence is just below that of the unary operators of + and -.

Two that are a slight bit unique, is the usage of “div” and “rem” for division and remainder, for integer numbers. This begs to bring up the point that whenever an integer is involved in multiplication, division, addition, subtraction or other operations, it is coerced into a float when being operated on against another float. Such as 2 + 3.47 would mean that 2 is turned into a float before it is added to 3.47.

Here’s some examples of operations occurring between numbers via the shell.

```erlang
$ erl
Erlang R15B01 (erts-5.9.1) [source] [smp:4:4] [async-threads:0] [hipe] [kernel-poll:false]

Eshell V5.9.1  (abort with ^G)
1> +15.
15
2> +2.
2
3> -11.
-11
4> 11 div 5.
2
5> 12 div 5
5> .
2
6> 15 div 5.
3
7> 14 div 5.
2
8> (12 + 345) div 12.
29
9> (3+2)/5.
1.0
10> 2*3*4.12.
24.72
11> 1+1+1+1+13+-2.
15
12> 2/3 + 3/4 -- (1/2 + 2/3) -- 1.
-0.75
13> 14 rem 5.
4
14>
```

These examples show a number of effects of how the operators work. Notable is how everything looks very much like simple math being done. This is one of the more readable aspects of Erlang. Note also that the rounding generally goes down.
