---
title: Learning Go Episode 2 – Further into packages, dependencies, application creation, and IDE’s
date: 2019-02-06 00:54:37 -0800
last_modified_at: 2019-07-05 19:39:00 -0700
permalink: /2019/02/06/learning-go-episode-2-further-into-packages-dependencies-application-creation-and-ides/
slug: learning-go-episode-2-further-into-packages-dependencies-application-creation-and-ides
wp_id: 15236
original_url: https://compositecode.blog/2019/02/06/learning-go-episode-2-further-into-packages-dependencies-application-creation-and-ides/
categories:
- golang
- ThrashingCode
- Video
tags:
- coding
- go
- golang
- learning
- learning to code
- programing
excerpt: 'Episode Post & Video Links: 1, 2 (this post), 3, 4, 5, 6, 7, and 8. Non-linked are in the works! Videos available now on Youtube however, so check em’ out! In episode two I went over a lot of the material that I covered in the first episode, but added more context, historical reasons …'
image: /wp-content/uploads/2018/10/thrashing-code-metal-gopher.png
---

Episode Post & Video Links:  [1](/2019/01/19/learning-go-episode-1/), 2 (this post), [3](/2019/03/10/learning-go-episode-3-more-data-types-casting-rendering-an-svg-file-and-writing-to-files/), [4](/2019/05/27/learning-go-episode-4-composite-types-slices-arrays-etc/), [5](/2019/07/05/learning-go-episode-5-functions-and-methods-and-lots-of-other-things/), 6, 7, and 8. Non-linked are in the works! Videos [available now on Youtube](https://www.youtube.com/playlist?list=PL4f75Y6Ce5ssiDTjB0Y_D7a-13eeAepHn) however, so check em’ out!

In episode two I went over a lot of the material that I covered in the first episode, but added more context, historical reasons certain things are the way they are in Go and the stack, and went over a number of new elements of information too. One thing I got further into this episode is the package and dependency management with Go Dep and also how to create a package, or dependency library for use in other Go libraries or applications. It’s just a small introduction in this episode, but pivotal to future episodes, as I’ll be jumping further into library creation and related details.

In this post I’ve got the time point breakdown like usual,  but also a few additional bits of information and code examples, plus links to the repository I’ve setup for this particular episode. The quick links to those references are below, and also I’ll link at particular call out points within the time points.

**Quick Links:**

- [Episode 2 Repository](https://github.com/Adron/learning-go-episode-2)
- Github: <https://github.com/golang/go>
- Golang: <https://golang.org>
- “[The Go Programming Language](http://www.informit.com/store/go-programming-language-9780134190440)” by Alan A. A. Donovan and Brian W. Kernighan

**Key Topics Covered**

*Data Types, Packages, and Dependency Management*

<iframe allowfullscreen="true" class="youtube-player" height="486" loading="lazy" sandbox="allow-scripts allow-same-origin allow-popups allow-presentation allow-popups-to-escape-sandbox" src="https://www.youtube.com/embed/HQbUjUiMVY0?version=3&amp;rel=1&amp;showsearch=0&amp;showinfo=1&amp;iv_load_policy=1&amp;fs=1&amp;hl=en-US&amp;autohide=2&amp;wmode=transparent" style="border:0;" width="863"></iframe>

[2:52](https://youtu.be/HQbUjUiMVY0/watch?v=HQbUjUiMVY0&t=172s) – Fumbling through getting started. It is after all Saturday morning!
[3:00](https://youtu.be/HQbUjUiMVY0/watch?v=HQbUjUiMVY0&t=180s) – Recap of what we covered in the first session. Includes a quick review of the previous session code too, such as the random data generation library we setup and used.
[6:40](https://youtu.be/HQbUjUiMVY0/watch?v=HQbUjUiMVY0&t=400s) – Covering some specifics of the IDE’s, the stories of the benefits of Go having a specific and somewhat detailed convention to the way syntax, variables, and related features are used.
[7:40](https://youtu.be/HQbUjUiMVY0/watch?v=HQbUjUiMVY0&t=460s) – Covering `gofmt` and what it gives us.
[9:45](https://youtu.be/HQbUjUiMVY0/watch?v=HQbUjUiMVY0&t=585s) – Looking at the `gofmt` plugins and IDE features around the conventions.
[14:06](https://youtu.be/HQbUjUiMVY0/watch?v=HQbUjUiMVY0&t=846s) – New example time! In this one, I work through an example showing how to find duplicate lines in passed in text.

## Duplicate Line Finder

I went through the various steps of creating the code, but then took a little bit of a detour from the example in the book. Instead of lines by the CLI it takes in content from a text file. The code in main.go ended up like this.

```
package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	counts := make(map[string]int)
	files := os.Args[1:]
	if len(files) == 0 {
		countLines(os.Stdin, counts)
	} else {
		for _, arg := range files {
			f, err := os.Open(arg)
			if err != nil {
				fmt.Printf("The Error Happened! %s", os.Stderr)
				continue
			}
			countLines(f, counts)
			errFile := f.Close()
			if errFile != nil {
				fmt.Println("Holy moley the file didn't close correctly!")
			}
		}
	}
	for line, n := range counts {
		if n > 1 {
			fmt.Printf("%d\t%s\n", n, line)
		}
	}
}

func countLines(f *os.File, counts map[string]int) {
	input := bufio.NewScanner(f)
	for input.Scan() {
		counts[input.Text()]++
	}
}
```

[View the gist on GitHub](https://gist.github.com/Adron/3c22e6880e347b95863f980b88af3b96/b446cfec3aa369bf91e53e364ed2199740a42b8a/main.go)

Then if you’d like to check out the text file and remaining content in that project, check out the master branch of the [episode 2 repo](https://github.com/Adron/learning-go-episode-2).

[36:34](https://youtu.be/HQbUjUiMVY0/watch?v=HQbUjUiMVY0&t=2194s) – Here I take a thorough step through committing this project to github, which is the included repo in this post. However I step through the interface of using Jetbrains Goland to do the commit, how it enables `gofmt` and other features to improve the condition of code and ensure it meets linter demands and related crtieria. I also cover the .gitignore file and other elements to create a usable repository.
[44:30](https://youtu.be/HQbUjUiMVY0/watch?v=HQbUjUiMVY0&t=2670s) – Setting up the repository for today’s code at [https://github.com/Adron/learning-go-…](/redirect?v=HQbUjUiMVY0&redir_token=yCyuEJdFPbeNJLUrd2VVPr3FgCZ8MTU0OTUyOTE3MUAxNTQ5NDQyNzcx&event=video_description&q=https%3A%2F%2Fgithub.com%2FAdron%2Flearning-go-episode-2)
[50:00](https://youtu.be/HQbUjUiMVY0/watch?v=HQbUjUiMVY0&t=3000s) – Setup of the key again for using Github. How to setup your ssh keys using ssh-keygen.
[56:00](https://youtu.be/HQbUjUiMVY0/watch?v=HQbUjUiMVY0&t=3360s) – Going beyond just the language, and building out a Go build on Travis CI.
[1:10:16](https://youtu.be/HQbUjUiMVY0/watch?v=HQbUjUiMVY0&t=4216s) – Creating a new branch for the next code examples and topics. At this point I shift into type declarations. Working through some constants, very basic function declarations, and related capabilities to calculate temperatures between Fahrenheit and Celsius.

The [tempApp Branch](https://github.com/Adron/learning-go-episode-2/tree/tempApp) is available in the repository [here](https://github.com/Adron/learning-go-episode-2/tree/tempApp).

At this point I shift into type declarations. Working through some constants, very basic function declarations, and related capabilities to calculate temperatures between Fahrenheit and Celsius.

During this point, we take a look at our first package. This package ended up looking like this.

```
package tempconv

type Celsius float64
type Fahrenheit float64

const (
	AbsoluteZeroC Celsius = -273.15
	FreezingC     Celsius = 0
	BoilingC      Celsius = 100
)

func CelsiusToFahrenheit(c Celsius) Fahrenheit {
	return Fahrenheit(c*9/5 + 32)
}

func FahrenheitToCelsius(f Fahrenheit) Celsius {
	return Celsius((f – 32) * 5 / 9)
}
```

[View the gist on GitHub](https://gist.github.com/Adron/c867124293511b955fae331ff70b5630/7dd2b519871d113e0e1bc599b19f379808098847/temperatureConversion.go)

In the main.go file, I showed how you can use this package by adding a respective import shown in this code.

```
package main

import (
	"fmt"
	tempconv "github.com/Adron/awesomeProject/tempconv"
)

func main() {
	fmt.Println("Temperatures are hard to figure off the top of one's mind!")

	boilingF := tempconv.CelsiusToFahrenheit(BoilingC)

	fmt.Printf("%v\n", boilingF)
	fmt.Printf("%s\n", boilingF)
	fmt.Println(boilingF)
	fmt.Printf("%g\n", boilingF)
}
```

[View the gist on GitHub](https://gist.github.com/Adron/ab76c8e797d56be908c3469ad8151d0f/377393ba157836be8603a97d7887909cefadc09e/main.go)

[1:17:54](https://youtu.be/HQbUjUiMVY0/watch?v=HQbUjUiMVY0&t=4674s) – At this point, to increase readability of font sizes I get into the various Goland IDE options.
[1:38:12](https://youtu.be/HQbUjUiMVY0/watch?v=HQbUjUiMVY0&t=5892s) – Creating the final branch for this session to pull in a public package and use it in project. For this, I pull in a random data generation package to use in some application code.

```
package main

import (
	"fmt"

	randomdata "github.com/Pallinder/go-randomdata"
)

func main() {
	// Print a random silly name
	fmt.Println(randomdata.SillyName())

	// Print a male title
	fmt.Println(randomdata.Title(randomdata.Male))

	// Print a female title
	fmt.Println(randomdata.Title(randomdata.Female))

	// Print a title with random gender
	fmt.Println(randomdata.Title(randomdata.RandomGender))

	// Print a male first name
	fmt.Println(randomdata.FirstName(randomdata.Male))

	// Print a female first name
	fmt.Println(randomdata.FirstName(randomdata.Female))

	// Print a last name
	fmt.Println(randomdata.LastName())

	// Print a male name
	fmt.Println(randomdata.FullName(randomdata.Male))

	// Print a female name
	fmt.Println(randomdata.FullName(randomdata.Female))

	// Print a name with random gender
	fmt.Println(randomdata.FullName(randomdata.RandomGender))

	// Print an email
	fmt.Println(randomdata.Email())

	// Print a country with full text representation
	fmt.Println(randomdata.Country(randomdata.FullCountry))

	// Print a country using ISO 3166-1 alpha-2
	fmt.Println(randomdata.Country(randomdata.TwoCharCountry))

	// Print a country using ISO 3166-1 alpha-3
	fmt.Println(randomdata.Country(randomdata.ThreeCharCountry))

	// Print BCP 47 language tag
	fmt.Println(randomdata.Locale())

	// Print a currency using ISO 4217
	fmt.Println(randomdata.Currency())

	// Print the name of a random city
	fmt.Println(randomdata.City())

	// Print the name of a random american state
	fmt.Println(randomdata.State(randomdata.Large))

	// Print the name of a random american state using two chars
	fmt.Println(randomdata.State(randomdata.Small))

	// Print an american sounding street name
	fmt.Println(randomdata.Street())

	// Print an american sounding address
	fmt.Println(randomdata.Address())

	// Print a random number >= 10 and < 20
	fmt.Println(randomdata.Number(10, 20))

	// Print a number >= 0 and < 20
	fmt.Println(randomdata.Number(20))

	// Print a random float >= 0 and < 20 with decimal point 3
	fmt.Println(randomdata.Decimal(0, 20, 3))

	// Print a random float >= 10 and < 20
	fmt.Println(randomdata.Decimal(10, 20))

	// Print a random float >= 0 and < 20
	fmt.Println(randomdata.Decimal(20))

	// Print a bool
	fmt.Println(randomdata.Boolean())

	// Print a paragraph
	fmt.Println(randomdata.Paragraph())

	// Print a postal code
	fmt.Println(randomdata.PostalCode("SE"))

	// Print a set of 2 random numbers as a string
	fmt.Println(randomdata.StringNumber(2, "-"))

	// Print a set of 2 random 3-Digits numbers as a string
	fmt.Println(randomdata.StringNumberExt(2, "-", 3))

	// Print a random string sampled from a list of strings
	fmt.Println(randomdata.StringSample("my string 1", "my string 2", "my string 3"))

	// Print a valid random IPv4 address
	fmt.Println(randomdata.IpV4Address())

	// Print a valid random IPv6 address
	fmt.Println(randomdata.IpV6Address())

	// Print a browser's user agent string
	fmt.Println(randomdata.UserAgentString())

	// Print a day
	fmt.Println(randomdata.Day())

	// Print a month
	fmt.Println(randomdata.Month())

	// Print full date like Monday 22 Aug 2016
	fmt.Println(randomdata.FullDate())

	// Print full date <= Monday 22 Aug 2016
	fmt.Println(randomdata.FullDateInRange("2016-08-22"))

	// Print full date >= Monday 01 Aug 2016 and <= Monday 22 Aug 2016
	fmt.Println(randomdata.FullDateInRange("2016-08-01", "2016-08-22"))

	// Print phone number according to e.164
	fmt.Println(randomdata.PhoneNumber())

	// Get a complete and randomised profile of data generally used for users
	// There are many fields in the profile to use check the Profile struct definition in fullprofile.go
	profile := randomdata.GenerateProfile(randomdata.Male | randomdata.Female | randomdata.RandomGender)
	fmt.Printf("The new profile's username is: %s and password (md5): %s\n", profile.Login.Username, profile.Login.Md5)

	// Get a random country-localised street name for Great Britain
	fmt.Println(randomdata.StreetForCountry("GB"))
	// Get a random country-localised street name for USA
	fmt.Println(randomdata.StreetForCountry("US"))

	// Get a random country-localised province for Great Britain
	fmt.Println(randomdata.ProvinceForCountry("GB"))
	// Get a random country-localised province for USA
	fmt.Println(randomdata.ProvinceForCountry("US"))
}
```

[View the gist on GitHub](https://gist.github.com/Adron/52c8a882ead33f808a826b979b92776f/2976b3ac6713d9d4e846bee90262ae1247166f97/main.go)

[1:44:50](https://youtu.be/HQbUjUiMVY0/watch?v=HQbUjUiMVY0&t=6290s) – Further discussion and explanation of what to include in .gitignore files to manage projects, but also what is and isn’t included for dependencies and other details around all of this.
[2:13:22](https://www.youtube.com/watch?v=HQbUjUiMVY0&t=8002s) – The wicked awesome hacker outtro.
