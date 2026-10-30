---
title: Go Library Data Generation Timings
date: 2018-06-30 23:11:21 -0700
last_modified_at: 2018-07-08 17:51:15 -0700
permalink: /2018/06/30/go-library-data-generation-timings/
slug: go-library-data-generation-timings
wp_id: 14257
original_url: https://compositecode.blog/2018/06/30/go-library-data-generation-timings/
categories:
- golang
tags:
- benchmark
- data
- data generation
- go
- golang
- random data
- timing
excerpt: 'Recently I put together some quick code to give some timings on the various data generation libraries available for Go. For each library there were a few key pieces of data generation I wanted to time: First Name – basically a first name of some sort, like Adam, Nancy, or Frank. Full Name – something …'
image: /wp-content/uploads/2018/05/dd-logo.jpg
---

Recently I put together some quick code to give some timings on the various data generation libraries available for Go. For each library there were a few key pieces of data generation I wanted to time:

- First Name – basically a first name of some sort, like Adam, Nancy, or Frank.
- Full Name – something like Jason McCormick or Sally Smith.
- Address – A basic street address, or whatever the generator might provide.
- User Agent – Such as that which is sent along with the browser response.
- Color – Something like red, blue, green, or other color beyond the basics.
- Email – A fully formed, albeit faked email address.
- Phone – A phone number, ideally with area code and prefix too.
- Credit Card Number – Ideally a properly formed one, which many of the generators seem to provide based on VISA, Mastercard, or related company specifications.
- Sentence – A stand multi-word lorem ipsum based sentence would be perfect.

I went through and searched for libraries that I wanted to try out. Of all the libraries I found I narrowed it down to three specific libraries. When I add the imports for these libraries, by way of how Go works, it gives you the repo locations:

