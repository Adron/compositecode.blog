---
title: Bunches of Databases in Bunches of Weeks – PostgreSQL Day 1
date: 2019-02-09 14:52:13 -0800
last_modified_at: 2019-06-06 11:11:30 -0700
permalink: /2019/02/09/bunches-of-databases-in-bunches-of-weeks-postgresql-day-1/
slug: bunches-of-databases-in-bunches-of-weeks-postgresql-day-1
wp_id: 15249
original_url: https://compositecode.blog/2019/02/09/bunches-of-databases-in-bunches-of-weeks-postgresql-day-1/
categories:
- Databases
- How-to
- Video
tags:
- container technology
- database
- docker
- postgresql
- technology
- ubuntu
excerpt: May the database deluge begin, it’s time for “Bunches of Databases in Bunches of Weeks”. We’ll get into looking at databases similar to how they’re approached in “7 Databases in 7 Weeks“. In this session I got into a hard look at PostgreSQL or as some refer to it just Postgres. This is the first …
image: /wp-content/uploads/2019/01/bunches-of-databases-in-bunches-of-weeks-postgresql.jpg
---

May the database deluge begin, it’s time for “Bunches of Databases in Bunches of Weeks”. We’ll get into looking at databases similar to how they’re approached in “[7 Databases in 7 Weeks](https://pragprog.com/book/rwdata/seven-databases-in-seven-weeks)“. In this session I got into a hard look at [PostgreSQL](https://www.postgresql.org/) or as some refer to it just Postgres. This is the first of a few sessions on PostgreSQL in which I get the database installed locally on Ubuntu. Which is transferable to any other operating system really, PostgreSQL is awesome like that. Then after installing and getting pgAdmin 4, the user interface for PostgreSQL working against that, I go the Docker route. Again, pointing pgAdmin 4 at that and creating a database and an initial table.

Below the video here I’ve added the timeline and other details, links, and other pertinent information about this series.

<iframe allowfullscreen="true" class="youtube-player" height="486" loading="lazy" sandbox="allow-scripts allow-same-origin allow-popups allow-presentation allow-popups-to-escape-sandbox" src="https://www.youtube.com/embed/UD5cQ9fMYcQ?version=3&amp;rel=1&amp;showsearch=0&amp;showinfo=1&amp;iv_load_policy=1&amp;fs=1&amp;hl=en-US&amp;autohide=2&amp;wmode=transparent" style="border:0;" width="863"></iframe>

[0:00](https://youtu.be/UD5cQ9fMYcQ/watch?v=UD5cQ9fMYcQ&t=0s) – The intro image splice and metal intro with tunes..
[3:34](https://youtu.be/UD5cQ9fMYcQ/watch?v=UD5cQ9fMYcQ&t=214s) – Start of the video database content.
[4:34](https://youtu.be/UD5cQ9fMYcQ/watch?v=UD5cQ9fMYcQ&t=274s) – Beginning the local installation of Postgres/PostgreSQL on the local machine.
[20:30](https://youtu.be/UD5cQ9fMYcQ/watch?v=UD5cQ9fMYcQ&t=1230s) – Getting pgAdmin 4 installed on local machine.
[24:20](https://youtu.be/UD5cQ9fMYcQ/watch?v=UD5cQ9fMYcQ&t=1460s) – Taking a look at pgAdmin 4, a stroll through setting up a table, getting some basic SQL from and executing with pgAdmin 4.
[1:00:05](https://youtu.be/UD5cQ9fMYcQ/watch?v=UD5cQ9fMYcQ&t=3605s) – Installing Docker and getting PostgreSQL setup as a container!
[1:00:36](https://youtu.be/UD5cQ9fMYcQ/watch?v=UD5cQ9fMYcQ&t=3636s) – Added the link to the [stellar post at Digital Ocean’s Blog](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-postgresql-on-ubuntu-18-04).
[1:00:55](https://youtu.be/UD5cQ9fMYcQ/watch?v=UD5cQ9fMYcQ&t=3655s) – My declaration that if Digital Ocean just provided documentation I’d happily pay for it, their blog entries, tutorials, and docs are hands down some of the best on the web!
[1:01:10](https://youtu.be/UD5cQ9fMYcQ/watch?v=UD5cQ9fMYcQ&t=3670s) – Installing Postgesql on Ubuntu 18.04.
[1:06:44](https://youtu.be/UD5cQ9fMYcQ/watch?v=UD5cQ9fMYcQ&t=4004s) – Signing in to Docker hub and finding the official Postgresql Docker Image.
[1:09:28](https://youtu.be/UD5cQ9fMYcQ/watch?v=UD5cQ9fMYcQ&t=4168s) – Starting the container with Docker.
[1:10:24](https://youtu.be/UD5cQ9fMYcQ/watch?v=UD5cQ9fMYcQ&t=4224s) – Connecting to the Docker Postgresql Container with pgadmin4.
[1:13:00](https://youtu.be/UD5cQ9fMYcQ/watch?v=UD5cQ9fMYcQ&t=4380s) – Creating a database and working with SQL, tables, and other resources with pgAdmin4 against the Docker container.
[1:16:03](https://youtu.be/UD5cQ9fMYcQ/watch?v=UD5cQ9fMYcQ&t=4563s) – The hacker escape outtro. Happy thrashing code!

For each of these sessions for the “[Bunches of Databases in Bunches of Weeks](https://www.youtube.com/playlist?list=PL4f75Y6Ce5ssKPOFLtPjUmDWsinO4K-c4)” series I’ll follow this following sequence. I’ll go through each database in [this list of my top 7 databases](/2019/01/04/lets-talk-top-7-options-for-database-gumbo/) for day 1 (see below), then will go through each database and work through the day 2, and so on. Accumulating additional days similarly to the “[7 Databases in 7 Weeks](https://pragprog.com/book/rwdata/seven-databases-in-seven-weeks)”

“**Day 1**” of the Database, I’ll work toward building a development installation of the particular database. For example, in this session I setup PostgreSQL by installing it to the local machine and also pulled a Docker image to run PostgreSQL.

“**Day 2**” of the respective database, I’ll get into working against the database with CQL, SQL, or whatever that one would use to work specifically with the database directly. At this point I’ll also get more deeply into the types, inserting, and storing data in the respective database.

“**Day 3**” of the respective database, I’ll get into connecting an application with C#, Node.js, and Go. Implementing a simple connection, prospectively a test of the connection, and do a simple insert, update, and delete of some sort against the respective database built on the previous day 2 of the same database.

“**Day 4**” and onward I’ll determine the path and layout of the topic later, so subscribe on [YouTube](https://www.youtube.com/channel/UCHSCXYCMOOS-VSUdRsn13GQ) and [Twitch](https://www.twitch.tv/adronhall/), and tune in. The [events are scheduled](https://www.twitch.tv/adronhall/events), with the option to be notified when a particular episode is coming on that you’d like to watch [here on Twitch](https://www.twitch.tv/adronhall/events).

### Next Events for “*Bunches of Databases in Bunches of Days*“

- [Bunches of Databases in Bunches of Weeks – SQL Server Day 1](https://www.twitch.tv/events/5JIXYj8rR-yp8Jv_Uy1LfQ)
- [Bunches of Databases in Bunches of Weeks – Elasticsearch Day 1](https://www.twitch.tv/events/Daf4_TYORvqxIbUFpc-TNw)
