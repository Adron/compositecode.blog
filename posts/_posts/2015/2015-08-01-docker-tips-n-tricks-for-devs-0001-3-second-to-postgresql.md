---
title: 'Docker Tips n’ Tricks for Devs – #0001 – 3 Second to Postgresql'
date: 2015-08-01 12:00:32 -0700
last_modified_at: 2015-08-01 12:00:32 -0700
permalink: /2015/08/01/docker-tips-n-tricks-for-devs-0001-3-second-to-postgresql/
slug: docker-tips-n-tricks-for-devs-0001-3-second-to-postgresql
wp_id: 11416
original_url: https://compositecode.blog/2015/08/01/docker-tips-n-tricks-for-devs-0001-3-second-to-postgresql/
categories:
- Containers
- How-to
tags:
- container
- database
- docker
- postgresql
excerpt: 'The easiest implementation of a docker container with Postgresql that I’ve found recently allows the following commands to pull and run a Postgresql server for you. docker pull postgres:latest docker run -p 5432:5432 postgres Then you can just connect to the Postgresql Server by opening up pgadmin with the following connection information: …'
image: /wp-content/uploads/2013/11/lxc.png
---

The easiest implementation of a docker container with Postgresql that I’ve found recently allows the following commands to pull and run a Postgresql server for you.

```bash
docker pull postgres:latest
docker run -p 5432:5432 postgres
```

Then you can just connect to the Postgresql Server by opening up pgadmin with the following connection information:

- Host: localhost
- Port: 5432
- Maintenance DB: postgres
- Username: postgres
- Password:

With that information you’ll be able to connect and use this as a development database that only takes about 3 seconds to launch whenever you need it.
