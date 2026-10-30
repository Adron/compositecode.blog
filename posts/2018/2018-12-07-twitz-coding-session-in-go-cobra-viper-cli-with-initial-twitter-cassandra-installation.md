---
title: Twitz Coding Session in Go – Cobra + Viper CLI with Initial Twitter + Cassandra Installation
date: 2018-12-07 14:09:59 -0800
last_modified_at: 2018-12-27 17:38:57 -0800
permalink: /2018/12/07/twitz-coding-session-in-go-cobra-viper-cli-with-initial-twitter-cassandra-installation/
slug: twitz-coding-session-in-go-cobra-viper-cli-with-initial-twitter-cassandra-installation
wp_id: 15007
original_url: https://compositecode.blog/2018/12/07/twitz-coding-session-in-go-cobra-viper-cli-with-initial-twitter-cassandra-installation/
categories:
- Coding Adventures
- Distributed Things
- golang
- How-to
- ThrashingCode
tags:
- apache cassandra
- cassandra
- cobra
- coding
- go
- golang
- programming
- twitter
- twitter api
- viper
excerpt: 'Part 2 of 3 – Coding Session in Go – Cobra + Viper CLI for Parsing Text Files, Retrieval of Twitter Data, Exports to various file formats, and export to Apache Cassandra. UPDATED PARTS: Twitz Coding Session in Go – Cobra + Viper CLI for Parsing Text Files Twitz Coding Session in Go – Cobra …'
image: /wp-content/uploads/2018/12/banner-code.png
---

*Part 2 of 3* – Coding Session in Go – Cobra + Viper CLI for Parsing Text Files, Retrieval of Twitter Data, Exports to various file formats, and export to Apache Cassandra.

**UPDATED PARTS:**

1. [Twitz Coding Session in Go – Cobra + Viper CLI for Parsing Text Files](/2018/12/04/twitz-coding-session-in-go-cobra-viper-cli-for-parsing-text-files/)
2. [Twitz Coding Session in Go – Cobra + Viper CLI with Initial Twitter + Cassandra Installation (this post)](/2018/12/07/twitz-coding-session-in-go-cobra-viper-cli-with-initial-twitter-cassandra-installation/)
3. [Twitz Coding Session in Go – Cobra + Viper CLI Wrap Up + Twitter Data Retrieval](/2018/12/27/twitz-coding-session-in-go-cobra-viper-cli-wrap-up-twitter-data-retrieval/)

Updated links to each part will be posted at bottom of  this post when I publish them. For code, written walk through, and the like scroll down below the video and timestamps.

<iframe allowfullscreen="true" class="youtube-player" height="486" loading="lazy" sandbox="allow-scripts allow-same-origin allow-popups allow-presentation allow-popups-to-escape-sandbox" src="https://www.youtube.com/embed/YQ7eeErPNY4?version=3&amp;rel=1&amp;showsearch=0&amp;showinfo=1&amp;iv_load_policy=1&amp;fs=1&amp;hl=en-US&amp;autohide=2&amp;wmode=transparent" style="border:0;" width="863"></iframe>

Hacking Together a CLI Installing Cassandra, Setting Up the Twitter API, ENV Vars, etc.

