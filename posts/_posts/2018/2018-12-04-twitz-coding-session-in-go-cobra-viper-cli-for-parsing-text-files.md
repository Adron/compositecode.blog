---
title: Twitz Coding Session in Go – Cobra + Viper CLI for Parsing Text Files
date: 2018-12-04 15:33:59 -0800
last_modified_at: 2018-12-27 17:39:00 -0800
permalink: /2018/12/04/twitz-coding-session-in-go-cobra-viper-cli-for-parsing-text-files/
slug: twitz-coding-session-in-go-cobra-viper-cli-for-parsing-text-files
wp_id: 15006
original_url: https://compositecode.blog/2018/12/04/twitz-coding-session-in-go-cobra-viper-cli-for-parsing-text-files/
categories:
- Coding Adventures
- golang
- Video
tags: []
excerpt: 'Part 1 of 3 – Coding Session in Go – Cobra + Viper CLI for Parsing Text Files, Retrieval of Twitter Data, Exports to various file formats, and export to Apache Cassandra. UPDATED PARTS: Twitz Coding Session in Go – Cobra + Viper CLI for Parsing Text Files (this post) Twitz Coding Session in Go …'
image: /wp-content/uploads/2018/12/two1.png
---

*Part 1 of 3* – Coding Session in Go – Cobra + Viper CLI for Parsing Text Files, Retrieval of Twitter Data, Exports to various file formats, and export to Apache Cassandra.

**UPDATED PARTS:**

1. [Twitz Coding Session in Go – Cobra + Viper CLI for Parsing Text Files (this post)](/2018/12/04/twitz-coding-session-in-go-cobra-viper-cli-for-parsing-text-files/)
2. [Twitz Coding Session in Go – Cobra + Viper CLI with Initial Twitter + Cassandra Installation](/2018/12/07/twitz-coding-session-in-go-cobra-viper-cli-with-initial-twitter-cassandra-installation/)
3. [Twitz Coding Session in Go – Cobra + Viper CLI Wrap Up + Twitter Data Retrieval](/2018/12/27/twitz-coding-session-in-go-cobra-viper-cli-wrap-up-twitter-data-retrieval/)

Updated links to each part will be posted at bottom of  this post when I publish them. For code, written walk through, and the like scroll down and I’ll have code samples toward the bottom of the timestamps under the video, so scroll, scroll, scroll.

<iframe allowfullscreen="true" class="youtube-player" height="486" loading="lazy" sandbox="allow-scripts allow-same-origin allow-popups allow-presentation allow-popups-to-escape-sandbox" src="https://www.youtube.com/embed/1iniLntln2A?version=3&amp;rel=1&amp;showsearch=0&amp;showinfo=1&amp;iv_load_policy=1&amp;fs=1&amp;hl=en-US&amp;autohide=2&amp;wmode=transparent" style="border:0;" width="863"></iframe>

