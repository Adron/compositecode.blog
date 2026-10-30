---
title: IDE Launcher via Amtrak Cascades to Portland for ML4ALL
date: 2018-05-27 08:22:52 -0700
last_modified_at: 2018-05-28 09:23:49 -0700
permalink: /2018/05/27/ide-launcher-via-amtrak-cascades-to-portland-for-ml4all/
slug: ide-launcher-via-amtrak-cascades-to-portland-for-ml4all
wp_id: 14126
original_url: https://compositecode.blog/2018/05/27/ide-launcher-via-amtrak-cascades-to-portland-for-ml4all/
categories:
- golang
- Ml4all
- Unknown Code Ramblings
tags:
- geektrain
- ide
- Ml4all
- portland
- train
excerpt: Got fidgety on the train, and just wanted to write code, on the way down to Portland for ML4ALL so I wrote up some decision tree code on determining what IDE’s I want opened up. Ya know, if you do something more than twice it needs automated, so I’ve started the process of automating all …
image: /wp-content/uploads/2018/05/portlands_rail_50-4k.jpg
---

Got fidgety on the train, and just wanted to write code, on the way down to Portland for ML4ALL so I wrote up some decision tree code on determining what IDE’s I want opened up. Ya know, if you do something more than twice it needs automated, so I’ve started the process of automating all startup and shutdown tasks for a day’s coding. Simplistic geeky train geek code fun code is fun geeky train code. Cheers!

```cpp
package main

import (
	"time"
	"fmt"
)

var sessionMinimal, sessionMedium, sessionLong, sessionZone time.Duration
var language string

func main() {
	sessionMinimal = 15
	sessionMedium = 45
	sessionLong = 90
	sessionZone = 180

	language = "golang"

	openIde("golang", 200)
}

func openIde(languageStack string, expectedCodingTime time.Duration) {
	var ide string

	switch  {
	case expectedCodingTime  sessionZone:
		ide = stackSpecific(languageStack, false, true, true)
		fmt.Printf("Launching: %s", ide)

	}
}

func stackSpecific(language string, fastLaunch bool, featureRich bool, introspective bool) string {
	if fastLaunch == true && featureRich == true && introspective == true {
		return "\n\nCome on, you know better. You get at best two out of three.\n\n"
	}

	if fastLaunch == true && featureRich == true {
		return "Visual Studio Code"
	}

	if featureRich == true && introspective == true {
		switch language {
		case "SQL":
			return "DataGrip"
		case "C":
			return "CLion"
		case "Python":
			return "PyCharm"
		case "golang":
			return "Goland"
		case "java":
			return "IntelliJ"
		case "scala":
			return "IntelliJ"
		case "kotlin":
			return "IntelliJ"
		case "dotnet":
			return "Rider"
		case "csharp":
			return "Rider"
		case "fsharp":
			return "Rider"
		case "vbnet":
			return "Rider"
		case "javascript":
			return "Webstorm"
		case "hcl":
			return "IntelliJ"
		case "ruby":
			return "RubyMine"
		case "swift":
			return "AppCode"
		case "obj-c":
			return "AppCode"
		default:
			return "IntelliJ"
		}
	}

	if featureRich == true {
		switch language {
		case "swift":
			return "AppCode"
		case "obj-c":
			return "AppCode"
		default:
			return "Visual Studio Code"
		}
	}

	if introspective == true {
		switch language {
		case "swift":
			return "AppCode"
		case "obj-c":
			return "AppCode"
		default:
			return "Visual Studio Code"
		}
	}

	if fastLaunch == true  {
		return "Sublime"
	}

	return "No IDE for you."
}
```
