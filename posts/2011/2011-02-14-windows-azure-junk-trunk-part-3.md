---
title: Put Stuff in Your Windows Azure Junk Trunk – Windows Azure Worker Role and Storage Queue
date: 2011-02-14 04:55:41 -0800
last_modified_at: 2011-02-13 19:56:33 -0800
permalink: /2011/02/14/windows-azure-junk-trunk-part-3/
slug: windows-azure-junk-trunk-part-3
wp_id: 2266
original_url: https://compositecode.blog/2011/02/14/windows-azure-junk-trunk-part-3/
categories:
- Azure
- How-to
tags:
- azure
- BLOB
- cloud
- cloud computing
- cloud storage
- microsoft
- web role
- windows azure
- windows azure blob
- windows azure queue
- windows azure table
- worker role
excerpt: Click on Part 1 and Part 2 of this series to review the previous examples and code. First and foremost have the existing code base created in the other two examples opened and ready in Visual Studio 2010. Next, I’ll just start rolling ASAP. In the JunkTrunk.Storage Project add the following class file and code …
---

Click on [Part 1](/2011/02/07/windows-azure-junk-trunk-part-1/) and [Part 2](/2011/02/10/windows-azure-junk-trunk-part-2/) of this series to review the previous examples and code.  First and foremost have the existing code base created in the other two examples opened and ready in Visual Studio 2010.  Next, I’ll just start rolling ASAP.

In the *JunkTrunk.Storage* Project add the following class file and code to the project. This will get us going for anything else we needed to do for the application from the queue perspective.

```csharp
public class Queue : JunkTrunkBase
{
    public static void Add(CloudQueueMessage msg)
    {
        Queue.AddMessage(msg);
    }

    public static CloudQueueMessage GetNextMessage()
    {
        return Queue.PeekMessage() != null ? Queue.GetMessage() : null;
    }

    public static List<CloudQueueMessage> GetAllMessages()
    {
        var count = Queue.RetrieveApproximateMessageCount();
        return Queue.GetMessages(count).ToList();
    }

    public static void DeleteMessage(CloudQueueMessage msg)
    {
        Queue.DeleteMessage(msg);
    }
}
```

Once that is done open up the FileBlobManager.cs file in the Models directory of the JunkTrunk ASP.NET MVC Web Application. In the PutFile() Method add this line of code toward the very end of that method. The method, with the added line of code should look like this.

```csharp
public void PutFile(BlobModel blobModel)
{
    var blobFileName = string.Format("{0}-{1}", DateTime.Now.ToString("yyyyMMdd"), blobModel.ResourceLocation);
    var blobUri = Blob.PutBlob(blobModel.BlobFile, blobFileName);

    Table.Add(
        new BlobMeta
            {
                Date = DateTime.Now,
                ResourceUri = blobUri,
                RowKey = Guid.NewGuid().ToString()
            });

    Queue.Add(new CloudQueueMessage(blobUri + "$" + blobFileName));
}
```

Now that we have something adding to the queue, we want to process this queue message. Open up the *JunkTrunk.WorkerRole* and make sure you have the following references in the project.
[![Windows Azure References](/images/adronhall.smugmug.com/Software/Software-Development/Windows-Azure-Table-Blob-Queue/references/1186883771_prHsN-O.png "Windows Azure References")](http://adronhall.smugmug.com/Software/Software-Development/Windows-Azure-Table-Blob-Queue/15711067_tbF6t#1186883771_prHsN-O-LB)

*Windows Azure References*

Next create a new class file called PhotoProcessing.cs. First add a method to the class titled ThumbnailCallback with the following code.

```csharp
public static bool ThumbnailCallback()
{
    return false;
}
```

Next add another method with a blobUri string and filename string as parameters. Then add the following code block to it.

```csharp
private static void AddThumbnail(string blobUri, string fileName)
{
    try
    {
        var stream = Repository.Blob.GetBlob(blobUri);

        if (blobUri.EndsWith(".jpg"))
        {
            var image = Image.FromStream(stream);
            var myCallback = new Image.GetThumbnailImageAbort(ThumbnailCallback);
            var thumbnailImage = image.GetThumbnailImage(42, 32, myCallback, IntPtr.Zero);
            thumbnailImage.Save(stream, ImageFormat.Jpeg);
            Repository.Blob.PutBlob(stream, "thumbnail-" + fileName);
        }
        else
        {
            Repository.Blob.PutBlob(stream, fileName);
        }
    }
    catch (Exception ex)
    {
        Trace.WriteLine("Error", ex.ToString());
    }
}
```

Last method to add to the class is the Run() method.

```csharp
public static void Run()
{
    var queueMessage = Repository.Queue.GetNextMessage();

    while (queueMessage != null)
    {
        var message = queueMessage.AsString.Split('$');
        if (message.Length == 2)
        {
            AddThumbnail(message[0], message[1]);
        }

        Repository.Queue.DeleteMessage(queueMessage);
        queueMessage = Repository.Queue.GetNextMessage();
    }
}
```

Now open up the WorkerRole.cs File and add the following code to the existing methods and add the additional even method below.

```csharp
public override void Run()
{
    Trace.WriteLine("Junk Trunk Worker entry point called", "Information");

    while (true)
    {
        PhotoProcessing.Run();

        Thread.Sleep(60000);
        Trace.WriteLine("Working", "Junk Trunk Worker Role is active and running.");
    }
}

public override bool OnStart()
{
    ServicePointManager.DefaultConnectionLimit = 12;
    DiagnosticMonitor.Start("Microsoft.WindowsAzure.Plugins.Diagnostics.ConnectionString");
    RoleEnvironment.Changing += RoleEnvironmentChanging;

    CloudStorageAccount.SetConfigurationSettingPublisher((configName, configSetter) =>
    {
        configSetter(RoleEnvironment.GetConfigurationSettingValue(configName));
        RoleEnvironment.Changed += (sender, arg) =>
        {
            if (arg.Changes.OfType<RoleEnvironmentConfigurationSettingChange>()
                .Any((change) => (change.ConfigurationSettingName == configName)))
            {
                if (!configSetter(RoleEnvironment.GetConfigurationSettingValue(configName)))
                {
                    RoleEnvironment.RequestRecycle();
                }
            }
        };
    });

    Storage.JunkTrunkSetup.CreateContainersQueuesTables();

    return base.OnStart();
}

private static void RoleEnvironmentChanging(object sender, RoleEnvironmentChangingEventArgs e)
{
    if (!e.Changes.Any(change => change is RoleEnvironmentConfigurationSettingChange)) return;

    Trace.WriteLine("Working", "Environment Change: " + e.Changes.ToList());
    e.Cancel = true;
}
```

At this point everything needed to kick off photo processing using Windows Azure Storage Queue as the tracking mechanism is ready. I’ll be following up these blog entries with some additional entries regarding rafactoring and streamlining what we have going on. I might even go all out and add some more functionality or some such craziness! So hope that was helpful and keep reading. I’ll have more bits of rambling and other trouble coming down the blob pipeline soon! Cheers!
