---
title: Put Stuff in Your Windows Azure Junk Trunk – Repository Base
date: 2011-02-07 05:15:34 -0800
last_modified_at: 2011-02-13 19:59:28 -0800
permalink: /2011/02/07/windows-azure-junk-trunk-part-1/
slug: windows-azure-junk-trunk-part-1
wp_id: 2204
original_url: https://compositecode.blog/2011/02/07/windows-azure-junk-trunk-part-1/
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
excerpt: 'Alright, so the title is rather stupid, but hey, it’s fun! 🙂 This project I setup to provide some basic functionality with Windows Azure Storage. I wanted to use each of the three mediums; Table, Blob, and Queue, and this example will cover each of these things. The application will upload and store images, provide a listing, some worker processing, and deletion of the images & associated metadata. This entry is part 1 of this series, with the following schedule for subsequent entries: Part 1: Today (this entry) Title aside, schedule laid out, description of the project completed, I’ll dive right in! Putting Stuff in Your Junk Trunk Create a new Windows Azure Project called PutJunkInIt.'
---

Alright, so the title is rather stupid, but hey, it’s fun!  🙂

This project I setup to provide some basic functionality with Windows Azure Storage.  I wanted to use each of the three mediums;  Table, Blob, and Queue, and this example will cover each of these things.  The application will upload and store images, provide a listing, some worker processing, and deletion of the images & associated metadata.  This entry is part 1 of this series, with the following schedule for subsequent entries:

