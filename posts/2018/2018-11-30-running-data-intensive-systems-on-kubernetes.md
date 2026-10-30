---
title: Lena presents “So You Want to Run Data-Intensive Systems on Kubernetes”
date: 2018-11-30 11:03:44 -0800
last_modified_at: 2018-11-30 11:03:47 -0800
permalink: /2018/11/30/running-data-intensive-systems-on-kubernetes/
slug: running-data-intensive-systems-on-kubernetes
wp_id: 14972
original_url: https://compositecode.blog/2018/11/30/running-data-intensive-systems-on-kubernetes/
categories:
- Distributed Things
- Meetups n' Such
- Unknown Code Ramblings
tags:
- apache
- cassandra
- distributed computing
- distributed systems
- elasticsearch
- kafka
- redis
- scalability
- seattle scalability
- tensorflow
excerpt: If you’re interested in running data-intensive systems (think Apache Cassandra, DataStax Enterprise, Kafka, Spark, Tensorflow, Elasticsearch, Redis, etc) in Kubernetes this is a great talk. @Lenadroid covers what options are available in Kubernetes, how architectural features around pods, jobs, stateful sets, and replica sets work together to provide distributed systems capabilities. Other features she continues …
image: /wp-content/uploads/2018/11/lenastalk.png
---

If you’re interested in running data-intensive systems (think Apache Cassandra, DataStax Enterprise, Kafka, Spark, Tensorflow, Elasticsearch, Redis, etc) in Kubernetes this is a great talk. [@Lenadroid](https://twitter.com/lenadroid) covers what options are available in Kubernetes, how architectural features around pods, jobs, stateful sets, and replica sets work together to provide distributed systems capabilities. Other features she continues and delves into include custom resource definitions (CRDs), operators, and HELM Charts, which include future and peripheral feature capabilities that can help you host various complex distributed systems. I’ve included references below the video here, enjoy.

<iframe allowfullscreen="true" class="youtube-player" height="486" loading="lazy" sandbox="allow-scripts allow-same-origin allow-popups allow-presentation allow-popups-to-escape-sandbox" src="https://www.youtube.com/embed/M0jPxoEdh8w?version=3&amp;rel=1&amp;showsearch=0&amp;showinfo=1&amp;iv_load_policy=1&amp;fs=1&amp;hl=en-US&amp;autohide=2&amp;wmode=transparent" style="border:0;" width="863"></iframe>

**References:**

- [Kubernetes Docs](https://kubernetes.io/docs/home/)
- [Kubernetes Customer Resource Definitions (CRD’s)](https://kubernetes.io/docs/tasks/access-kubernetes-api/custom-resources/custom-resource-definitions/)
- [Kubernetes Operators](https://coreos.com/blog/introducing-operators.html)
- [Helm Charts](https://docs.helm.sh/)
- *Systems*: [Apache Cassandra](http://cassandra.apache.org/), [DataStax Enterprise](https://docs.datastax.com/en/landing_page/doc/landing_page/current.html), [Apache Kafka](https://kafka.apache.org/), [Apache Spark](https://spark.apache.org/), & [Redis](https://redis.io/).
- Follow Lena on Twitter [@lenadroid](https://twitter.com/lenadroid).
