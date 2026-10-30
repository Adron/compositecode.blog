---
title: MariaDB & SkySQL DBAAS
date: 2023-08-10 11:46:47 -0700
last_modified_at: 2023-08-23 09:24:54 -0700
permalink: /2023/08/10/mariadb-skysql-dbaas/
slug: mariadb-skysql-dbaas
wp_id: 66527
original_url: https://compositecode.blog/2023/08/10/mariadb-skysql-dbaas/
categories:
- Databases
tags:
- databases
- dbaas
- mariadb
- mysql
- relational database management system
- skysql
- sql
excerpt: Starting to use, or interested in using MariaDB? This is a getting started post that will get you started with MariaDB and SkySQL. Prerequisite knowledge of SQL is helpful, but I step through every single little detail in this post to get you up and running, with a good context of what you’re getting.
image: /wp-content/uploads/2023/08/Database-Illustrator.jpg
---

This is a *getting started* guide for MariaDB SkySQL. Let’s start with two prerequisites definitions:

1. MariaDB – MariaDB is an open-source relational database management system (RDBMS) that is a fork of MySQL, another popular open-source database system. It was created by the original developers of MySQL after concerns arose about the acquisition of MySQL by Oracle Corporation in 2010. MariaDB is designed to be a drop-in replacement for MySQL, which means that many applications and tools developed for MySQL can also work seamlessly with MariaDB without requiring significant changes. It retains much of the same syntax, APIs, and commands as MySQL, making the transition relatively straightforward for users.
2. MariaDB SkySQL – MariaDB SkySQL is a cloud-native Database as a Service (DBaaS) offering provided by MariaDB Corporation, the company behind the development of the MariaDB open-source database system. SkySQL is designed to simplify database management, deployment, and scaling by providing a fully managed and highly available MariaDB database solution in the cloud.

Some key features of MariaDB include:

1. **High Performance**: MariaDB incorporates optimizations and improvements to enhance query execution speed and overall performance.
2. **Storage Engines**: MariaDB supports multiple storage engines, including the popular InnoDB and Aria engines. Each engine has its own characteristics and performance attributes, allowing users to choose the one that best fits their requirements.
3. **Security**: MariaDB includes various security enhancements, such as data encryption at rest and in transit, improved authentication methods, and better access control mechanisms.
4. **Open Source**: MariaDB is fully open source, which means its source code is available for anyone to inspect, modify, and contribute to.
5. **Community and Development**: MariaDB has a vibrant and active community of developers and contributors who work on its continued development and improvement.
6. **Compatibility**: As mentioned earlier, MariaDB aims for compatibility with MySQL, allowing applications developed for MySQL to work with minimal changes.
7. **Extensions**: MariaDB introduces some features not present in MySQL, such as the Aria storage engine, thread pooling, and more advanced geographic information system (GIS) functionality.
8. **Replication and Clustering**: Like MySQL, MariaDB supports various replication methods and clustering solutions for high availability and fault tolerance.
9. **Plugins**: MariaDB offers a plugin architecture that allows users to add custom functionality and features to the database system.

To elaborate further on the specifics of MariaDB SkySQL, here are some of the features of the DBAAS (DataBase As A Service):

1. **Managed Service**: SkySQL takes care of database administration tasks such as provisioning, backup, monitoring, maintenance, and security updates. This allows users to focus more on their applications and less on managing the underlying database infrastructure.
2. **High Availability**: SkySQL offers built-in high availability configurations that ensure database uptime and data durability. This includes automatic failover and replication setups.
3. **Scalability**: SkySQL supports both vertical and horizontal scaling. Vertical scaling involves adjusting the resources of a single database instance, while horizontal scaling involves distributing data across multiple nodes for improved performance and capacity.
4. **Security**: Security features such as encryption at rest and in transit, role-based access control, and network security protocols are integrated to help protect sensitive data.
5. **Multi-Cloud Support**: SkySQL is designed to work across various cloud providers, enabling users to choose the cloud environment that best suits their needs. It supports popular cloud platforms like Amazon Web Services (AWS), Microsoft Azure, and Google Cloud Platform (GCP).
6. **Compatibility**: SkySQL maintains compatibility with the MariaDB database, which means applications developed for MariaDB can run seamlessly on SkySQL with minimal modifications.
7. **Global Distributed Architecture**: SkySQL offers the capability to deploy databases across multiple geographic regions for improved performance and data availability across different parts of the world.
8. **Managed Upgrades**: Regular updates and improvements to the MariaDB database engine are managed by the SkySQL service, ensuring that your databases remain up to date without manual intervention.
9. **Pay-as-You-Go**: SkySQL’s pricing model is typically based on usage, allowing users to pay for the resources they consume. This can be cost-effective for businesses as it eliminates the need to invest in and maintain dedicated database infrastructure.

