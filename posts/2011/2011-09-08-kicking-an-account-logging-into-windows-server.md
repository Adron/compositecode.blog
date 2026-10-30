---
title: Kicking An Account, Logging Into Windows Server
date: 2011-09-08 01:16:00 -0700
last_modified_at: 2011-09-07 14:29:00 -0700
permalink: /2011/09/08/kicking-an-account-logging-into-windows-server/
slug: kicking-an-account-logging-into-windows-server
wp_id: 3685
original_url: https://compositecode.blog/2011/09/08/kicking-an-account-logging-into-windows-server/
categories:
- How-to
tags:
- rdc
- remote
- remote desktop connection
excerpt: Yesterday I had to get logged into a Windows Server, however the connections were all consumed already. I had to kick somebody. I’d never done this via the command line, so I pinged a coworker who laid out how to lay low the over-connected users. With two simple commands I was logged in and running! To see who is logged into a server… 1 qwinsta -server theServerNameHere …and then to kick the users by their ID as shown by the query command above… 1 rwinsta -server theServerNameHere ID# …and you can now access the server via Remote Desktop Connection. Have fun with your new found connection powers!
---

Yesterday I had to get logged into a Windows Server, however the connections were all consumed already. I had to kick somebody. I’d never done this via the command line, so I pinged a coworker who laid out how to lay low the over-connected users. With two simple commands I was logged in and running!

To see who is logged into a server…

```bash
qwinsta -server theServerNameHere
```

…and then to kick the users by their ID as shown by the query command above…

```bash
rwinsta -server theServerNameHere ID#
```

…and you can now access the server via Remote Desktop Connection. Have fun with your new found connection powers! 🙂
