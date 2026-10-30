---
title: _______1 |> F# – Getting Started, Thinking Functionally (Notes)
date: 2015-06-16 16:23:51 -0700
last_modified_at: 2015-06-20 23:27:56 -0700
permalink: /2015/06/16/_______1-f-getting-started-thinking-functionally/
slug: _______1-f-getting-started-thinking-functionally
wp_id: 11115
original_url: https://compositecode.blog/2015/06/16/_______1-f-getting-started-thinking-functionally/
categories:
- F#
- How-to
tags:
- functional programming
- functional thinking
- mathematics
excerpt: Recently I took the plunge into writing F# on OS-X and Linux (Ubuntu specifically). This is the first of a new series I’m starting (along with my other ongoing series on JavaScript workflow and practices). In this article particularly I’m just going to provide an overview and notes of key paradigms in functional programming. Most of these …
image: /wp-content/uploads/2015/06/ah_f_256.png
---

Recently I took the plunge into writing F# on OS-X and Linux (Ubuntu specifically). This is the first of a new series I’m starting (along with my other ongoing series on JavaScript workflow and practices). In this article particularly I’m just going to provide an overview and notes of key paradigms in functional programming. Most of these notes are derived from a great series called “[Thinking Functionally](http://fsharpforfunandprofit.com/series/thinking-functionally.html)“.

## [#1 Thinking Functionally: Introduction](http://fsharpforfunandprofit.com/posts/thinking-functionally-intro/)

This is the article that kicks off the series. The emphasis is focused around realizing that a different way of thinking needs applied when using a functional language. The difference between functional thinking and imperative. The key topics of the series includes:

- Mathematical Functions
- Functions and Values
- Types
- Functions with Multiple Parameters
- Defining Functions
- Function Signatures
- Organizing Functions

## [#2 Mathematical Functions](http://fsharpforfunandprofit.com/posts/mathematical-functions/)

Functional programming, its paradigms and its origins, are all rooted in mathematics. A mathematical function looks something like this:

Add1(x) = x + 1

- The set of values that can be used as input to the function is called the *domain*.
- The set of possible output values from the function is called the *range*.
- The function is said to *map* the *domain* to the *range*.

If F# the definition would look like this.

```fsharp
let add1 x = x + 1
```

The signature of the function would look like this.

```fsharp
val add1 : int -> int
```

**Key Properties of Mathematical Functions**

- A function always gives the same output value for a given input value.
- A function has no side effects.

**Pure functions**

- They are trivially parallelizable.
- I can use a function lazily.
- A function only needs to be evaluated once. (i.e. memoization)
- The function can be evaluated in any order.

**Prospectively “Unhelpful” properties of mathematical functions**

- The input and output values are immutable.
- A function always has exactly one input and one output

## [#3 Function Values and Simple Values](http://fsharpforfunandprofit.com/posts/function-values-and-simple-values/)

Looking at this function again:

```fsharp
let add1 x = x + 1
```

The x means:

- Accept some value from the input domain.
- Use the name “x” to represent that value so that we can refer to it later.

It is also referred to as x is bound to the input value. In this binding it will only ever be that input value. This is not an assignment of a variable. Emphasis on the fact that there are no “variables”, only values. This is a critical part of functional thinking.

**Function Values:** this is a value that provides binding for a function to a name.

**Simple Values:** This is what one might think of as constants.

```fsharp
let c = 5
```

**Simple Values vs. Function Values**

Both are bound to names using the keyword *let*. The key difference is a function needs to be application to an argument to get a result, and a simple value doesn’t, as it is the value it is.

**“Values” vs. “Objects”**

In F# most things are referred to as “values”, contrary to “objects” in C# (or other languages like JavaScript for that matter). A value is just a member of a domain, such as a domain of ints, string, or functions that map ints to strings. In theory a value is immutable and has no behavior attached to it. However in F#, even some primitive values have some object-like behavior such as calling a member or property with dot notation syntax like “theValue”.Length or something similar.

**Naming Values**

Most of the naming is the general ruleset that applies to practically every language. However there is one odd feature that comes in handy in some scenarios. Let’s say you want to have a name such as “this is my really long and flippantly ridiculous name” for a domain. Well, what you can use is the “this is my really long and flippantly ridiculous name“ to have that be the name. It’s a strange feature, but I’ll cover more of it in subsequent articles.

In F# it is also practice to name functions and values with camel case instead of pascal case (camelCase vs. PascalCase).

## [#4 How Types Work with Functions](http://fsharpforfunandprofit.com/posts/how-types-work-with-functions/)

Function signatures look like this, with the arrow notation.

```fsharp
val functionName : domain -> range
```

Example functions:

