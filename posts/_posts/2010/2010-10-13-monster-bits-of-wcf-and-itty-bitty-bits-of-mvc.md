---
title: Monster Bits of WCF and Itty Bitty Bits of MVC
date: 2010-10-13 06:08:14 -0700
last_modified_at: 2010-10-13 08:32:17 -0700
permalink: /2010/10/13/monster-bits-of-wcf-and-itty-bitty-bits-of-mvc/
slug: monster-bits-of-wcf-and-itty-bitty-bits-of-mvc
wp_id: 1473
original_url: https://compositecode.blog/2010/10/13/monster-bits-of-wcf-and-itty-bitty-bits-of-mvc/
categories:
- How-to
tags:
- asp.net mvc
- controller
- controller action
- http
- rest
- restful
- web services
excerpt: I’ve had the pleasure of working with WCF on three specific projects that have brought me to this blog entry. I haven’t used WCF on only three projects, there are just three that have brought me to write this entry. I’ve used WCF a lot, since back when it was a beta. WCF is great when creating SOAP services and you aren’t too worried about the extra overhead. WCF is great for what it does, for the ideas behind what it does. But writing RESTful web services doesn’t seem to be its strong point. On two huge projects WCF has basically been dropped, or so scaled back one really can’t honestly say that WCF is used, and either an alternate framework has been used or a LOT of custom code ends up being written. The first time I used WCF to implement RESTful service was at Webtrends. Albeit, there is a single service that returns all types of awesome reporting goodness, however to implement basic auth, logging, polling, and a whole host of other Enterprise Scale needs we had to custom roll most of it. Keep in mind, when doing this the WCF REST capabilities were brand shiny and new, so there were a few issues to work out. Now, maybe WCF could be used and a lot of it would be built in. However as it was, we easily spent 60% of the time writing custom bits because WCF just didn’t have the right options with the right bindings. But I digress, I recently implemented an architecture using RESTful services using WCF. But now I’ve come to find myself dropping WCF because of the back and forth and going with ASP.NET MVC controller actions to return JSON instead. With that, here’s to the lean mean controller actions rockin’ the JSON. Here’s what I’ve done to port everything from WCF to MVC. To see what I had done, except on a smaller scale, check out my previous blog entry on ASP.NET MVC with a WCF project smack in the middle of it . This will give you an idea of what I was using the WCF services for, merely to provide JSON results via RESTful services to an ASP.NET MVC front end requesting data with jQuery. This is how I’ve setup the controller to return JSON results via an action.
---

I’ve had the pleasure of working with WCF on three specific projects that have brought me to this blog entry.  I haven’t used WCF on only three projects, there are just three that have brought me to write this entry.  I’ve used WCF a lot, since back when it was a beta.  WCF is great when creating SOAP services and you aren’t too worried about the extra overhead.  WCF is great for what it does, for the ideas behind what it does.

But writing RESTful web services doesn’t seem to be its strong point.  On two huge projects WCF has basically been dropped, or so scaled back one really can’t honestly say that WCF is used, and either an alternate framework has been used or a LOT of custom code ends up being written.

The first time I used WCF to implement RESTful service was at Webtrends.  Albeit, there is a single service that returns all types of awesome reporting goodness, however to implement basic auth, logging, polling, and a whole host of other Enterprise Scale needs we had to custom roll most of it.  Keep in mind, when doing this the WCF REST capabilities were brand shiny and new, so there were a few issues to work out.  Now, maybe WCF could be used and a lot of it would be built in.  However as it was, we easily spent 60% of the time writing custom bits because WCF just didn’t have the right options with the right bindings.

But I digress, I recently implemented an architecture using RESTful services using WCF.  But now I’ve come to find myself dropping WCF because of the back and forth and going with ASP.NET MVC controller actions to return JSON instead.  With that, here’s to the lean mean controller actions rockin’ the JSON.  Here’s what I’ve done to port everything from WCF to MVC.

To see what I had done, except on a smaller scale, check out my previous blog entry on [ASP.NET MVC with a WCF project smack in the middle of it](/2010/09/03/aggregated-web-services-pt-ii-2/).  This will give you an idea of what I was using the WCF services for, merely to provide JSON results via RESTful services to an ASP.NET MVC front end requesting data with jQuery.

This is how I’ve setup the controller to return JSON results via an action.

First start a new ASP.NET MVC Project and add a new controller.  Cleanup the controller so that you have the following in the controller.

```csharp
using System.Web.Mvc;

namespace RestWebServicesWithMvc.Controllers
{
    public class ServicesController : Controller
    {

    }
}
```

Now create a testing project to create your test first.  Remember to add the reference to the ASP.NET MVC project.  From here we can create the first test.

```csharp
using Microsoft.VisualStudio.TestTools.UnitTesting;
using RestWebServicesWithMvc.Controllers;

namespace RestWebServicesWithMvc.Tests
{
    [TestClass]
    public class UnitTest1
    {
        [TestMethod]
        public void TestMethod1()
        {
            var controller = new ServicesController();
            var result = controller.GetBiz();
            Assert.IsNotNull(result);
        }
    }
}
```

Now fill out the basic skeleton of the action in the controller.

```csharp
using System;
using System.Web.Mvc;

namespace RestWebServicesWithMvc.Controllers
{
    public class ServicesController : Controller
    {
        public ActionResult GetBiz()
        {
            throw new NotImplementedException();
        }
    }
}
```

Now we should have a good red running on our test.  Let’s create a business model class to return as our result next.

```csharp
namespace RestWebServicesWithMvc.Models
{
    public class BizEntity
    {
        public string BizName { get; set; }
        public string StartupDate { get; set; }
        public int SalesThisMonth { get; set; }
    }
}
```

Now let’s return that object with some fake data.  First add [AcceptVerbs(HttpVerbs.Post)] to the action in the controller.  Then return a serializable object to the actual method as shown.

```csharp
[AcceptVerbs(HttpVerbs.Post)]
public ActionResult GetBiz()
{
    return Json(
        new BizEntity()
            {
                BizName = "Adron's Code Workingz",
                SalesThisMonth = 3429,
                StartupDate = DateTime.Now.AddYears(-5).ToString()
            }
        );
}
```

This is a quick starter.  There are a few dozen other options around this capability including other verb usage.  For many, this is all you need for your services, especially if their primary purpose is to communicate with a specific website and one doesn’t want the overhead of WCF.

[![Shout it](http://dotnetshoutout.com/image.axd?url=http%3A%2F%2Fcompositecode.com%2F2010%2F10%2F13%2Fmonster-bits-of-wcf-and-itty-bitty-bits-of-mvc%2F)](http://dotnetshoutout.com/Monster-Bits-of-WCF-and-Itty-Bitty-Bits-of-MVC-Composite-Code)
