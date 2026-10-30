---
title: Kōans of Code
date: 2011-06-11 18:43:13 -0700
last_modified_at: 2011-06-11 18:43:13 -0700
permalink: /2011/06/11/koans-of-code/
slug: koans-of-code
wp_id: 3005
original_url: https://compositecode.blog/2011/06/11/koans-of-code/
categories:
- Code Katas
- How-to
- Ruby on Rails Bits
tags:
- kata
- koan
- learning
- ruby
excerpt: I’ve continued the Kōans, but there is one thing that won’t be noticeable from this blog entry. I however wanted to mention it. The first blog entry was worked through on an OS-X Apple Machine, the second on an Ubunta Linux Machine, and now I’m heading for this blog entry to be completed with Windows 7. It is of course completely irrelevant, but at the same time very relevant. 🙂 But enough about operating system awesomeness. Let’s take a look at the new gazillion Kōans that caught my note taking interest.
---

I’ve continued the Kōans, but there is one thing that won’t be noticeable from this blog entry. I however wanted to mention it. The first blog entry was worked through on an OS-X Apple Machine, the second on an Ubunta Linux Machine, and now I’m heading for this blog entry to be completed with  Windows 7. It is of course completely irrelevant, but at the same time very relevant.  🙂 But enough about operating system awesomeness. Let’s take a look at the new gazillion Kōans that caught my note taking.

```ruby
class AboutArrays < EdgeCase::Koan
  def test_creating_arrays
    empty_array = Array.new
    assert_equal Array, empty_array.class
    assert_equal 0, empty_array.size
  end
```

Easy peasy. Array.new creates a new empty array. Got it. An Array is the class type retrieved when calling empty\_array.class. Got it. The empty array has a size of zero, Got it.

```ruby
  def test_array_literals
    array = Array.new
    assert_equal [], array

    array[0] = 1
    assert_equal [1], array

    array[1] = 2
    assert_equal [1, 2], array

    array << 333
    assert_equal [1, 2, 333], array
  end
```

Ok, this one has some interesting bits in it. Having array[0] and array[1] assigned to a value of 1 and 2 seems standard operating practice for a language. This dual chevrons pointing into the array thing is a little more unique. This operator appears to take the value on the right, and put it onto the array’s stack. Simply, the double kick operator (or whatever it is called) puts the value on the next available array index position. Ok, cool. Got it.

```ruby
  def test_accessing_array_elements
    array = [:peanut, :butter, :and, :jelly]

    assert_equal :peanut, array[0]
    assert_equal :peanut, array.first
    assert_equal :jelly, array[3]
    assert_equal :jelly, array.last
    assert_equal :jelly, array[-1]
    assert_equal :butter, array[-3]
  end
```

Alright, got an array with 4 elements in it. First assert confirms that :peanut is the returned value from the first element in the array. The array.first call functionally does the same thing. The third assert gets the 3rd value in the array, keeping in mind a zero based index for the array, that gives us the 4th actual item in the list of items stored within the array. I love it, standard programmer weirdness. Why do programmers start with zero when nobody on earth starts a “list” of items with a zero. Blagh, whatever, that’s the reality of it. (That was, in a sense, somewhat rhetorical, I get the underlying reasons but that doesn’t help explain a zero based index to initial non-programmers.)

```ruby
  def test_slicing_arrays
    array = [:peanut, :butter, :and, :jelly]

    assert_equal [:peanut], array[0,1]
    assert_equal [:peanut, :butter], array[0,2]
    assert_equal [:and, :jelly], array[2,2]
    assert_equal [:and, :jelly], array[2,20]
    assert_equal [], array[4,0]
    assert_equal [], array[4,100]
    assert_equal nil, array[5,0]
  end
```

Slicing arrays again with the PB & J. With two values, the first thing I notice is that this is no multidimensional array. Two values within the square brackets means that you have a starting position and then a value of how many to retrieve. If there is a value like the fourth asset, starting at the 2nd position (3rd actual value) and taking the next 20 elements, basically retrieves whatever values are available, which in this case gets us 2 elements.

Now, I’m a slight bit perplexed though as to why nil is returned for something request nothing from the 5th starting point of the array versus the same being requested from the 4th starting point in the array. I’ll have to read up on that…

```ruby
  def test_arrays_and_ranges
    assert_equal Range, (1..5).class
    assert_not_equal [1,2,3,4,5], (1..5)
    assert_equal [1,2,3,4,5], (1..5).to_a
    assert_equal [1,2,3,4], (1...5).to_a
  end
```

Again, identifying the class object type is easy, a range of numbers is a Range Object. Check. A range stating 1..5 does not provide the numbers one through five. Calling to\_a on a range however does provide you those numbers. Doing the same thing to an array specified with three periods instead of two with the to\_a provides numbers one through four. That seems odd, but I got it.

```ruby
  def test_slicing_with_ranges
    array = [:peanut, :butter, :and, :jelly]

    assert_equal [:peanut, :butter, :and], array[0..2]
    assert_equal [:peanut, :butter], array[0...2]
    assert_equal [:and, :jelly], array[2..-1]
    assert_equal [:peanut, :butter, :and], array[0..-2]
  end
```

Slicing an array of four values, stating the starting and ending point with the syntax of a range, provides the elements based on the values associated with that range. I actually added an assert to this test to determine what exactly the negative values do. It appears that the array starts at the point of the first number, then follows a range from that until the negative number from the end of the array. So with 10 items, starting at point 2 and ending -2 from the end will retrieve the middle 6 elements. Strange, but I can see how this would be very useful.

```ruby
  def test_pushing_and_popping_arrays
    array = [1,2]
    array.push(:last)

    assert_equal [1,2,:last], array

    popped_value = array.pop
    assert_equal :last, popped_value
    assert_equal [1, 2], array
  end
```

Pop. Easy, get that last value. But wait a second, the array itself doesn’t have :last in it? Aha! Popping it not only gets that last value, but literally takes the value out of the array.

```ruby
  def test_shifting_arrays
    array = [1,2]
    array.unshift(:first)

    assert_equal [:first, 1, 2], array

    shifted_value = array.shift
    assert_equal :first, shifted_value
    assert_equal [1,2], array
  end

end
```

Ah, kind of like a popped value but shifted out of the array? Weird, this is a little confusing at first. I see what it is appearing to do, but figured a good read of the documentation would be good. I did a search on Google and the first hit is someone asking this question.

[What does Ruby’s Array Shift Do?](http://stackoverflow.com/questions/3718625/what-does-rubys-arrayshift-do)

From that quick read it appears that shift and unshift are used similar to pop and push in a stack (ala git, etc).

That answers that question. With that, I’m off to other realms.
