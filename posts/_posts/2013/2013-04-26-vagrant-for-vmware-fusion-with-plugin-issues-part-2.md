---
title: Vagrant for VMware Fusion with plugin issues…  Part 2
date: 2013-04-26 14:03:53 -0700
last_modified_at: 2013-04-26 14:03:53 -0700
permalink: /2013/04/26/vagrant-for-vmware-fusion-with-plugin-issues-part-2/
slug: vagrant-for-vmware-fusion-with-plugin-issues-part-2
wp_id: 8248
original_url: https://compositecode.blog/2013/04/26/vagrant-for-vmware-fusion-with-plugin-issues-part-2/
categories:
- How-to
- Riak
tags:
- bosh
- riak
- vagrant
- vmware
excerpt: After the previous blog entry I wrote up, working through getting vagrant to spool up a vmware image I got a few other suggestions via Twitter. @adron Delete the “.vagrant” directory. — Mitchell Hashimoto (@mitchellh) April 26, 2013 @adron @mitchellh @jeffsussna @dberkholz @monkchips @sogrady did you delete your .vagrant subfolder and try again with –provider …
---

After the previous blog entry I wrote up, working through getting vagrant to spool up a vmware image I got a few other suggestions via Twitter.

<blockquote class="twitter-tweet">
<p>@<a href="https://twitter.com/adron">adron</a> Delete the “.vagrant” directory.</p>
<p>— Mitchell Hashimoto (@mitchellh) <a href="https://twitter.com/mitchellh/status/327863433192161280">April 26, 2013</a></p></blockquote>

<blockquote class="twitter-tweet">
<p>@<a href="https://twitter.com/adron">adron</a> @<a href="https://twitter.com/mitchellh">mitchellh</a> @<a href="https://twitter.com/jeffsussna">jeffsussna</a> @<a href="https://twitter.com/dberkholz">dberkholz</a> @<a href="https://twitter.com/monkchips">monkchips</a> @<a href="https://twitter.com/sogrady">sogrady</a> did you delete your .vagrant subfolder and try again with –provider flag?</p>
<p>— Troy Howard (@thoward37) <a href="https://twitter.com/thoward37/status/327870593473069058">April 26, 2013</a></p></blockquote>

With that quick delete of the hidden vagrant directory I gave it a shot again with the provider flagh.

```bash
rm -rf .vagrant/
$ vagrant up --provider=vmware_fusionBringing machine 'default' up with 'vmware_fusion' provider...
[default] VMware requires root privileges to make many of the changes
necessary for Vagrant to control it. In a moment, Vagrant will ask for
your administrator password in order to install a helper that will have
permissions to make these changes. Note that Vagrant itself continues
to run without administrative privileges.
Password:
[default] Box 'bosh-solo-0.6.4' was not found. Fetching box from specified URL for
the provider 'vmware_fusion'. Note that if the URL does not have
a box for this provider, you should interrupt Vagrant now and add
the box yourself. Otherwise Vagrant will attempt to download the
full box prior to discovering this error.
Downloading or copying the box...
```

Which this seemed to work. Downloading the helpers and such started and I waited patiently.

*A Few Thoughts…*

Needing to delete a hidden file struck me as one of those completely arbitrary and random solutions. It worked, which is awesome, but it working is a completely counter intuitive solution. I did a ‘destroy’ previously along with a number of things that were somewhat not intuitive. At this point the steps were fine, I had to ask for help, and I got help really fast. That’s awesome, but needing to go through those steps was unfortunate and ties back around to [@jeffsussna](http://twitter.com/jeffsussna)‘s tweet earlier.

<blockquote class="twitter-tweet">
<p>Hey <a href="https://twitter.com/search/%23developersaskingmakers">#developersaskingmakers</a> dudes: how come UX for Dev/Ops tools still sucks? @<a href="https://twitter.com/dberkholz">dberkholz</a> @<a href="https://twitter.com/monkchips">monkchips</a> @<a href="https://twitter.com/sogrady">sogrady</a></p>
<p>— Jeff Sussna (@jeffsussna) <a href="https://twitter.com/jeffsussna/status/327822545472585729">April 26, 2013</a></p></blockquote>

Anyway, as soon as I did this I decided Virtual Box it is. As it went through a 40 minute download of an image (??) it finished and displayed…

```bash
$ vagrant up --provider=vmware_fusionBringing machine 'default' up with 'vmware_fusion' provider...
[default] VMware requires root privileges to make many of the changes
necessary for Vagrant to control it. In a moment, Vagrant will ask for
your administrator password in order to install a helper that will have
permissions to make these changes. Note that Vagrant itself continues
to run without administrative privileges.
Password:
[default] Box 'bosh-solo-0.6.4' was not found. Fetching box from specified URL for
the provider 'vmware_fusion'. Note that if the URL does not have
a box for this provider, you should interrupt Vagrant now and add
the box yourself. Otherwise Vagrant will attempt to download the
full box prior to discovering this error.
Downloading or copying the box...
Extracting box...te: 119k/s, Estimated time remaining: --:--:--)
The box you attempted to add doesn't match the provider you specified.

Provider expected: vmware_fusion
Provider of box: virtualbox
```

… because the image isn’t available for vmware according to Vagrant, so for now, with some solutions and more questions I’m just going to go with the Virtual Box Solution and get back on track with the larger picture blog entry I’m writing. Thanks to [@brianmmclain](http://twitter.com/brianmmclain), [@mitchelh](http://twitter.com/mitchelh), [@jeffsussna](http://twitter.com/jeffsussna) and [@thoward37](http://twitter.com/thoward37).
