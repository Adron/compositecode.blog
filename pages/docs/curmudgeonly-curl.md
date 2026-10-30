---
layout: page
title: Curmudgeonly cURL
date: 2013-11-30 18:18:50 -0800
last_modified_at: 2015-09-02 19:16:29 -0700
permalink: /docs/curmudgeonly-curl/
slug: curmudgeonly-curl
wp_id: 9287
original_url: https://compositecode.blog/docs/curmudgeonly-curl/
---

For reference, [curmudgeonly](http://www.thefreedictionary.com/curmudgeon). We all love a good curmedgeonly old fart, sometimes that’s exactly what cURL is, it has after all been around for a long time in tech years!

```bash
curl http://0.0.0.0:8080/hello/Adron
```

The straight usage of curl does a get against the URI and returns the response body of the request made.

```bash
curl -i http://0.0.0.0:8080/hello/Adron
```

or

```bash
curl --include http://0.0.0.0:8080/hello/Adron
```

The -i returns the header info of the response of the request made. It is the same as the –include option.

```bash
curl -H "connection: close" http://0.0.0.0:8080/hello/Adron
```

This curl command adds the connection: close option to the GET request to the curl command. The server then, instead of leaving the connection open afterwards immediately closes the connection and shows this in the response.

The commands above can be combined, as can others, into commands such as this.

```bash
curl -iH "connection: close" http://0.0.0.0:8080/hello/Adron
```
