---
title: 'Converting 2D Arrays to CSV in Go: Problem-Solving and Testing'
date: 2024-06-30 14:20:00 -0700
last_modified_at: 2024-07-03 11:03:50 -0700
permalink: /2024/06/30/converting-2d-arrays-to-csv-in-go-problem-solving-and-testing/
slug: converting-2d-arrays-to-csv-in-go-problem-solving-and-testing
wp_id: 68577
original_url: https://compositecode.blog/2024/06/30/converting-2d-arrays-to-csv-in-go-problem-solving-and-testing/
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
excerpt: In this programming article, the author discusses converting a two-dimensional numeric array into a CSV string using Go. They define tests using the Go testing package, implement the ToCsvText function, and then refactor it using strings.Join for better performance. Multiple test cases ensure the correct handling of empty, single-element, and complex input arrays.
image: /wp-content/uploads/2020/04/golang-rocker.png
---

Programming Problems & Solutions : “Transforming 2D Arrays to CSV Format in Go”. The introduction to this series is [here](/2024/05/29/coding-with-ai-a-comparative-series/) and includes all links to every post in the series. *This is the 7th of a dozen programming challenges I’m doing to setup for an eventual blog post on AI coding*. The intent is to setup these programming challenges, get a solution, find a good refactoring, and then see how the AI tooling performs going through the same thing or refactoring what is in place. If you’re interested in how AI performs, and checking out these experiments and tests, subscribe to the blog to have the articles delivered directly to your email!

Hey there, coding enthusiasts! Today, I’m diving into an interesting problem that involves converting a two-dimensional numeric array into its CSV (Comma-Separated Values) representation. This is a common task when working with data in various formats, and I’ll explore how to tackle it using Go.

The Problem: Imagine you have a 2D array filled with numbers, and you need to convert it into a CSV string. Each row of the array should be represented as a line in the CSV, with the elements separated by commas. For example, consider the following input array:

```
[
    [0, 1, 2, 3, 4],
    [10, 11, 12, 13, 14],
    [20, 21, 22, 23, 24],
    [30, 31, 32, 33, 34]
]
```

The expected output CSV string should look like this:

```
0,1,2,3,4
10,11,12,13,14
20,21,22,23,24
30,31,32,33,34
```

Before I jump into the implementation, I’ll define some tests to ensure our solution works as expected. I’ll use the standard Go testing package and create a test file named `csv_test.go`. Here’s what my tests look like:

```
package main

import "testing"

func TestToCsvText(t *testing.T) {
	testCases := []struct {
		input    [][]int
		expected string
	}{
		{
			input: [][]int{
				{0, 1, 2, 3, 45},
				{10, 11, 12, 13, 14},
				{20, 21, 22, 23, 24},
				{30, 31, 32, 33, 34},
			},
			expected: "0,1,2,3,45\n10,11,12,13,14\n20,21,22,23,24\n30,31,32,33,34",
		},
		{
			input: [][]int{
				{-25, 21, 2, -33, 48},
				{30, 31, -32, 33, -34},
			},
			expected: "-25,21,2,-33,48\n30,31,-32,33,-34",
		},
		{
			input: [][]int{
				{5, 55, 5, 5, 55},
				{6, 6, 66, 23, 24},
				{666, 31, 66, 33, 7},
			},
			expected: "5,55,5,5,55\n6,6,66,23,24\n666,31,66,33,7",
		},
	}

	for _, tc := range testCases {
		result := ToCsvText(tc.input)
		if result != tc.expected {
			t.Errorf("Expected: %q, Got: %q", tc.expected, result)
		}
	}
}
```

I then define a test function `TestToCsvText` that includes multiple test cases. Each test case consists of an input 2D array and the expected CSV string. I iterate over the test cases, call my `ToCsvText` function with the input, and compare the result with the expected output. If there’s a mismatch, the test fails, and an error is reported.

Now, let’s take a look at the implementation of the `ToCsvText` function in the `csv.go` file:

```
package kata

import "strconv"

func ToCsvText(array [][]int) string {
    var result string

    for i, row := range array {
        for j, num := range row {
            result += strconv.Itoa(num)
            if j < len(row)-1 {
                result += ","
            }
        }
        if i < len(array)-1 {
            result += "\n"
        }
    }

    return result
}
```

A run of the tests and victory, first draft is good to go!

[![](/wp-content/uploads/2024/05/CleanShot-2024-05-20-at-23.25.54@2x.png)](/wp-content/uploads/2024/05/CleanShot-2024-05-20-at-23.25.54@2x.png)

The `ToCsvText` function takes a 2D slice of integers (`[][]int`) as input and returns the CSV string representation. Here’s how it works:

1. I initialize an empty string variable `result` to store the CSV output.
2. I use a nested loop to iterate over each row and each element of the 2D array.
3. For each element, I convert the integer to a string using `strconv.Itoa(num)` and append it to the `result` string.
4. After appending each element, I check if it’s not the last element in the row. If it’s not the last element, I append a comma (`,`) to separate the elements.
5. After processing each row, I check if it’s not the last row. If it’s not the last row, I append a newline character (`\n`) to separate the rows.
6. Finally, I return the `result` string, which contains the CSV representation of the 2D array.

With that, I’ve got it! However as always, I like to take a stab at some refactoring. Get the code whittled down to something more concise or get it into a more performant state.

## Refactoring

Let me start by revisiting the original implementation of the `ToCsvText` function. While this implementation works, I can simplify it by leveraging Go’s built-in `strings.Join` function and avoiding the manual concatenation of commas and newline characters. Here’s my refactored version:

```
func ToCsvText(array [][]int) string {
    var rows []string

    for _, row := range array {
        var rowStr []string
        for _, num := range row {
            rowStr = append(rowStr, strconv.Itoa(num))
        }
        rows = append(rows, strings.Join(rowStr, ","))
    }

    return strings.Join(rows, "\n")
}
```

Now for a few more tests.

```
        // ... (existing test cases)
        {
            input:    [][]int{},
            expected: "",
        },
        {
            input: [][]int{
                {1},
            },
            expected: "1",
        },
        {
            input: [][]int{
                {1, 2, 3},
                {4, 5, 6},
            },
            expected: "1,2,3\n4,5,6",
        },
```

I’ve added the following:

1. An empty input array (`[][]int{}`) to ensure my function handles an empty input gracefully and returns an empty string.
2. A single-element array (`[[1]]`) to verify that my function correctly handles a 2D array with only one element.
3. A 2D array with multiple rows and columns (`[[1, 2, 3], [4, 5, 6]]`) to confirm that my function generates the expected CSV string for a more complex input.

Again, another good build and tests passing.

[![](/wp-content/uploads/2024/05/CleanShot-2024-05-20-at-23.43.31@2x.png)](/wp-content/uploads/2024/05/CleanShot-2024-05-20-at-23.43.31@2x.png)

Until next coding challenge, happy thrashing code!

## Reference

- [Github repo](https://github.com/Adron/CsvText) and [first draft](https://github.com/Adron/CsvText/commit/090fc1f9bced698a2b044b4ff7f2dea129622a61) followed with the [refactored code](https://github.com/Adron/CsvText/commit/97febfa704a7b56d9722b4642b0d52ee336c7e15).
