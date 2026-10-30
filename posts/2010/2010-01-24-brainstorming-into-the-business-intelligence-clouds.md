---
title: Brainstorming Into the Business Intelligence Clouds
date: 2010-01-24 12:53:00 +0000
last_modified_at: 2010-01-24 12:53:00 +0000
permalink: /2010/01/24/brainstorming-into-the-business-intelligence-clouds/
slug: brainstorming-into-the-business-intelligence-clouds
wp_id: 685
original_url: https://compositecode.blog/2010/01/24/brainstorming-into-the-business-intelligence-clouds/
categories:
- Uncategorized Bits
tags: []
excerpt: Part II of my Business/Enterprise Intelligence Series, check out part 1. In the previous part of this ongoing series of getting the business intelligence and analytics pieces of the enterprise intelligence world figure out, I hit on the first step of the entire process. Collection of available data points. Not the desired data points, nice to …
---

Part II of my Business/Enterprise Intelligence Series, check out [part 1](/blogs/technology__software_development/post/2010/01/13/Where-Is-The-Other-Data-Tracking!-Where-Are-My-Acronyms!.aspx).

In the previous part of this ongoing series of getting the business intelligence and analytics pieces of the enterprise intelligence world figure out, I hit on the first step of the entire process. Collection of available data points. Not the desired data points, nice to haves, or might haves, but the available data points.

In this entry I will step past that and get into a little more of the technical depth of how these data points will be connected in the enterprise systems. More to the point, how they are not connected and will need to be in the enterprise.

**A Quick Review, The Systems**

> - Point Of Sale (POS) w/ 300+ stores
> - Webtrends Analytics tracking the Awe Widgets Inc Website
> - Internal Accounting Software (IAS)
> - In-house Built Customer Lists for Sales w/ Excel & Access

With the four systems we have a huge amount of actionable data points. So how do we connect all of these data points? That is the thorny question that comes up. Again, just like during the discovery of what data is available, we have a simple first step for this process.

**Figure out the origin and destination!**

That is really it. Of course, as anyone would concede, there is a lot in between. Without knowing where we are starting and where we need to end up though, finding the in between is in vain. Sure, one can make the mistake as many business intelligence projects do, and start building architecture before anyone knows or actually can use the architecture. This is a severe mistake, and I myself have literally seen millions of dollars get wasted only to have to start a project over, right in the middle of the original project. Do NOT become one of those projects, find the origin and destination!

In this case I am again, going to use my creative side and determine the operations of this company. Awe Widgets Incorporated is currently using SQL Server and has in house skills developed among their staff. That provides an easy option of moving towards SQL Server Reporting Services (SSRS) and working with SQL Server Integration Services (SSIS) for the ETL bits. Whatever other platforms are in between will be easily connected with these two tool stacks. So now I know my multiple originations, and my single point destination.

**Moving on to the fun bits.**

Now we have to figure out how we're going to get from our origination to our destination. This is where the trip becomes interesting. Just to make sure things stay clear, and list out what we have that we are working with.

|  |  |
| --- | --- |
| **Originations** | |
| Excel & Access (Office 2007) | \*.mdb, \*.xlsx, and \*.csv/\*.txt data stores |
| Internal Account Software (IAS) | This one is a prospective can of worms.  Proprietary layouts, de-normalized & normalized data, and all sorts of redundant, non-atomic data.  This sounds like an accounting package right?  :p |
| [Webtrends](http://www.webtrends.com) Analytics Data Exchange Web Services ([DX](http://developer.webtrends.com/community/dx/)) | Webtrends web services provide REST style architecture, with the ability for data to be retrieved in XML, JSON, HTML, or other formats (we can add more if need be, just let us know). |
| Point of Sale System (POS) | This system provides two daily exports, one at 6:00am and one at noon for processing.  The export format is \*.csv. |

|  |  |
| --- | --- |
| **Destination** | |
| SSIS & SSRS | SQL Server Integration Services used to connect SQL Server Reporting Services, with the core underlying data stored in SQL Server. |

So now we are starting to get somewhere.  We now where we are, what we have, and where we want to go.  Time to wire some things up, so stay tuned.  That will be in the next entry.  Also, if you are planning on attending Webtrends Engage in New Orleans, but sure to look up the Enterprise Intelligence session that I will be presenting with Heather Crince of Webtrends and Tony G. of Orbitz?

If you missed the previous entry in this series, check out [Where is the Other Data Tracking?!  Where are My Acronyms?!?!](/blogs/technology__software_development/post/2010/01/13/Where-Is-The-Other-Data-Tracking!-Where-Are-My-Acronyms!.aspx)
