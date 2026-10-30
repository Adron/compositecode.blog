---
layout: page
title: Setting up Ubuntu With SSH & WMware Tools on VMware Fusion
date: 2013-12-10 16:48:36 -0800
last_modified_at: 2013-12-10 16:48:36 -0800
permalink: /setting-up-ubuntu-with-ssh-wmware-tools-on-vmware-fusion/
slug: setting-up-ubuntu-with-ssh-wmware-tools-on-vmware-fusion
wp_id: 9344
original_url: https://compositecode.blog/setting-up-ubuntu-with-ssh-wmware-tools-on-vmware-fusion/
---

I do a lot of work with Ubuntu, 90% or so of that work is from an Ubuntu instance. Often that instance happens to be a local VM running in VMware Fusion (or sometimes Virtual Box). Often I’ll start with a base server image which isn’t entirely setup for SSHing into the instance. These are the steps to get that installed and ready to go.

First install the image, in this particular situation I’m using the Ubuntu 12.04 LTS Server image. Here’s a quick walk through video or…

<http://vimeo.com/adronhall/vmwarefusionubuntusetup>

…just keep following the steps here.

[![Ubuntu 12.04 Server. Click for full size image.](https://photos.adron.me/Software/Software-Development/Docker-Virtual-Machines/i-mkQtmRF/0/M/New_Virtual_Machine_Assistant_and_Virtual_Machine_Library-M.png)](https://photos.adron.me/Software/Software-Development/Docker-Virtual-Machines/i-mkQtmRF/0/O/New_Virtual_Machine_Assistant_and_Virtual_Machine_Library.png)

*Ubuntu 12.04 Server. Click for full size image.*

That will take a few minutes to install, on machines these days I’ve experience just about 8-15 minutes. There are a million other options to do this too, such as starting with a clean Ubuntu image using Vagrant, which takes all of about 1-2 minutes, sometimes a bit more if you have to download the image. But either way, get one built and running.

[![Installing Ubuntu using VMware Fusion. Click for full size image.](https://photos.adron.me/Software/Software-Development/Docker-Virtual-Machines/i-W5FHGG7/0/M/New_Virtual_Machine_Assistant_and_Virtual_Machine_Library%20002-M.png)](https://photos.adron.me/Software/Software-Development/Docker-Virtual-Machines/i-W5FHGG7/0/O/New_Virtual_Machine_Assistant_and_Virtual_Machine_Library%20002.png)

*Installing Ubuntu using VMware Fusion. Click for full size image.*

Once the image is installed, login and install openssh-server and openssh-client. Here’s a short video installing the SSH Server and Client.

<https://vimeo.com/81557254>

```bash
sudo apt-get install openssh-server openssh-client
```

Once that’s installed I pull up my IP address with ifconfig.

```bash
ifconfig
```

The ifconfig command shows a lot of information regarding the network configuration associated with the various network adapters in the machine that it is executed on. In the image I’ve circled the local IP address that is assigned to the instance.

[![The local IP address using the ifconfig command. Click for full size image.](https://photos.adron.me/Software/Software-Development/Docker-Virtual-Machines/i-xt2t3bb/0/M/New_Virtual_Machine_Assistant_and_Virtual_Machine_Library%20003-M.png)](https://photos.adron.me/Software/Software-Development/Docker-Virtual-Machines/i-xt2t3bb/0/O/New_Virtual_Machine_Assistant_and_Virtual_Machine_Library%20003.png)

*The local IP address using the ifconfig command. Click for full size image.*

Now that you have the local IP of the instance, bring up a local terminal (in this case I’m on OS-X, but if you’re on Windows pull up Putty or on Linux or another \*nix variant pull up a shell). In the terminal you can now enter the follow SSH command to log in from the local machine versus the running instance. This comes in handy when you want to treat the machine like an actual hosted machine somewhere, in which you wouldn’t be directly logged into the server.

```bash
ssh username@192.168.77.197
```

![Logged In.](https://photos.adron.me/Software/Software-Development/Docker-Virtual-Machines/i-LTpthgL/0/O/New_Virtual_Machine_Assistant_and_Virtual_Machine_Library%20004.png)

*Logged In.*

## Getting VMware Tool Installed

This assumes that you mount the installation files (aka the cdrom) via the built into mount option in the VMware Fusion menu.

[![Selecting 'Reinstall VMware Tools' to mount the installation files. Click for full size image.](https://photos.adron.me/Software/Software-Development/Docker-Virtual-Machines/i-fC6hp7P/0/M/menu-M.jpg)](https://photos.adron.me/Software/Software-Development/Docker-Virtual-Machines/i-fC6hp7P/0/O/menu.jpg)

*Selecting ‘Reinstall VMware Tools’ to mount the installation files. Click for full size image.*

Once that’s mounted, the machine is ready to install the tools on. However, there are a few other things to install just before installing these. First get the latest updates for apt-get with the update command.

```bash
sudo apt-get update
```

Now install the latest gcc, make, kernel headers and other important tools.

```bash
sudo apt-get install gcc make build-essential
sudo apt-get install linux-headers-$(uname -r)
```

In the above, everything can be put on one line, but I separated the linux-headers just for extra clarity. I can now via remote SSH on the local machine or directly into the virtual machine and run the following commands to install the VMware Tools.

```bash
sudo mkdir /mnttools
sudo mount /dev/cdrom /mnttools
tar xzvf /mnttools/VMwareTools-x.x.x-xxxx.tar.gz -C /tmp/
cd /tmp/vmware-tools-distrib/
sudo ./vmware-install.pl -d
```

Finish everything up with a good reboot.

```bash
sudo shutdown -r now
```

Now I have the VMware Tools installed and able to SSH remotely, giving me the ability to use the virtual machine as I would an actual hosted instance.
