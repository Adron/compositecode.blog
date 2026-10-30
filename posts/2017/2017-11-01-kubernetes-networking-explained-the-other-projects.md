---
title: Kubernetes Networking Explained & The Other Projects
date: 2017-11-01 09:17:42 -0700
last_modified_at: 2017-11-01 09:17:42 -0700
permalink: /2017/11/01/kubernetes-networking-explained-the-other-projects/
slug: kubernetes-networking-explained-the-other-projects
wp_id: 13620
original_url: https://compositecode.blog/2017/11/01/kubernetes-networking-explained-the-other-projects/
categories:
- Unknown Code Ramblings
tags:
- cloud computing
- Data Diluvium
- golang
- Kubernetes
- terraform
excerpt: 'Still stumbling through determining what Kubernetes does for networking? Here’s a good piece written up by Mark Betz, titled “Understanding Kubernetes Networking: Pods”. Just reading Mark’s latest on Kubernetes is great, but definitely take a look at his other writing too, it’s a steady stream of really solid material that is insightful, helpful, and well …'
---

Still stumbling through determining what Kubernetes does for networking? Here’s a good piece written up by [Mark Betz](https://medium.com/@betz.mark), titled “[Understanding Kubernetes Networking: Pods](https://medium.com/google-cloud/understanding-kubernetes-networking-pods-7117dd28727)”. Just reading Mark’s latest on Kubernetes is great, but definitely take a look at his other writing too, it’s a steady stream of really solid material that is insightful, helpful, and well thought out. Good job Mark.

I’ve got two more blog entries on getting Kubernetes deployed and what you get with default Terraform configuration setups in Azure and AWS (The Google Cloud Platform write up is posted [here](http://blog.adron.me/articles/terraform-kubernetes-gcp/)). Once complete that’s a wrap for that series. Then I’m going shift gears again and start working on a number of elements around application and services (ala microservices) development.

Always staying nimble means always jumping around to the specific details of the things that need done! This, among many efforts to jump around to the specific thing that needs done, actually feels more like a return to familiar territory. After all, the vast majority of my work in the last many years has been writing code implemented against various environments to ensure reliable data access and available services for customers; customers being web front end devs, nurses in a hospitals, GIS workers resolving mapping conflicts, veterinarians, video watching patrons on the internet, or any host of someone using the software I’ve built.

In light of that, here’s a few extra thoughts and tidbits about what’s in the works next.

- Getting the [Data Diluvium Project](http://datadiluvium.com/) running, a core product implemented, and usable live out there on the wild web.
- Getting [blue-land-app](https://github.com/Adron/blue-land-app) (It’s a Go Service), [blue-world-noding](https://github.com/Adron/blue-world-noding) (It’s a Node.js Service), and [blue-world-making](https://github.com/Adron/blue-world-making) (It’s the infrastructure the two run on) are all working and in usable states for prospective tutorials, sample usage, and for speaking from in presentations. They’re going to be, in the end, solid examples of how to get up and running with those particular stacks + Kubernetes. A kind of a from zero to launch examples.

Other Links of Note:

- Mark’s “[Comparing Amazon Elastic Container Service and Google Kubernetes](https://medium.com/@betz.mark/comparing-amazon-elastic-container-service-and-google-kubernetes-1c63fbf19ccd)”
