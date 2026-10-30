---
title: More Code Kōans
date: 2011-06-07 05:00:29 -0700
last_modified_at: 2011-06-07 13:47:31 -0700
permalink: /2011/06/07/more-code-koans/
slug: more-code-koans
wp_id: 2957
original_url: https://compositecode.blog/2011/06/07/more-code-koans/
categories:
- Code Katas
- How-to
- Ruby on Rails Bits
tags: []
excerpt: This is a continuation of my effort to get through all of the Ruby Kōans. def test_creating_arrays empty_array = Array.new assert_equal Array, empty_array.class assert_equal 0, empty_array.size end Creating a new array, just use Array.net. That I like. 🙂 Next assert verifies that the class is an Array. The third assert verifies that we have an empty array. That works, very logical, very array like…
---

This is a continuation of my effort to get through all of the Ruby Kōans.

```ruby
def test_creating_arrays
  empty_array = Array.new
  assert_equal Array, empty_array.class
  assert_equal 0, empty_array.size
end
```

Creating a new array, just use Array.net. That I like. 🙂 Next assert verifies that the class is an Array. The third assert verifies that we have an empty array. That works, very logical, very array like.

```ruby
def test_array_literals
  array = Array.new
  assert_equal [], array

  array[0] = 1
  assert_equal [1], array

  array[1] = 2
  assert_equal [1, 2], array

  array << 333
  assert_equal [1, 2, 333] array
end
```

array[0] makes sense, seems par for the course. Now << operator putting the value of 333 into the array in the next available position. I’m a fan. 😀

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

Ok, this is somewhat understandable. The peanut (with the colon? why is the colon included?) is the first value. Cool. That makes sense. The zero is actually the first part of the array, which matches well to array.first, still making sense. The jelly value is in the 3rd, or last location and I’m good with that. Now it gets weird, where is -1? I suppose it is jelly since that test now asserts true. Negative 3 is butter though, which I guess negative values just start from the end. Does that make sense? Either way, it appears to be working that way.

NOTE: This is a a great scenario, to me, and maybe for others, when taking notes pays off. It doesn’t matter if you’re studying for a test or not. I didn’t quit realize what was happening here until I wrote a note, simply explaining it back to myself. Even if you think you get something, writing it down and forcing yourself to think it through is a proven method to putting something to memory.

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

Basically the array is saying, give me one item based on the index of 0. The second assert is starting at index 0 and providing the next two array elements. The same thing then happens for the next two. Of course, starting at index 2 and getting the next 20 values just gets the available values. I can cope with that. The next two asserts then return no value, as there is no 4th array position (remember, it starts at zero.) The last item asks for no items from the array, thus nil is returned.

Well, that’s it for now. More to come in the near future.
