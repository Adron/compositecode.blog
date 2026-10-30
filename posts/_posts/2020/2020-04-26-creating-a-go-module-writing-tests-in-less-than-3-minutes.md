---
title: Creating a Go Module & Writing Tests in Less Than 3 Minutes
date: 2020-04-26 17:41:47 -0700
last_modified_at: 2020-04-26 17:41:47 -0700
permalink: /2020/04/26/creating-a-go-module-writing-tests-in-less-than-3-minutes/
slug: creating-a-go-module-writing-tests-in-less-than-3-minutes
wp_id: 16855
original_url: https://compositecode.blog/2020/04/26/creating-a-go-module-writing-tests-in-less-than-3-minutes/
categories:
- golang
- Testing
- Unknown Code Ramblings
tags:
- coding
- programming
- software development
- testing
- unit testing
excerpt: In this short (less than 4 minutes) video I put together a Go module library, then setup some first initial tests calling against functions in the module.
image: /wp-content/uploads/2020/04/golang-rocker.png
---

In this short (less than 4 minutes) video I put together a Go module library, then setup some first initial tests calling against functions in the module.

<iframe allowfullscreen="allowfullscreen" class="fluidvids-elem" data-mce-fragment="1" height="399" loading="lazy" src="https://www.youtube.com/embed/Qs7vHHQPv18" width="710"></iframe>

[00:12](https://www.youtube.com/watch?v=Qs7vHHQPv18&t=12s) – Writing unit tests.

[00:24](https://www.youtube.com/watch?v=Qs7vHHQPv18&t=24s) – Create the first go file.

[00:40](https://www.youtube.com/watch?v=Qs7vHHQPv18&t=40s) – Creating the Go go.mod file. When creating the go.mode file, note the command is go mod init [repopath] where repopath is the actual URI to the repo. The go.mod file that is generated would look like this.

```go
module github.com/adron/awesomeLib

go 1.13
```

[00:56](https://www.youtube.com/watch?v=Qs7vHHQPv18&t=56s) – [Enabling Go mod integration](https://blog.jetbrains.com/go/2020/02/26/working-with-go-modules-getting-started/) for Goland IDE. This dialog has an option to turn off the proxy or go direct to repo bypassing the proxy. For more details on the Go proxy, check out [goproxy.io](https://goproxy.io/) and the [Go docs for more details](https://blog.golang.org/using-go-modules).

[01:09](https://www.youtube.com/watch?v=Qs7vHHQPv18&t=69s) – Instead of TDD, first I cover a simple function implementation. Note the casing is very important in setting up a test in Go. The test function needs to be public, thus capitalized, and the function needs accessible, thus also capitalized. The function in the awesomeLib.go file, just to have a function that would return some value, looks like this.

```go
package awesomeLib

func GetKnownResult() string {
    return "known"
}
```

[01:30](https://www.youtube.com/watch?v=Qs7vHHQPv18&t=90s) – Creating the test file, awesomeLib\_test.go, then creating the test. In this I also show some of the features of the Goland IDE that extracts and offers the function names of a module prefaced with Test and other naming that provides they perform a test, performance, or related testing functionality.

```go
package awesomeLib

import "testing"

func TestGetKnownResult(t *testing.T) {
    got := GetKnownResult()
    if got != "known" {
        t.Error("Known result not received, test failed.")
    }
}
```

[02:26](https://www.youtube.com/watch?v=Qs7vHHQPv18&t=146s) – Running the standard `go test` to execute the test. To run tests for all files within this module, such as if we’ve added multiple directories and other files, would be `go test ./...`.

[02:36](https://www.youtube.com/watch?v=Qs7vHHQPv18&t=156s) – Using Goland to run the tests with singular or multiple tests being executed. With Goland there are other capabilities to show test coverage, what percentage of functionality is covered by tests, and other various code metrics around testing, performance, and other telemetry.

That’s it, now the project is ready for elaboration and is setup for a TDD, BDD, or implement and test style approach to development.

For JavaScript, Go, Python, Terraform, and more infrastructure, web dev, and coding in general I stream regularly on Twitch at <https://twitch.tv/adronhall>, post the VOD’s to YouTube along with entirely new tech and *metal* content at <https://youtube.com/c/ThrashingCode>.
