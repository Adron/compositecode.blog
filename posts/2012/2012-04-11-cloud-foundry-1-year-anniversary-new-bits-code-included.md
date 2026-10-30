---
title: Cloud Foundry 1 Year Anniversary & New Bits (Code Included)
date: 2012-04-11 15:15:07 -0700
last_modified_at: 2012-04-11 15:15:07 -0700
permalink: /2012/04/11/cloud-foundry-1-year-anniversary-new-bits-code-included/
slug: cloud-foundry-1-year-anniversary-new-bits-code-included
wp_id: 5417
original_url: https://compositecode.blog/2012/04/11/cloud-foundry-1-year-anniversary-new-bits-code-included/
categories:
- Cloud Speak
- Platform (as a Service)
tags:
- bosh
- cloudfoundry
- iaas
- paas
excerpt: Today was the 1 year anniversary for the Cloud Foundry Open Source PaaS Project. For info on what PaaS is, especially related to open source and related to Cloud Foundry check out my 5 part series at New Relic’s Blog; Part 1, Part 2, Part 3.1, Part 3.14159265, Part 4, and Part 5 (which I …
---

[![](/images/adronhall.smugmug.com/Software/Software-Development/The-CloudFoundry-Story/i-zM8zbZR/0/S/cloudfoundry-S.png)](http://www.cloudfoundry.org)Today was the 1 year anniversary for the Cloud Foundry Open Source PaaS Project. For info on what PaaS is, especially related to open source and related to Cloud Foundry check out my 5 part series at New Relic’s Blog; [Part 1](http://blog.newrelic.com/2012/01/11/removing-the-operating-system-barrier-with-platform-as-a-service-paas-a-guest-post-from-adron-hall/), [Part 2](http://blog.newrelic.com/2012/01/26/removing-the-operating-system-barrier-with-platform-as-a-service-paas-part-2-a-guest-post-from-adron-hall/), [Part 3.1](http://blog.newrelic.com/2012/02/08/noops-appops-devops-more-removing-the-os-barrier-with-paas-part-3/), [Part 3.14159265](http://blog.newrelic.com/2012/02/17/node-js-asp-net-sinatra-rails-java-the-list-goes-on-removing-the-os-barrier-with-paas-part-3-14159265/), [Part 4](http://blog.newrelic.com/2012/02/23/cloud-foundry-architecture-removing-the-os-barrier-with-paas-part-4/), and [Part 5](http://blog.newrelic.com/2012/03/08/the-finale-of-removing-the-os-barrier-with-paas-part-5/) (which I know, it is really a 6 part series).

**Updates, Updates, and More Updates!**

Today was pretty cool and jam packed with code & information. There are a load of updates in the [Cloud Foundry Repository](https://github.com/cloudfoundry) now.

One of the big parts of the new features released today, isn’t so much a feature, but an entire open source project based around actually building & deploying an entire Cloud Foundry PaaS Environment called [BOSH](https://github.com/cloudfoundry/bosh). Here’s my takeaway notes about this project, what it does, and how it can help Cloud Foundry usage.

**[BOSH](https://github.com/cloudfoundry/bosh.git) (<https://github.com/cloudfoundry/bosh.git>)**

The first thing to do, when learning about and using BOSH is to hit the groups:

- [BOSH Users Group](https://groups.google.com/a/cloudfoundry.org/group/bosh-users/topics)
- [BOSH Developers](https://groups.google.com/a/cloudfoundry.org/group/bosh-dev/)
- and [VCAP Dev](https://groups.google.com/a/cloudfoundry.org/group/vcap-dev/) if you want to follow the Cloud Foundry Development too.

***What is it?***

BOSH is a [YAML](http://en.wikipedia.org/wiki/YAML) based Cloud Foundry deployment tool. It provides a way to deploy a multiple image machine into a new Cloud Foundry environment. These images, just basic VMs, are referred to in the BOSH System as Stem Cells.

There is more to learn about BOSH, but for now suffice it to say there is some serious potential in what it enables for building out a Cloud Foundry Environment. Up until now this process was a manual installation effort which would take take a lot of energy and take an long time.

**Cloud Foundry Additions?**

There are a lot of Cloud Foundry changes that are in the works and a lot that went in. However, from an external point of view, there isn’t a lot of visible changes. No new user interface or anything like that. The biggest changes have been around stability, scaling, deployment, and other core capabilities.

For further information and news on the release, check out some of these write ups:

- <http://siliconangle.com/blog/2012/04/11/cloud-foundry-team-announces-new-deployment-tool-called-bosh/>
- <http://www.marketwire.com/press-release/cloud-foundry-ecosystem-celebrates-first-anniversary-nyse-vmw-1642701.htm>
- <http://www.zdnet.com/blog/open-source/vmware-cloud-foundry-paas-will-be-the-linux-of-the-cloud/10754>
- <http://www.zdnet.com/blog/btl/vmware-cto-describes-cloud-foundry-as-linux-of-the-cloud/73865?tag=mantle_skin;content>
- <http://www.eweek.com/c/a/Application-Development/VMwares-Cloud-Foundry-Celebrates-First-Anniversary-651422/>

***Cloud 9 IDE ROCKS!***

Outside of the [Cloud Foundry Project](http://www.cloudfoundry.net) there are other things working toward interoperability with Cloud Foundry and building in features that will help you work against Cloud Foundry. One of those companies is [Cloud 9](http://c9.io/). They’ve enabled [single-click deployment via their Cloud 9 IDE](http://servicesangle.com/blog/2012/04/11/cloud9-ide-announces-one-click-node-js-deploys-to-cloud-foundry/).

That’s it from me for now. I’ll have a lot more regarding [Cloud Foundry](http://www.cloudfoundry.org), [Iron Foundry](http://www.ironfoundry.org), and other projects related to PaaS soon.
