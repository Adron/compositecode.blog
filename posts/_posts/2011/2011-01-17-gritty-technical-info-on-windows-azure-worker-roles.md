---
title: Gritty Technical Info on Windows Azure Worker Roles
date: 2011-01-17 05:00:41 -0800
last_modified_at: 2011-01-17 02:53:56 -0800
permalink: /2011/01/17/gritty-technical-info-on-windows-azure-worker-roles/
slug: gritty-technical-info-on-windows-azure-worker-roles
wp_id: 2102
original_url: https://compositecode.blog/2011/01/17/gritty-technical-info-on-windows-azure-worker-roles/
categories:
- Azure
- How-to
tags:
- cloud
- cloud computing
- microsoft
- web services
- windows azure
- worker role
excerpt: In the last blog entry, “Gritty Technical Info on Windows Azure Web Roles”, I covered the creation and startup of a web role within the Windows Azure Development Fabric and observing the web role with the Windows Azure Compute Emulator. In this blog entry I’ll cover the worker role.
---

In the last blog entry, “[Gritty Technical Info on Windows Azure Web Roles](2011/01/14/gritty-technical-info-on-windows-azure-web-roles/)“, I covered the creation and startup of a web role within the Windows Azure Development Fabric and observing the web role with the Windows Azure Compute Emulator.  In this blog entry I’ll cover the worker role.

Open the Windows Azure Web Role Sample Solution.  Right click on the Windows Azure and select New Worker Role Project.

