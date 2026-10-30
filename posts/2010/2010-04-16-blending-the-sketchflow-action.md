---
title: Blending the Sketchflow Action
date: 2010-04-16 14:25:42 +0000
last_modified_at: 2010-07-30 14:52:12 -0700
permalink: /2010/04/16/blending-the-sketchflow-action/
slug: blending-the-sketchflow-action
wp_id: 723
original_url: https://compositecode.blog/2010/04/16/blending-the-sketchflow-action/
categories:
- How-to
tags: []
excerpt: Started a new Sketchflow Prototype in Expression Blend recently and documented each of the steps. This blog entry covers some of those steps, which are the basic elements of any prototype. I will have more information regarding design, prototype creation, and the process of the initial phases for development in the future. For now, I …
---

Started a new Sketchflow Prototype in Expression Blend recently and documented each of the steps.  This blog entry covers some of those steps, which are the basic elements of any prototype.  I will have more information regarding design, prototype creation, and the process of the initial phases for development in the future.  For now, I hope you enjoy this short walk through.  Also, be sure to check out my last [quick entry on Sketchflow](http://blog.adronbhall.com/post/2010/02/22/Sketchflow-and-Clients.aspx).

I started off with a Sketchflow Project, just like I did in my [previous entry](http://blog.adronbhall.com/post/2010/02/22/Sketchflow-and-Clients.aspx) (more specifics in that entry about how to manipulate and build out the [Sketchflow Map](http://blog.adronbhall.com/post/2010/02/22/Sketchflow-and-Clients.aspx)).

![](https://adronhall.smugmug.com/Software/Prototyping/A%C3%BCt%C3%B8chart-Scorecards/Sketchflow-001/838774833_GHVRN-M.png)

Once I created the project I setup the following Sketchflow Map.

![](/images/adronhall.smugmug.com/Software/Prototyping/A-t-chart-Scorecards/Sketchflow-004/838774862_aBa2s-M.png)

The CoreNavigation is a ComponentScreen setup solely for the page navigation at the top of the screen.  The XAML markup in case you want to create a Component Screen with the same design is included below.

```
<UserControl
    xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation"
    xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
    xmlns:d="http://schemas.microsoft.com/expression/blend/2008"
    xmlns:mc="http://schemas.openxmlformats.org/markup-compatibility/2006"
    mc:Ignorable="d"
    xmlns:i="clr-namespace:System.Windows.Interactivity;assembly=System.Windows.Interactivity" xmlns:pb="clr-namespace:Microsoft.Expression.Prototyping.Behavior;assembly=Microsoft.Expression.Prototyping.Interactivity"
    x:Class="RapidPrototypeSketchScreens.CoreNavigation"
    d:DesignWidth="624" d:DesignHeight="49" Height="49" Width="624">
    <Grid x:Name="LayoutRoot">
        <TextBlock HorizontalAlignment="Stretch" Margin="307,3,0,0" Style="{StaticResource TitleCenter-Sketch}" Text="A?t?chart Scorecards" TextWrapping="Wrap">
            <i:Interaction.Triggers>
                <i:EventTrigger EventName="MouseLeftButtonDown">
                    <pb:NavigateToScreenAction TargetScreen="RapidPrototypeSketchScreens.Screen_1"/>
                </i:EventTrigger>
            </i:Interaction.Triggers>
        </TextBlock>
        <Button HorizontalAlignment="Left" Margin="164,8,0,11" Style="{StaticResource Button-Sketch}" Width="144" Content="Scorecard">
            <i:Interaction.Triggers>
                <i:EventTrigger EventName="Click">
                    <pb:NavigateToScreenAction TargetScreen="RapidPrototypeSketchScreens.Screen_1_2"/>
                </i:EventTrigger>
            </i:Interaction.Triggers>
        </Button>
        <Button HorizontalAlignment="Left" Margin="8,8,0,11" Style="{StaticResource Button-Sketch}" Width="152" Content="Standard Reports">
            <i:Interaction.Triggers>
                <i:EventTrigger EventName="Click">
                    <pb:NavigateToScreenAction TargetScreen="RapidPrototypeSketchScreens.Screen_1_1"/>
                </i:EventTrigger>
            </i:Interaction.Triggers>
        </Button>
    </Grid>
</UserControl>
```

Now that the CoreNavigation Component Screen is done I built out each of the others.  In each of those screens I included the CoreNavigation Screen (all those little green lines in the image) as the top navigation.  In order to do that, as I created each of the pages I would hover over the CoreNavigation Object in the Sketchflow Map.  When the utilities drawer (the small menu that pops down under a node when you hover over it) shows click on the third little icon and drag it onto the page node you want a navigation screen on.

Once I created all the screens I setup the navigation by opening up each screen and right clicking on the objects that needed to point to somewhere else in the prototype.

![](/images/adronhall.smugmug.com/Software/Prototyping/A-t-chart-Scorecards/Sketchflow-007/838774889_QYARH-M.png)

Once I was done with the main page, my Home Navigation Page, it looked something like this in the Expression Blend Designer.

![](/images/adronhall.smugmug.com/Software/Prototyping/A-t-chart-Scorecards/Sketchflow-005/838774868_kwaiJ-M.png)

I fleshed out each of the additional screens.  Once I was done I wanted to try out the deployment package.  The way to deploy a Sketchflow Prototype is to merely click on File ?> Package SketchFlow Project and a prompt will appear.  In the prompt enter what you want the package to be called.

![](/images/adronhall.smugmug.com/Software/Prototyping/A-t-chart-Scorecards/Sketchflow-008/838774900_LSawQ-M.png)

I like to see the files generated afterwards too, so I checked the box to see that.  When Expression Blend is done generating everything you?ll have a directory like the one shown below, with all the needed files for deployment.

![](/images/adronhall.smugmug.com/Software/Prototyping/A-t-chart-Scorecards/Sketchflow-009/838774920_WKCjr-M.png)

Now these files can be copied or moved to any location for viewing.  One can even copy them (such as via FTP) to a server location to share with others.  Once they are deployed and you run the “TestPage.html” the other features of the Sketchflow Package are available.

In the image below I have tagged a few sections to show the Sketchflow Player Features.  To the top left is the navigation, which provides a clearly defined area of movement in a list.  To the center right is the actual prototype application.  I have placed lists of things and made edits.  On the left hand side is the highlight feature, which is available in the Feedback section of the lower left.  On the right hand list I underlined the Autochart with an orange marker, and marked out two list items with a red marker.

![](/images/adronhall.smugmug.com/Software/Prototyping/A-t-chart-Scorecards/Sketchflow-010/838850239_qJdBZ-M.png)

In the lower left hand side in the Feedback section is also an area to type in your feedback.  This can be useful for time based feedback, when you post this somewhere and want people to provide subsequent follow up feedback.

Overall lots of great features, that enable some fairly rapid prototyping with customers.  Once one is familiar with the steps and parts of this Sketchflow Prototype Capabilities it is easy to step through an application without even stopping.  It really is that easy.  So get hold of Expression Blend 3 and get ramped up on Sketchflow, it will pay off in the design phases to do so!
