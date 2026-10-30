---
title: Learning Go Episode 5 – Functions (and Methods and lots of other things)
date: 2019-07-05 15:33:02 -0700
last_modified_at: 2019-07-05 19:39:49 -0700
permalink: /2019/07/05/learning-go-episode-5-functions-and-methods-and-lots-of-other-things/
slug: learning-go-episode-5-functions-and-methods-and-lots-of-other-things
wp_id: 15986
original_url: https://compositecode.blog/2019/07/05/learning-go-episode-5-functions-and-methods-and-lots-of-other-things/
categories:
- golang
- ThrashingCode
tags:
- coding
- go
- golang
- learning
- programming
- software development
excerpt: 'Episode Post & Video Links: 1, 2, 3, 4, 5 (this post), 6, 7, and 8. Non-linked are in the works! Videos available now on Youtube however, so check em’ out! In this session we covered a host of topics around Go Functions. Along with some troubleshooting, debugging, and other features in Jetbrains Goland IDE. …'
image: /wp-content/uploads/2018/10/thrashing-code-metal-gopher.png
---

Episode Post & Video Links:  [1](/2019/01/19/learning-go-episode-1/), [2](/2019/02/06/learning-go-episode-2-further-into-packages-dependencies-application-creation-and-ides/), [3](/2019/03/10/learning-go-episode-3-more-data-types-casting-rendering-an-svg-file-and-writing-to-files/), [4](/2019/05/27/learning-go-episode-4-composite-types-slices-arrays-etc/), 5 (this post), 6, 7, and 8. Non-linked are in the works! Videos [available now on Youtube](https://www.youtube.com/playlist?list=PL4f75Y6Ce5ssiDTjB0Y_D7a-13eeAepHn) however, so check em’ out!

In this session we covered a host of topics around Go Functions. Along with some troubleshooting, debugging, and other features in Jetbrains Goland IDE.

If you’d like to go through this material too in book form, I highly suggest “The Go Programming Language” by Alan A.A. Donovan & Brian W. Kernighan as a starting point. I’m using it as a simple guideline, but also doing a lot more in each stream that includes ecosystem, dependency management with godep, IDE use of [Goland](https://www.jetbrains.com/go/) from [Jetbrains](https://www.jetbrains.com/), and more. In this session I get specifically into: functions, signatures, declarations, recursion, return values, and more.

<iframe allowfullscreen="true" class="youtube-player" height="486" loading="lazy" sandbox="allow-scripts allow-same-origin allow-popups allow-presentation allow-popups-to-escape-sandbox" src="https://www.youtube.com/embed/FVGN1GAsHOA?version=3&amp;rel=1&amp;showsearch=0&amp;showinfo=1&amp;iv_load_policy=1&amp;fs=1&amp;hl=en-US&amp;autohide=2&amp;wmode=transparent" style="border:0;" width="863"></iframe>

## Video Time Points & Topics

[2:50](https://www.youtube.com/watch?v=FVGN1GAsHOA&t=170s) – Introduction to the snowy wonderland of Seattle and episode 5 of the Learning Go series. Introduction to the various screen transitions and such.
[6:40](https://www.youtube.com/watch?v=FVGN1GAsHOA&t=400s) – Getting started, opening up JetBrains Goland and creating a new project. The project exists on Github as [https://github.com/adron/learning-go-…](https://www.youtube.com/redirect?v=FVGN1GAsHOA&redir_token=jHg5w8O8VkpX51WcfTomZB8EwJF8MTU2MjQ1MDA1NUAxNTYyMzYzNjU1&event=video_description&q=https%3A%2F%2Fgithub.com%2Fadron%2Flearning-go-episode-5).
[12:18](https://www.youtube.com/watch?v=FVGN1GAsHOA&t=738s) – Starting with functions in Go. See the blog entry I wrote on the topic for more additional information around this first code session within the episode 5 session.

Code – This first example I setup a basic function in Go that is called by the main function. The sample function below I’ve named exampleExecutor, and the signature is made up of an int parameter called this, a string parameter called that, and a return parameter of type int and one of type string. In summary for the function signature we have two input parameters going in and two return parameters coming out.

The function does very little besides print the parameters passed in and then return the parameters back out as the return parameters.

```
package main

import "fmt"

func main() {

	var this, result int
	var that, message string
	this = 2
	that = "42"

	result, message = exampleExecutor(this, that)

	fmt.Printf("%s\n%d", message, result)
}

func exampleExecutor(this int, that string) (int, string) {

	fmt.Printf("Numbers: %d, %s\n", this, that)

	return this, "This is the result: " + that
}
```

[View the gist on GitHub](https://gist.github.com/Adron/22707c9175759a43f2538abdbcd2af6d/4e918ff36ed5eee4674ef09330c3f88b80587abf/func_main_plus_example_executor.go)

### Recursion with Go & HTML Parsing

[28:10](https://www.youtube.com/watch?v=FVGN1GAsHOA&t=1690s) – Here I get into recursion and the application example, largely taken from the book but with some very distinctive modifications, that parses HTML and the various nodes within an HTML document.

For the recursion section I use an example from the book with an expanded sample set of HTML. The HTML is included in the repo under the [function-recursion branch](https://github.com/Adron/learning-go-episode-5/tree/function-recursion). For this example I setup a set of types and variables up that are needed throughout the code.

First a type setup called NodeType of type int32. A constant array of ErrorNode, TextNode, DocumentNode, ElementNode, CommentNode, and DoctypeNode for determining the different nodes within an HTML document. Then a general struct called Node with Type, Data, Attr for attribute, and FirstChild with NextSibling setup as a pointer to \*Node, which gives a type of memory recursion to the underlying type. Then finally the Attribute struct with a Key a Value.

```
type NodeType int32

const (
 ErrorNode NodeType = iota
 TextNode
 DocumentNode
 ElementNode
 Commentnode
 DoctypeNode
)

type Node struct {
 Type NodeType
 Data string
 Attr                    []Attribute
 FirstChild, NextSibling *Node
}

type Attribute struct {
 Key, Val string
}
```

[View the gist on GitHub](https://gist.github.com/Adron/a82f44803107b169f5916d212077de87/934a93896d7d42d3cb78f9ae6bb4fa9495dbfe66/types_nodes_etc.go)

One of the first functions I then end up with is the visit function. It turns out as shown below. Here the function takes a links parameter that is of type string array, a parameter name n that is a pointer reference to an a node within html, and then the function returns a parameter of type string array.

```
func visit(links []string, n *html.Node) []string {
	if n.Type == html.ElementNode && n.Data == "a" {
		for _, a := range n.Attr {
			if a.Key == "href" {
				links = append(links, a.Val)
			}
		}
	}
	for c := n.FirstChild; c != nil; c = c.NextSibling {
		links = visit(links, c)
	}
	return links
}
```

[View the gist on GitHub](https://gist.github.com/Adron/894f3e63e426793adfb2ec59ad04cccb/8c26d44541e15b9cbfd515c365837f0f2e244907/visit_func.go)

After that function I worked through and created two additional functions, one for countsWordsAndImages and one called CountWordsAndImages. The casing being specific to scope and use of the functions, and they respectively look like this in completion.

```
func CountWordsAndImages(url string) (words, images int, err error) {
	resp, err := http.Get(url)

	if err != nil {
		return
	}

	doc, err := html.Parse(resp.Body)
	resp.Body.Close()
	if err != nil {
		err = fmt.Errorf("parsing HTML: %s", err)
	}
	words, images = countWordsAndImages(doc)
	return
}

func countWordsAndImages(n *html.Node) (words, images int) {
	if n.Type == html.TextNode {
		words += len(strings.Split(n.Data, " "))
		return
	}

	if n.Data == "img" {
		images++
	} else {
		if n.FirstChild != nil {
			w, i := countWordsAndImages(n.FirstChild)
			words += w
			images += i
		}
		if n.NextSibling != nil {
			w, i := countWordsAndImages(n.NextSibling)
			words += w
			images += i
		}
	}
	return
}
```

[View the gist on GitHub](https://gist.github.com/Adron/3ff88fb9749227f82b964bc0de0a7e2c/4616fbb9b25d6f5ce830b134d32b76dd4c2f6a6a/counting.go)

Then all that is wrapped up, with recursive calls and more, in the main function for program execution.

```
func main() {

	htmlContent, err := ioutil.ReadFile("compositecode.html")
	if err != nil {
		fmt.Println(err)
	}

	htmlData := string(htmlContent)
	r := strings.NewReader(htmlData)

	doc, err := html.Parse(r)
	if err != nil {
		fmt.Fprintf(os.Stderr, "find links: %v\n", err)
		os.Exit(1)
	}
	for _, link := range visit(nil, doc) {
		fmt.Println(link)
	}

	w, i, _ := CountWordsAndImages("https://compositecode.blog&quot;)
	fmt.Printf("Words: %d\nImages: %d\n", w, i)
}
```

[View the gist on GitHub](https://gist.github.com/Adron/de1693ba971e2df7ea1857bfcf31dda5/9b4ac6e71c91c3b61233671999bf896879f444a5/TheCountingRecursionOfThings.go)

### Starting Error Handling && Anonymous Functions

[1:32:40](https://www.youtube.com/watch?v=FVGN1GAsHOA&t=5560s) – At this point in the episode 5 session I get into a simple Error handling function, and further into function signatures and how to set them up.
[1:52:24](https://www.youtube.com/watch?v=FVGN1GAsHOA&t=6744s) – Setting up some anonymous functions and reviewing what they are.
[1:59:00](https://www.youtube.com/watch?v=FVGN1GAsHOA&t=7140s) – Introduction to panics in Go. After this short introduction I also discuss some of the pedantic specifics of methods vs functions and related verbiage around the Go language. Additionally I provide more examples around these specifics for declaring functions, various scope, and other types for function calls and related usage.

With that done the wrap up of the session is then a short introduction to anonymous functions.
