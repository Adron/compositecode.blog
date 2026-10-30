---
title: The Confusions of IaaS, PaaS, and SaaS
date: 2011-01-04 22:25:43 -0800
last_modified_at: 2011-01-04 22:25:43 -0800
permalink: /2011/01/04/the-confusions-of-iaas-paas-and-saas/
slug: the-confusions-of-iaas-paas-and-saas
wp_id: 2043
original_url: https://compositecode.blog/2011/01/04/the-confusions-of-iaas-paas-and-saas/
categories:
- Cloud Speak
tags:
- cloud
- cloud computing
- iaas
- infrastructure as a service
- paas
- platform as a service
- saas
- software as a service
excerpt: The Confusions of IaaS, PaaS, and SaaS IaaS, PaaS, and SaaS stand for Infrastructure as a Service, Platform as a Service, and Software as a Service respectively. But what exactly is the context & definition of each of these acronyms? The simple definitions I’ve included below. IaaS – A service provided by a company, group, community, or government that provides basic computer networking, load balancing, content delivery networks, routing, commodity data storage, and virtualized operating system hosting. PaaS – A service provided by a company, group, community, or government that provides a platform in which to develop software applications, usually web based, with immediate abstractions of the underlying infrastructure. SaaS – A service provided by a company, group, community, or government that provides a software solution to the system clients. The software may be internal to a business, delivered by other means, or most commonly delivered over the Internet.
---

# IaaS, PaaS, and SaaS stand for Infrastructure as a Service, Platform as a Service, and Software as a Service respectively.  But what exactly is the context & definition of each of these acronyms?  The simple definitions I have included below.

- **IaaS** – A service provided by a company, group, community, or government that provides basic computer networking, load balancing, content delivery networks, routing, commodity data storage, and virtualized operating system hosting.
- **PaaS** – A service provided by a company, group, community, or government that provides a platform in which to develop software applications, usually web based, with immediate abstractions of the underlying infrastructure.
- **SaaS** – A service provided by a company, group, community, or government that provides a software solution to the system clients.  The software may be internal to a business, delivered by other means, or most commonly delivered over the Internet.

IaaS, PaaS, and SaaS are heavily used acronyms in the cloud computing industry.  These three acronyms describe services in particular, but not cloud computing specifically.  It just happens that cloud computing is often broken down into these three segments.  From here on though, I will use IaaS, PaaS, and SaaS in relation to cloud computing.

Windows Azure is highly focused around being a platform.  It has often been said internally and externally at Microsoft that Windows Azure is not infrastructure or software that you can buy, but a platform that software is built to without a need to think about the infrastructure.  Recent events and changes have cast a shadow of doubt on Microsoft’s intentions toward the infrastructure and services aspect of this.  I’ll cover more specifics as I break these services apart.

Traditionally, and even today and ongoing tomorrow, there are a number of existing infrastructure, platforms, and software solutions that are provided in the context of IaaS, PaaS, and SaaS.  These solutions are not always cloud technologies, and can be provided in a number of ways.  Let’s break out the three into the traditional environments that would provide these services.

**Traditional Infrastructure**

Traditionally infrastructure was, and still today, often provided to companies internally and by 3rd party providers.  These providers, such as small businesses or internal IT Departments, would deliver actual hardware including cabling, architectural design, network configuration & setup, load balancing, hosting of physical servers, data storage in arrays, and other services.  Some examples would be a traditional RAID array with multiple disks, and storing dedicated single copy data as a backup on that array.  Another is documents stored on a file server and backed up to a tape drive.

For further context, take this working example of a very common infrastructure scenario.  An industrial company that makes, manages, and operates the manufacturing of widget X.  The company has a primary office space in an office building in a major metropolitan area.  In that office there are approximately 90 employees.  There is a satellite office with another 25 employees in another part of the city, located about 6 miles from the main office.  These two offices have a combined total of 115 PCs & Laptops.  These machines are interconnected on a network that connects to a collocation facility where the servers are stored & connected to a large pipe on the Internet.  This collocation facility provides the access for all customers via the Internet and also all the access for employees to their internal servers.

