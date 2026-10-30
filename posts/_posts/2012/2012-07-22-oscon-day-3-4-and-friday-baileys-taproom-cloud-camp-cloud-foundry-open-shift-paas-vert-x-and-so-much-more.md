---
title: 'OSCON Day #3, #4, and Friday => Bailey’s Taproom, Cloud Camp, Cloud Foundry, Open Shift, PaaS, vert.x, and so much more…'
date: 2012-07-22 13:40:45 -0700
last_modified_at: 2012-07-22 13:40:45 -0700
permalink: /2012/07/22/oscon-day-3-4-and-friday-baileys-taproom-cloud-camp-cloud-foundry-open-shift-paas-vert-x-and-so-much-more/
slug: oscon-day-3-4-and-friday-baileys-taproom-cloud-camp-cloud-foundry-open-shift-paas-vert-x-and-so-much-more
wp_id: 6062
original_url: https://compositecode.blog/2012/07/22/oscon-day-3-4-and-friday-baileys-taproom-cloud-camp-cloud-foundry-open-shift-paas-vert-x-and-so-much-more/
categories:
- Cloud Foundry
- Cloud Speak
- Conferences
- Javascript
- Node.js Things
- Platform (as a Service)
tags:
- andy piper
- cloud
- cloud computing
- cloud foundry
- cloudfoundry
- erica brescia
- iaas
- iron foundry
- ironfoundry
- jono bacon
- josh long
- node
- node.js
- open source
- oscon
- oss
- paas
- vert.x
excerpt: Tuesday night, as usual ended with great technical conversation at Bailey’s Taproom. Bailey’s is basically the epicenter of the Portland tech scene. Almost every programmer, devops, or technical person either goes about once a month or has this establishment as a regular watering hole! It’s great, the atmosphere is chill, the beer is SUPERB, the …
---

Tuesday night, as usual ended with great technical conversation at Bailey’s Taproom. Bailey’s is basically the epicenter of the Portland tech scene. Almost every programmer, devops, or technical person either goes about once a month or has this establishment as a regular watering hole! It’s great, the atmosphere is chill, the beer is SUPERB, the beer menu kicks ass (see: [Beer Dashboard Kick’s Ass](/2011/09/01/beer-dashboard-kick-ass-awesome/)) and the list of fun cool things just continues on and on.

This week of course OSCON adds a little spice to the regular roll call at Bailey’s. There were a number of conversations that broke out, which I’ve broken out the key topics below:

