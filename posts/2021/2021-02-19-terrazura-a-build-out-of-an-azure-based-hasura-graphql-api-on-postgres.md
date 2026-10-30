---
title: Terrazura – A Build Out of an Azure based, Hasura GraphQL API on Postgres
date: 2021-02-19 13:46:57 -0800
last_modified_at: 2022-04-01 11:21:18 -0700
permalink: /2021/02/19/terrazura-a-build-out-of-an-azure-based-hasura-graphql-api-on-postgres/
slug: terrazura-a-build-out-of-an-azure-based-hasura-graphql-api-on-postgres
wp_id: 63494
original_url: https://compositecode.blog/2021/02/19/terrazura-a-build-out-of-an-azure-based-hasura-graphql-api-on-postgres/
categories:
- Azure
- Databases
- graphql
tags:
- api
- azure
- devops
- graphql
- graphql api
- programming
- terraform
excerpt: I created this repo https://github.com/Adron/terrazura​ during a live stream on my Twitch Thrashing Code Channel 🤘 at 10am on the 30th of December, 2020. The VOD is now available on my YouTube Thrashing Code Channel https://youtube.com/thrashingcode​ . A rough as hell year, but wanted to wrap it up with some solid content. In this stream I …
image: /wp-content/uploads/2021/02/Terrazura.png
---

