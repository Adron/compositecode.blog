---
title: PIP Install Trash Fire – AWS CLI Issues & Fixes for Installation
date: 2018-10-05 09:03:19 -0700
last_modified_at: 2018-10-05 09:19:11 -0700
permalink: /2018/10/05/pip-install-trash-fire-aws-cli-issues-fixes-for-installation/
slug: pip-install-trash-fire-aws-cli-issues-fixes-for-installation
wp_id: 14702
original_url: https://compositecode.blog/2018/10/05/pip-install-trash-fire-aws-cli-issues-fixes-for-installation/
categories:
- Unknown Code Ramblings
tags: []
excerpt: I sat down again, for about the eight billionth time to install AWS’s CLI and get to work against some infrastructure. For at least the gazillionth time I get a stupid error, that at this point I really feel the installation process ought to ignore, mitigate, or otherwise handle. But anyway, here’s one very common …
---

I sat down again, for about the eight billionth time to install AWS’s CLI and get to work against some infrastructure. For at least the gazillionth time I get a stupid error, that at this point I really feel the installation process ought to ignore, mitigate, or otherwise handle. But anyway, here’s one very common issue that keeps popping up over and over if you’ve got *six* installed already that isn’t the version that `awscli` wants (or doesn’t want).

![pip-install.png](/wp-content/uploads/2018/10/pip-install.png)

*Found existing installation: six 1.4.1
Cannot uninstall ‘six’. It is a distutils installed project and thus we cannot accurately determine which files belong to it which would lead to only a partial uninstall.*

The quick solution to this is to just tell `pip` to ignore the existing six installation.

```bash
pip install awscli --ignore-installed six --user
```

I did a quick search too, just to see what others had found and it looked like this wasn’t an entirely uncommon issue. On [Stackoverflow there’s this same issue coming up with other installations](https://stackoverflow.com/questions/50954182/python-cannot-uninstall-six-while-pip-install-tld).

I’d love to see this, and about a dozen other odd issues that always come up specifically with the `awscli`. The simple fix, is for AWS just to go ahead and dig into how GCP builds `gcloud` because that CLI is easily the slickest option of the big three. But I digress, back to work on getting some infrastructure resources out there.
