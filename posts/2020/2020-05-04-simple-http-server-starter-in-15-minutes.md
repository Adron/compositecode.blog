---
title: Simple Go HTTP Server Starter in 15 Minutes
date: 2020-05-04 07:26:33 -0700
last_modified_at: 2020-05-09 13:35:40 -0700
permalink: /2020/05/04/simple-http-server-starter-in-15-minutes/
slug: simple-http-server-starter-in-15-minutes
wp_id: 16870
original_url: https://compositecode.blog/2020/05/04/simple-http-server-starter-in-15-minutes/
categories:
- golang
- Unknown Code Ramblings
tags:
- coding
- golang
- http
- programming
- software development
- status codes
- web server
excerpt: In this post I cover putting together a simple http server with a video on creating the http server, setting a status code, which provides the basic elements you need to further build out a fully featured server. This post is paired with a video too.
image: /wp-content/uploads/2018/10/gopher-metal-head.jpg
---

This is a quick starter, to show some of the features of Go’s http library. ([sample repo here](https://github.com/Adron/coro-era-coding-go-sample)) The [docs](https://golang.org/pkg/net/http/) for the library are located [here](https://golang.org/pkg/net/http/) if you want to dig in deeper. In this post however I cover putting together a simple http server with a video on creating the http server, setting a status code, which provides the basic elements you need to further build out a fully featured server. This post is paired with a video I’ve put together, included below.

<iframe allowfullscreen="allowfullscreen" class="fluidvids-elem" data-mce-fragment="1" height="399" loading="lazy" src="https://www.youtube.com/embed/xQkJ7ZRA-BI" width="710"></iframe>

[00:15](https://www.youtube.com/watch?v=xQkJ7ZRA-BI&t=15s) Reference to the Github Repo where I’ve put the code written in this sample.
<https://github.com/Adron/coro-era-coding-go-sample>
[00:18](https://www.youtube.com/watch?v=xQkJ7ZRA-BI&t=18s) Using Goland IDE (Jetbrains) to clone the repository from Github.
[00:40](https://www.youtube.com/watch?v=xQkJ7ZRA-BI&t=40s) Creating code files.
[01:00](https://www.youtube.com/watch?v=xQkJ7ZRA-BI&t=60s) Pasted in some sample code, and review the code and what is being done.
[02:06](https://www.youtube.com/watch?v=xQkJ7ZRA-BI&t=126s) First run of the web server.
[02:24](https://www.youtube.com/watch?v=xQkJ7ZRA-BI&t=144s) First function handler to handle the request and response of an HTTP request and response cycle.
[04:56](https://www.youtube.com/watch?v=xQkJ7ZRA-BI&t=296s) Checking out the response in the browser.
[05:40](https://www.youtube.com/watch?v=xQkJ7ZRA-BI&t=340s) Checking out the same interaction with Postman. Also adding a header value and seeing it returned via the browser & related header information.
[09:28](https://www.youtube.com/watch?v=xQkJ7ZRA-BI&t=568s) Starting the next function to provide further HTTP handler functionality.
[10:08](https://www.youtube.com/watch?v=xQkJ7ZRA-BI&t=608s) Setting the status code to 200.
[13:28](https://www.youtube.com/watch?v=xQkJ7ZRA-BI&t=808s) Changing the status code to 500 to display an error.

## Getting a Server Running

I start off the project by pulling an empty repository that I had created before starting the video. In this I use the Jetbrains Goland IDE to pull this repository from Github.

![1](/wp-content/uploads/2020/05/1.jpg)

Next I create two files; `main.go` and `main_test.go`. We won’t use the `main_test.go` file right now, but in a subsequent post I’ll put together some unit tests specifically to test out our HTTP handlers we’ll create. Once those are created I pasted in some code that just has a basic handler, using an anonymous function, provides some static file hosting, and then sets up the server and starts listening. I make a few tweaks, outlined in the video, and execute a first go with the following code.

```go
package main

import (
    "fmt"
    "net/http"
)

func main() {
    http.HandleFunc("/", func (w http.ResponseWriter, r *http.Request) {
        fmt.Fprintf(w, "Welcome to my website!")
    })

    http.ListenAndServe(":8080", nil)
}
```

When that executes, opening a browser to localhost:8080 will bring up the website which then prints out “Welcome to my website!”.

![2](/wp-content/uploads/2020/05/2.jpg)

## Adding a Function as an HTTP Handler

The next thing I want to add is a function that can act as an HTTP handler for the server. To do this create a function just like we’d create any function in Go. For this example, the function I built included several print line calls to the `ResponseWriter` with `Request` properties and a string passed in.

```go
func RootHandler(w http.ResponseWriter, r *http.Request){
    fmt.Fprintln(w, "This is my content.")
    fmt.Fprintln(w, r.Header)
    fmt.Fprintln(w, r.Body)
}
```

In the `func main` I changed out the root handler to use this newly created handler instead of the anonymous function that it currently has in place. So swap out this…

```go
http.HandleFunc("/", func (w http.ResponseWriter, r *http.Request) {
    fmt.Fprintf(w, "Welcome to my website!")
})
```

with this…

```go
http.HandleFunc("/", RootHandler)
```

Now the full file reads as shown.

```go
package main

import (
    "fmt"
    "net/http"
)

func main() {
    http.HandleFunc("/", RootHandler)
    http.ListenAndServe(":8080", nil)
}
```

Now executing this and navigating to localhost:8080 will display the following.

![3](/wp-content/uploads/2020/05/3.jpg)

The string is displayed first “This is my content.”, then the header, and body respectively. The body, we can see is empty. Just enclosed with two braces `{}`. The header is more interesting. It is returned as a map type, between the brackets `[]`. Showing an accept, accept-encoding, accept-language, user-agent, and other header information that was passed.

This is a good thing to explore further, check out how to view or set the values associated with the header values in HTTP responses, requests, and their related metadata. To go a step further, and get into this metadata a tool like Postman comes in handy. I open this tool up, setup a GET request and add an extra header value just to test things out.

![4](/wp-content/uploads/2020/05/4.jpg)

## Printing Readable Body Contents

For the next change I wanted to get a better print out of body contents, as the previous display was actually just attempting to print out the body in an unreadable way. In this next section I used an `ioutil` function to get the body to print out in a readable format. The `ioutil.ReadAll` function takes the body, then I retrieve a `body` variable with the results, pending no error, the body variable is then cast as a string and print out to the `ResponseWriter` on the last line. The RootHandler function then reads like this with the changes.

```go
func RootHandler(w http.ResponseWriter, r *http.Request){
    fmt.Fprintln(w, "This is my content.")
    fmt.Fprintln(w, r.Header)

    defer r.Body.Close()

    body, err := ioutil.ReadAll(r.Body)
    if err != nil {
        fmt.Fprintln(w, err)
    }
    fmt.Fprintln(w, string(body))
}
```

If the result is then requested using Postman again, the results now display appropriately!

![5](/wp-content/uploads/2020/05/5.jpg)

## Response Status Codes!

HTTP Status codes fit in to a set of ranges for various categories of responses. The most common code is of course the success code, which is 200 “Status OK”. Another common one is status code 500, which is a generic catch all for “Server Error”. The ranges are as follows:

- Informational responses (100–199)
- Successful responses (200–299)
- Redirects (300–399)
- Client errors (400–499)
- and Server errors (500–599)

For the next function, to get an example working of how to set this status code, I added the following function.

```go
func ResponseExampleHandler(w http.ResponseWriter, r *http.Request) {
    w.WriteHeader(200)
    fmt.Fprintln(w, "Testing status code. Manually added a 200 Status OK.")
    fmt.Fprintln(w, "Another line.")
}
```

With that, add a handler to the `main` function.

```go
http.HandleFunc("/response", ResponseExampleHandler)
```

Now we’re ready to try that out. In the upper right of Postman, the 200 status is displayed. The other data is shown in the respective body & header details of the response.

![6](/wp-content/uploads/2020/05/6.jpg)

Next up, let’s just write a function specifically to return an error. We’ll use the standard old default 500 status code.

```go
func ErrorResponseHandler(w http.ResponseWriter, r *http.Request) {
    w.WriteHeader(500)
    fmt.Fprintln(w, "Server error.")
}
```

Then in `main`, as before, we’ll add the http handle for the function handler.

```go
http.HandleFunc("/errexample", ErrorResponseHandler)
```

Now if the server is run again and an HTTP request is sent to the end point, the status code changes to 500 and the message “Server error.” displays on the page.

![7](/wp-content/uploads/2020/05/7.jpg)

## Summary

That’s a quick intro to writing an HTTP server with Go. From here, we can take many next steps such as writing tests to verify the function handlers, or setup a Docker image in which to deploy the server itself. In subsequent blog entries I’ll write up just those and many other step by step procedures. For now, a great next step is to expand on trying out the different functions and features of the http library.

That’s it for now. However, if you’re interested in joing me to write some JavaScript, Go, Python, Terraform, and more infrastructure, web dev, and coding in general I stream regularly on Twitch at <https://twitch.tv/adronhall>, post the VOD’s to YouTube along with entirely new tech and *metal* content at <https://youtube.com/c/ThrashingCode>. Feel free to check out a coding session, ask questions, interject, or just come and enjoy the tunes!
