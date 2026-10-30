---
title: Hasura 2.0 – A Short Story of v1.3.3 to v2.0 Upgrades
date: 2021-02-23 14:34:33 -0800
last_modified_at: 2021-02-23 14:49:47 -0800
permalink: /2021/02/23/hasura-2-a-short-story/
slug: hasura-2-a-short-story
wp_id: 63506
original_url: https://compositecode.blog/2021/02/23/hasura-2-a-short-story/
categories:
- graphql
tags:
- api
- azure
- graphql
- hasura
- hasura v2
- rest
- rest api
- restful
- terraform
excerpt: Today at Hasura we released Hasura v2.0! This is a pretty major release with a number of new features that will dramatically increase the capabilities for Hasura. For several of my projects, specifically the infrastructure as code projects terrazura and tenancy-bydata I was able to get the upgrade to Hasura v2.0 done in moments!
image: /wp-content/uploads/2021/02/Terrazura-updated.png
---

Today at [Hasura](https://hasura.io/) we released [Hasura v2.0](https://hasura.io/blog/announcing-hasura-graphql-engine-2-0/)! This is a pretty major release with a number of new features that will dramatically increase the capabilities for Hasura. For several of my projects, specifically the infrastructure as code projects *[terrazura](https://adron.github.io/terrazura/)* (***[check out the previous blog post w/ video time points and more](/2021/02/19/terrazura-a-build-out-of-an-azure-based-hasura-graphql-api-on-postgres/)***) and *[tenancy-bydata](https://github.com/adron/tenancy-bydata)* I was able to get the upgrade to [Hasura v2.0](https://hasura.io/blog/announcing-hasura-graphql-engine-2-0/) done in moments! Since I don’t have to pull backups or anything for these projects, it merely involved the following steps.

1. Upgrade the Hasura CLI. This is super easy, just issue the command `hasura update-cli --version v2.0.0-alpha.1`. This command will then download and update the CLI.
2. Next I updated the Terraform file so the container pulls the latest version `image = "hasura/graphql-engine:v2.0.0-alpha.1"`.

Next run an updated `terraform apply` command, which in my case is this command in the case of the *[terrazura](https://adron.github.io/terrazura/)* project for example.

```
terraform init

terraform apply -auto-approve \
  -var 'server=terrazuraserver' \
  -var 'username='$PUSERNAME'' \
  -var 'password='$PPASSWORD'' \
  -var 'database=terrazuradb' \
  -var 'apiport=8080'

cd migrations

hasura migrate apply
```

Boom! Everything is now updated to v2.0 and we’re ready for all the upcoming Twitch streams relating back to these particular projects!

For more, be sure to subscribe to the [HasuraHQ Twitch](https://twitch.tv/hasurahq) Channel and my Twitch Channel [Thrashing Code](https://twitch.tv/thrashingcode) as I’ll be covering more of the new features in the coming days!
