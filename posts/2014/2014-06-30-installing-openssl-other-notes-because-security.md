---
title: 'Installing OpenSSL, Other Notes. Because: Security'
date: 2014-06-30 16:25:25 -0700
last_modified_at: 2014-06-30 16:48:33 -0700
permalink: /2014/06/30/installing-openssl-other-notes-because-security/
slug: installing-openssl-other-notes-because-security
wp_id: 10058
original_url: https://compositecode.blog/2014/06/30/installing-openssl-other-notes-because-security/
categories:
- How-to
tags:
- certificate
- certificate signing request
- csr
- openssl
- ssl
- x.509
- x509
excerpt: I am in the process of setting up an SSL (Secure Sockets Layer) Cert to enable HTTPS on some sites and APIs I’m building. In that effort I needed to setup OpenSSL to create a CSR (Certificate Signing Request) and get the process started. Here’s the steps I went through to accomplish this. First download …
---

![](https://photos.adron.me/Software/Sharepoint/Sharepoint2010andanalytics/i-gXWn5rQ/0/O/1269363482_connect_to_network.png)I am in the process of setting up an SSL ([Secure Sockets Layer](http://en.wikipedia.org/wiki/Secure_Sockets_Layer)) Cert to enable HTTPS on some sites and APIs I’m building. In that effort I needed to setup OpenSSL to create a CSR (Certificate Signing Request) and get the process started. Here’s the steps I went through to accomplish this. First [download OpenSSL](http://www.openssl.org/source/).

Next make sure you have the prerequisites installed:

- make
- Perl 5
- ANSI C Compiler
- Dev Environment  in form of dev libraries and C header files
- Supported Unix Operating System (i.e. – not windows, you’ll have to google those directions separately, for these steps though, get a \*nix OS)

Get the zipped contents of the OpenSSL into a working directory to build them. Then follow the standard config, make, and make install steps below.

```bash
./config
make
make test
make install
```

Once you have that installed there are a number of actions you can perform. Here’s a few.

- Create a CSR (Certificate Signing Request):

  ```bash
  openssl req -out CSR.csr -new -newkey rsa:2048 -nodes -keyout privateKey.key
  ```

  This creates a CSR.csr and privateKey.key file for use for SSL.
- Create a self-signed certificate:

  ```bash
  openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout privateKey.key -out certificate.crt
  ```

  Self signed certificates are great to use on local servers that are used internally, great for dev servers that need SSL, and similar reasons. For most dev needs there is no need to purchase an extra certificate for SSL, just generate one yourself and use it for development purposes.
- Check a CSR:

  ```bash
  openssl req -text -noout -verify -in CSR.csr
  ```
- Check a private key:

  ```bash
  openssl rsa -in privateKey.key -check
  ```
- Check a cert:

  ```bash
  openssl x509 -in certificate.crt -text -noout
  ```
- Generate a cert signing request from existing cert:

  ```bash
  openssl x509 -x509toreq -in certificate.crt -out CSR.csr -signkey privateKey.key
  ```
- Removing a pass key:

  ```bash
  openssl rsa -in privateKey.pem -out newPrivateKey.pem
  ```
- Generate a CSR for an existing private key:

  ```bash
  openssl req -out CSR.csr -key privateKey.key -new
  ```

More to come in the near future. I’ve almost got this SSL mess straightened out and am putting together a more complete how-to.

References:

- [OpenSSL](https://www.openssl.org/)
- [SSL Defined @ Wikipedia](http://en.wikipedia.org/wiki/Secure_Sockets_Layer)
