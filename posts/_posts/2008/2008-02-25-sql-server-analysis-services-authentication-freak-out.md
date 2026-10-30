---
title: SQL Server Analysis Services Authentication Freak Out
date: 2008-02-25 05:45:12 -0800
last_modified_at: 2008-02-25 05:45:12 -0800
permalink: /2008/02/25/sql-server-analysis-services-authentication-freak-out/
slug: sql-server-analysis-services-authentication-freak-out
wp_id: 332
original_url: https://compositecode.blog/2008/02/25/sql-server-analysis-services-authentication-freak-out/
categories:
- Uncategorized Bits
tags: []
excerpt: '[Rant On] What is the deal really with the anti-user intuitive situation with analysis services when it decides that the data connection to a data source needs to use some arbitrary user authentication! I had my SSAS cube set to process against a nice normal authenticated account and somehow, someway it went and stuck some …'
---

[Rant On]

What is the deal really with the anti-user intuitive situation with analysis services when it decides that the data connection to a data source needs to use some arbitrary user authentication!  I had my SSAS cube set to process against a nice normal authenticated account and somehow, someway it went and stuck some completely unrelated user in the account login for the data source.  Now how is that supposed to help anything?

[Rant Off]

Needless to say, I’m looking forward to SQL Server 2008.  I hope it truly is cleaned up a good bit and as streamlined for cubes as I’ve been hearing.
