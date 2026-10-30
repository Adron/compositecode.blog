---
title: Twitz Coding Session in Go – Cobra + Viper CLI Wrap Up + Twitter Data Retrieval
date: 2018-12-27 16:11:30 -0800
last_modified_at: 2018-12-27 17:38:55 -0800
permalink: /2018/12/27/twitz-coding-session-in-go-cobra-viper-cli-wrap-up-twitter-data-retrieval/
slug: twitz-coding-session-in-go-cobra-viper-cli-wrap-up-twitter-data-retrieval
wp_id: 15008
original_url: https://compositecode.blog/2018/12/27/twitz-coding-session-in-go-cobra-viper-cli-wrap-up-twitter-data-retrieval/
categories:
- Coding Adventures
- Distributed Things
- golang
- Video
tags:
- cassandra
- cli
- go
- golang
- twitter
- twitz
excerpt: 'Part 3 of 3 – Coding Session in Go – Cobra + Viper CLI for Parsing Text Files, Retrieval of Twitter Data, and Exports to various file formats. UPDATED PARTS: Twitz Coding Session in Go – Cobra + Viper CLI for Parsing Text Files Twitz Coding Session in Go – Cobra + Viper CLI with …'
image: /wp-content/uploads/2018/12/two1.png
---

Part 3 of 3 – Coding Session in Go – Cobra + Viper CLI for Parsing Text Files, Retrieval of Twitter Data, and Exports to various file formats.

**UPDATED PARTS:**

1. [Twitz Coding Session in Go – Cobra + Viper CLI for Parsing Text Files](/2018/12/04/twitz-coding-session-in-go-cobra-viper-cli-for-parsing-text-files/)
2. [Twitz Coding Session in Go – Cobra + Viper CLI with Initial Twitter + Cassandra Installation](/2018/12/07/twitz-coding-session-in-go-cobra-viper-cli-with-initial-twitter-cassandra-installation/)
3. [Twitz Coding Session in Go – Cobra + Viper CLI Wrap Up + Twitter Data Retrieval (this post)](/2018/12/27/twitz-coding-session-in-go-cobra-viper-cli-wrap-up-twitter-data-retrieval/)

Updated links to each part will be posted at bottom of  this post when I publish them. For code, written walk through, and the like scroll down below the video and timestamps.

<iframe allowfullscreen="true" class="youtube-player" height="486" loading="lazy" sandbox="allow-scripts allow-same-origin allow-popups allow-presentation allow-popups-to-escape-sandbox" src="https://www.youtube.com/embed/j-jEQaG6byA?version=3&amp;rel=1&amp;showsearch=0&amp;showinfo=1&amp;iv_load_policy=1&amp;fs=1&amp;hl=en-US&amp;autohide=2&amp;wmode=transparent" style="border:0;" width="863"></iframe>

