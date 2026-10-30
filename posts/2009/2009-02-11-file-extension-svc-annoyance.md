---
title: File Extension ".svc" Annoyance!
date: 2009-02-11 05:21:23 +0000
last_modified_at: 2009-02-11 05:21:23 +0000
permalink: /2009/02/11/file-extension-svc-annoyance/
slug: file-extension-svc-annoyance
wp_id: 586
original_url: https://compositecode.blog/2009/02/11/file-extension-svc-annoyance/
categories:
- Uncategorized Bits
tags: []
excerpt: REST Services are intended to have clean URIs. So when Microsoft started pushing their REST over WCF Services I thought, “SWEET”, lemme get some of that. While working with these services though a problem arose, “ http://www.soemthing.com/someservice.svc” ; is NOT a very clean REST URI. I just don’t dig nonsense like this so I went digging about …
---

REST Services are intended to have clean URIs.  So when Microsoft started pushing their REST over WCF Services I thought, “SWEET”, lemme get some of that.  While working with these services though a problem arose, “<http://www.soemthing.com/someservice.svc&#8221>; is NOT a very clean REST URI.  I just don’t dig nonsense like this so I went digging about for a fix.

Sure one can go into the whole process of doing some URI rewriting, but I wanted something fast, simple, and deployed in about 10-15 minutes.  HTTP Modules to the rescue!

First I created a regular class project and created a class file called RestUriCleanup.cs.  I then added the following code into the class file.

```
   1:  using System.Web;
   2:
   3:  namespace StandardServicesApplication
   4:  {
   5:      public class RestUriCleanup : IHttpModule
   6:      {
   7:          #region IHttpModule Members
   8:
   9:          public void Init(HttpApplication context)
  10:          {
  11:              context.BeginRequest +=
  12:                  delegate
  13:                      {
  14:                          var ctx = HttpContext.Current;
  15:                          string path = ctx.Request.AppRelativeCurrentExecutionFilePath;
  16:
  17:                          int i = path.IndexOf('/', 2);
  18:                          if (i > 0)
  19:                          {
  20:                              string svc = path.Substring(0, i) + ".svc";
  21:                              string rest = path.Substring(i, path.Length - i);
  22:                              string qs = ctx.Request.QueryString.ToString();
  23:                              ctx.RewritePath(svc, rest, qs, false);
  24:                          }
  25:                      };
  26:          }
  27:
  28:          public void Dispose()
  29:          {
  30:          }
  31:
  32:          #endregion
  33:      }
  34:  }
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

In the web.config file I added the following configuration settings in the httpModules Section.  Notice that the ScriptModule is already included as a handler as of .NET 3.5.

```
   1:      <httpModules>
   2:        <add name="RestUriCleanup" type="StandardServicesApplication.RestUriCleanup, StandardServicesApplication" />
   3:        <add name="ScriptModule" type="System.Web.Handlers.ScriptModule, System.Web.Extensions, Version=3.5.0.0, Culture=neutral, PublicKeyToken=31BF3856AD364E35"/>
   4:      </httpModules>
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

Now at this point things can get tricky.  Depending on the version of IIS you’ll possibly need to make some changes at this point.  IIS 6.0 is setup as follows.  Open up the management console and right click the app or virtual directory and click on properties.  Click on the *Home Directory* tab and click on the *Configuration* button.

[![](/images/adronhall.smugmug.com/photos/471674999_Wtf6f-M.png)](http://adronhall.smugmug.com/gallery/7330712_92KEW#471674999_Wtf6f)

Once you have that dialog open then *Insert* a new wildcard application map.  Find and select the aspnet\_isapi.dll file.  It should be located here:  “*C:\WINDOWS\Microsoft.NET\Framework\v2.0.50727\aspnet\_isapi.dll*“

[![](/images/adronhall.smugmug.com/photos/471675033_mQoBf-M.png)](http://adronhall.smugmug.com/gallery/7330712_92KEW#471675033_mQoBf-A-LB)

Make SURE when you are adding the file, do NOT leave or check the Verify that file exists box.  I repeat, do NOT check it.

[![](/images/adronhall.smugmug.com/photos/471675045_RhYy6-M.png)](http://adronhall.smugmug.com/gallery/7330712_92KEW#471675045_RhYy6)

That’s it.  You now have your \*.svc extension removed from your services file and should have nice clean REST based URIs.  This process is slightly different on IIS 7 w/ Vista or Windows Server 2008.  First off you do NOT need to create a wildcard on IIS 7 but you will need to go in and create a setting in IIS for the HTTP Module.  If interested let me know and I’ll add another blog entry for that, but for now…  this is how one gets rid of the \*.svc extension.
