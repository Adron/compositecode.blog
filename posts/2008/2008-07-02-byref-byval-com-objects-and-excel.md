---
title: ByRef, ByVal, COM Objects, and Excel
date: 2008-07-02 06:42:29 +0000
last_modified_at: 2008-07-02 06:42:29 +0000
permalink: /2008/07/02/byref-byval-com-objects-and-excel/
slug: byref-byval-com-objects-and-excel
wp_id: 273
original_url: https://compositecode.blog/2008/07/02/byref-byval-com-objects-and-excel/
categories:
- Uncategorized Bits
tags: []
excerpt: I’m working on getting things into and out of Excel. In one scenario I copy an Excel Range or Rows from one Excel Worksheet to a Worksheet in another Workbook. This Workbook then acts as a storage repository for the Range of Rows and is saved and closed. Each of these Range of Rows are …
---

I’m working on getting things into and out of Excel.  In one scenario I copy an Excel Range or Rows from one Excel Worksheet to a Worksheet in another Workbook.  This Workbook then acts as a storage repository for the Range of Rows and is saved and closed.  Each of these Range of Rows are saved with a unique identifier on the row above the copied in Range of Rows.

I then want to retrieve the Range of Rows to insert back into that Workbook’s Worksheet in another location.  I have an Excel Addin that provides a dialog box.  This dialog box goes through the Workbook’s Worksheet that is acting as a repository and retrieves each Range of Rows and provides a list based on the unique name in a dialog box.  The user can then click on the unique Range of Rows unique name and the idea is then to open the Range of Rows and copy them into the Worksheet the user is actually working in.

I had created a nice clean class object to put the “Range of Rows” in, but I’ve stumbled into a problem.  I can’t assign the Range object to a Range object in my domain class.  The problem being is the Range object is a bloody piece of @#$% COM object and won’t do a deep copy of the object itself.  So now I need to find some way to do a deep copy of the COM object or I have to open the Workbook’s Worksheet back up again and actually find again each Range of Rows that need to be pulled into the user’s Worksheet.

Overall, this is really ticking me off, the lack of operability and integration with the managed code base Microsoft works with .NET now is the polar opposite of the archaic and frustrating COM derived API of the Office Model.

If any Microsoftie’s are reading this, please, somebody get off the laurels and get this mess fixed.  The Office Model is impossible for all but the crudest of implementations and doing things “right” is almost completely removed from the options list.  Integrating the Office Model, especially with Microsoft’s Tech Stack of WCF, WF, WPF, and all that, is almost difficult to the point that you wouldn’t use Office for anything except if absolutely necessary.  Microsoft needs to fix this, open it up, get some clean API integration and improve the operability.

…and for the love of sanity Mr. Microsoft, practice what you preach and toss that COM @#$%.  It’s beyond frustrating dealing with unreliable COM objects and… well, I could rant for days about COM objects.

*If anybody has any ideas on the best way to work around this, shoot some comments at me.  Eventually I’ll figure out something ideal for this, but for now I’m stuck with a really nasty way to get back at the Range of Rows.*

Technorati Tags: [COM](http://technorati.com/tags/COM),[Microsoft](http://technorati.com/tags/Microsoft),[Office](http://technorati.com/tags/Office),[Excel](http://technorati.com/tags/Excel),[Object](http://technorati.com/tags/Object),[Range](http://technorati.com/tags/Range),[Row](http://technorati.com/tags/Row),[Worksheet](http://technorati.com/tags/Worksheet),[Workbook](http://technorati.com/tags/Workbook)

del.icio.us Tags: [COM](http://del.icio.us/popular/COM),[Microsoft](http://del.icio.us/popular/Microsoft),[Office](http://del.icio.us/popular/Office),[Excel](http://del.icio.us/popular/Excel),[Object](http://del.icio.us/popular/Object),[Range](http://del.icio.us/popular/Range),[Row](http://del.icio.us/popular/Row),[Worksheet](http://del.icio.us/popular/Worksheet),[Workbook](http://del.icio.us/popular/Workbook)
