---
title: Implementing Enterprise Library Architecture Part 1
date: 2008-12-16 01:04:00 -0800
last_modified_at: 2010-09-03 14:41:47 -0700
permalink: /2008/12/16/implementing-enterprise-library-architecture-part-1/
slug: implementing-enterprise-library-architecture-part-1
wp_id: 572
original_url: https://compositecode.blog/2008/12/16/implementing-enterprise-library-architecture-part-1/
categories:
- Architecture
- How-to
tags: []
excerpt: Policy Injection (AOP Cross Cutting), Logging, Exception Handling, Security/Authentication, and more… Logging Exception Handling Authentication Authorization Audit Services (Web Services) Implementation Client Tier with either Web Forms or MVC Imagine all of this functionality rolled into a clear layer with well defined separation of concerns. Ok, stop imagining it and get it done, here’s how. …
---

### Policy Injection (AOP Cross Cutting), Logging, Exception Handling, Security/Authentication, and more…

- Logging
- Exception Handling
- Authentication
- Authorization
- Audit
- Services (Web Services) Implementation
- Client Tier with either Web Forms or MVC

Imagine all of this functionality rolled into a clear layer with well defined *separation of concerns*.  Ok, stop imagining it and get it done, here’s how.

First off, get a clean VS.NET 2008 Installation and make sure you have Enterprise Library 4.1 Installed and ready to go.  Now, here’s the step by step.

First setup two projects.  A more broken out solution is possible, but that moves past the realm of KISS and into the YAGNI realm.  The first project let’s name *PipServices.* We’ll make in a WCF Services Project like shown below.

