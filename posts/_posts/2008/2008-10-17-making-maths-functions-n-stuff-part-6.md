---
title: Making Maths Functions n' Stuff Part 6
date: 2008-10-17 02:00:11 -0700
last_modified_at: 2008-10-17 02:00:11 -0700
permalink: /2008/10/17/making-maths-functions-n-stuff-part-6/
slug: making-maths-functions-n-stuff-part-6
wp_id: 206
original_url: https://compositecode.blog/2008/10/17/making-maths-functions-n-stuff-part-6/
categories:
- Uncategorized Bits
tags: []
excerpt: First off I changed up the UI a little bit to accommodate the changes I wanted to make. I mainly wanted to show how, at the same time utilizing the functions, the way WPF controls work. Numerous controls work in ways they never have before, utilizing a more object oriented patterns and practices oriented nomenclature. …
---

First off I changed up the UI a little bit to accommodate the changes I wanted to make.  I mainly wanted to show how, at the same time utilizing the functions, the way WPF controls work.  Numerous controls work in ways they never have before, utilizing a more object oriented patterns and practices oriented nomenclature.  I like it, but at the same time it is a learning curve to think of the controls less in their ancient VB4 and VB6 days and more like the real objects that they now are.

```
   1:  <Window x:Class="Maths.MathsCooking"
   2:      xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation"
   3:      xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
   4:      Title="Maths Cooking" Height="768" Width="1024">
   5:      <Grid>
   6:          <TextBox Height="65" Margin="10,0,14,50" Name="textAnswers" VerticalAlignment="Bottom" />
   7:          <Button Height="23" HorizontalAlignment="Right" Margin="0,0,14,14" Name="exitApplicationButton" VerticalAlignment="Bottom" Width="75" Click="exitApplicationButton_Click">Exit</Button>
   8:          <GroupBox Header="Fraction Functions" Margin="18,20,489,0" Name="groupBox1" Height="187" VerticalAlignment="Top">
   9:              <Grid HorizontalAlignment="Stretch" VerticalAlignment="Stretch">
  10:                  <Button BorderThickness="3" Click="getApproximateEqualityButton_Click" Height="23" HorizontalAlignment="Right" Margin="0,0,18,23.085" Name="getApproximateEqualityButton" VerticalAlignment="Bottom" Width="150">Get Approximate Equality</Button>
  11:                  <TextBox Height="23" Margin="190,10,198,0" Name="textNumerator" VerticalAlignment="Top"/>
  12:                  <TextBox Height="23" Margin="190,0,198,57.723" Name="textValue" VerticalAlignment="Bottom" />
  13:                  <TextBox Height="23" Margin="190,0,198,21.723" Name="textEpsilon" VerticalAlignment="Bottom"/>
  14:                  <TextBox Height="23" Margin="190,48,198,0" Name="textDenominator" VerticalAlignment="Top"/>
  15:                  <Label Height="28" HorizontalAlignment="Left" Margin="10,10,0,0" Name="labelNumerator" VerticalAlignment="Top" Width="150">Numerator</Label>
  16:                  <Label Height="28" HorizontalAlignment="Left" Margin="10,48,0,0" Name="labelDenominator" VerticalAlignment="Top" Width="150">Denominator</Label>
  17:                  <Label Height="28" HorizontalAlignment="Left" Margin="10,0,0,16.723" Name="labelEpsilon" VerticalAlignment="Bottom" Width="150">Epsilon</Label>
  18:                  <Label Height="28" HorizontalAlignment="Left" Margin="10,0,0,52.723" Name="labelValue" VerticalAlignment="Bottom" Width="150">A Value (Float or Double)</Label>
  19:                  <Button BorderThickness="3" Click="getDecimalButton_Click" Height="23" HorizontalAlignment="Right" Margin="0,46.638,18,0" Name="getDecimalButton" VerticalAlignment="Top" Width="150">Get Decimal</Button>
  20:              </Grid>
  21:          </GroupBox>
  22:          <GroupBox Header="Is Numeric Check" Margin="18,223,489,0" Name="groupBox2" Height="103" VerticalAlignment="Top">
  23:              <Grid HorizontalAlignment="Stretch" VerticalAlignment="Stretch">
  24:                  <Button Height="23" HorizontalAlignment="Right" Margin="0,15,18,0" Name="getAnalysisOfString" VerticalAlignment="Top" Width="150" Click="getAnalysisOfString_Click">Analyze</Button>
  25:                  <TextBox Height="23" Margin="10,15,0,0" Name="textIsNumeric" VerticalAlignment="Top" HorizontalAlignment="Left" Width="95" />
  26:                  <CheckBox Height="16" Margin="142,18,222,0" Name="checkIsNumeric" VerticalAlignment="Top">Is Numeric?</CheckBox>
  27:                  <CheckBox Height="16" Margin="142,0,222,26" Name="checkIsEven" VerticalAlignment="Bottom">Is Even?</CheckBox>
  28:              </Grid>
  29:          </GroupBox>
  30:          <GroupBox Header="GroupBox" Height="187" HorizontalAlignment="Right" Margin="0,20,24,0" Name="groupRounding" VerticalAlignment="Top" Width="446">
  31:              <Grid HorizontalAlignment="Stretch" VerticalAlignment="Stretch">
  32:                  <Button Click="getRoundedAnswers_Click" Height="23" HorizontalAlignment="Right" Margin="0,0,19,23.085" Name="getRoundedAnswers" VerticalAlignment="Bottom" Width="150">Round</Button>
  33:                  <Label Height="28" Margin="160,0,154,54.723" Name="labelRoundDown" VerticalAlignment="Bottom">Down</Label>
  34:                  <Label Height="28" Margin="160,45.999,154,0" Name="lableRoundUp" VerticalAlignment="Top">Up</Label>
  35:                  <Label Height="28" Margin="160,10,154,0" Name="labelRoundIeee" VerticalAlignment="Top">IEEE</Label>
  36:                  <TextBox Height="23" Margin="0,48,19,0" Name="textRoundUp" VerticalAlignment="Top" HorizontalAlignment="Right" Width="120" />
  37:                  <TextBox Height="23" HorizontalAlignment="Right" Margin="0,12,19,0" Name="textRoundIeee" VerticalAlignment="Top" Width="120" />
  38:                  <TextBox Height="23" HorizontalAlignment="Right" Margin="0,0,19,57.723" Name="textRoundDown" VerticalAlignment="Bottom" Width="120" />
  39:                  <TextBox Height="23" HorizontalAlignment="Left" Margin="19,48,0,0" Name="textNumberToRound" VerticalAlignment="Top" Width="120" />
  40:                  <Label HorizontalAlignment="Left" Margin="19,10,0,0" Name="labelNumberToRound" Width="120" Height="28" VerticalAlignment="Top">Round This</Label>
  41:              </Grid>
  42:          </GroupBox>
  43:      </Grid>
  44:  </Window>
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

After I made the UI changes I altered some of the code and added some code.  The first change was to the but that used to check for numeric value, that now does multiple checks.  The Analyze Button now looks like this.

```
   1:          private void getAnalysisOfString_Click(object sender, RoutedEventArgs e)
   2:          {
   3:              if (textIsNumeric.Text != string.Empty)
   4:              {
   5:                  bool isNumberic = Functions.IsNumeric(textIsNumeric.Text);
   6:
   7:                  checkIsNumeric.IsChecked = isNumberic;
   8:
   9:                  bool isEven;
  10:                  if (isNumberic)
  11:                  {
  12:                      Int64 numeric = Convert.ToInt64(textIsNumeric.Text);
  13:                      isEven = Functions.IsEven(numeric);
  14:                      checkIsEven.IsChecked = isEven;
  15:                      textAnswers.Text = "Numeric? " + isNumberic + ". Even? " + isEven + ".";
  16:                  }
  17:                  else
  18:                  {
  19:                      textAnswers.Text = "Numeric? " + isNumberic + ".";
  20:                  }
  21:              }
  22:              else
  23:              {
  24:                  MessageBox.Show(
  25:                      "Technically string.empty is not numeric, but it is more useful if you enter a value to check.",
  26:                      "Enter a value!",
  27:                      MessageBoxButton.OK,
  28:                      MessageBoxImage.Hand,
  29:                      MessageBoxResult.OK);
  30:              }
  31:          }
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