[**vert.x**](http://vertx.io/) => To summarize as is written on the site itself, “*Write your application components in JavaScript, Ruby, Groovy or Java. Or mix and match several programming languages in a single application. Create real, scalable applications in just a few lines of code. No sprawling xml config. Scale using messaging passing and immutable shared data to efficiently utilise your server cores. Super-simple concurrency model frees you from the hassles of traditional multi-threaded programming.*”

Here’s an example from the site in a few of the languages:

**Java**

```java
import org.vertx.java.core.Handler;
import org.vertx.java.core.http.HttpServerRequest;
import org.vertx.java.deploy.Verticle;

public class Server extends Verticle {
    public void start() {
        vertx.createHttpServer().requestHandler(new Handler() {
            public void handle(HttpServerRequest req) {
                String file = req.path.equals("/") ? "index.html" : req.path;
                req.response.sendFile("webroot/" + file);
            }
        }).listen(8080);
    }
}
```

**JavaScript**

```javascript
load('vertx.js')

vertx.createHttpServer().requestHandler(function(req) {
    var file = req.path === '/' ? 'index.html' : req.path;
    req.response.sendFile('webroot/' + file);
}).listen(8080)
```

**Ruby**

```ruby
require "vertx"

Vertx::HttpServer.new.request_handler do |req|
    file = req.uri == "/" ? "index.html" : req.uri
    req.response.send_file "webroot/#{file}"
end.listen(8080)
```

## Wednesday Roughness

I felt beat up a bit start Wednesday, but rolled into it after a short while. Needless to say, the intensity of conversations (and maybe a few of those rounds of beer) and number of ideas, new things to check out and fitting it all in can wear one out.

The morning sessions were solid, I attended most of “[Comparing Open Source Private Cloud Platforms](http://www.oscon.com/oscon2012/public/schedule/detail/24376)“. Lance did a solid job of laying out the tooling, virtualization software and where these things come together to form a number of OSS options for cloud computing. Check out more from Lance on his [@ramereth](https://twitter.com/ramereth), his [blog Lance Albertson](http://www.lancealbertson.com/), or check out his band he’s in “[The Infallible Collective](http://www.infalliblecollective.com/)“.

## Wednesday, Thursday and Friday Meets

I met a ton of people. All of whom I must say, I hope to get to talk to again, work with on projects, or just sling some code sometime. Absolutely great people, friendly, intelligent and highly motivated. Some of these people I met included:

**Andy Piper ([@andypiper](http://twitter.com/andypiper))** – Part of Great Britain’s contingent of VMware Cloud Foundry advocates and such. We got to hang out and talk about a zillion different topics at a number of events. Andy was kind enough to show me a few tips and tricks he’s been using with Cloud Foundry, the VMC, and in general working with the platform.

**Josh Long ([@starbuxman](https://twitter.com/starbuxman))** – I met Josh once before on the Cloud Foundry open tour, where he brought COBOL programming… oh no wait, he brought some great Sprint Java samples and such to demo on the Cloud Foundry Platform. I fulfilled Josh’s dreams by telling him that COBOL, could indeed run on Cloud Foundry thanks to the .NET capabilities of Iron Foundry! (ya know, if anybody is into that type of thing)

**Erica Brescia ([@ericabrescia](https://twitter.com/ericabrescia))** – I finally got to meet Erica in person, after chit chatting on Twitter about all the great applications her company Bitnami helps to deploy in the cloud. There are some really great deployment hosting solutions from them, check them out if you’re looking for some streamlined deployment practices. She also mentioned I need to meet…

**Jono Bacon ([@jonobacon](https://twitter.com/jonobacon))** – I managed to meet Jono by randomness. He’s, well, let’s say he does some absolutely great work in the tech industry for Canonical and in the open source universe. In addition Jono has some superb tastes in music. **\m/  \m/**Check out some of his work:  [Blog](http://www.jonobacon.org/blog/), [personal site](http://www.jonobacon.org/), and you can probably google him too. Do it, he’s got a lot of great material out there.

As I was saying, these aren’t the only people that I met. To all those people I didn’t mention, it was awesome hanging out, catching up and hearing about what everyone is working on and creating.

## PaaS, IaaS and The Driving Open Source Coders

On the topic of PaaS, it continues to expand into new realms of publicly (or privately) run services. PaaS is quickly expanding past mere framework services around .NET, PHP, Rails, Sinatra and such and moving into the realm of databases, services buses, and other capabilities as a service. As laid out with the SOA mindset. Even though enterprises failed to bring SOAP to an effective worldwide use, RESTful services are expanding rapidly. \*aaS is pushing those even further, to do what the enterprise had wanted but failed to do. Creating a universal acceptance of scalable, powerful, expandable and extensible services through APIs.

As more services are extended we’ll start seeing a lot of offerings around truly scalable databases with various feature sets around those databases offered as a key service. Examples would include “atomic database as a service”, “transactional data store as a service”, or “document store as a service”. In the end it will include the amount of usefulness for the services while eliminating a need to know each in intimate detail. Knowing the core capabilities of an option and just using the service will grossly outpace the attempt to implement these services internally.

So keep watching PaaS to grow in many various ways. Consuming the service being the driver over attempting to build the service. Of course, if the service doesn’t exist, *get on that it’s business opportunity!*

## Random OSCON Diversions

I had a great time visiting with family while at OSCON also. To whom they all send a hello and horns up, thrash on salute to the coders of the world!

[![Voodoo Donut Break with Florida Family Contingent](/images/adronhall.smugmug.com/Software/Meetups-N-Conferences/OSCON-2012/i-Cr8tp2R/0/S/IMAG1031-S.jpg "Voodoo Donut Break with Florida Family Contingent")](/images/adronhall.smugmug.com/Software/Meetups-N-Conferences/OSCON-2012/i-Cr8tp2R/0/O/IMAG1031.jpg)

*Voodoo Donut Break with Florida Family Contingent.*

[![My brother Adam, the IT Department](/images/adronhall.smugmug.com/Portland-Action/Adam-Florida-Family-Visit/i-v9P2kw6/0/S/20120715135751-S.jpg "My brother Adam, the IT Department")](http://adronhall.smugmug.com/Portland-Action/Adam-Florida-Family-Visit/24194741_KPrg5r#!i=1967768783&k=v9P2kw6&lb=1&s=O)

*My brother Adam, the IT Department*

***My Brother Runs an IT Shop of One…***

**…thanks to cloud computing capabilities.**

This kind of blew my mind. I *sort of* of knew what he did, but it didn’t hit me how close our professional lives are until this trip. He’s just recently moved several hundred miles away from the main office, but still manages the entire company.

One of the unique happenstances is, my brother (the guy next to the bald guy that is me, he’s wearing a Tesla t-shirt) is the top IT guy for a little billion dollar a year company. Which, in this case, he’s proven the power of cloud computing. Why do I say this? Because traditionally this organization would have needed an army of PC techs, network knob fiddlers, and such. But with the advantages of cloud computing, both on premise and off premise, and have a DevOps Guy that knows what he’s doing they are able to efficiently run their entire company with one single guy.

Needless to say, with the synergy of OSCON we had more than a few conversations around tech. Some of those included the replacement of PCs with mobile devices, such as iPads or smart phones. Another was the mix of on-premise data that couldn’t easily be transferred or utilized form cloud services. These are just a few fo the things that have helped him to run the show, the entire show.

## Summary

OSCON was awesome. Next time I will be taking off a day or two before and a day or two afterwards so that I can do an even more elaborate write up of the event. My aim is to have interviews, video and otherwise, and really step it up in relation to providing an eye into the event from a developer’s point of view.