[![](/images/adronhall.smugmug.com/photos/437417460_r3CFY-M.png)](http://adronhall.smugmug.com/gallery/6842104_frBDt#437417460_r3CFY)

The next step is to add the client applications.  Add a ASP.NET Web Forms Application and a ASP.NET MVC Application.

[![](/images/adronhall.smugmug.com/photos/437417441_uR2CE-M.png)](http://adronhall.smugmug.com/gallery/6842104_frBDt#437417441_uR2CE)

***(**[**Click any image for larger representations or click here for the entire gallery of images.**](http://adronhall.smugmug.com/gallery/6842104_frBDt#437417441_uR2CE)**)***

[![](/images/adronhall.smugmug.com/photos/437418452_6PCmH-M.png)](http://adronhall.smugmug.com/gallery/6842104_frBDt#437418452_6PCmH)

For the ASP.NET MVC Application go ahead and add the Unit Test Project.

[![](/images/adronhall.smugmug.com/photos/437419663_9jZQg-M.png)](http://adronhall.smugmug.com/gallery/6842104_frBDt#437419663_9jZQg)

After that the solution should look like this.

[![](/images/adronhall.smugmug.com/photos/437419700_GEodG-X2.png)](http://adronhall.smugmug.com/gallery/6842104_frBDt#437419700_GEodG)

After the solution is together I added to solution folders for client and services and put the respective projects in those folders.  It is just a little easier to eye ball which solution is which that way.

[![](/images/adronhall.smugmug.com/photos/437421501_hfHfh-L.png)](http://adronhall.smugmug.com/gallery/6842104_frBDt#437421501_hfHfh)

Next bring up the EntLib Configuration Editor by right clicking on the web.config file of the WCF Services Project.

[![](/images/adronhall.smugmug.com/photos/437421594_SZyL3-X2.png)](http://adronhall.smugmug.com/gallery/6842104_frBDt#437421594_SZyL3)

Let’s setup a quick User Database and Authorization Setup.  First run the setup file for the database.  The executable is named aspnet\_regsql.exe and is located in this directory [C:\WINDOWS\Microsoft.NET\Framework\v2.0.50727](\WINDOWS\Microsoft.NET\Framework\v2.0.50727).  For a quick review check out my entry “[ASP.NET 2.0 Users, Roles, and Membership APIs](/blogs/technology__software_development/post/2007/02/03/ASPNET-20-Users-Roles-and-Membership-APIs.aspx)“.  Step through the wizard that comes up when you run the executable and create a database named PipDatabase.

[![](/images/adronhall.smugmug.com/photos/437421609_Y34mF-L.png)](http://adronhall.smugmug.com/gallery/6842104_frBDt#437421609_Y34mF)

Once the database is created head back over to the EntLib Configuration Editor.  The editor screen should be displayed and have a configuration section for *Connection Strings* within the *Data Access Application Block Section*.  In the Connection Strings section there should be an item called *LocalSqlServer*.  Change that to *PopSqlServer.* After renaming the connection select it and then hit F4 to bring up the properties for that item.  The properties window should look like the image below.

[![](/images/adronhall.smugmug.com/photos/437421617_Q6D6q-L.png)](http://adronhall.smugmug.com/gallery/6842104_frBDt#437421617_Q6D6q)

Change the connection string from the default of “*data source=.\SQLEXPRESS;Integrated Security=SSPI;AttachDBFilename=|DataDirectory|aspnetdb.mdf;User Instance=true*” to the connection string you setup for your *PipDatabase*.  If need be there is an ellipsis you can click on to get a *Connection Properties* window.  Once you’ve changed the connection string do a build of the entire solution.  If everything checks out move on to the next steps.  Otherwise, if you get an error go about fixing that.  At this point the configuration file will look like below.  The display for the Enterprise Configuration Editor will look like the image below.

[![](/images/adronhall.smugmug.com/photos/437421625_3Bgfx-L.png)](http://adronhall.smugmug.com/gallery/6842104_frBDt#437421625_3Bgfx)

It’s easy to check the additions and subtractions that aren’t shown easily via the configuration tool.

Next select the root of the specific configuration file.  This would be the tree node that has the file path listed.  Something akin to “*c:\users\username\Document\Visual Studio 2008\Projects\PolicyInjectFramework\PipServices\Web.config*“.  On the context menu click on the *Exception Handling Application Block* item as shown.

[![](/images/adronhall.smugmug.com/photos/437421577_RLZ9M-L.png)](http://adronhall.smugmug.com/gallery/6842104_frBDt#437421577_RLZ9M)

One thing I always do after adding anything via the Enterprise Configuration Tool is to right click and select *Validate* at the root node level.  It is much easier to resolve any issues as soon as you run into them versus after doing a bunch of configuration and then finding something is out of whack.

Next add three additional *application block configuration sections*; *Logging, Policy Injection, and Security*.

[![](/images/adronhall.smugmug.com/photos/437424765_ajzU7-L.png)](http://adronhall.smugmug.com/gallery/6842104_frBDt#437424765_ajzU7)

[![](/images/adronhall.smugmug.com/photos/437424770_ZUnCK-L.png)](http://adronhall.smugmug.com/gallery/6842104_frBDt#437424770_ZUnCK)

[![](/images/adronhall.smugmug.com/photos/437424784_xMo3P-L.png)](http://adronhall.smugmug.com/gallery/6842104_frBDt#437424784_xMo3P)

After adding all of these sections the configuration file in the editor will look like this.

[![](/images/adronhall.smugmug.com/photos/437424789_oifpC-X2.png)](http://adronhall.smugmug.com/gallery/6842104_frBDt#437424789_oifpC)

After adding all these sections we’ll jump right into setting up some test harness application pieces to prove functionality.  First add a *Test Project* called *PipServices.Tests* to create some tests first.

Add a class file called *TestPipServices.cs* and add the following tests.

```
   1:
 using Microsoft.VisualStudio.TestTools.UnitTesting;
   2:
   3:  namespace PipServices.Tests
   4:  {
   5:      [TestClass]
   6:      public class TestPipServices
   7:      {
   8:          [TestMethod]
   9:          public void TestServicesObjectInstantiation()
  10:          {
  11:              var services = new PipServices();
  12:              Assert.IsNotNull(services);
  13:          }
  14:
  15:          [TestMethod]
  16:          public void TestDoWorkTrue()
  17:          {
  18:              var services = new PipServices();
  19:              Assert.IsTrue(services.DoWork(false));
  20:          }
  21:          [TestMethod]
  22:          public void TestDoWorkFalse()
  23:          {
  24:              var services = new PipServices();
  25:              Assert.IsFalse(services.DoWork(true));
  26:          }
  27:      }
  28:  }
```

If you realize, all that we are doing here is testing the mere classes and its methods.  We aren’t testing the actual service itself that will be hosted via WCF.  We’ll get to testing the actual services later.  Since testing the service is more of a configuration or integration test than it is a unit test it is best to leave those to after the configuration or integration is known.  At this point of development one knows what the classes will do, and what they would need but would not particularly know the exact configuration or integration of the services.  So no real point in creating integration tests yet.

Now in the WCF Service Project add a WCF Service called *PipServices* ( I always delete the service that the project has in place per the template ).  After you add that then enter the following code to replace the interface.

```
   1:  using System;
   2:  using System.Collections.Generic;
   3:  using System.Runtime.Serialization;
   4:  using System.ServiceModel;
   5:  using Microsoft.Practices.EnterpriseLibrary.PolicyInjection.CallHandlers;
   6:
   7:  namespace PipServices
   8:  {
   9:      [ServiceContract]
  10:      public interface IPipServices
  11:      {
  12:          [OperationContract]
  13:          [LogCallHandler]
  14:          bool DoWork(bool passBoolean);
  15:
  16:          [OperationContract]
  17:          [LogCallHandler]
  18:          List<AnObject> GetSomeAnObjects(AnObject anObject);
  19:      }
  20:
  21:      [DataContract]
  22:      public class AnObject
  23:      {
  24:          [DataMember]
  25:          public string SomeString { get; set; }
  26:
  27:          [DataMember]
  28:          public int SomeNumber { get; set; }
  29:
  30:          [DataMember]
  31:          public Guid SomeGuid { get; set; }
  32:
  33:          [DataMember]
  34:          public DateTime SomeDateTime { get; set; }
  35:      }
  36:  }
```

.csharpcode, .csharpcode pre
{
font-size: small;
color: black;
font-family: consolas, “Courier New”, courier, monospace;
background-color: #ffffff;
/\*white-space: pre;\*/
}
.csharpcode pre { margin: 0em; }
.csharpcode .rem { color: #008000; }
.csharpcode .kwrd { color: #0000ff; }
.csharpcode .str { color: #006080; }
.csharpcode .op { color: #0000c0; }
.csharpcode .preproc { color: #cc6633; }
.csharpcode .asp { background-color: #ffff00; }
.csharpcode .html { color: #800000; }
.csharpcode .attr { color: #ff0000; }
.csharpcode .alt
{
background-color: #f4f4f4;
width: 100%;
margin: 0em;
}
.csharpcode .lnum { color: #606060; }

After entering the interface add the proper implementations below for the actual service class.

```
   1:  using System;
   2:  using System.Collections.Generic;
   3:
   4:  namespace PipServices
   5:  {
   6:      public class PipServices : IPipServices
   7:      {
   8:          #region IPipServices Members
   9:
  10:          public bool DoWork(bool passBoolean)
  11:          {
  12:              return passBoolean == false;
  13:          }
  14:
  15:          public List<AnObject> GetSomeAnObjects(AnObject anObject)
  16:          {
  17:              throw new NotImplementedException();
  18:          }
  19:
  20:          #endregion
  21:      }
  22:  }
```

.csharpcode, .csharpcode pre
{
font-size: small;
color: black;
font-family: consolas, “Courier New”, courier, monospace;
background-color: #ffffff;
/\*white-space: pre;\*/
}
.csharpcode pre { margin: 0em; }
.csharpcode .rem { color: #008000; }
.csharpcode .kwrd { color: #0000ff; }
.csharpcode .str { color: #006080; }
.csharpcode .op { color: #0000c0; }
.csharpcode .preproc { color: #cc6633; }
.csharpcode .asp { background-color: #ffff00; }
.csharpcode .html { color: #800000; }
.csharpcode .attr { color: #ff0000; }
.csharpcode .alt
{
background-color: #f4f4f4;
width: 100%;
margin: 0em;
}
.csharpcode .lnum { color: #606060; }

Once you’ve added that then build the solution again to make sure everything is properly placed and builds successfully.  Now open the Enterprise Library Configuration Tool again.  Right click on the *Policy Injection Application Block* section and right click on the *Policies* Node below that.  Select *New* and then *Policy*.  You’ll see a policy added directly below the *Policies* Node.  Add one more and then name one *Exception Handling* and the other *Log Handling*.

The Policies Node should now look like this.

[![](/images/adronhall.smugmug.com/photos/437424804_KkHc5-L.png)](http://adronhall.smugmug.com/gallery/6842104_frBDt#437424804_KkHc5)

Now right click on the *Matching Rules* Node under the *Exception Handling* Policies.  Right click on the *Matching Rules* Node and select new and then *Member Name Matching Rule*.  Right click again and add a *Type Matching Rule*.  Now do the same thing to add to the *Handlers* Node a *Performance Counters Handler* and an *Exception Handling Handler*.

Once complete Add a *Namespace Matching Rule* under the *Matching Rules* of the *Log Handling* and a *Logging Handler* under the *Handlers* of the *Log Handling* Node.  Once complete do a build on the project and you’ll have a tree structure like this under the Policy Injection Application Block.

[![](/images/adronhall.smugmug.com/photos/437424757_YKUPy-XL.png)](http://adronhall.smugmug.com/gallery/6842104_frBDt#437424757_YKUPy)

Select the first node that displays red.  Hit F4 to bring up the properties window.  On the properties window click on the *Matches* Property ellipsis (In the value area you’ll see *(Collection)*).

[![](/images/adronhall.smugmug.com/photos/437428973_VrmZu-L.png)](http://adronhall.smugmug.com/gallery/6842104_frBDt#437428973_VrmZu)

When you click on the ellipsis a dialog will appear for adding match list items.  Click Add once and you’ll see an item appear.  Enter *TestException* in the property *Value*.

[![](/images/adronhall.smugmug.com/photos/437428978_hQrwt-S.png)](http://adronhall.smugmug.com/gallery/6842104_frBDt#437428978_hQrwt)

Now select the *Type Matching Rule* and get the properties window showing again (F4).  Go through the same steps as with adding the *TestException* to add a *TestTypeMatcher* to the *Value* property.

Now skip down and go to the last remaining configuration error and add to *Namespace Matching Rule* the namespace value *PipServices*.  After this do another build and you should only have a single remaining error displayed for the *Exception Handling Handler*.

For the *Exception Handling Handler* we’ll have to add a policy to the *Exception Handling Application Block* Node.  Right click on the *Exception Handling Application Block* Node and select *New* and then *Exception Policy*.  Now go down to the *Exception Handling Handler* under the *Handlers* under the *Exception Handling* node of the *Policies* of the *Policy Injection Application Block* node.  Get the properties window up for the *Exception Handling Handler* and for the policy property select the newly created *Exception Policy*.  Now do a project build and all should be good.

At this time it is good to actually run (F5) the services project so that the *Web.config* file will be modified for debugging.  This is something that always happens as the default configuration for a WCF web services project is not setup for debugging.  Along with adding the debugging config file settings we can also check to be sure the service is available.

### Integrating the Logging Application Block with WCF Applications

Now there is a slight issue with the WCF Services, Logging, and the PIAB.  Check out “[Integrating the Logging Application Block with WCF Applications](http://msdn.microsoft.com/en-us/library/dd203259.aspx)” on MSDN for more information.  Basically what we have to do is as follows.

First make sure the Enterprise Library Configuration Tool is open again for some some configuration settings.  First right click on Category Sources and add a category called System.ServiceModel.  To that right click and add an XML Trace Listener (B).  Under the Trace Listeners (A) add an XML Trace Listener.

[![](/images/adronhall.smugmug.com/photos/437429050_TsbSY-L.png)](http://adronhall.smugmug.com/gallery/6842104_frBDt#437429050_TsbSY)

Next right click on the System.ServiceModel node in the tree view and click on the Trace Listener Reference.  In the properties pane select ReferencedTraceListener and pick XML Trace Listener.

[![](/images/adronhall.smugmug.com/photos/437428960_j3yHc-L.png)](http://adronhall.smugmug.com/gallery/6842104_frBDt#437428960_j3yHc)

Now hit F4 again to show the properties and select the XML Trace Listener.  Under the properties select a place for the log file to be placed and enter the information as shown.

[![](/images/adronhall.smugmug.com/photos/437432414_q9mj2-M.png)](http://adronhall.smugmug.com/gallery/6842104_frBDt#437432414_q9mj2)

Now double click on the web.config file and add this to the very end just before the closing </configuration> tag.

```
   1:    <system.diagnostics>
   2:      <sources>
   3:        <source name="System.ServiceModel" switchValue="All">
   4:          <listeners>
   5:            <add name="traceListener" type="Microsoft.Practices.EnterpriseLibrary.Logging.TraceListeners.EntLibLoggingProxyTraceListener, Microsoft.Practices.EnterpriseLibrary.Logging" />
   6:          </listeners>
   7:        </source>
   8:      </sources>
   9:    </system.diagnostics>
```

.csharpcode, .csharpcode pre
{
font-size: small;
color: black;
font-family: consolas, “Courier New”, courier, monospace;
background-color: #ffffff;
/\*white-space: pre;\*/
}
.csharpcode pre { margin: 0em; }
.csharpcode .rem { color: #008000; }
.csharpcode .kwrd { color: #0000ff; }
.csharpcode .str { color: #006080; }
.csharpcode .op { color: #0000c0; }
.csharpcode .preproc { color: #cc6633; }
.csharpcode .asp { background-color: #ffff00; }
.csharpcode .html { color: #800000; }
.csharpcode .attr { color: #ff0000; }
.csharpcode .alt
{
background-color: #f4f4f4;
width: 100%;
margin: 0em;
}
.csharpcode .lnum { color: #606060; }

Under the <system.serviceModel> tag add this.

```
   1:      <diagnostics>
   2:        <messageLogging logEntireMessage="true" logMalformedMessages="true" logMessagesAtTransportLevel="true" />
   3:      </diagnostics>
```

.csharpcode, .csharpcode pre
{
font-size: small;
color: black;
font-family: consolas, “Courier New”, courier, monospace;
background-color: #ffffff;
/\*white-space: pre;\*/
}
.csharpcode pre { margin: 0em; }
.csharpcode .rem { color: #008000; }
.csharpcode .kwrd { color: #0000ff; }
.csharpcode .str { color: #006080; }
.csharpcode .op { color: #0000c0; }
.csharpcode .preproc { color: #cc6633; }
.csharpcode .asp { background-color: #ffff00; }
.csharpcode .html { color: #800000; }
.csharpcode .attr { color: #ff0000; }
.csharpcode .alt
{
background-color: #f4f4f4;
width: 100%;
margin: 0em;
}
.csharpcode .lnum { color: #606060; }

Check [here for a complete listing of the web.config file](/blogs/technology__software_development/page/Implementing-Enterprise-Library-Architecture-WebConfig-Version-1.aspx).

### References

We’ve done most of the configuration and other necessities on that end.  Now it is time to write some code and put some attributes on some classes and methods.  First thing, add the needed references.

Create a directory called *EntLib* in the solution directory (where the \*.sln file is located).  Now copy over the following files from the C:\EntLib41Src\bin directory into the *EntLib* folder in the solution directory;

- Microsoft.Practices.Unity.Interception.dll
- Microsoft.Practices.Unity.Interception.xml

Once the references are added the references tree then add a reference by using the *Browse* tab option on the *Add Reference* Dialog.

Next add the rest of the needed references via the standard GAC method.

[![](/images/adronhall.smugmug.com/photos/437429033_DUGsU-M.png)](http://adronhall.smugmug.com/gallery/6842104_frBDt#437429033_DUGsU)

After setting up the references set the port number to a static port.  This makes it easier to test the services.  Right click on the WCF Services Project and select properties.  Then select the Web tab on the properties screen.  In there, as shown below, is an option to set the port to a specific number.  Change that to 9999.

[![](/images/adronhall.smugmug.com/photos/437429045_hfyrS-M.png)](http://adronhall.smugmug.com/gallery/6842104_frBDt#437429045_hfyrS)

Test After Part of Services

At this point we’ll want to test the services we have to assure we’re actually logging the data appropriately.  Add another Test Project to the solution called *PipServices.Hosted.Tests*.

Next add a services reference to the project and call it *ProxyPipServices*.  After adding the services reference your Project should have the following.

[![](/images/adronhall.smugmug.com/photos/437432424_LLB65-L.png)](http://adronhall.smugmug.com/gallery/6842104_frBDt#437432424_LLB65)

Next add a file to the project called *HostedServicesTest.cs* and enter the following code.

```
   1:  using Microsoft.VisualStudio.TestTools.UnitTesting;
   2:  using PipServices.Hosted.Tests.ProxyPipServices;
   3:
   4:  namespace PipServices.Hosted.Tests
   5:  {
   6:      [TestClass]
   7:      public class HostedServicesTest
   8:      {
   9:          [TestMethod]
  10:          public void TestServices()
  11:          {
  12:              // Test executing against: http://localhost:9999/PipServices.svc
  13:              var client = new PipServicesClient();
  14:
  15:              Assert.IsTrue(client.DoWork(false));
  16:              Assert.IsFalse(client.DoWork(true));
  17:              client.Close();
  18:          }
  19:
  20:          [TestMethod]
  21:          public void TestServicesLoggingWithLotsOfData()
  22:          {
  23:              var client = new PipServicesClient();
  24:
  25:              for (int i =0; i < 1000; i++)
  26:              {
  27:                  Assert.IsTrue(client.DoWork(false));
  28:                  Assert.IsFalse(client.DoWork(true));
  29:              }
  30:              client.Close();
  31:          }
  32:      }
  33:  }
```

.csharpcode, .csharpcode pre
{
font-size: small;
color: black;
font-family: consolas, “Courier New”, courier, monospace;
background-color: #ffffff;
/\*white-space: pre;\*/
}
.csharpcode pre { margin: 0em; }
.csharpcode .rem { color: #008000; }
.csharpcode .kwrd { color: #0000ff; }
.csharpcode .str { color: #006080; }
.csharpcode .op { color: #0000c0; }
.csharpcode .preproc { color: #cc6633; }
.csharpcode .asp { background-color: #ffff00; }
.csharpcode .html { color: #800000; }
.csharpcode .attr { color: #ff0000; }
.csharpcode .alt
{
background-color: #f4f4f4;
width: 100%;
margin: 0em;
}
.csharpcode .lnum { color: #606060; }

Right click on the PipServices.svc file in the PipServices WCF Project and select *View in Browser*.

[![](/images/adronhall.smugmug.com/photos/437432433_TZ7Cm-L.png)](http://adronhall.smugmug.com/gallery/6842104_frBDt#437432433_TZ7Cm)

This should get the cassini server running with our service endpoint.  To check the cassini server just click on the icon in the task icon area of the start bar.  This service, and the other two (the MVC Application and Web Forms Application) will probably be running, the main one we want to see of course is the web service running on port 9999.

[![](/images/adronhall.smugmug.com/photos/437432441_8L2ZB-M.png)](http://adronhall.smugmug.com/gallery/6842104_frBDt#437432441_8L2ZB)

Now just run those tests to be sure everything gives green lights.

[![](/images/adronhall.smugmug.com/photos/437432449_ThbDJ-L.png)](http://adronhall.smugmug.com/gallery/6842104_frBDt#437432449_ThbDJ)

Once the tests run navigate to where the XML Trace Listener File is to be sure everything populated.  (The path should be something similar to C:\Users\YourUser\Documents\Visual Studio 2008\Projects\PolicyInjectionFramework\PipServices if you’ve left the default folder as your solution/project creation folder)

In that folder you should see a file called trace-xml (or whatever you’ve named it).  If you’ve only run the tests once, the file will probably be about 150-200Kb.  Without filtering what is logged this file grows at a VERY fast rate.  If you set the loop in the tests provided to repeat 1000 times instead of 100 you’ll see a much larger at a very rapid pace.  On my 2Ghz Dual Core it takes about 2 minutes to run through a thousand repetitions of this test.  As one can guess, the logging needs drastically reduced for a production environment.

[![](/images/adronhall.smugmug.com/photos/437432459_dXPEe-S.png)](http://adronhall.smugmug.com/gallery/6842104_frBDt#437432459_dXPEe)

[![kick it on DotNetKicks.com](http://www.dotnetkicks.com/Services/Images/KickItImageGenerator.ashx?url=http%3a%2f%2fwww.adronbhall.com%2fblogs%2ftechnology__software_development%2fpost%2f2008%2f12%2f16%2fImplementing-Enterprise-Library-Architecture-Part-1.aspx&bgcolor=3333FF&cfgcolor=CC3300)](http://www.dotnetkicks.com/kick/?url=http%3a%2f%2fwww.adronbhall.com%2fblogs%2ftechnology__software_development%2fpost%2f2008%2f12%2f16%2fImplementing-Enterprise-Library-Architecture-Part-1.aspx)
