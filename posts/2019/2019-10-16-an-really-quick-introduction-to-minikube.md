---
title: A Really Quick Introduction to Minikube
date: 2019-10-16 10:54:04 -0700
last_modified_at: 2019-10-26 16:08:16 -0700
permalink: /2019/10/16/an-really-quick-introduction-to-minikube/
slug: an-really-quick-introduction-to-minikube
wp_id: 16412
original_url: https://compositecode.blog/2019/10/16/an-really-quick-introduction-to-minikube/
categories:
- Kubernetes
- Unknown Code Ramblings
tags:
- containers
- docker
- k8s
- Kubernetes
- minikube
excerpt: There’s likely a million introductions to Minikube, but I wanted one of my own. Thus, here you go! Minikube is basically Kubernetes light that runs on your own machine. Albeit, it does this similarly to how Docker used to do it, via a virtual machine. Thus, you can do some things with it but if …
image: /wp-content/uploads/2019/10/logo.png
---

There’s likely a million introductions to [Minikube](https://minikube.sigs.k8s.io/), but I wanted one of my own. Thus, here you go!  Minikube is basically [Kubernetes](https://kubernetes.io/) *light* that runs on your own machine. Albeit, it does this similarly to how Docker used to do it, via a virtual machine. Thus, you can do some things with it but if you want to get serious you’ll still need to spool up a proper cluster somewhere as it will start to bog down your machine with any heavy workloads.

## 1: Minikube – Installing

Linux Direct:

```shell
 curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64 \
   && sudo install minikube-linux-amd64 /usr/local/bin/minikube
```

Linux Debian:

```shell
 curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64 \
   && sudo install minikube-linux-amd64 /usr/local/bin/minikube
```

Linux Red Hat:

```shell
curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-1.4.0.rpm \
 && sudo rpm -ivh minikube-1.4.0.rpm
```

## 2: Starting Minikube

`minikube start` will start a minikube instance, pulling images, resources, kubelets, kubeadm, dashboard, and all those resources.

![00-starting](/wp-content/uploads/2019/10/00-starting.png)

## 3: Stopping Minikube

`minikube stop` brings the minikube service to a stop, allowing for restart later.

![09-stopping-minikube](/wp-content/uploads/2019/10/09-stopping-minikube.png)

## 4. Deleting Minikube

`minikube delete` will delete the minikube. This will delete any of the content or related collateral that was running in the minikube.

![01-delete](/wp-content/uploads/2019/10/01-delete.png)

## 5. Restarting after Delete

`minikube start` this is the way to restart a minikube instance after you’ve stopped the instance. It’s also the way start a minikube, as shown above.

![03-restarting-after-delete](/wp-content/uploads/2019/10/03-restarting-after-delete.png)

## 6. Starting a Named Minikube

If you want a named minikube instance, use the -p switch, with a command like `minikube start -p adrons-minikube`.

![04-minikube-with-name](/wp-content/uploads/2019/10/04-minikube-with-name.png)

## 7. Starting & Using the Dashboard

To check out the dashboard, that pretty Google dashboard for Kubernetes, run `minikube dashboard` to bring that up.

![05-starting-dashboard](/wp-content/uploads/2019/10/05-starting-dashboard.png)

![06-minikube-dashboard.png](/wp-content/uploads/2019/10/06-minikube-dashboard.png)

## 8. Status!

To get a quick update on the current state of the minikube instance just run `minikube status`.

![07-other-minikube-commands](/wp-content/uploads/2019/10/07-other-minikube-commands.png)

## 9. Starting Minikube sans a Virtual Machine

This is, albeit I may be mistaken, this is a Linux only feature. Run `minikube start --vm-driver=none` and it’ll kick off a minikube right there on your local machine.

![09-minikube-no-vm-started.png](/wp-content/uploads/2019/10/09-minikube-no-vm-started.png)

**References:**

- [Minikube Repo](https://github.com/kubernetes/minikube)
