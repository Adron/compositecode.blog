---
title: JSON Serialization & Deserialization, The Simple Stuff (Part 1)
date: 2009-03-09 02:50:00 -0700
last_modified_at: 2009-03-09 02:50:00 -0700
permalink: /2009/03/09/json-serialization-deserialization-the-simple-stuff-part-1/
slug: json-serialization-deserialization-the-simple-stuff-part-1
wp_id: 597
original_url: https://compositecode.blog/2009/03/09/json-serialization-deserialization-the-simple-stuff-part-1/
categories:
- Uncategorized Bits
tags: []
excerpt: Here‘s a few snippets outlining serialization and deserialization of a few object with JSON. At first I started using JSON.NET but it is a bit picky about various things and the samples I found where disparate. I then realized also that in the System.Web.Extensions Namespace there is a class that handles JSON anyway. Might as …
---

Here‘s a few snippets outlining serialization and deserialization of a few object with JSON.  At first I started using JSON.NET but it is a bit picky about various things and the samples I found where disparate.  I then realized also that in the *System.Web.Extensions* Namespace there is a class that handles JSON anyway.  Might as well use it since it is already included.  *Please note, I’m merely using unit tests below to showcase the functionality of the serialization and deserialization of JSON, there is no real need to unit test the class functionality, just what you’ll do in your own code in isolation of the particular serialization and deserialization.  If you want to test your serializations and deserializations that is fine, I’m merely suggesting that it doesn’t particularly need to be.*

First things first, let’s get some data serializing.  Here’s my basic class I’m starting with.

```
public class ProfileItem
{
    public string Name;
    public string Id;
}

public class ReportItem
{
    public string accountID;
    public string name;
    public string ID;
}
```

