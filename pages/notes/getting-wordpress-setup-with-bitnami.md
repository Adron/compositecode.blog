---
layout: page
title: Getting WordPress Setup With Bitnami
date: 2014-01-29 17:14:43 -0800
last_modified_at: 2014-01-29 17:17:20 -0800
permalink: /notes/getting-wordpress-setup-with-bitnami/
slug: getting-wordpress-setup-with-bitnami
wp_id: 9594
original_url: https://compositecode.blog/notes/getting-wordpress-setup-with-bitnami/
---

Back to [Full Notes Listing](http://compositecode.com/write-up-series/notes/).

## Setting Up Domain Names

<http://wiki.bitnami.com/Applications/BitNami_Wordpress_Stack#How_to_change_the_WordPress_domain_name.3f>

If you are using a WordPress version higher than 3.3.1-5 version, you only have to specify your domain name in the installdir/apps/wordpress/htdocs/wp-config.php file. You can replace the following lines with your domain name:
define(‘WP\_SITEURL’, ‘<http://&#8217>; . $\_SERVER[‘HTTP\_HOST’] . ‘/wordpress’);
define(‘WP\_HOME’, ‘<http://&#8217>; . $\_SERVER[‘HTTP\_HOST’] . ‘/wordpress’);
with
define(‘WP\_SITEURL’, ‘<http://blog.deconstructed.io&#8217>;);
define(‘WP\_HOME’, ‘<http://blog.deconstructed.io&#8217>;);
If you have previously removed the “/wordpress” prefix from the URL, do not specify it.
How to create a full backup of WordPress?

Then Tried….
<http://stackoverflow.com/questions/12898094/having-problems-changing-the-default-url-to-root-in-wordpress>

That worked…

## Backing Up

Because BitNami stacks are self-contained, the simplest option for performing your backups is to copy or compress the BitNami Stack installation directory. To do so in a safe manner, you will need to stop all servers, so this method may not be appropriate if you have people accessing the application continously.
linux\_platform.png On Linux and OS X:mac\_platform.png
$ cd installdir
$ ./ctlscript.sh stop
$ cp -r installdir application-backup
Or you can create a tarball:
$ tar -czvf application-backup.tar.gz installdir
Or a zip file:
$ zip -r application-backup.zip installdir/\*
To restore this backup you only need to uncompress the backup in the same location. It is important to use the same path that was used when the stack was originally installed.
For example if you have a backup in a Red Hat machine, you can copy it to an Ubuntu Linux machine (a different distro!) in the same location. Then start the servers and that’s all.
$ cd installdir
$ ./ctlscript.sh start
You just need to be carefull to keep the same permissions for the files and folders. If you installed as root make sure that in the new machine you copy the files also as root. And this case, if you are also moving MySQL or PostgreSQL, you will need to create those users in the new machine (if they don’t exist yet).
