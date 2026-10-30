---
title: Part 1 Basic Webtrends REST Examples
date: 2010-04-14 12:20:01 +0000
last_modified_at: 2010-07-20 10:15:33 -0700
permalink: /2010/04/14/part-1-basic-webtrends-rest-examples/
slug: part-1-basic-webtrends-rest-examples
wp_id: 721
original_url: https://compositecode.blog/2010/04/14/part-1-basic-webtrends-rest-examples/
categories:
- How-to
tags: []
excerpt: In this entry I just want to cover some examples of how to connect to Webtrends DX Web Services. The DX Web Services use REST as the architecture, providing simple URI based end points to connect to. With the Webtrends SDK you can connect to these services with your account information. Here are the basic …
---

In this entry I just want to cover some examples of how to connect to [Webtrends](http://www.webtrends.com) [DX](http://developer.webtrends.com) Web Services.  The [DX](http://developer.webtrends.com) Web Services use REST as the architecture, providing simple URI based end points to connect to.  With the [Webtrends](http://www.webtrends.com) SDK you can connect to these services with your account information.  Here are the basic steps to retrieve a profile list, the reports from one of those profiles, and then the report you want from that report list.

First step is to create a Webtrends User.

```
WebTrends.Sdk.Account.User webtrendsUser = new Account.User();
webtrendsUser.UserName = username;
webtrendsUser.Password = password;
webtrendsUser.AccountName = account;
```

After you create the Webtrends User, simple request a profile list by getting list of ProfileDefinition Objects.

```
List<WebTrends.Sdk.Profile.ProfileDefinition> profiles =
  WebTrends.Sdk.Factory.NavigationFactory.BuildListing(webtrendsUser);
```

Next you will want to grab a report based on the profile you are in and your credentials.

```
List<WebTrends.Sdk.Report.ReportDefinition> reports =
WebTrends.Sdk.Factory.NavigationFactory.BuildListing(profiles[i], webtrendsUser);
```

In the code above, i would equate to the specific profile you want from the retrieved list of profiles in the profiles list.  The common scenario is that one has pulled the profiles into a drop down, combo, or list box that the user can select.  Then when the user selects the specific profile that profile object can then be used to pull the List of ReportDefinitions.

Once we have the report definitions, all sorts of criteria can be added together to query for a specific report.  This is also were things can get a little tricky.  For instance, take a look at the code below.

```
WebTrends.Sdk.Factory.ReportFactory.CreateDimensionalReport(
    report.ID.ToString(), profiles[i].ID.ToString(), "2010m01", webtrendsUser);
```

The CreateDimensionalReport takes 4 parameters for this particular overload.  The report ID, profile ID, the Webtrends Date Format, and the Webtrends User Object.  There are a number of other overloads available within this factory’s method that allow for passing the specific REST URI, and other criteria to retrieve the report of your choice.  In the near future we will be adding some more to this method also, which will provide more flexibility without needing to use the full REST URI.

I will have more on this, so all you Coders out there using Webtrends DX Services, I hope this is helpful!  Enjoy.
