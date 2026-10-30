---
title: SOLID Thoughts
date: 2010-04-06 13:22:27 +0000
last_modified_at: 2010-04-06 13:22:27 +0000
permalink: /2010/04/06/solid-thoughts/
slug: solid-thoughts
wp_id: 709
original_url: https://compositecode.blog/2010/04/06/solid-thoughts/
categories:
- Uncategorized Bits
tags: []
excerpt: SOLID came up again in discussion. What is SOLID? Well, glad you asked, because I am going to elaborate on the SOLID Principles a bit. Initial Concept S Single Responsibility Principle O Open/Closed Principle L Liskov Substitution Principle I Interface Segregation Principle D Dependency Inversion/Injection Principle The Single Responsibility Principle (SRP) is stated that every …
---

SOLID came up again in discussion.  What is SOLID?  Well, glad you asked, because I am going to elaborate on the SOLID Principles a bit.

|  |  |
| --- | --- |
| **Initial** | **Concept** |
| S | Single Responsibility Principle |
| O | Open/Closed Principle |
| L | Liskov Substitution Principle |
| I | Interface Segregation Principle |
| D | Dependency Inversion/Injection Principle |

The *[Single Responsibility Principle (SRP)](http://www.objectmentor.com/resources/articles/srp.pdf)* is stated that every object should have a single responsibility and should be entirely encapsulated by the class.  This helps keep cohesion.  Here is a short example, starting with a basic class.

```
public class Car
{
    decimal Gas;
    int Doors;
    int Speed;
    decimal RampJumpSpeed;
}
```

.csharpcode, .csharpcode pre
{
font-size: small;
color: black;
font-family: consolas, “Courier New”, courier, monospace;
background-color: #ffffff;
/\*white-space: pre;\*/
}
.csharpcode pre { margin: 0em; }
.csharpcode .rem { color: #008000; }
.csharpcode .kwrd { color: #0000ff; }
.csharpcode .str { color: #006080; }
.csharpcode .op { color: #0000c0; }
.csharpcode .preproc { color: #cc6633; }
.csharpcode .asp { background-color: #ffff00; }
.csharpcode .html { color: #800000; }
.csharpcode .attr { color: #ff0000; }
.csharpcode .alt
{
background-color: #f4f4f4;
width: 100%;
margin: 0em;
}
.csharpcode .lnum { color: #606060; }Now I will refactor a little bit to make it a bit more SRP friendly.

```
public class Car
{
    decimal Gas;
    int Speed;
}

public class DuneBuggy : Car
{
    decimal RampJumpSpeed;
}

public class EconomyCar : Car
{
    int Doors;
}
```

.csharpcode, .csharpcode pre
{
font-size: small;
color: black;
font-family: consolas, “Courier New”, courier, monospace;
background-color: #ffffff;
/\*white-space: pre;\*/
}
.csharpcode pre { margin: 0em; }
.csharpcode .rem { color: #008000; }
.csharpcode .kwrd { color: #0000ff; }
.csharpcode .str { color: #006080; }
.csharpcode .op { color: #0000c0; }
.csharpcode .preproc { color: #cc6633; }
.csharpcode .asp { background-color: #ffff00; }
.csharpcode .html { color: #800000; }
.csharpcode .attr { color: #ff0000; }
.csharpcode .alt
{
background-color: #f4f4f4;
width: 100%;
margin: 0em;
}
.csharpcode .lnum { color: #606060; }

What we end up with, instead of one class, is an abstract class and two classes that have their respective methods or properties to keep the responsibilities were they need to be.

The *[Open Closed Principle (OCP)](http://www.objectmentor.com/resources/articles/ocp.pdf)* is one of my favorites, which states simply, that you should be able to extend a classes behavior without modifying it.  There are a couple of ways one can extend a class, by inheritance, composition, or by proxy implementation.

The *[Liskov Substitution Principle (LSP)](http://www.objectmentor.com/resources/articles/lsp.pdf)* states that a derived class must be substitutable for their base classes.

The *[Dependency Inversion Principle (DIP)](http://www.objectmentor.com/resources/articles/dip.pdf)* states that one should depend on abstractions and not on concrete implementations.

Finally, the *[Interface Segregation Principle (ISP)](http://www.objectmentor.com/resources/articles/isp.pdf)* states that fine grain interfaces should be client specific.

So hope that helps with kicking off a basic understanding of SOLID Principles.  I will be following this entry up with some new bits in the near future related to good software design and practice.
