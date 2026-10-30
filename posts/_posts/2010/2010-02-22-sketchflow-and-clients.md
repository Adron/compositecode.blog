---
title: Sketchflow and Clients
date: 2010-02-22 01:13:00 -0800
last_modified_at: 2010-07-30 14:52:10 -0700
permalink: /2010/02/22/sketchflow-and-clients/
slug: sketchflow-and-clients
wp_id: 693
original_url: https://compositecode.blog/2010/02/22/sketchflow-and-clients/
categories:
- Uncategorized Bits
tags: []
excerpt: Sketchflow is a project template type that can be created to quickly prototype application design, quick UI experiments, and communicating design intent. I decided, to get a bit more practiced at using the Sketchflow capabilities, that I would write a quick tutorial on starting and creating a basic Sketchflow Application. First step, open up Microsoft …
---

Sketchflow is a project template type that can be created to quickly prototype application design, quick UI experiments, and communicating design intent.  I decided, to get a bit more practiced at using the Sketchflow capabilities, that I would write a quick tutorial on starting and creating a basic Sketchflow Application.

First step, open up Microsoft Expression Blend 3.  Then click on *File* and then *New Project*.  In that dialog you will see the available Expression Blend Project Templates.  For this tutorial I selected the Silverlight Project Types, then the Silverlight 3 SketchFlow Application Project Template to the right.  (Click for full size image)

