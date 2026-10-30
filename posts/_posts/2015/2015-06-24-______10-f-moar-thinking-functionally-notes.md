---
title: ______10 |> F# – Moar Thinking Functionally (Notes)
date: 2015-06-24 18:57:19 -0700
last_modified_at: 2015-06-24 18:57:19 -0700
permalink: /2015/06/24/______10-f-moar-thinking-functionally-notes/
slug: ______10-f-moar-thinking-functionally-notes
wp_id: 11294
original_url: https://compositecode.blog/2015/06/24/______10-f-moar-thinking-functionally-notes/
categories:
- .NET Bits
- F#
- How-to
tags:
- .NET
- f#
- fsharp
- functional programming
excerpt: 'More notes on the “Thinking Functionally” series. Previous notes are @ “_______1 |> F# – Getting Started, Thinking Functionally“. #6 Partial Application Breaking down functions into single parameter functions is the mathematically correct way of doing it, but that is not the only reason it is done — it also leads to a very powerful …'
image: /wp-content/uploads/2015/06/ah_f_256.png
---

More notes on the “[Thinking Functionally](http://fsharpforfunandprofit.com/series/thinking-functionally.html)” series. Previous notes are @ “[\_\_\_\_\_\_\_1 |> F# – Getting Started, Thinking Functionally](/2015/06/16/_______1-f-getting-started-thinking-functionally/)“.

## [#6 Partial Application](http://fsharpforfunandprofit.com/posts/partial-application/)

Breaking down functions into single parameter functions is the mathematically correct way of doing it, but that is not the only reason it is done — it also leads to a very powerful technique called partial function application.

For example:

```fsharp
let add42 = (+) 42 // partial application
add42 1
add42 3

[1;2;3] |> List.map add42

let twoIsLessThan = (<) 2 // partial application twoIsLessThan 1 twoIsLessThan 3 // filter each element with the twoIsLessThan function [1;2;3] |> List.filter twoIsLessThan

let printer = printfn "printing param=%i"

[1;2;3] |> List.iter printer
```

Each case a partially applied function above it can then be reused in multiple contexts. It can also fix function parameters.

```fsharp
let add1 = (+) 1
let add1ToEach = List.map add1   // fix the "add1" function

add1ToEach [1;2;3;4]

let filterEvens =
   List.filter (fun i -> i%2 = 0) // fix the filter function

filterEvens [1;2;3;4]
```

Then the following shows plug in behavior that is transparent.

```fsharp
let adderWithPluggableLogger logger x y =
    logger "x" x
    logger "y" y
    let result = x + y
    logger "x+y"  result
    result

let consoleLogger argName argValue =
    printfn "%s=%A" argName argValue

let addWithConsoleLogger = adderWithPluggableLogger consoleLogger
addWithConsoleLogger  1 2
addWithConsoleLogger  42 99

let popupLogger argName argValue =
    let message = sprintf "%s=%A" argName argValue
    System.Windows.Forms.MessageBox.Show(
                                 text=message,caption="Logger")
      |> ignore

let addWithPopupLogger  = adderWithPluggableLogger popupLogger
addWithPopupLogger  1 2
addWithPopupLogger  42 99
```

**Designing Functions for Partial Application**

Sample calls to the list library:

```fsharp
List.map    (fun i -> i+1) [0;1;2;3]
List.filter (fun i -> i>1) [0;1;2;3]
List.sortBy (fun i -> -i ) [0;1;2;3]
```

Here are the same examples using partial application:

```fsharp
let eachAdd1 = List.map (fun i -> i+1)
eachAdd1 [0;1;2;3]

let excludeOneOrLess = List.filter (fun i -> i>1)
excludeOneOrLess [0;1;2;3]

let sortDesc = List.sortBy (fun i -> -i)
sortDesc [0;1;2;3]
```

Commonly accepted guidelines to multi-parameter function design.

1. Put earlier: parameters ore likely to be static. The parameters that are most likely to be “fixed” with partial application should be first.
2. Put last: the data structure or collection (or most varying argument). Makes it easier to pipe a structure or collection from function to function. Like:

   ```fsharp
   let result =
      [1..10]
      |> List.map (fun i -> i+1)
      |> List.filter (fun i -> i>5)
   ```
3. For well-known operations such as “subtract”, put in the expected order.

Wrapping BCL Function for Partial Application

Since the data parameter is generally last versus most BCL calls that have the data parameter first, it’s good to wrap the BCL.

```fsharp
let replace oldStr newStr (s:string) =
  s.Replace(oldValue=oldStr, newValue=newStr)

let startsWith lookFor (s:string) =
  s.StartsWith(lookFor)
```

Then pipes can be used with the BCL call in the expected way.

```fsharp
let result =
     "hello"
     |> replace "h" "j"
     |> startsWith "j"

["the"; "quick"; "brown"; "fox"]
     |> List.filter (startsWith "f")
```

…or we can use function composition.

```fsharp
let compositeOp = replace "h" "j" >> startsWith "j"
let result = compositeOp "hello"
```

**Understanding the Pipe Function**

The pipe function is defined as:

```fsharp
let (|>) x f = f x
```

It allows us to put the function argument in front of the function instead of after.

```fsharp
let doSomething x y z = x+y+z
doSomething 1 2 3
```

If the function has multiple parameters, then it appears that the input is the final parameter. Actually what is happening is that the function is partially applied, returning a function that has a single parameter: the input.

```fsharp
let doSomething x y  =
   let intermediateFn z = x+y+z
   intermediateFn        // return intermediateFn

let doSomethingPartial = doSomething 1 2
doSomethingPartial 3
3 |> doSomethingPartial
```

## [#7 Function Associativity and Composition](http://fsharpforfunandprofit.com/posts/function-composition/)

**Function Associativity**

This…

```fsharp
let F x y z = x y z
```

…means this…

```fsharp
let F x y z = (x y) z
```

Also three equivalent forms.

```fsharp
let F x y z = x (y z)
let F x y z = y z |> x
let F x y z = x <| y z
```

**Function Composition**

Here’s an example

```fsharp
let f (x:int) = float x * 3.0  // f is int->float
let g (x:float) = x > 4.0      // g is float->bool
```

We can create a new function h that takes the output of “f” and uses it as the input for “g”.

```fsharp
let h (x:int) =
    let y = f(x)
    g(y)                   // return output of g
```

A much more compact way is this:

```fsharp
let h (x:int) = g ( f(x) ) // h is int->bool

//test
h 1
h 2
```

These are notes, to read more check out the [Function Composition](http://fsharpforfunandprofit.com/posts/function-composition/).

##
