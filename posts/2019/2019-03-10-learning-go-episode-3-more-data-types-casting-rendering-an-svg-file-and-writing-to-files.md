---
title: Learning Go Episode 3 – More Data Types, Casting, Rendering an SVG file, and writing to Files.
date: 2019-03-10 15:48:46 -0700
last_modified_at: 2019-07-05 19:39:03 -0700
permalink: /2019/03/10/learning-go-episode-3-more-data-types-casting-rendering-an-svg-file-and-writing-to-files/
slug: learning-go-episode-3-more-data-types-casting-rendering-an-svg-file-and-writing-to-files
wp_id: 15247
original_url: https://compositecode.blog/2019/03/10/learning-go-episode-3-more-data-types-casting-rendering-an-svg-file-and-writing-to-files/
categories:
- golang
- Video
tags:
- coding
- data types
- go
- golang
- keygen
- learning
- programming
- ssh
- svg
- svg file
- types
excerpt: 'Episode Post & Video Links: 1, 2, 3 (this post), 4, 5, 6, 7, and 8. Non-linked are in the works! Videos available now on Youtube however, so check em’ out! Episode 3 of my recurring “Learning Go” Saturday stream really got more into the particulars of Go data types including integers, strings, more string …'
image: /wp-content/uploads/2018/10/thrashing-code-metal-gopher.png
---

