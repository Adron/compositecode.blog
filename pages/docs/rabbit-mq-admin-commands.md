---
layout: page
title: Rabbit MQ – Admin Commands
date: 2015-05-19 10:16:24 -0700
last_modified_at: 2015-05-19 10:18:21 -0700
permalink: /docs/rabbit-mq-admin-commands/
slug: rabbit-mq-admin-commands
wp_id: 11042
original_url: https://compositecode.blog/docs/rabbit-mq-admin-commands/
---

[Home](http://compositecode.com/) > [Docs](/docs/) >

### Using rabbitmq.com APT Repository

- Add the following line to your /etc/apt/sources.list:

  ```bash
  deb http://www.rabbitmq.com/debian/ testing main
  ```
- (optional) To avoid warnings about unsigned packages, add the Rabbit MQ [public key](https://www.rabbitmq.com/rabbitmq-signing-key-public.asc) to your trusted key list using apt-key(8):

  ```bash
  wget https://www.rabbitmq.com/rabbitmq-signing-key-public.asc
  sudo apt-key add rabbitmq-signing-key-public.asc
  ```

  Our public signing key is also [available from Bintray](https://bintray.com/user/downloadSubjectPublicKey?username=rabbitmq).
- Run apt-get update.
- Install packages as usual; for instance,

  ```bash
  sudo apt-get install rabbitmq-server
  ```

## Start & Stop the Server

```bash
invoke-rc.d rabbitmq-server stop/start/etc.
```

To stop and check on the status of the server, run these two commands.

```bash
rabbitmqctl stop
rabbitmqctl status
```

## Security and Ports

SELinux and similar mechanisms may prevent RabbitMQ from binding to a port. When that happens, RabbitMQ will fail to start. Make sure the following ports can be opened:

- 4369 (epmd), 25672 (Erlang distribution)
- 5672, 5671 (AMQP 0-9-1 without and with TLS)
- 15672 (if management plugin is enabled)
- 61613, 61614 (if STOMP is enabled)
- 1883, 8883 (if MQTT is enabled)

## Default user access

The broker creates a user guest with password guest. Clients not configured will use these credentials. These credentials are only be used when connecting to the broker as localhost so accounts are needed for deployed use.

See the documentation on [access control](https://www.rabbitmq.com/access-control.html) for information on how to create more users, delete the guest user, or allow remote access to the guest user.
