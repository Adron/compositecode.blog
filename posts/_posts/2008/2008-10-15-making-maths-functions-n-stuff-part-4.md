---
title: Making Maths Functions n' Stuff Part 4
date: 2008-10-15 07:02:08 -0700
last_modified_at: 2008-10-15 07:02:08 -0700
permalink: /2008/10/15/making-maths-functions-n-stuff-part-4/
slug: making-maths-functions-n-stuff-part-4
wp_id: 208
original_url: https://compositecode.blog/2008/10/15/making-maths-functions-n-stuff-part-4/
categories:
- Uncategorized Bits
tags: []
excerpt: This time I’ll add one more test, a respective method, and then put together the WPF UI for the additional methods added in this part and part 3. With this additional method I’ll toss in a little validation too. So first I’ll go ahead and get the validation of string as a number method out …
---

This time I’ll add one more test, a respective method, and then put together the WPF UI for the additional methods added in this part and [part 3](http://www.adronbhall.com/blogs/technology__software_development/post/2008/10/14/Making-Maths-Functions-n-Stuff-Part-3.aspx).  With this additional method I’ll toss in a little validation too.  So first I’ll go ahead and get the validation of string as a number method out of the way.  First things first, going to get a couple tests running.

```
   1:          [Test]
   2:          public void TestStringIsNumberWithNumber()
   3:          {
   4:              string theTestString = "52";
   5:              Console.WriteLine(theTestString);
   6:              Console.WriteLine(MathCookbook.Functions.IsNumeric(theTestString));
   7:              Assert.IsTrue(MathCookbook.Functions.IsNumeric(theTestString));
   8:          }
   9:
  10:          [Test]
  11:          public void TestStringIsNumberWithString()
  12:          {
  13:              string theTestString = "ThisIsObviouslyNotNumber";
  14:              Console.WriteLine(theTestString);
  15:              Console.WriteLine(MathCookbook.Functions.IsNumeric(theTestString));
  16:              Assert.IsFalse(MathCookbook.Functions.IsNumeric(theTestString));
  17:          }
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

Then I’ll throw in the method needed to get a green light.

```
   1:          /// <summary>
   2:          /// This method returns a true or false depending on the passed parameter being a numeric value or not.
   3:          /// </summary>
   4:          /// <param name="valueToCheck">Enter the string value to check for numeric type.</param>
   5:          /// <returns>Returns true if the string is a number or false if it is alphanumeric.</returns>
   6:          public static bool IsNumeric(string valueToCheck)
   7:          {
   8:              Regex reg = new Regex(@"^[\+\-]?\d*\.?[Ee]?[\+\-]?\d*$", RegexOptions.Compiled);
   9:
  10:              valueToCheck = valueToCheck.Trim();
  11:              Match m = reg.Match(valueToCheck);
  12:              return m.Value != string.Empty;
  13:          }
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

Next I’ll start putting together the WPF needed to test execute these new methods.  First the additional UI changes.

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
  11:                  <TextBox Height="23" Margin="190,10,198,0" Name="textNumerator" VerticalAlignment="Top" />
  12:                  <TextBox Height="23" Margin="190,0,198,57.723" Name="textValue" VerticalAlignment="Bottom" />
  13:                  <TextBox Height="23" Margin="190,0,198,21.723" Name="textEpsilon" VerticalAlignment="Bottom" />
  14:                  <TextBox Height="23" Margin="190,48,198,0" Name="textDenominator" VerticalAlignment="Top" />
  15:                  <Label Height="28" HorizontalAlignment="Left" Margin="10,10,0,0" Name="labelNumerator" VerticalAlignment="Top" Width="150">Numerator</Label>
  16:                  <Label Height="28" HorizontalAlignment="Left" Margin="10,48,0,0" Name="labelDenominator" VerticalAlignment="Top" Width="150">Denominator</Label>
  17:                  <Label Height="28" HorizontalAlignment="Left" Margin="10,0,0,16.723" Name="labelEpsilon" VerticalAlignment="Bottom" Width="150">Epsilon</Label>
  18:                  <Label Height="28" HorizontalAlignment="Left" Margin="10,0,0,52.723" Name="labelValue" VerticalAlignment="Bottom" Width="150">A Value (Float or Double)</Label>
  19:                  <Button BorderThickness="3" Click="getDecimalButton_Click" Height="23" HorizontalAlignment="Right" Margin="0,46.638,18,0" Name="getDecimalButton" VerticalAlignment="Top" Width="150">Get Decimal</Button>
  20:              </Grid>
  21:          </GroupBox>
  22:          <GroupBox Header="Is Numeric Check" Margin="18,223,489,0" Name="groupBox2" Height="69" VerticalAlignment="Top">
  23:              <Grid HorizontalAlignment="Stretch" VerticalAlignment="Stretch">
  24:                  <Button HorizontalAlignment="Right" Margin="0,12,18,14.723" Name="getIsNumberic" Width="150" Click="getIsNumberic_Click">Is Numeric</Button>
  25:                  <Label HorizontalAlignment="Left" Margin="10,10,0,11.723" Name="labelIsNumeric" Width="120">Is Numeric?</Label>
  26:                  <TextBox Margin="190,12,198,14.723" Name="textIsNumeric" />
  27:              </Grid>
  28:          </GroupBox>
  29:      </Grid>
  30:  </Window>
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

Now the additional functionality.

```
   1:          private void exitApplicationButton_Click(object sender, RoutedEventArgs e)
   2:          {
   3:              Close();
   4:          }
   5:
   6:          private void getIsNumberic_Click(object sender, RoutedEventArgs e)
   7:          {
   8:              textAnswers.Text = Functions.IsNumeric(textIsNumeric.Text).ToString();
   9:          }
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

Last but not least I’ll put in the validation so I don’t fat finger the wrong value types in the text boxes.  This is a little tricky, but it works.  In most environments you’d want to setup a decent validation framework for this, which might be one of my next blog entries.

```
   1:  #region
   2:
   3:  using System;
   4:  using System.Windows;
   5:  using System.Windows.Controls;
   6:  using MathCookbook;
   7:
   8:  #endregion
   9:
  10:  namespace Maths
  11:  {
  12:      public partial class MathsCooking : Window
  13:      {
  14:          public MathsCooking()
  15:          {
  16:              InitializeComponent();
  17:          }
  18:
  19:          private void getDecimalButton_Click(object sender, RoutedEventArgs e)
  20:          {
  21:              if (textNumerator.Text != string.Empty && Functions.IsNumeric(textNumerator.Text) &&
  22:                  textDenominator.Text != string.Empty && Functions.IsNumeric(textDenominator.Text))
  23:              {
  24:                  textAnswers.Text = Functions.GetDecimalOfFraction(
  25:                      Convert.ToDouble(textNumerator.Text),
  26:                      Convert.ToDouble(textDenominator.Text)).ToString();
  27:              }
  28:              else
  29:              {
  30:                  MessageBox.Show(
  31:                      "You must enter numeric values in the numerator and denominator text boxes.",
  32:                      "Enter values!",
  33:                      MessageBoxButton.OK,
  34:                      MessageBoxImage.Hand,
  35:                      MessageBoxResult.OK);
  36:              }
  37:          }
  38:
  39:          private void getApproximateEqualityButton_Click(object sender, RoutedEventArgs e)
  40:          {
  41:              if (textNumerator.Text != string.Empty && Functions.IsNumeric(textNumerator.Text) &&
  42:                  textDenominator.Text != string.Empty && Functions.IsNumeric(textDenominator.Text) &&
  43:                  textValue.Text != string.Empty && Functions.IsNumeric(textValue.Text) &&
  44:                  textEpsilon.Text != string.Empty && Functions.IsNumeric(textEpsilon.Text))
  45:              {
  46:                  textAnswers.Text = Functions.IsApproximatelyEqualTo(
  47:                      Convert.ToDouble(textNumerator.Text),
  48:                      Convert.ToDouble(textDenominator.Text),
  49:                      Convert.ToDouble(textValue.Text),
  50:                      Convert.ToDouble(textEpsilon.Text)).ToString();
  51:              }
  52:              else
  53:              {
  54:                  MessageBox.Show(
  55:                      "You must enter numeric values in the numerator, denominator, value, and epsilon text boxes.",
  56:                      "Enter values!",
  57:                      MessageBoxButton.OK,
  58:                      MessageBoxImage.Hand,
  59:                      MessageBoxResult.OK);
  60:              }
  61:          }
  62:
  63:          private void exitApplicationButton_Click(object sender, RoutedEventArgs e)
  64:          {
  65:              Close();
  66:          }
  67:
  68:          private void getIsNumberic_Click(object sender, RoutedEventArgs e)
  69:          {
  70:              if (textIsNumeric.Text != string.Empty)
  71:              {
  72:                  textAnswers.Text = Functions.IsNumeric(textIsNumeric.Text).ToString();
  73:              }
  74:              else
  75:              {
  76:                  MessageBox.Show(
  77:                      "Technically string.empty is not numeric, but it is more useful if you enter a value to check.",
  78:                      "Enter a value!",
  79:                      MessageBoxButton.OK,
  80:                      MessageBoxImage.Hand,
  81:                      MessageBoxResult.OK);
  82:              }
  83:          }
  84:      }
  85:  }
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

That’s that.  Now I have a simple application available for providing some simple mathematical calculations.  I’ll be creating another multi-part series, but next on the list will be something a bit different then some mathematical calculations.  Instead I’ll be focusing on putting together some architectural pieces of an application.

The finished code can be downloaded from [Codeplex](http://www.codeplex.com/), via the [C# Cooking Project](http://www.codeplex.com/csharpcooking) I’ve created.
