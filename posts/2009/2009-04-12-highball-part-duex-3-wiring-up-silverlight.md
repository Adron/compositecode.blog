---
title: HighBall Part Duex (#3) Wiring Up Silverlight
date: 2009-04-12 18:40:00 +0000
last_modified_at: 2014-01-08 17:16:10 -0800
permalink: /2009/04/12/highball-part-duex-3-wiring-up-silverlight/
slug: highball-part-duex-3-wiring-up-silverlight
wp_id: 617
original_url: https://compositecode.blog/2009/04/12/highball-part-duex-3-wiring-up-silverlight/
categories:
- .NET Bits
- How-to
tags:
- bootstrapper
- c#
- csharp
- dependency injection
- silverlight
excerpt: 'Navigation of Highball Series Part #1 | Part #2 | Part #3 | Part #4 In this part I’ll be covering wiring up Silverlight with an appropriate module similarly to what part #1 and part #2 covered for WPF. What I want to show in this entry is basically the differences of each module and the difference in the …'
---

Navigation of Highball Series [Part #1](/2009/03/30/highball-part-duex-01/) | [Part #2](/2009/04/01/highball-part-duex-02-adding-the-composite-application-libraries/) | [Part #3](/2009/04/12/highball-part-duex-3-wiring-up-silverlight/) | [Part #4](/2009/04/13/highball-part-duex-4-patterns/)

In this part I’ll be covering wiring up Silverlight with an appropriate module similarly to what [part #1](/2009/03/30/highball-part-duex-01/) and [part #2](/2009/04/01/highball-part-duex-02-adding-the-composite-application-libraries/) covered for WPF.  What I want to show in this entry is basically the differences of each module and the difference in the startup shell.  The differences are however very minimal, which leaves me curious about abstracting some of this and removing the code duplication, or maybe I should say xaml duplication.

One of the things I did after the first two parts of this series is to add some more projects that I would need once wired up and ready to continue with other parts of the project.  First I added the respective test projects, the other [Silverlight](http://silverlight.net/) Module projects etc.

[![](/images/adronhall.smugmug.com/photos/511423290_egGbe-S.png)](http://adronhall.smugmug.com/gallery/7887595_YsDZg#511423290_egGbe)This brings me to one of the differences between the WPF and Silverlight Interfaces.  For the modules that will be used in the Silverlight Project you?ll need to add Silverlight Class Library Project as shown to the left.  The Silverlight Class Library Template adds various assemblies and other references that are needed for these modules to be used in Silverlight Applications.

[![](/images/adronhall.smugmug.com/photos/511422014_hcoKc-S.png)](http://adronhall.smugmug.com/gallery/7887595_YsDZg#511422014_hcoKc)At this time I added a project to match each of the WPF Modules I had added previously.  I created four, then basically created the exact same presenters and views for the Silverlight Module.  After all of this I ended up with the following solution explorer view ? check the image to the right.

The second differences is in the shells and boot strappers.

In the WPF application the shell has the following simple code to kick off of the shell.  I used ReSharper to remove the unnecessary assemblies and other references.

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

What I ended [up](http://www.up.com/) with was simple an OnStartup method overriding the Application Class method.  In this method is simply the base class call, instantiation, and the Run method to kick off the boot strapper.  This is very different then the slew of code needed for the Silverlight application bootstrapper startup.  Now keep in mind that most of this code is generated when you create the Silverlight Application.

```csharp
using System;
using System.Diagnostics;
using System.Windows;
using System.Windows.Browser;

namespace HighBall.Interface.Silverlight
{
    public partial class App : Application
    {
        public App()
        {
            Startup += Application_Startup;
            Exit += Application_Exit;
            UnhandledException += Application_UnhandledException;

            InitializeComponent();
        }

        private void Application_Startup(object sender, StartupEventArgs e)
        {
            var bootstrapper = new HighBallBootStrapper();
            bootstrapper.Run();
        }

        private void Application_Exit(object sender, EventArgs e)
        {
        }

        private void Application_UnhandledException(object sender, ApplicationUnhandledExceptionEventArgs e)
        {
            if (!Debugger.IsAttached)
            {
                e.Handled = true;
                Deployment.Current.Dispatcher.BeginInvoke(delegate { ReportErrorToDOM(e); });
            }
        }

        private void ReportErrorToDOM(ApplicationUnhandledExceptionEventArgs e)
        {
            try
            {
                string errorMsg = e.ExceptionObject.Message + e.ExceptionObject.StackTrace;
                errorMsg = errorMsg.Replace('"', '\").Replace("\r\n", @"\n");

                HtmlPage.Window.Eval("throw new Error(\"Unhandled Error in Silverlight 2 Application " + errorMsg +
                                     "\");");
            }
            catch (Exception)
            {
            }
        }
    }
}
```

The only method that is really altered is the Application\_Startup method.  Simply instantiate the boot strapper and call run.

Now that we have that take a look at the boot strappers themselves.  They each have some respective differences.  The WPF bootstrapper looks like this:

```csharp
using System.Windows;
using HighBall.Interface.Modules.Schedule;
using Microsoft.Practices.Composite.Modularity;
using Microsoft.Practices.Composite.UnityExtensions;

namespace HighBall.Interface.Wpf
{
    internal class HighBallBootStrapper : UnityBootstrapper
    {
        protected override DependencyObject CreateShell()
        {
            var shell = new HighBallShell();
            return shell;
        }

        protected override IModuleCatalog GetModuleCatalog()
        {
            var catalog = new ModuleCatalog();
            catalog.AddModule(typeof(ScheduleAddPresenter));
            return catalog;
        }
    }
}
```

The Silverlight bootstrapper is below:

```csharp
using System.Windows;
using HighBall.Interface.Modules.Schedule.Silverlight;
using Microsoft.Practices.Composite.Modularity;
using Microsoft.Practices.Composite.UnityExtensions;

namespace HighBall.Interface.Silverlight
{
    public class HighBallBootStrapper : UnityBootstrapper
    {
        protected override DependencyObject CreateShell()
        {
            var shell = Container.Resolve();
            Application.Current.RootVisual = shell;
            return shell;
        }

        protected override IModuleCatalog GetModuleCatalog()
        {
            var catalog = new ModuleCatalog();
            catalog.AddModule(typeof(ScheduleAddPresenter));
            return catalog;
        }
    }
}
```

The one difference as one can see is the Silverlight Application sets the Application.Current.RootVisual to the application shell.  Again, one of those places that just screams code duplication.  That?s it.

In my next entry I’m going to do a real quick wrap up and then post the code for what I?ve worked through so far.
