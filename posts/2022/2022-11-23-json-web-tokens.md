---
title: JSON Web Tokens
date: 2022-11-23 13:52:51 -0800
last_modified_at: 2022-11-23 13:52:51 -0800
permalink: /2022/11/23/json-web-tokens/
slug: json-web-tokens
wp_id: 65628
original_url: https://compositecode.blog/2022/11/23/json-web-tokens/
categories:
- References
tags:
- javascript
- json web token
- jwt
- web
- web development
excerpt: JSON Web Tokens, one hears all about them all the time. But what exactly are they? I’ve used them a thousand times myself but I never really checked out exactly what they are. So this post fills that gap for me, and hopefully it’s useful to a few of you readers out there too. What …
---

[JSON](/2022/11/22/json-javascript-object-notation/) Web Tokens, one hears all about them all the time. But what exactly are they? I’ve used them a thousand times myself but I never really checked out exactly what they are. So this post fills that gap for me, and hopefully it’s useful to a few of you readers out there too.

## What is a JSON Web Token?

JSON Web Token, or JWT, is open standard RFC 7519 for compact and self-contained secure information transmission between two parties using JSON objects. For a refresher, JSON stands for JavaScript Object Notation. JWTs provide security between parties by being signed, which can be used the verify the integrity of the claims contained. JWTs can be signed using a secret or a public / private key pair using RSA or ECDSA. JWTs can also be encrypted to hide those claims as well.

## What are JWTs good for? When should you use a JWT?

The most common, and what I’ve found the most recommended use of JWTs, is for API authentication or server-to-server authorization.

## JWT Structure

Paraphrased and summarized using the Wikipedia example [here](https://en.wikipedia.org/wiki/JSON_Web_Token).

The header identifies which algorithm generated the signature, such as HMAC-SHA256, as indicated in the example below.

```
{
  "alg": "HS256",
  "typ": "JWT"
}
```

Then the contenxt, or payload, contains the claims. There are seven Registered Claim Names (RCN) as standard fields commonly included in tokens. Custom claims can also be included, the following is the `At Time` claim, designated `iat` and custom claim of `loggedInAs`. The others include: `iss` (issuer), `sub` (subject), `aud` (audience), `exp` (expiration time), `nbf` (not before time), `iat` (issued at time), and `jti` (JWT ID). For these and many other claims the IANA has a [resource here](https://www.iana.org/assignments/jwt/jwt.xhtml#claims).

```
{
  "loggedInAs": "admin",
  "iat": 1422779638
}
```

The signature securely validates the token. It’s calculated through encoding the header and payload using Base64url encoding per RFC 4648 and concatenated with a period as the seperator. This string is run through a cryptographic algorithm specified in the header (i.e. HMAC SHA 256). A function signature would look something like this.

```
HMAC_SHA256(
  secret,
  base64urlEncoding(header) + '.' +
  base64urlEncoding(payload)
)
```

All concatenated together the token would then look like this.

```
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJsb2dnZWRJbkFzIjoiYWRtaW4iLCJpYXQiOjE0MjI3Nzk2Mzh9.gzSraSYS8EXBxLN_oWnFSRgCzcmJmMjLiuyu5CSpyHI
```

## Do and Do Nots

- Do not use JWTs as session tokens. At least in general, they have a wider range of features and a wider scope. Session tokens are a different beast and using JWTs can increase potential mistakes. Some other issues with this is a JWT doesn’t simply can’t be removed at the end of a session, as it is self-contained without a central authority, and another is that they’re *relatively* large for such a purpose.
- Do use JWTs for API Authentication. This is the most common use for JWTs today, as it fits the use case and in many ways was designed specifically for it.
- Do use a library or some other known way to generate JWT tokens. Don’t just randomly generate a string that *looks like* a JWT. I’ve seen people just generate a big ole’ wad of text that looks like a JWT before but then it is literally just a big wad of text, you can’t fake a JWT, and in turn when it’s verified or processed by a library for authentication purposes you’ll end up with errors and other issues.
