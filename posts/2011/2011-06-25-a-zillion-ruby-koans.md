---
title: A Zillion Ruby Kōans
date: 2011-06-25 10:45:36 -0700
last_modified_at: 2011-06-20 19:45:40 -0700
permalink: /2011/06/25/a-zillion-ruby-koans/
slug: a-zillion-ruby-koans
wp_id: 3051
original_url: https://compositecode.blog/2011/06/25/a-zillion-ruby-koans/
categories:
- Code Katas
- Ruby on Rails Bits
tags:
- koans
- ruby
excerpt: 'NOTE: Because of formatting, I couldn’t have a curly bracket with a colon and an “o” or it turns up with some unavailable WordPress Emoticon URI. So thus I have changed items with this naming to :z_one and :z_two respectively. Yup, still moving through all the Ruby Koans. There are, after all 276 of these …'
---

> *NOTE: Because of formatting, I couldn’t have a curly bracket with a colon and an “o” or it turns up with some unavailable WordPress Emoticon URI. So thus I have changed items with this naming to :z\_one and :z\_two respectively.*

Yup, still moving through all the Ruby Koans. There are, after all 276 of these things! 😉 So no more yapping, onto the notes and green lighting the tests. Cheers!

```ruby
def test_creating_hashes
  empty_hash = Hash.new
  assert_equal Hash, empty_hash.class
  assert_equal({ }, empty_hash)
  assert_equal 0, empty_hash.size
end

def test_hash_literals
  hash = { :z_one  => "uno", :z_two => "dos" }
  assert_equal 2, hash.size
end

def test_accessing_hashes
  hash = { :z_one => "uno", :z_two => "dos" }
  assert_equal "uno", hash[:z_one]
  assert_equal "dos", hash[:z_two]
  assert_equal nil, hash[:doesnt_exist]
end
```

From test\_creating\_hashes a Hash.new or {} both appear to create a new empty hash object. The second test creates and adds values to the hash. The third test has asserts that verify the data is inserted in the positions that are expected.

```ruby
def test_changing_hashes
  hash = { :z_one => "uno", :z_two => "dos" }
  hash[:z_one] = "eins"

  expected = { :z_one => "eins", :z_two => "dos" }
  assert_equal true, expected == hash

  # Bonus Question: Why was "expected" broken out into a variable
  # rather than used as a literal?
end
```

Again, the hash is setup into the hash variable. Then the expected is setup in another variable. Since Ruby is pointer oriented, the expected variable is setup identical to the hash variable to assure that they truly are identical.

```ruby
def test_hash_is_unordered
  hash1 = { :z_one => "uno", :z_two => "dos" }
  hash2 = { :z_two => "dos", :z_one => "uno" }

  assert_equal true, hash1 == hash2
end

def test_hash_keys
  hash = { :z_one => "uno", :z_two => "dos" }
  assert_equal 2, hash.keys.size
  assert_equal true, hash.keys.include?(:z_one)
  assert_equal true, hash.keys.include?(:z_two)
  assert_equal Array, hash.keys.class
end

def test_hash_values
  hash = { :z_one => "uno", :z_two => "dos" }
  assert_equal 2, hash.values.size
  assert_equal true, hash.values.include?("uno")
  assert_equal true, hash.values.include?("dos")
  assert_equal Array, hash.values.class
end
```

test\_hash\_is\_unordered shows that a hash, no matter the order the values are assigned, assigns them to the values that are directly set to.

```ruby
def test_combining_hashes
  hash = { "jim" => 53, "amy" => 20, "dan" => 23 }
  new_hash = hash.merge({ "jim" => 54, "jenny" => 26 })

  assert_equal true, hash != new_hash

  expected = { "jim" => __, "amy" => 20, "dan" => 23, "jenny" => __ }
  assert_equal false, expected == new_hash
end
```

This test asserts that the two different hashes are different, nothing amazing or odd there. The second part asserts that the next and expected hashes are different. Which again, is what we expect.

```ruby
def test_default_value
  hash1 = Hash.new
  hash1[:z_one] = 1

  assert_equal 1, hash1[:z_one]
  assert_equal nil, hash1[:z_two]

  hash2 = Hash.new("dos")
  hash2[:z_one] = 1

  assert_equal 1, hash2[:z_one]
  assert_equal "dos", hash2[:z_two]
end
```

This test confirms that a hash with a request against a hash position that isn’t assigned to yet returns nil. The later two asserts show that a number compared to the hash position that contains a number compares as a number, and a string compared to a position that has a string also compares as equal.

Until next time, hack some koans.
