---
title: 'T-SQL Date Range Usage :: Tip o'' The Day'
date: 2007-11-15 12:38:48 +0000
last_modified_at: 2007-11-15 12:38:48 +0000
permalink: /2007/11/15/t-sql-date-range-usage-tip-o-the-day/
slug: t-sql-date-range-usage-tip-o-the-day
wp_id: 395
original_url: https://compositecode.blog/2007/11/15/t-sql-date-range-usage-tip-o-the-day/
categories:
- Uncategorized Bits
tags: []
excerpt: Often times a date range is used in a where clause with a start date and an end date that are the same. The dates however are entered with the intention of getting that single day worth of data. By default T-SQL will look at that but not give you the full 24 hours worth …
---

Often times a date range is used in a where clause with a start date and an end date that are the same.  The dates however are entered with the intention of getting that single day worth of data.  By default T-SQL will look at that but not give you the full 24 hours worth of data.  To fix that, toss in an IF statement early in the query to check and fix this problem.  The code below is uber easy to just copy and paste into a SQL query for confirmation, then just alter for your custom needs.

DECLARE @EndDate datetime
DECLARE @StartDate datetime

SET @StartDate = ‘1/1/07’
SET @EndDate = ‘1/1/07’

PRINT ‘Start Date: ‘
PRINT @StartDate
PRINT ‘End Date: ‘
PRINT @EndDate

IF  DATEPART(hh, @EndDate) = 0 BEGIN
    SET @EndDate = DATEADD(hh, 23, @EndDate)
    SET @EndDate = DATEADD(mi, 59, @EndDate)
    SET @EndDate = DATEADD(ss, 59, @EndDate)
    SET @EndDate = DATEADD(ms, 99, @EndDate)
END

PRINT ‘Start Date: ‘
PRINT @StartDate
PRINT ‘End Date: ‘
PRINT @EndDate
