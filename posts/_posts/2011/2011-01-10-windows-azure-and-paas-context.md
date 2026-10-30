---
title: Windows Azure and the PaaS Context
date: 2011-01-10 05:41:35 -0800
last_modified_at: 2011-01-10 16:12:35 -0800
permalink: /2011/01/10/windows-azure-and-paas-context/
slug: windows-azure-and-paas-context
wp_id: 2051
original_url: https://compositecode.blog/2011/01/10/windows-azure-and-paas-context/
categories:
- Azure
- Cloud Speak
tags:
- azure
- cloud
- cloud computing
- microsoft
- paas
- platform as a service
excerpt: PaaS stands for Platform as a Service. The new concept around Devops* (Developer + Operations) has allowed cloud computing to reach an apex of agility for business. For developers PaaS provides an ultimately clean and agile experience around staging and deployment. PaaS is also the highest level of cost savings for most prospective enterprise and mid-size business users of the cloud computing services. Windows Azure has positioned itself with the vast majority of its services as a platform. Working with a platform, instead of an infrastructure based cloud computing service allows Devops to focus almost solely on the business problems. In addition this prevents an unnecessary staffing level for IT in most organizations. With staff re-focused on business problems and eliminating the majority of hardware issues in an organization costs go down while return on investment dramatically increases.
---

# PaaS stands for Platform as a Service.  The new concept around *Devops\* (Developer + Operations)* has allowed cloud computing to reach an apex of agility for business.  For developers PaaS provides an ultimately clean and agile experience around staging and deployment.  PaaS is also the highest level of cost savings for most prospective enterprise and mid-size business users of the cloud computing services.  Windows Azure has positioned itself with the vast majority of its services as a platform.

Working with a platform, instead of an infrastructure based cloud computing service allows Devops to focus almost solely on the business problems.  In addition this prevents an unnecessary staffing level for IT in most organizations.  With staff re-focused on business problems and eliminating the majority of hardware issues in an organization costs go down while return on investment dramatically increases.

**The Ideal PaaS Scenario, Athenaeum Corporation**

Imagine a company, I’ll call it Athenaeum Corporation that has around 250 people and provides a web based on demand service.  Right now they have 4 geographically dispersed data centers that incur real estate, staffing, energy, and other costs.  In each of those geographically dispersed data centers there are network switches and dedicated web servers connected to clustered with failover databases.  Each set of clustered databases is setup to replicate among all the geographically disperse locations everyday on a near real-time basis.  The website that these locations host is then balanced by load balancers, which also require maintenance and administration.

The headquarters of this company is located away from the data centers, but has a smaller duplicate data center of its own that also receives replicated data and hosts the website.  This is for internal and development purposes.  The development team consists of approximately 45 people out of the 250 staff.  The network operations staff is about 25 people, with internal IT making up another 15 people.  Altogether the direct support of development and operations is 85 people out of a 250 person staff.

At the headquarters are approximately 280 machines ranging from desktop PCs to Laptops.  These machines are used to support operations, sales, accounting, support, and every other part of the company.  These 280 machines are connected to approximately 60 internal servers that provide things like Exchange Services, file sharing directories, communications on instant messengers, Sharepoint services, and other IT related tools.  In addition there are other switches, cabling, and other items related to the routing, load balancing, and usage of these internal services.

The Athenaeum Corporation that I’ve described is a perfect scenario that could literally save hundreds of thousands of dollars with cloud computing services.  While saving that money they could possibly increase their physical service, better their uptime & system processing performance, and more just by migrating to the Windows Azure Platform.

Before jumping into how a company like the Athenaeum Corporation might jump into PaaS with the Windows Azure Platform, let’s take a quick review of the services that the Windows Azure Platform provides.

**The Platform of Windows Azure**

The core Windows Azure Platform is made up of compute and storage.  The compute is broken up into Web, Worker, and CGI Roles.  The storage is broken up into Table, Blob, and Queue services.  All of these features have a platform SDK that can be used or RESTful Web Service APIs.  From the basis of an operating system, it is abstracted away and only the platform is of concern to development.

Beyond the core compute and storage elements the Windows Azure Platform cloud has the Windows Azure AppFabric and the SQL Azure Relational Database for service bus, security access control, and storage of highly structured data.  The AppFabric is made up of two core features; the access control and the service bus.  The SQL Azure is really just a clustered, high end instance of SQL Server running with a hot swappable backup that is managed by Microsoft in their data centers.

