---
title: 'Finding A Week in T-SQL :: Tip o'' The Day'
date: 2007-12-04 06:15:47 +0000
last_modified_at: 2007-12-04 06:15:47 +0000
permalink: /2007/12/04/finding-a-week-in-t-sql-tip-o-the-day/
slug: finding-a-week-in-t-sql-tip-o-the-day
wp_id: 378
original_url: https://compositecode.blog/2007/12/04/finding-a-week-in-t-sql-tip-o-the-day/
categories:
- Uncategorized Bits
tags: []
excerpt: 'Recently I needed to identify a week within a T-SQL Query. First off I figured I would want to know what day it is, then I could easily figure out a week time frame. To verify what day you have selected, use the following code: IF DATENAME(weekday, ‘1/7/07’) = ‘Sunday’ BEGIN SELECT ‘Sunday’END ELSE SELECT …'
---

Recently I needed to identify a week within a T-SQL Query.  First off I figured I would want to know what day it is, then I could easily figure out a week time frame.

To verify what day you have selected, use the following code:

> IF DATENAME(weekday, ‘1/7/07’) = ‘Sunday’ BEGIN
>     SELECT ‘Sunday’
> END ELSE
>     SELECT ‘Not Sunday’

I created this check to verify that someone had entered the beginning of the week they wanted properly.  If it isn’t Sunday, they won’t get a proper week.  The key function above is the DATENAME.

Once I have the first day of the week figuring out the date range for the week is super easy.  I made a few modifications and added a select statement to print out the start and end date of the date range.

> DECLARE @StartDate smalldatetime
> DECLARE @EndDate smalldatetime
>
> SET @StartDate = ‘1/7/07’
>
> IF DATENAME(weekday, ‘1/7/07’) = ‘Sunday’ BEGIN
>     SET @EndDate = DATEADD(day, 7, @StartDate)
> END ELSE
>     SELECT ‘Not Sunday’
>
> SELECT @StartDate AS ‘Start Date’, @EndDate AS ‘End Date’

I’m working on some other things for this particular date calculating type of need, and will write up an entry based on that too.  One of the things I think would be a great addition to this function is to be able to enter any date and have the SQL give a week date range in return based on the closest week starting date.
