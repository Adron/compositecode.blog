---
title: 'Backup Riak – Learning About Distributed Databases :: Issue 001'
date: 2013-05-08 11:57:24 -0700
last_modified_at: 2013-05-08 15:36:32 -0700
permalink: /2013/05/08/distributed-databases-issue-001/
slug: distributed-databases-issue-001
wp_id: 8273
original_url: https://compositecode.blog/2013/05/08/distributed-databases-issue-001/
categories:
- AWS
- Basho
- Databases
- Distributed Things
- How-to
- Riak
tags:
- backup
- basho
- distributed database
- distributed systems
- riak
excerpt: I’ve got more than a few series in the queue, so why not another one eh! The intent is, I’ll grab a specific topic to break down and add details to related to distributed systems, primarily around Riak. I will however diverge into other distributed databases too, but I’ll primarily be sticking to Riak. Without …
---

I’ve got more than a few series in the queue, so why not another one eh! The intent is, I’ll grab a specific topic to break down and add details to related to distributed systems, primarily around Riak. I will however diverge into other distributed databases too, but I’ll primarily be sticking to Riak. Without more introduction, the first topic is…

## Backing Up and Recovery of Riak (Nodes)

![](/images/adronhall.smugmug.com/Software/Misc-Images/Bad-Resume/i-5crkLQb/0/O/1368057009_data_backup.png)I’ve been asked approximately 423,983,321.7 zillion times how this is done. So here’s a quick summary and respective links to the best ways to backup Riak, how to recover nodes.

When backing up Riak there are two key things that need copied to the backup storage; the ring and data directories. Each of these things are specific based on the backend used with Riak. In addition to the core backup containing the ring and data, another good thing to backup is the configuration directory. When recovering this comes in useful.

For the locations of data, it depends slightly based on the operating system being used. The two big variances are OS-X and Linux Distros. On OS-X the data path, ring data and configuration are located at the locations listed below:

- Bitcask data: ./data/bitcask
- LevelDB data: ./data/leveldb
- Ring data: ./data/riak/ring
- Configuration: ./etc