The other functionality I then added was the rounding group box.  The code is included below.

```
   1:          private void getRoundedAnswers_Click(object sender, RoutedEventArgs e)
   2:          {
   3:              if(Functions.IsNumeric( textNumberToRound.Text))
   4:              {
   5:                  double numberToRound = Convert.ToDouble(textNumberToRound.Text);
   6:                  string roundedUp= Functions.Round(Functions.RoundDirection.Up, numberToRound).ToString();
   7:                  string roundedDown= Functions.Round(Functions.RoundDirection.Down, numberToRound).ToString();
   8:                  string roundedIeee= Functions.Round(Functions.RoundDirection.IeeeStandard, numberToRound).ToString();
   9:                  textRoundUp.Text = roundedUp;
  10:                  textRoundDown.Text = roundedDown;
  11:                  textRoundIeee.Text = roundedIeee;
  12:              }
  13:              else
  14:              {
  15:                  MessageBox.Show(
  16:                      "You must enter numeric values in the text box to round.",
  17:                      "Enter a numeric value!",
  18:                      MessageBoxButton.OK,
  19:                      MessageBoxImage.Hand,
  20:                      MessageBoxResult.OK);
  21:              }
  22:          }
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

I still have many things I’ll be adding to this strange and haphazard application, as the cooking is never done.  Over the next few months and weeks I intend to add string manipulations and other useful things to the application.  The idea of course, is to use it as reference, and possibly, as something for finding out information!

The code for this entire solution is available at [CodePlex](http://www.codeplex.com/): <http://www.codeplex.com/csharpcooking>
