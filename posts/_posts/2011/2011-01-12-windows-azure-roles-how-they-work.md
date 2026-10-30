---
title: Windows Azure Web, Worker, and CGI Roles – How They Work
date: 2011-01-12 07:23:27 -0800
last_modified_at: 2011-01-12 18:16:32 -0800
permalink: /2011/01/12/windows-azure-roles-how-they-work/
slug: windows-azure-roles-how-they-work
wp_id: 2084
original_url: https://compositecode.blog/2011/01/12/windows-azure-roles-how-they-work/
categories:
- Architecture
- Azure
- Cloud Speak
tags:
- azure
- cloud
- cloud computing
- cloud storage
- paas
- web role
- web services
- windows azure
excerpt: 'This is a write up I’ve put together of how the roles in Windows Azure work. As far as I know, this is all correct – but if there are any Windows Azure Team Members out there that wouldn’t mind providing some feedback about specifics or adding to the details I have here – please do add comments! 🙂 Windows 2008 and Hyper-V Windows Azure is built on top of Windows 2008 & Hyper-V. Hyper-V provides virtualization to the various instance types and allocation of resources to those instances. Windows 2008 provides the core operating system functionality for those systems and the Windows Azure Platform Roles and Storage. The hypervisor that a Hyper-V installation implements does a few unique things compared to many of the other virtualization offerings in the industry. Xen (The Open Source Virtualization Software that Amazon Web Services use) & VMWare both use a shared resource model for utilization of physical resources within a system. This allows for more virtualized instances to be started per physical machine, but can sometimes allow hardware contention. On the other hand Hyper-V pins a particular amount of resources to a virtualized instance, which decreases the number of instances allowed on a physical machine. This enables Hyper-V to prevent hardware contention though. Both designs have their plusses and minuses and in cloud computing these design choices are rarely evident. The context however is important to know when working with high end computing within the cloud. Windows Azure Fabric Controller The Windows Azure Fabric Controller is kind of the magic glue that holds all the pieces of Windows Azure together. The Azure Fabric Controller automates all of the load balancing, switches, networking, and other networking configuration. Usually within an IaaS environment you’d have to setup the load balancer, static IP address, internal DNS that would allow for connection and routing by the external DNS, the switch configurations, configuring the DMZ, and a host of other configuration & ongoing maintenance is needed. With the Windows Azure Platform and the Fabric Controller, all of that is taken care of entirely. Maintenance for these things goes to zero. The Windows Azure Fabric Controller has several primary tasks: networking, hardware, and operating system management, service modeling, and life cycle management of systems. The low level hardware that the Windows Azure Fabric Controller manages includes switches, load balancers, nodes, load balancers, and other network elements. In addition it manipulates the appropriate internal DNS and other routing needed for communication within the cloud so that each URI is accessed seamlessly from the outside. The service modeling that the fabric controller provides is a to map the topology of services, port usage, and as mentioned before the internal communication within the cloud. All of this is done by the Fabric Controller without any interaction other than creating an instance or storage service within Windows Azure. The operating system management from the Fabric Controller involves patching the operating system to assure that security, memory and storage, and other integral operating system features are maintained and optimized. This allows the operating system to maintain uptime and application performance characteristics that are optimal. Finally the Fabric Controller has the responsibility for service life cycle. This includes updates and configuration changes for domains and fault domains. The Fabric Controller does so in a way to maintain uptime for the services. Each role is maintained in a way, by the Fabric Controller, that if the role stops responding it is recycled and a new role takes over. This can sometimes take several minutes, and is a core reason behind the 99.99% uptime SLA requiring two roles to be running. In addition to this the role that is recycled is rebuilt from scratch, thus destroying any data that would be stored on the role instance itself. This is when Windows Azure Storage plays a pivotal role in maintaining Windows Azure Cloud Applications.'
---

