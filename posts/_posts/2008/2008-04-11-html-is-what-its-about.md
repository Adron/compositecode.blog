---
title: HTML is What It's About!
date: 2008-04-11 06:38:37 -0700
last_modified_at: 2008-04-11 06:38:37 -0700
permalink: /2008/04/11/html-is-what-its-about/
slug: html-is-what-its-about
wp_id: 314
original_url: https://compositecode.blog/2008/04/11/html-is-what-its-about/
categories:
- Uncategorized Bits
tags: []
excerpt: I’ve never had to actually utilize the custom extension build provider or http handler in .NET since way way back pre-2.0. Well that came up again and I went to messing with it and came to the conclusion that it is slightly different now. What I had to do to get HTML pages to build …
---

I’ve never had to actually utilize the custom extension build provider or http handler in .NET since way way back pre-2.0.  Well that came up again and I went to messing with it and came to the conclusion that it is slightly different now.  What I had to do to get HTML pages to build and render as HTML just like ASPX is below.  Kind of funny trying to get build-able HTML to render HTML?  There is some type of paradox or something there.  doh!

First I added the httpHandler below with the buildProvider.  That was it, nothing else to configure really.  When deploying make sure the server (IIS) handles this correctly.  Other than that, to create \*.aspx pages out of \*.html pages this is it.

<system.web>
  <compilation debug=”true”>
    <buildProviders>
      <add extension=”.html” type=”System.Web.Compilation.PageBuildProvider” />
    </buildProviders>
  </compilation>
  <httpHandlers>
    <add verb=”\*” path=”\*.html” type=”System.Web.UI.PageHandlerFactory” />
 </httpHandlers>

Now when you’re creating these HTML / ASPX pages there are a few tricks to simplify things.  First off, don’t select HTML out of the menu of templates when you are creating new pages.  Instead create the \*.aspx pages just like you normally would, the difference is, you just rename the file.  That way all of the properly placed markup is in the file for you already, and if you want to select a custom master page you can do so and not have to worry about the markup either.

With some of the things I’m doing with ASP.NET MVC I think this would be a grand idea also, as the restful services, clean paths, and other things are used, developers should also nix the \*.aspx extension and just run the things as \*.html.  Since really, that is the way it was meant to be, and that is what it’s all about!

del.icio.us Tags: [PageBuildProvider](http://del.icio.us/popular/PageBuildProvider),[PageHandlerFactory](http://del.icio.us/popular/PageHandlerFactory),[buildProvider](http://del.icio.us/popular/buildProvider),[httpHandlers](http://del.icio.us/popular/httpHandlers),[aspx](http://del.icio.us/popular/aspx),[html](http://del.icio.us/popular/html),[compilation](http://del.icio.us/popular/compilation),[ASP.NET](http://del.icio.us/popular/ASP.NET)

Technorati Tags: [PageBuildProvider](http://technorati.com/tags/PageBuildProvider),[PageHandlerFactory](http://technorati.com/tags/PageHandlerFactory),[buildProvider](http://technorati.com/tags/buildProvider),[httpHandlers](http://technorati.com/tags/httpHandlers),[aspx](http://technorati.com/tags/aspx),[html](http://technorati.com/tags/html),[compilation](http://technorati.com/tags/compilation),[ASP.NET](http://technorati.com/tags/ASP.NET)