[0:04](https://www.youtube.com//watch?v=YQ7eeErPNY4&t=4s) Kick ass intro. Just the standard rocking tune.

[3:40](https://www.youtube.com//watch?v=YQ7eeErPNY4&t=220s) A quick recap. Check out the previous write “[Twitz Coding Session in Go – Cobra + Viper CLI for Parsing Text Files](/2018/12/04/twitz-coding-session-in-go-cobra-viper-cli-for-parsing-text-files/)” of this series.

[4:30](https://www.youtube.com//watch?v=YQ7eeErPNY4&t=270s) Beginning of completion of `twitz parse` command for exporting out to XML, JSON, and CSV (already did the text export previous session). This segment also includes a number of refactorings to clean up the functions, break out the control structures and make the code more readable.

In the end of refactoring `twitz parse` came out like this. The completed list is put together by calling the `buildTwitterList()` function which is actually in the helpers.go file. Then prints that list out as is, and checks to see if a file export should be done. If there is a configuration setting set for file export then that process starts with a call to `exportParsedTwitterList(exportFilename string, exportFormat string, ... etc ... )`. Then a simple single level control if then else structure to determine which format to export the data to, and a call to the respective export function to do the actual export of data and writing of the file to the underlying system. There’s some more refactoring that could be done, but for now, this is cleaned up pretty nicely considering the splattering of code I started with at first.

```
var parseCmd = &cobra.Command{
	Use:   "parse",
	Short: "This command will extract the Twitter Accounts form a text file.",
	Long: `This command will extract the Twitter Accounts and clean up or disregard other characters
or text around the twitter accounts to create a simple, clean, Twitter Accounts only list.`,
	Run: func(cmd *cobra.Command, args []string) {
		completedTwittererList := buildTwitterList()
		fmt.Println(completedTwittererList)
		if viper.Get("fileExport") != nil {
			exportParsedTwitterList(viper.GetString("fileExport"), viper.GetString("fileFormat"), completedTwittererList)
		}
	},
}

func exportParsedTwitterList(exportFilename string, exportFormat string, twittererList []string) {
	if exportFormat == "txt" {
		exportTxt(exportFilename, twittererList, exportFormat)
	} else if exportFormat == "json" {
		exportJson(exportFilename, twittererList, exportFormat)
	} else if exportFormat == "xml" {
		exportXml(exportFilename, twittererList, exportFormat)
	} else if exportFormat == "csv" {
		exportCsv(exportFilename, twittererList, exportFormat)
	} else {
		fmt.Println("Export type unsupported.")
	}
}

func exportXml(exportFilename string, twittererList []string, exportFormat string) {
	fmt.Printf("Starting xml export to %s.", exportFilename)
	xmlContent, err := xml.Marshal(twittererList)
	check(err)
	header := xml.Header
	collectedContent := header + string(xmlContent)
	exportFile(collectedContent, exportFilename+"."+exportFormat)
}

func exportCsv(exportFilename string, twittererList []string, exportFormat string) {
	fmt.Printf("Starting txt export to %s.", exportFilename)
	collectedContent := rebuildForExport(twittererList, ",")
	exportFile(collectedContent, exportFilename+"."+exportFormat)
}

func exportTxt(exportFilename string, twittererList []string, exportFormat string) {
	fmt.Printf("Starting %s export to %s.", exportFormat, exportFilename)
	collectedContent := rebuildForExport(twittererList, "\n")
	exportFile(collectedContent, exportFilename+"."+exportFormat)
}

func exportJson(exportFilename string, twittererList []string, exportFormat string) {
	fmt.Printf("Starting %s export to %s.", exportFormat, exportFilename)
	collectedContent := collectContent(twittererList)
	exportFile(string(collectedContent), exportFilename+"."+exportFormat)
}

func collectContent(twittererList []string) []byte {
	collectedContent, err := json.Marshal(twittererList)
	check(err)
	return collectedContent
}

func rebuildForExport(twittererList []string, concat string) string {
	var collectedContent string
	for _, twitterAccount := range twittererList {
		collectedContent = collectedContent + concat + twitterAccount
	}
	if concat == "," {
		collectedContent = strings.TrimLeft(collectedContent, concat)
	}
	return collectedContent
}

func exportFile(collectedContent string, exportFile string) {
	contentBytes := []byte(collectedContent)
	err := ioutil.WriteFile(exportFile, contentBytes, 0644)
	check(err)
}
```

[View the gist on GitHub](https://gist.github.com/Adron/6bdc0dfe6c64e4bb1d13b164ea7b87d7/fec045ece7f9556e1217ee33e7853935dba0d937/parse.go)

[50:00](https://www.youtube.com//watch?v=YQ7eeErPNY4&t=3000s) I walk through a quick install of an Apache Cassandra single node that I’ll use for development use later. I also show quickly how to start and stop post-installation.

**Reference**: [Apache Cassandra](http://cassandra.apache.org/), [Download Page, and Installation Instructions](http://cassandra.apache.org/download/).

[53:50](https://www.youtube.com//watch?v=YQ7eeErPNY4&t=3230s) Choosing the go-twitter API library for Go. I look at a few real quickly just to insure that is the library I want to use.

**Reference**: [go-twitter library](https://github.com/dghubble/go-twitter)

[56:35](https://www.youtube.com//watch?v=YQ7eeErPNY4&t=3395s) At this point I go through how I set a Twitter App within the API interface. This is a key part of the series where I take a look at the consumer keys and access token and access token secrets and where they’re at in the Twitter interface and how one needs to reset them if they just showed the keys on a stream (like I just did, shockers!)

[57:55](https://www.youtube.com//watch?v=YQ7eeErPNY4&t=3475s) Here I discuss and show where to setup the environment variables inside of [Goland IDE](https://www.jetbrains.com/go/) to building and execution of the CLI. Once these are setup they’ll be the main mechanism I use in the IDE to test the CLI as I go through building out further features.

[1:00:18](https://www.youtube.com//watch?v=YQ7eeErPNY4&t=3618s) Updating the `twitz config` command to show the keys that we just added as environment variables. I set these up also with some string parsing and cutting off the end of the secrets so that the whole variable value isn’t shown but just enough to confirm that it is indeed a set configuration or environment variable.

[1:16:53](https://www.youtube.com//watch?v=YQ7eeErPNY4&t=4613s) At this point I work through some additional refactoring of functions to clean up some of the code mess that exists. Using Goland’s extract method feature and other tooling I work through several refactoring efforts that clean up the code.

[1:23:17](https://www.youtube.com//watch?v=YQ7eeErPNY4&t=4997s) Copying a build configuration in Goland. A handy little thing to know you can do when you have a bunch of build configuration options.

[1:37:32](https://www.youtube.com//watch?v=YQ7eeErPNY4&t=5852s) At this part of the video I look at the app-auth example in the code library, but I gotta add the caveat, I run into problems using the exact example. But I work through it and get to the first error messages that anybody would get to pending they’re using the same examples. I get them fixed however in the next session, this segment of the video however provides a basis for my pending PR’s and related work I’ll submit to the repo.

The remainder of the video is trying to figure out what is or isn’t exactly happening with the error.

I’ll include the working `findem` code in the next post on this series. Until then, watch the wrap up and enjoy!

[1:59:20](https://www.youtube.com//watch?v=YQ7eeErPNY4&t=7160s) Wrap up of video and upcoming stream schedule on Twitch.

**UPDATED SERIES PARTS**

1. 1. [Twitz Coding Session in Go – Cobra + Viper CLI for Parsing Text Files](/2018/12/04/twitz-coding-session-in-go-cobra-viper-cli-for-parsing-text-files/)
   2. [Twitz Coding Session in Go – Cobra + Viper CLI with Initial Twitter + Cassandra Installation (this post)](/2018/12/07/twitz-coding-session-in-go-cobra-viper-cli-with-initial-twitter-cassandra-installation/)
   3. [Twitz Coding Session in Go – Cobra + Viper CLI Wrap Up + Twitter Data Retrieval](/2018/12/27/twitz-coding-session-in-go-cobra-viper-cli-wrap-up-twitter-data-retrieval/)
