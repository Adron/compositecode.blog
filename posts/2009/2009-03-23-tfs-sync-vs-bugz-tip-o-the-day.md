---
title: 'TFS Sync & VS Bugz :: Tip o'' The Day'
date: 2009-03-23 07:08:04 +0000
last_modified_at: 2009-03-23 07:08:04 +0000
permalink: /2009/03/23/tfs-sync-vs-bugz-tip-o-the-day/
slug: tfs-sync-vs-bugz-tip-o-the-day
wp_id: 605
original_url: https://compositecode.blog/2009/03/23/tfs-sync-vs-bugz-tip-o-the-day/
categories:
- Uncategorized Bits
tags: []
excerpt: 'If you receive this error, “TF31005: Team Foundation cannot retrieve the list of team projects because it cannot connect to Team Foundation Server”, or if you are debugging and the code you see on screen is not what is being stepped through or you see VS stepping through white space lines, try this out. Clear …'
---

If you receive this error, “TF31005: Team Foundation cannot retrieve the list of team projects because it cannot connect to Team Foundation Server”, or if you are debugging and the code you see on screen is not what is being stepped through or you see VS stepping through white space lines, try this out.

Clear out the cache here on Vista…

```
C:\Users\userName\AppData\Local\Microsoft\Team Foundation\2.0\Cache
```

.csharpcode, .csharpcode pre
{
font-size: small;
color: black;
font-family: consolas, “Courier New”, courier, monospace;
background-color: #ffffff;
/\*white-space: pre;\*/
}
.csharpcode pre { margin: 0em; }
.csharpcode .rem { color: #008000; }
.csharpcode .kwrd { color: #0000ff; }
.csharpcode .str { color: #006080; }
.csharpcode .op { color: #0000c0; }
.csharpcode .preproc { color: #cc6633; }
.csharpcode .asp { background-color: #ffff00; }
.csharpcode .html { color: #800000; }
.csharpcode .attr { color: #ff0000; }
.csharpcode .alt
{
background-color: #f4f4f4;
width: 100%;
margin: 0em;
}
.csharpcode .lnum { color: #606060; }

…or try clearing out this directory on XP/Server 2003.

```
C:\Documents and Settings\userName\Local Settings\Application Data\Microsoft\Team Foundation\2.0\Cache
```

.csharpcode, .csharpcode pre
{
font-size: small;
color: black;
font-family: consolas, “Courier New”, courier, monospace;
background-color: #ffffff;
/\*white-space: pre;\*/
}
.csharpcode pre { margin: 0em; }
.csharpcode .rem { color: #008000; }
.csharpcode .kwrd { color: #0000ff; }
.csharpcode .str { color: #006080; }
.csharpcode .op { color: #0000c0; }
.csharpcode .preproc { color: #cc6633; }
.csharpcode .asp { background-color: #ffff00; }
.csharpcode .html { color: #800000; }
.csharpcode .attr { color: #ff0000; }
.csharpcode .alt
{
background-color: #f4f4f4;
width: 100%;
margin: 0em;
}
.csharpcode .lnum { color: #606060; }

This should get the ball rolling for Visual Studio & TFS Synchronization again.

UPDATE:  This thing kept nagging me throughout the day until Denis (coworker) finally got into the logs and found this “*Invalid length parameter passed to the SUBSTRING function*“.  This occurs, usually, right after a SP1 upgrade on the TFS Server.  After poking around a while Denis found this [KB](http://support.microsoft.com/kb/967138).  After running a simple update statistics…

```
use tfsintegration

update statistics tbl_security_identity_cache
```

.csharpcode, .csharpcode pre
{
font-size: small;
color: black;
font-family: consolas, “Courier New”, courier, monospace;
background-color: #ffffff;
/\*white-space: pre;\*/
}
.csharpcode pre { margin: 0em; }
.csharpcode .rem { color: #008000; }
.csharpcode .kwrd { color: #0000ff; }
.csharpcode .str { color: #006080; }
.csharpcode .op { color: #0000c0; }
.csharpcode .preproc { color: #cc6633; }
.csharpcode .asp { background-color: #ffff00; }
.csharpcode .html { color: #800000; }
.csharpcode .attr { color: #ff0000; }
.csharpcode .alt
{
background-color: #f4f4f4;
width: 100%;
margin: 0em;
}
.csharpcode .lnum { color: #606060; }

…all was running flawlessly after that.  Only an 8 hour day lost.  🙁  But hey!  At least this helps somebody out there!
