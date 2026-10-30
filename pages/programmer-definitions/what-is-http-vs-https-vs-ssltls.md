---
layout: page
title: What is HTTP vs. HTTPS vs. SSL/TLS?
date: 2014-12-14 18:30:28 -0800
last_modified_at: 2018-04-19 15:12:39 -0700
permalink: /programmer-definitions/what-is-http-vs-https-vs-ssltls/
slug: what-is-http-vs-https-vs-ssltls
wp_id: 10504
original_url: https://compositecode.blog/programmer-definitions/what-is-http-vs-https-vs-ssltls/
---

- **H**yper**t**ext **T**ransfer **P**rotocol or **HTTP**: This is the standard application protocol layer that all web traffic operates over. Other transports do exist, but this is the standard known and used by the vast majority of anything that is on the public internet. For the discussion in this article, I’ll be using this as the basic transport assumption throughout the article.
- **HTTP** **S**ecure or **HTTPS**: Hypertext Transport Protocol Secure is standard HTTP layered on/under(?) TLS or SSL based protocols for security.
- **S**ecure **S**ockets **L**ayer or **SSL**: A cryptographic protocol designed to provide communication securely on the internet. They use X.509 certificates to prove asymmetric cryptography to authenticate the counterparty with whom they are communicating and exchange a symmetric key. The session key is then used to encrypt data that travels between the parties over HTTP. This, in theory, provides message confidentiality, authentication codes and respectively message authentication. A key feature concept is forward secrecy, which insures the short-term session key cannot be derived form the long-term asymmetric secret key. This is used in web browsing, API services, email, internet faxes, instant messaging and voice over IP (VoIP).
- **T**ransport **L**ayer **S**ecurity or **TLS**: TLS is the successor of SSL and provides a more modern level of security that SSL v2 or v3. SSL v2 is generally even turned off in every major browser and considered to be insecure under most circumstances. As a cryptographic protocol TLS is designed similarly to SSL to stop man-in-the-middle, tapping and related attacks.
