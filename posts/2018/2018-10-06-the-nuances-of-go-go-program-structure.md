---
title: 'The Nuances of Go: Go Program Structure'
date: 2018-10-06 15:54:20 -0700
last_modified_at: 2018-10-06 15:55:47 -0700
permalink: /2018/10/06/the-nuances-of-go-go-program-structure/
slug: the-nuances-of-go-go-program-structure
wp_id: 14657
original_url: https://compositecode.blog/2018/10/06/the-nuances-of-go-go-program-structure/
categories:
- golang
tags:
- assignments
- data types
- declarations
- go
- golang
- keywords
- programming
- types
excerpt: Talking About Types, Variables, Pointers, and More In my endeavor to get more of the specifics of Go figured out, I’ve been diving a bit more in depth to each of the specific features, capabilities, and characteristics of the language. I’ll be doing the same for Cassandra over the coming months and producing a blog …
image: /wp-content/uploads/2018/10/gopher-metal-head.jpg
---

## Talking About Types, Variables, Pointers, and More

In my endeavor to get more of the specifics of Go figured out, I’ve been diving a bit more in depth to each of the specific features, capabilities, and characteristics of the language. I’ll be doing the same for Cassandra over the coming months and producing a blog entry series about it. This new series however is about Go, and this first in the series is about types, variables, pointers, and naming of these things. Enjoy.

### Reserved Words, Keywords & Related Systemic Parts of Go

First off let’s talk about the reserved words in Go. The list includes 25 keywords that can’t be used as variables or names of functions or anything like that. This list includes:

|  |  |  |  |
| --- | --- | --- | --- |
| if | import | interface | map |
| select | return | range | package |
| struct | switch | type | var |
| for | func | go | goto |
| default | defer | else | fallthrough |
| case | const | chan | continue |
| break |  |  |  |

Beyond these 25 keywords there are also some predeclared names that can be but usually shouldn’t be used for naming. These include:

**Constants**

|  |  |  |  |
| --- | --- | --- | --- |
| true | false | iota | nil |

**Types**

|  |  |  |  |
| --- | --- | --- | --- |
| int | int8 | int16 | int32 |
| int64 | uint | uint8 | uint16 |
| uint32 | uint64 | uintptr | float32 |
| float64 | complex128 | complex64 | bool |
| byte | rune | string | error |

**Functions**

|  |  |  |  |
| --- | --- | --- | --- |
| make | len | cap | new |
| append | copy | close | delete |
| complex | real | imag | panic |
| recover |  |  |  |

When declaring an entity within a function, it’s scope is limited to that function. When declaring it outside of the function it is available to the contents of the package it is declared inside of. The case of the first letter also has the effect of allowing access within or across package boundaries. If the name begins with an upper case character it is exported for other packages. Package names themselves are always lower case however.

### Camel Casing

It’s also important to know about the emphasis and standard within Go to use camel casing. Except it appears that for acronyms and such like; HTML, XML, JSON, or such things, it is routine to use names like HTMLthingy, XMLjunkHere, or rockStarJSON. Go is somewhat particular about these types of things, so it is extremely important to use the Go format standards. To help with this, there’s also the gofmt function, but it’s always good to just use the proper formatting during writing of the code anyway.

### The Four Declarations

The four declarations are kind of like the four horsement, except not really. Forget that analogy as it was already going nowhere. The four declarations include:

|  |  |  |  |
| --- | --- | --- | --- |
| var | const | type | func |

Here are some code samples of various declarations. First use of the func. In any new Go program there’s always the main() function. Declared like this.

```javascript
func main() {
    // Stuff goes here.
}
```

Another example of a function declaration with parameters passed and expected results to return. The signature works like func followed by the name of the function, then in parenthesis parameter name followed by its type, for as may parameters as is needed. Then after the parenthesis the type of the expected result of the function. Of course, if no result is expected to be returned, then there would be no tpe specified here. Just as if no parameters, the parenthesis would still be used but no parameters specified.

