---
title: A Collection of Links & Tour of DataStax Docker Images
date: 2018-06-27 17:22:02 -0700
last_modified_at: 2018-07-08 17:51:24 -0700
permalink: /2018/06/27/a-collection-of-links-tour-of-datastax-docker-images/
slug: a-collection-of-links-tour-of-datastax-docker-images
wp_id: 14213
original_url: https://compositecode.blog/2018/06/27/a-collection-of-links-tour-of-datastax-docker-images/
categories:
- cassandra
- Distributed Things
tags:
- cassandra
- datastax
- datastax enterprise
- distributed databases
- distributed systems
- dse
excerpt: Another way to get up and running with a DataStax Enterprise 6 setup on your local machine is to use the available (and supported by DataStax) Docker images. For additional description of what each of the images is, what is contained on the images, I read up on via Kathryn Erickson’s (@012345) blog entry “DataStax …
image: /wp-content/uploads/2018/06/docker_logo-500x250.png
---

Another way to get up and running with a DataStax Enterprise 6 setup on your local machine is to use the [available (and supported by DataStax) Docker images](https://hub.docker.com/u/datastax/). For additional description of what each of the images is, what is contained on the images, I read up on via Kathryn Erickson’s ([@012345](https://twitter.com/012345)) blog entry “[DataStax Now Offering Docker Images for Development](https://www.datastax.com/2018/04/its-here-datastax-docker-images-for-dse)“. Also there’s a video Jeff Carpenter ([@jscarp](https://twitter.com/jscarp)) put together which talks from the 5.x version of the release (since v6 wasn’t released at the time).

<iframe allowfullscreen="true" class="youtube-player" height="486" loading="lazy" sandbox="allow-scripts allow-same-origin allow-popups allow-presentation allow-popups-to-escape-sandbox" src="https://www.youtube.com/embed/bolptfhDni4?version=3&amp;rel=1&amp;showsearch=0&amp;showinfo=1&amp;iv_load_policy=1&amp;fs=1&amp;hl=en-US&amp;autohide=2&amp;wmode=transparent" style="border:0;" width="863"></iframe>

I’m adding some lagniappe to that material here and providing additional notes to things. Before continuing however it’s a good idea to read Kathryn’s blog entry and watch Jeff’s video real quick, I promise it’ll only take you minutes of time, so do that and then come back. My post will still be here.

The three images that are available include:

- [dse-server](https://hub.docker.com/r/datastax/dse-server/)
- [dse-opscenter](https://hub.docker.com/r/datastax/dse-opscenter/)
- [dse-studio](https://hub.docker.com/r/datastax/dse-studio/)

The easiest way to get started with these images since they inter-operate together, and the dse-server image can be used to make a cluster, is to use docker-compose to spin them up. First though, I’ll need to actually pull the images down from the Docker Hub.

```bash
docker pull datastax/dse-studio
docker pull datastax/dse-opscenter
docker pull datastax/dse-server
```

Now that we have the images, there are some docker-compose yaml files available in the [DataStax Github Repo here](https://github.com/datastax/docker-images/tree/master/example_compose_yamls) that make it a single command line run to get an environment going locally. Various setups are available on a single machine depending on what you need too. Before running anything though, here are the yaml files with some extra descriptions about what’s going on with each.

This is the file for a server node. The image is datastax/dse-server which is available locally since I ran the commands listed earlier in the post. There’s a DS\_LICENSE that is set to accept, ulimits memlock is set to -1, sets environment variables for DS\_LICENSE and SEEDS, and some other settings specific to allowing mlock to lock memory. All kind of self-explanatory for each section of the yaml below.

```bash
version: '2'
services:
  seed_node:
    image: "datastax/dse-server"
    environment:
      -- DS_LICENSE=accept
    # Allow DSE to lock memory with mlock
    cap_add:
    -- IPC_LOCK
    ulimits:
      memlock: -1
  node:
    image: "datastax/dse-server"
    environment:
      -- DS_LICENSE=accept
      -- SEEDS=seed_node
    links:
      -- seed_node
    # Allow DSE to lock memory with mlock
    cap_add:
    -- IPC_LOCK
    ulimits:
      memlock: -1
```

This is the studio file contents, which opens up a mapping for port 9091, sets the environment setting for the DS\_LICENSE variable, and that’s really it. The image already has DSE Studio installed and ready to run as soon as the image is used to spin up a container.

```bash
version: '2'
services:
  studio:
    image: "datastax/dse-studio"
    environment:
      -- DS_LICENSE=accept
    ports:
      -- 9091:9091
```

The last file is the Ops Center startup. Also has pretty minimal contents since the image is setup and installed with what it needs to get up and running quickly. A port is also mapped to 8888 for use, and seed\_node is bound appropriately with the other containers.

```bash
version: '2'
services:
  opscenter:
    image: "datastax/dse-opscenter"
    ports:
      -- 8888:8888
    environment:
      -- DS_LICENSE=accept
  seed_node:
    links:
      -- opscenter
  node:
    links:
      -- opscenter
```

To get these started in various executions, for instance, I’ll start with a 3-node cluster, Ops Center running, and DSE Studio.

```bash
docker-compose -f docker-compose.yml -f docker-compose.opscenter.yml -f docker-compose.studio.yml up -d --scale node=2
```

Breaking that apart, this is a command using docker-compose that uses all three of the yaml files shown above. I start with `docker-compose` then follow that by pointing to a file with the `-f` switch and then the file itself, `docker-compose.yml`. The next with another `-f docker-composie.opscenter.yml`, then the last `-f docker-compose.studio.yml` and the sub command `up`. Then follow this with `-d` so that the containers are run in a detached state. Follow that with `--scale node-2` which will give us the starting node count of two nodes for the server.

With that command, one can then break it apart to startup different combinations to work with such as this command below which just starts up a single node and the studio. A great setup using minimal resources if we just want to work with studio.

```bash
docker-compose -f docker-compose.yml -f docker-compose.studio.yml up -d --scale node=0
```

Another combination might be to just startup a 3 node cluster, of course, one could try more but that will likely decimate a machines resources pretty quickly.

```bash
docker-compose  -f docker-compose.yml up -d --scale node=2
```

If we want to play around with Ops Center a great way to do that is to spin up a 3-node cluster and opscenter by itself.

```bash
docker-compose -f docker-compose.yml -f docker-compose.opscenter.yml up -d --scale node=2
```

That gives us options around what to start and which things we actually want to work with at any particular time. A great way to setup a demo or just test out different features within DataStax Enterprise Ops Center, Studio, or even just setting up a cluster.

If you’d like to get involved, run into an issue, or just simply have a question or two check out the Github repo to file an issue or add a comment in Docker Hub.

- As a comment in [Docker Hub](https://hub.docker.com/u/datastax/)
- File an issue in the [GitHub repo](https://github.com/datastax/docker-images)
- Email us at [techpartner@datastax.com](mailto:techpartner@datastax.com)

## Summary

Some days ago I took a quick tour through [Azure and GCP Marketplace options for getting a DSE6 Cassandra Cluster up and running](/2018/06/21/quick-marketplace-clusters-for-cassandra-datastax-enterprise-6/). I’ll be taking a look at additional methods for installation, setup, and configuration in the coming weeks and days. So stay tuned, subscribe, or if you’d like to hear about new Cassandra or related distributed systems meetups in the Seattle area be sure to sign up to my [Thrashing Code Newsletter](https://adron.us11.list-manage.com/subscribe?u=7f73ff0427183b9b64e1f336a&id=a6fc3efde0) (and select *Event News Only* if you only want to know about events).