[0:54](https://youtu.be/j-jEQaG6byA/watch?v=j-jEQaG6byA&t=54s) The thrashing introduction.
[3:40](https://youtu.be/j-jEQaG6byA/watch?v=j-jEQaG6byA&t=220s) Getting started, with a recap of the previous sessions but I’ve not got the sound on so ignore this until [5:20](https://youtu.be/j-jEQaG6byA/watch?v=j-jEQaG6byA&t=320s).
[5:20](https://youtu.be/j-jEQaG6byA/watch?v=j-jEQaG6byA&t=320s) I notice, and turn on the volume. Now I manage to get the recap, talking about some of the issues with the Twitter API. I step through setup of the app and getting the appropriate ID’s and such for the Twitter API Keys and Secrets.
[9:12](https://youtu.be/j-jEQaG6byA/watch?v=j-jEQaG6byA&t=552s) I open up the code base, and review where the previous sessions got us to. Using Cobra w/ Go, parsing and refactoring that was previously done.
[10:30](https://youtu.be/j-jEQaG6byA/watch?v=j-jEQaG6byA&t=630s) Here I talk about configuration again and the specifics of getting it setup for running the application.
[12:50](https://youtu.be/j-jEQaG6byA/watch?v=j-jEQaG6byA&t=770s) Talking about Go’s fatal panic I was getting. The dependency reference to Github for the application was different than what is in application and don’t show the code that is actually executing. I show a quick fix and move on.
[17:12](https://youtu.be/j-jEQaG6byA/watch?v=j-jEQaG6byA&t=1032s) Back to the Twitter API use by using the go-twitter library. Here I review the issue and what the fix was for another issue I was having previous session with getting the active token! Thought the library handled it but that wasn’t the case!
[19:26](https://youtu.be/j-jEQaG6byA/watch?v=j-jEQaG6byA&t=1166s) Now I step through creating a function to get the active oath bearer token to use.
[28:30](https://youtu.be/j-jEQaG6byA/watch?v=j-jEQaG6byA&t=1710s) After deleting much of the code that doesn’t work from the last session, I go about writing the code around handling the retrieval of Twitter results for various passed in Twitter Accounts.

*The bulk of the next section is where I work through a number of functions, a little refactoring, and answering some questions from the audience/Twitch Chat (working on a way to get it into the video!), fighting with some dependency tree issues, and a whole slew of silliness. Once that wraps up I get some things committed into the Github repo and wrap up the core functionality of the Twitz Application.*

[58:00](https://youtu.be/j-jEQaG6byA/watch?v=j-jEQaG6byA&t=3480s) Reviewing some of the other examples in the go-twitter library repo. I also do a quick review of the other function calls form the library that take action against the Twitter API.
[59:40](https://youtu.be/j-jEQaG6byA/watch?v=j-jEQaG6byA&t=3580s) One of the PR’s I submitted to the project itself I review and merge into the repo that adds documentation and a build badge for the README.md.
[1:02:48](https://youtu.be/j-jEQaG6byA/watch?v=j-jEQaG6byA&t=3768s) Here I add some more information about the configuration settings to the README.md file.

[1:05:48](https://youtu.be/j-jEQaG6byA/watch?v=j-jEQaG6byA&t=3948s) The Twitz page is now updated: <https://adron.github.io/twitz/>
[1:06:48](https://youtu.be/j-jEQaG6byA/watch?v=j-jEQaG6byA&t=4008s) Setup of the continuous integration for the project on Travis CI itself: <https://travis-ci.org/Adron/twitz>
[1:08:58](https://youtu.be/j-jEQaG6byA/watch?v=j-jEQaG6byA&t=4138s) Setup fo the actual travis.yml file for Go. After this I go through a few stages of troubleshooting getitng the build going, with some white space in the ole’ yaml file and such. Including also, the famous casing issue! Ugh!
[1:26:20](https://youtu.be/j-jEQaG6byA/watch?v=j-jEQaG6byA&t=5180s) Here I start a wrap up of what is accomplished in this session.

**NOTE:** *Yes, I realize I spaced and forgot the feature where I export it out to Apache Cassandra. Yes, I will indeed have a future stream where I build out the part that exports the responses to Apache Cassandra! So subcribe, stay tuned, and I’ll get that one done ASAP!!!*

[1:31:10](https://youtu.be/j-jEQaG6byA/watch?v=j-jEQaG6byA&t=5470s) Further CI troubleshooting as one build is green and one build is yellow. More CI troubleshooting! Learn about the travis yaml here.
[1:34:32](https://youtu.be/j-jEQaG6byA/watch?v=j-jEQaG6byA&t=5672s) Finished, just the bad ass outtro now!

## The Codez

In the previous posts I outlined two specific functions that were built out:

- [Part 1](/2018/12/04/twitz-coding-session-in-go-cobra-viper-cli-for-parsing-text-files/) – The `config` function for the `twitz config` command.
- [Part 2](/2018/12/07/twitz-coding-session-in-go-cobra-viper-cli-with-initial-twitter-cassandra-installation/) – The `parse` function for the `twitz parse` command.

In this post I focused on updating both of these and adding additional functions for the bearer token retrieval for auth and ident against the Twitter API and other functionality. Let’s take a look at what the functions looked like and read like after this last session wrap up.

The `config` command basically ended up being 5 lines of `fmt.Printf` functions to print out pertinent configuration values and environment variables that are needed for the CLI to be used.

```
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
		fmt.Printf("Consumer API Key: %s\n", viper.GetString("consumer_api_key")[0:6])
		fmt.Printf("Consumer API Secret: %s\n", viper.GetString("consumer_api_secret")[0:6])
	},
}
```

[View the gist on GitHub](https://gist.github.com/Adron/03ce2e36533af12862e6b9119467df88/7eebc8ce91dc621c5521128285949542da0fbdff/config.go)

The `parse` command was a small bit changed. A fair amount of the functionality I refactored out to the `buildTwitterList()` and `exportFile`, and `rebuildForExport` functions. The `buildTwitterList()` I put in the helper.go file, which I’ll cover a littler later. But in this file, which could still use some refactoring which I’ll get to, I have several pieces of functionality; the export to formats functions, and the *if else if* logic of the `exportParsedTwitterList` function.

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

[View the gist on GitHub](https://gist.github.com/Adron/376904c39ea5c11ef5a0dcc87de317ab/e289c8f8fc2cb564dbedcce5da2d8d1e53456948/parse.go)

Next up after parse, it seems fitting to cover the *[helpers.go](https://github.com/Adron/twitz/blob/master/cmd/helpers.go)* file code. First I have the `check` function, which simply wraps the routinely copied error handling code snippet. Check out the file directly for that. Then below that I have the `buildTwitterList()` function which gets the config setting for the file name to open to parse for Twitter accounts. Then the code reads the file, splits the results of the text file into fields, then steps through and parses out the Twitter accounts. This is done with a REGEX (*I know I know now I have two problems, but hey, this is super simple!*). It basically finds fields that start with an @ and then verifies the alphanumeric nature, combined with a possible underscore, that then remove unnecessary characters on those fields. Wrapping all that up by putting the fields into a string/slice array and returning that string array to the calling code.

```
func buildTwitterList() []string {
	theFile := viper.GetString("file")
	theTwitterers, err := ioutil.ReadFile(theFile)
	check(err)
	stringTwitterers := string(theTwitterers[:])
	splitFields := strings.Fields(stringTwitterers)
	var completedTwittererList []string
	for _, aField := range splitFields {
		if strings.HasPrefix(aField, "@") && aField != "@" {
			reg, _ := regexp.Compile("[^a-zA-Z0-9_@]")
			processedString := reg.ReplaceAllString(aField, "")
			completedTwittererList = append(completedTwittererList, processedString)
		}
	}
	return completedTwittererList
}
```

[View the gist on GitHub](https://gist.github.com/Adron/c7bc7a244dee5d81a2cbe83326cc0b93/41b2816efec01b78375ae9bf5c79548956ccb24c/buildTwitterListFunction.go)

The next function in the *[Helpers.go](https://github.com/Adron/twitz/blob/master/cmd/helpers.go)* file is the `getBearerToken` function. This was a tricky bit of code. This function takes in the consumer key and secret from the Twitter app (check out the video at [5:20](https://www.youtube.com/watch?v=j-jEQaG6byA&t=320s) for where to set it up). It returns a string and error, empty string if there’s an error, as shown below.

The code starts out with establishing a POST request against the Twitter API, asking for a token and passing the client credentials. Catches an error if that doesn’t work out, but if it can the code then sets up the b64Token variable with the standard encoding functionality when it receives the token string byte array ( lines 9 and 10). After that the request then has the header built based on the needed authoriztaion and content-type properties (*properties, values? I don’t recall what spec calls these*), then the request is made with `http.DefaultClient.Do(req)`. The response is returned, or error and empty response (or nil? I didn’t check the exact function signature logic). Next up is the defer to ensure the response is closed when everything is done.

Next up the JSON result is parsed (unmarshalled) into the `v struct` which I now realize as I write this I probably ought to rename to something that isn’t a single letter. But it works for now, and v has the pertinent AccessToken variable which is then returned.

```
func getBearerToken(consumerKey, consumerSecret string) (string, error) {
	req, err := http.NewRequest("POST", "https://api.twitter.com/oauth2/token&quot;,
		strings.NewReader("grant_type=client_credentials"))

	if err != nil {
		return "", fmt.Errorf("cannot create /token request: %+v", err)
	}

	b64Token := base64.StdEncoding.EncodeToString(
		[]byte(fmt.Sprintf("%s:%s", consumerKey, consumerSecret)))
	req.Header.Add("Authorization", "Basic "+b64Token)
	req.Header.Add("Content-Type", "application/x-www-form-urlencoded;charset=UTF-8")

	resp, err := http.DefaultClient.Do(req)
	if err != nil {
		return "", fmt.Errorf("/token request failed: %+v", err)
	}
	defer resp.Body.Close()

	var v struct {
		AccessToken string `json:"access_token"`
	}

	if err := json.NewDecoder(resp.Body).Decode(&v); err != nil {
		return "", fmt.Errorf("error parsing json in /token response: %+v", err)
	}
	if v.AccessToken == "" {
		return "", fmt.Errorf("/token response does not have access_token")
	}
	return v.AccessToken, nil
}
```

[View the gist on GitHub](https://gist.github.com/Adron/f418d8e745fe1cf269499728538c10f0/351c0b305e68e0d606cc0962cec4d68ca850f500/GetBearerToken.go)

Wow, ok, that’s a fair bit of work. Up next, the `findem.go` file and related function for twitz. Here I start off with a few informative prints to the console just to know where the CLI has gotten to at certain points. The twitter list is put together, reusing that same function – yay code reuse right! Then the access token is retrieved. Next up the http client is built, the twitter client is passed that and initialized, and the user lookup request is sent. Finally the users are printed out and below that a count and print out of the count of users is printed.

```
var findemCmd = &cobra.Command{
	Use:   "findem",
	Short: "A brief description of your command",
	Long: `A longer description that spans multiple lines and likely contains examples
and usage of using your command. For example:
Cobra is a CLI library for Go that empowers applications.
This application is a tool to generate the needed files
to quickly create a Cobra application.`,
	Run: func(cmd *cobra.Command, args []string) {

		fmt.Println("Starting Twitter Information Retrieval.")
		completedTwitterList := buildTwitterList()

		fmt.Printf("Getting Twitter details for: \n%s", completedTwitterList)

		accessToken, err := getBearerToken(viper.GetString("consumer_api_key"), viper.GetString("consumer_api_secret"))
		check(err)

		config := &oauth2.Config{}
		token := &oauth2.Token{AccessToken: accessToken}
		// OAuth2 http.Client will automatically authorize Requests
		httpClient := config.Client(context.Background(), token)
		// Twitter client
		client := twitter.NewClient(httpClient)

		// users lookup
		userLookupParams := &twitter.UserLookupParams{ScreenName: completedTwitterList}
		users, _, _ := client.Users.Lookup(userLookupParams)
		fmt.Printf("\n\nUsers:\n%+v\n", users)

		howManyUsersFound := len(users)
		fmt.Println(howManyUsersFound)
	},
}
```

[View the gist on GitHub](https://gist.github.com/Adron/d7376f729468f4dff53fa6c7ca28532e/9c046f0c01e61c33f4505d3dc95a8d322884205a/Findem.go)

I realized, just as I wrapped this up I completely spaced on the Apache Cassandra export. I’ll have those post coming soon and will likely do another refactor to get the output into a more usable state before I call this one done. But the core functionality, setup of the systemic environment needed for the tool, the pertinent data and API access, and other elements are done. For now, that’s a wrap, if you’re curious about the final refactor and the Apache Cassandra export then subscribe to my Twitch [@adronhall](https://www.twitch.tv/adronhall) and/or my YouTube channel [ThrashingCode](https://www.youtube.com/channel/UCHSCXYCMOOS-VSUdRsn13GQ).

**UPDATED SERIES PARTS**

1. 1. [Twitz Coding Session in Go – Cobra + Viper CLI for Parsing Text Files](/2018/12/04/twitz-coding-session-in-go-cobra-viper-cli-for-parsing-text-files/)
   2. [Twitz Coding Session in Go – Cobra + Viper CLI with Initial Twitter + Cassandra Installation](/2018/12/07/twitz-coding-session-in-go-cobra-viper-cli-with-initial-twitter-cassandra-installation/)
   3. [Twitz Coding Session in Go – Cobra + Viper CLI Wrap Up + Twitter Data Retrieval (this post)](/2018/12/27/twitz-coding-session-in-go-cobra-viper-cli-wrap-up-twitter-data-retrieval/)
