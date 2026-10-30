---
title: Setting Up Nodes, Firewall, & Instances in Google Cloud Platform
date: 2018-09-21 09:36:31 -0700
last_modified_at: 2018-09-21 09:36:31 -0700
permalink: /2018/09/21/setting-up-nodes-firewall-instances-in-google-cloud-platform/
slug: setting-up-nodes-firewall-instances-in-google-cloud-platform
wp_id: 14649
original_url: https://compositecode.blog/2018/09/21/setting-up-nodes-firewall-instances-in-google-cloud-platform/
categories:
- Infrastructure
- ThrashingCode
- Video
tags:
- deployment
- infrastructure
- infrastructure as code
- terraform
- thrashing code
- thrashingcode
- twitch
- video
excerpt: Here’s the run down of what I covered in the latest Thrashing Code Session (go subscribe here to the channel for future sessions or on Twitch). The core focus of this session was getting some further progress on my Terraform Project around getting a basic Cassandra and DataStax Enterprise Apache Cassandra Cluster up and running …
---

Here’s the run down of what I covered in the latest Thrashing Code Session (go [subscribe here](https://www.youtube.com/channel/UCHSCXYCMOOS-VSUdRsn13GQ) to the channel for future sessions or on [Twitch](https://www.twitch.tv/adronhall)). The core focus of this session was getting some further progress on my Terraform Project around getting a basic Cassandra and DataStax Enterprise Apache Cassandra Cluster up and running in Google Cloud Platform.

The code and configuration from the work is available on Github at [terraform-fields](https://github.com/Adron/terraformed-fields) and a summary of code changes and other actions taken during the session are further along in this blog entry.

## Streaming Session Video

<iframe allowfullscreen="true" class="youtube-player" height="486" loading="lazy" sandbox="allow-scripts allow-same-origin allow-popups allow-presentation allow-popups-to-escape-sandbox" src="https://www.youtube.com/embed/NmlzGKUnln4?version=3&amp;rel=1&amp;showsearch=0&amp;showinfo=1&amp;iv_load_policy=1&amp;fs=1&amp;hl=en-US&amp;autohide=2&amp;wmode=transparent" style="border:0;" width="863"></iframe>

In this session I worked toward completing a few key tasks for the Terraform project around creating a Cassandra Cluster. Here’s a run down of the time points where I tackle specific topics.

- [3:03](https://www.youtube.com/watch?v=NmlzGKUnln4&t=183s) – Welcome & objectives list: Working toward DataStax Enterprise Apache Cassandra Cluster and standard Apache Cassandra Cluster.
- [3:40](https://www.youtube.com/watch?v=NmlzGKUnln4&t=220s) – Review of what infrastructure exists from where we left off in the previous [episode](https://youtu.be/lEujfUM2LcU).
- [5:00](https://www.youtube.com/watch?v=NmlzGKUnln4&t=300s) – Found music to play that is copyright safe! \m/
- [5:50](https://www.youtube.com/watch?v=NmlzGKUnln4&t=350s) – Recap on where the project lives on Github in the [terraformed-fields repo](https://github.com/Adron/terraformed-fields).
- [8:52](https://www.youtube.com/watch?v=NmlzGKUnln4&t=532s) – Adding a google\_compute\_address for use with the instances. Leads into determining static public and private google\_compute\_address resources. The idea being to know the IP for our cluster to make joining them together easier.
- [11:44](https://www.youtube.com/watch?v=NmlzGKUnln4&t=704s) – Working to get the access\_config and related properties set on the instance to assign the google\_compute\_address resources that I’ve created. I run into a few issues but work through those.
- [22:28](https://www.youtube.com/watch?v=NmlzGKUnln4&t=1348s) – Bastion server is set with the IP.
- [37:05](https://www.youtube.com/watch?v=NmlzGKUnln4&t=2225s) – I setup some files, following a kind of “bad process” as I note. Which I’ll refactor and clean up in a subsequent episode. But the bad process also limits the amount of resources I have in one file, so it’s a little easier to follow along.
- [54:27](https://www.youtube.com/watch?v=NmlzGKUnln4&t=3267s) – Starting to look at [provisioners](https://www.terraform.io/docs/provisioners/index.html) to execute script files and commands before or after the instance creation. Super helpful, with the aim to use this feature to download and install the DataStax Enterprise Apache Cassandra or standard Apache Cassandra software.
- [1:16:18](https://www.youtube.com/watch?v=NmlzGKUnln4&t=4578s) – Ah, a need for firewall rule for ssh & port 22. I work through adding those and then end up with an issue that we’ll be resolving next episode!

## **Session Content**

**Starting Point:** I started this episode from where I left off [last session](https://youtu.be/lEujfUM2LcU).

**Work Done:** In this session I added a number of resources to the project and worked through a number of troubleshooting scenarios, as one does.

Added firewall resources to open up port 22 and icmp (ping, etc).

```bash
resource "google_compute_firewall" "bastion-ssh" {
  name    = "gimme-bastion-ssh"
  network = "${google_compute_network.dev-network.name}"

  allow {
    protocol = "tcp"
    ports    = ["22"]
  }
}

resource "google_compute_firewall" "bastion-icmp" {
  name    = "gimme-bastion-icmp"
  network = "${google_compute_network.dev-network.name}"

  allow {
    protocol = "icmp"
  }
}
```

I also broke out the files so that each instances has its own IP addresses with it in the file specific to that instance. Later I’ll add context for why I gave the project file bloat, by refactoring to use modules.

![terraform-files.png](/wp-content/uploads/2018/09/terraform-files.png)

Added each node resource as follows. I just increased each specific node count by one for each subsequent node, such as making this node1\_internal IP google\_compute\_address increment to node2\_internal. Everything also statically defined, adding to my file and configuration bloat.

```bash
resource "google_compute_address" "node1_internal" {
  name         = "node-1-internal"
  subnetwork   = "${google_compute_subnetwork.dev-sub-west1.self_link}"
  address_type = "INTERNAL"
  address      = "10.1.0.5"
}

resource "google_compute_instance" "node_frank" {
  name         = "frank"
  machine_type = "n1-standard-1"
  zone         = "us-west1-a"

  boot_disk {
    initialize_params {
      image = "ubuntu-minimal-1804-bionic-v20180814"
    }
  }

  network_interface {
    subnetwork = "${google_compute_subnetwork.dev-sub-west1.self_link}"
    address    = "${google_compute_address.node1_internal.address}"
  }

  service_account {
    scopes = [
      "userinfo-email",
      "compute-ro",
      "storage-ro",
    ]
  }
}
```

I also setup the bastion server so it looks like this. Specifically designating a public IP so that I can connect via SSH.

```bash
resource "google_compute_address" "bastion_a" {
  name = "bastion-a"
}

resource "google_compute_instance" "a" {
  name         = "a"
  machine_type = "n1-standard-1"
  zone         = "us-west1-a"

  provisioner "file" {
  source      = "install-c.sh"
  destination = "install-c.sh"

  connection {
    type     = "ssh"
    user     = "root"
    password = "${var.root_password}"
    }
  }

  boot_disk {
    initialize_params {
      image = "ubuntu-minimal-1804-bionic-v20180814"
    }
  }

  network_interface {
    subnetwork = "${google_compute_subnetwork.dev-sub-west1.self_link}"
    access_config {
      nat_ip = "${google_compute_address.bastion_a.address}"
    }
  }

  service_account {
    scopes = [
      "userinfo-email",
      "compute-ro",
      "storage-ro",
    ]
  }
}
```

Plans for next session include getting the nodes setup so that the bastion server can work with and deploy or execute commands against them without the nodes being exposed publicly to the internet. We’ll talk more about that then. For now, happy thrashing code!
