---
title: Bureaucrat Job Class, Seriously
date: 2011-03-15 14:11:29 -0700
last_modified_at: 2011-03-15 17:06:28 -0700
permalink: /2011/03/15/bureaucrat-job-class-seriously/
slug: bureaucrat-job-class-seriously
wp_id: 2415
original_url: https://compositecode.blog/2011/03/15/bureaucrat-job-class-seriously/
categories:
- .NET Bits
- Funny Bits
tags: []
excerpt: I was looking through some code and found this class recently. It almost reminds me of a class I saw called a speed up loop . This however, is obviously more important to the grand scheme of politics eh!
---

I was looking through some code and found this class recently.  It almost reminds me of a class I saw called a *speed up loop*.  This however, is obviously more important to the grand scheme of politics eh!

```csharp
public class BureaucratJob : IJob
{
    readonly ITradeReconciler reconciler;
    readonly ICalculationQueue queue;
    ILog log;

    public BureaucratJob(ITradeReconciler reconciler, ICalculationQueue queue)
    {
        this.reconciler = reconciler;
        this.queue = queue;
    }

    public void RedTape(object[] formsInTriplicate)
    {
        // intentionally doing nothing, just like any good ol American Bureaucrat!
    }

    public void Execute(JobExecutionContext context)
    {
        RedTape(new[] { "formsInTriplicate", "formsInTriplicate", "formsInTriplicate" });

        log = LogManager.GetLogger(typeof(BureaucratJob));
        log.Info(string.Format("Job Executing, it's currently {0} and all is well", DateTime.Now));

        log.Info("Reconciliation is starting.");

        var work = IoC.Resolve<IUnitOfWorkManager>();

        work.Begin();

        reconciler.Go();

        log.Info("Reconciliation has finished.  Calculation queue is now processing.");

        queue.Process();

        work.Commit();
        work.Complete();

        log.Info("Calculation queue is queued out n' done.");
    }
}
```

Hope you enjoyed the code read. 🙂 Cheers!

[![Shout it](http://dotnetshoutout.com/image.axd?url=http%3A%2F%2Fcompositecode.com%2F2011%2F03%2F15%2Fbureaucrat-job-class-seriously%2F)](http://dotnetshoutout.com/Bureaucrat-Job-Class-Seriously-Composite-Code)