## Prerequisites

Before going any further, let’s check box some prerequisites for getting started. For any database I work with I like to pick up the native tool to work with that database. For some databases, like SQL Server, that might be a specific user interface application or others it may be a CLI. In the case of MariaDB, the default native way that many connect to MariaDB is via the mariadb CLI. For each installation method per your specific operating system, I’ll leave it to you dear reader to choose the one that fits your needs. The number of installation resources out on the web for MariaDB, specific to one’s operating system (Windows, Linux, or MacOS) are pretty extensive. The installation guides that I’ve found useful in the past, and some that have been created recently are pretty nice, which I’ve included here:

- Digital Ocean’s “[How to Install MariaDB on Ubuntu 20.04](https://www.digitalocean.com/community/tutorials/how-to-install-mariadb-on-ubuntu-20-04)” is a full installation guide, but a great way to get a first install running. Which in turn, will ensure you have the mariadb CLI installed.
- To use brew to install MariaDB on MacOS check out these [docs here](https://mariadb.com/kb/en/installing-mariadb-on-macos-using-homebrew/).
- Digital Ocean has a page specific to MariaDB that lists out all of their installation guides [here](https://www.digitalocean.com/community/tutorial-collections/how-to-install-mariadb).
- To get up and running on Windows, with a nice wizard installation, check out the [docs page here](https://mariadb.com/kb/en/installing-mariadb-msi-packages-on-windows/) on installing with an MSI package.

### Final Prerequisite Checklist

- Base OS Load and IDE’s, like [this](/2020/05/26/development-machine-environment-build-language-stack-installations-browsers-ides/).
- CLI `mariadb` installed.
- Jetbrains Datagrip installed, one of the default I [always install](/2020/05/26/development-machine-environment-build-language-stack-installations-browsers-ides/).

## MariaDB SkySQL Getting Started

[![](/wp-content/uploads/2023/08/image-1.png)](/wp-content/uploads/2023/08/image-1.png)

*Click on the image for a giant full size one.*

At this point, sign up for an account and setup an instance via the “Launch a Cloud Database” page. Here’s a nice long screenshot, with my choices for the instance I wanted all chosen.

Selected Enterprise Server since that would provide the basics of what I want to try out. Next up, a single node would serve well. Then the Oregon, USA us-west-2 location of AWS’s. Went with the default AMD64 with a Sky-2×4 instance with standard gp2. I also left the transactional storage size at 100GB.

Next up I selected the Enterprise Server 10.6.14-9, the recommended version. Gave it a most excellent service name and wrapped up by selecting to allow the service IP. I did learn, for quick access you want select the current IP to add.

[![](/wp-content/uploads/2023/08/image-3.png)](/wp-content/uploads/2023/08/image-3.png)

*Click for full size image.*

Finally, I needed to “Add payment method & launch”. Clicking that brought up the “Add a new credit card” dialog. I filled this out and the “save” button isn’t active. Before getting the save button activated I had click on the validate phone number button. With that completed the instance started launching. This can take a few minutes in my experience.

[![](/wp-content/uploads/2023/08/image-4.png)](/wp-content/uploads/2023/08/image-4.png)

*Instance launching.*

[![](/wp-content/uploads/2023/08/image-5.png)](/wp-content/uploads/2023/08/image-5.png)

*The instance now launched with a nice status dashboard.*

[![](/wp-content/uploads/2023/08/image-9.png)](/wp-content/uploads/2023/08/image-9.png)

Once the instance is up and running, navigate to the settings (left hand side) and open up that screen to setup Secure Access.

[![](/wp-content/uploads/2023/08/image-10.png)](/wp-content/uploads/2023/08/image-10.png)

In this dialog, since I didn’t check the “add IP address” previously, I’ll add it here.

[![](/wp-content/uploads/2023/08/image-11.png)](/wp-content/uploads/2023/08/image-11.png)

I added the IP this way instead of selecting the check box previously for two reasons.

1. I wanted to make sure I went and found out where I could add IPs to the allowlist. My IP will be changing, as they tend to do, and I want to know exactly where I’ll have to go to add additional IPs when my IP changes. In addition, if I travel, the same situation would arise where I would need to add a new IP wherever it is that I am at.
2. The second reason is even simpler, I wanted to figure out where this was in the interface and see how the interface was designed. It’s a pretty straight forward interface and even enables you to just click and it will give you your IP. At least, the IP that it can identity via the browser you’re using. If you’re using a VPN or under some other networking setup this might not be accurate, but it’ll cover 99% of the cases.

[![](/wp-content/uploads/2023/08/image-7.png)](/wp-content/uploads/2023/08/image-7.png)

Once I added the IP, I navigated back to this screen. Over to the far right is the “manage” button which provides many of the standard actions one would have to take to start, stop, or take other actions against the database instance.

Next to that is the “connect” button which is key to the next steps I want to take. On this modal dialog I have all the details, along with the \*.pem to download, to make a connection with the various tools I want to connect with.

[![](/wp-content/uploads/2023/08/image-8.png)](/wp-content/uploads/2023/08/image-8.png)

Since the CLI connection details are on the dialog, I’ll connect that way first. The first step is to download the \*.pem key. The cool thing is the commands on this dialog are setup to use the \*.pem key right from your downloads directory. So you can just download it right to where it goes (by default that is, if you’ve changed this note where it will be, you’ll need to make that change). With that downloaded we’re ready for the next steps.

## Getting Connected via `mariadb` CLI

[![](/wp-content/uploads/2023/08/image-12.png)](/wp-content/uploads/2023/08/image-12.png)

Here (in the above terminal image) I’ve executed the `mariadb --host xyz.skysql.mariadb.com --port 3306 --user theUserHere -p --ssl-ca ~/Downloads/skysql_chain_2022.pem` command. I then enter the password for my account, the command via the passed \*.pem file then ssl connects me to the database and I’m in.

[![](/wp-content/uploads/2023/08/image-13.png)](/wp-content/uploads/2023/08/image-13.png)

The next command the connect dialog provides is to set the password for the database account to something that isn’t the default generated password.

[![](/wp-content/uploads/2023/08/image-14.png)](/wp-content/uploads/2023/08/image-14.png)

Here I copied my first attempt to change the password and noted there are complexity rules applied to the password. Simple enough, added some good characters (special and all), and that met the check.

Now with the security needs met I was ready to do some database things! First step, I wanted a database on my database server! But I was also curious, what databases already exist on the server and could I view them with a `SHOW DATABASES;` command? Sure enough, information\_schema, mysql, performance\_schema, sky, and sys are there. These are the system tables that the database needs, and I presume the `sky` database is probably SkySQL related.

[![](/wp-content/uploads/2023/08/image-15.png)](/wp-content/uploads/2023/08/image-15.png)

Now that I know what databases exist, I wanted to get my own created so issued a minimal create database command.

```
CREATE DATABASE adrons_epic_db;
```

That completed successfully so I followed it with another `SHOW DATABASES;` but with the added `LIKE` to it to show just the database I created.

[![](/wp-content/uploads/2023/08/image-16.png)](/wp-content/uploads/2023/08/image-16.png)

I presumed next up I’d need to switch to that database to issue commands against it. I followed that command with a create table command to get something to put data into.

[![](/wp-content/uploads/2023/08/image-17.png)](/wp-content/uploads/2023/08/image-17.png)

With a table created I could now finally store some data in the database. With a simple insert statement I was able to add a row to the table. Since I’d not set a default value for the id I also inserted it, normally I’d set a default and just let it auto create the value here.

I followed that up. with a select to see the data I just added. You can also see I pulled dyslexic maneuver on the word “railraods” which is a great reason to check out something that can autocomplete like DataGrip. Which just happens to be the next tool I wanted to connect!

[![](/wp-content/uploads/2023/08/image-18.png)](/wp-content/uploads/2023/08/image-18.png)

Last action however, closing out the connection with `exit`. It’s always a good practice to close out of things properly, so that connections aren’t left hanging.

[![](/wp-content/uploads/2023/08/image-19.png)](/wp-content/uploads/2023/08/image-19.png)

## Using Jetbrains DataGrip

DataGrip is a great tool from JetBrains for working against a huge number of databases. With any new database I like to get DataGrip wired up as one of my primary tools. I’ll show you how I went about doing that with this new MariaDB SkySQL database now. Pay close attention, as there are specific pecularities to getting this to work.

[![](/wp-content/uploads/2023/08/image-21.png)](/wp-content/uploads/2023/08/image-21.png)

First step was simply starting a new project.

[![](/wp-content/uploads/2023/08/image-22.png)](/wp-content/uploads/2023/08/image-22.png)

Next up the connection itself. From the long list of databases I found and selected MariaDB.

[![](/wp-content/uploads/2023/08/image-23.png)](/wp-content/uploads/2023/08/image-23.png)

Next up on the connection, I went with the default name it spit out by pasting in the “Host”. That value comes from the connection dialog, which if you note, there are copy icons which will copy the specific text into your copy paste cache. It’s a good idea to use those instead of trying to select the dialog content directly.

[![](/wp-content/uploads/2023/08/image-25.png)](/wp-content/uploads/2023/08/image-25.png)

With the host set I also needed to download the driver, which I did using the download link, which in this image is replaced with the “Test Connection” link. With these settings made, then I clicked on the SSH/SSL tab of the connection dialog. On this tab of the dialog I clicked on “Use SSL”, used the select button to navigate via the file browser to the location of the certificate file. I then clicked on “Test Connection” and got an error.It seemed I’d done everything correct, but the Mode needed to be set to “Verify CA”. Once I did that, the connection worked.

[![](/wp-content/uploads/2023/08/image-26.png)](/wp-content/uploads/2023/08/image-26.png)

Click on Server Objects and choosing a new workspace I could then issue SQL commands, just as with the CLI before.

[![](/wp-content/uploads/2023/08/image-27.png)](/wp-content/uploads/2023/08/image-27.png)

A quick `SHOW DATABASES` gave me a list of databases in the results below, and I went ahead and issued a USE database command, and as you can see the autocomplete kicked off immediately! The glory and ease of development when you’ve got autocomplete!

[![](/wp-content/uploads/2023/08/image-28.png)](/wp-content/uploads/2023/08/image-28.png)

I also mocked going through and creating a table just because I wanted to snag a screenshot showing the details of how you can go in and create a table with DataGrip. It’s sometimes a clunky interface but its also very powerful. It’s easy to create table and other elements of the database without remembering the esoteric nuances of the create syntax, all while seeing the SQL syntax in the preview below the form.

[![](/wp-content/uploads/2023/08/image-29.png)](/wp-content/uploads/2023/08/image-29.png)

Just for good measure, here’s the dialog querying against that same table I created earlier with the CLI. With all that, a solid getting started tour, and I’m now setup to start development against my database. All that, and more, in subsequent posts.

So if you’re looking for a MariaDB option, MariaDB SkySQL is a very good option. It’s easy to get started, and it’s easy to use. With – and this makes me happy – decent starting security! I’m looking forward to using it more in the future.
