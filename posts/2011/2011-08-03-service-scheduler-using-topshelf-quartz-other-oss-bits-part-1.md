---
title: 'Service & Scheduler: Using Topshelf, Quartz, & Other OSS Bits Part 1'
date: 2011-08-03 17:14:45 -0700
last_modified_at: 2011-08-31 15:44:51 -0700
permalink: /2011/08/03/service-scheduler-using-topshelf-quartz-other-oss-bits-part-1/
slug: service-scheduler-using-topshelf-quartz-other-oss-bits-part-1
wp_id: 3472
original_url: https://compositecode.blog/2011/08/03/service-scheduler-using-topshelf-quartz-other-oss-bits-part-1/
categories:
- .NET Bits
- How-to
tags:
- nuget
- topshelf
- windows service
excerpt: This how-to entry will detail the steps for getting Topshelf installed, running, and a schedule integrated and timed appropriately using Quartz. Once that is complete I’ll go over how to get custom schedules added to the service. Topshelf To get Topshelf up and running open up Visual Studio, start a Windows Console Project, and then use …
---

![](/images/adronhall.smugmug.com/Software/Software-Development/Topshelf-Services/i-LTdCZM7/0/O/1312408528runningprocess.png)This how-to entry will detail the steps for getting Topshelf installed, running, and a schedule integrated and timed appropriately using Quartz. Once that is complete I’ll go over how to get custom schedules added to the service.

## [Topshelf](http://topshelf-project.com/)

To get [Topshelf](http://topshelf-project.com/) up and running open up Visual Studio, start a Windows Console Project, and then use [Nuget](http://nuget.codeplex.com/) (if you don’t have [Nuget](http://nuget.codeplex.com/) installed, I suggest doing that ASAP, you’ll need it to follow along with any reference additions).

[![Get Topshelf Through Nuget](/images/adronhall.smugmug.com/Software/Software-Development/Topshelf-Services/i-DTj9b3Q/0/S/step-01-S.png "Get Topshelf Through Nuget")](http://adronhall.smugmug.com/Software/Software-Development/Topshelf-Services/18361245_KpnDbM/1414634731_Nk2Gtnm#1414704308_DTj9b3Q-O-LB)

*Get Topshelf Through Nuget*

Once you have Topshelf and associated references added via Nuget create a new class file called StatusCheckIn and add the following code.

```csharp
using System;
using System.Timers;

namespace Sample.Services
{
    public class StatusCheckIn
    {
        readonly Timer _timer;

        public StatusCheckIn()
        {
            _timer = new Timer(5000) { AutoReset = true };
            _timer.Elapsed += TimeHappened;
        }

        static void TimeHappened(object sender, EventArgs eventArgs)
        {
            Console.WriteLine("Status Time: {0} checking in.",
                DateTime.Now);
            Console.WriteLine("Sender Type: {0}",
                sender.GetType());
            Console.WriteLine("Event Argument Type: {0}",
                eventArgs);
        }

        public void Start()
        {
            _timer.Start();
        }

        public void Stop()
        {
            _timer.Stop();
        }
    }
}
```

After adding the StatusCheckIn Class, open up the Program.cs file and add or change the following code.

```csharp
using Topshelf;

namespace Sample.Services
{
    class Program
    {
        static void Main()
        {
            HostFactory.Run(hostConfigurator =>
            {
                hostConfigurator.Service<StatusCheckIn>(
                    serviceConfigurator =>
                {
                    serviceConfigurator.SetServiceName("TS");
                    serviceConfigurator.ConstructUsing(
                        name => new StatusCheckIn());
                    serviceConfigurator.WhenStarted(tc => tc.Start());
                    serviceConfigurator.WhenStopped(tc => tc.Stop());
                });

                hostConfigurator.RunAsLocalSystem();
                hostConfigurator.SetDescription("Sample  Host");
                hostConfigurator.SetDisplayName("Display Name");
                hostConfigurator.SetServiceName("Topshelf Service");
            });
        }
    }
}
```

If you run into an odd reference error, it is likely that VS2010 has determined you want the client profile of .NET 4.0 again. If anyone at MS on the VS2010/.NET 4.0 reads this, we DO NOT want this to be the default. It’s ridiculous that it gets set as default without some type of manual change. But I digress, open up the properties of the console/service project and set it under the dialog as shown.

[![Setting the appropriate .NET 4.0 Version in the Properties Dialog](/images/adronhall.smugmug.com/Software/Software-Development/Topshelf-Services/i-dbwsX9b/1/S/step-02-S.jpg "Setting the appropriate .NET 4.0 Version in the Properties Dialog")](http://adronhall.smugmug.com/Software/Software-Development/Topshelf-Services/18361245_KpnDbM/1414634731_Nk2Gtnm#1414704326_dbwsX9b-O-LB)

*Setting the appropriate .NET 4.0 Version in the Properties Dialog*

***NOTES***: Working code available on Github under my [Topshelf Repo](https://github.com/Adron/Topshelf).