[![](/images/adronhall.smugmug.com/Software/Prototyping/SketchFlow/Sketchflow-001/793570888_P2e9B-M.png)](http://adronhall.smugmug.com/Software/Prototyping/SketchFlow)

When the project opens up a standard XAML screen will be displayed called Screen 1 (Screen 1.xaml).  There is also a *SketchFlow Map*, if it is not showing use *Shift + F12* or select *Window* and then *SketchFlow Map* on the menus.  That will get the following screens showing.  Feel free to position those wherever you need them to work within the *SketchFlow Map*.  (Click for full size image)

[![](/images/adronhall.smugmug.com/Software/Prototyping/SketchFlow/Sketchflow-002/793570900_TGtth-M.png)](http://adronhall.smugmug.com/Software/Prototyping/SketchFlow)

Next right click on the Screen 1 Node and rename the node to *Set Credentials*.  Now hover with your mouse over the node until the utilities drawer shows up.  Click on the *Create a Connected Screen* icon in the utilities drawer and hold down and drag.  This will allow you to create a connected node.  (Click for full size image)

[![](/images/adronhall.smugmug.com/Software/Prototyping/SketchFlow/Sketchflow-003/793570904_o6xA9-M.png)](http://adronhall.smugmug.com/Software/Prototyping/SketchFlow)

[![](/images/adronhall.smugmug.com/Software/Prototyping/SketchFlow/Sketchflow-002a/793570903_qFfFQ-M.png)](http://adronhall.smugmug.com/Software/Prototyping/SketchFlow)

I created each node as shown, one for the Set Credentials, View Scorecard, and Select Reports screens.  In the Projects tab that shows the Solution and the XAML files I renamed each file so it is easily referenced to the node that the XAML file represents.

[![](/images/adronhall.smugmug.com/Software/Prototyping/SketchFlow/Sketchflow-004/793570919_J7vu8-M.png)](http://adronhall.smugmug.com/Software/Prototyping/SketchFlow)

Now that each screen exists, I have created the following screens.  The first one of course, is the *Set Credentials Screen/SetCredentials.xaml*.  The XAML is below to make creation of the screen super easy.

```
<UserControl
    xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation"
    xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
    xmlns:d="http://schemas.microsoft.com/expression/blend/2008"
    xmlns:mc="http://schemas.openxmlformats.org/markup-compatibility/2006"
    mc:Ignorable="d"
    xmlns:i="clr-namespace:System.Windows.Interactivity;assembly=System.Windows.Interactivity" xmlns:pb="clr-namespace:Microsoft.Expression.Prototyping.Behavior;assembly=Microsoft.Expression.Prototyping.Interactivity"
    x:Class="AnalyticsScorecardApplicationSketchScreens.Screen_1"
    Width="640" Height="480">

    <Grid x:Name="LayoutRoot" Background="White">
        <TextBox x:Name="textAccount" Height="25" HorizontalAlignment="Left" Margin="79,88,0,0" Style="{StaticResource BasicTextBox-Sketch}" VerticalAlignment="Top" Width="136" Text="webtrends_com" TextWrapping="Wrap" ToolTipService.ToolTip="Enter your account here."/>
        <PasswordBox x:Name="passwordBox" Height="25" HorizontalAlignment="Right" Margin="0,88,103,0" Style="{StaticResource PasswordBox-Sketch}" VerticalAlignment="Top" Width="136" Password="XXXXXXX" ToolTipService.ToolTip="Enter your password here."/>
        <TextBox x:Name="textUsername" Height="25" Margin="241,89,263,0" Style="{StaticResource BasicTextBox-Sketch}" VerticalAlignment="Top" TextWrapping="Wrap" ToolTipService.ToolTip="Enter your username here." Text="Adron"/>
        <Button x:Name="buttonLoginSetCredentials" HorizontalAlignment="Right" Margin="0,159,103,0" Style="{StaticResource Button-Sketch}" VerticalAlignment="Top" Width="201" Content="Login &amp; Set Credentials">
            <i:Interaction.Triggers>
                <i:EventTrigger EventName="Click">
                    <pb:NavigateToScreenAction TargetScreen="AnalyticsScorecardApplicationSketchScreens.Screen_1_3"/>
                </i:EventTrigger>
            </i:Interaction.Triggers>
        </Button>
        <TextBlock HorizontalAlignment="Left" Margin="81,60,0,0" Style="{StaticResource BasicTextBlock-Sketch}" VerticalAlignment="Top" Text="Account" TextWrapping="Wrap"/>
        <TextBlock HorizontalAlignment="Left" Margin="242,60,0,0" Style="{StaticResource BasicTextBlock-Sketch}" VerticalAlignment="Top" Text="Username" TextWrapping="Wrap"/>
        <TextBlock HorizontalAlignment="Right" Margin="0,60,181,0" Style="{StaticResource BasicTextBlock-Sketch}" VerticalAlignment="Top" Text="Password" TextWrapping="Wrap"/>
    </Grid>
</UserControl>
```

Now that we have this screen, I will step through some of the things I did to make this screen functional for the prototype.  The main thing, is to assure that the button is linked up to the right navigation.  Right click on the button and look for the Navigation items and select the screen it will navigate to, as shown below.

[![](/images/adronhall.smugmug.com/Software/Prototyping/SketchFlow/Sketchflow-005/793570925_AZDZv-M.png)](http://adronhall.smugmug.com/Software/Prototyping/SketchFlow)

Next create the following two screens to show the appropriate navigation and screens to navigate to.

*Select Reports / SelectReports.xaml Screen*

```
<UserControl
    xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation"
    xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
    xmlns:d="http://schemas.microsoft.com/expression/blend/2008"
    xmlns:mc="http://schemas.openxmlformats.org/markup-compatibility/2006"
    mc:Ignorable="d"
    xmlns:i="clr-namespace:System.Windows.Interactivity;assembly=System.Windows.Interactivity" xmlns:pb="clr-namespace:Microsoft.Expression.Prototyping.Behavior;assembly=Microsoft.Expression.Prototyping.Interactivity"
    x:Class="AnalyticsScorecardApplicationSketchScreens.Screen_1"
    Width="640" Height="480">

    <Grid x:Name="LayoutRoot" Background="White">
        <TextBox x:Name="textAccount" Height="25" HorizontalAlignment="Left" Margin="79,88,0,0" Style="{StaticResource BasicTextBox-Sketch}" VerticalAlignment="Top" Width="136" Text="webtrends_com" TextWrapping="Wrap" ToolTipService.ToolTip="Enter your account here."/>
        <PasswordBox x:Name="passwordBox" Height="25" HorizontalAlignment="Right" Margin="0,88,103,0" Style="{StaticResource PasswordBox-Sketch}" VerticalAlignment="Top" Width="136" Password="XXXXXXX" ToolTipService.ToolTip="Enter your password here."/>
        <TextBox x:Name="textUsername" Height="25" Margin="241,89,263,0" Style="{StaticResource BasicTextBox-Sketch}" VerticalAlignment="Top" TextWrapping="Wrap" ToolTipService.ToolTip="Enter your username here." Text="Adron"/>
        <Button x:Name="buttonLoginSetCredentials" HorizontalAlignment="Right" Margin="0,159,103,0" Style="{StaticResource Button-Sketch}" VerticalAlignment="Top" Width="201" Content="Login &amp; Set Credentials">
            <i:Interaction.Triggers>
                <i:EventTrigger EventName="Click">
                    <pb:NavigateToScreenAction TargetScreen="AnalyticsScorecardApplicationSketchScreens.Screen_1_3"/>
                </i:EventTrigger>
            </i:Interaction.Triggers>
        </Button>
        <TextBlock HorizontalAlignment="Left" Margin="81,60,0,0" Style="{StaticResource BasicTextBlock-Sketch}" VerticalAlignment="Top" Text="Account" TextWrapping="Wrap"/>
        <TextBlock HorizontalAlignment="Left" Margin="242,60,0,0" Style="{StaticResource BasicTextBlock-Sketch}" VerticalAlignment="Top" Text="Username" TextWrapping="Wrap"/>
        <TextBlock HorizontalAlignment="Right" Margin="0,60,181,0" Style="{StaticResource BasicTextBlock-Sketch}" VerticalAlignment="Top" Text="Password" TextWrapping="Wrap"/>
    </Grid>
</UserControl>

View Scorecard / ViewScorecard.xaml Screen
```

```html
<UserControl
    xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation"
    xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
    xmlns:d="http://schemas.microsoft.com/expression/blend/2008"
    xmlns:mc="http://schemas.openxmlformats.org/markup-compatibility/2006"
    mc:Ignorable="d"
    xmlns:i="clr-namespace:System.Windows.Interactivity;assembly=System.Windows.Interactivity" xmlns:pb="clr-namespace:Microsoft.Expression.Prototyping.Behavior;assembly=Microsoft.Expression.Prototyping.Interactivity" xmlns:local="clr-namespace:AnalyticsScorecardApplicationSketchScreens"
    x:Class="AnalyticsScorecardApplicationSketchScreens.Screen_1_3"
    Width="640" Height="480">

    <Grid x:Name="LayoutRoot" Background="White">
        <Button HorizontalAlignment="Right" Style="{StaticResource Button-Sketch}" VerticalAlignment="Top" Width="122" Content="Select Reports" Margin="0,24,158,0" Cursor="Hand">
            <i:Interaction.Triggers>
                <i:EventTrigger EventName="Click">
                    <pb:NavigateToScreenAction TargetScreen="AnalyticsScorecardApplicationSketchScreens.Screen_1_4"/>
                </i:EventTrigger>
            </i:Interaction.Triggers>
        </Button>
        <Button Style="{StaticResource Button-Sketch}" Content="Set Credentials" Cursor="Hand" Height="30" HorizontalAlignment="Right" VerticalAlignment="Top" Width="122" Margin="0,25,19,0">
            <i:Interaction.Triggers>
                <i:EventTrigger EventName="Click">
                    <pb:NavigateToScreenAction TargetScreen="AnalyticsScorecardApplicationSketchScreens.Screen_1"/>
                </i:EventTrigger>
            </i:Interaction.Triggers>
        </Button>
    </Grid>
</UserControl>
```

That’s it for this entry.  For now this is a complete working SketchFlow Application.  Just run it and you’ll see a screen that you can navigate around as shown below.

[![](/images/adronhall.smugmug.com/Software/Prototyping/SketchFlow/Sketchflow-006/793570971_KzY2J-M.png)](http://adronhall.smugmug.com/Software/Prototyping/SketchFlow)

I’ll have another one when I get to fleshing out the various parts of the prototype more.  I intend to do a complete work-through, but we all know about intents and blog entries.  So I shall see.
