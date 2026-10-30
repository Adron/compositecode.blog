---
title: Ways to Interact Asynchronously with C#
date: 2012-09-15 14:36:43 -0700
last_modified_at: 2012-09-16 11:09:59 -0700
permalink: /2012/09/15/ways-to-interact-asynchronously-with-c/
slug: ways-to-interact-asynchronously-with-c
wp_id: 6575
original_url: https://compositecode.blog/2012/09/15/ways-to-interact-asynchronously-with-c/
categories:
- .NET Bits
- Cloud Foundry
- How-to
- Iron Foundry
- Platform (as a Service)
- Thor Project
tags:
- cloud
- cloud computing
- cloud foundry
- cloudfoundry
- iron foundry
- ironfoundry
- paas
- platform as a service
- thor
- thor project
- thorproject
- vcap
- vcap client
excerpt: 'NOTE: All of this code is available at my Github Project “Remembering” ( https://github.com/Adron/Remembering ). Feel free to fork it, share it, or send me corrections or pull requests. While working on the Thor Project there have been numerous situations where I need to fire off an asynchronous callback in C# while maintaining good responsiveness in the …'
---

***NOTE: All of this code is available at my [Github Project “Remembering” (https://github.com/Adron/Remembering)](https://github.com/Adron/Remembering). Feel free to fork it, share it, or send me corrections or pull requests.***

[![](/images/adronhall.smugmug.com/Software/Software-Development/Thor/i-GwfBwZn/0/S/hammer-S-S.png)](http://www.ironfoundry.org)While working on the [Thor Project](http://www.ironfoundry.org/thor) there have been numerous situations where I need to fire off an asynchronous callback in C# while maintaining good responsiveness in the actual user interface. Benjamin (@bvanderveen) has been using [Reactive Extensions with subscriptions to do this in the Objective-C](/2012/09/03/thor-cool-objective-c-bits-libraries-and-code-snippets-theseries-alloc-init/) code for the [Cocoa based OS-X Thor](http://www.ironfoundry.org/thor) user interface. See my [previous blog](/2012/09/03/thor-cool-objective-c-bits-libraries-and-code-snippets-theseries-alloc-init/) entry for an example of what he’s doing.

For a good example of asynchronous calls against Cloud Foundry I setup the following project using the Iron Foundry Project VCAP Client Library. The first thing I setup was a static class with a few constants to use across the examples for the URI, username and password for the Cloud Foundry Account.

```csharp
public static class YourSecrets
{
    public const string Username = "youremail@someplace.com";
    public const string Password = "AnAwesom3HardPassw0rd!";
    public const string Uri = "http://api.yourpaas.com&quot;;
}
```

[![](/images/adronhall.smugmug.com/Software/Software-Development/Thor/i-jwLWNnb/0/S/VMW-LGO-CloudFoundry-217-S.png)](http://www.cloudfoundry.org)Next step was to setup the delegate and method I’d use for calling out to the Cloud Foundry environment and retrieving data in parallel to my active console or user interface. That code snippet looked like this. I also added a private variable \_finished for use in tracking when the request was completed in the begin and end invoke example below.

```csharp
private bool _finished;

IEnumerable TheMethodToConnectThatWillTakeLongTime(string uri)
{
    var client = new VcapClient(uri);
    client.Login(TheSecretBits.YourSecrets.Username, TheSecretBits.YourSecrets.Password);

    _finished = false;

    return client.GetApplications();
}

delegate IEnumerable MethodDelegate(string uri);
```

Once I had that setup I was ready to create my baseline method that would make a synchronous call. A synchronous call is one that makes the call as if it just called the method directly. There’s no real reason to create one like I’ve done here, but I was just using it to provide a basic example of calling the delegate.

```csharp
public void SynchronousCall()
{
    var starting = DateTime.Now.ToLongTimeString();

    var delegateMethod = new MethodDelegate(TheMethodToConnectThatWillTakeLongTime);
    var returnedBits = delegateMethod(TheSecretBits.YourSecrets.Uri);

    var ending = DateTime.Now.ToLongTimeString();

    Console.WriteLine(string.Format("The delegate call returned \n\n{0}\n\nstarting at {1} and

ending at {2} which takes a while of waiting.",
        returnedBits, starting, ending));

    _finished = false;
}
```

That gets us a baseline. If you run a synchronous call against anything with a console application or a windows app, WPF or whatever it will lock up the calling thread while it is waiting for a response. In any type of user interface that is unacceptable. One of the best options is to fire of an asynchronous callback. The way I did this, which is an ideal way to make calls with the Iron Foundry Client Library against a Cloud Foundry Environment, is shown below.

This is my asynchronous call.

```csharp
public void DemoCall()
{
    Console.WriteLine("Callback:");
    var delegateMethod = new MethodDelegate(TheMethodToConnectThatWillTakeLongTime);

    var callbackDelegate = new AsyncCallback(MyAsyncCallback);

    Console.WriteLine(" starting...{0}", DateTime.Now.ToLongTimeString());
    delegateMethod.BeginInvoke(TheSecretBits.YourSecrets.Uri, callbackDelegate, delegateMethod);
    Console.WriteLine(" ending...{0}", DateTime.Now.ToLongTimeString());
}
```

Now the simple callback.

```csharp
public void MyAsyncCallback(IAsyncResult ar)
{
    Console.WriteLine("Things happening, async state calling.");

    var delegateMethod = (MethodDelegate)ar.AsyncState;

    Console.WriteLine(" called...{0}", DateTime.Now.ToLongTimeString());

    var returnedBits = delegateMethod.EndInvoke(ar);

    Console.WriteLine(" end invoked...{0}", DateTime.Now.ToLongTimeString());

    foreach (Application application in returnedBits)
    {
        Console.WriteLine("Application {0} is in {1} state...",
            application.Name, application.State);
        Console.WriteLine(" with {0} running instances, {1} memory per instance, {2} disk allocated...",
            application.RunningInstances, application.Resources.Memory, application.Resources.Disk);
        Console.Write(" hosted at ");
        foreach (var uri in application.Uris)
        {
            Console.Write(uri + " ");
        }
        Console.WriteLine(".");
    }
}
```

That’ll get the call running on a parallel thread and when it is wrapped up it returns the data.

## The User Interface Interaction Issue

This is all fine and dandy for the command console. But if you want to give control back to the UI thread in a UI application and make sure that the background thread can actually update a control when fired off, do the same thing as I’ve discussed here except set the control up to invoke the dispatcher, so that the “threads don’t cross” when trying to return information to a control that needs updated. In order to do this take the control that needs updated and set the Dispatcher Invoke method as shown below.

```csharp
private void Write(string updateText)
{
    UpdatingTextBlock.Dispatcher.Invoke(
    System.Windows.Threading.DispatcherPriority.Normal,
        new Action(delegate
    {
        UpdatingTextBlock.Text += updateText;
    }
    ));
}
```

For more on the Iron Foundry Project and the library I’ve used here, check out the [Iron Foundry Blog](http://blog.ironfoundry.org/) & [Site](http://www.ironfoundry.org/). For more information on Thor and to follow or get involved check out the [Thor Project Site](http://www.ironfoundry.org/thor) (Hosted with [Cloud Foundry](http://www.cloudfoundry.org) at [Tier 3](http://www.tier3.com)!).

All of this code is available in my [Github Project “Remembering” (https://github.com/Adron/Remembering)](https://github.com/Adron/Remembering). Feel free to fork it, share it, or send me corrections or pull requests.

[My CodeProject](http://www.codeproject.com/script/Articles/BlogFeedList.aspx?amid=471911)
