---
title: Code Kōans
date: 2011-06-06 05:55:07 -0700
last_modified_at: 2011-06-06 13:52:59 -0700
permalink: /2011/06/06/code-koans/
slug: code-koans
wp_id: 2946
original_url: https://compositecode.blog/2011/06/06/code-koans/
categories:
- Code Katas
- How-to
- Ruby on Rails Bits
tags:
- code koan
- koans
- ruby
excerpt: Recently (albeit it seems a few years after a lot of my fellow developers) I’ve dug into kōans. A kōan (Chinese 公案, Korean 공안, I had to put the symbols, but I just find them awesome 🙂 ) is a fundamental part of the history and lore of ZenBuddhism. It consists of a story, dialogue, question, or statement, the meaning of which cannot be understood by rational thinking but may be accessible through intuition. The classic example is “Two hands clap and there is a sound; what is the sound of one hand?” The first set of koans I checked out (thanks to @Ang3lfir3) were the Clojure Kōans. I’ll admit, I had a slightly higher priority with Ruby so I grabbed the Ruby Kōans. I’ll get to the Clojure ones soon, as Clojure is a great language to work through and derive meaning through intuition. With that little intro, I’ll dive in… The first file is absurdly easy, basically making sure reality exists in that true is true and true is not false. These seem pretty straight forward. When I got into the subsequent koan test files though, things started to get interesting. The Ruby Language itself started to show itself and how it actually works. When working through the koans, you’re actually working with real Ruby Unit Tests and code files. In my descriptions below I’ve cut those files up so I can comment in between each bit of code. I will however format each bit of code properly for readability. Cheers!
---

Recently (*albeit it seems a few years after a lot of my fellow developers*) I’ve dug into [kōans](http://en.wikipedia.org/wiki/K%C5%8Dan). A **kōan** (Chinese 公案, Korean 공안, I had to put the symbols, but I just find them awesome 🙂 ) is a fundamental part of the history and lore of [Zen](http://en.wikipedia.org/wiki/Zen "Zen")[Buddhism](http://en.wikipedia.org/wiki/Buddhism "Buddhism"). It consists of a [story](http://en.wikipedia.org/wiki/Narrative "Narrative"), [dialogue](http://en.wikipedia.org/wiki/Dialogue "Dialogue"), question, or statement, the meaning of which cannot be understood by [rational](http://en.wikipedia.org/wiki/Rationality "Rationality") thinking but may be accessible through [intuition](http://en.wikipedia.org/wiki/Intuition_(knowledge)#Intuition_and_spirituality "Intuition (knowledge)"). The classic example is “*Two hands clap and there is a sound; what is the sound of one hand?*”

The first set of koans I checked out (thanks to [@Ang3lfir3](http://twitter.com/#!/ang3lfir3)) were the [Clojure Kōans](https://github.com/functional-koans/clojure-koans). I’ll admit, I had a slightly higher priority with Ruby so I grabbed the [Ruby Kōans](https://github.com/edgecase/ruby_koans). I’ll get to the Clojure ones soon, as Clojure is a great language to work through and derive meaning through intuition. With that little intro, I’ll dive in…

The first file is absurdly easy, basically making sure reality exists in that true is true and true is not false. These seem pretty straight forward. When I got into the subsequent koan test files though, things started to get interesting. The Ruby Language itself started to show itself and how it actually works. When working through the koans, you’re actually working with real Ruby Unit Tests and code files. In my descriptions below I’ve cut those files up so I can comment in between each bit of code. I will however format each bit of code properly for readability. Cheers!

```ruby
class AboutObjects &lt; EdgeCase::Koan
  def test_everything_is_an_object
    assert_equal true, 1.is_a?(Object)
    assert_equal true, 1.5.is_a?(Object)
    assert_equal true, "string".is_a?(Object)
    assert_equal true, nil.is_a?(Object)
    assert_equal true, Object.is_a?(Object)
  end
```

After running through this test, it’s a little obvious the point. Everything is an object. Get it? :O

```ruby
  def test_objects_can_be_converted_to_strings
    assert_equal "123", 123.to_s
    assert_equal "", nil.to_s
  end
```

Ok, so I kind of feel that to\_s is a bit silly for a method name, but whatever. I’m also assuming at this point that “nil” is a reserved object or something. I’m not sure what the assumption of nil is though, since it is an empty string, but sort of null, but not null, but maybe no value? I’ll just have to look this bit up later.

I did a search to dig this up and am even more confused now. I found this [entry first](http://www.themomorohoax.com/2009/05/21/when-to-use-nil-in-ruby-methods), which would lead me to believe that nil is also a method on an object, but an object itself? Ok, I’ll read more later and move on to the next tests, maybe intuition will strike and I’ll all of a sudden realize what I’m working with here.

```ruby
  def test_objects_can_be_inspected
    assert_equal "123", 123.inspect
    assert_equal "nil", nil.inspect
  end
```

The inspect method, seems simple enough. The method is or has a sort of default print out of what it is called under “inspection”. Ok, next…

```ruby
  def test_every_object_has_an_id
    obj = Object.new
    assert_equal Fixnum, obj.object_id.class
  end
```

This is simple enough, every object gets an ID, whatever it may be. I’d bet it is unique, not that this test proves that. …I do wonder though, what exactly is Fixnum?

```ruby
  def test_every_object_has_different_id
    obj = Object.new
    another_obj = Object.new
    assert_equal true, obj.object_id != another_obj.object_id
  end
```

Ok, as I suspected, object IDs are unique. Got it.

```ruby
  def test_some_system_objects_always_have_the_same_id
    assert_equal 0, false.object_id
    assert_equal 2, true.object_id
    assert_equal 4, nil.object_id
  end
```

Umm. Yeah. Ok. That makes sense sort of. I’m now more confused about nil. It is 4, or null, or part of an enumeration? Who knows, who could tell from this test. I’ve got it though, false is zero, and two is true for some reason? I want to know what happened to one, which I suppose, is another thing I’ll have to intuit later. Onward!

```ruby
  def test_small_integers_have_fixed_ids
    assert_equal 1, 0.object_id
    assert_equal 3, 1.object_id
    assert_equal 5, 2.object_id
    assert_equal 7, 3.object_id
    assert_equal 9, 4.object_id
    assert_equal 11, 5.object_id
    assert_equal 13, 6.object_id
    assert_equal 201, 100.object_id
    # THINK ABOUT IT: 2x the number +1 == WTF? Why choose that?
    # What pattern do the object IDs for small integers follow?
  end
```

Ok, I wanted to verify what the pattern was, so I actually added some asserts to this test. Hmmm, it appears, after adding the tests, that there is this nifty patter but I just can’t put my finger on it! 😉 (in case it isn’t evident, I’m being sarcastic here)

```ruby
  def test_clone_creates_a_different_object
    obj = Object.new
    copy = obj.clone
    assert_equal true, obj           != copy
    assert_equal true, obj.object_id != copy.object_id
  end
end
```

Ok, verified that object IDs stay unique upon creation or even cloning of new objects. This is an important thing to realize and understand within the overall design of Ruby. Enough for this short work through, more later, and again go and check out the [Ruby Kōans](https://github.com/edgecase/ruby_koans) yourself, they’re a lot of fun to work through.