This is a write up I’ve put together of how the roles in Windows Azure work.  As far as I know, this is all correct – but if there are any Windows Azure Team Members out there that wouldn’t mind providing some feedback about specifics or adding to the details I have here – please do [add comments](/2011/01/12/windows-azure-roles-how-they-work/#comments)!  🙂

**Windows 2008 and Hyper-V**

Windows Azure is built on top of Windows 2008 & Hyper-V. Hyper-V provides virtualization to the various instance types and allocation of resources to those instances. Windows 2008 provides the core operating system functionality for those systems and the Windows Azure Platform Roles and Storage.

The hypervisor that a Hyper-V installation implements does a few unique things compared to many of the other virtualization offerings in the industry. Xen (The Open Source Virtualization Software that Amazon Web Services use) & VMWare both use a shared resource model for utilization of physical resources within a system. This allows for more virtualized instances to be started per physical machine, but can sometimes allow hardware contention. On the other hand Hyper-V pins a particular amount of resources to a virtualized instance, which decreases the number of instances allowed on a physical machine. This enables Hyper-V to prevent hardware contention though. Both designs have their plusses and minuses and in cloud computing these design choices are rarely evident. The context however is important to know when working with high end computing within the cloud.

**Windows Azure Fabric Controller**

The Windows Azure Fabric Controller is kind of the magic glue that holds all the pieces of Windows Azure together. The Azure Fabric Controller automates all of the load balancing, switches, networking, and other networking configuration. Usually within an IaaS environment you’d have to setup the load balancer, static IP address, internal DNS that would allow for connection and routing by the external DNS, the switch configurations, configuring the DMZ, and a host of other configuration & ongoing maintenance is needed. With the Windows Azure Platform and the Fabric Controller, all of that is taken care of entirely. Maintenance for these things goes to zero.

The Windows Azure Fabric Controller has several primary tasks: networking, hardware, and operating system management, service modeling, and life cycle management of systems.

The low level hardware that the Windows Azure Fabric Controller manages includes switches, load balancers, nodes, load balancers, and other network elements. In addition it manipulates the appropriate internal DNS and other routing needed for communication within the cloud so that each URI is accessed seamlessly from the outside.

The service modeling that the fabric controller provides is a to map the topology of services, port usage, and as mentioned before the internal communication within the cloud. All of this is done by the Fabric Controller without any interaction other than creating an instance or storage service within Windows Azure.

The operating system management from the Fabric Controller involves patching the operating system to assure that security, memory and storage, and other integral operating system features are maintained and optimized. This allows the operating system to maintain uptime and application performance characteristics that are optimal.

Finally the Fabric Controller has the responsibility for service life cycle. This includes updates and configuration changes for domains and fault domains. The Fabric Controller does so in a way to maintain uptime for the services.

Each role has at least one instance running. A role however can have multiple instances, with a theoretically limitless number. In this way, the Fabric Controller, if an instance stops responding is recycled and a new instance takes over. This can sometimes take several minutes, and is a core reason behind the 99.99% uptime SLA requiring two instances within a role to be running. In addition to this the instance that is recycled is rebuilt from scratch, thus destroying any data that would be stored on the role instance itself. This is when Windows Azure Storage plays a pivotal role in maintaining Windows Azure Cloud Applications.

**Web Role**

The Windows Azure Web Role is designed as a simply to deploy IIS web site or services hosting platform feature. The Windows Azure Web Role can provide hosting for any .NET related web site such as; ASP.NET, ASP.NET MVC, MonoRails, and more.

The Windows Azure Web Role is provides this service hosting with a minimal amount of maintenance required. No routing or load balancing setup is needed; everything is handled by the Windows Azure Fabric Controller.

Uses: Hosting ASP.NET, ASP.NET MVC, MonoRails, or other .NET related web site in a managed, high uptime, highly resilient, controlled environment.

**Worker Role**

A worker role can be used to host any number of things that need to pull, push, or run continuously without any particular input. A service role can be used to setup a schedule or other type of service. This provides a role dedicated to what could closely be compared to a Windows Service. The options and capabilities of a Worker Role however vastly exceed a simple Windows Service.

**CGI Role**

This service role is designed to allow execution of technology stacks such as Ruby on Rails, PHP, Java, and other non-Microsoft options.

**Windows Azure Storage**

Windows Azure Storage is broken into three distinct features within the service. Windows Azure provides tables, blob, and queue for storage needs. Any of the Windows Azure Roles can also connect to the storage to maintain data across service lifecycle reboots, refreshes, and any temporary loss of a Windows Azure Role.

*A note about Windows Azure Storage compared to most Cloud Storage Providers:*  None of the Azure Storage Services are “eventually consistent”. When a write is done, it is instantly visible to all subsequent readers. This simplifies coding but slows down the data storage mechanisms more than eventually consistent data architectures.

[![Shout it](http://dotnetshoutout.com/image.axd?url=http%3A%2F%2Fcompositecode.com%2F2011%2F01%2F12%2Fwindows-azure-roles-how-they-work%2F)](http://dotnetshoutout.com/Windows-Azure-Web-Worker-and-CGI-Roles-How-They-Work-Composite-Code)
