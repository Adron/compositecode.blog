---
title: Making Maths Functions n' Stuff Part 2
date: 2008-10-10 02:57:09 +0000
last_modified_at: 2008-10-10 02:57:09 +0000
permalink: /2008/10/10/making-maths-functions-n-stuff-part-2/
slug: making-maths-functions-n-stuff-part-2
wp_id: 213
original_url: https://compositecode.blog/2008/10/10/making-maths-functions-n-stuff-part-2/
categories:
- Uncategorized Bits
tags: []
excerpt: After completing the tests and functional methods for the other part of the solution in part 1, we’re jumping into getting the WPF application built. First I started out by simply creating a new WPF application and renaming the default xaml form. After renaming remember to change the StartupUri property name in the App.xaml file …
---

After completing the tests and functional methods for the other part of the solution in [part 1](http://www.adronbhall.com/blogs/technology__software_development/post/2008/10/08/Making-Maths-Functions-n-Stuff-Part-1.aspx), we’re jumping into getting the WPF application built.

[![](/images/adronhall.smugmug.com/photos/390588932_Pxsfh-M.png)](http://adronhall.smugmug.com/gallery/6181616_zg5Ko/1/390588932_Pxsfh)

First I started out by simply creating a new WPF application and renaming the default xaml form.  After renaming remember to change the StartupUri property name in the App.xaml file so things startup appropriately.

[![](/images/adronhall.smugmug.com/photos/390588926_XSjy2-M.png)](http://adronhall.smugmug.com/gallery/6181616_zg5Ko/1/390588926_XSjy2)

```
   1:  <Application x:Class="Maths.App"
   2:      xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation"
   3:      xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
   4:      StartupUri="MathsCooking.xaml">
   5:      <Application.Resources>
   6:
   7:      </Application.Resources>
   8:  </Application>
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

I then made the following changes the the MathsCooking.xaml form and added the events below.

```
   1:  <Window x:Class="Maths.Window1"
   2:      xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation"
   3:      xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
   4:      Title="Maths Cooking" Height="768" Width="1024">
   5:      <Grid>
   6:          <Button BorderThickness="3" Height="23" HorizontalAlignment="Left" Margin="332,123.638,0,0" Name="getApproximateEqualityButton" VerticalAlignment="Top" Width="150" Click="getApproximateEqualityButton_Click">Get Approximate Equality</Button>
   7:          <TextBox Height="23" HorizontalAlignment="Left" Margin="190,10,0,0" Name="textNumerator" VerticalAlignment="Top" Width="95" />
   8:          <TextBox Height="23" HorizontalAlignment="Left" Margin="190,87,0,0" Name="textValue" VerticalAlignment="Top" Width="95" />
   9:          <TextBox Height="23" HorizontalAlignment="Left" Margin="190,123,0,0" Name="textEpsilon" VerticalAlignment="Top" Width="95" />
  10:          <TextBox Height="23" HorizontalAlignment="Left" Margin="190,48,0,0" Name="textDenominator" VerticalAlignment="Top" Width="95" />
  11:          <Label Height="28" HorizontalAlignment="Left" Margin="10,10,0,0" Name="labelNumerator" VerticalAlignment="Top" Width="150">Numerator</Label>
  12:          <Label Height="28" HorizontalAlignment="Left" Margin="10,48,0,0" Name="labelDenominator" VerticalAlignment="Top" Width="150">Denominator</Label>
  13:          <Label Height="28" HorizontalAlignment="Left" Margin="10,123,0,0" Name="labelEpsilon" VerticalAlignment="Top" Width="150">Epsilon</Label>
  14:          <Label Height="28" HorizontalAlignment="Left" Margin="10,87,0,0" Name="labelValue" VerticalAlignment="Top" Width="150">A Value (Float or Double)</Label>
  15:          <Button BorderThickness="3" Height="23" HorizontalAlignment="Left" Margin="332,48.638,0,0" Name="getDecimalButton" VerticalAlignment="Top" Width="150" Click="getDecimalButton_Click">Get Decimal</Button>
  16:          <TextBox Height="65" HorizontalAlignment="Left" Margin="10,168,0,0" Name="textAnswers" VerticalAlignment="Top" Width="472" />
  17:      </Grid>
  18:  </Window>
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

The C# Code Behind file.  (Eventually I’ll learn all the lingo for this WPF stuff, until then, you can just deal with my WinForm speak)

```
   1:  #region
   2:
   3:  using System.Windows;
   4:
   5:  #endregion
   6:
   7:  namespace Maths
   8:  {
   9:      public partial class Window1 : Window
  10:      {
  11:          public Window1()
  12:          {
  13:              InitializeComponent();
  14:          }
  15:
  16:          private void getDecimalButton_Click(object sender, RoutedEventArgs e)
  17:          {
  18:          }
  19:
  20:          private void getApproximateEqualityButton_Click(object sender, RoutedEventArgs e)
  21:          {
  22:          }
  23:      }
  24:  }
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

Next in order was the effort to make the UI actually do some things.

```
   1:  #region
   2:
   3:  using System;
   4:  using System.Windows;
   5:  using MathCookbook;
   6:
   7:  #endregion
   8:
   9:  namespace Maths
  10:  {
  11:      public partial class Window1 : Window
  12:      {
  13:          public Window1()
  14:          {
  15:              InitializeComponent();
  16:          }
  17:
  18:          private void getDecimalButton_Click(object sender, RoutedEventArgs e)
  19:          {
  20:              textAnswers.Text = Functions.GetDecimalOfFraction(
  21:                  Convert.ToDouble(textNumerator.Text),
  22:                  Convert.ToDouble(textDenominator.Text)).ToString();
  23:          }
  24:
  25:          private void getApproximateEqualityButton_Click(object sender, RoutedEventArgs e)
  26:          {
  27:              textAnswers.Text = Functions.IsApproximatelyEqualTo(
  28:                  Convert.ToDouble(textNumerator.Text),
  29:                  Convert.ToDouble(textDenominator.Text),
  30:                  Convert.ToDouble(textValue.Text),
  31:                  Convert.ToDouble(textEpsilon.Text)).ToString();
  32:          }
  33:      }
  34:  }
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

Now we can actually try out various numbers with a UI.  Next we’ll tackle a few more additional methods and move towards some non-math related items.  I needed the Math Library refresher so I’ve hit that library first.
