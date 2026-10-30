---
title: 'Debugging ADO.NET Data Services :: Tip o'' The Day'
date: 2008-12-01 02:50:25 +0000
last_modified_at: 2008-12-01 02:50:25 +0000
permalink: /2008/12/01/debugging-ado-net-data-services-tip-o-the-day/
slug: debugging-ado-net-data-services-tip-o-the-day
wp_id: 567
original_url: https://compositecode.blog/2008/12/01/debugging-ado-net-data-services-tip-o-the-day/
categories:
- Uncategorized Bits
tags: []
excerpt: I haven’t written up a tip o’ the day in ages, so it was about time that I ran smack into one. While working with ADO.NET Data Services I kept getting this AWESOME error message! An error occurred while processing this request. That being one of the most awesome, fully articulate, well written, useful, cool …
---

I haven’t written up a tip o’ the day in ages, so it was about time that I ran smack into one.  While working with ADO.NET Data Services I kept getting this AWESOME error message!

> ***An error occurred while processing this request.***

That being one of the most awesome, fully articulate, well written, useful, cool error messages ever created!

Ok, so if you’re like me, and you’d actually like some idea of the underlying error, then here’s the trick.  First, grab that web.config and make sure your services have the appropriate debugging attributes.

```
   1:    <system.serviceModel>
   2:      <behaviors>
   3:        <serviceBehaviors >
   4:          <behavior name="DebugEnabled">
   5:            <serviceDebug includeExceptionDetailInFaults="True"/>
   6:          </behavior>
   7:        </serviceBehaviors>
   8:        <endpointBehaviors>
   9:          <behavior name="TheReporter.AjaxConnectionServiceAspNetAjaxBehavior">
  10:            <enableWebScript/>
  11:          </behavior>
  12:          <behavior name="TheReporter.Services.AjaxConnectorServicesAspNetAjaxBehavior">
  13:            <enableWebScript/>
  14:          </behavior>
  15:        </endpointBehaviors>
  16:      </behaviors>
  17:      <services>
  18:        <service name="TheReporter.AjaxConnectionService" behaviorConfiguration ="DebugEnabled">
  19:          <endpoint address="" behaviorConfiguration="TheReporter.AjaxConnectionServiceAspNetAjaxBehavior" binding="webHttpBinding" contract="TheReporter.AjaxConnectionService"/>
  20:        </service>
  21:        <service name="TheReporter.Services.AjaxConnectorServices" behaviorConfiguration ="DebugEnabled">
  22:          <endpoint address="" behaviorConfiguration="TheReporter.Services.AjaxConnectorServicesAspNetAjaxBehavior" binding="webHttpBinding" contract="TheReporter.Services.AjaxConnectorServices"/>
  23:        </service>
  24:      </services>
  25:      <serviceHostingEnvironment aspNetCompatibilityEnabled="true"/>
  26:    </system.serviceModel>
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

Note the attributes that have words like "debugged" in them.  Throw those in and you’re probably set.  Another thing you can do is to throw in the following code in your actual data service to enable verbose debugging.

```
   1:      public class RssStorageService : DataService<RssStoreEntities>
   2:      {
   3:          public static void InitializeService(IDataServiceConfiguration config)
   4:          {
   5:              config.UseVerboseErrors = true;
   6:              config.SetEntitySetAccessRule("*", EntitySetRights.All);
   7:          }
   8:      }
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

So that should provide some reasonable error messages instead of the awesome one at the top of this here post.   …Oh but wait, there’s more!  One last tip for this tip is the code attribute tag.  Throw this onto a particular method to add verbose debugging.

```
   1:  [System.ServiceModel.ServiceBehavior(IncludeExceptionDetailInFaults = true)]
```

(I snagged these last two from [here](http://www.snowball.be/Debugging+ADONET+Data+Services.aspx), the first part of this tip I snagged from [here](http://blogs.msdn.com/phaniraj/archive/2008/06/18/debugging-ado-net-data-services.aspx).)
