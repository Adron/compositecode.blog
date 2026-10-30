---
layout: page
title: WordPress on Ubuntu
date: 2014-01-10 11:45:36 -0800
last_modified_at: 2014-01-10 14:07:46 -0800
permalink: /wordpress-on-ubuntu/
slug: wordpress-on-ubuntu
wp_id: 9514
original_url: https://compositecode.blog/wordpress-on-ubuntu/
---

First, get the LAMP stack running.

```bash
sudo apt-get install lamp-server^
sudo apt-get install php5 php5-gd php5-mysql php5-curl php5-cli php5-cgi php5-dev
sudo apt-get install phpmyadmin
```

Now get some WordPress happening.

```bash
sudo apt-get install wordpress
sudo ln -s /usr/share/wordpress /var/www/wordpress
```

Then a few More Commands for Setup

```bash
sudo bash /usr/share/doc/wordpress/examples/setup-mysql -n wordpress localhost
```

If you know this info related to your URI/Domain, doing this will get ya mapped up.

```bash
sudo bash /usr/share/doc/wordpress/examples/setup-mysql -n wordpress_preciseserver blog.preciseserver.com
```

Set some permissions

```bash
sudo chown -R www-data /usr/share/wordpress
```
