---
title: 'Cloud Throw Down:  Part 3 – Relational Databases and Instance Prices'
date: 2010-11-08 05:15:56 -0800
last_modified_at: 2010-11-09 10:54:13 -0800
permalink: /2010/11/08/cloudthrowdown-part3-2/
slug: cloudthrowdown-part3-2
wp_id: 1612
original_url: https://compositecode.blog/2010/11/08/cloudthrowdown-part3-2/
categories:
- AWS
- Azure
- Tech Throw-down
tags:
- amazon web services
- aws
- azure
- cloud
- cloud computing
- ec2
- virtual
- web role
- windows azure
excerpt: Now we’re going to throw down on something that I’ve had more than a few requests for. I’m going to break out and get some charts, graphs, and price differentials on AWS and Windows Azure. This throw down entry is going to be nothing but money, money, and more money. Have any guesses yet how this one is going to come out? Well read on! Relational Database Storing 1 GB to 50 GB This comparison may shock you. The two primary products from AWS and Windows Azure are AWS RDS, or Amazon Web Services Relation Data Store and SQL Azure. The following chart shows the initial cost at 1GB of storage in each, and then the progressive increase in price as we scale up to 50GB. There is one thing to add here, that at 50GB SQL Azure stops, so if you have more than 50GB of storage you want in a relational database, you don’t even have an option in SQL Azure. But let’s just take a look, and then I’ll go through and explain the pricing and declare the victorious. Here’s a graph, with pricing along the left y axis and the storage requirement along the x axis. Feel free to check out the original spreadsheet too.
---

|  |  |
| --- | --- |
| [Amazon Web Services](http://aws.amazon.com)  *Amazon Web Services* | [Windows Azure](http://www.microsoft.com/windowsazure)  *Windows Azure* |

[Previous Throw Down…](/2010/11/03/cloudthrowdown-part2/)

Now we’re going to throw down on something that I’ve had more than a few requests for. I’m going to break out and get some charts, graphs, and price differentials on AWS and Windows Azure. This throw down entry is going to be nothing but money, money, and more money. Have any guesses yet how this one is going to come out? Well read on!

**Relational Database Storing 1 GB to 50 GB**

This comparison may shock you.  The two primary products from AWS and Windows Azure are AWS RDS, or Amazon Web Services Relation Data Store and SQL Azure.  The following chart shows the initial cost at 1GB of storage in each, and then the progressive increase in price as we scale up to 50GB.  There is one thing to add here, that at 50GB SQL Azure stops, so if you have more than 50GB of storage you want in a relational database, you don’t even have an option in SQL Azure.  But let’s just take a look, and then I’ll go through and explain the pricing and declare the victorious.

Here’s a graph, with pricing along the left y axis and the storage requirement along the x axis.  Feel free to check out the [original spreadsheet](https://spreadsheets.google.com/pub?key=0AjzoXvTKg56mdFJOaUwtNVozeWV6VGx2YzhJTlF6eHc&hl=en&output=html) too.

[![RDBMS with SQL Azure and AWS RDS](/images/adronhall.smugmug.com/Software/Reviews/throw-down/RDBMS-01/1074107608_SWUyU-O.png "RDBMS with SQL Azure and AWS RDS")](http://adronhall.smugmug.com/Software/Reviews/throw-down/)

*RDBMS with SQL Azure and AWS RDS*

Like I was saying about the surprise.  SQL Azure starts out cheaper than Amazon’s options but immediately goes into the stratosphere of pricing!  $499.95 just seems absolutely insane.  You really gotta love a limited SQL Server to go diving after that RDBMS versus Amazon’s more scalable RDS option, which never breaks $82.50.  Really, this isn’t a victory, it’s a wholesale slaughter over SQL Azure.

***Rating & Winner:  **Relational Database Storing 1 GB to 50 GB**** goes to AWS.*

**Single Instance .NET Web Application running on Windows**

First off, let’s just take a look at the micro instances.  The instances are perfect for testing out, basic development work and developer servers, and even scaling to larger things.  Here’s how the costs pan out.

[![Windows Azure vs. AWS Micro Instances](/images/adronhall.smugmug.com/Software/Reviews/throw-down/chart-for-micro-instances/1074185498_gmuCq-O.png "Windows Azure vs. AWS Micro Instances")](http://adronhall.smugmug.com/Software/Reviews/throw-down/chart-for-micro-instances)

*Windows Azure vs. AWS Micro Instances*

The blue, in Windows Azure color shows the Windows Azure Micro Instance.  Almost double what a similar instance running Windows Server 2008 would cost you on AWS, and more well more than double, which I’ll point out again in the next section.  AWS is the obvious cheaper candidate with the smallest instances.  But what about the slightly larger sizes, let’s take a look at that.

[![Windows Azure vs. Amazon Web Services Middle Tier Instances](/images/adronhall.smugmug.com/Software/Reviews/throw-down/chart-for-mid-tier-instances/1074196499_mJkcz-O.png "Windows Azure vs. Amazon Web Services Middle Tier Instances")](http://adronhall.smugmug.com/Software/Reviews/throw-down/chart-for-mid-tier-instances/)

*Windows Azure vs. Amazon Web Services Middle Tier Instances*

The charts are also available in the previously [linked spreadsheet](https://spreadsheets.google.com/pub?key=0AjzoXvTKg56mdFJOaUwtNVozeWV6VGx2YzhJTlF6eHc&hl=en&output=html).  As one can see from these prices they fluctuate on sizes as the instances increase in size.  The Linux instances are almost always cheaper than a comparable Windows Azure instance, and from a ECU/Processor Compute range AWS almost always comes out less expensive with the similar Windows Azure offering.  I still haven’t compared actual process power and performance, but I intend to do that one of these days over the next few weeks or months.  However for pricing on instances the options, and lower price winner with generally equal processing power is…

***Rating & Winner:  **Single Instance .NET Web Application running on Windows**** goes to AWS.*

**Single Instance PHP, Java, or Ruby on Rails Web Application running on Linux**

Now really, we don’t have to do too much more research for this measurement.  Again, AWS handily beats Windows Azure in price and instance capabilities for the Linux, LAMP stack, and general PHP applications.  For more information regarding this I also posted a link regarding WordPress Hosting on AWS & Windows Azure.  Technically feasible with both services, however astronomically cheaper on AWS.  Thus, in this category…

***Rating & Winner:  **Single Instance PHP, Java, or Ruby on Rails Web Application running on Linux**** goes to AWS****.*****

This competition just wasn’t really a good bout.  AWS handily beats Windows Azure in price and compute power overall.  Even when getting into the higher performance options, AWS has high performance compute options that aren’t even available.  Don’t worry Windows Azure fans, there is hope still.  In my next bout I intend to compare the two from a more PaaS oriented point of view.  One of the features and capabilities that will come up is Windows Azure AppFabric.  That will be a much closer fight I’m sure.  For now though…

[![Amazon Web Services and Windows Azure](/images/adronhall.smugmug.com/Software/Software-Development/Technology-Company-Logos/azure-aws-logos/1071455180_FWu37-S.png "Amazon Web Services and Windows Azure")](http://compositecode.com/clouds)

*Amazon Web Services and Windows Azure*

***Today’s Winners is easily*** **AWS**.  The rest of my throw down series will be coming over the next week.  If you have any ideas or things I should compare the two services on, please let me know.  Thanks and hope you enjoyed another bout of the cloud giants.

To check out more about either cloud service navigate over to:

- [Amazon Web Services](http://aws.amazon.com) or
- [Windows Azure](http://www.microsoft.com/windowsazure)