```javascript
func doSomeComputation(someValue float64, anotherFloaty float64) float64 {
    return someValue * anotherFloat
}
```

Using the var for declaration of variables looks like this.

```javascript
var f = 212.0
var result = 2 + 2
var celsius = (f -- 32) * 5 / 9
```

Variable types can be defined in this way. Using var keyword, followed by the variable name, then followed by its type, and then if desired assigned via = and then the specific value or function with a result to assign to the variable.

*var name type = expression*

Without an assignment, the variable is simply created with the intent of assigning a value later. Such as these variable declarations.

```javascript
var f float32
var result float64
var celsius float64
var someVariable int
var junk string
```

A shorter version of the creation and assignment of variables looks like this. It however can only be used within a function.

*name := expression*

Actual use of this shorter version would look like this.

```javascript
f := 212.0
randomStuff := rand.Float64()
wordContent := "This is some character string nonsense."
```

One can also do some other tricks with this shorter method of assignment. Let’s say some variables are needed that will have integers assigned to them. You could set up the variables with values like this. I’ve noticed some get a bit confused about this and tuple assignments, this is not the same thing. This merely gives you three variables: k, l, and m and assigns the values 0, 1, and 2 to the respective variable.

```javascript
k, l, m := 0, 1, 2
```

It’s also important to note, a short declaration doesn’t always declare all of the variables on the left-hand side. Some, if already declared in the same lexical block, it then acts as an assignment to the variables instead.

Declaring a constant value with const would look like this.

```javascript
const fahrenheitBoiling = 212.0
```

### Pointers

A variable holds a particular value, where as a pointer holds the address in memory of a particular value. Sometimes, it gets a bit difficult to mentally keep track of pointers, so let’s look at a few examples. First I’ll start with a plain old variable.

```javascript
someVariable := "The original value of this variable."
```

Then I’ll add another variable, which will point at the address and respective value of someVariable.

```javascript
someVariable := "The original value of this variable."
anotherVariable := &someVariable
fmt.Println(*anotherVariable)
```

In this situation what does the fmt.Println(\*anotherVariable) function print out? The result would be “The original value of this variable.” because anotherVariable is a variable that points to the value of someVariable. Which means anotherVariable doesn’t take the resources that someVariable does, but merely points to it.

The reasoning here is, if you have variable for example that stores a very large value in memory. One can merely point to that data with a pointer and the large value doesn’t have to change it’s memory space. Imagine if that variable were a gigabyte of data and it had to be moved every time something needed referenced or calculated with it, with a pointer we don’t have to move it. It can be used in various ways without it getting shifted around.

Now if I take the pointer value anotherVariable and assign it a value, like this.

```javascript
*anotherVariable = "42"
```

Then what happens? The pointer now is re-allocated and assigned the new value of “42”. It no longer references the address space of the pointer and instead now has the value 42 assigned to the variable.

### The Fancy `new` Function

There’s also another function, a built-in one, that creates a variable. Using the expression new(type) will create an unnamed variable of type, initializes it, and returns the address of the value of type. In pointer speak, it’d be \*type. Here are some examples.

```javascript
pinto := new(int)
fmt.Println(*pinto)
```

This code will create a variable of type int, then initialize the value to zero since it is an int. Let’s say we want to actually give it a value after it’s created though. We could assign pinto like this.

```javascript
*pinto = 42
fmt.Println(*p)
```

This will then print out the value 42, of type integer. Note, this new is just sugar, a syntactical convenience feature really. They can be useful however, and there are a few caveats that need to be noted. For example, check out this gotcha.

If I declare two new values using new.

```javascript
firstThing := new(int)
secondThing := new(int)
fmt.Println(firstThing == secondThing)
```

In this case, the firstThing and secondThing don’t actually match, because the comparison is on the address space, and they’re different address spaces!

Alright, that’s it for now, just a few important nuances around how variables, pointers, and Go features work.
