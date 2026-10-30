---
title: Vagrant for VMware Fusion with plugin issues…
date: 2013-04-26 12:01:23 -0700
last_modified_at: 2013-04-26 12:11:15 -0700
permalink: /2013/04/26/vagrant-for-vmware-fusion/
slug: vagrant-for-vmware-fusion
wp_id: 8231
original_url: https://compositecode.blog/2013/04/26/vagrant-for-vmware-fusion/
categories:
- How-to
- Riak
tags:
- bosh
- riak
- vagrant
excerpt: I’ve started using Vagrant pretty regularly. I downloaded Virtual Box and been tinkering away with some of the vagrant packages. The one huge bummer was that I was under the delusion that it only worked with Vagrant. Then, I was told by a fellow coder that I needed to check out the VMware Fusion plugin. …
---

I’ve started using Vagrant pretty regularly. I downloaded Virtual Box and been tinkering away with some of the vagrant packages. The one huge bummer was that I was under the delusion that it only worked with Vagrant. Then, I was told by a fellow coder that I needed to check out the VMware Fusion plugin. I immediately was stoked! Simply, have you…

```bash
$ vagrant plugin install vagrant-vmware-fusion
Installing the 'vagrant-vmware-fusion' plugin. This can take a few minutes...
Installed the plugin 'vagrant-vmware-fusion (0.6.1)'!
$ vagrant plugin license vagrant-vmware-fusion license.lic
Installing license for 'vagrant-vmware-fusion'...
The license for 'vagrant-vmware-fusion' was successfully installed!
$
```

Now mind you, you’ll need to go out and buy the VMware Fusion Plugin from [Hashi Corp](http://www.hashicorp.com/). From my perspective I was happy with this purchase just to get the stability improvements of VMware Fusion.

## Vagrant & Riak

For my first example of the new plugin I [forked and then cloned the Bosh Riak Repository](https://github.com/Adron/riak-boshrelease). Once that was cloned I simply opened a terminal and navigated to the path of the repository and tried…

```bash
vagrant up
```

…and immediately got the message, “Failed to load the “vagrant-vmware-fusion” plugin. View logs for more details.” Noooooooooooooooez! 🙁 I was sad. But dove into the logs by executing vagrant up with…

```bash
VAGRANT_LOG=INFO vagrant up
```

…and there was the error amid the log was something about the VMware Plugin requiring Vagrant the latest version.

Doh! I’d forgotten to upgrade first. I installed the upgrade via the [downloads for 1.2.2](http://downloads.vagrantup.com/). Once I upgrade I ran into the same error. A quick ‘vagrant -v’ to check the version showed 1.2.2 was installed. Not knowing the special secret sauce at this point, I figured I’d just reboot. It had been about 20-30 days since I had, so who knew what weird service or something needed to be restarted. I guessed correctly and after a restart vagrant kicked off the download of the vagrant image for the Bosh Riak deploy. It went by fast, and since it didn’t spit out an error about not loading the plugin I thought everything had worked…

```bash
$ vagrant up
Bringing machine 'default' up with 'virtualbox' provider...
[default] Setting the name of the VM...
[default] Clearing any previously set forwarded ports...
[default] Creating shared folders metadata...
[default] Clearing any previously set network interfaces...
[default] Preparing network interfaces based on configuration...
[default] Forwarding ports...
[default] --- 22 => 2222 (adapter 1)
[default] Booting VM...
[default] Waiting for VM to boot. This can take a few minutes.

...more stuff here...
```

…or so I had thought. Scrolling back up through the log I realized Vagrant had NOT used the plugin for VMware Fusion. I was still stuck with VirtualBox. I went through the plugin install again to see if it just needed re-applied. At this point, since I’d already installed Virtual Box previously I figured maybe I’d just keep plunging forward and mess with the vmware plugin later, however I’d REALLY like to have all my virtualized images running via Fusion. Not sure what I missed I decided to give it one more try…

```bash
$ vagrant plugin install vagrant-vmware-fusion
Installing the 'vagrant-vmware-fusion' plugin. This can take a few minutes...
Installed the plugin 'vagrant-vmware-fusion (0.6.1)'!
Adrons-MacBook-Air-3:Downloads adronhall$ vagrant plugin license vagrant-vmware-fusion license.lic
Installing license for 'vagrant-vmware-fusion'...
The license for 'vagrant-vmware-fusion' was successfully installed!
$ cd ~/Codez/riak-release/
$ vagrant up
Bringing machine 'default' up with 'virtualbox' provider...
```

Ugh… so I almost give up at this point. I read this, it seems ironic.

<blockquote class="twitter-tweet"><p>@<a href="https://twitter.com/jeffsussna">jeffsussna</a> @<a href="https://twitter.com/dberkholz">dberkholz</a> @<a href="https://twitter.com/monkchips">monkchips</a> @<a href="https://twitter.com/sogrady">sogrady</a> I feel as though Vagrant’s UX is quite good. No? — Mitchell Hashimoto (@mitchellh) <a href="https://twitter.com/mitchellh/status/327823216724803584">April 26, 2013</a></p></blockquote>

Being this isn’t the best user experience I stumble forward trying something else. I get a suggestion from a fellow coder (thx Brian) to try this.

```bash
$ vagrant up --provider=vmware_fusionAn active machine was found with a different provider. Vagrant
currently allows each machine to be brought up with only a single
provider at a time. A future version will remove this limitation.
Until then, please destroy the existing machine to up with a new
provider.

Machine name: default
Active provider: virtualbox
Requested provider: vmware_fusion
$
```

Well, that didn’t work either. It looks like maybe if I just blew away my VirtualBox images it would work? Well, funny, being I don’t have any VirtualBox images running or installed. Well, just to make sure I checked the VirtualBox directory. Nothing. I went ahead and deleted the entire VirtualBox Application. Tried again.

```bash
$ vagrant up --provider=vmware_fusionAn active machine was found with a different provider. Vagrant
currently allows each machine to be brought up with only a single
provider at a time. A future version will remove this limitation.
Until then, please destroy the existing machine to up with a new
provider.

Machine name: default
Active provider: virtualbox
Requested provider: vmware_fusion
$
```

Ok, I’ve no idea now. Any help would be greatly appreciated! This same thing appears to work fine under VirtualBox, but with the plugin added and VirtualBox removed I’m still not able to get this to work. Help!
