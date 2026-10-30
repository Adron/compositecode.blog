---
title: jQuery Starter Bits
date: 2010-07-06 04:56:11 -0700
last_modified_at: 2010-07-07 13:57:38 -0700
permalink: /2010/07/06/jquery-starter-bits/
slug: jquery-starter-bits
wp_id: 140
original_url: https://compositecode.blog/2010/07/06/jquery-starter-bits/
categories:
- Unknown Code Ramblings
tags: []
excerpt: I’m going to be doing some jQuery work over the next few months so I thought to myself, “why don’t I put my notes and such up on the blog”. I decided that was a good idea so this is the start of those notes & other such how-to write ups. The first thing anyone needs to do when starting to use jQuery is to reference the library. There area couple different ways to do this, depending on which version you want to use.
---

I’m going to be doing some jQuery work over the next few months so I thought to myself, “why don’t I put my notes and such up on the blog”.  I decided that was a good idea so this is the start of those notes & other such how-to write ups.

The first thing anyone needs to do when starting to use jQuery is to reference the library.  There area  couple different ways to do this, depending on which version you want to use.

**Reference Method #1**

One of the most common reference methods for jQuery is to reference the latest, greatest, always updated library located at [Google](http://www.google.com) hosted or Microsoft hosted CDN.  With this method you just reference the particular version you are using as shown below.

```html
<link rel="stylesheet" type="text/css" href="../../Content/Site.css" />
<script type="text/javascript" src="http://ajax.googleapis.com/ajax/libs/jquery/1.3.2/jquery.min.js">
</script>
```

The [Microsoft jQuery CDN](http://visitmix.com/Opinions/jquery-love) can be found here:

```html
<link rel="stylesheet" type="text/css" href="../../Content/Site.css" />
<script type="text/javascript" src="http://ajax.microsoft.com/ajax/jQuery/jquery-1.3.2.min.js">
</script>
```

**Reference Method #2**

The second method is to download the library from the [jQuery.com Website](http://jquery.com/).  Then of course reference it locally to the server you host it on.

```html
<head runat="server">

<link rel="stylesheet" type="text/css" href="../../Content/Site.css" />
<script type="text/javascript" src="../../Scripts/jquery-1.4.1.js">
</script>
```

**Some ASP.NET and ASP.NET MVC specific notes.**

ASP.NET and ASP.NET MVC comes with version 1.4.1 included in the *Scripts* Directory of any ASP.NET or ASP.NET MVC Project Application Template you create/start.  This backs the new [Microsoft](http://www.microsoft.com) support of the [jQuery Library](http://weblogs.asp.net/scottgu/archive/2008/09/28/jquery-and-microsoft.aspx).

[![Shout it](http://dotnetshoutout.com/image.axd?url=http%3A%2F%2Fcompositecode.com%2F2010%2F07%2F06%2Fjquery-starter-bits%2F)](http://dotnetshoutout.com/jQuery-Starter-Bits)
