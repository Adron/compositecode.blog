---
title: 'Law of Demeter :: Tip O'' The Day'
date: 2007-06-21 11:44:00 -0700
last_modified_at: 2007-06-21 11:44:00 -0700
permalink: /2007/06/21/law-of-demeter-tip-o-the-day/
slug: law-of-demeter-tip-o-the-day
wp_id: 466
original_url: https://compositecode.blog/2007/06/21/law-of-demeter-tip-o-the-day/
categories:
- Uncategorized Bits
tags: []
excerpt: An important thing to remember when developing software is that readability and reliability are key to the future use and maintenance of the software. This is especially true in the code. One of the key laws that applies to this is the “Law of Demeter“. This key law is simply to assure that object graphs …
---

An important thing to remember when developing software is that readability and reliability are key to the future use and maintenance of the software.  This is especially true in the code.  One of the key laws that applies to this is the “[Law of Demeter](http://en.wikipedia.org/wiki/Law_Of_Demeter)“.  This key law is simply to assure that object graphs stay reasonable, code is reliable to call, and that friends speak to friends and not strangers.

> The **Law of Demeter (LoD)**, or **Principle of Least Knowledge** is a design guideline for developing [software](http://en.wikipedia.org/wiki/Software), particularly [object-oriented programs](http://en.wikipedia.org/wiki/Object-oriented_programming). The guideline was invented at [Northeastern University](http://en.wikipedia.org/wiki/Northeastern_University_%28Boston%2C_Massachusetts%29) in the fall of [1987](http://en.wikipedia.org/wiki/1987), and can be succinctly summarized as “Only talk to your immediate friends.” The fundamental notion is that a given object should assume as little as possible about the structure or properties of anything else (including its subcomponents).
>
> It is so named for its origin in the [Demeter Project](http://en.wikipedia.org/w/index.php?title=Demeter_Project&action=edit), an [adaptive programming](http://en.wikipedia.org/w/index.php?title=Adaptive_programming&action=edit) and [aspect-oriented programming](http://en.wikipedia.org/wiki/Aspect-oriented_programming) effort. This project was named in honor of [Demeter](http://en.wikipedia.org/wiki/Demeter), “distribution-mother” and [goddess](http://en.wikipedia.org/wiki/Goddess) of [agriculture](http://en.wikipedia.org/wiki/Agriculture), to signify a bottom-up philosophy of programming which is also embodied in the law itself.
>
> When applied to object-oriented programs, the Law of Demeter can be more precisely called the “Law of Demeter for Functions/Methods” (LoD-F). In this case, an object A can request a service (call a method) of an object instance B, but object A cannot “reach through” object B to access yet another object to request its services. Doing so would mean that object A implicitly requires greater knowledge of object B’s internal structure. Instead, B’s class should be modified if necessary so that object A can simply make the request directly of object B, and then let object B propagate the request to any relevant subcomponents. If the law is followed, only object B knows its internal structure.
>
> More formally, the Law of Demeter for functions requires that a method *M* of an object *O* may only invoke the methods of the following kinds of objects:
>
> 1. *O* itself
> 2. *M’*s parameters
> 3. any objects created/instantiated within *M*
> 4. *O’*s direct component objects
>
> In particular, an object should avoid invoking methods of a member object returned by another method.

Continuing on in the definition points out the obvious advantages and disadvantages:

> The advantage of following the Law of Demeter is that the resulting software tends to be more maintainable and adaptable. Since objects are less dependent on the internal structure of other objects, object containers can be changed without reworking their callers.
>
> A disadvantage of the Law of Demeter is that it requires writing a large number of small “wrapper” methods (sometimes referred to as Demeter Transmogrifiers) to propagate method calls to the components – these increase development time, increase space overhead, increase maintenance cost, and decrease performance. Automated tools exist to at least partially counteract these problems.

The advantages in my opinion far outweigh the disadvantages.  Agree?  Disagree?

[![kick it on DotNetKicks.com](http://www.dotnetkicks.com/Services/Images/KickItImageGenerator.ashx?url=http://adronbhall.com/blogs/technology__software_development/archive/2007/06/21/4890.aspx)](http://www.dotnetkicks.com/kick/?url=http://adronbhall.com/blogs/technology__software_development/archive/2007/06/21/4890.aspx)
