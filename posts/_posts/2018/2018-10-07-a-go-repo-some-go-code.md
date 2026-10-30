---
title: A Go Repo & Some Go Code
date: 2018-10-07 19:26:45 -0700
last_modified_at: 2018-10-08 11:01:10 -0700
permalink: /2018/10/07/a-go-repo-some-go-code/
slug: a-go-repo-some-go-code
wp_id: 14709
original_url: https://compositecode.blog/2018/10/07/a-go-repo-some-go-code/
categories:
- golang
tags:
- coding
- core libraries
- go
- golang
- javascript object notation
- json
- programming
excerpt: Wrapped up another Twitch stream (follow here) and streamed live via YouTube where the video is now (subscribe here, video here). However the more interesting part IMHO was where I broke down a few key parts of the application building features around file writes, reads, JSON marshalling, and some other functionality. I also put together …
image: /wp-content/uploads/2018/10/thrashing-code-metal-gopher.png
---

Wrapped up another Twitch stream ([follow here](https://www.twitch.tv/)) and streamed live via YouTube where the video is now ([subscribe here](https://www.youtube.com/channel/UCHSCXYCMOOS-VSUdRsn13GQ), [video here](https://youtu.be/sg4Nnnb-Vvc)). However the more interesting part IMHO was where I broke down a few key parts of the application building features around file writes, reads, JSON marshalling, and some other functionality. I also put together a repo of the code I put together [here on Github](https://github.com/Adron/Thrashing_Code_Sample_001) (code shown and explained below). I dove into this topic in the later part of the stream which I’ve time tagged below. For the full timeline and the rest of the video just watch from the beginning of the video. I do make some progress working on [Colligere](https://github.com/ThrashingCode/colligere), but I’ll cover that topic in a subsequent blog entry and Twitch stream.

<iframe allowfullscreen="true" class="youtube-player" height="486" loading="lazy" sandbox="allow-scripts allow-same-origin allow-popups allow-presentation allow-popups-to-escape-sandbox" src="https://www.youtube.com/embed/sg4Nnnb-Vvc?version=3&amp;rel=1&amp;showsearch=0&amp;showinfo=1&amp;iv_load_policy=1&amp;fs=1&amp;hl=en-US&amp;autohide=2&amp;start=5565&amp;wmode=transparent" style="border:0;" width="863"></iframe>

- [1:32:40](https://youtu.be/sg4Nnnb-Vvc?t=5560s) – Creating a new application with [Jetbrains Goland](https://www.jetbrains.com/go/) to show off how to use the Go core libraries around the user, JSON, and some basic file creation and writing.
- [1:36:40](https://youtu.be/sg4Nnnb-Vvc?t=5800s) – At this point I start adding some basic code to pull the current user and collect some information about that user.
- [1:40:42](https://youtu.be/sg4Nnnb-Vvc?t=6042s) – I extract the error code using the [Goland](https://www.jetbrains.com/go/) refactoring feature and setup a `func check()` for error checking. That cleans up the inline code a bit.
- [1:43:10](https://youtu.be/sg4Nnnb-Vvc?t=6190s) – Here I add to the user data retrieved some environment variables to that list of collected data. I also cover again, as I have a number of times, how the environment variables are pulled in IDE versus user session versus out of IDE.
- [1:47:46](https://youtu.be/sg4Nnnb-Vvc?t=6466s) – Now I add a file exists check and start working on that logic.
- [1:48:56](https://youtu.be/sg4Nnnb-Vvc?t=6536s) – Props to Edd Turtle on a solid site on Go. Here’s the blog entry, and respectively the path to more of Edd’s material @ <https://golangcode.com/>. Also, Edd seems like a good guy to follow [@eddturtle](https://twitter.com/eddturtle).
- [2:01:33](https://youtu.be/sg4Nnnb-Vvc?t=7293s) – Starting the JSON Work here to marshal and unmarshall.
- [2:26:33](https://youtu.be/sg4Nnnb-Vvc?t=8793s) – At this point I push the code up to [Github](https://www.github.com/) ([repo here](https://github.com/Adron/Thrashing_Code_Sample_001)) using the built in [Goland](https://www.jetbrains.com/go/) VCS features. I realize I’ve named the repo “adron” by accident so I rename it, close [Goland](https://www.jetbrains.com/go/), and then clone the code back down locally with [Goland’s](https://www.jetbrains.com/go/) VCS features. It’s kind of interesting to see [Goland](https://www.jetbrains.com/go/) go through the 2-factor auth for this too.
- [2:58:56](https://youtu.be/sg4Nnnb-Vvc?t=10736s) – The Seattle Thrashing Code outtro!

There were a few notes I took during the session with my collected links and references for things I looked up. Those included the following:

- File Modes for Go folder creation: <https://golang.org/pkg/os/#FileMode>
- My ref letter & number. File permissions: <https://www-s.acm.illinois.edu/webmonkeys/html_workshop/unix.html>
- Excellent little permissions map written in ASCII yay! <https://stackoverflow.com/questions/14249467/os-mkdir-and-os-mkdirall-permission-value>

The code for the Github repo, ended in this state. Just a single main.go file, which shows how to use several features of Go and capabilities of the core libraries.

```javascript
package main

import (
	"encoding/json"
	"io/ioutil"
	"log"
	"os"
	"os/user"
	"strconv"
)

type UserInformation struct {
	Name     string   `json:"name"`
	UserId   int64    `json:"userid"`
	GroupId  int64    `json:"groupid"`
	HomeDir  string   `json:"homedir"`
	UserName string   `json:"username"`
	GroupIds []string `json:"groupids"`
	GoPath   string   `json:"gopath"`
	EnvVar   string   `json:"environmentvariable"`
}

func main() {
	currentUser, err := user.Current()
	check(err)
	changeDataForMarshalling(currentUser)
}

func changeDataForMarshalling(currentUser *user.User) {
	groupsIds, err := currentUser.GroupIds()
	check(err)
	userId, err := strconv.ParseInt(currentUser.Uid, 6, 64)
	check(err)
	groupId, err := strconv.ParseInt(currentUser.Gid, 6, 64)
	check(err)

	workingUserInformation := &UserInformation{
		Name:     currentUser.Name,
		UserId:   userId,
		GroupId:  groupId,
		HomeDir:  currentUser.HomeDir,
		UserName: currentUser.Username,
		GroupIds: groupsIds,
		GoPath:   os.Getenv("GOPATH"),
		EnvVar:   os.Getenv("NEW_STRING_ENVIRONMENT_VARIABLE"),
	}

	resultingUserInformation, _ := json.Marshal(workingUserInformation)

	filename := "collected_values.json"
	if _, err := os.Stat(filename); os.IsNotExist(err) {
		writeFileContents(err, filename, string(resultingUserInformation))
	} else {
		newUserInformation, err := openFileMakeChanges(filename)
		writeFileContents(err, filename, newUserInformation)
	}
}

func openFileMakeChanges(filename string) (string, error) {
	jsonFile, err := os.Open(filename)
	check(err)
	defer jsonFile.Close()
var changingUserInformation UserInformation
	byteValue, _ := ioutil.ReadAll(jsonFile)
	json.Unmarshal(byteValue, &changingUserInformation)
changingUserInformation.Name = "Adron Hall"
	changingUserInformation.GoPath = "/where/is/the/goland"
	newUserInformation, _ := json.Marshal(changingUserInformation)
return string(newUserInformation), err
}

func writeFileContents(err error, filename string, text string) {
	f, err := os.OpenFile(filename, os.O_CREATE|os.O_WRONLY, 0600)
	check(err)
	defer f.Close()

	if _, err = f.WriteString(text); err != nil {
		panic(err)
	}
}

func check(err error) {
	if err != nil {
		log.Fatal(err)
	}
}
```

The import section includes several core libraries for the application “encoding/json”, “io/ioutil”, “log”, “os”, “os/user”, and “strconv”. Then I’ve got a *structure* declared that I use throughout the code with various *fields*.

Then just for the heck of it I created a changeDataForMarshalling function and passed in userInfo and parsed the string results of gid and uid to int data types. From there the remaining values are passed in then marshalled to JSON and written to a file, depending on if it’s a new file or existing. The writing however I broke out to a function dubbed writeFileContents. Definitely some more refactoring and tweaking to really make it functional and usable, but shows easily what strconv, marshalling, and other features of these core libraries do. This code provides some examples on what functionality [Colligere](https://github.com/ThrashingCode/colligere) will use to read in schema configuration, edit, and save that schema. More about that in the [next Twitch few streams](https://www.twitch.tv/adronhall/events).
