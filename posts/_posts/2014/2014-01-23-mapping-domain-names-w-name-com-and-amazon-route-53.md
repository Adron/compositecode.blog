---
title: Mapping Domain Names with name.com, Elastic Beanstalk, Elastic Load Balancer and AWS Route 53
date: 2014-01-23 11:47:33 -0800
last_modified_at: 2014-01-30 11:48:58 -0800
permalink: /2014/01/23/mapping-domain-names-w-name-com-and-amazon-route-53/
slug: mapping-domain-names-w-name-com-and-amazon-route-53
wp_id: 9390
original_url: https://compositecode.blog/2014/01/23/mapping-domain-names-w-name-com-and-amazon-route-53/
categories:
- Architecture
- AWS
- How-to
- Infrastructure
tags:
- amazon
- amazon route 53
- amazon web services
- aws
- dns
- domain
- domain names
- domains
- ec2
- elastic compute
- elastic load balancer
- elb
- load balancer
- mapping
- name.com
- route 53
- route53
excerpt: I finally wrapped up my name server and DNS mapping needs with Name.com, Route 53 and Elastic Beanstalk. Since this was a little confusing I thought a short write up was in order. Thanks to Evan @evandbrown for helping out! The first thing needed is a delegation set of name servers for your DNS and name …
image: /wp-content/uploads/2013/12/internetdomains.jpg
---

I finally wrapped up my name server and DNS mapping needs with [Name.com](http://www.name.com), Route 53 and Elastic Beanstalk. Since this was a little confusing I thought a short write up was in order. Thanks to Evan [@evandbrown](http://twitter.com/evandbrown) for helping out!

The first thing needed is a delegation set of name servers for your DNS and name server provider. These can be found by creating a hosted zone. The way to do this is open up the AWS Management Console and navigate into the Route 53 management area. The Route 53 icon is under the Compute & Networking section on the management console.

[![Beanstalk, Route 53 - Click for full size image](https://photos.adron.me/Software/Software-Development/Deconstructedio/i-6jmzzsd/0/XL/beanstalk%2001-XL.png "Beanstalk, Route 53 - Click for full size image")](https://photos.adron.me/Software/Software-Development/Deconstructedio/i-6jmzzsd/0/O/beanstalk%2001.png)

*Beanstalk, Route 53 – Click for full size image*

Upon navigating to the Route 53 console area click on the *Create Hosted Zones* button.

[![Create Hosted Zone](https://photos.adron.me/Software/Software-Development/Deconstructedio/i-MV8SF4b/0/L/Route_53_Management_Console-L.png "Create Hosted Zone")](https://photos.adron.me/Software/Software-Development/Deconstructedio/i-MV8SF4b/0/O/Route_53_Management_Console.png)

*Create Hosted Zone – Click for full size image*

When the zone is created then the delegation set can be found under the *Hosted Zone Details*. This delegation set now needs setup as the name servers for whoever, in this case [name.com](https://www.name.com/), is the domain provider.

[![Delegation Set - Click for full size image.](https://photos.adron.me/Software/Software-Development/Deconstructedio/i-FXJbQ9d/0/XL/route%2053%2001-XL.png)](https://photos.adron.me/Software/Software-Development/Deconstructedio/i-FXJbQ9d/0/O/route%2053%2001.png)

*Delegation Set – Click for full size image.*

Open up the management console for the name server administration.

…

Upon adding them the list should look something like this.

[![Name servers list built from the delegation set of the hosted zone. Click for full size image.](https://photos.adron.me/Software/Software-Development/Deconstructedio/i-M25jKmH/0/M/namecom%2002-M.png)](https://photos.adron.me/Software/Software-Development/Deconstructedio/i-M25jKmH/0/O/namecom%2002.png)

*Name servers list built from the delegation set of the hosted zone. Click for full size image.*

Once the name servers are setup, those will need time to propagate. Likely this could take a good solid chunk of time, somewhere in the hours range likely, and don’t be surprised if it takes a little bit more than a day.

While the propagation starts navigate back to the AWS Management Console and open up the EC2 section of the console. On the right hand side of the Resources list there is a Load Balancers section. Click it.

[![Load Balancers - Click for full size image.](https://photos.adron.me/Software/Software-Development/Deconstructedio/i-jMPSnFS/0/XL/beanstalk%2002-XL.png)](https://photos.adron.me/Software/Software-Development/Deconstructedio/i-jMPSnFS/0/O/beanstalk%2002.png)

*Load Balancers – Click for full size image.*

In this section there is a listing of all load balancers that have been created manually or by Elastic Beanstalk.

[![Load Balancers - Click for full size image.](https://photos.adron.me/Software/Software-Development/Deconstructedio/i-LR8Fkqq/0/XL/beanstalk%2004-XL.png)](https://photos.adron.me/Software/Software-Development/Deconstructedio/i-LR8Fkqq/0/O/beanstalk%2004.png)

*Load Balancers – Click for full size image.*

Make note of the *Load Balancer Name* for selection in Route 53. This is what Route 53 needs in order to point an alias at for incoming traffic to that particular Elastic Beanstalk application. In this particular image above there are 4 load balancers listed, the easiest way to prevent confusion is to take note of the load balancer name at the time of creation, but this is the easiest way to find them otherwise.

[![Record Set - Click for full size image](https://photos.adron.me/Software/Software-Development/Deconstructedio/i-wmkqWTT/0/XL/route%2053%2002%20its%20not%20a%20records%20strangely%20oh-XL.png)](https://photos.adron.me/Software/Software-Development/Deconstructedio/i-wmkqWTT/0/O/route%2053%2002%20its%20not%20a%20records%20strangely%20oh.png)

*Record Set – Click for full size image*

Now when going back to the hosted zone to set it up with the appropriate information, create a new record with the appropriate name, in this case I was setting up the admin.deconstructed.io (no it isn’t live yet, I just set it up to test it out) to point to an alias target. Just leave the *Type* set to *A – IPv4 address* and click the radio control so that *Alias* is set to *Yes*. In the alias target select the appropriate load balancer for the Elastic Beanstalk (or whatever it points to) application.

That’s it, give it a few hours (or a day) and eventually the domain or subdomain will be pointed appropriately at the Elastic Beanstalk load balanced application.
