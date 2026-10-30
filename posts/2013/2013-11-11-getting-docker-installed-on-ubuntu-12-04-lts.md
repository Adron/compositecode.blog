---
title: Getting Docker Installed on Ubuntu 12.04 LTS
date: 2013-11-11 08:50:25 -0800
last_modified_at: 2014-01-23 17:38:09 -0800
permalink: /2013/11/11/getting-docker-installed-on-ubuntu-12-04-lts/
slug: getting-docker-installed-on-ubuntu-12-04-lts
wp_id: 9133
original_url: https://compositecode.blog/2013/11/11/getting-docker-installed-on-ubuntu-12-04-lts/
categories:
- Containers
- How-to
- Linux
tags:
- 12.04 LTS
- containers
- docker
- docker 0.6
- kernel 3.8
- linux
- linux containers
- linux kernel
- lxc
- ubuntu
- ubuntu 12.04 LTS
- ubuntu linux
- ubuntu server
excerpt: A few days ago I posted the blog entry “Using SSH Locally to Work With Ubuntu VM + VMware Tools Installation via Shell“, it was related to getting a clean Ubuntu Server install running with VMware Tools and so that I could use it as a hosted instance. Simply put, being able to SSH into …
image: /wp-content/uploads/2013/11/photodune-404355-train-l.jpg
---

[![](https://photos.adron.me/Software/Misc-Images/Just-Icons-and-Bits/i-jzq52Bs/0/O/logo-ubuntu_cof-orange-hex.jpg)](http://www.ubuntu.com/)A few days ago I posted the blog entry “[Using SSH Locally to Work With Ubuntu VM + VMware Tools Installation via Shell](/2013/11/10/using-ssh-locally-to-work-with-ubuntu-vm-vmware-tools-installation-via-shell/)“, it was related to getting a clean Ubuntu Server install running with VMware Tools and so that I could use it as a hosted instance. Simply put, being able to SSH into it just as I would a hosted AWS or Windows Azure Ubuntu Server image. [![](https://photos.adron.me/Software/Misc-Images/Just-Icons-and-Bits/i-CjZhXch/0/S/homepage-docker-logo-S.png)](http://www.docker.io/)Once I had the default virtual machine running 12.04 LTS I went about another installation that is needed to run Docker. Docker will have issues with anything pre-3.8 kernel. Running the command below will show that kernel 3.5 is the current kernel in 12.04 LTS.

```bash
apt-cache search linux-headers-$(uname -r)
```

To update to the 3.8 kernel I ran the following command and then rebooted.

```bash
sudo apt-get install linux-image-generic-lts-raring linux-headers-generic-lts-raring
sudo shutdown -r now
```

With the reboot complete, I checked the kernel version again and 3.8 was installed successfully.

```bash
@ubuntu:~$ apt-cache search linux-headers-$(uname -r)
linux-headers-3.8.0-33-generic -- Linux kernel headers for version 3.8.0 on 64 bit x86 SMP
```

To get Docker installed (as of 0.6) run the following command.

```bash
sudo sh -c "wget -qO- https://get.docker.io/gpg | apt-key add -"
sudo sh -c "echo deb http://get.docker.io/ubuntu docker main\
> /etc/apt/sources.list.d/docker.list"
```

Next update the sources, then install lxc-docker.

```bash
sudo apt-get update
sudo apt-get install lxc-docker
```

To verify that docker is installed I executed the following command and…

```bash
sudo docker run -i -t ubuntu /bin/bash
```

…see similar results just after issuing the command.

```bash
Unable to find image 'ubuntu' (tag: latest) locally
Pulling repository ubuntu
8dbd9e392a96: Download complete
b750fe79269d: Download complete
27cf78414709: Download complete
```

After that displays then I typed exit to leave docker. I now have a running version of docker on the Ubuntu 12.04 LTS instance ready for testing and hacking with docker.
