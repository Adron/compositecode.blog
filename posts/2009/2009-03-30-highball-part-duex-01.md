---
title: HighBall Part Duex (#01)
date: 2009-03-30 02:35:00 +0000
last_modified_at: 2014-01-08 17:28:00 -0800
permalink: /2009/03/30/highball-part-duex-01/
slug: highball-part-duex-01
wp_id: 608
original_url: https://compositecode.blog/2009/03/30/highball-part-duex-01/
categories:
- .NET Bits
- How-to
tags:
- c#
- csharp
- dependency injection
- silverlight
excerpt: 'Navigation of Highball Series Part #1 | Part #2 | Part #3 | Part #4 I’m working through this next part of my HighBall Project, which I’ll be blogging regularly, using TDD and UI/X First Development. In other words, to give some context, I’m building out a UI first, then I’ll start from the back end and build together …'
---

Navigation of Highball Series [Part #1](/2009/03/30/highball-part-duex-01/) | [Part #2](/2009/04/01/highball-part-duex-02-adding-the-composite-application-libraries/) | [Part #3](/2009/04/12/highball-part-duex-3-wiring-up-silverlight/) | [Part #4](/2009/04/13/highball-part-duex-4-patterns/)

I’m working through this next part of my [HighBall Project](http://www.codeplex.com/highball), which I’ll be blogging regularly, using TDD and UI/X First Development.  In other words, to give some context, I’m building out a UI first, then I’ll start from the back end and build together using primarily TDD style development.  I’ll admit, I’m a bit unsure of how to go about building out the UI with a TDD style process.  But hopefully by the end of this little application building exercise I’ll have it figured out.

My basic user stories so far is as follows.

1. As a manager I want to create a schedule for a particular route.
2. As a manager I want to delete an old schedule for a particular route.
3. As a manager I want to view all of the schedules for all routes.
4. As a manager I want to view the history of all past schedules for all routes.
5. The driver needs to select a route and view the route schedule.

Basically we have the simple CRUD operations for a schedule tracking system.  I’ll elaborate more as I work through this project.

For the first step I created the follow UI pieces in Silverlight & WPF, one for web and one for desktop.  Eventually I might even toss in the ASP.NET MVC for a non-Silverlight web version.  But for now the first step is to mock up the screens as the manager & drivers would view them.

### Mocking Up the Screens

I created the create screen first to figure out how I would do this.  Keep in mind I’m going at this almost completely blind, as I’m not even sure what the actual architecture might be.  I’m merely giving both of these approaches a shot at the same time.  One last note, I’ll be using [TriMet](http://www.trimet.org), NJ Transit, and [Sound Transit](http://www.soundtransit.org) as my sources of example data, so if it seems familiar, it is.

The first view module that I built was the add route schedule screen.  Upon completion of the basic screen I was amazed at how similar the xaml was for the Silverlight and the WPF.  With this level of similarity I’m thinking there will be many more ways to refactor the xaml itself.  Maybe even create a xaml view generator?  At this point, the goal is to get the view modules created, so back to work.  Here is my first module below.  So far the WPF and Silverlight screen are exactly the same.

```xml
<UserControl x:Class="HighBall.Interface.Wpf.ScheduleAdd"
    xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation&quot;
    xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml&quot;
    Foreground="White" Background="Black">
    <Grid x:Name="LayoutRoot" Background="Black">
        <Grid.ColumnDefinitions>
            <ColumnDefinition></ColumnDefinition>
            <ColumnDefinition></ColumnDefinition>
        </Grid.ColumnDefinitions>
        <Grid.RowDefinitions>
            <RowDefinition Height="25"></RowDefinition>
            <RowDefinition></RowDefinition>
        </Grid.RowDefinitions>
        <TextBlock Margin="5,5,5,5" x:Name="textRoutes">Routes:</TextBlock>
        <ListBox Margin="5,5,5,5" Grid.Column="0" Grid.Row="1" HorizontalAlignment="Stretch" VerticalAlignment="Stretch">
            <ListBoxItem x:Name="routeOne" Content="WES Commuter Rail"></ListBoxItem>
            <ListBoxItem x:Name="routeTwo" Content="9 Powell"></ListBoxItem>
            <ListBoxItem x:Name="routeThree" Content="72 Killingsworth/82nd Ave"></ListBoxItem>
            <ListBoxItem x:Name="routeFour" Content="590 Tacoma/Seattle"></ListBoxItem>
            <ListBoxItem x:Name="routeFive" Content="Sounder Commuter Rail"></ListBoxItem>
            <ListBoxItem x:Name="routeSix" Content="The Newark Light Rail Orange Line"></ListBoxItem>
            <ListBoxItem x:Name="routeSeven" Content="The Newark Light Rail Blue Line"></ListBoxItem>
            <ListBoxItem x:Name="routeEight" Content="The River Line"></ListBoxItem>
        </ListBox>
        <TextBlock x:Name="routeName" Margin="0,5,5,5" Grid.Column="1" Grid.Row="0"  >Add New Schedule</TextBlock>
        <StackPanel Grid.Column="1" Grid.Row="1" >
            <TextBlock x:Name="frequencyIdentifier" Margin="0,5,5,0" Grid.Column="1" Grid.Row="1"  HorizontalAlignment="Left" VerticalAlignment="Top">Frequency Identifier</TextBlock>
            <TextBox x:Name="textFrequencyIdentifier"  Margin="0,5,5,0" Grid.Column="1" Grid.Row="1" Height="23" HorizontalAlignment="Stretch" VerticalAlignment="Top" Text=""></TextBox>
            <TextBlock x:Name="startLocation" Margin="0,5,5,0" Grid.Column="1" Grid.Row="1"  HorizontalAlignment="Left" VerticalAlignment="Top">Start Location</TextBlock>
            <TextBox x:Name="textStartLocation"  Margin="0,5,5,0" Grid.Column="1" Grid.Row="1" Height="23" HorizontalAlignment="Stretch" VerticalAlignment="Top" Text=""></TextBox>
            <TextBlock x:Name="startTime" Margin="0,5,5,0" Grid.Column="1" Grid.Row="1"  HorizontalAlignment="Left" VerticalAlignment="Top">Start Time</TextBlock>
            <TextBox x:Name="textStartTime"  Margin="0,5,5,0" Grid.Column="1" Grid.Row="1" Height="23" HorizontalAlignment="Stretch" VerticalAlignment="Top" Text=""></TextBox>
            <TextBlock x:Name="endLocation" Margin="0,5,5,0" Grid.Column="1" Grid.Row="1"  HorizontalAlignment="Left" VerticalAlignment="Top">End Location</TextBlock>
            <TextBox x:Name="textEndLocation"  Margin="0,5,5,0" Grid.Column="1" Grid.Row="1" Height="23" HorizontalAlignment="Stretch" VerticalAlignment="Top" Text=""></TextBox>
            <TextBlock x:Name="endTime" Margin="0,5,5,0" Grid.Column="1" Grid.Row="1"  HorizontalAlignment="Left" VerticalAlignment="Top">End Time</TextBlock>
            <TextBox  x:Name="textEndTime" Margin="0,5,5,0" Grid.Column="1" Grid.Row="1" Height="23" HorizontalAlignment="Stretch" VerticalAlignment="Top" Text=""></TextBox>
            <TextBlock x:Name="scheduleStarts" Margin="0,5,5,0" Grid.Column="0" HorizontalAlignment="Left" VerticalAlignment="Top">Schedule Starts</TextBlock>
            <TextBox  x:Name="textScheduleStarts" Margin="0,5,5,0" Grid.Column="1" Grid.Row="1" Height="23" HorizontalAlignment="Stretch" VerticalAlignment="Top" Text=""></TextBox>
            <TextBlock x:Name="scheduleEnds" Margin="0,5,5,0" Grid.Column="1"  HorizontalAlignment="Left" VerticalAlignment="Top">Schedule Ends</TextBlock>
            <TextBox  x:Name="textScheduleEnds" Margin="0,5,5,0" Grid.Column="1" Grid.Row="1" Height="23" HorizontalAlignment="Stretch" VerticalAlignment="Top" Text=""></TextBox>
            <Button x:Name="buttonAddNewSchedule" Margin="10,10" Grid.Column="1" Grid.Row="1" Height="Auto" Width="Auto" HorizontalAlignment="Right"  VerticalAlignment="Top" Content="Add Schedule"></Button>
        </StackPanel>
    </Grid>
</UserControl>
```

The next screen I built was the view all module.  Since I would most likely reuse this screen, or at least a large part of it, for the delete screen it would be best not to get the cart before the horse.

```xml
<UserControl x:Class="HighBall.Interface.Silverlight.ScheduleViewAll"
    xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation&quot;
    xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml&quot; >
    <Grid x:Name="LayoutRoot" Background="White">
        <Grid.ColumnDefinitions>
            <ColumnDefinition></ColumnDefinition>
        </Grid.ColumnDefinitions>
        <Grid.RowDefinitions>
            <RowDefinition></RowDefinition>
        </Grid.RowDefinitions>
        <ListBox x:Name="listSchedules">
            <ListBox.ItemTemplate>
                <DataTemplate>
                    <StackPanel Orientation="Horizontal">
                        <TextBlock Width="Auto" Height="Auto" Padding="5" MinWidth="260" Text="{Binding Path=FrequencyIdenfitier}"/>
                        <TextBlock Width="Auto" Height="Auto" Padding="5" MinWidth="210" Text="{Binding Path=Route}"/>
                        <TextBlock Width="Auto" Height="Auto" Padding="5" MinWidth="100" Text="{Binding Path=StartLocation}"/>
                        <TextBlock Width="Auto" Height="Auto" Padding="5" MinWidth="100" Text="{Binding Path=EndLocation}"/>
                        <TextBlock Width="Auto" Height="Auto" Padding="5" MinWidth="140" Text="{Binding Path=ScheduleStarts}"/>
                        <TextBlock Width="Auto" Height="Auto" Padding="5" MinWidth="140" Text="{Binding Path=ScheduleEnds}"/>
                        <TextBlock Width="Auto" Height="Auto" Padding="5" MinWidth="80" Text="{Binding Path=StartTime}"/>
                        <TextBlock Width="Auto" Height="Auto" Padding="5" MinWidth="80" Text="{Binding Path=EndTime}"/>
                    </StackPanel>
                </DataTemplate>
            </ListBox.ItemTemplate>
        </ListBox>
    </Grid>
</UserControl>
```

To test out what it would look like I added the following class and code just for an example.

```csharp
using System;
using System.Collections.Generic;
using System.Windows.Controls;
namespace HighBall.Interface.Silverlight
{
    public partial class ScheduleViewAll : UserControl
    {
        public ScheduleViewAll()
        {
            InitializeComponent();
            var schedules = LoadTestViewData();
            listSchedules.ItemsSource = schedules;
        }
        private static List<RouteSchedule> LoadTestViewData()
        {
            var schedules =
                new List<RouteSchedule>
                    {
                        new RouteSchedule
                            {
                                Route = "WES Commuter Rail",
                                EndLocation = "Beaverton",
                                EndTime = DateTime.Now.AddHours(-5),
                                FrequencyIdenfitier = Guid.NewGuid().ToString(),
                                ScheduleEnds = DateTime.Now.AddDays(185),
                                ScheduleStarts = DateTime.Now.AddDays(5),
                                StartLocation = "Wilsonville",
                                StartTime = DateTime.Now.AddHours(10)
                            },
                        new RouteSchedule
                            {
                                Route = "WES Commuter Rail",
                                EndLocation = "Wilsonville",
                                EndTime = DateTime.Now.AddHours(-5),
                                FrequencyIdenfitier = Guid.NewGuid().ToString(),
                                ScheduleEnds = DateTime.Now.AddDays(185),
                                ScheduleStarts = DateTime.Now.AddDays(5),
                                StartLocation = "Beaverton",
                                StartTime = DateTime.Now.AddHours(10)
                            },
                        new RouteSchedule
                            {
                                Route = "WES Commuter Rail",
                                EndLocation = "Beaverton",
                                EndTime = DateTime.Now.AddHours(-5.5),
                                FrequencyIdenfitier = Guid.NewGuid().ToString(),
                                ScheduleEnds = DateTime.Now.AddDays(185),
                                ScheduleStarts = DateTime.Now.AddDays(5),
                                StartLocation = "Wilsonville",
                                StartTime = DateTime.Now.AddHours(9.5)
                            },
                        new RouteSchedule
                            {
                                Route = "WES Commuter Rail",
                                EndLocation = "Wilsonville",
                                EndTime = DateTime.Now.AddHours(-5.5),
                                FrequencyIdenfitier = Guid.NewGuid().ToString(),
                                ScheduleEnds = DateTime.Now.AddDays(185),
                                ScheduleStarts = DateTime.Now.AddDays(5),
                                StartLocation = "Beaverton",
                                StartTime = DateTime.Now.AddHours(9.5)
                            },
                        new RouteSchedule
                            {
                                Route = "590 Tacoma/Seattle",
                                EndLocation = "Seattle",
                                EndTime = DateTime.Now.AddHours(-5),
                                FrequencyIdenfitier = Guid.NewGuid().ToString(),
                                ScheduleEnds = DateTime.Now.AddDays(185),
                                ScheduleStarts = DateTime.Now.AddDays(5),
                                StartLocation = "Tacoma",
                                StartTime = DateTime.Now.AddHours(10)
                            }
                    };
            return schedules;
        }
    }
    public class RouteSchedule
    {
        public string Route { get; set; }
        public string FrequencyIdenfitier { get; set; }
        public string StartLocation { get; set; }
        public string EndLocation { get; set; }
        public DateTime StartTime { get; set; }
        public DateTime EndTime { get; set; }
        public DateTime ScheduleStarts { get; set; }
        public DateTime ScheduleEnds { get; set; }
    }
}
```

While trying to get this to work in the Silverlight screen I ran into the dreaded “[AG\_E\_INVALID\_ARGUMENT](http://blog.wekeroad.com/2007/07/09/silverlight-how-to-avoid-the-dreaded-ag_e_invalid_argument-2210-error/)” exception.  This is some type of xaml parsing issue, which I jumped right out to [Google](http://www.google.com/) to try and figure out.  The link above eventually led me to this [entry on the silverlight forums](http://silverlight.net/forums/t/1755.aspx).  Even after digging through all of these ancient (in Silverlight terms) fixes, I still had the error.  At this point I threw up my hands and recreated the entire screen.  Once I did that, it worked.  However, the Silverlight xaml screen stopped color coding the xaml correctly and shaded out ALL of the ListBox.ItemTemplate xaml between the tags.  I don’t know what is wrong with this but it is extremely annoying.

StringFormat is another thing that works in WPF but not in Silverlight.  I started to use them to format the date time bound fields.  Since there is this disparity, I just left that as is.  I’ll eventually get back to cleaning up data a bit later.

At this point I needed to wire these together for the customer (which at this point is me, but I’m following Agile Practice).  I didn’t want to get too many UI modules done and then realize I had to change significant parts.  In my next entry I’ll cover working with the Composite Application Library (used to be the Composite Application Block, but that’s evil) to get two builds, one for Silverlight and one for WPF.

Other bits of Information relating to user stories, UI/X, TDD, and other topics.

- [User Stories and Use Cases](http://tynerblain.com/blog/2009/02/02/user-stories-and-use-cases/)
- [Example of a User Story](http://www.agile-software-development.com/2008/01/example-of-user-story.html)
- [User Stories](http://www.agile-software-development.com/2008/01/user-stories.html)
- [Writing Good User Stories](http://www.extremeplanner.com/blog/2006/01/writing-good-user-stories.html)
- [WPF in Action](http://www.manning.com/feldman2/)
- [Using a ConverterParameter in a Silverlight 2 Value Converter](http://blogs.msdn.com/synergist/archive/2008/07/30/using-a-converterparameter-in-a-silverlight-2-value-converter.aspx)
