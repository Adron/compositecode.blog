---
title: DataStax Enterprise Kubernetes Operator Release
date: 2019-12-03 08:45:58 -0800
last_modified_at: 2020-04-16 09:17:13 -0700
permalink: /2019/12/03/datastax-enterprise-kubernetes-operator-release/
slug: datastax-enterprise-kubernetes-operator-release
wp_id: 16553
original_url: https://compositecode.blog/2019/12/03/datastax-enterprise-kubernetes-operator-release/
categories:
- kubecon
- Kubernetes
tags:
- k8s
- k8s operator
- kubecon
- kubecon 2019
- Kubernetes
- kubernetes operator
excerpt: Recently KubeCon 2019 was held in San Diego. I was intending to go but things came up and I had to alter my plans. Even without attending I still was able to accrue a lot of the details from people attending and just kind of watching the Twittersphere. Twitter is, contrary to a lot of …
image: /wp-content/uploads/2019/10/logo.png
---

Recently KubeCon 2019 was held in San Diego. I was intending to go but things came up and I had to alter my plans. Even without attending I still was able to accrue a lot of the details from people attending and just kind of watching the Twittersphere. Twitter is, contrary to a lot of conversations, very useful sometimes. At DataStax where I work we had our own release at KubeCon for our DataStax Enterprise – AKA ‘DSE’ – Kubernetes – AKA ‘K8s’ Operator.

With KubeCon wrapped up I got to catch up with Christopher Bradford about this release of the DSE K8s Operator on the Distributed Data Show – AKA DDS. Here’s the podcast of the DDS DSE K8s episode talking points:

- 00:30 – 01:12 The not secret name of the DataStax Enterprise Operator for Kubernetes, or as I call it the DSE K8s Operator.
- 01:13 – 02:28 Discussing KubeCon, which reached 12k attendees this year!
- 02:29 – 04:19 What is the DataStax mission in creating a K8s Operator? How to squelch the complexity of Kubernetes!
- 04:20 – 06:06 Delving into the idea behind custom resources, architectural setup around “[Cassandra Racks and Datacenters](/2018/10/29/cassandra-datacenter-racks/)” and how that maps to Kubernetes and the Operator managing these within a Kubernetes Cluster.
- 06:07 – 07:59 Where do the container images live, who maintains them, and how can you get them for use with Kubernetes?
- 08:00 – 11:59 What about support, business impacts, and what are the plans for the human operators around this? How can a company get support for this product?
- 12:00 – 15:28 What about he other Kubernetes Operators for Apache Cassandra? Well, we discuss some of the options (see links below under the references) and the differences between those operators and the DSE Operator.
- 15:29 – 23:14 It’s important to discuss the current state of stateful workloads. Elaborating on how we can have pets and not just cattle for specific systems like this in Kubernetes now!
- 23:15 – 25:13 Last minute thoughts on KubeCon & Kubernetes.
- 25:14 – [end] Take it for a test spin in beta! Mentions for more materials, references, etc, which I’ve posted below.

Here’s the podcast, “**First Look at the DSE Kubernetes Operator with Christopher Bradford | Episode 128 Distributed Data Show**”

- [Podcast on iTunes](https://podcasts.apple.com/us/podcast/first-look-at-dse-kubernetes-operator-christopher-bradford/id1261618796?i=1000458545791)

<https://soundcloud.com/datastaxdevelopers/first-look-at-the-dse-kubernetes-operator-with-chris-bradford-ep-128-the-distributed-data-show>

References for K8s Operators for DSE & Apache Cassandra:

- K8s Operators for DataStax Enterprise

  1. <https://github.com/datastax/labs/tree/master/dse-k8s-operator>
  2. <https://www.datastax.com/blog/2019/11/simplifying-datastax-enterprise-deployments-kubernetes-containerized-workflows>
  3. <https://www.datastax.com/dev/kubernetes>

  K8s Operators for Apache Cassandra

  1. <https://github.com/jetstack/navigator>
  2. <https://github.com/vgkowski/cassandra-operator>
  3. <https://github.com/Orange-OpenSource/cassandra-k8s-operator>
  4. <https://github.com/instaclustr/cassandra-operator>
