---
title: Getting COPY For Bulk CSV Working on a Container Running PostgreSQL
date: 2021-05-14 01:07:27 -0700
last_modified_at: 2021-05-14 01:07:27 -0700
permalink: /2021/05/14/getting-copy-for-bulk-csv-working-on-a-container-running-postgresql/
slug: getting-copy-for-bulk-csv-working-on-a-container-running-postgresql
wp_id: 63822
original_url: https://compositecode.blog/2021/05/14/getting-copy-for-bulk-csv-working-on-a-container-running-postgresql/
categories:
- Unknown Code Ramblings
tags: []
excerpt: (Video is available at the end of this post, be sure to check it out for further details) First off, check out this post if you’re curious how I put together the csv file. There is a ton of data out there that you can just download that is in csv format, but I wanted to have …
image: /wp-content/uploads/2020/12/Line-Banners-07.png
---

(Video is available at the end of this post, be sure to check it out for further details)

First off, check out this [post](/2021/05/12/javascript-csv-data-generation/) if you’re curious how I put together the csv file. There is a ton of data out there that you can just download that is in csv format, but I wanted to have data that was specific to a DDL (Data Definition Langauge) I wrote. Once I had a file, I went through the following steps to make it easily repeated through automation.

With that file make sure, at least for this example, that the first row of data has the column names as the commas seperated values. It should look something like this (per my example mentioned above), and obviously have far more data than the example below.

```
id,country,ip,created_at,updated_at,project_id
4cf25606-5f3e-4575-86ea-c585513fcc39,Solomon Islands,169.137.96.151,2020-12-25T05:04:26.124Z,2020-12-30T11:04:26.124Z,d6ef3dfd-9596-4391-b0ef-3d7a8a1a6d10
cbeaf6ab-23cc-43c5-a740-7191f59d8cc5,Solomon Islands,106.92.223.22,2020-12-25T05:04:26.124Z,2020-12-30T11:04:26.124Z,d6ef3dfd-9596-4391-b0ef-3d7a8a1a6d10
17a7ec0b-2758-4721-b104-f368c8109b6a,Solomon Islands,248.8.206.229,2020-12-25T05:04:26.124Z,2020-12-30T11:04:26.124Z,d6ef3dfd-9596-4391-b0ef-3d7a8a1a6d10
```

Now my next steps was to get this file copied to the server where the database is running. To check the containers I have running I call a quick `docker ps` to get a list.

[![The container list of running containers.](https://res.cloudinary.com/practicaldev/image/fetch/s--WCV_rhVH--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https%3A//dev-to-uploads.s3.amazonaws.com/uploads/articles/g2avep0b5mrhzuurbfiz.png)](https://res.cloudinary.com/practicaldev/image/fetch/s--WCV_rhVH--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https%3A//dev-to-uploads.s3.amazonaws.com/uploads/articles/g2avep0b5mrhzuurbfiz.png)

In this list, the PostgreSQL server is the container named `pgdb`. To copy the file to that server, the following command will get the job done.

```
docker cp ./name_of_file.csv pgdb:/name_of_file.csv
```

If you’d like the destination name of the file to be different, that is possible in this command too. I like to keep them the same to prevent confusion. For example, if I log into the server and have a bunch of terminals open, seeing the file named on things one place and another in the other place, that’ll throw a wrench into things.

With the file copied, I can now run the PostgreSQL command to bulk copy the data into a table. The command to get that done looks like this.

```
COPY the_table_where_the_data_will_go FROM '/name_of_file.csv' CSV HEADER;
```

That’s it! Well ok not really, this is one of the simpliest use cases. Such as, if any columns don’t map one to one with the column names of the csv file to the table column names, this command won’t work as is. Check out the [COPY documentation](https://www.postgresql.org/docs/10/sql-copy.html) to get the details on how to use the command if you have various things you need to tweak for your own work. However, for this basic premise and for what I want to talk about next, that’s it! 😁

To get into more details about how I automated this process, check out the video.

<iframe allowfullscreen="true" class="youtube-player" height="486" loading="lazy" sandbox="allow-scripts allow-same-origin allow-popups allow-presentation allow-popups-to-escape-sandbox" src="https://www.youtube.com/embed/aDLyjfuz-Uc?version=3&amp;rel=1&amp;showsearch=0&amp;showinfo=1&amp;iv_load_policy=1&amp;fs=1&amp;hl=en-US&amp;autohide=2&amp;wmode=transparent" style="border:0;" width="863"></iframe>