In this example we have a number of systems & networking interconnects needed for day to day operations.  This is a very common, and often a rather complex array of services.  This scenario is one that requires a moderate need for Internet infrastructure, but needs mount for file sharing, backups, redundancies, a the ability to startup new servers easily for usage, testing, development, or day to day operations.  The purchase cycle for additional hardware to bulk up this infrastructure isn’t measured in minutes, but is measured in days, weeks, and all too commonly months.

Take another example using a software game company.  This company traditionally delivers games via boxed medium to stores like Target, Wal-mart, or Gamestop.  The game shop is primarily located in a single office with 45 employees.  They have Internet access that connects them to their partners that handle graphics rendering compute time, e-mail & communication server hosting, & other sources.  The backup and storage for their work is on-premises with tape backups, file servers in building, and other equipment for the day to day operations of game development.

This company has needs for a large pipe to their rendering farm partners.  The file servers are local and also require a fair sized pipe to the workstations and huge disks for storing rendered images.  The rendering farm partners have appropriate networking connections on their end for uploading and downloading of their content to this company.  At the end of the development cycle when the game is ready for release they send off the gold copy of the build to manufacturing which is also in another geographic location.  This company then prints the boxes & discs and sends the game out through logistical distribution companies to the stores that will sell the product.

**A Traditional Platform**

Traditionally a platform was something that consisted of Ruby on Rails, the .NET Framework, Java Server Pages, or PHP.  One had to be responsible for the deployment of these platforms to infrastructure, and all the configuration, maintenance patches, updates, software installation, and other work required staffing at appropriate levels to handle the workload.  The .NET Framework is an example of developing to a platform, and then installing Windows Server (or running it on Mono under Linux), setting up the IIS Server on Windows, then appropriately installing updates, patches, fixes, and other pieces of software.

A great example of real world platform usage is alive in almost all companies to some degree.  Take Visual Basic for Office as an example.  This is often used in offices that have no dedicated development teams, nor any real trained developers.  Visual Basic for Office allowed almost anyone to get up to speed and use very simple programming concepts to get something built using the Microsoft Office Suite as the platform.

A great scenario, and extremely common, is a mid-size enterprise at approximately 170 employees.  In the main office there are a number of people in accounting, sales, support, logistics, marketing, advertising, and other departments.  Each of these departments often have custom needs to deal with their specific business needs within the enterprise.  Sales may want to have an ongoing list of customer contacts and their relation to particular sales people, so one of the sales guys hacks together a solution with Microsoft Office Access.  The next thing everyone in sales is using it.  Going beyond that someone in accounting figures out some cool tricks with Visual Basic for Applications and builds a way to keep in progress work in balance to simplify the daily tracking of numbers.  Again, the next step is other people in the department start using that same application.  Visual Basic for Applications, and the later incarnation Visual Studio Tools for Office is a great example of a software suite that had a platform built on it.

Another common scenario is the business that has grown to about 320 people and starts to migrate some of the rogue databases or custom Visual Basic for Application tweaks into applications that can be formalized and setup for use more easily within the enterprise.  Visual Studio and SQL Server are purchased and development work begins on the .NET Framework to codify these solutions.

The last example is one of the newer platforms out today.  Ruby on Rails started out as a platform to build on that did things in a very simple, minimalistic, rapid manner.  Development was started on the platform by people that eventually formed 37signals.com and built the tools that company sells; Basecamp, Highrise, Backpack, and Campfire.  The Ruby on Rails Platform makes web development faster and easier than it ever has been with traditional software platforms.  It has had such a huge impact that Microsoft has even released competing offerings such as ASP.NET MVC to counter the development patterns and style of the Ruby on Rails patterns.  This platform has some notable applications including Twitter, Yellowpages, Scribd, Hulu, Slideshare, Medhelp, Github, Odeo, Jango, Ravelry, MTV Style and many more.

**A Traditional Software Solution**

This is the point of all the other layers, the ability to provide software that clients can use to complete daily work, communicate, and create solutions for their business needs.  This traditionally has been provided by installing tools like Microsoft Office, Visual Studio, WordPerfect, Lotus, or other software packages.

This is probably the easiest service type of the “as a Service” differentiations to describe.  It is what is commonly seen by end users.

One of the most common software solutions that is used throughout the world is the Office Suite.  Microsoft’s Office Suite being the most common at this time.  Another great example of a software package commonly used is CAD & Photoshop.  There are literally thousands of other software offerings that are used at home, in the enterprise, or in small businesses every day.
