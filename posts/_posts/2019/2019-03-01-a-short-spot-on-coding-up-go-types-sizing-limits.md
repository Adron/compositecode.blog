---
title: A Short Spot on Coding up Go Types Sizing Limits
date: 2019-03-01 13:46:52 -0800
last_modified_at: 2019-03-01 13:46:54 -0800
permalink: /2019/03/01/a-short-spot-on-coding-up-go-types-sizing-limits/
slug: a-short-spot-on-coding-up-go-types-sizing-limits
wp_id: 15467
original_url: https://compositecode.blog/2019/03/01/a-short-spot-on-coding-up-go-types-sizing-limits/
categories:
- golang
tags:
- go
- golang
- math
- max
- min
- types
excerpt: In an effort, finally, to get around to putting more content together I’ve created this video. It’s the first of many that I’ll put together. This one is a quick coding example of getting the maximum size of particular types in Go. At just about a minute, it’s a quick way to pick up a …
image: /wp-content/uploads/2019/03/quick-spot-1.png
format: aside
---

In an effort, finally, to get around to putting more content together I’ve created this video. It’s the first of many that I’ll put together. This one is a quick coding example of getting the maximum size of particular types in Go. At just about a minute, it’s a quick way to pick up a way to do something coding. If you like this video, do leave a comment, if you thought it wasn’t useful leave a comment. Either way I’d like to read the over under on material like this and if it is or isn’t useful (*or entertaining*) for you. It’ll mostly be just little tips n’ tricks on how to get things done.

<iframe allowfullscreen="true" class="youtube-player" height="486" loading="lazy" sandbox="allow-scripts allow-same-origin allow-popups allow-presentation allow-popups-to-escape-sandbox" src="https://www.youtube.com/embed/l1AxgaQYtqo?version=3&amp;rel=1&amp;showsearch=0&amp;showinfo=1&amp;iv_load_policy=1&amp;fs=1&amp;hl=en-US&amp;autohide=2&amp;wmode=transparent" style="border:0;" width="863"></iframe>

*The code gist.*

```
package main

import (
	"fmt"
	"math"
)

const(
	MinUint uint = 0 // all zeroes
	// Perform a bitwise NOT to change every bit from 0 to 1.
	MaxUint = ^MinUint // all ones

	// Shift the binary number to the right to get the high bit to zero
	MaxInt = int(MaxUint >> 1) // all ones except high bit

	MinInt = ^MaxInt // all zeroes except high bit.
)

func main() {
	// integer max
	fmt.Printf("max for int64 = %+v\n", math.MaxInt64)
	fmt.Printf("max for int32 = %+v\n", math.MaxInt32)
	fmt.Printf("max for int16 = %+v\n", math.MaxInt16)
	fmt.Printf("max for int8 = %+v\n", math.MaxInt8)

	// integer min
	fmt.Printf("min for int64 = %+v\n", math.MinInt64)
	fmt.Printf("min for int32 = %+v\n", math.MinInt32)
	fmt.Printf("min for int16 = %+v\n", math.MinInt16)
	fmt.Printf("min for int8 = %+v\n", math.MinInt8)

	// Added parts that aren't in the video!
	fmt.Printf("max float64 = %+v\n", math.MaxFloat64)
	fmt.Printf("max float32 = %+v\n", math.MaxFloat32)
	fmt.Printf("smallest nonzero float64 = %+v\n", math.SmallestNonzeroFloat64)
	fmt.Printf("smallest nonzero float32 = %+v\n", math.SmallestNonzeroFloat32)

	fmt.Printf("max uint = %+v\n", MaxUint)
	fmt.Printf("min uint = %+v\n", MinUint)
	fmt.Printf("max int = %+v\n", MaxInt)
	fmt.Printf("min int = %+v\n", MinInt)
}
```

[View the gist on GitHub](https://gist.github.com/Adron/a43e7090703d8361cd3a5451602ecbde/de4a385f1b1a3b0f8e31aeb74e76428748d71f45/main.go)
