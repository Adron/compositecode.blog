---
title: Practices for WCF Data Contracts Part 1
date: 2008-10-26 19:03:50 -0700
last_modified_at: 2008-10-26 19:03:50 -0700
permalink: /2008/10/26/practices-for-wcf-data-contracts-part-1/
slug: practices-for-wcf-data-contracts-part-1
wp_id: 547
original_url: https://compositecode.blog/2008/10/26/practices-for-wcf-data-contracts-part-1/
categories:
- Uncategorized Bits
tags: []
excerpt: Ok, now to the meaty section on WCF based Web Services. This entry is about the data contracts that hold together and describe the data the web services offer across the wire. These first few topics are solely on how to mark various classes, enumerations, and structures as a data contract. In subsequent parts we’ll …
---

Ok, now to the meaty section on WCF based Web Services.  This entry is about the data contracts that hold together and describe the data the web services offer across the wire.  These first few topics are solely on how to mark various classes, enumerations, and structures as a data contract.  In subsequent parts we’ll cover data sets, collections, and other ways to move sets of data across the wire.

The basic structure is like this:

```
   1:      [DataContract]
   2:      public class Note
   3:      {
   4:          [DataMember]
   5:          public string Body { get; set; }
   6:      }
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

Pretty much any class that can be serialized or is serialized can be setup to move across the wire by this means.  Now what happens for some of the other types, such as a structure or a enumeration?  You can set those up like this:

```
   1:      [DataContract]
   2:      public enum Priority
   3:      {
   4:          [EnumMember]
   5:          Low,
   6:          [EnumMember]
   7:          Medium,
   8:          [EnumMember]
   9:          High
  10:      }
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

and a structure:

```
   1:      [DataContract]
   2:      public struct TimeInfo
   3:      {
   4:          [DataMember]
   5:          public Int16 EstimatedHours { get; set; }
   6:
   7:          [DataMember]
   8:          public Int16 ActualHours { get; set; }
   9:
  10:          [DataMember]
  11:          public DateTime StartDate { get; set; }
  12:
  13:          [DataMember]
  14:          public DateTime EndDate { get; set; }
  15:
  16:          [DataMember]
  17:          public DateTime CompletionDate { get; set; }
  18:      }
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

There are other properties of the attributes that can come in handy also.  Take this same Task Class as an example.

```
   1:      [DataContract(Name = "TaskItem")]
   2:      public class Task
   3:      {
   4:          [OnSerializing]
   5:          public void OnSerializing(StreamingContext context)
   6:          {
   7:              ClientKey = Guid.NewGuid().ToString();
   8:          }
   9:
  10:          [DataMember(IsRequired = true, Order = 1)]
  11:          public string ClientKey { get; private set; }
  12:
  13:          [DataMember(IsRequired = true, Order = 2)]
  14:          public string Title { get; set; }
  15:
  16:          [DataMember(Order = 3)]
  17:          public string Description { get; set; }
  18:
  19:          [DataMember(IsRequired = true, Order = 4)]
  20:          public Priority Priority { get; set; }
  21:
  22:          [DataMember(Order = 5)]
  23:          public TimeInfo TimeInformation { get; set; }
  24:
  25:          [DataMember(Order = 6)]
  26:          public Decimal Cost { get; set; }
  27:      }
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

The **Name Property** replaces the class or member name and provides a name to use instead.  The others are **IsRequired**, which sets the property as required or not, obviously.  The **Order** Property sets the order in which the serialization will serialize the particular property.

In the above example there is also the [OnSerializing] attribute.  There are four events that occur during the serialization and deserialization processing of the object;  *OnSerializing*, *Serialized*, *OnDeserializing*, and *OnDeserialized*.  Any method tagged with the particular attribute of the same name, will allow the method to be triggered during that particular event.
