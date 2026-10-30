---
title: AWS, WordPress, Windows Azure, Clouds, and More…
date: 2010-08-24 11:35:16 -0700
last_modified_at: 2010-08-24 12:28:15 -0700
permalink: /2010/08/24/aws-vs-windows-azure-wordpress/
slug: aws-vs-windows-azure-wordpress
wp_id: 1006
original_url: https://compositecode.blog/2010/08/24/aws-vs-windows-azure-wordpress/
categories:
- AWS
- Azure
- Cloud Speak
tags:
- amazon web services
- aws
- azure
- blog
- cloud
- wordpress
excerpt: I’ve been looking into getting a blog, specifically Wordpress, into the cloud. Of course the first two I take a look at are Windows Azure and AWS. This is what I’ve found so far. Windows Azure… Amazon Web Services…
---

I’ve been looking into getting a blog, specifically WordPress, into the cloud.  Of course the first two I take a look at are Windows Azure and AWS.  This is what I’ve found so far.

[**Windows Azure**](http://www.microsoft.com/windowsazure/)

Windows Azure is easy enough, sort of, but distinctly limits the control and abilities of the actual blog.  This is primarily because of the way one has to host a blog, and the software just isn’t really built to take advantage of the platform specifically.  In other words, WordPress isn’t really built around horizontal scalability.  Also one has to run WordPress in a CGI Instance, not exactly ideal either.  It works, and really does work well, but there are just options that aren’t available in this situation.

The other issue is that a single running CGI Role is going to run you around $100 bucks a month.  I’ve checked and if you push off the entries into a Windows Azure Table Storage area, that’ll easily break past that $100 bucks into the **$110-200** range or higher.  It all really depends on how many transactions and views your site is getting.  If you really necessitate Table Storage vs. a traditional relational data store for your blog, I seriously doubt a couple hundred bucks will be an issue.  In all reality, if you’re using the Table Storage you most likely should be in the traffic range that would run you about $1000 bucks a month or more, in each geographic area.

[**Amazon Web Services**](http://aws.amazon.com/)

AWS is however a different beast altogether.  First, running an EC2 instance you can get everything running that you need.  The data store for the entries and also gain access to a level that allows you to add plugins and all the other features of WordPress.

The pricing on Amazon gets a lot better too.  One can get the reserved instance for $350 bucks a year (or $227.50 for Linux/UNIX).  That enables one to install WordPress with total control for about **$30** bucks a month.  Considering the redundancy, uptime, and general availability and performance of the cloud that is a really decent price.  Even if one gets some heavy bandwidth usage, the cost for that shouldn’t go above a few dollars.

**Summary**

At this time, if you want some cloud computing power behind your blog, AWS is the clear winner in price and performance!

> *A few reference links:*
>
> - [How to Install WordPress in an AWS EC2 Instance](http://www.cloudtweaks.com/2010/07/great-how-to-install-and-run-wordpress-using-microsoft-web-platform-on-amazon-ec2/)
> - [Host WordPress on Windows Azure](http://blogs.msdn.com/b/windows-azure-support/archive/2010/08/13/microsoft-cloud-computing-windows-azure-host-wordpress-on-windows-azure-host-wordpress-on-windows-azure.aspx)
