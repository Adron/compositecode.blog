---
title: HighBall Part Duex (#02) Adding the Composite Application Libraries
date: 2009-04-01 13:50:27 -0700
last_modified_at: 2014-01-08 17:43:16 -0800
permalink: /2009/04/01/highball-part-duex-02-adding-the-composite-application-libraries/
slug: highball-part-duex-02-adding-the-composite-application-libraries
wp_id: 609
original_url: https://compositecode.blog/2009/04/01/highball-part-duex-02-adding-the-composite-application-libraries/
categories:
- .NET Bits
- How-to
tags:
- c#
- csharp
- dependency injection
excerpt: 'Navigation of Highball Series Part #1 | Part #2 | Part #3 | Part #4 The first thing I did was go download the Composite Application Library Guidance. The Patterns & Practices Group Page on the Composite Application Library is available also with more links and information. The steps I took to get all the CAL stuff added went …'
---

Navigation of Highball Series [Part #1](/2009/03/30/highball-part-duex-01/) | [Part #2](/2009/04/01/highball-part-duex-02-adding-the-composite-application-libraries/) | [Part #3](/2009/04/12/highball-part-duex-3-wiring-up-silverlight/) | [Part #4](/2009/04/13/highball-part-duex-4-patterns/)

The first thing I did was go download the [Composite Application Library Guidance](http://www.microsoft.com/downloads/details.aspx?FamilyID=fa07e1ce-ca3f-4b9b-a21b-e3fa10d013dd&DisplayLang=en).  The [Patterns & Practices](http://msdn.microsoft.com/en-us/practices/default.aspx) Group Page on the [Composite Application Library](http://msdn.microsoft.com/en-us/library/dd458809.aspx) is available also with more links and information.  The steps I took to get all the CAL stuff added went something like this.

- I added the projects & test projects for;  Composite.Desktop, Composite.Desktop.Tests, Composite.Presentation.Desktop, Composite.Presentation.Desktop.Tests, Composite.UnityExtensions.Desktop, Composite.UnityExtensions.Desktop.Tests.
- Then I added the Microsoft.Practices.ServiceLocation.dll to the 3rd Party Assemblies directory and fixed the references in the above projects.  Since I had literally copied them from the CAL directory that the installer places them, I had to fix up the references, but I had done so on purpose so that I’d know exactly what references what.

After adding that I setup a project for my first module named *HighBall.Interface.Modules.ScheduleModule*.  In this module I made a view called *ScheduleAddView.xaml* and a module called *ScheduleAddModule.cs*.  In the xaml view I added the following markup, which is identical to the markup I created for the *ScheduleAdd.xaml* in the [previous blog post](http://www.adronbhall.com/blogs/technology__software_development/post/2009/03/30/HighBall-Part-Duex-(01).aspx).

```xml
<UserControl x:Class="HighBall.Interface.Modules.ScheduleModule.Views.ScheduleAdd"
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

In the code behind and the class file I added nothing at this time.  We?ll come back to that in a minute.

Once I created that I went back to the *HighBall.Interface.Wpf* project that I had created in the [previous blog entry](http://www.adronbhall.com/blogs/technology__software_development/post/2009/03/30/HighBall-Part-Duex-(01).aspx).  I then added a *HighBallBootStrapper.cs* class file to the project.  In that file I added the following code.

```csharp
using System.Windows;
using HighBall.Interface.Modules.ScheduleModule;
using Microsoft.Practices.Composite.Modularity;
using Microsoft.Practices.Composite.UnityExtensions;

namespace HighBall.Interface.Wpf
{
    class HighBallBootStrapper : UnityBootstrapper
    {
        protected override DependencyObject CreateShell()
        {
            var shell = new HighBallShell();
            shell.Show();
            return shell;
        }
        protected override IModuleCatalog GetModuleCatalog()
        {
            var catalog = new ModuleCatalog()
                .AddModule(typeof (ScheduleAddModule));
            return catalog;
        }
    }
}
```

In the code behind of the *App.xaml* file I then added the following.

```csharp
using System.Windows;
namespace HighBall.Interface.Wpf
{
    public partial class App : Application
    {
        protected override void OnStartup(StartupEventArgs e)
        {
            base.OnStartup(e);
            var bootstrapper = new HighBallBootStrapper();
            bootstrapper.Run();
        }
    }
}
```

Now that we?re wired up there, we move on to the last few steps.  The next step is to wire the module up so it will show up in the shell when it is launched.  So open up the *ScheduleAddModule.cs* class file and add the following code.

```csharp
using HighBall.Interface.Modules.ScheduleModule.Views;
using Microsoft.Practices.Composite.Modularity;
using Microsoft.Practices.Composite.Regions;
namespace HighBall.Interface.Modules.ScheduleModule
{
    public class ScheduleAddModule : IModule
    {
        private readonly IRegionViewRegistry regionViewRegistry;
        public ScheduleAddModule(IRegionViewRegistry registry)
        {
            regionViewRegistry = registry;
        }

        public void Initialize()
        {
            regionViewRegistry.RegisterViewWithRegion("HighBallMainRegion", typeof(ScheduleAddView));
        }
    }
}
```

Before wrapping up I went ahead and added the remaining view into the module project that is still in the *HighBall.Interface.Wpf project*.  Now I have the ScheduleViewAll.xaml view in the *HighBall.Interface.Modules.ScheduleModule* project.  Just to make sure all the associations where correct I actually made the file and THEN copied all of the xaml into the new file.  That way everything gets generated correctly.

I did run into an odd scenario during working through this example.  I launched the application and everything showed up as it is supposed to, BUT, two application screens would pop up.  I fiddled around a bit more and ended up with a blank screen with my injection broken.  Eventually I got it working but it was really odd regardless.

In my next entry I’ll be getting into describing the nuts and bolts of what is going on so far to provide some context.