```fsharp
let intToString x = sprintf "x is %i" x  // format int to string
let stringToInt x = System.Int32.Parse(x)
```

Example function signatures:

```fsharp
val intToString : int -> string
val stringToInt : string -> int
```

This means:

- intToString has a domain of int which it maps onto the range string.
- stringToInt has a domain of string which it maps onto the range int.

**Primitive Types**

Standard known types you’d expect: string, int, float, bool, char, byte, etc.

**Type Annotations**

Sometimes type might not be inferred, if that is the case, the compiler can take annotations to resolve type.

```fsharp
let stringLength (x:string) = x.Length
let stringLengthAsInt (x:string) :int = x.Length
```

**Function Types as Parameters**

A function that takes other functions as parameters, or returns a function, is called a higher-order function (sometimes abbreviated as HOF).

Example:

```fsharp
let evalWith5ThenAdd2 fn = fn 5 + 2
```

The signature looks like:

```fsharp
val evalWith5ThenAdd2 : (int -> int) -> int
```

Looking at an example executing. The example:

```fsharp
let times3 x = x * 3
evalWith5ThenAdd2 times3
```

The signature looks like:

```fsharp
val times3 : int -> int
val it : int = 17
```

Also these are very sensitive to types, so beward.

```fsharp
let times3float x = x * 3.0
evalWith5ThenAdd2 times3float
```

Gives an error:

```fsharp
error FS0001: Type mismatch. Expecting a int -> int but
              given a float -> float
```

**Function as Output**

A function value can also be the output of a function. For example, the following function will generate an “adder” function that adds using the input value.

```fsharp
let adderGenerator numberToAdd = (+) numberToAdd
```

**Using Type Annotations to Constrain Function Types**

This example:

```fsharp
let evalWith5ThenAdd2 fn = fn 5 +2
```

Becomes this:

```fsharp
let evalWith5AsInt (fn:int->int) = fn 5
```

…or maybe this:

```fsharp
let evalWith5AsFloat (fn:int->float) = fn 5
```

**The “unit” Type**

When a function returns no output, it still requires a range, and since there isn’t a void function in mathematical functions this supplants the void as return output. This special range is called a “unit” and has one specific value only, a “()”. It is similar to a void type or a null in C# but also is not, in that it is the value “()”.

**Parameterless Functions**

For a [WAT](https://www.destroyallsoftware.com/talks/wat) moment here, parameterless functions come up. In this example we might expect “unit” and “unit”.

```fsharp
let printHello = printf "hello world"
```

But what we actually get is:

```fsharp
hello world
val printHello : unit = ()
```

Like I said, a very [WAT](https://www.destroyallsoftware.com/talks/wat) kind of moment. To get what we expect, we need to force the definition to have a “unit” argument, as shown.

```fsharp
let printHelloFn () = printf "hello world"
```

Then we get what we expect.

```fsharp
val printHelloFn : unit -> unit
```

So why is this? Well, you’ll have to dive in a little deeper and check out the [F# for fun and profit](http://fsharpforfunandprofit.com/) “[Thinking Functional](http://fsharpforfunandprofit.com/series/thinking-functionally.html)” entry on “[How Types Work with Functions](http://fsharpforfunandprofit.com/posts/how-types-work-with-functions/)” for the full low down on that. Suffice it I’ve documented how you get what you would expect, the writer on the site goes into the nitty gritty of what is actually happening here. Possibly, you might have guessed what is happen already. There is also some strange behavior that takes place with [forcing unit types with the ignore function](http://fsharpforfunandprofit.com/posts/how-types-work-with-functions/) that you may want to read on that article too, but if you’re itching to move on, and get going faster than digging through all of this errata, keep going. I’m going to jump ahead to the last section I want to cover for this blog entry of notes, currying.

## [#5 Currying](http://fsharpforfunandprofit.com/posts/currying/)

[![Haskell Curry](https://photos.adron.me/Software/Software-Development/Functional-Bits/i-5DfnVgK/0/O/haskell.jpg)](https://en.wikipedia.org/wiki/Haskell_Curry)

*Haskell Curry*

Breaking multi-parameter functions into smaller one-parameter functions. The way to write a function with more than one parameter is to use a process called currying. For more history on this check out [Haskell Curry](https://en.wikipedia.org/wiki/Haskell_Curry) the mathematician to dive deep into his work (*which also covers a LOT of other things beside merely currying, like combinatory logic and Curry’s paradox for instance*).

Basic example:

```fsharp
let printTwoParameters x y =
   printfn "x=%i y=%i" x y
```

This of course looks neat enough right? Well, if we look at the compiler rewrite, it gets rather interesting.

```fsharp
let printTwoParameters x =
   let subFunction y =
      printfn "x=%i y=%i" x y
   subFunction
```
