---
title: Using HTTP Compression for Faster Downloads With .NET C#
date: 2009-03-24 12:07:29 -0700
last_modified_at: 2009-03-24 12:07:29 -0700
permalink: /2009/03/24/using-http-compression-for-faster-downloads-with-net-c/
slug: using-http-compression-for-faster-downloads-with-net-c
wp_id: 607
original_url: https://compositecode.blog/2009/03/24/using-http-compression-for-faster-downloads-with-net-c/
categories:
- Uncategorized Bits
tags: []
excerpt: 'IIS provides the following compression options: Static files only. Dynamic application responses only. Both static files and dynamic application responses. It is important on dynamic responses that the resource is compressed on the fly every single time it is requested. This can cause some heavy processor utilization. To enable HTTP compression (IIS 6.0) follow these …'
---

IIS provides the following compression options:

- Static files only.- Dynamic application responses only.- Both static files and dynamic application responses.

It is important on dynamic responses that the resource is compressed on the fly every single time it is requested.  This can cause some heavy processor utilization.

To enable HTTP compression (IIS 6.0) follow these steps.  You must be an adminstrator to complete these steps, so use the runas or command prompt with

```
runas /user:Administrative_AccountName"mmc %systemroot%\system32\inetsrv\iis.msc"
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

to gain access to IIS.

***…as quoted steps from*** [***Microsoft TechNet for IIS 6.0 Compression Settings***](http://www.microsoft.com/technet/prodtechnol/WindowsServer2003/Library/IIS/502ef631-3695-4616-b268-cbe7cf1351ce.mspx?mfr=true)***…***

1. To enable global HTTP compression by using IIS Manager
   In IIS Manager, double-click the local computer, right-click the Web Sites folder, and then click Properties.- Click theService tab, and in the HTTP compression section, select the Compress application files check box to enable compression for dynamic files.- Select the Compress static files check box to enable compression for static files.- In the Temporary directory box, type the path to a local directory or click Browse to locate a directory. Once a static file is compressed, it is cached in this temporary directory until it expires, or the content changes. The directory must be on the local drive of an NTFS–formatted partition. The directory cannot be compressed or shared, and the access control lists (ACLs) for the directory must include Full Control access to the identity of the application pool or to the IIS\_WPG group.- Under Maximum temporary directory size, click a folder size option. If you specify a maximum size under Limited to (in megabytes) (the default setting is 95 MB), then when the limit is reached, IIS automatically cleans up the temporary directory by applying the “least recently used” rule.- Click Apply, and then click OK.

To enable global HTTP compression by using Adsutil.vbs

1. Open a command prompt.- To enable dynamic compression, type the following at the command prompt and then press ENTER:

     ```
     cscript adsutil.vbs set w3svc/filters/compression/parameters/HcDoDynamicCompression true
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

     - To enable static compression, type the following at the command prompt and then press ENTER:

       ```
       cscript adsutil.vbs set w3svc/filters/compression/parameters/HcDoStaticCompression true
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

To enable HTTP Compression for Individual Sites and Site Elements

1. Disable global static compression by executing the following command at a command prompt:

   ```
   adsutil set w3svc/filters/compression/parameters/HcDoStaticCompression false
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

   - Enable static compression at this directory by executing the following command at a command prompt:

     ```
     adsutil set w3svc/1/root/Home/StyleSheets/DoStaticCompression true
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

To disable static compression for only a single directory, first enable global static compression (if it is disabled) and then disable static compression at that directory. For example, to enable static compression for a directory at <http://www.contoso.com/Home/StyleSheets>, perform the following steps:

1. Disable global static compression by executing the following command at a command prompt:

   ```
   adsutil set w3svc/filters/compression/parameters/HcDoStaticCompression true
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

   - Enable static compression at this directory by executing the following command at a command prompt:

     ```
     adsutil set w3svc/1/root/Home/StyleSheets/DoStaticCompression false
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

For IIS 7.0 information I found some on [www.iis.net](http://www.iis.net).  If you’re [looking to setup IIS 7](http://www.iis.net/ConfigReference/system.webServer/httpCompression) this is by far the best source.  So go check it out.

…the next step of course, is to make sure you have requested via the HTTP Header context that the server return the content in compressed encoding.  This can save upwards of 75% on size.

The way this content encoding is provided via the header shows up like this.

Browsers and servers have brief conversations over what they’d like to receive and send. Using HTTP headers, they zip messages back and forth over the ether with their content shopping lists. A compression-aware browser tells servers it would prefer to receive encoded content with a message in the HTTP header like this:

```
GET / HTTP/1.1
Host: www.webcompression.org
User-Agent: Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.5)
  Gecko/20031007 Firebird/0.7
Accept: text/xml,application/xml,application/xhtml+xml,text/html;q=0.9,
  text/plain;q=0.8,video/x-mng,image/png,image/jpeg,image/gif;q=0.2,*/*;q=0.1
Accept-Language: en-us,en;q=0.5
Accept-Encoding: gzip,deflate
Accept-Charset: ISO-8859-1,utf-8;q=0.7,*;q=0.7
Keep-Alive: 300
Connection: keep-alive
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

An HTTP 1.1-compliant server would then deliver the requested document with using an encoding accepted by the client. Here’s a sample response.

```
HTTP/1.1 200 OK
Date: Thu, 04 Dec 2003 16:15:12 GMT
Server: Apache/2.0
Vary: Accept-Encoding
Content-Encoding: gzip
Cache-Control: max-age=300
Expires: Thu, 04 Dec 2003 16:20:12 GMT
X-Guru: basic-knowledge=0, general-knowledge=0.2, complete-omnipotence=0.99
Content-Length: 1533
Content-Type: text/html; charset=ISO-8859-1
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

***Client Code for Requesting Compression***

So how does one get the content type programmatically?  Easy, and here’s a quick example I put together in C# using standard HttpWebRequest objects to request compression.

```
namespace Sdk.Tests
{
    [TestFixture]
    public class TestsProvidingCodeSamples
    {
        [Test]
        public void TestBaselineCompressedRequest()
        {
            // Use Twitter or whatever other service is available.
            var request = (HttpWebRequest)WebRequest.Create("https://somedomain/somepage.aspx");
            request.Headers.Add(HttpRequestHeader.AcceptEncoding, "gzip,deflate");
            request.Credentials = new NetworkCredential("someUser", "somePassword");

            var response = request.GetResponse();
            var responseStream = new StreamReader(response.GetResponseStream(), Encoding.UTF8);
            string getTheResults = responseStream.ReadToEnd();

            Assert.IsNotNull(responseStream);
            Assert.IsNotNull(getTheResults);
        }
    }
}
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

This should get anyone kick started to assuring that your data over the Internet is compressed and efficiently being transferred.