Episode Post & Video Links:  [1](/2019/01/19/learning-go-episode-1/), [2](/2019/02/06/learning-go-episode-2-further-into-packages-dependencies-application-creation-and-ides/), 3 (this post), [4](/2019/05/27/learning-go-episode-4-composite-types-slices-arrays-etc/), [5](/2019/07/05/learning-go-episode-5-functions-and-methods-and-lots-of-other-things/), 6, 7, and 8. Non-linked are in the works! Videos [available now on Youtube](https://www.youtube.com/playlist?list=PL4f75Y6Ce5ssiDTjB0Y_D7a-13eeAepHn) however, so check em’ out!

[Episode 3](https://youtu.be/k1R8jAV_rbw) of my recurring “[Learning Go](https://www.youtube.com/playlist?list=PL4f75Y6Ce5ssiDTjB0Y_D7a-13eeAepHn)” Saturday stream really got more into the particulars of Go data types including integers, strings, more string formatting verbs, concatenation, type casting, and lots of other pedantic details. In the episode I also delve into some OBS details with the audience, and we get the Twitch interface I’ve setup a bit more streamlined for easier readability. Overall, I think it’s looking much better than just the last episode! Hats off to the conversational assist from the audience.

Here’s the play by play of what was covered in [episode 3](https://youtu.be/k1R8jAV_rbw) with the code in gists plus the repo is available on [Github](https://github.com/Adron/learning-go-episode-3). Video below the timeline.

**Timeline**

[0:00](https://youtu.be/k1R8jAV_rbw/watch?v=k1R8jAV_rbw&t=0s) Intro
[6:08](//youtu.be/k1R8jAV_rbw/watch?v=k1R8jAV_rbw&t=368s) The point I fix the sound. Just skip that first bit!
[6:24](//youtu.be/k1R8jAV_rbw/watch?v=k1R8jAV_rbw&t=384s) Re-introducing the book I’m using as a kind of curriculum guide for these go learning sessions.
[7:44](//youtu.be/k1R8jAV_rbw/watch?v=k1R8jAV_rbw&t=464s) Quick fix of the VM, a few updates, discussion of Goland updates, and fixing the Material Theme to a more visually less caustic theme. Also showing where it is in the IDE.
[9:52](//youtu.be/k1R8jAV_rbw/watch?v=k1R8jAV_rbw&t=592s) Getting into the learning flow, starting a new project with Go 1.11.4 using the Goland IDE new project dialog.

```
package main

import (
	"fmt"
	"math"
	"strconv"
)

func main() {
	var someInt int
	var anotherValue int64
	thisValue := 45
	thisVAlue, thatValue, someValue := 20, 23, 15
	someInt = thisVAlue
	anotherValue = 64

	const knownSet = 7.12904
	const anotherKnown = 9.10347

	for x := 0; x < 20; x++ {
		fmt.Printf("x = %d  e = %8.3f\n", x, math.Exp(float64(x)))
	}

	fmt.Printf("Known Set and Another Known: %2.7f, %2.7f", knownSet, anotherKnown)

	fmt.Printf("The values: %6d, %6d, %6d, and %s.\n", thisValue, thisVAlue, thatValue, strconv.Itoa(someValue))
	fmt.Printf("Other values: %4d, %4d.\n", someInt, anotherValue)

	fmt.Printf("Function doThings: %6d\n", doThings(thisVAlue, thisValue))
	fmt.Printf("Function doMoreThings: %s", doMoreThings(someInt, int(anotherValue), "Adron"))
}

func doThings (valueOne int, valueTwo int) int64 {
	result := valueOne * valueTwo
	return int64(result)
}

func doMoreThings (valueOne int, valueTwo int, name string) string {
	result := valueTwo + valueOne * 10
	return "The result added and exponentially multiplied for you " + name + " this: " + strconv.Itoa(result)
}
```

[View the gist on GitHub](https://gist.github.com/Adron/7201a3467caa5586873aa9a9761974fa/903f110c5d72db9a5de0a12da5b296d729e025bf/main.go)

[10:50](//youtu.be/k1R8jAV_rbw/watch?v=k1R8jAV_rbw&t=650s) Creating the Github repo for learning-go-episode-3.
[12:14](//youtu.be/k1R8jAV_rbw/watch?v=k1R8jAV_rbw&t=734s) Setting up the initial project and CODING! Finally getting into some coding. It takes a while when we do it from nothing like this, but it’s a fundamentally important part of starting a project!
[13:04](//youtu.be/k1R8jAV_rbw/watch?v=k1R8jAV_rbw&t=784s) From nothing, creating the core basic elements of a code file for go with main.go. In this part I start showing the various ways to declare types, such as int and int64 with options on style.
[14:14](//youtu.be/k1R8jAV_rbw/watch?v=k1R8jAV_rbw&t=854s) Taking a look at printing out the various values of the variables using formatter verbs via the fmt.Printf function.
[17:00](//youtu.be/k1R8jAV_rbw/watch?v=k1R8jAV_rbw&t=1020s) Looking at converting values from one type to another type. There are a number of ways to do this in Go.

I also, just recently, posted a [quick spot video and code](/2019/03/01/a-short-spot-on-coding-up-go-types-sizing-limits/) ([blog entry + code](/2019/03/01/a-short-spot-on-coding-up-go-types-sizing-limits/)) on getting the minimum and maximum value in Go for a number of types. This isn’t the course video, just a *quick spot*. Keep reading for the main episode below.

<iframe allowfullscreen="true" class="youtube-player" height="486" loading="lazy" sandbox="allow-scripts allow-same-origin allow-popups allow-presentation allow-popups-to-escape-sandbox" src="https://www.youtube.com/embed/l1AxgaQYtqo?version=3&amp;rel=1&amp;showsearch=0&amp;showinfo=1&amp;iv_load_policy=1&amp;fs=1&amp;hl=en-US&amp;autohide=2&amp;wmode=transparent" style="border:0;" width="863"></iframe>

[18:16](//youtu.be/k1R8jAV_rbw/watch?v=k1R8jAV_rbw&t=1096s) Oh dear the mouse falls on the ground. The ongoing battle of streaming, falling objects! But yeah, I get into adding a function – one of the earlier functions being built in the series – and we add a signature with a return int64 value. I continue, with addition of another function and looking at specifics of the signature.
[25:50](//youtu.be/k1R8jAV_rbw/watch?v=k1R8jAV_rbw&t=1550s) Build this code and take a look at the results. At this point, some of the formatting is goofed up so I take a look into the formatter verbs to figure out what should be used for the output formatting.
[33:40](//youtu.be/k1R8jAV_rbw/watch?v=k1R8jAV_rbw&t=2020s) I change a few things and take a look at more output from the various calculations that I’ve made, showing how various int, int64, and related calculations can be seen.
[37:10](//youtu.be/k1R8jAV_rbw/watch?v=k1R8jAV_rbw&t=2230s) Adding a constant, what it is, and when and where and why to declare something as a constant.
[38:05](//youtu.be/k1R8jAV_rbw/watch?v=k1R8jAV_rbw&t=2285s) Writing out another for loop for output results of sets.
[42:40](//youtu.be/k1R8jAV_rbw/watch?v=k1R8jAV_rbw&t=2560s) A little git work to create a branch, update the .gitignore, and push the content to github. Repo is here btw: <https://github.com/Adron/learning-go-episode-3>

At this point I had to take a short interruption to get my ssh keys setup for this particular VM so I could push the code! I snagged just a snippet of the video and made a *quick spot* video out of it too. Seems a useful thing to do.

<iframe allowfullscreen="true" class="youtube-player" height="486" loading="lazy" sandbox="allow-scripts allow-same-origin allow-popups allow-presentation allow-popups-to-escape-sandbox" src="https://www.youtube.com/embed/hAwMFvmp70A?version=3&amp;rel=1&amp;showsearch=0&amp;showinfo=1&amp;iv_load_policy=1&amp;fs=1&amp;hl=en-US&amp;autohide=2&amp;wmode=transparent" style="border:0;" width="863"></iframe>

[47:44](//youtu.be/k1R8jAV_rbw/watch?v=k1R8jAV_rbw&t=2864s) Have to add a new ssh key for the virtual machine to github, so this is a good little snippet of a video showing how that is done.
[56:38](//youtu.be/k1R8jAV_rbw/watch?v=k1R8jAV_rbw&t=3398s) Building out a rendering of an SVG file to build a graphic. The complete snippet is below, watch the video for more details, troubleshooting, and working through additions and refactoring of the code.

```
package main

import (
	"fmt"
	"io/ioutil"
	"math"
	"strconv"
)

const (
	width, height = 600, 600
	cells         = 100
	xyrange       = 30.0
	xyscale       = width / 2 / xyrange
	zscale        = height * 0.4
	angle         = math.Pi / 6
)

var sin30, cos30 = math.Sin(angle), math.Cos(angle)

func main() {

	var outputResult string

	outputResult = "<svg xmlns='http://www.w3.org/2000/svg&#39; " +
		"style='stroke: blue; fill: white; stroke-width: 0.7' " +
		"width='" + strconv.Itoa(width) + "' height='" + strconv.Itoa(height) + "'>"

	for i := 0; i < cells; i++ {
		for j := 0; j < cells; j++ {
			ax, ay := corner(i+1, j)
			bx, by := corner(i, j)
			cx, cy := corner(i, j+1)
			dx, dy := corner(i+1, j+1)

			outputResult = outputResult + "<polygon points='" +
				ax + "," + ay +
				bx + "," + by +
				cx + "," + cy +
				dx + "," + dy +
				"'/>\n"
		}
	}
	outputResult = outputResult + "</svg>"
	fmt.Printf(outputResult)
	err := ioutil.WriteFile("surface-plot.svg", []byte(outputResult), 0644)
	if err != nil {
		fmt.Printf("Error: %s", err)
	}
}

func corner(i, j int) (string, string) {
	x := xyrange * (float64(i)/cells – 0.5)
	y := xyrange * (float64(j)/cells – 0.5)

	z := f(x, y)

	sx := width/2 + (x-y)*cos30*xyscale
	sy := height/2 + (x+y)*sin30*xyscale – z*zscale

	xResult := strconv.FormatFloat(sx, 'f', -1, 64)
	yResult := strconv.FormatFloat(sy, 'f', -1, 64)
	return xResult, yResult
}

func f(x, y float64) float64 {
	r := math.Hypot(x, y)
	return math.Sin(r)
}
```

[View the gist on GitHub](https://gist.github.com/Adron/052a3fe17066514634b84f9bb1decb5a/080152ccdd1196e352e5f2009a77fc88b671f8ba/main.go)

[1:15:32](//youtu.be/k1R8jAV_rbw/watch?v=k1R8jAV_rbw&t=4532s) We begin the mission of bumping up the font size in Goland. It’s a little tricky but we get it figured out.
[1:33:20](//youtu.be/k1R8jAV_rbw/watch?v=k1R8jAV_rbw&t=5600s) Upon realization, we need to modify for our work, that this outputs directly to a file instead of just the console. Things will work better that way so I work into the code a write out to file.
[1:40:05](//youtu.be/k1R8jAV_rbw/watch?v=k1R8jAV_rbw&t=6005s) Through this process of changing it to output to file, I have to work through additional string conversions, refactoring, and more. There’s a lot of nuance and various things to learn during this section of the video, albeit a little slow. i.e. LOTS of strconv usage.
[2:01:24](//youtu.be/k1R8jAV_rbw/watch?v=k1R8jAV_rbw&t=7284s) First view of the generated SVG file! Yay! Oh dear!
[2:09:10](//youtu.be/k1R8jAV_rbw/watch?v=k1R8jAV_rbw&t=7750s) More troubleshooting to try and figure out where the math problem is!
[2:22:50](//youtu.be/k1R8jAV_rbw/watch?v=k1R8jAV_rbw&t=8570s) Wrapping up with the math a little off kilter, but sort of fixed, I move on to getting a look into the build but also pushing each of the respective branches on github. Repo is here btw: <https://github.com/Adron/learning-go-episode-3>

<iframe allowfullscreen="true" class="youtube-player" height="486" loading="lazy" sandbox="allow-scripts allow-same-origin allow-popups allow-presentation allow-popups-to-escape-sandbox" src="https://www.youtube.com/embed/k1R8jAV_rbw?version=3&amp;rel=1&amp;showsearch=0&amp;showinfo=1&amp;iv_load_policy=1&amp;fs=1&amp;hl=en-US&amp;autohide=2&amp;wmode=transparent" style="border:0;" width="863"></iframe>
