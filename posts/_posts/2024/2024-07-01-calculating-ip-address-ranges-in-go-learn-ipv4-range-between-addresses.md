---
title: 'Calculating IP Address Ranges in Go: Learn IPv4 Range Between Addresses'
date: 2024-07-01 08:00:00 -0700
last_modified_at: 2024-07-03 11:03:57 -0700
permalink: /2024/07/01/calculating-ip-address-ranges-in-go-learn-ipv4-range-between-addresses/
slug: calculating-ip-address-ranges-in-go-learn-ipv4-range-between-addresses
wp_id: 68578
original_url: https://compositecode.blog/2024/07/01/calculating-ip-address-ranges-in-go-learn-ipv4-range-between-addresses/
categories:
- Code Katas
- golang
tags:
- code kata
- coding
- go
- golang
- kata
- programming
excerpt: This article discusses solving a programming problem related to calculating the number of IP addresses between two IPv4 addresses. The solution, implemented in Go, involves parsing the IP addresses, converting them to integer representations, and handling various edge cases. The article also includes code refactoring for improved readability and compactness.
image: /wp-content/uploads/2020/04/golang-rocker.png
---

Programming Problems & Solutions : “Exploring IP Address Ranges in Go”. The introduction to this series is [here](/2024/05/29/coding-with-ai-a-comparative-series/) and includes all links to every post in the series. *This is the 8th of a dozen programming challenges I’m doing to setup for an eventual blog post on AI coding*. The intent is to setup these programming challenges, get a solution, find a good refactoring, and then see how the AI tooling performs going through the same thing or refactoring what is in place. If you’re interested in how AI performs, and checking out these experiments and tests, subscribe to the blog to have the articles delivered directly to your email!

Hey there, fellow code adventurers! Today, we’re diving into the world of IP addresses and ranges. We’ve got an exciting coding challenge on our hands, and we’ll be tackling it using the Go programming language. So, grab your favorite beverage, and let’s get started!

**The Challenge**

Our mission, should we choose to accept it, is to implement a function that takes two IPv4 addresses as input and returns the number of addresses between them (including the first one, but excluding the last one). We’ll be working with valid IPv4 addresses in the form of strings, and the last address will always be greater than the first one.

Examples To give you a better idea of what we’re aiming for, here are a few examples:

- With input “10.0.0.0” and “10.0.0.50”, the function should return 50.
- With input “10.0.0.0” and “10.0.1.0”, the function should return 256.
- With input “20.0.0.10” and “20.0.1.0”, the function should return 246.

Testing Our Code Before we dive into the implementation, let’s take a look at the tests we’ll be running to ensure our code is up to par. We’ll be using the Ginkgo testing framework and the Gomega assertion library to write our tests.

```
package main

import "testing"

func TestIpsBetween(t *testing.T) {
	t.Run("should handle basic cases", func(t *testing.T) {
		assertEqual(t, IpsBetween("10.0.0.0", "10.0.0.50"), 50)
		assertEqual(t, IpsBetween("20.0.0.10", "20.0.1.0"), 246)
	})

	t.Run("should handle large ranges", func(t *testing.T) {
		assertEqual(t, IpsBetween("10.0.0.0", "10.0.1.0"), 256)
		assertEqual(t, IpsBetween("10.0.0.0", "10.1.0.0"), 65536)
	})

	t.Run("should handle different octets", func(t *testing.T) {
		assertEqual(t, IpsBetween("10.0.0.0", "11.0.0.0"), 16777216)
		assertEqual(t, IpsBetween("10.0.0.0", "12.0.0.0"), 33554432)
	})

	t.Run("should handle same start and end addresses", func(t *testing.T) {
		assertEqual(t, IpsBetween("10.0.0.0", "10.0.0.0"), 0)
		assertEqual(t, IpsBetween("192.168.1.1", "192.168.1.1"), 0)
	})
}

func assertEqual(t *testing.T, actual, expected int) {
	if actual != expected {
		t.Errorf("Expected %d, but got %d", expected, actual)
	}
}
```

These tests cover various scenarios, including basic cases, large ranges, different octets, and even the case where the start and end addresses are the same.

The Solution Now, let’s take a look at the solution:

```
package main

import (
	"fmt"
	"net"
)

func main() {
	fmt.Println(IpsBetween("10.0.0.0", "10.0.0.50"))
}

func IpsBetween(start, end string) int {
	startIP := net.ParseIP(start).To4()
	endIP := net.ParseIP(end).To4()

	if startIP == nil || endIP == nil {
		panic(fmt.Sprintf("Invalid IPv4 address: start=%s, end=%s", start, end))
	}

	startNum := ipToInt(startIP)
	endNum := ipToInt(endIP)

	return int(endNum - startNum)
}

func ipToInt(ip net.IP) uint32 {
	result := uint32(ip[0]) << 24
	result |= uint32(ip[1]) << 16
	result |= uint32(ip[2]) << 8
	result |= uint32(ip[3])
	return result
}
```

Let’s break it down:

1. We start by parsing the input IPv4 addresses using `net.ParseIP()` and converting them to 4-byte representations using `.To4()`. This ensures we’re working with valid IPv4 addresses.
2. If either `startIP` or `endIP` is `nil`, it means the input address is invalid, so we panic with an appropriate error message.
3. We convert the start and end IP addresses to their integer representations using the `ipToInt()` function. This function shifts and combines the individual bytes of the IP address to form a single 32-bit unsigned integer.
4. Finally, we calculate the difference between the integer representations of the end and start IP addresses and return the result as an `int`.

And there you have it! A solution to calculate the number of IP addresses between two given IPv4 addresses.

## Refactoring

Ok, I kicked off and came up with some good refactoring, here are the changes:

1. In the `IpsBetween` function, I directly return the result of subtracting the int representations of the start and end IP addresses. I parse and convert the IP addresses inline using `net.ParseIP(end).To4()` and `net.ParseIP(start).To4()`.
2. Next I removed the error handling with the panic statement. If an invalid IP address is provided, `net.ParseIP()` will return `nil`, and the `ipToInt` function will panic with a “runtime error: invalid memory address or nil pointer dereference” error. This is a more idiomatic way of handling errors in Go, as it allows the caller to handle the error appropriately.
3. In the `ipToInt` function, I combined the bit shifting and OR operations into a single line to make it more concise.

With these changes, the code is more compact and easier to read. The functionality remains the same, and it still passes all the tests. It comes out looking like this

```
package main

import (
	"fmt"
	"net"
)

func main() {
	fmt.Println(IpsBetween("10.0.0.0", "10.0.0.50"))
}

func IpsBetween(start, end string) int {
	return int(ipToInt(net.ParseIP(end).To4()) - ipToInt(net.ParseIP(start).To4()))
}

func ipToInt(ip net.IP) uint32 {
	return uint32(ip[0])<<24 | uint32(ip[1])<<16 | uint32(ip[2])<<8 | uint32(ip[3])
}
```

I hope you enjoyed this coding adventure as much as I did. Until next time, happy coding, and may your IP addresses always be in range!

## References

- [Github repo](https://github.com/Adron/eye-peas/) and the [first draft](https://github.com/Adron/eye-peas/commit/e253c7d3df50cd78a573367d0585abdebb0dc2e6) followed with the [refactored code](https://github.com/Adron/eye-peas/commit/e02c443b25b4ccc13a6df7d33ab321c366193bea).
