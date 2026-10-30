---
title: Terraform Changes, Provisioners, Connections, and Static Nodes
date: 2018-10-10 17:33:41 -0700
last_modified_at: 2018-10-12 10:21:17 -0700
permalink: /2018/10/10/terraform-changes-provisioners-connections-and-static-nodes/
slug: terraform-changes-provisioners-connections-and-static-nodes
wp_id: 14743
original_url: https://compositecode.blog/2018/10/10/terraform-changes-provisioners-connections-and-static-nodes/
categories:
- Google Cloud
- Infrastructure
tags:
- cluster nodes
- connections
- gcp
- Google Cloud
- instance resources
- provisioners
- resources
- terraform
excerpt: 'NOTE: Video toward the bottom of the post with the timeline so you can navigate into certain points of the video where I speak to different topics. Cluster Nodes Currently First I start out this session with a simple issue I ran into the previous night. The fact that a variable in the name of …'
image: /wp-content/uploads/2018/10/terraform-long-header.png
---

**NOTE:** *Video toward the bottom of the post with the timeline so you can navigate into certain points of the video where I speak to different topics.*

## Cluster Nodes Currently

First I start out this session with a simple issue I ran into the previous night. The fact that a variable in the name of the instance resource being created causes the instance to be destroyed and created on every single execution of terraform. That won’t do so I needed to just declare each node, at least the first three, maybe five (cuz’ it’s best to go with 2n+1 instances in most distributed systems). So I removed the module I created in the last session and created two nodes to work with, for creation and setup of the provisioners that I’d use to setup Cassandra.

In addition to making each of the initial nodes statically declared, I also, at least for now added public IP’s for troubleshooting purposes. Once those are setup I’ll likely remove those and ensure that the cluster just communicates on the private IP’s, or at least disallow traffic from hitting the individual nodes of the cluster even via the public IP’s via the firewall settings.

The nodes, public and private IP addresses, now look like this.