- “github.com/bxcodec/faker” – [faker](https://github.com/bxcodec/faker) – Faker generates data based on a Struct, which is a pretty cool way to determine what type of data you want and to get it returned in a particularly useful format.
- “github.com/icrowley/fake” – [fake](https://github.com/icrowley/fake) – Fake is a library inspired by the ffaker and forgery Ruby gems. Not that you’d be familiar with those, but if you are you have instant insight into how this library works.
- “github.com/malisit/kolpa” – [kolpa](https://github.com/malisit/kolpa) – This is another data generator that creates fake data for various types of data, structures, strings, sentences, and more.

I pulled in the imports for these and then created a function for each, that generates as close to the list above that I could get from the library.

```javascript
import (
	"fmt"
	"github.com/bxcodec/faker"
	"github.com/icrowley/fake"
	"github.com/malisit/kolpa"
	"time"
)
```

The fake data library function for making data generation calls.

```javascript
func fakeDataLib(repeat int) {
	for i := 0; i < repeat; i++ {
		fake.FirstName()
		fake.FullName()
		fake.StreetAddress()
		fake.UserAgent()
		fake.Color()
		fake.EmailAddress()
		fake.Phone()
		fake.Gender()
		fake.CreditCardNum("VISA")
		fake.Sentence()
	}
}
```

The kolpa library function.

```
func kolpaDataLib(repeat int) {
	k := kolpa.C()
	for i := 0; i < repeat; i++ {
		k.FirstName()
		k.Name()
		k.Address()
		k.UserAgent()
		k.Color()
		k.Email()
		k.Phone()
		k.Gender()
		k.PaymentCard()
		k.LoremSentence()
	}
}
```

The faker data library calls wrapped up in a function.

```
func fakerDataLib(repeat int) {
	for i := 0; i < repeat; i++ {
		a := SomeStruct{}
		err := faker.FakeData(&a)
		if err != nil {
			fmt.Println(err)
		}
	}
}
```

Then back to the top of the code file and I'll add the Struct for the faker library.

```
type SomeStruct struct {
	UserName string `faker:"username"`
	FirstNameMale   string `faker:"first_name_male"`
	FirstNameFemale string `faker:"first_name_female"`
	LastName        string `faker:"last_name"`
	Email            string `faker:"email"`
	PhoneNumber string `faker:"phone_number"`
	Word      string `faker:"word"`
	CreditCardNumber string `faker:"cc_number"`
	Name            string `faker:"name"`
	Date string `faker:"date"`
	Time string `faker:"time"`
	Timestamp string `faker:"timestamp"`
	Sentence  string `faker:"sentence"`
	Sentences string `faker:"sentences"`
}
```

Then I executed these functions with simple calls in main as shown. The repeats for generating data I set at 100,000 so that I'd have a large number of records created during each run but also to ensure that during execution it would really show the trend of time generating the data instead of what might be outlier if I only create just a few at a time. Next I added some print statements so I can easily read what the result is.

```
func main() {

	timeFormat := time.Stamp
	t := time.Now

	generationRepeats := 100000

	start := t()
	fmt.Printf("Starting tests with fake library at %s.\n", start.Format(timeFormat))
	fakeDataLib(generationRepeats)
	currentTime := t()
	elapsed := currentTime.Sub(start).Seconds()
	fmt.Printf("It took %.0f seconds to execute the fake library data generation ending at %s.\n\n", elapsed, currentTime.Format(timeFormat))

	kolpaStart := t()
	fmt.Printf("Starting tests with kolpa library at %s.\n", kolpaStart.Format(timeFormat))
	kolpaDataLib(generationRepeats)
	kolpaEnd := t()
	kolpaElapsed := kolpaEnd.Sub(kolpaStart).Seconds()
	fmt.Printf("It took %.0f seconds to execute the kolpa library data generation ending at %s.\n\n", kolpaElapsed, kolpaEnd.Format(timeFormat))

	fakerStart := t()
	fmt.Printf("Starting tests with faker library at %s.\n", fakerStart.Format(timeFormat))
	fakerDataLib(generationRepeats)
	fakerEnd := t()
	fakerElapsed := fakerEnd.Sub(fakerStart).Seconds()
	fmt.Printf("It took %.0f second to execute the faker library data generation ending at %s.\n", fakerElapsed, fakerEnd.Format(timeFormat))
}
```

I ran this via two methods.

`go run main.go`

Then I also built the package and then ran the executable. In both cases the results showed around this range. Mind you, this first execution was done on my Dell XPS 13 Laptop, so by no means a beast of a machine.

> Starting tests with fake library at Jun 30 09:58:57.
> It took 0 seconds to execute the fake library data generation ending at Jun 30 09:58:57.
>
> Starting tests with kolpa library at Jun 30 09:58:57.
> It took 31 seconds to execute the kolpa library data generation ending at Jun 30 09:59:29.
>
> Starting tests with faker library at Jun 30 09:59:29.
> It took 1 second to execute the faker library data generation ending at Jun 30 09:59:30.
>
> Process finished with exit code 0

Wow, what a difference! Kolpa was taking an extremely long time versus the other libraries. That almost instantly narrowed down further examinations to just the fake and faker libraries. But just to be sure I decided I’d try another method and throw in some go routines. I went about that refactor like this.

Just to clean up things a bit I made two immediate changes by adding two new functions to handle the display of messages to the console. This function kicks off with the current time and prints that out with a message of whatever library it is, with that being passed in via a string parameter.

```
func startTiming(library string) (string, func() time.Time, time.Time) {
	timeFormat := time.Stamp
	t := time.Now
	start := t()
	fmt.Printf("Starting tests with %s library at %s.\n", library, start.Format(timeFormat))
	return timeFormat, t, start
}
```

Between execution of the above function, I’d have a closing function to finish the timing, calculate the diff and print that out for total time executing.

```
func finishTiming(t func() time.Time, start time.Time, timeFormat string, library string) {
	currentTime := t()
	elapsed := currentTime.Sub(start).Seconds()
	fmt.Printf("It took about %.0f seconds to execute the %s library data generation ending at %s.\n\n", elapsed, library, currentTime.Format(timeFormat))
}
```

To manage the go routines so they all finish executing I created a global variable to use the sync wait group functionality.

```
var wg sync.WaitGroup
```

Next I refactored the individual functions testing the three libraries. First the faker data function. The startTiming and finishTiming functions are called before and after the data generation is complete, and at the end `defer wg.Done()` is set.

```
func fakerDataLib(repeat int) {
	library := "faker"
	timeFormat, t, start := startTiming(library)

	for i := 0; i < repeat; i++ {
		a := SomeStruct{}
		err := faker.FakeData(&a)
		if err != nil {
			fmt.Println(err)
		}
	}

	finishTiming(t, start, timeFormat, library)
	defer wg.Done()
}
```

On to the next library being tested for kolpa. Maybe, just maybe this will squeeze a little bit more out of it? Naw, not likely.

```
func kolpaDataLib(repeat int) {
	library := "kolpa"
	timeFormat, t, start := startTiming(library)

	k := kolpa.C()
	for i := 0; i < repeat; i++ {
		k.FirstName()
		k.Name()
		k.Address()
		k.UserAgent()
		k.Color()
		k.Email()
		k.Phone()
		k.Gender()
		k.PaymentCard()
		k.LoremSentence()
	}

	finishTiming(t, start, timeFormat, library)
	defer wg.Done()
}
```

Then the fake data generation library refactored.

```
func fakeDataLib(repeat int) {
	library := "fake"
	timeFormat, t, start := startTiming(library)

	for i := 0; i < repeat; i++ {
		fake.FirstName()
		fake.FullName()
		fake.StreetAddress()
		fake.UserAgent()
		fake.Color()
		fake.EmailAddress()
		fake.Phone()
		fake.Gender()
		fake.CreditCardNum("VISA")
		fake.Sentence()
	}

	finishTiming(t, start, timeFormat, library)
	defer wg.Done()
}
```

Alright. Now I can refactor the main function down to a much more minimal amount of code. Adding the wg.Add(3) for the respective routines being initiated below with the addition of the go keyword, and at the end adding a wg.Wait() and deleting a whole bunch of the other redundant code.

```
func main() {
	wg.Add(3)
	generationRepeats := 100000

	go fakeDataLib(generationRepeats)
	go kolpaDataLib(generationRepeats)
	go fakerDataLib(generationRepeats)

	wg.Wait()
}
```

With all those changes, my main.go file contents in totality looks like this. Of course, in totality like this it's a quick copy & paste if you want to give it a try.

```
package main

import (
	"fmt"
	"github.com/bxcodec/faker"
	"github.com/icrowley/fake"
	"github.com/malisit/kolpa"
	"time"
	"sync"
)

type SomeStruct struct {
	UserName string `faker:"username"`
	FirstNameMale   string `faker:"first_name_male"`
	FirstNameFemale string `faker:"first_name_female"`
	LastName        string `faker:"last_name"`
	Email            string `faker:"email"`
	PhoneNumber string `faker:"phone_number"`
	Word      string `faker:"word"`
	CreditCardNumber string `faker:"cc_number"`
	Name            string `faker:"name"`
	Date string `faker:"date"`
	Time string `faker:"time"`
	Timestamp string `faker:"timestamp"`
	Sentence  string `faker:"sentence"`
	Sentences string `faker:"sentences"`
}

var wg sync.WaitGroup

func main() {
	wg.Add(3)
	generationRepeats := 100000

	go fakeDataLib(generationRepeats)
	go kolpaDataLib(generationRepeats)
	go fakerDataLib(generationRepeats)

	wg.Wait()
}

func fakerDataLib(repeat int) {
	library := "faker"
	timeFormat, t, start := startTiming(library)

	for i := 0; i < repeat; i++ {
		a := SomeStruct{}
		err := faker.FakeData(&a)
		if err != nil {
			fmt.Println(err)
		}
	}

	finishTiming(t, start, timeFormat, library)
	defer wg.Done()
}

func kolpaDataLib(repeat int) {
	library := "kolpa"
	timeFormat, t, start := startTiming(library)

	k := kolpa.C()
	for i := 0; i < repeat; i++ {
		k.FirstName()
		k.Name()
		k.Address()
		k.UserAgent()
		k.Color()
		k.Email()
		k.Phone()
		k.Gender()
		k.PaymentCard()
		k.LoremSentence()
	}

	finishTiming(t, start, timeFormat, library)
	defer wg.Done()
}

func fakeDataLib(repeat int) {
	library := "fake"
	timeFormat, t, start := startTiming(library)

	for i := 0; i < repeat; i++ {
		fake.FirstName()
		fake.FullName()
		fake.StreetAddress()
		fake.UserAgent()
		fake.Color()
		fake.EmailAddress()
		fake.Phone()
		fake.Gender()
		fake.CreditCardNum("VISA")
		fake.Sentence()
	}

	finishTiming(t, start, timeFormat, library)
	defer wg.Done()
}

func finishTiming(t func() time.Time, start time.Time, timeFormat string, library string) {
	currentTime := t()
	elapsed := currentTime.Sub(start).Seconds()
	fmt.Printf("It took about %.0f seconds to execute the %s library data generation ending at %s.\n\n", elapsed, library, currentTime.Format(timeFormat))
}

func startTiming(library string) (string, func() time.Time, time.Time) {
	timeFormat := time.Stamp
	t := time.Now
	start := t()
	fmt.Printf("Starting tests with %s library at %s.\n", library, start.Format(timeFormat))
	return timeFormat, t, start
}
```

Executing this it still looks like the libraries performed similarly. Now however I can add record counts a bit more easily to test out. I tried out a thousand records first.

> API server listening at: 127.0.0.1:35455
> Starting tests with faker library at Jun 30 23:00:48.
> Starting tests with fake library at Jun 30 23:00:48.
> Starting tests with kolpa library at Jun 30 23:00:48.
> It took about 0 seconds to execute the fake library data generation ending at Jun 30 23:00:48.
> It took about 1 seconds to execute the faker library data generation ending at Jun 30 23:00:48.
> It took about 5 seconds to execute the kolpa library data generation ending at Jun 30 23:00:53.
>
> Debugger finished with exit code 0

Then bumped it up a bit to ten thousand.

> API server listening at: 127.0.0.1:41509
> Starting tests with faker library at Jun 30 23:01:40.
> Starting tests with fake library at Jun 30 23:01:40.
> Starting tests with kolpa library at Jun 30 23:01:40.
> It took about 0 seconds to execute the fake library data generation ending at Jun 30 23:01:41.
> It took about 5 seconds to execute the faker library data generation ending at Jun 30 23:01:46.
> It took about 52 seconds to execute the kolpa library data generation ending at Jun 30 23:02:32.
>
> Debugger finished with exit code 0

Oh wow. Yeah, with routines executing the different libraries things are getting a bit multiplicative here. Going from 1000 to 10,000 records all of a sudden bumps the fake from sub-zero to sub-zero and the faker lib from ~1 second to 5 seconds, while the kolpa library goes from 5 seconds to a massive 52 seconds. That’s enough for me, next up I’ll tweak the fake and faker libraries a bit and prospectively even use both for future implementations.

…until later, on to next steps!
