---
title: Simian Satasin Asynchronous Calls
date: 2009-02-20 02:07:14 -0800
last_modified_at: 2010-08-17 10:24:15 -0700
permalink: /2009/02/20/simian-satasin-asynchronous-calls/
slug: simian-satasin-asynchronous-calls
wp_id: 591
original_url: https://compositecode.blog/2009/02/20/simian-satasin-asynchronous-calls/
categories:
- Uncategorized Bits
tags: []
excerpt: All I wanted was an asynchronous WebClient call. What do I get? Tons of dead links in MSDN, tons of pure crap of non working code all over the net. Then I realized I needed to search for silverlight AND asynchronous instead of just asynchronous. Anyway I finally found some legit code snippets and put …
---

All I wanted was an asynchronous WebClient call.  What do I get?  Tons of dead links in MSDN, tons of pure crap of non working code all over the net.  Then I realized I needed to search for *silverlight* AND *asynchronous* instead of just *asynchronous*.  Anyway I finally found some legit code snippets and put together this simple test.  The story goes like this…

Here’s a little test for getting asynchronous calls up and running, and tested.  Keep in mind long tests that take place over the network or that will introduce extensive latency should NOT be part of a CI build.  If anything set these into a separate build that can run over a period of time to assure integrity and that the services are up, but seriously, don’t add them to a CI build.  I’ve seen enough of these, and it is VERY destructive to productive development.  No really, did I point this out yet, do NOT add these to a standard CI build.  K – thx.

With that warning, here’s a way to test some services over REST.

```csharp
     [TestClass]
     public class AsyncTest
     {
         private XDocument doc;

         [TestMethod]
         public void TestMethod1()
         {
             string baseUri = "<a href="http://twitter.com/statuses/public_timeline.xml">http://twitter.com/statuses/public_timeline.xml</a>&quot;;
             var svc = new WebClient();
             svc.DownloadStringCompleted += svc_DownloadStringCompleted;
             svc.DownloadStringAsync(new Uri(baseUri));

             Thread.Sleep(1000);
             Assert.IsNotNull(doc);
             XDocument docTest = new XDocument();
             Assert.IsInstanceOfType(doc, docTest.GetType());
         }

         private void svc_DownloadStringCompleted(object sender, DownloadStringCompletedEventArgs e)
         {
             doc = XDocument.Parse(e.Result);
         }
     }
```

Create a variable that the handler will assign a value to, it doesn’t really matter what it assigns as long as it proves the handler executed.  Of course, if you’re looking for a particular bit of code or a property you would want to test for that, but otherwise the primary concern is to test that it fired appropriately and didn’t cause an explosion of some type.

Next create the method that initiates the call and wire up the event handler to the event.  Now when you execute the method, which I’ve left as the default lame name of TestMethod1, you should get a positive test.  The big question for this test is, “Will the REST service return in less than a second?”  If it takes longer you need to add to the Thread.Sleep(X) method.

There is of course all types of issue with this particular test.  Isolation is broken, it breaches boundaries, yadda yadda yadda yadda.  The point is, you get a test that can verify that a service is up, and that it responds with something.  As an extra kicker you can even verify that the service is responding within a certain threshold of time since a Thread.Sleep method is used.  If it fails because the time isn’t enough, you would know you need to do something about the performance.

Either way, good luck on testing these, if you have any other ideas on legit ways to test services like these, please pop a comment on this entry.