I created this repo [https://github.com/Adron/terrazura​](https://github.com/Adron/terrazura) during a live stream on my Twitch Thrashing Code Channel 🤘 at 10am on the 30th of December, 2020. The VOD is now available on my YouTube Thrashing Code Channel [https://youtube.com/thrashingcode​](https://youtube.com/thrashingcode%E2%80%8B). A rough as hell year, but wanted to wrap it up with some solid content. In this stream I tackled a ton of specifics, in detail about getting Hasura deployed in Azure, Postgres backed, a database schema designed and created, using database schema migrations, and all sorts of tips n’ tricks along the way. 3 hours of solid how to get shit done material!

For live streams, check out and follow at [https://www.twitch.tv/thrashingcode​](https://www.twitch.tv/thrashingcode%E2%80%8B) 👊🏻 or for VOD viewing check out <https://youtube.com/thrashingcode>

[![](/wp-content/uploads/2021/02/CleanShot-2021-02-19-at-13.56.22.png)](https://youtu.be/7glsC88h2Ss)

*A point in coding during the video!*

[02:49](https://youtu.be/7glsC88h2Ss/watch?v=7glsC88h2Ss&t=169s)​ – Shout out to the stream sponsor, Azure, and links to some collateral material.
[14:50](https://youtu.be/7glsC88h2Ss/watch?v=7glsC88h2Ss&t=890s)​ – In this first segment, I start but run into some troubleshooting needs around the provider versions for Terraform in regards to Azure. You can skip this part unless you want to see what issue I ran into.
[18:24](https://youtu.be/7glsC88h2Ss/watch?v=7glsC88h2Ss&t=1104s)​ – Since I ran into issues with the current version of Terraform I had installed, at this time I show a quick upgrade to the latest version.
[27:22](https://youtu.be/7glsC88h2Ss/watch?v=7glsC88h2Ss&t=1642s)​ – After upgrading and fighting through trial and error execution of Terraform until I finally get the right combination of provider and Terraform versions.
[27:53](https://youtu.be/7glsC88h2Ss/watch?v=7glsC88h2Ss&t=1673s)​ – Adding the first Terraform resource, the Azure resource group.
[29:47](https://youtu.be/7glsC88h2Ss/watch?v=7glsC88h2Ss&t=1787s)​ – Azure Portal oddness, just to take note off if/when you’re working through this. Workaround later in the stream.
[32:00](https://youtu.be/7glsC88h2Ss/watch?v=7glsC88h2Ss&t=1920s)​ – Adding the Postgres server resource.
[44:43](https://youtu.be/7glsC88h2Ss/watch?v=7glsC88h2Ss&t=2683s)​ – In this segment I switched over to Jetbrain’s Intellij to do the rest of the work. I also tweak the IDE to re-add the plugin for the material design themes and icons. If you use this IDE, it’s very much IMHO worth getting this to switch between themes.
[59:32](https://youtu.be/7glsC88h2Ss/watch?v=7glsC88h2Ss&t=3572s)​ – After getting leveled-up with the IDE, I wrap up the [#Postgres](https://dev.to/hashtag/postgres)​ server resource and [#terraform](https://dev.to/hashtag/terraform)​ apply it the overall set of resources. At this point I also move forward with the infrastructure as code, with emphasis on additive changes to the immutable infrastructure by emphasizing use of `terraform apply` and minimizing any `terraform destroy` use.
[1:02:07](https://youtu.be/7glsC88h2Ss/watch?v=7glsC88h2Ss&t=3727s)​ – At this time, I try figuring out the portal issue by `az logout` and logging back in `az login` to Azure Still no resources shown but…
[1:08:47](https://youtu.be/7glsC88h2Ss/watch?v=7glsC88h2Ss&t=4127s)​ – eventually I realize I have to use the hack solution of pasting the subscription ID into the
@Azure portal to get resources for the particular subscription account which seems highly counter intuitive since its the ONLY account. 🧐
[1:22:54](https://youtu.be/7glsC88h2Ss/watch?v=7glsC88h2Ss&t=4974s)​ – The next thing I setup, now that I have variables that need passed in on every `terraform` execution, I add a script to do this for me.
[1:29:35](https://youtu.be/7glsC88h2Ss/watch?v=7glsC88h2Ss&t=5375s)​ – Next up is adding the database to the database server and firewall rule. Also we get to see Jetbrains [#Intellij](https://dev.to/hashtag/intellij)​ HCL plugin introspection at work adding required properties to the firewall resource! A really useful feature.
[1:38:24](https://youtu.be/7glsC88h2Ss/watch?v=7glsC88h2Ss&t=5904s)​ – Next up, creating the Azure container to deploy our Hasura GraphQL API for [#Postgres](https://dev.to/hashtag/postgres)​ to!
[1:51:42](https://youtu.be/7glsC88h2Ss/watch?v=7glsC88h2Ss&t=6702s)​ – BAM! API Server is done and launched! I’ve got a live [#GraphQL](https://dev.to/hashtag/graphql)​ API up and running in Azure and we’re ready to start building a data model!
[1:56:22](https://youtu.be/7glsC88h2Ss/watch?v=7glsC88h2Ss&t=6982s)​ – In this segment I show how to turn off the public facing console and shift one’s development workflow to the local Hasura console working against – local OR your live dev environment.
[1:58:29](https://youtu.be/7glsC88h2Ss/watch?v=7glsC88h2Ss&t=7109s)​ – Next segment I get into schema migrations, initializing a directory structure for Hasura CLI use, and metadata, migrations, and related data. Including an update to the latest CLI so you can see how to do that, after a run into a slight glitch. 😬
[2:23:02](https://youtu.be/7glsC88h2Ss/watch?v=7glsC88h2Ss&t=8582s)​ – I also shift over to dbdiagram to graphically build out some of the schema via their markdown, then use the SQL export option for [#postgres](https://dev.to/hashtag/postgres)​ combined with Hasura’s option to execute plain ole SQL via migrations…
[2:31:48](https://youtu.be/7glsC88h2Ss/watch?v=7glsC88h2Ss&t=9108s)​ – Getting a bit more in depth in this segment, I delve through – via the Hasura console – to build out relationships between the tables and data so the graphql queries can introspect accordingly.
[2:40:30](https://youtu.be/7glsC88h2Ss/watch?v=7glsC88h2Ss&t=9630s)​ – Next segment, graphql time! I show some of the options of what is available immediately for queries and mutations via the console.
[2:50:36](https://youtu.be/7glsC88h2Ss/watch?v=7glsC88h2Ss&t=10236s)​ – Then some more details about metadata. I’m going to do a stream with further details, since I was a little fuzzy on some of those details myself, in the very very near future. However a good introduction to what the metadata does for the [#graphql](https://dev.to/hashtag/graphql)​ API.
[2:59:07](https://youtu.be/7glsC88h2Ss/watch?v=7glsC88h2Ss&t=10747s)​ – Then as a wrap up to all of this… I nuke EVERYTHING and deploy it all out to Azure again inclusive of schema migrations, metadata, etc. 🤘🏻
[3:16:30](https://youtu.be/7glsC88h2Ss/watch?v=7glsC88h2Ss&t=11790s)​ – Final segment, I add some data to the database and get into a few basic queries and mutations in [#graphql](https://dev.to/hashtag/graphql)​ via the [#graphiql](https://dev.to/hashtag/graphiql)​ console interface in [#Hasura](https://dev.to/hashtag/hasura)​.
