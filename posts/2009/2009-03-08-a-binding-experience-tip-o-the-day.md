---
title: 'A Binding Experience :: Tip o'' The Day'
date: 2009-03-08 06:50:00 +0000
last_modified_at: 2009-03-08 06:50:00 +0000
permalink: /2009/03/08/a-binding-experience-tip-o-the-day/
slug: a-binding-experience-tip-o-the-day
wp_id: 596
original_url: https://compositecode.blog/2009/03/08/a-binding-experience-tip-o-the-day/
categories:
- Uncategorized Bits
tags: []
excerpt: 'I was trying to get some deserialized JSON objects to bind to my WPF application interface and was struggling. I figured out what the fix was, I took the shortcut route on my objects and should have built them correctly. My original objects where built as such: public class ReportItem { public string AccountId; public …'
---

I was trying to get some deserialized JSON objects to bind to my WPF application interface and was struggling.  I figured out what the fix was, I took the shortcut route on my objects and should have built them correctly.

My original objects where built as such:

```
public class ReportItem
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

However, they should have appeared as follows:

```
public class ReportItem
{
    public string AccountId { get; set; }
    public string Name { get; set; }
    public string Id { get; set; }
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

The classes that will be bound need to have legitimate properties, not merely public members.

Now when I do a binding via the XAML

```
        <ComboBox
            Margin="193,75,12,0"
            Name="comboProfiles"
            Height="23"
            VerticalAlignment="Top"
            IsEnabled="True"
            ItemsSource="{Binding}"
            DisplayMemberPath="Name"
            SelectionChanged="comboProfiles_SelectionChanged"
            SelectedIndex="0" />
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

and then bind at run time like this

```
var javaScriptSerializer = new JavaScriptSerializer();
comboProfiles.DataContext = javaScriptSerializer.Deserialize<List<ProfileItem>>(e.Result);
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

everything works flawlessly.