- [Part 1:  Today (this entry)](#)
- [Part 2:  The Junk Trunk ASP.NET MVC 2 Web Application (Publishing on February 10th)](/2011/02/10/windows-azure-junk-trunk-part-2/)
- [Part 3:  Windows Azure Worker Role and Storage Queue (Publishing on February 14th)](/2011/02/14/windows-azure-junk-trunk-part-3/)

Title aside, schedule laid out, description of the project completed, I’ll dive right in!

**Putting Stuff in Your Junk Trunk**

Create a new Windows Azure Project called *PutJunkInIt*.  (Click any screenshot for the full size, and also note some of the text may be off – I had to recreate a number of these images)

[![Windows Azure PutJunkInIt](/images/adronhall.smugmug.com/Software/Software-Development/Windows-Azure-Table-Blob-Queue/06fig01/1177548441_Z28se-S.png "Windows Azure PutJunkInIt")](http://adronhall.smugmug.com/Software/Software-Development/Windows-Azure-Table-Blob-Queue/15711067_tbF6t#1177548441_Z28se-O-LB)

*Windows Azure PutJunkInIt*

Next select the ASP.NET MVC 2 Web Application and also a Worker Role and name the projects *JunkTrunk* and *JunkTrunk.WorkerRole*.

[![Choosing Windows Azure Projects](/images/adronhall.smugmug.com/Software/Software-Development/Windows-Azure-Table-Blob-Queue/06fig02/1177548445_oQeU3-S.png "Choosing Windows Azure Projects")](http://adronhall.smugmug.com/Software/Software-Development/Windows-Azure-Table-Blob-Queue/15711067_tbF6t#1177548445_oQeU3-O-LB)

*Choosing Windows Azure Projects*

In the next dialog choose to create the unit test project and click OK.

[![Create Unit Test Project](/images/adronhall.smugmug.com/Software/Software-Development/Windows-Azure-Table-Blob-Queue/06fig03/1177548443_8qD8n-S.png "Create Unit Test Project")](http://adronhall.smugmug.com/Software/Software-Development/Windows-Azure-Table-Blob-Queue/15711067_tbF6t#1177548443_8qD8n-O-LB)

*Create Unit Test Project*

After the project is created the following projects are setup within the *PutJunkInIt* Solution.  There should be a *JunkTrunk*, *JunkTrunk.Worker*, *JunkTrunk* Windows Azure Deployment Project, and a *JunkTrunk.Tests* Project.

[![Solution Explorer](/images/adronhall.smugmug.com/Software/Software-Development/Windows-Azure-Table-Blob-Queue/06fig04/1177548453_YSfub-S.png "Solution Explorer")](http://adronhall.smugmug.com/Software/Software-Development/Windows-Azure-Table-Blob-Queue/15711067_tbF6t#1177548453_YSfub-O-LB)

*Solution Explorer*

Next add a Windows Class Library Project and title it *JunkTrunk.Storage*.

[![Windows Class Library](/images/adronhall.smugmug.com/Software/Software-Development/Windows-Azure-Table-Blob-Queue/06fig05/1177548456_Xk3oU-S.png "Windows Class Library")](http://adronhall.smugmug.com/Software/Software-Development/Windows-Azure-Table-Blob-Queue/15711067_tbF6t#1177548456_Xk3oU-O-LB)

*Windows Class Library*

Add a reference to the Microsoft.WindowsAzure.ServiceRuntime and Microsoft.WindowsAzure.StorageClient assemblies to the *JunkTrunk.Storage* Project.  Rename the Class1.cs file and class to *JunkTrunkBase*.  Now open up the Class1.cs file in the *JunkTrunk.Storage* Project.  First add the following fields and constructor to the class.

```csharp
public const string QueueName = "metadataqueue";
public const string BlobContainerName = "photos";
public const string TableName = "MetaData";
static JunkTrunkBase()
{
    CloudStorageAccount.SetConfigurationSettingPublisher((configName, configSetter) =>
    {
        configSetter(RoleEnvironment.GetConfigurationSettingValue(configName));
        RoleEnvironment.Changed
            += (sender, arg) =>
                    {
                        if (!arg.Changes.OfType()
                                .Any(change => (change.ConfigurationSettingName == configName)))
                            return;
                        if (!configSetter(RoleEnvironment.GetConfigurationSettingValue(configName)))
                        {
                            RoleEnvironment.RequestRecycle();
                        }
                    };
    });
}
```

After that add the following blob container and reference methods.

```csharp
protected static CloudBlobContainer Blob
{
    get { return BlobClient.GetContainerReference(BlobContainerName); }
}
private static CloudBlobClient BlobClient
{
    get
    {
        return Account.CreateCloudBlobClient();
    }
}
```

Now add code for the table & queue client and reference methods.

```csharp
protected static CloudQueue Queue
{
    get { return QueueClient.GetQueueReference(QueueName); }
}
private static CloudQueueClient QueueClient
{
    get { return Account.CreateCloudQueueClient(); }
}
protected static CloudTableClient Table
{
    get { return Account.CreateCloudTableClient(); }
}
protected static CloudStorageAccount Account
{
    get
    {
        return
            CloudStorageAccount
            .FromConfigurationSetting("Microsoft.WindowsAzure.Plugins.Diagnostics.ConnectionString");
    }
}
```

This class now provides the basic underpinnings needed to retrieve the appropriate information from the configuration.  This base class can then provide that connection information to connect to the table, queue, or blob mediums.

Next step is to create some initialization code to get the containers created if they don’t exist in Windows Azure.  Add a new class file to the *PutJunkInIt* Project.

[![JunkTrunkSetup](/images/adronhall.smugmug.com/Software/Software-Development/Windows-Azure-Table-Blob-Queue/delete6/1177569329_NBohK-S.png "JunkTrunkSetup")](http://adronhall.smugmug.com/Software/Software-Development/Windows-Azure-Table-Blob-Queue/15711067_tbF6t#1177569329_NBohK-O-LB)

*JunkTrunkSetup*

```csharp
public class JunkTrunkSetup : JunkTrunkBase
{
    public static void CreateContainersQueuesTables()
    {
        Blob.CreateIfNotExist();
        Queue.CreateIfNotExist();
        Table.CreateTableIfNotExist(TableName);
    }
}
```

Next add the System.Data.Services.Client Assembly to the project.  After adding the assembly add two new classes and name them *BlobMeta.cs* and *Table.cs*. Add the following code to the *Table.cs* Class.

```csharp
public class Table
{
    public static string PartitionKey;
}
```

Next add another class file and name it  *BlobMetaContext.cs* and add the following code.

```csharp
public class BlobMetaContext : TableServiceContext
{
    public BlobMetaContext(string baseAddress, StorageCredentials credentials)
        : base(baseAddress, credentials)
    {
        IgnoreResourceNotFoundException = true;
    }
    public IQueryable Data
    {
        get { return CreateQuery(RepositoryBase.TableName); }
    }
    public void Add(BlobMeta data)
    {
        data.RowKey = data.RowKey.Replace("/", "_");
        BlobMeta original = (from e in Data
                                where e.RowKey == data.RowKey
                                    && e.PartitionKey == Table.PartitionKey
                                select e).FirstOrDefault();
        if (original != null)
        {
            Update(original, data);
        }
        else
        {
            AddObject(RepositoryBase.TableName, data);
        }
        SaveChanges();
    }
    public void Update(BlobMeta original, BlobMeta data)
    {
        original.Date = data.Date;
        original.ResourceUri = data.ResourceUri;
        UpdateObject(original);
        SaveChanges();
    }
}
```

Now add the following code to the *BlobMeta* Class.

```csharp
public class BlobMeta : TableServiceEntity
{
    public BlobMeta()
    {
        PartitionKey = Table.PartitionKey;
    }
    public DateTime Date { get; set; }
    public string ResourceUri { get; set; }
}
```

At this point, everything should build. Give it a go to be sure nothing got keyed in wrong (or copied in wrong). Once assured the build is still solid, add the *Blob.cs* Class to the project.

```csharp
public class Blob : JunkTrunkBase
{
    public static string PutBlob(Stream stream, string fileName)
    {
        var blobRef = Blob.GetBlobReference(fileName);
        blobRef.UploadFromStream(stream);
        return blobRef.Uri.ToString();
    }
    public static Stream GetBlob(string blobAddress)
    {
        var stream = new MemoryStream();
        Blob.GetBlobReference(blobAddress)
            .DownloadToStream(stream);
        return stream;
    }
    public static Dictionary<string, string> GetBlobList()
    {
        var blobs = Blob.ListBlobs();
        var blobDictionary =
            blobs.ToDictionary(
                listBlobItem => listBlobItem.Uri.ToString(),
                listBlobItem => listBlobItem.Uri.ToString());
        return blobDictionary;
    }
    public static void DeleteBlob(string blobAddress)
    {
        Blob.GetBlobReference(blobAddress).DeleteIfExists();
    }
}
```

After that finalize the Table Class with the following changes and additions.

```csharp
public class Table : RepositoryBase
{
    public const string PartitionKey = "BlobMeta";
    public static void Add(BlobMeta data)
    {
        Context.Add(data);
    }
    public static BlobMeta GetMetaData(Guid key)
    {
        return (from e in Context.Data
                where e.RowKey == key.ToString() &&
                e.PartitionKey == PartitionKey
                select e).SingleOrDefault();
    }
    public static void DeleteMetaDataAndBlob(Guid key)
    {
        var ctxt = new BlobMetaContext(
            Account.TableEndpoint.AbsoluteUri,
            Account.Credentials);
        var entity = (from e in ctxt.Data
                        where e.RowKey == key.ToString() &&
                        e.PartitionKey == PartitionKey
                        select e).SingleOrDefault();
        ctxt.DeleteObject(entity);
        Repository.Blob.DeleteBlob(entity.ResourceUri);
        ctxt.SaveChanges();
    }
    public static List<BlobMeta> GetAll()
    {
        return (from e in Context.Data
                select e).ToList();
    }
    public static BlobMetaContext Context
    {
        get
        {
            return new BlobMetaContext(
                Account.TableEndpoint.AbsoluteUri,
                Account.Credentials);
        }
    }
}
```

The final file to add is the Queue.cs Class File. Add that and then add the following code to the class.

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

The now gives us a fully functional class that utilizes the Windows Azure SDK. In Part 2 I’ll start building on top of that using the ASP.NET MVC 2 Web Project. Part 2 will be published tomorrow, so stay tuned.
