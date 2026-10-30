---
title: 'Thrashing Code Special Session: Netboot, Debian, Fighting BIOS UEFI, ISC DHCP, Ansible, Cassandra Cluster, and More'
date: 2018-09-02 21:48:46 -0700
last_modified_at: 2018-09-02 21:53:16 -0700
permalink: /2018/09/02/thrashing-code-special-session/
slug: thrashing-code-special-session
wp_id: 14593
original_url: https://compositecode.blog/2018/09/02/thrashing-code-special-session/
categories:
- Video
tags:
- distributed systems
- kvm
- net boot
- pxe boot
excerpt: Recently my friend swung by to record a Twitch stream on setting up the network, hardware, OS loads, PXE boot, and related items for the cluster in the office. Here’s a rundown of notes, details, and related links and such from the video, and as icing on the cake, here’s the video after some edits. …
image: /wp-content/uploads/2018/09/thrashing-code-light-brackground-cropped.png
---

Recently my friend swung by to record a Twitch stream on setting up the network, hardware, OS loads, PXE boot, and related items for the cluster in the office. Here’s a rundown of notes, details, and related links and such from the video, and as icing on the cake, here’s the video after some edits. I’ve managed to cut the Twitch stream down to a clean 150 minutes and 40 seconds from over 240 minutes! A little bit more digestible in this shorter format.

<iframe allowfullscreen="true" class="youtube-player" height="486" loading="lazy" sandbox="allow-scripts allow-same-origin allow-popups allow-presentation allow-popups-to-escape-sandbox" src="https://www.youtube.com/embed/jMFm6fmUWJw?version=3&amp;rel=1&amp;showsearch=0&amp;showinfo=1&amp;iv_load_policy=1&amp;fs=1&amp;hl=en-US&amp;autohide=2&amp;wmode=transparent" style="border:0;" width="863"></iframe>

Some of the additional changes, that you’ll distinctly notice if you watched the original stream, is that I cleaned up the audio in some places, *attempted* to raise the audio in others, and for the mono audio I bumped it out to stereo so it isn’t so strange to listen to. I’ve also added callout text for all the configuration files edited, and some other commands here and there were Jeremy uses his fast typing to open a file so fast you might not see which it was. Overall, it should be easier to listen to, more bite size in segments, and more useful to reference.

In addition, below I’ve broken out key parts of the process at their respective time points.

