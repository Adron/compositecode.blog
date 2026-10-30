---
title: Learning Go Episode 4 – Composite Types, Slices, Arrays, Etc.
date: 2019-05-27 20:51:27 -0700
last_modified_at: 2019-07-05 19:39:41 -0700
permalink: /2019/05/27/learning-go-episode-4-composite-types-slices-arrays-etc/
slug: learning-go-episode-4-composite-types-slices-arrays-etc
wp_id: 15845
original_url: https://compositecode.blog/2019/05/27/learning-go-episode-4-composite-types-slices-arrays-etc/
categories:
- golang
- Unknown Code Ramblings
- Video
tags:
- coding
- golang
- learning
- programming
- software development
excerpt: 'Episode Post & Video Links: 1, 2, 3, 4 (this post), 5, 6, 7, and 8. Non-linked are in the works! Videos available now on Youtube however, so check em’ out! If you’d like to go through this material too in book form, I highly suggest “The Go Programming Language” by Alan A.A. Donovan & …'
image: /wp-content/uploads/2018/10/thrashing-code-metal-gopher.png
---

Episode Post & Video Links:  [1](/2019/01/19/learning-go-episode-1/), [2](/2019/02/06/learning-go-episode-2-further-into-packages-dependencies-application-creation-and-ides/), [3](/2019/03/10/learning-go-episode-3-more-data-types-casting-rendering-an-svg-file-and-writing-to-files/), 4 (this post), [5](/2019/07/05/learning-go-episode-5-functions-and-methods-and-lots-of-other-things/), 6, 7, and 8. Non-linked are in the works! Videos [available now on Youtube](https://www.youtube.com/playlist?list=PL4f75Y6Ce5ssiDTjB0Y_D7a-13eeAepHn) however, so check em’ out!

If you’d like to go through this material too in book form, I highly suggest “The Go Programming Language” by Alan A.A. Donovan & Brian W. Kernighan. I use it throughout these sessions to provide a guideline. I however add a bunch of other material about IDE’s, development tips n’ tricks and other material.

<iframe allowfullscreen="true" class="youtube-player" height="486" loading="lazy" sandbox="allow-scripts allow-same-origin allow-popups allow-presentation allow-popups-to-escape-sandbox" src="https://www.youtube.com/embed/iQS2dTArLWY?version=3&amp;rel=1&amp;showsearch=0&amp;showinfo=1&amp;iv_load_policy=1&amp;fs=1&amp;hl=en-US&amp;autohide=2&amp;wmode=transparent" style="border:0;" width="863"></iframe>

[8:00](https://youtu.be/iQS2dTArLWY?t=480s) Starting the core content with some notes. Composite types, arrays, slices, etc.
[11:40](https://youtu.be/iQS2dTArLWY?t=700s) Announcement of my first reload – [http://compositecode.blog/2019/02/11/…](/redirect?v=iQS2dTArLWY&redir_token=1_ne_Y_h-eZj_dek5GvhR5vg_RJ8MTU1OTEwMTMwM0AxNTU5MDE0OTAz&event=video_description&q=http%3A%2F%2Fcompositecode.blog%2F2019%2F02%2F11%2Fre-installation-of-linux-the-fuckery-of-windows-10-microsoft-licensing%2F) – second successful time blogged here) of the XPS 15 I have, which – [https://youtu.be/f0z1chi4v1Q](https://youtu.be/iQS2dTArLWY/watch?v=f0z1chi4v1Q) – actually ended in catastrophe the first time!
[14:08](https://youtu.be/iQS2dTArLWY?t=848s) Starting the project for this session.
[16:48](https://youtu.be/iQS2dTArLWY?t=1008s) Setting up arrays, the things that could be confusing, and setup of our first code for the day. I work through assignment, creation, new vs. comparison, and various other characteristics of working with arrays during this time.

```
fmt.Println("Hello, let's talk composite types.")

basketOfStuff := [3]string{"The first string","second","This string."}
var zeeValues [2]int

for i, v := range basketOfStuff {
	fmt.Printf("Value %d: %s\n", i, v)
}

fmt.Println(zeeValues)

if zeeValues[0] == zeeValues[1] {
	fmt.Println("The values are the same, this doesn't instantiate like the `new` keyword.")
} else {
	fmt.Println("The way go appears to instantiate unset variable values, such as in this array is like the `new` keyword instantiation.")
}

zeeValues[0] = 1 + 52 * 3
zeeValues[1] = 9

fmt.Println(zeeValues[len(zeeValues) – 1])
```

[View the gist on GitHub](https://gist.github.com/Adron/a362eac92b1a63797120f03460ed8669/8fe05737d83ff47efd44ce2e373f249107bbbf07/testing-out-composite-types.go)

[29:36](https://youtu.be/iQS2dTArLWY?t=1776s) Creation of a type, called Currency, of type int, setting up constants, and using this kind of like an enumerator to work with code that reads cleaner. Plus of course, all the various things that you might want to, or need for a setup of types, ints, and related composite types like this.

```
type Currency int

const (
	USD Currency = iota
	CAN
	EUR
	GBP
	JPY
	NOK
	SEK
	DKK
)

symbol := […]string{USD: "$", CAN: "$",  EUR: "€", GBP: "£", JPY:"¥", NOK:"kr", SEK:"kr",DKK:"kr"}

fmt.Println(EUR, symbol[EUR])

fmt.Println(JPY, symbol[JPY])

r := […]int{99: -1}

r[36] = 425
r[42] = 42

fmt.Println(r[36] + r[42])
fmt.Println(strconv.Itoa(r[36]))
```

[View the gist on GitHub](https://gist.github.com/Adron/62312b77bd4315214771ebb966575599/3cbf08d44289608bca328ba377613aaae6196564/currency.go)

[43:48](https://youtu.be/iQS2dTArLWY?t=2628s) Creating an example directly from the aforementioned book enumerating the months of the year. This is a great example I just had to work through it a bit for an example.

```
months := […]string{1: "January", 2:"February", 3: "March", 4:"April", 12:"December"}

for _, s := range months {
	fmt.Printf("The month: %s\n", s)
}

var runes []rune
for _, r := range "Language: 走" {
	runes = append(runes, r)
}
fmt.Printf("%q \n", runes)

var x, y []int
for i := 0; i < 10; i++ {
	y = appendInt(x, i)
	fmt.Printf("%d cap=%d\t%v\n", i, cap(y), y)
	x = y
}
```

[View the gist on GitHub](https://gist.github.com/Adron/aaa7d9de0921b728612b5eafb5d40890/5698e9c6403c7e809b069cc011f44f7fb9981e4b/the_months.go)

[52:40](https://youtu.be/iQS2dTArLWY?t=3160s) Here I start showing, and in the process, doing some learning of my own about runes. I wasn’t really familiar with them before digging in just now!

```
… the rest of the main.go file is here…

  var runes []rune
	for _, r := range "Language: 走" {
		runes = append(runes, r)
	}
	fmt.Printf("%q \n", runes)

	var x, y []int
	for i := 0; i < 10; i++ {
		y = appendInt(x, i)
		fmt.Printf("%d cap=%d\t%v\n", i, cap(y), y)
		x = y
	}

}

func appendInt(x []int, i int) []int {
	var z []int
	zlen := len(x) + 1
	if zlen <= cap(x) {
		z = x[:zlen]
	} else {
		zcap := zlen
		if zcap < 2* len(x) {
			zcap = 2 * len(x)
		}
		z = make([]int, zlen, zcap)
		copy(z, x)
	}

	return z
}
```

[View the gist on GitHub](https://gist.github.com/Adron/081a81173c271d5865cbf39ea38aa73b/f0304a2eb82432e02fec71871a9e0523a5a9fc3d/main.go)

[1:09:40](https://youtu.be/iQS2dTArLWY?t=4180s) Here I break things down and start a new branch for some additional examples. I also derail off into some other things about meetups and such for a short bit. Skip to the next code bits at the next time point.
[1:23:58](https://youtu.be/iQS2dTArLWY?t=5038s) From here on to the remainder of the video I work through a few examples of how to setup maps, how make works, and related coding around how to retrieve, set, and otherwise manipulate the maps one you’ve got them.

```
package main

import "fmt"

func main() {
	ages := map[string]int{
		"Peterson": 52,
		"Sally":    22,
		"Javovia":  15,
		"Ben":      42,
	}

	jobAssociation := make(map[string]string)
	jobAssociation["Peterson"] = "Engineer"
	jobAssociation["Sally"] = "CEO"
	jobAssociation["Jovovia"] = "Gamer"
	jobAssociation["Ben"] = "Programmer"

	printAges(ages)
	printJobAssociations(jobAssociation)

	fmt.Println(ages)
	fmt.Println(jobAssociation)
	fmt.Println(jobAssociation["Jovovia"])
	fmt.Println(jobAssociation["Frank"]) // Blank! 😮
	fmt.Println(ages["Sally"])

	delete(ages, "Sally")

	fmt.Println(ages)
	fmt.Println(ages["Sally"])

	delete(jobAssociation, "Jovovia")

	fmt.Println(jobAssociation)
	fmt.Println(jobAssociation["Jovovia"]) // Blank.

	ages2 := map[string]int{
		"Frank":     52,
		"Johnson":   22,
		"Smith":     15,
		"Jezebelle": 42,
	}

	ages3 := map[string]int{
		"Frank":     52,
		"Johnson":   22,
		"Smith":     15,
		"Jezebelle": 42,
	}

	if equal(ages, ages2) {
		fmt.Println("Naw, not really equal.")
	} else {
		fmt.Println("This is correct, not equal.")
	}

	if equal(ages2, ages3) {
		fmt.Println("True, these are effectively the same map values and keys.")
	}
}

func printJobAssociations(associations map[string]string) {
	for name, job := range associations {
		fmt.Printf("%s\t%s\n", name, job)
	}
}

func printAges(ages map[string]int) {
	for name, age := range ages {
		fmt.Printf("%s\t%d\n", name, age)
	}
}

func equal(x, y map[string]int) bool {
	if len(x) != len(y) {
		return false
	}
	for k, xv := range x {
		if yv, ok := y[k]; !ok || yv != xv {
			return false
		}
	}
	return true
}
```

[View the gist on GitHub](https://gist.github.com/Adron/f8dc67a810ae86b3d0fc95354a848289/d994177401c9264390bb5f0b6e27307d1ead94cb/map_types.go)

That’s it for this synopsis. Until next episode, happy code thrashing and go coding!