For each specific distro, there are slight variations on where the locations are, for a full list check out the [Basho Riak docs on backups](http://docs.basho.com/riak/latest/cookbooks/Backups/). But on Linux distros the paths are as follows:

Debian and Ubuntu

- Bitcask data: /var/lib/riak/bitcask
- LevelDB data: /var/lib/riak/leveldb
- Ring data: /var/lib/riak/ring
- Configuration: /etc/riak

Fedora and RHEL

- Bitcask data: /var/lib/riak/bitcask
- LevelDB data: /var/lib/riak/leveldb
- Ring data: /var/lib/riak/ring
- Configuration: /etc/riak

Other Operating System Paths

Freebsd

- Bitcask data: /var/db/riak/bitcask
- LevelDB data: /var/db/riak/leveldb
- Ring data: /var/db/riak/ring
- Configuration: /usr/local/etc/riak

SmartOS

- Bitcask data: /var/db/riak/bitcask
- LevelDB data: /var/db/riak/leveldb
- Ring data: /var/db/riak/ring
- Configuration: /opt/local/etc/riak

Solaris

- Bitcask data: /opt/riak/data/bitcask
- LevelDB data: /opt/riak/data/leveldb
- Ring data: /opt/riak/ring
- Configuration: /opt/riak/etc

When backing things up, it’s important to note that each node could have slightly inconsistent data. The data however is rebuilt by the Riak read-repair system once it is recovered and brought into use.

**Backup Jobs**

One of the easiest ways to backup Riak is to setup a cron job with your choice of cp, rsync or tar. Then just get those files onto whatever your choice of backup medium. An example tar cron job to backup a [Bitcask](http://docs.basho.com/riak/latest/tutorials/choosing-a-backend/Bitcask/) backend is shown below (snagged from the [documentation](http://docs.basho.com/riak/latest/cookbooks/Backups/#Bitcask-Backups)) just to give you an idea of where to start.

```bash
tar -czf /mnt/riak_backups/riak_data_`date +%Y%m%d_%H%M`.tar.gz /var/lib/riak/bitcask /var/lib/riak/ring /etc/riak
```

For a [leveldb](http://docs.basho.com/riak/latest/tutorials/choosing-a-backend/LevelDB/) back end the most important thing to note is that the node must be stopped. The basic workflow of backing up a node in this manner is to stop the node, backup the data, ring and configuration and then start the node back up.

**Backup Recovery / Restoring**

When recovering data on a node that is replacing an existing node that has the same name (fully qualified or IP) then follow the steps below:

1. Install Riak
2. Restore the old node’s configuration, data & ring.
3. Start the node

Once you’ve got the node started back up it’s a good idea to do a ping or status against the node to verify it is in a good state.

If node names have been changed there are additional steps.

1. Mark the original instance down

   ```bash
   riak-admin down
   ```
2. Join the restored cluster

   ```bash
   riak-admin join
   ```
3. Replace the original with

   ```bash
   riak-admin cluster force-replcae
   ```
4. Get the cluster plan built

   ```bash
   riak-admin cluster plan
   ```
5. Commit the changes

   ```bash
   riak-admin cluster commit
   ```
6. Change the -name setting in the vm.args configuration file to match the new name.
7. Change & verify that the IP reflects the instances IP in the app.config for http and protocol buffer interfaces.

**Cluster Backups via Riak Enterprise Multi-Data Center (MDC)**

In the above sections I wrote about the traditional backup approaches. This is very similar to the way RDBMS are backed up. However, with a distributed system like Riak there is another great alternative if you’re utilizing multiple datacenters and Enterprise Riak. In this version of Riak, which is basically Riak with additional features and capabilities, one of the possible backup scenarios is to use the Multi-Data Center, or MDC, to replicate a duplicate cluster and use it as an active, real-time and always ready backup.

One workflow that is an exceptionally effective way to provide backups is to setup the “backup” cluster beside the current operative cluster. As an example, if your cluster is operational in AWS and it is running in X region and Y zone then you’d want to put the backup cluster in that same region and zone. Once you’ve setup Riak Enterprise and MDC, then just setup a full sync. Once the full sync is done you can then remove the backup cluster and it provides a point in time backup of the data.

```bash
riak-repl start-fullsync
```

It’s easy to schedule full sync operations to low usage periods and it is also possible to pause and resume full sync operations.

```bash
riak-repl resume-fullsync<br />riak-repl pause-fullsync
```

The variations on backing up data with Riak Enterprise and MDC are pretty expansive. Doing a point in time, maintaining a secondary live copy of the data, using the replication as a data dump to another cluster or even just using the MDC replication to dump all of the data to a single instance.

## File System Snapshots

One other technique that is extremely efficient, fast and thorough is [snapshotting the file system](http://en.wikipedia.org/wiki/Snapshot_(computer_storage)). The backup workflow for snapshots is extremely easy. First stop Riak, then snapshot, then start Riak again. Of all the methods, snapshotting is one of the easiest of the options. Just like setting up a cron job, automating snapshots based on some pre-defined schedule and meshing that with automated start and stop of Riak provides a very thorough backup.

With these options, have fun strategizing your stratagems into strategies for backups.

## Diskettes

[![](/images/adronhall.smugmug.com/Software/Misc-Images/Bad-Resume/i-wcd4pJL/0/O/1368057001_3floppy_unmount.png)](http://en.wikipedia.org/wiki/Sarcasm)One of the oldest, tried and true backups is the old diskette. The bestest way to backup with diskettes is to backup each node on three diskettes each. The send one of each diskettes to a geographically dispersed to a bank lock box or other secure facility. Do this for each node, and if need be use as many diskettes for each node as needed. A particularly useful method is to use the sharded zip strategy to stripe a backup across many diskettes. Once each lock box has a copy of the node for each node in the cluster, you’ll have one of the most secure backups in existence. [Nothing compares to the diskette backup](http://en.wikipedia.org/wiki/Sarcasm)!

**References:**

1. [Basho Docs – Backups](http://docs.basho.com/riak/latest/cookbooks/Backups/)
2. [Basho Docs – MDC Full Sync](http://docs.basho.com/riakee/latest/cookbooks/Multi-Data-Center-Replication-Scheduling-Full-Sync/)