[![New Worker Role Project...](/images/adronhall.smugmug.com/Software/Software-Development/windows-azure-roles/04fig11/1159318583_R6LAr-O.png "New Worker Role Project...")](http://adronhall.smugmug.com/Software/Software-Development/windows-azure-roles/15431091_6D8HE#1159318583_R6LAr-A-LB)

*New Worker Role Project...*

Once the worker role project SampleWorkerRole is added the solution explorer will display the project just like the web role, albeit fewer files.

[![Solution Explorer](/images/adronhall.smugmug.com/Software/Software-Development/windows-azure-roles/04fig12/1159316914_ydQCo-O.png "Solution Explorer")](http://adronhall.smugmug.com/Software/Software-Development/windows-azure-roles/15431091_6D8HE#1159316914_ydQCo-O-LB)

*Solution Explorer*

Next right click on the SampleWorkerRole instance in the Windows Azure Web Role Sample and select properties.  Now set the instance count to 2 and the VM size to extra large.

[![SampleWorkerRole Properties](/images/adronhall.smugmug.com/Software/Software-Development/windows-azure-roles/Windows-Azure-Worker-Role-03/1155222909_Sr9zJ-S.png "SampleWorkerRole Properties")](http://adronhall.smugmug.com/Software/Software-Development/windows-azure-roles/15431091_6D8HE#1155222909_Sr9zJ-O-LB)

*SampleWorkerRole Properties*

Click on F5 to run the application.  Now when the application executes the 6 web role instances will start and the 2 worker role instances will start.

[![Windows Azure Compute Emulator](/images/adronhall.smugmug.com/Software/Software-Development/windows-azure-roles/04fig14/1159316934_KYXbG-S.png "Windows Azure Compute Emulator")](http://adronhall.smugmug.com/Software/Software-Development/windows-azure-roles/15431091_6D8HE#1159316934_KYXbG-O-LB)

*Windows Azure Compute Emulator*

Examine the first worker role instance.

[![SampleWorkerRole Instance Status](/images/adronhall.smugmug.com/Software/Software-Development/windows-azure-roles/04fig15/1159316937_ked2o-S.png "SampleWorkerRole Instance Status")](http://adronhall.smugmug.com/Software/Software-Development/windows-azure-roles/15431091_6D8HE#1159316937_ked2o-O-LB)

*SampleWorkerRole Instance Status*

The worker role instance displays a number of new diagnostic messages in a similar way to the web role.  The first half of the trace diagnostics are configuration and instance messages.  The second half of the trace diagnostics are status messages that are printed from the worker role running.

Open up the code in the WorkerRole.cs file in the SampleWorkerRole Project.  As a comparison open the WebRole.cs file in the SampleWebRole Project.

```csharp
using System.Diagnostics;
using System.Net;
using System.Threading;
using Microsoft.WindowsAzure.ServiceRuntime;

namespace SampleWorkerRole
{
    public class WorkerRole : RoleEntryPoint
    {
        public override void Run()
        {
            Trace.WriteLine("SampleWorkerRole entry point called", "Information");

            while (true)
            {
                Thread.Sleep(10000);
                Trace.WriteLine("Working", "Information");
            }
        }

        public override bool OnStart()
        {
            ServicePointManager.DefaultConnectionLimit = 12;
            return base.OnStart();
        }
    }
}
```

In the WorkerRole.cs file the code inherites from the RoleEntryPoint for the WorkerRole. In the WorkerRole Class the Run and OnStart Methods are overridden to provide some basic trace information and set the default connection limit.

The Run method has a basic while loop that updates every 10000 milliseconds, which displays on the Windows Azure Compute Emulator as “Information: Working”.

```csharp
using Microsoft.WindowsAzure.ServiceRuntime;

namespace SampleWebRole
{
    public class WebRole : RoleEntryPoint
    {
        public override bool OnStart()
        {
            return base.OnStart();
        }
    }
}
```

In the code for the WebRole.cs file there is very little actually going on.  Take a closer look at the OnStart method override.  Technically this code doesn’t even need to be in the generated file and can be deleted, but provides a good starting point to add any other code needed in the start of the web role.

Next I’ll add some code in the worker role to provide a telnet prompt that responds with worker role information.  To work through this exercise completely download a telnet client like Putty (<http://www.chiark.greenend.org.uk/~sgtatham/putty/>).

If Visual Studio 2010 is no longer open, launch it and open the Windows Azure Web Role Sample Solution.  Right click on the SampleWorkRole Role in the Windows Azure Web Role Sample Project.  Click on the Endpoints tab of the properties window and click on Add Endpoint and call it TelnetServiceEndpoint.

[![Endpoint](/images/adronhall.smugmug.com/Software/Software-Development/windows-azure-roles/04fig16/1159316936_HqYHe-S.png "Endpoint")](http://adronhall.smugmug.com/Software/Software-Development/windows-azure-roles/15431091_6D8HE#1159316936_HqYHe-O-LB)

*Endpoint*

Add a private member and create a run method with the following code.

```csharp
private readonly AutoResetEvent _connectionWait = new AutoResetEvent(false);

public override void Run()
{
    Trace.WriteLine("Starting Telnet Service...", "Information");

    TcpListener listener;
    try
    {
        listener = new TcpListener(
            RoleEnvironment.CurrentRoleInstance.InstanceEndpoints["TelnetServiceEndpoint"].IPEndpoint) { ExclusiveAddressUse = false };
        listener.Start();

        Trace.WriteLine("Started Telnet Service.", "Information");
    }
    catch (SocketException se)
    {
        Trace.Write("Telnet Service could not start.", "Error");
        return;
    }

    while (true)
    {
        listener.BeginAcceptTcpClient(HandleAsyncConnection, listener);
        _connectionWait.WaitOne();
    }
}
```

After adding this code, add the following code for the role information to write to a stream.

```csharp
private static void WriteRoleInformation(Guid clientId, StreamWriter writer)
{
    writer.WriteLine("--- Current Client ID, Date & Time ----");
    writer.WriteLine("Current date: " + DateTime.Now.ToLongDateString() + " " + DateTime.Now.ToLongTimeString());
    writer.WriteLine("Connection ID: " + clientId);
    writer.WriteLine();

    writer.WriteLine("--- Current Role Instance Information ----");
    writer.WriteLine("Role ID: " + RoleEnvironment.CurrentRoleInstance.Id);
    writer.WriteLine("Role Count: " + RoleEnvironment.Roles.Count);
    writer.WriteLine("Deployment ID: " + RoleEnvironment.DeploymentId);
    writer.WriteLine();

    writer.WriteLine("--- Instance Endpoints ----");

    foreach (KeyValuePair<string, RoleInstanceEndpoint> instanceEndpoint in RoleEnvironment.CurrentRoleInstance.InstanceEndpoints)
    {
        writer.WriteLine("Instance Endpoint Key: " + instanceEndpoint.Key);

        RoleInstanceEndpoint roleInstanceEndpoint = instanceEndpoint.Value;

        writer.WriteLine("Instance Endpoint IP: " + roleInstanceEndpoint.IPEndpoint);
        writer.WriteLine("Instance Endpoint Protocol: " + roleInstanceEndpoint.Protocol);
        writer.WriteLine("Instance Endpoint Type: " + roleInstanceEndpoint);
        writer.WriteLine();
    }
}
```

Now add a handle method for the asynchronous call.

```csharp
private void HandleAsyncConnection(IAsyncResult result)
{
    var listener = (TcpListener)result.AsyncState;
    var client = listener.EndAcceptTcpClient(result);
    _connectionWait.Set();

    var clientId = Guid.NewGuid();
    Trace.WriteLine("Connection ID: " + clientId, "Information");

    var netStream = client.GetStream();
    var reader = new StreamReader(netStream);
    var writer = new StreamWriter(netStream);
    writer.AutoFlush = true;

    var input = string.Empty;
    while (input != "3")
    {
        writer.WriteLine(" 1) Display Worker Role Information");
        writer.WriteLine(" 2) Recycle");
        writer.WriteLine(" 3) Quit");
        writer.Write("Enter your choice: ");

        input = reader.ReadLine();
        writer.WriteLine();

        switch (input)
        {
            case "1":
                WriteRoleInformation(clientId, writer);
                break;
            case "2":
                RoleEnvironment.RequestRecycle();
                break;
        }

        writer.WriteLine();
    }

    client.Close();
}
```

Finally override the OnStart() method and setup the RoleEnvironmentChanging Event.

```csharp
public override bool OnStart()
{
    ServicePointManager.DefaultConnectionLimit = 12;

    DiagnosticMonitor.Start("DiagnosticsConnectionString");

    RoleEnvironment.Changing += RoleEnvironmentChanging;

    return base.OnStart();
}

private static void RoleEnvironmentChanging(object sender, RoleEnvironmentChangingEventArgs e)
{
    if (e.Changes.Any(change => change is RoleEnvironmentConfigurationSettingChange))
    {
        e.Cancel = true;
    }
}
```

Now run the role by hitting F5. When the application runs open up the Windows Azure Compute Emulator to check for the end point and verify the instances of the role are running.

[![Endpoint displayed in the Windows Azure Compute Emulator](/images/adronhall.smugmug.com/Software/Software-Development/windows-azure-roles/04fig17/1159316941_twoZt-S.png "Endpoint displayed in the Windows Azure Compute Emulator")](http://adronhall.smugmug.com/Software/Software-Development/windows-azure-roles/15431091_6D8HE#1159316941_twoZt-O-LB)

*Endpoint displayed in the Windows Azure Compute Emulator*

The Service Name should be Windows\_Azure\_Web\_Role, with an Interface Type of SampleWorkerRole running on the tcp://\*:1234 URL and the IP is 127.0.0.1P:1234.

[![SampleWorkerRole](/images/adronhall.smugmug.com/Software/Software-Development/windows-azure-roles/04fig18/1159316956_JbLXW-S.png "SampleWorkerRole")](http://adronhall.smugmug.com/Software/Software-Development/windows-azure-roles/15431091_6D8HE#1159316956_JbLXW-O-LB)

*SampleWorkerRole*

Click on one of the instances, which should be green, and assure that each has started up appropriately.

[![PuTTY](/images/adronhall.smugmug.com/Software/Software-Development/windows-azure-roles/04fig19/1159316953_GEnNN-S.png "PuTTY")](http://adronhall.smugmug.com/Software/Software-Development/windows-azure-roles/15431091_6D8HE#1159316953_GEnNN-O-LB)

*PuTTY*

Startup a telnet application, such as Putty and enter the information in as shown in screenshot above.

[![Telnet](/images/adronhall.smugmug.com/Software/Software-Development/windows-azure-roles/04fig20/1159316958_hPjKt-S.png "Telnet")](http://adronhall.smugmug.com/Software/Software-Development/windows-azure-roles/15431091_6D8HE#1159316958_hPjKt-O-LB)

*Telnet*

Start the telnet prompt connecting to the Windows Azure Worker Role. The prompt with the three choices will display. Click to recycle and then display worker role information a few times, just to make sure all the information is available and the worker role telnet application service is working. Select 3 to exit out and the prompt should close while the role continues to run on the development fabric.
