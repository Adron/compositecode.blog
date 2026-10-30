---
layout: page
title: Elastic Beanstalk – Setting up ‘eb’ Command Line Tools
date: 2013-12-06 00:36:05 -0800
last_modified_at: 2013-12-06 01:16:29 -0800
permalink: /amazon-web-services/elastic-beanstalk-setting-up-eb-command-line-tools/
slug: elastic-beanstalk-setting-up-eb-command-line-tools
wp_id: 9313
original_url: https://compositecode.blog/amazon-web-services/elastic-beanstalk-setting-up-eb-command-line-tools/
---

1. Download the **[command line tools](http://aws.amazon.com/code/6752709412171743)**.
2. Unzip/tar and place the directory in a location that you want to keep the tools in. Usually something like *etc/AWStools*.
3. Open the .bash\_profile and add the following line to it.

   ```bash
   export PATH=$PATH:/Users/adronhall/Coderz/AWS-ElasticBeanstalk-CLI-2.5.1/eb/macosx/python2.7/
   ```
4. Restart the terminal/bash and type eb, eb –help or eb status. You’ll see these results based on what you’ve typed.

   ```bash
   $ eb
   Error: too few arguments
   usage: eb {COMMAND} [options]
   Try eb --help for more information.

   $ eb status
   The configuration file, "config", cannot be found. Use the "init" command to create it.

   $ eb --help
   usage: eb {COMMAND} [options]

   AWS Elastic Beanstalk Command Line Interface v2.5.1

   positional arguments:
     COMMAND               init, branch, start, status, update, stop, delete,
                           logs, events, push
     SUBCOMMAND
   ```

   …etc., etc., etc., etc
5. Now enjoy the use of the Amazon Web Services Elastic Beanstalk CLI Tool.