```bash
resource "google_compute_address" "node_zero_address" {
  name         = "node-0-address"
  subnetwork   = "${module.network_development.subnetwork_west}"
  address_type = "INTERNAL"
  address      = "10.1.0.2"
}

resource "google_compute_address" "node_zero_public_address" {
  name = "node-0-public"
}

resource "google_compute_instance" "node_zero" {
  name         = "node-0"
  machine_type = "n1-standard-1"
  zone         = "us-west1-a"

  boot_disk {
    initialize_params {
      image = "ubuntu-minimal-1804-bionic-v20180814"
    }
  }

  network_interface {
    subnetwork = "${module.network_development.subnetwork_west}"
    address    = "${google_compute_address.node_zero_address.address}"

    access_config {
      nat_ip = "${google_compute_address.node_zero_public_address.address}"
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

## Provisioners

When using [Terraform provisioners](https://www.terraform.io/docs/provisioners/index.html) there are a few things to take into account. First, which is kind of obvious but none the less I’m going to mention it, is to know which user, ssh keys, and related authentication details you’re using to actually login to the instances you create. It can get a little confusing sometimes, at least it’s gotten me more than once, when gcloud initiates making ssh keys for me while I’ve got my own keys already created. Then when I setup a provisioner I routinely forget that I don’t want to use the id\_rsa but instead the google created keys. I talk more about this in the video, with more ideas about insuring also that the user on the machine is the right user, it’s setup for centos or ubuntu or whatever distro your using, and all of these specifics.

Once that’s all figured out, sorted, and not confused, it’s just a few steps to get a provisioner setup and working. The first thing is we need to setup whichever provisioner it is we want to use. There are several options; file, local-exec, remote-exec, and some others for chef, salt-masterless, null\_resource, and habitat. Here I’m just going to cover file, local-exec, and remote-exec. First let’s take a look at the file provisioner.

```bash
resource "google_compute_instance" "someserver" {
  # ... some other fields for the particular instance being created.

  # Copies the myapp.conf file to /etc/myapp.conf
  provisioner "file" {
    source      = "directory/relative/to/repo/path/thefile.json"
    destination = "/the/path/that/will/be/created/andthefile.json"
  }
}
```

This example of a provisioner shows, especially with my fancy naming, several key things;

The provisioner goes into an instance resource, as a field within the instance resource itself.
The provisioner, which I’ve selected the “file” type of provisioner here, then has several key fields within the field, for the file provisioner those two required fields are source and destination.
The source takes the file to be copied to the instance, which is locally in this repository, or I suppose could be outside of it, based on a general path and the file name. You could just put the filename if it’s just there in the root of where this is being executed.
The destination is where within the instance users folder is on the remote server. So if I set a folder/filename.json it’ll create a folder called “folder” and put the file in it, possibly renamed if it isn’t the same name, here as filename.json.

But of course, one can’t just simply copy a file to a remote instance without a user and the respective authentication, which is where the connection resource comes into play within the provisioner resource. That makes the provisioner look like this.

```bash
resource "google_compute_instance" "someserver" {
  # ... some other fields for the particular instance being created.

  # Copies the myapp.conf file to /etc/myapp.conf
  provisioner "file" {
    source      = "directory/relative/to/repo/path/thefile.json"
    destination = "/the/path/that/will/be/created/andthefile.json"
    connection {
      type        = "ssh"
      user        = "useraccount"
      private_key = "${file("~/.ssh/id_rsa")}"
      agent       = false
      timeout     = "30s"
    }
  }
}
```

Here the connection resource adds several new fields that are used to make the connection. This is the same for the file or remote-exec provisioner. As mentioned earlier, and through troubleshooting in the video, in this case I’ve just put in the syntax id\_rsa since that’s the common ssh private key. However with GCP I needed to be using the google\_compute\_engine ssh private key.

The other fields are pretty self-explanatory, but let’s discuss real quick. The type, is simply that it is an ssh connection that will be used. One can also use plain text and some other options, or in the case of windows one uses the winrm connection type.

The user field is simply the name of the user which will be used to authenticate to the remote instance upon creation. The private key is the private ssh key of the user that needs to connect to that particular instance and do whatever the provisioner is going to do.

The agent, if set to false, doesn’t use ssh-agent, but if set to true does. On windows the only supported ssh authentication is pageant.

Then the timeout field is the time, in seconds as shown, that the provisioner will wait for execution to respond before an error is thrown in the terraform execution.

After all of those things were setup I created a simple script to install Cassandra which I called install-c.sh.

```bash
#!/usr/bin/env bash

# Installing Cassandra 3.11.3

