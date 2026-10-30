---
title: Just A Bit More REST
date: 2009-02-26 14:31:28 +0000
last_modified_at: 2010-08-17 10:21:30 -0700
permalink: /2009/02/26/just-a-bit-more-rest/
slug: just-a-bit-more-rest
wp_id: 592
original_url: https://compositecode.blog/2009/02/26/just-a-bit-more-rest/
categories:
- Uncategorized Bits
tags: []
excerpt: Just a few more examples, kind of a follow up to my Simian Satasin Asynchronous Calls Entry. Keep in mind, I’m providing these as examples, I do NOT suggest writing tests with Thread.Wait calls in them. Very very bad practice. [TestClass] public class GetRestServices { private XDocument doc; [TestMethod] public void TestSynchronousCallWithHttpWebRequest() { …
---

Just a few more examples, kind of a follow up to my Simian Satasin Asynchronous Calls Entry.  Keep in mind, I’m providing these as examples, I do NOT suggest writing tests with Thread.Wait calls in them.  Very very bad practice.

```csharp
    [TestClass]
    public class GetRestServices
    {
        private XDocument doc;

        [TestMethod]
        public void TestSynchronousCallWithHttpWebRequest()
        {
            var request = (HttpWebRequest) WebRequest.Create("https://twitter.com/statuses/public_timeline.xml&quot;);
            var response = request.GetResponse();
            var responseStream = new StreamReader(response.GetResponseStream(), Encoding.UTF8);
            var doc = new XmlDocument();
            doc.Load(responseStream);
            Assert.IsNotNull(doc);
        }

        [TestMethod]
        public void TestAsynchronousCall()
        {
            const string baseUri = "http://twitter.com/statuses/public_timeline.xml&quot;;
            var svc = new WebClient();
            svc.DownloadStringCompleted += svc_DownloadStringCompleted;
            svc.DownloadStringAsync(new Uri(baseUri));

            Thread.Sleep(1000);
            Assert.IsNotNull(doc);
            var docTest = new XDocument();
            Assert.IsInstanceOfType(doc, docTest.GetType());
        }

        private void svc_DownloadStringCompleted(object sender, DownloadStringCompletedEventArgs e)
        {
            doc = XDocument.Parse(e.Result);
        }

        [TestMethod]
        public void TestAsynchronousCallWithSecurity()
        {
            const string baseUri = "http://twitter.com/statuses/friends_timeline.xml&quot;;
            var svc = new WebClient();
            svc.Credentials = new NetworkCredential("yourtuweetusername", "yourtuweetpassword");
            svc.DownloadStringCompleted += svc_DownloadStringCompleted;
            svc.DownloadStringAsync(new Uri(baseUri));

            Thread.Sleep(3000);
            Assert.IsNotNull(doc);
            var docTest = new XDocument();
            Assert.IsInstanceOfType(doc, docTest.GetType());
        }
    }
```

Hope those are helpful for those searching.