.csharpcode, .csharpcode pre
{
font-size: small;
color: black;
font-family: consolas, “Courier New”, courier, monospace;
background-color: #ffffff;
/\*white-space: pre;\*/
}
.csharpcode pre { margin: 0em; }
.csharpcode .rem { color: #008000; }
.csharpcode .kwrd { color: #0000ff; }
.csharpcode .str { color: #006080; }
.csharpcode .op { color: #0000c0; }
.csharpcode .preproc { color: #cc6633; }
.csharpcode .asp { background-color: #ffff00; }
.csharpcode .html { color: #800000; }
.csharpcode .attr { color: #ff0000; }
.csharpcode .alt
{
background-color: #f4f4f4;
width: 100%;
margin: 0em;
}
.csharpcode .lnum { color: #606060; }

Notice here how I’ve used proper code analysis naming & case convention on the ProfileItem but not on the ReportItem.  I’ve done this to show how the Microsoft JSON Serialize uses intelligent mapping to pair up properties that have case differences.  This is something I like since One might want to follow the conventions, while the data properties you?re consuming might break convention.

Next step was to generate some data.  First add the reference to System.Web.Script.Serialization.  Then munge up some data.  I created and verified the serialization of one object as below.

```
[Test]
public void TestJsonSerialization()
{
    const string serializedResult = @"{""Name"":""TheProfileName"",""Id"":""01cc6fd1-79ec-4ca9-b84c-48a5cf35e666""}";

    var javaScriptSerializer = new JavaScriptSerializer();

    var profileItem =
        new ProfileItem
            {
                Id = new Guid(@"01cc6fd1-79ec-4ca9-b84c-48a5cf35e666").ToString(),
                Name = "TheProfileName"
            };

    var serializedProfileItem = javaScriptSerializer.Serialize(profileItem);

    Assert.IsNotNull(serializedProfileItem);
    Assert.AreEqual(serializedProfileItem, serializedResult);
}
```

.csharpcode, .csharpcode pre
{
font-size: small;
color: black;
font-family: consolas, “Courier New”, courier, monospace;
background-color: #ffffff;
/\*white-space: pre;\*/
}
.csharpcode pre { margin: 0em; }
.csharpcode .rem { color: #008000; }
.csharpcode .kwrd { color: #0000ff; }
.csharpcode .str { color: #006080; }
.csharpcode .op { color: #0000c0; }
.csharpcode .preproc { color: #cc6633; }
.csharpcode .asp { background-color: #ffff00; }
.csharpcode .html { color: #800000; }
.csharpcode .attr { color: #ff0000; }
.csharpcode .alt
{
background-color: #f4f4f4;
width: 100%;
margin: 0em;
}
.csharpcode .lnum { color: #606060; }

Now that I?ve verified the serialization, I?m going to test the deserialization.

```
[Test]
public void TestJsonDeserialization()
{
    const string serializedResult = @"{""Name"":""TheProfileName"",""Id"":""01cc6fd1-79ec-4ca9-b84c-48a5cf35e666""}";
    var javaScriptSerializer = new JavaScriptSerializer();

    var deSerializedResult = javaScriptSerializer.Deserialize<ProfileItem>(serializedResult);

    Assert.AreEqual(deSerializedResult.Id, @"01cc6fd1-79ec-4ca9-b84c-48a5cf35e666");
    Assert.AreEqual(deSerializedResult.Name, "TheProfileName");
}
```

.csharpcode, .csharpcode pre
{
font-size: small;
color: black;
font-family: consolas, “Courier New”, courier, monospace;
background-color: #ffffff;
/\*white-space: pre;\*/
}
.csharpcode pre { margin: 0em; }
.csharpcode .rem { color: #008000; }
.csharpcode .kwrd { color: #0000ff; }
.csharpcode .str { color: #006080; }
.csharpcode .op { color: #0000c0; }
.csharpcode .preproc { color: #cc6633; }
.csharpcode .asp { background-color: #ffff00; }
.csharpcode .html { color: #800000; }
.csharpcode .attr { color: #ff0000; }
.csharpcode .alt
{
background-color: #f4f4f4;
width: 100%;
margin: 0em;
}
.csharpcode .lnum { color: #606060; }

With that complete I have two working examples of basic serialization and deserialization.  Now for a few twists on that to see what kind of results we get.  As I pointed out above I have the ReportItem with the case convention that is, well, disliked by code anlysis/fxCop etc.  Here’s an example of how one can have a serialized object with incongruent convention, but you can create an object that has your own desired casing.  Before moving forward, I created one more class, which one can tell what I’m up to by its name.

```
public class ReportItemMyWay
{
    public string AccountId;
    public string Name;
    public string Id;
}
```

.csharpcode, .csharpcode pre
{
font-size: small;
color: black;
font-family: consolas, “Courier New”, courier, monospace;
background-color: #ffffff;
/\*white-space: pre;\*/
}
.csharpcode pre { margin: 0em; }
.csharpcode .rem { color: #008000; }
.csharpcode .kwrd { color: #0000ff; }
.csharpcode .str { color: #006080; }
.csharpcode .op { color: #0000c0; }
.csharpcode .preproc { color: #cc6633; }
.csharpcode .asp { background-color: #ffff00; }
.csharpcode .html { color: #800000; }
.csharpcode .attr { color: #ff0000; }
.csharpcode .alt
{
background-color: #f4f4f4;
width: 100%;
margin: 0em;
}
.csharpcode .lnum { color: #606060; }

Now that I have a class done the way I?d prefer the convention I?ll get some data serialized with the convention of the ReportItem class I created above.

```
[Test]
public void TestJsonSerializationToDeserializationCasing()
{
    const string serializedResult =
        @"{""accountID"":""01cc6fd1-79ec-4ca9-b84c-48a5cf35e661"",""name"":""Campaigns by Countries"",""ID"":""01cc6fd1-79ec-4ca9-b84c-48a5cf35e662""}";
    var javaScriptSerializer = new JavaScriptSerializer();

    var reportItem =
        new ReportItem
            {
                accountID = new Guid(@"01cc6fd1-79ec-4ca9-b84c-48a5cf35e661").ToString(),
                ID = new Guid(@"01cc6fd1-79ec-4ca9-b84c-48a5cf35e662").ToString(),
                name = "Campaigns by Countries"
            };

    var serializedReport = javaScriptSerializer.Serialize(reportItem);

    Assert.AreEqual(serializedResult, serializedReport);

    var deserializedReport = javaScriptSerializer.Deserialize<ReportItemMyWay>(serializedReport);

    Assert.AreEqual(deserializedReport.Id, reportItem.ID);
    Assert.AreEqual(deserializedReport.Name, reportItem.name);
    Assert.AreEqual(deserializedReport.AccountId, reportItem.accountID);
}
```

.csharpcode, .csharpcode pre
{
font-size: small;
color: black;
font-family: consolas, “Courier New”, courier, monospace;
background-color: #ffffff;
/\*white-space: pre;\*/
}
.csharpcode pre { margin: 0em; }
.csharpcode .rem { color: #008000; }
.csharpcode .kwrd { color: #0000ff; }
.csharpcode .str { color: #006080; }
.csharpcode .op { color: #0000c0; }
.csharpcode .preproc { color: #cc6633; }
.csharpcode .asp { background-color: #ffff00; }
.csharpcode .html { color: #800000; }
.csharpcode .attr { color: #ff0000; }
.csharpcode .alt
{
background-color: #f4f4f4;
width: 100%;
margin: 0em;
}
.csharpcode .lnum { color: #606060; }

You’ll notice that the deserialized object goes smoothly into the new class with the preferred casing & such.  Now for some other twisted bits.  Often the data will get serialized in and deserialized as Generic Lists of X Type.  The example below shows what the results look like if a list of ReportItem Objects are serialized.

At this point I stumbled on some pure genius.  If you look at the previous examples I was using the @ symbol to build all of the JSON strings.  Well, when I copy them from the value when debugging (yeah, that’s how I grabbed the strings of JSON), they’re all automatically escaped.  So in the example below, you’ll notice how the string is escaped and I just left the @ off.  Whoduthunkit.  :/

```
[Test]
public void TestJsonSerializationOfLists()
{
    const string serializedResult =
        "[{\"AccountId\":\"01cc6fd1-79ec-4ca9-b84c-48a5cf35e661\",\"Name\":\"Campaigns by Countries\",\"Id\":\"01cc6fd1-79ec-4ca9-b84c-48a5cf35e662\"},{\"AccountId\":\"01cc6fd1-79ec-4ca9-b84c-48a5cf35e663\",\"Name\":\"Geography by RSS Feeds\",\"Id\":\"01cc6fd1-79ec-4ca9-b84c-48a5cf35e664\"}]";
    var javaScriptSerializer = new JavaScriptSerializer();

    var reportItem1 =
        new ReportItemMyWay
            {
                AccountId = new Guid(@"01cc6fd1-79ec-4ca9-b84c-48a5cf35e661").ToString(),
                Id = new Guid(@"01cc6fd1-79ec-4ca9-b84c-48a5cf35e662").ToString(),
                Name = "Campaigns by Countries"
            };
    var reportItem2 =
        new ReportItemMyWay
            {
                AccountId = new Guid(@"01cc6fd1-79ec-4ca9-b84c-48a5cf35e663").ToString(),
                Id = new Guid(@"01cc6fd1-79ec-4ca9-b84c-48a5cf35e664").ToString(),
                Name = "Geography by RSS Feeds"
            };

    var reportItemMyWays =
        new List<ReportItemMyWay> {reportItem1, reportItem2};

    var serializedList = javaScriptSerializer.Serialize(reportItemMyWays);

    Assert.AreEqual(serializedList, serializedResult);
}
```

.csharpcode, .csharpcode pre
{
font-size: small;
color: black;
font-family: consolas, “Courier New”, courier, monospace;
background-color: #ffffff;
/\*white-space: pre;\*/
}
.csharpcode pre { margin: 0em; }
.csharpcode .rem { color: #008000; }
.csharpcode .kwrd { color: #0000ff; }
.csharpcode .str { color: #006080; }
.csharpcode .op { color: #0000c0; }
.csharpcode .preproc { color: #cc6633; }
.csharpcode .asp { background-color: #ffff00; }
.csharpcode .html { color: #800000; }
.csharpcode .attr { color: #ff0000; }
.csharpcode .alt
{
background-color: #f4f4f4;
width: 100%;
margin: 0em;
}
.csharpcode .lnum { color: #606060; }

This points out the multiple levels for the Generic List serialization.  The deserialization smoothly puts it right back into the ole object per the test below.

```
[Test]
public void TestJsonDeserializationOfLists()
{
    const string serializedResult =
        "[{\"AccountId\":\"01cc6fd1-79ec-4ca9-b84c-48a5cf35e661\",\"Name\":\"Campaigns by Countries\",\"Id\":\"01cc6fd1-79ec-4ca9-b84c-48a5cf35e662\"},{\"AccountId\":\"01cc6fd1-79ec-4ca9-b84c-48a5cf35e663\",\"Name\":\"Geography by RSS Feeds\",\"Id\":\"01cc6fd1-79ec-4ca9-b84c-48a5cf35e664\"}]";
    var javaScriptSerializer = new JavaScriptSerializer();

    var serializedList = javaScriptSerializer.Deserialize<List<ReportItemMyWay>>(serializedResult);

    Assert.AreEqual(serializedList[0].Id,new Guid(@"01cc6fd1-79ec-4ca9-b84c-48a5cf35e662").ToString());
    Assert.AreEqual(serializedList[0].Name, "Campaigns by Countries");
    Assert.AreEqual(serializedList[0].AccountId, new Guid(@"01cc6fd1-79ec-4ca9-b84c-48a5cf35e661").ToString());

    Assert.AreEqual(serializedList[1].Id, new Guid(@"01cc6fd1-79ec-4ca9-b84c-48a5cf35e664").ToString());
    Assert.AreEqual(serializedList[1].Name, "Geography by RSS Feeds");
    Assert.AreEqual(serializedList[1].AccountId, new Guid(@"01cc6fd1-79ec-4ca9-b84c-48a5cf35e663").ToString());
}
```

.csharpcode, .csharpcode pre
{
font-size: small;
color: black;
font-family: consolas, “Courier New”, courier, monospace;
background-color: #ffffff;
/\*white-space: pre;\*/
}
.csharpcode pre { margin: 0em; }
.csharpcode .rem { color: #008000; }
.csharpcode .kwrd { color: #0000ff; }
.csharpcode .str { color: #006080; }
.csharpcode .op { color: #0000c0; }
.csharpcode .preproc { color: #cc6633; }
.csharpcode .asp { background-color: #ffff00; }
.csharpcode .html { color: #800000; }
.csharpcode .attr { color: #ff0000; }
.csharpcode .alt
{
background-color: #f4f4f4;
width: 100%;
margin: 0em;
}
.csharpcode .lnum { color: #606060; }

I’ll have some follow up entries on getting data type specifics in and out of the JSON Objects.  The JSON serialization gets tricky, annoying, and a bit confusing when I jump into data types so subscribe – cheers.
