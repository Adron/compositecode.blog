---
title: TFS Frustration, Returning to Subversion
date: 2007-09-02 10:35:00 +0000
last_modified_at: 2007-09-02 10:35:00 +0000
permalink: /2007/09/02/tfs-frustration-returning-to-subversion/
slug: tfs-frustration-returning-to-subversion
wp_id: 430
original_url: https://compositecode.blog/2007/09/02/tfs-frustration-returning-to-subversion/
categories:
- Uncategorized Bits
tags: []
excerpt: After almost a year of frustration with personal and professional projects utilizing TFS (Team Foundation Server), I have decided to return my personal projects to Subversion. The time, effort, and the costs are far to high for me to use TFS on my personal projects. It is somewhat sad, as the potential with TFS is …
---

After almost a year of frustration with personal and professional projects utilizing TFS (Team Foundation Server), I have decided to return my personal projects to [Subversion](http://subversion.tigris.org/).  The time, effort, and the costs are far to high for me to use TFS on my personal projects.  It is somewhat sad, as the potential with TFS is massive, but the core element, the source control, has failed me too many times and ate up too much time for me at this point.

With that in mind, I present my most recent re-diving into [Subversion](http://subversion.tigris.org/) for my source control.  I’ll be giving TFS another go in a few months, especially when VS 2008 and SQL Server 2008 are released, but for now it is good ole’ reliable Subversion.

To get Subversion up and running nice and quick like, follow these turbo boosted instructions.

First download the following:

1. Head over to the main [Subversion](http://subversion.tigris.org/) site at [Tigris](http://www.tigris.org/) and download the latest copy of [Subversion](http://subversion.tigris.org/).
   [![](/photos/random_screen_captures_and_other_assorted_stuff/images/5260/original.aspx)](http://subversion.tigris.org/)- After that I grabbed a download of the latest [TortoiseSVN](http://tortoisesvn.tigris.org/) for Explorer Integration.
     [![](/photos/random_screen_captures_and_other_assorted_stuff/images/5261/original.aspx)](http://tortoisesvn.tigris.org/)- Last I picked up [ankhsvn](http://ankhsvn.tigris.org/) also on [Tigris](http://www.tigris.org/).  If you want to keep up with happenings for ankhSVN check out [Arild Fines Blog](http://arildf.spaces.live.com/).
       [![](/photos/random_screen_captures_and_other_assorted_stuff/images/5262/original.aspx)](http://svn1clicksetup.tigris.org/)

Once those are downloaded get to installing.  An even faster way to setup [Subversion](http://subversion.tigris.org/) and [TortoiseSVN](http://tortoisesvn.tigris.org/) is also available via [SVN-1](http://svn1clicksetup.tigris.org/).  It is a single click install basically, well that’s how it’s advertised but there are some extremely easy steps that need clicked through.  If you want to use this instead of installing the items separately that is fine, just make sure to grab [ankhSVN](http://ankhsvn.tigris.org/) above to follow the rest of the steps.  I personally like to install the packages separately so that I am intimately familiar with what is and is not actually being installed.

1. Install [Subversion](http://subversion.tigris.org/).- Install [TortoiseSVN](http://tortoisesvn.tigris.org/).- Install [ankhSVN](http://ankhsvn.tigris.org/).

With those installed it is now time to setup the repository and get some source code under source control.  The following instructions are also shown in this video.

1. Create a new directory, ideally something like *SubversionRepository* so it is easy to tell what the directory is for.- Right click on the newly created folder and select “Create Repository Here”.- A prompt will come up asking to choose either “Native File System (FSFS)” or “Berkeley database(BDB).  I always choose the native file system.  When complete you will receive a dialog that states, “The Repository was successfully created.”- I always check the repository, just to make sure I had everything clicked on correctly.  In the repository directory you should see the following folders;  conf, dav, db, hooks, locks, and the following files;  format and README.txt.  DO NOT PUT THINGS IN THIS DIRECTORY, JUST LEAVE IT AS IS!- To do a full import of items into the source repository navigate to the directory that has the project files in it.- Right click either on the root, or individual files and select “Tortoise SVN” and then the “Import” option.- A dialog will appear.  Enter the proper Url, the image has an example of a physical file location, and click “OK”.[![](/photos/random_screen_captures_and_other_assorted_stuff/images/5266/original.aspx)](/photos/random_screen_captures_and_other_assorted_stuff/category1102/picture5266.aspx)- Another dialog will come up to show the status of the files being imported.  When it finishes just click “OK” again.  The files and folders are now in the repository.- [![](/photos/random_screen_captures_and_other_assorted_stuff/images/5267/original.aspx)](/photos/random_screen_captures_and_other_assorted_stuff/category1102/picture5267.aspx)- Check out the drive space now, I do it with DiskView Visualizer since it’s ridiculously easy to get a view of space changes in a matter of seconds.  Now that you’ve added something there should be a few MB in the db directory, up from the default standard load db directory of about~100k or so.

[![](/photos/random_screen_captures_and_other_assorted_stuff/images/5268/original.aspx)](/photos/random_screen_captures_and_other_assorted_stuff/category1102/picture5268.aspx)

Now let’s say someone else needs to get a copy of the project folders to work with.  This is unbelievably easy, so don’t think it didn’t happen once you’ve done it once.

1. First right click anywhere in a folder, on a drive within the Windows Explorer.  On the right click menu “SVN Checkout…” should be available, select it.- The check out dialog should now appear.  Enter the information pertinent to your installation and project like what appears in the screen shot.  Click “OK” when you’ve entered all of the information.
     [![](/photos/random_screen_captures_and_other_assorted_stuff/images/5269/original.aspx)](/photos/random_screen_captures_and_other_assorted_stuff/images/5269/original.aspx)- If you haven’t created the check out directory you will be prompted by TortoiseSVN to create them.
       [![](/photos/random_screen_captures_and_other_assorted_stuff/images/5271/original.aspx)](/photos/random_screen_captures_and_other_assorted_stuff/category1102/picture5271.aspx)- Once the checkout is finished, you will be provided a dialog as shown in the following screen shot.  Click “OK”.
         [![](/photos/random_screen_captures_and_other_assorted_stuff/images/5273/original.aspx)](/photos/random_screen_captures_and_other_assorted_stuff/category1102/picture5273.aspx)- After all this you will see the directory that was added in the folder structure as displayed in the following screen shot.
           [![](/photos/random_screen_captures_and_other_assorted_stuff/images/5272/original.aspx)](/photos/random_screen_captures_and_other_assorted_stuff/category1102/picture5272.aspx)

My next Subversion Tutorial will cover some of the steps to update, check file differences, and commit changes back to the repository.  Stay tuned!  ![Smile [:)]](/emoticons/emotion-1.gif)

Technorati Tags: [TFS](http://technorati.com/tags/TFS), [Team Foundation Server](http://technorati.com/tags/Team%20Foundation%20Server), [Visual Studio](http://technorati.com/tags/Visual%20Studio), [Subversion](http://technorati.com/tags/Subversion), [Tortoise](http://technora
ti.com/tags/Tortoise), [ankh](http://technorati.com/tags/ankh), [SVN](http://technorati.com/tags/SVN)

del.icio.us Tags: [TFS](http://del.icio.us/popular/TFS), [Team Foundation Server](http://del.icio.us/popular/Team%20Foundation%20Server), [Visual Studio](http://del.icio.us/popular/Visual%20Studio), [Subversion](http://del.icio.us/popular/Subversion), [Tortoise](http://del.icio.us/popular/Tortoise), [ankh](http://del.icio.us/popular/ankh), [SVN](http://del.icio.us/popular/SVN)
