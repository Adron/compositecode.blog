---
title: Red Hat, OpenShift PaaS and Cartridges for Riak
date: 2013-04-14 21:32:22 -0700
last_modified_at: 2013-04-14 22:29:31 -0700
permalink: /2013/04/14/red-hat-openshift-paas-and-cartridges-for-riak/
slug: red-hat-openshift-paas-and-cartridges-for-riak
wp_id: 8149
original_url: https://compositecode.blog/2013/04/14/red-hat-openshift-paas-and-cartridges-for-riak/
categories:
- AWS
- Databases
- Distributed Things
- How-to
- Linux
- OpenShift
- Platform (as a Service)
- Riak
tags:
- distributed database
- openshift
- openshift cartridge
- openstack
- riak
excerpt: Today I participated in the OpenShift Community Day here in Portland at the Doubletree Hotel. One of the things I wanted to research was the possibility of putting together a OpenShift Origin Cartridge for Riak. As with most PaaS Systems this isn’t the most straight forward process. The reason is simple, OpenShift and CloudFoundry have …
---

Today I participated in the [OpenShift Community Day](http://openshiftorigincommunityday.eventbrite.com/) here in Portland at the Doubletree Hotel. One of the things I wanted to research was the possibility of putting together a OpenShift Origin Cartridge for Riak. As with most PaaS Systems this isn’t the most straight forward process. The reason is simple, OpenShift and CloudFoundry have a deployment model based around certain conventions that don’t fit with the multi-node deployment of a distributed database. But there are ways around this and my intent was to create or come up with a plan for a Cartridge to commit these work-arounds.

After reading the “[New OpenShift Cartridge Format – Part 1](https://www.openshift.com/blogs/new-openshift-cartridge-format-part-1)” by Mike McGrath [@Michael\_Mcgrath](https://twitter.com/Michael_McGrath) I set out to get a Red Hat Enterprise Linux image up and running. The quickest route to that was to spool up an AWS EC2 instance. 30 seconds later I had exactly that up and running. The next goal was to get Riak [installed and running on this instance](http://docs.basho.com/riak/latest/tutorials/installation/Installing-on-RHEL-and-CentOS/). I wasn’t going to actually build a cluster right off, but I wanted at least a single running Riak node to use for trying this out.

In the article “[New OpenShift Cartridge Format – Part 1](https://www.openshift.com/blogs/new-openshift-cartridge-format-part-1)” Mike skips the specifics of the cartridge and focuses on getting a service up and running that will be turned into a Cartridge. As Mike writes,

> What do we really need to do to create an new cartridge? Step one is to pick something to create a cartridge for.

…to which my answer is, “alright, creating a Cartridge for Riak!”  😉

However, even though I have the RHEL instance up and running already, with Riak installed, I decided I’d follow along with his exactly example too. So I dove in with

```bash
sudo yum install httpd
```

to install Apache. With that done I now have Riak & Apache installed on the RHEL EC2 instance. The goal with both of these services is to get them running as the regular local Unix user in a home directory.

With both Riak and Apache installed, time to create a local user directory for each of the respective tools. However, before that, with this version of Linux on AWS we’ll need to create a local user account.

```bash
useradd -c "Adron Hall" adron
passwd adron

Changing password for user adron.
New password:
Retype new password:
passwd: all authentication tokens updated successfully.
```

Next I switched to the user I created ‘su adron’ and created the following directories in the home path for attempting to get Apache and Riak up and running locally like this. I reviewed the rest of the steps in making the Cartridge w/ Apache and then immediately started running into a few issues with getting Riak setup just like I need it to be able to build a cartridge around it. At least, with my first idea of how I should build a cartridge.

At this point I decided we need to have a conversation around the strategy here. So Bill Decoste, Ryan and some of the other Red Hat team on hand today. After a discussion with Bill it sounds like there are some possibilities to get Riak running via the OpenShift Origin Cartridges.

**The Strategy**

The plan now is to get a cartridge setup so that the cartridge can launch a single Riak instance. That instance, then with post-launch scripts can then join itself to the overall Riak cluster. The routing can be done via the internal routing and some other capabilities that are inherent to what is in OpenShift itself. It sounds like it’ll take a little more tweaking, but the possibility is there for the near future.

At this point I sat down and read up on the Cartridge a little more before taking off for the day. Overall a good start and interesting to get an overview of the latest around OpenShift.

Thanks to the Red Hat Team, have a great time at the OpenStack Conference and I’ll be hacking on this Cartridge strategy!

**References**

- [Introduction to Cartridge Building](https://www.openshift.com/wiki/introduction-to-cartridge-building)
- [New OpenShift Cartridge Format – Part 1](https://www.openshift.com/blogs/new-openshift-cartridge-format-part-1)
- [New OpenShift Cartridge Format – Part 2](https://www.openshift.com/blogs/new-openshift-cartridge-format-part-2)
- [How to Write a Cartridge for OpenShift Origin Cartridge 2.0](https://github.com/openshift/origin-server/blob/master/node/README.writing_cartridges.md)
- [Installing Riak on RHEL or CentOS](http://docs.basho.com/riak/latest/tutorials/installation/Installing-on-RHEL-and-CentOS/)
