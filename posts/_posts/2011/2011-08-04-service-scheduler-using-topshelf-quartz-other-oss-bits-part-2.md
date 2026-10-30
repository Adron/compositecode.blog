---
title: 'Service & Scheduler: Using Topshelf, Quartz, & Other OSS Bits Part 2'
date: 2011-08-04 11:58:16 -0700
last_modified_at: 2011-08-04 20:32:17 -0700
permalink: /2011/08/04/service-scheduler-using-topshelf-quartz-other-oss-bits-part-2/
slug: service-scheduler-using-topshelf-quartz-other-oss-bits-part-2
wp_id: 3486
original_url: https://compositecode.blog/2011/08/04/service-scheduler-using-topshelf-quartz-other-oss-bits-part-2/
categories:
- .NET Bits
- How-to
tags:
- quartz
- quartz.net
- schedule
- scheduler
excerpt: In the previous entry in this series I setup a service using TopShelf. Now it is time to jump into scheduling with Quartz. I’ve started an entirely new service to work through an example of this service functionality. Open up Visual Studio and create another Windows Console Project. …click to read more…
---

In the previous entry in this series I setup a service using TopShelf.![](/images/adronhall.smugmug.com/Software/Software-Development/Topshelf-Services/i-dHkV2XW/0/O/1312438675calendar.png) Now it is time to jump into scheduling with Quartz. I’ve started an entirely new service to work through an example of this service functionality.

To read more about [Quartz.NET](http://www.quartz-scheduler.net/) from the source, check out the [Quartz.NET Project Site](http://www.quartz-scheduler.net/) or the [Github Repo](https://github.com/quartznet/quartznet/).

Open up Visual Studio and create another Windows Console Project. Next add a reference to [Quartz.NET](http://www.quartz-scheduler.net/) with Nuget.

[![Adding Quartz.](/images/adronhall.smugmug.com/Software/Software-Development/Topshelf-Services/i-NKBWt6f/0/S/step-09-S.png "Adding Quartz.")](http://adronhall.smugmug.com/Software/Software-Development/Topshelf-Services/18361245_KpnDbM#1415821473_NKBWt6f-O-LB)

*Adding Quartz.*

Next add a class called SomeJob as shown.

```csharp
using System;
using Quartz;

namespace quartz
{
    public class SomeJob : IJob
    {
        public SomeJob() { }

        public void Execute(JobExecutionContext context)
        {
            Console.WriteLine("DumbJob is executing.");
        }
    }
}
```

Next add and change the code in Program.cs to the code below.

```csharp
using System;
using Quartz;
using Quartz.Impl;

namespace quartz
{
    class Program
    {
        static void Main()
        {
            var schedFact = new StdSchedulerFactory();

            var sched = schedFact.GetScheduler();
            sched.Start();

            var jobDetail =
                new JobDetail("myJob", null, typeof(SomeJob));

            var trigger = TriggerUtils.MakeSecondlyTrigger(5);
            trigger.StartTimeUtc = DateTime.UtcNow;
            trigger.Name = "myTrigger";
            sched.ScheduleJob(jobDetail, trigger);
        }
    }
}
```

***NOTES***: Working code available on Github under my [Quartz Repo](https://github.com/Adron/Quartz).