echo "deb http://www.apache.org/dist/cassandra/debian 311x main" | sudo tee -a /etc/apt/sources.list.d/cassandra.sources.list
curl https://www.apache.org/dist/cassandra/KEYS | sudo apt-key add --
sudo apt-get update
sudo apt-key adv --keyserver pool.sks-keyservers.net --recv-key A278B781FE4B2BDA
sudo apt-get install -Y cassandra
```

Now with the script done I can use the file provisioner to move it over to the server. Which I did in the video, and then started putting together the remote-exec provisioner. However I messed around with the local-exec provisioner too but then realized I’d gotten them turned around in my head. The local-exec actually initiates a script executing here on the local machine that terraform execution starts from, which I needed terraform to execute the script that is out on the remote instance that was just created. That provisioner looks like this.

```bash
provisioner "remote-exec" {
  inline = [
    "chmod +x install-c.sh",
    "install-c.sh",
  ]

  connection {
    type        = "ssh"
    user        = "adron"
    private_key = "${file("~/.ssh/google_compute_engine")}"
    agent       = false
    timeout     = "30s"
  }
}
```

In this provisioner the inline field takes an array of strings which will be executed on the remote server. I could have just entered the installation steps for installing cassandra here, but considering I’ll actually want to take additional steps and actions, that would make the privisioner exceedingly messy. So what I do here is setup the connection and then for the inline field I modify the file so that it can be executed and then execute the script on the server. It then goes through the steps of adding the apt-get repo, taking respective verification steps, running and update, and then installing cassandra.

After that I wrap up for this session. Static instances created, provisioners dedicated, and connections made and verified for the provisioners with cassandra being installed. So for the next session I’m all set to start connecting the nodes together into a cluster and taking whatever next steps I need.

<iframe allowfullscreen="true" class="youtube-player" height="486" loading="lazy" sandbox="allow-scripts allow-same-origin allow-popups allow-presentation allow-popups-to-escape-sandbox" src="https://www.youtube.com/embed/aT7cTR7_5SY?version=3&amp;rel=1&amp;showsearch=0&amp;showinfo=1&amp;iv_load_policy=1&amp;fs=1&amp;hl=en-US&amp;autohide=2&amp;start=227&amp;wmode=transparent" style="border:0;" width="863"></iframe>

- [0:57](https://www.youtube.com/watch?v=aT7cTR7_5SY&t=57s) Thrashing Code Intro
- [3:43](https://www.youtube.com/watch?v=aT7cTR7_5SY&t=223s) Episode Intro, stepping into Terraform for the session.
- [4:25](https://www.youtube.com/watch?v=aT7cTR7_5SY&t=265s) Starting to take notes during session!
- [6:12](https://www.youtube.com/watch?v=aT7cTR7_5SY&t=372s) Describing the situation where variables in key values of resources causes the resources to recreate every `terraform apply` so I broke out each individual node.
- [9:36](https://www.youtube.com/watch?v=aT7cTR7_5SY&t=576s) I start working with the provisioner to get a script file on machine and also execute that script file. It’s tricky, because one has to figure out what the user for the particular image is. Also some oddball mess with my mic starts. Troubleshooting this, but if you know what’s up with OBS streaming software and why this is happening, lemme know I’m all ears! 🙂
- [31:25](https://www.youtube.com/watch?v=aT7cTR7_5SY&t=1885s) Upon getting the file provisioner to finally work, setting extra fields for time out and such, I moved on to take next steps with IntelliJ cuz the IDE is kind of awesome. In addition, the plugins for HCL (HashiCorp Configuration Language) and related elements including features built into the actual IDE provide some extra autocomplete and such for Terraform work. At this time I go through actually setting up the IDE (installed it earlier while using Visual Studio Code).
- [34:15](https://www.youtube.com/watch?v=aT7cTR7_5SY&t=2055s) Setup of IntelliJ plugins specific to Terraform and the work at hand.
- [35:50](https://www.youtube.com/watch?v=aT7cTR7_5SY&t=2150s) I show some of the additional fields that the autocomplete in Terraform actually show, which helps a lot during troubleshooting or just building out various resources.
- [37:05](https://www.youtube.com/watch?v=aT7cTR7_5SY&t=2225s) Checking out the Apache Cassandra ([http://cassandra.apache.org/](https://www.youtube.com/redirect?q=http%3A%2F%2Fcassandra.apache.org%2F&event=video_description&redir_token=Nr7hHKwCJXDCWKFA_jyb5XiJW5N8MTUzOTMwMTM2OEAxNTM5MjE0OTY4&v=aT7cTR7_5SY)) download and install commands and adding those to the install script for the Terraform provisioner file copy to copy over to the instance.
- [43:18](https://www.youtube.com/watch?v=aT7cTR7_5SY&t=2598s) I add some configurations for terraform builds/execution via IntelliJ. There are terraform specific build options and also bash file execution options which I cover in video.
- [45:32](https://www.youtube.com/watch?v=aT7cTR7_5SY&t=2732s) I take a look at IntelliJ settings to determine where to designate the Terraform executable file. This is important for getting the other terraform build configuration options to work.
- [48:00](https://www.youtube.com/watch?v=aT7cTR7_5SY&t=2880s) Start of debugging and final steps between now and…
- [1:07:16](https://www.youtube.com/watch?v=aT7cTR7_5SY&t=4036s) …finish of successful Cassandra install on nodes using provisioners.
- [1:07:18](https://www.youtube.com/watch?v=aT7cTR7_5SY&t=4038s) Finishing up by committing the latest changes to repository.
- [1:09:04](https://www.youtube.com/watch?v=aT7cTR7_5SY&t=4144s) Hacker outtro!

**Resources:**

- [Terraform Docs](https://www.terraform.io/docs)
- Github Repo [terraformed-fields](https://github.com/Adron/terraformed-fields)
- [Apache Cassandra](http://cassandra.apache.org/)
