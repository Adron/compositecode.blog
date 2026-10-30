---
title: Windows Azure and the IaaS Context (or lack thereof)
date: 2011-01-06 05:15:21 -0800
last_modified_at: 2011-01-04 22:41:04 -0800
permalink: /2011/01/06/windows-azure-and-the-iaas-context-or-lack-thereof/
slug: windows-azure-and-the-iaas-context-or-lack-thereof
wp_id: 2047
original_url: https://compositecode.blog/2011/01/06/windows-azure-and-the-iaas-context-or-lack-thereof/
categories:
- Azure
- Cloud Speak
tags:
- azure
- cloud
- cloud computing
- iaas
- infrastructure as a service
- microsoft
- vm role
excerpt: Windows Azure has several primary competitors in the IaaS Realm, even though they aren’t technically an IaaS Cloud Provider at all. Some of these competitors in this space are Amazon Web Services (AWS), Rackspace, GoGrid and VMWare. Each of these providers offer virtual machines with either Windows or Linux Operating Systems, multiple data centers for …
---

# Windows Azure has several primary competitors in the IaaS Realm, even though they aren’t technically an IaaS Cloud Provider at all.  Some of these competitors in this space are Amazon Web Services (AWS), Rackspace, GoGrid and VMWare.  Each of these providers offer virtual machines with either Windows or Linux Operating Systems, multiple data centers for geographically dispersed access, dynamic scaling, and other features associated with hosting infrastructure in cloud computing.

Some of the more dedicated infrastructure services provide content delivery, routing, load balancing, virtualized instances, virtualized & dedicated private clouds, DNS routing, autoscaling at an infrastructure level and more.  Some of the providers and their respective services are listed below:

Amazon Web Services Infrastructure Services

- Amazon Cloudwatch enables Autoscaling.
- Amazon Cloudfront is a content delivery network (CDN).
- Amazon Route 53 for highly available and scalable DNS.
- Amazon Virtual Private Cloud (VPC) for secure bridges into on-premises computing.
- Elastic Load Balancing for distributing incoming application traffic.
- SQS, or Simple Queue Service for messaging.
- SNS, or Simple Notification Service for alerting.

Rackspace Infrastructure Services

- Content Delivery Network (CDN)
- Simple Load Balancing using virtualized server to provide load balancing.

GoGrid Infrastructure Services

- Content Delivery Network (CDN) with a boasted 18 points of presence on 4 continents.
- F5 Hardware Load Balancing
- Data Center specific provisioning.
- Autoscaling with Vertical RAM Scaling and more features.

**Pricing IaaS**

These companies offer a lower price point, which plays into the assumption that the user of the cloud services is skilled in setting up the needed networking, access, services, servers, and other things needed for each virtual machine launched within the respective cloud environment.  Some of the price points, especially in regards to Linux, are 1/3rd to 2/3rd the price of Windows Azure.

The Windows Azure advantage is at a higher price point, but lower total cost of ownership.  This advantage unfolds when operating in the dedicated development environment, but removing the networking and information technology arm of a company.  Basically, a company buys the cloud services from the grid just like they would the building power for their headquarters.  This leaves the generation of power, or simply the compute power, to a dedicated utility instead of having in house management of these resources.

**Infrastructure Services**

There are a number of companies in the technology industry today that offer infrastructure services.  Infrastructure services generally revolve around a few specific characteristics;

- Content Delivery
- Routing & Load Balancing
- Virtual or Dedicated Private Cloud
- Operating System Virtualized Instances

Windows Azure provides two primary infrastructure services.  Both of the services are somewhat minimal, since Windows Azure is focused on being a platform and not an infrastructure.  The service is the Windows Azure Content Delivery Network and the Windows Azure VM Role.

The content delivery network is provided as an add-on to the Windows Azure Storage to provide faster geographically dispersed access to data.  This increases the speed of access to the data and sties within the Windows Azure Cloud Platform.

**Windows Azure VM Role**

Windows Azure as marketed by Microsoft is not an infrastructure service.  However Microsoft has broken from being a pure platform only service with the Windows Azure VM Role.  The Windows Azure Platform is still primarily a platform service, but the VM Role has been provided with the intent of migrating customers that may need a full machine instance of Windows Server to run existing applications.  This enables an enterprise or other business to start migrating existing applications without a complete rewrite of those applications.

This enables the migration of applications that have long, non-scriptable, fragile installation steps to be moved into the Windows Azure Cloud Platform.  The VM Role does pose a possible distraction to developers, who should focus on developing applications against the Windows Azure Web or Service Roles.  This provides the greatest benefit and chance for savings over time.  In addition the roles are patched, and kept up to date by Windows Azure instead of needing hands on maintenance from the account holder or developers.

On a Windows Azure VM Role the operating system, updates, and other maintenance of the role are left up to the account holder.  Microsoft offers no automated patching or other support.  The VM Role must also be monitored by the account holder.  Windows Azure knows when the system becomes unresponsive but otherwise doesn’t act unless the system completely crashes, shuts down, or otherwise stops.

The VM Role is also advantageous when an account holder or developer needs elevated privileges for a particular application.  This however does not mean it is an encouraged practice to use elevated privileges for application development within Windows Azure.  But the VM Role offers the ability for those situations that are inflexible and require abrogation of good design principles.  This feature offers the ability to install MSIs, custom configure IIS, or otherwise manipulate the server environment for hosting needs.

One of the largest concerns with the VM Role is that the savings and decrease in maintenance associated with Windows Azure Platform managing the networking, load balancing, and other related infrastructure services.  The VM Role does not retain this automated level of management and at this time does not have load balancing or other features enabled.  Load balancing can be done externally to the Windows Azure Platform, but requires CNAME and custom DNS management in order to do so.