The Windows Azure AppFabric is one of the features of Windows Azure Platform that makes working with on-premises, internal, disparate, and Windows Azure Platform or other cloud services easy.  With the AppFabric access control security, claims based identification, and other authentication mechanisms may be used for seemless single sign-on experiences.  With the systems secured with the access control, the AppFabric service bus can then be used as a way to manage and keep communication between those disparate systems flowing and active.  The AppFabric Access Control & Services Bus provides a way to incorporate any request to incorporate systems that a business enterprise, government, or other entity may have.

With SQL Azure, a hosted, high end solution to relational data storage needs is provided.  One big concern is that the data sizes are to 50GB in storage.  Although the there is this 50GB limit, once this size has been attained the data most likely should not be contained solely in a relational data store.  This is when the other Windows Azure Storage mediums come into play.  But for data under 50 GB, a relational data store setup to work seamlessly in Windows Azure like this provides additional platform capabilities for developers to port traditionally hosted applications into the cloud with minimal changes.

Now that the platform is covered, how would the Athenaeum Corporation move their system & website operations into the Windows Azure Platform for increased capabilities and decreased costs?  The first thing needed is a breakdown of the individual systems and interoperations.

1. Relational databases in each of the geographically dispersed data centers with failover databases.
2. Headquarters has 280 PCs and Laptops.
3. Headquarters has 60 internal IT maintained servers with custom applications, file-sharing, and other tools running on Windows Server.
4. Load balancing is done for the web based on demand services in house.
5. 4 Data Centers geographically dispersed with respective real estate, staffing, energy, and other costs.
6. Network operations requires approximately 25 staff for 24-hour a day operational uptime.
7. Web Based On Demand Services.

I’ll start breaking down these 7 key functionalities and state how the move to Windows Azure would change costing by using the platform.  Relational databases in each of these data centers can be moved in a couple different ways.

1. One is to move the databases into one single primary SQL Azure instance.  Since the databases are most likely located at each of the datacenters for location CDN reasons, it made sense before, but with the move to the cloud the Windows Azure CDN could be used and the database would likely have better access to the geographically dispersed web presence points.
2. The second is to move the databases to affinity points within the cloud that already match the current locations, porting the replication functionality for the specific data that each site needs.
3. The 280 PCs and Laptops would still need connectivity and access to all of the existing applications they have now.  The cloud changes little in regard to this situation.  However redundant machines could be removed and with the implementation of SaaS based solutions, which I’ll discuss further in the next section, would dramatically decrease the cost of machines that each employee would need along with a decrease in support, administration, and maintenance of the software they currently use.
4. The 60 internal servers at headquarters that IT maintains could be migrated completely, especially if they’re all running a Windows Operating System.  For anything that isn’t, one may want to look to AWS, Rackspace, or other virtualization solution at these cloud providers.  In Windows Azure internal servers hosting IIS applications could likely have them moved to Web or Worker Roles.  Anything such as Ruby on Rails, PHP, or Java that is hosted via IIS can be moved to a CGI Role in Windows Azure.  For anything that has other complexities and such can be installed on a Windows Azure VM Role.
5. Current in house load balancing can be eliminated entirely.  There is no need for in house management of this with a PaaS like the Windows Azure Platform.  So mark this off the cost list, it is included in the cost of the service and requires no configuration, management, or other interaction.
6. Each data center that previously provided geographic locations for the web presence can be brought into the Windows Azure Cloud.  There are two primary locations in North America at this time, and several more in other countries throughout the world.  With this ability the need to have 4 different data centers is removed.  In most cases, the centers that Windows Azure is located in also have significant security and penetration tests done at a physical level.  This effectively increases the security of each of the geographic access points.  Removing one more cost, while providing more for the money.
7. Network operations, effectively simplified by the removal of routing, load balancing, and other concerns that needed to be done in house.  The cloud offers 24x7x365 operational uptime.  This eliminates the need for the in house staffing, with only a 4-6 staff needed for this particular scenario.  The roles and requirements for the 4-6 staffing positions would primarily be there to maintain data, assure that systems that are custom are maintained and operational within the Windows Azure Cloud.
8. The last item is easily moved into the Windows Azure Platform using a Windows Azure Web Role.  This provides everything needed to operate a SaaS Web Application with the Windows Azure Portal PaaS.

On that last point of moving the Athenaeum Software into the Windows Azure Cloud, is SaaS on the Windows Azure Platform.