**[3:40](https://www.youtube.com/watch?v=1iniLntln2A&t=220s)** Stated goals of application. I go through a number of features that I intend to build into this application, typing them up in a text doc. The following are the items I added to the list.

1. The ability to import a text file of Twitter handles that are mixed in among a bunch of other text.
2. The ability to clean up that list.
3. The ability to export the cleaned up list of handles to a text, csv, JSON, xml, or plain text file.
4. The ability, using the Twitter API, to pull data form the bio, latest tweets, and other related information.

![github](/wp-content/uploads/2018/12/github.png)[**8:26**](https://www.youtube.com/watch?v=1iniLntln2A&t=506s) Creating a new Github Repo. A few tips and tricks with creating a new repo with the Github.

- Github Repo: [Twitz](https://github.com/Adron/twitz)
- License: [Apache-2.0](https://github.com/Adron/twitz/blob/master/LICENSE)
- Issue Filing Options: [Feature Request](https://github.com/Adron/twitz/issues/new?template=feature_request.md) or [Bug Report](https://github.com/Adron/twitz/issues/new?template=bug_report.md).
- [README.md](https://github.com/Adron/twitz/blob/master/README.md)
- The [Jeckyll yml file](https://github.com/Adron/twitz/blob/master/_config.yml) that provides the skinning for the [project page](https://adron.github.io/twitz/) at <https://adron.github.io/twitz/>.

[**9:46**](https://www.youtube.com/watch?v=1iniLntln2A&t=586s) Twitz is brought into existence! Woo
~~ Have to reset up my SSH key real quick. This is a quick tutorial if you aren’t sure how to do it, otherwise skip forward to the part where I continue with project setup and initial coding.

[**12:40**](https://www.youtube.com/watch?v=1iniLntln2A&t=760s) Call out for @justForFunc and Francesc’s episode on Cobra!

Check out @Francesc’s “Just for Func”. It’s a great video/podcast series of lots and lots of Go!

- [@JustforFunc](https://twitter.com/justforfunc) on Twitter.
- [Just for Func on Youtube](https://www.youtube.com/channel/UC_BzFbxG2za3bp5NRRRXJSw).
- The episode I mentioned regarding the [Cobra CLI Library](https://youtu.be/WvWPGVKLvR4).

[**13:02**](https://www.youtube.com/watch?v=1iniLntln2A&t=782s) Back to project setup. Cloning repo, getting initial README.emd, .gitignore file setup, and related collateral for the basic project. I also add Github’s “issues” files via the Github interface and rebase these changes in later.
[**14:20**](https://www.youtube.com/watch?v=1iniLntln2A&t=860s) Adding some options to the .gitignore file.
[**15:20**](https://www.youtube.com/watch?v=1iniLntln2A&t=920s) Set dates and copyright in license file.
**[16:00](https://www.youtube.com/watch?v=1iniLntln2A&t=960s)** Further setup of project, removing WIKIs, projects, and reasoning for keeping issues.
[**16:53**](https://www.youtube.com/watch?v=1iniLntln2A&t=1013s) Opening Goland up after an update. Here I start going through the specific details of how I setup a Go Project in Goland, setting configuration and related collateral.
[**17:14**](https://www.youtube.com/watch?v=1iniLntln2A&t=1034s) Setup of Goland’s `golang` Command Line Launcher.
**[25:45](https://www.youtube.com/watch?v=1iniLntln2A&t=1545s)** Introduction to Cobra (and first mention of Viper by association).
**[26:43](https://www.youtube.com/watch?v=1iniLntln2A&t=1603s)** Installation of Cobra with `go get github.com/spf13/cobra/cobra/` and the gotchas (remember to have your paths set, etc).
[**29:50**](https://www.youtube.com/watch?v=1iniLntln2A&t=1790s) Using Cobra CLI to build out the command line interface app’s various commands.
[**35:03**](https://www.youtube.com/watch?v=1iniLntln2A&t=2103s) Looking over the generated code and commenting on the comments and their usefulness.
**[36:00](https://www.youtube.com/watch?v=1iniLntln2A&t=2160s)** Wiring up the last bits of Cobra with some code, via main func, for CLI execution.
**[48:07](https://www.youtube.com/watch?v=1iniLntln2A&t=2887s)** I start wiring up the Viper configuration at this point. Onward from here it’s coding, coding, and configuration, and more coding.

## Implementing the `twitz config` Command

**[1:07:20](https://www.youtube.com/watch?v=1iniLntln2A&t=4040s)** Confirming config and working up the `twitz config` command implementation.
**[1:10:40](https://www.youtube.com/watch?v=1iniLntln2A&t=4240s)** First execution of `twitz config` and I describe where and how Cobra’s documentation strings work through the `--help` flag and is put into other help files based on the need for the short or long description.

The basic config code when implemented looked something like this end of session. This snippet of code doesn’t do much beyond provide the displace of the configuration variables from the configuration file. Eventually I’ll add more to this file so the CLI can be easier to debug when setting it up.

```
package cmd

import (
	"fmt"
	"github.com/spf13/cobra"
	"github.com/spf13/viper"
)

// configCmd represents the config command
var configCmd = &cobra.Command{
	Use:   "config",
	Short: "A brief description of your command",
	Long: `A longer description that spans multiple lines and likely contains examples
and usage of using your command. For the custom example:
Cobra is a CLI library for Go that empowers applications.
This application is a tool to generate the needed files
to quickly create a Cobra application.`,
	Run: func(cmd *cobra.Command, args []string) {
		fmt.Printf("Twitterers File: %s\n", viper.GetString("file"))
		fmt.Printf("Export File: %s\n", viper.GetString("fileExport"))
		fmt.Printf("Export Format: %s\n", viper.GetString("fileFormat"))
	},
}

func init() {
	rootCmd.AddCommand(configCmd)
}
```

## Implementing the `twitz parse` Command

[**1:14:10**](https://www.youtube.com/watch?v=1iniLntln2A&t=4450s) Starting on the implementation of the `twitz parse` command.
**[1:16:24](https://www.youtube.com/watch?v=1iniLntln2A&t=4584s)** Inception of my “helpers.go” file to consolidate and clean up some of the code.
[**1:26:22**](https://www.youtube.com/watch?v=1iniLntln2A&t=5182s) REDEX Implementation time!
**[1:32:12](https://www.youtube.com/watch?v=1iniLntln2A&t=5532s)** Trying out the REGEX101.com site.

I’ll post the finished code and write up some details on the thinking behind it when I post video two of this application development sessions.

That’s really it for this last session. Hope the summary helps for anybody working through building CLI apps with Go and Cobra. Until next session, happy thrashing code.

**UPDATED SERIES PARTS**

1. [Twitz Coding Session in Go – Cobra + Viper CLI for Parsing Text Files (this post)](/2018/12/04/twitz-coding-session-in-go-cobra-viper-cli-for-parsing-text-files/)
2. [Twitz Coding Session in Go – Cobra + Viper CLI with Initial Twitter + Cassandra Installation](/2018/12/07/twitz-coding-session-in-go-cobra-viper-cli-with-initial-twitter-cassandra-installation/)
3. [Twitz Coding Session in Go – Cobra + Viper CLI Wrap Up + Twitter Data Retrieval](/2018/12/27/twitz-coding-session-in-go-cobra-viper-cli-wrap-up-twitter-data-retrieval/)
