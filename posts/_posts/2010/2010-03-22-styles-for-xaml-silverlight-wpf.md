---
title: Styles for XAML (Silverlight & WPF)
date: 2010-03-22 11:53:13 -0700
last_modified_at: 2010-03-22 11:53:13 -0700
permalink: /2010/03/22/styles-for-xaml-silverlight-wpf/
slug: styles-for-xaml-silverlight-wpf
wp_id: 704
original_url: https://compositecode.blog/2010/03/22/styles-for-xaml-silverlight-wpf/
categories:
- Uncategorized Bits
tags: []
excerpt: This is a quick walk through of how to setup things for skinning within a XAML Application. First thing, find the App.xaml file within the WPF or Silverlight Project. Within the App.xaml file set some default styles for your controls. I set the following for a button, label, and border control for an application I …
---

This is a quick walk through of how to setup things for skinning within a XAML Application.  First thing, find the App.xaml file within the WPF or [Silverlight](http://www.microsoft.com/silverlight) Project.

Within the App.xaml file set some default styles for your controls.  I set the following for a button, label, and border control for an application I am creating.

**Button Control**

```
<Style x:Key="ButtonStyle" TargetType="Button">
    <Setter Property="FontFamily" Value="Arial" />
    <Setter Property="FontWeight" Value="Bold" />
    <Setter Property="FontSize" Value="14" />
    <Setter Property="Width" Value="180" />
    <Setter Property="Height" Value="Auto" />
    <Setter Property="Margin" Value="8" />
    <Setter Property="Padding" Value="8" />
    <Setter Property="Foreground" Value="AliceBlue" />
    <Setter Property="Background" >
        <Setter.Value>
            <LinearGradientBrush EndPoint="0.5,1" StartPoint="0.5,0">
                <GradientStop Color="Black" Offset="0" />
                <GradientStop Color="#FF5B5757" Offset="1" />
            </LinearGradientBrush>
        </Setter.Value>
    </Setter>
</Style>
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

**Label Control**

```
<Style x:Key="LabelStyle" TargetType="Label">
    <Setter Property="Width" Value="Auto"/>
    <Setter Property="Height" Value="28" />
    <Setter Property="Foreground" Value="Black"/>
    <Setter Property="Margin" Value="8"/>
</Style>
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

**Border Control**

```
<Style x:Key="BorderStyle" TargetType="Border">
    <Setter Property="BorderThickness" Value="4"/>
    <Setter Property="Width" Value="Auto"/>
    <Setter Property="Height" Value="Auto" />
    <Setter Property="Margin" Value="0,8,0,0"/>
    <Setter Property="CornerRadius" Value="18"/>
    <Setter Property="BorderBrush">
        <Setter.Value>
            <LinearGradientBrush EndPoint="1,0.5" StartPoint="0,0.5">
                <GradientStop Color="CornflowerBlue" Offset="0" />
                <GradientStop Color="White" Offset="1" />
            </LinearGradientBrush>
        </Setter.Value>
    </Setter>
</Style>
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

These provide good examples of setting individual properties to a default, such as;

```
<Setter Property="Width" Value="Auto"/>
<Setter Property="Height" Value="Auto" />
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

Also for settings a more complex property, such as with a LinearGradientBrush;

```
<Setter Property="BorderBrush">
    <Setter.Value>
        <LinearGradientBrush EndPoint="1,0.5" StartPoint="0,0.5">
            <GradientStop Color="CornflowerBlue" Offset="0" />
            <GradientStop Color="White" Offset="1" />
        </LinearGradientBrush>
    </Setter.Value>
</Setter>
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

These property setters should be located between the opening and closing <Application.Resources></Application.Resources> tags.

```
<Application x:Class="ScorecardAndDashboard.App"
             xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation"
             xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
             StartupUri="MainWindow.xaml">
    <Application.Resources>
    </Application.Resources>
</Application>
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

Now in the pages, user controls, or whatever you are marking up with XAML, for the Style Property just set a StaticResource such as shown below.

```
     <!-- Border Control -->
<Border Name="borderPollingFrequency" Style="{StaticResource BorderStyle}">
     <!-- Label Control -->
<Label Content="Trigger Name:" Style="{StaticResource LabelStyle}"></Label>
     <!-- Button Control -->
<Button Content="Save Schedule" Name="buttonSaveSchedule"  Style="{StaticResource ButtonStyle}" HorizontalAlignment="Right"/>
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

That’s it.  Simple as that.  There are other ways to setup resource files that are separate from the App.xaml, but the App.xaml file is always a good quick place to start.  As moving the styles to a specific resource file later is a mere copy and paste.

[![Shout it](http://dotnetshoutout.com/image.axd?url=http%3A%2F%2Fwww.adronbhall.com%2Fblogs%2Ftechnology__software_development%2Fpost%2F2010%2F03%2F22%2FVisual-State-Manager-for-XAML-(Silverlight-WPF).aspx)](http://dotnetshoutout.com/Styles-for-XAML-Silverlight-WPF) [![kick it on DotNetKicks.com](http://www.dotnetkicks.com/Services/Images/KickItImageGenerator.ashx?url=http%3a%2f%2fwww.adronbhall.com%2fblogs%2ftechnology__software_development%2fpost%2f2010%2f03%2f22%2fVisual-State-Manager-for-XAML-(Silverlight-WPF).aspx&bgcolor=3333FF&cfgcolor=CC3300)](http://www.dotnetkicks.com/kick/?url=http%3a%2f%2fwww.adronbhall.com%2fblogs%2ftechnology__software_development%2fpost%2f2010%2f03%2f22%2fVisual-State-Manager-for-XAML-(Silverlight-WPF).aspx)
