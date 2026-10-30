---
title: Data Contracts in Windows Communication Foundation (WCF)
date: 2008-10-24 10:33:31 -0700
last_modified_at: 2008-10-24 10:33:31 -0700
permalink: /2008/10/24/data-contracts-in-windows-communication-foundation-wcf/
slug: data-contracts-in-windows-communication-foundation-wcf
wp_id: 202
original_url: https://compositecode.blog/2008/10/24/data-contracts-in-windows-communication-foundation-wcf/
categories:
- Uncategorized Bits
tags: []
excerpt: I’ve been going over data contracts for WCF lately and wanted to post a few specifics. One issue I ran into recently was odd, as it included an enumeration that needed to be included in part of a data contract. I had tagged the enumeration with the [DataContract] attribute but I was receiving an odd …
---

I’ve been going over data contracts for WCF lately and wanted to post a few specifics. One issue I ran into recently was odd, as it included an enumeration that needed to be included in part of a data contract. I had tagged the enumeration with the [DataContract] attribute but I was receiving an odd issue about the service disconnecting. The error message I was getting was something like this:

[![](/images/adronhall.smugmug.com/photos/401494853_AYJv8-M.png)](http://adronhall.smugmug.com/gallery/4027372_CP4dr/1/401494853_AYJv8)

I had read, or thought via failed comprehension, that I could just tag an enumeration with [DataContract] as below.

```
   1:  [DataContract]
   2:  public enum Priority
   3:  {
   4:      Low,
   5:      Medium,
   6:      High
   7:  }
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

As it turns out though, the [EnumMember] attribute needs added to the enumeration.

```
   1:  [DataContract]
   2:  public enum Priority
   3:  {
   4:      [EnumMember]
   5:      Low,
   6:      [EnumMember]
   7:      Medium,
   8:      [EnumMember]
   9:      High
  10:  }
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

After I added that, smooth sailing resumed. So don’t just tag the enumeration, tag the members too. I’m also working on some other notes from my reintroduction to WCF (I’ve done a ton of work with it in the past) so stay tuned for that.
