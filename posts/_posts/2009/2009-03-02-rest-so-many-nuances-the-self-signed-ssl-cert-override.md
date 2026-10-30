---
title: REST, So Many Nuances, The Self Signed SSL Cert Override
date: 2009-03-02 08:36:25 -0800
last_modified_at: 2009-03-02 08:36:25 -0800
permalink: /2009/03/02/rest-so-many-nuances-the-self-signed-ssl-cert-override/
slug: rest-so-many-nuances-the-self-signed-ssl-cert-override
wp_id: 593
original_url: https://compositecode.blog/2009/03/02/rest-so-many-nuances-the-self-signed-ssl-cert-override/
categories:
- Uncategorized Bits
tags: []
excerpt: Another thing that comes up frequently is the need to do development internally against some REST Services that have SSL as the transport. If this is your case, in client code you’ll need to toss a delegate in to actually get past the SSL Self Signed Cert and get to the rest of your REST …
---

Another thing that comes up frequently is the need to do development internally against some REST Services that have SSL as the transport.  If this is your case, in client code you’ll need to toss a delegate in to actually get past the SSL Self Signed Cert and get to the rest of your REST Services authentication or whatever else is next in the process.  Here’s a code snippet on how to toss a delegate in.

```
textResults.Text = DateTime.Now.ToLongTimeString() + "\n";
if (!textUriRoot.Text.EndsWith("/"))
    textUriRoot.Text += "/";
string baseUri = textUriRoot.Text + ProfileUri;
MessageBox.Show(baseUri, "Using URI", MessageBoxButton.OK, MessageBoxImage.Information, MessageBoxResult.OK);

// Deal with the self signed SSL certificate.
ServicePointManager.ServerCertificateValidationCallback = delegate { return true; };

var webClient = new WebClient();
webClient.Credentials = new NetworkCredential(@"username", @"password");
webClient.DownloadStringCompleted += GetProfiles;
webClient.DownloadStringAsync(new Uri(baseUri));
```

.csharpcode, .csharpcode pre
{
font-size: small;
color: black;
font-family: consolas, “Courier New”, courier, monospace;
background-color: #ffffff;
/\*white-space: pre;\*/
}
.csharpcode pre { margin: 0em; }
.csharpcode .rem { color: #008000; }
.csharpcode .kwrd { color: #0000ff; }
.csharpcode .str { color: #006080; }
.csharpcode .op { color: #0000c0; }
.csharpcode .preproc { color: #cc6633; }
.csharpcode .asp { background-color: #ffff00; }
.csharpcode .html { color: #800000; }
.csharpcode .attr { color: #ff0000; }
.csharpcode .alt
{
background-color: #f4f4f4;
width: 100%;
margin: 0em;
}
.csharpcode .lnum { color: #606060; }
