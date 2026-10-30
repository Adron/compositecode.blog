---
title: 'ASP.NET MVC + Other Cleanup o’ The Day #1'
date: 2011-05-27 11:33:49 -0700
last_modified_at: 2011-05-27 12:50:04 -0700
permalink: /2011/05/27/asp-net-mvc-other-cleanup-o-the-day-1/
slug: asp-net-mvc-other-cleanup-o-the-day-1
wp_id: 2871
original_url: https://compositecode.blog/2011/05/27/asp-net-mvc-other-cleanup-o-the-day-1/
categories:
- .NET Bits
- How-to
tags: []
excerpt: 'Cleanup #1: Here, let me help. Replace this:'
---

Cleanup #1:

Here, let me help.  Replace this:

```csharp
using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.Mvc;
using System.Web.Routing;

namespace Baseline
{
    // Note: For instructions on enabling IIS6 or IIS7 classic mode,
    // visit http://go.microsoft.com/?LinkId=9394801

    public class MvcApplication : System.Web.HttpApplication
    {
        public static void RegisterGlobalFilters(GlobalFilterCollection filters)
        {
            filters.Add(new HandleErrorAttribute());
        }

        public static void RegisterRoutes(RouteCollection routes)
        {
            routes.IgnoreRoute("{resource}.axd/{*pathInfo}");

            routes.MapRoute(
                "Default", // Route name
                "{controller}/{action}/{id}", // URL with parameters
                new { controller = "Home", action = "Index", id = UrlParameter.Optional } // Parameter defaults
            );

        }

        protected void Application_Start()
        {
            AreaRegistration.RegisterAllAreas();

            RegisterGlobalFilters(GlobalFilters.Filters);
            RegisterRoutes(RouteTable.Routes);
        }
    }
}
```

With this:

```csharp
using System.Web.Mvc;
using System.Web.Routing;

namespace Baseline
{
    public class MvcApplication : System.Web.HttpApplication
    {
        public static void RegisterGlobalFilters(GlobalFilterCollection filters)
        {
            filters.Add(new HandleErrorAttribute());
        }

        public static void RegisterRoutes(RouteCollection routes)
        {
            routes.IgnoreRoute("{resource}.axd/{*pathInfo}");
            routes.MapRoute("Default", "{controller}/{action}/{id}",
                new { controller = "Home", action = "Index", id = UrlParameter.Optional }
            );
        }

        protected void Application_Start()
        {
            AreaRegistration.RegisterAllAreas();

            RegisterGlobalFilters(GlobalFilters.Filters);
            RegisterRoutes(RouteTable.Routes);
        }
    }
}
```

It’s not a huge cleanup, but it is cleaner. Got some other ideas to add? 🙂