- 0:00:56 Determining what’s going to be setup and installed; Starting with a net install, setting up bastion server first, then figuring out the cassandra install once we have that.
- 0:02:10 Added *lftp*.

  ```bash
  sudo apt-get install lftp
  ```

  – [lftp wikipedia](https://en.wikipedia.org/wiki/Lftp) – [lftp site](https://lftp.yar.ru/) – [lftp manual page](https://lftp.yar.ru/lftp-man.html)
- 0:02:50 Whoops, wrong initial iso image. Cut out the cycling through BIOS and mess as that needs to be setup per whatever machines are involved. But now, back to the correct Debian image.
- 0:04:20 Getting image from Debian Distro FTP Servers. [ftp.us.debian.org](ftp://ftp.us.debian.org) at path [ftp://ftp.us.debian.org/debian-cdimage/current/amd64/iso-cd](ftp://ftp.us.debian.org/debian-cdimage/current/amd64/iso-cdftp://ftp.us.debian.org/debian-cdimage/current/amd64/iso-cd).
- 0:04:46 Plan is: Initial server will be a DHCP server setup so we can setup TFTP options to clients. – [TFTP Trivial File Transfer Protocol](https://en.wikipedia.org/wiki/Trivial_File_Transfer_Protocol) – TFTP will then be used to grab the kernal and ramdisk for Debian which will contain the installer. This will include a [preseed file](https://wiki.debian.org/DebianInstaller/Preseed) for Debian.
- 0:07:36 Initial setup of Debian.
- 0:08:05 Setup of the NIC with two ports begins. One port for internet, one port for inward facing network for the cluster.
- 0:11:04 Setup of the drives, since there’s a number of disks in the bastion server. Includes setup of home, swap, etc and Jeremy’s thoughts on that. Then some booting conflicts with the ssd vs. flash vs. other drives.
- 0:12:40 Jeremy and I discuss swap, failure approaches and practices.
- 0:14:10 Discussing various ways to automate the installation. Preseed, kickstart, [various automated installs](https://wiki.debian.org/AutomatedInstallation), etc.
- 0:30:38 A request for a bigger font, so Jeremy tweaks that while the webcam camera goes all auto-focus nightmare.
- 0:31:26 Jeremy installs his dot files. For more on dot files check out [here](https://code.tutsplus.com/tutorials/setting-up-a-mac-dev-machine-from-zero-to-hero-with-dotfiles--net-35449), [here](https://driesvints.com/blog/getting-started-with-dotfiles/), [here](https://medium.com/@webprolific/getting-started-with-dotfiles-43c3602fd789), and all the dot files on Github [here](https://dotfiles.github.io/) are useful.
- 0:32:30 Installing & configuration of [ISC (Internet Systems Consortium) DHCP (Dynamic Host Configuration Protocol)](https://www.isc.org/downloads/dhcp/) [download](https://www.isc.org/downloads/dhcp/). The Debian [docs page](https://wiki.debian.org/DHCP_Server). To install issue command

  ```bash
  sudo apt-get install isc-dhcp-server
  ```

  . Configuration file is */etc/default/isc-dhcp-server*.
- 0:32:50 Configure the isc-dhcp-server file.
- 0:33:35 Configure the dhcpd.conf file.
- 0:34:10 Initial subnet setup with 192 range,
- 0:36:44 Oh shit, wrong range. Switching to guns, going with 10 dot range.
- 0:38:10 Troubleshooting some as server didn’t start immediately.
- 0:39:17 Beginning of NAT Traffic setup & related.
- 0:39:38 Setup of iptables begins.
- 0:40:03 Jeremy declares he’ll just setup the iptables from memory. Then, he does indeed setup iptables from memory.
- 0:41:49 Setup port 22 and anything on the inside network.
- 0:42:50 Setup iptables to run on boot.
- 0:43:18 Set in /etc/network/interfaces
- 0:43:49 Set firewall to run first.
- 0:44:17 Reboot confirmation of load sequence.
- 0:44:55 Switching masquerade to be on interface vs. IP.
- 0:46:50 iptables hangs and troubleshooting commences.
- 0:48:42 Setup sshd\_config; turn off ‘use dns’.
- 0:49:33 Jeremy switches to Chromebook to complete the remaining configuration steps.
- 0:50:48 ssh key setup.
- 0:51:20 ssh key setup on Chromebook and respective key setup.
- 0:53:40 Install tftpd.

  ```bash
  sudo apt-get install tftpd
  ```
- 0:55:00 Adding iptables rules for additional changes made since initial iptables setup.
- 0:55:40 Setup/download inetd, tftpd, and other tools on bastion to setup remaining network and servers. Jeremy also provides an explanation of the daemons and how and what is getting setup now and respective DDOS concerns.
- 0:57:40 Starts download of netboot installer and everything else required to netboot a machine.
- 0:58:48 First pxelinux steps. Setup of configuration file.
- 1:00:52 First pxeboot attempt of a node server. KVM Switch confusion, and a flicker of life on the first node!
- 1:01:50 The pxe boot got the installer started, but no further steps were taken. Jeremy delves into the log files to determine why the pxe boot didn’t launch further into the installer.
- 1:04:20 Looks up pxelinux to setup some of the defaults and determine solutions. Good reference point for further research is available via [syslinux.org](https://www.syslinux.org/wiki/index.php?title=PXELINUX).
- 1:05:40 After a couple minutes of pxelinux information, back to the configuration.
- 1:07:23 Jeremy gets into preseed configuration but before diving in too deep covers some ground on what to do in a production environment versus what is getting setup in the current environment for this video.
- 1:08:47 Takes a preseed example to work from. Works through the file to setup the specifics of the installation for each of the nodes.
- 1:16:09

  ```bash
  sudo dpkg-reconfigure tzdata
  ```

  since earlier we set the time zone to PST since it was one of the only options but really wanted UTC. After reconfiguration execute a timesync.

  ```bash
  sudo systemctl restart systemd-timesyncd
  ```

  and then get a status

  ```bash
  sudo systemctl restart systemd-timesyncd
  ```
- 1:21:46 Finished reviewing the installation for the nodes. Started at 1:08:47, so it took a while to cover all those bases!
- 1:22:28 Moves new preseed file into the correct path in the installer inetrd.
- 1:27:44 After some troubleshooting, the pxeboot loading gets to the business of successfully loading a node, success! We follow up a short celebration of getting the first pxeboot with a little summary, restating the purpose of pxeboot, and some form and function of how pxeboot will work, i.e. pxeboot works when all other boot methods on a node fail. So when a drive is totally formatted and no master boot record to load from, boot, kicks off via pxeboot and we get a new image. Thus, it’s as simple as plugging in a new server and turning it on and I’ll have a brand new node in the cluster.
- 1:29:30 Cycling through each of the servers, which we’ve powered on to start loading from pxeboot, just to watch them start loading and to try an initial load.
- 1:29:51 Jeremy discusses the reasoning behind setting up some things specifically to the way they’ve been setup specific to having a database loaded on the servers versus just standard servers or another configuration of use.
- 1:32:13 With Jeremy declaring, “it’s just YAML right?!” we opt to use Ansible for the next steps of configuration for the nodes and their respective Cassandra database installations and setup.
- 1:32:22 Jeremy and I have a small debate about Python being trash for CLI’s or not. I’m wrong but it’s still garbage for a CLI, why does it keep getting used for CLI’s, use Go already. Grumble grumble, whatever.
- 1:35:46 Jeremy and I now have a discussion on the configuration related to IP’s, what the range would give us, how to assign them specifically, service discoverability of the nodes, and how all of this complexity can be mitigated by something simple for us to setup right now, instead of later.
- 1:38:25 After discussing, we opt to go with a hard coded DHCP configuration for now so we can just use the static (in function, but now literally of course since they’re designated in the DHCP) IP’s.
- 1:41:56 Setting up the actual Ansible Playbook for Cassandra starts here.
- 1:43:27 Executing Ansible and troubleshooting connectivity issues between nodes.
- 1:43:48 Need sshpass, installed with

  ```bash
  sudo apt-get install sshpass
  ```
- 1:44:18 We realize there’s a problem with the machines actually re-installing via pxe boot and change boot sequence to give that a temp fix.
- 1:45:25 Back into the Ansible Playbook. Further troubleshooting of the Ansible playbook.
- 1:45:59 Checking out the ansible hosts file.
- 1:46:19 Checking out the cassandra.yml for Ansible further. Which leads to…
- 1:46:53 …the realization we’re also installing Spark in addition to Cassandra. Hmmm, Ok, let’s do that too.
- 1:47:xx For the next several minutes Jeremy steps through and makes additions and fixes to the Ansible file(s).
- 1:59:52 Took a break at this point.
- 2:01:11 Had names for IP’s swapped. Fixed.
- 2:03:09 3 of the 5 nodes are now reachable after some troubleshooting.
- 2:03:27 After some more quick checks and troubleshooting executing the playbook again.
- 2:05:15 Oh dear it appears to be install Cassandra finally! Even with 3 nodes and 2 failing, that’s enough for quorum so moving forward!
- 2:08:44 Further edits and tweaks to the playbook.
- 2:09:20 Executing playbook again.
- 2:09:36 Removing further cruft from the playbook we copied.
- 2:09:53 Troubleshooting the Cassandra loads.
- 2:15:04 At this point there’s three executing Cassandra installs pulled from FTP for installation and on nodes.
- 2:30:40 End

As a shout out and props to Jeremy, when you need or want a new hard drive, check our https://diskprices.com/. It’s pretty solid for finding excellent disk prices and Jeremy gets a few pennies per order. Cheers, thanks for watching, and thanks Jeremy for swinging by and educating us all!
