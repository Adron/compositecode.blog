---
title: WordPress on Amazon Web Services (AWS) Linux EC2 Micro Instance, For Free
date: 2011-03-29 04:07:20 -0700
last_modified_at: 2011-03-29 18:18:41 -0700
permalink: /2011/03/29/aws-linux-ec2-wordpress-free/
slug: aws-linux-ec2-wordpress-free
wp_id: 2442
original_url: https://compositecode.blog/2011/03/29/aws-linux-ec2-wordpress-free/
categories:
- AWS
- How-to
- Video
tags:
- aws
- ec2
- linux
- wordpress
excerpt: I’ve been wanting to get a write up done for Wordpress on AWS, the fact that it is free for a year, since they’ve released the free-tier many months ago. Well I finally got around to it, however it isn’t a write up. I went ahead and put the work in to produce a video of the steps for setup & configuration. Enjoy. The commands to install php, mysql, httpd (apache), and manipulate the config files are included below for copy and paste needs.
---

I’ve been wanting to get a write up done for WordPress on AWS, the fact that it is free for a year, since they’ve released the free-tier many months ago. Well I finally got around to it, however it isn’t a write up. I went ahead and put the work in to produce a video of the steps for setup & configuration. Enjoy.

**`<iframe allow="clipboard-write; presentation" allowfullscreen="" aria-label="VideoPress Video Player" data-resize-to-parent="true" frameborder="0" height="538" src="https://videopress.com/embed/VAiI7dqy?hd=1&amp;cover=1&amp;loop=0&amp;autoPlay=0&amp;permalink=1&amp;muted=0&amp;controls=1&amp;playsinline=0&amp;useAverageColor=0&amp;preloadContent=metadata" title="VideoPress Video Player" width="862"></iframe>`**

The commands to install php, mysql, httpd (apache), and manipulate the config files are included below for copy and paste needs.

> Create a Linux Instance on AWS – create & assign an IP Address
>
> Login with ‘ec2-user’
>
> sudo -i
> lsof -i
>
> yum -y install httpd
>
> service httpd start
>
> yum -y install php mysql
> yum install mysql-server
>
> wget <http://packages.sw.be/rpmforge-release/rpmforge-release-0.3.6-1.el5.rf.i386.rpm>
> rpm -Uvh rpmforge-release-0.3.6-1.el5.rf.i386.rpm
> yum install phpmyadmin
>
> vi /etc/httpd/conf.d/phpmyadmin.conf
>
> Hit insert hey to make changes to the conf file.
>
> ————————————————————————————
> # Web application to manage MySQL
>
> # Order Deny,Allow
> # Deny from all
> Allow from all
>
> Alias /phpmyadmin /usr/share/phpmyadmin
> Alias /phpMyAdmin /usr/share/phpmyadmin
> Alias /mysqladmin /usr/share/phpmyadmin
> ————————————————————————————
>
> service httpd restart
> service mysqld start
> /usr/bin/mysqladmin -u root password ‘somepassword’
> vi /etc/httpd/conf.d/phpmyadmin.conf
> vi /usr/share/phpmyadmin/config.inc.php
>
> ————————————————————————————
> […] /\* Authentication type \*/
> $cfg[‘Servers’][$i][‘auth\_type’] = ‘http’;
> […]
> ————————————————————————————
>
> Watch the video for the WordPress Database creation in mysql w/ phpmyadmin.
>
> wget <http://wordpress.org/latest.tar.gz>
> tar -xzvf latest.tar.gz -C /var/www/html/
> cp -avr /var/www/html/wordpress/\* /var/www/html/
> rm -rf /var/www/html/wordpress/
>
> cd /etc/httpd/conf
> vi httpd.conf
> Find the user here… it should be ‘apache’
>
> cp /var/www/html/wp-config-sample.php /var/www/html/wp-config.php
> vi /var/www/html/wp-config.php
>
> …Add the database settings.
>
> chown -R apache /var/www/html
> chmod -R 755 /var/www/html
