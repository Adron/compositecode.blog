---
title: Join the Apollo Beta for FREE! Help the Databass!
date: 2019-10-11 16:34:26 -0700
last_modified_at: 2019-10-11 16:34:29 -0700
permalink: /2019/10/11/apollo-beta-released/
slug: apollo-beta-released
wp_id: 16428
original_url: https://compositecode.blog/2019/10/11/apollo-beta-released/
categories:
- Databases
- Distributed Things
tags:
- apache cassandra
- beta
- constellation apollo
- cql
- datastax
- datastax apollo
- datastax constellation
excerpt: Hello to all the data curious, database lovers, and sciency datamungers! I have a small favor to ask of you all. At DataStax we just opened up our Apollo service i.e. “Apache Cassandra as a Service” i.e. DBaaS offering and I’m looking for people that want to test drive the database! Now, you don’t have to …
image: /wp-content/uploads/2019/10/square.png
---

Hello to all the *data curious*, *database lovers*, and *sciency datamungers*! I have a small favor to ask of you all. At [DataStax](https://www.datastax.com/) we just opened up our **[Apollo](https://apollo.datastax.com/)** service i.e. “*Apache Cassandra as a Service*” i.e. *DBaaS* offering and I’m looking for people that want to test drive the database! Now, you don’t have to actually tell me you’re using it or anything, but I’d love to know if you are. Maybe we could even chat about your experience using it.

To get started:

1. Sign up [here](https://apollo.datastax.com).
2. Create a database [here](https://apollo.datastax.com/createDatabase).
3. Pick a driver [here](https://helpdocs.datastax.com/aws/dscloud/apollo/dscloudUsingDrivers.html).  [[C#](https://helpdocs.datastax.com/aws/dscloud/apollo/dscloudConnectCsharpDriver.html)/F#, [Node.js/JavaScript](https://helpdocs.datastax.com/aws/dscloud/apollo/dscloudConnectNodeJsDriver.html), [Java](https://helpdocs.datastax.com/aws/dscloud/apollo/dscloudConnectJavaDriver.html), [C++](https://helpdocs.datastax.com/aws/dscloud/apollo/dscloudConnectCplusDriver.html), and [Python](https://helpdocs.datastax.com/aws/dscloud/apollo/dscloudPythonDriver.html#dscloudPythonDriver)] – I added F# cuz ya know, that’s how F# works and all, you just use the C# driver and BOOM, you’ve got F# access!!
4. Write [CQL](http://cassandra.apache.org/doc/latest/cql/) and execute the database!
5. **Profit**!

Alright, where profit is that’s when you let me know what works for you and what doesn’t. Feel free to comment here, ping me via Twitter [@adron](https://twitter.com/Adron), or via the [response form here](/contact/), or however you’ve got to message me. I’d be super stoked to chat!

## Getting Started Specifics

To create a database, once you’ve got an account, just navigate to <https://apollo.datastax.com/createDatabase> and you’ll get prompted with the following screen.

![apollo-create-database](/wp-content/uploads/2019/10/apollo-create-database.png)

Currently during beta we have AWS as the provider option, and you can choose between Developer, Startup, Standard, and Enterprise. Each offering various configurations and future prospective SLA’s and such.

![asdf](/wp-content/uploads/2019/10/asdf.png)

Once you have the database name, keyspace, user name, and you password set, click on Launch Database and the spin up of the multi-node database will begin. You’ll be greeted with a message notifying you that it’ll take a little bit of time for the database to spin up and an email will be sent once it is done. Enjoy a coffee in the meantime.

![prompt](/wp-content/uploads/2019/10/prompt.png)

Once the database spins up there are two key sections on the database page. First, there is the connection details. They’re located in the bottom left of the database page.

![database-connection-details](/wp-content/uploads/2019/10/database-connection-details.png)

If you click on the “Learn How” you’ll get directly linked to the docs pages with multiple examples of how to get connected to the database you’ve just created. You can also reset your password here and retrieve the security bundle (it’s a tar/zip file) that you’ll need to authenticate any applications with.

The other part that can be really helpful, especially as you do any development or testing with your database is the grafana dashboard. It’s on the Health tab of the database page.

![grafana-metrics](/wp-content/uploads/2019/10/grafana-metrics.png)

A trick that I used, to get an easier and full screen view of all the metrics, is to inspect the page right at the metrics, within that you’ll find the iframe in which to get the link specifically to the Grafana metrics. They look pretty nice broken out of frame! As you work through queries and such keep an eye on this for extra insight.

![broken-out](/wp-content/uploads/2019/10/broken-out.png)

Any other thoughts, contemplation, or otherwise do get in touch!
