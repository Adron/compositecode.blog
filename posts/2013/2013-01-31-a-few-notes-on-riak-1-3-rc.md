---
title: A Few Notes on Riak 1.3 RC
date: 2013-01-31 16:13:02 -0800
last_modified_at: 2013-01-31 16:13:02 -0800
permalink: /2013/01/31/a-few-notes-on-riak-1-3-rc/
slug: a-few-notes-on-riak-1-3-rc
wp_id: 7607
original_url: https://compositecode.blog/2013/01/31/a-few-notes-on-riak-1-3-rc/
categories:
- Basho
- Databases
tags:
- database
- distributed database
- key value
- riak
- riak 1.3
- riak database
- riak key value
- riak kv
- software
- technology
excerpt: Full context – Riak 1.3 RC came out just a couple dozen hours ago. RC stands for release candidate, which in turn basically means that version 1.3 is complete and any other additions will be for quick fixes or any issues that crop up. I’ve just started rolling a few new systems myself with this …
---

Full context – [Riak 1.3 RC](https://github.com/basho/riak) came out just a couple dozen hours ago. RC stands for release candidate, which in turn basically means that version 1.3 is complete and any other additions will be for quick fixes or any issues that crop up. I’ve just started rolling a few new systems myself with this new version and hope you’ll join me in taking a hack at it. Let’s jump into a few reason why you’d want to leap into 1.3. You can read about the features below via the [release notes](https://github.com/basho/riak/blob/1.3/RELEASE-NOTES.md) also, but I’ve turned them into smaller bit size chunks below.

- [![Giddyup in action!](/images/adronhall.smugmug.com/Software/Misc-Images/Bad-Resume/i-mSDMPDt/0/S/riaktestgiddyup-S.png)](https://github.com/basho/giddyup)

  *Giddyup in action!*

  The first thing with the latest v1.3 has been the massive effort put into testing via the **[riak\_test](https://github.com/basho/riak_test)** and the **[giddyup](https://github.com/basho/giddyup)** repos. Ongoing there will be a much easier way to move forward in features & quality. This is one of the reasons I love working for Basho, the whole team isn’t about smoke and mirrors with testing, they readily and diligently work on testing. Which to add context, remember we’re talking about distributed systems here, which aren’t exactly the easiest thing to test. One doesn’t just merely walk in and write unit tests and assume a distributed systems is tested. This moves us forward, and those that want to contribute and get involved more heavily in Riak now have a platform to dive in confidently when using these testing repositories.
- **Active Anti-Entropy** – Alright, now we’re getting to the features with bad ass sounding names. Also referred to as AAE, this feature grabs bad replica data and begins a correction through read repair to protect data. It’s one more layer of protection against any type of data loss, disaster, bit rot, etc).
- **MapReduce Sink Backpressure** – This one reminds me of tuning when setting up forced induction, AKA a turbo on a car. But I digress, I’ve snagged a description from the release notes for this feature, “*Riak Pipe brought inter-stage backpressure to Riak KV’s MapReduce system. However, prior to Riak 1.3, that backpressure did not extend to the sink. It was assumed that the Protocol Buffers or HTTP endpoint could handle the full output rate of the pipe. With Riak 1.3, backpressure has been extended to the sink so that those endpoint processes no longer become overwhelmed. This backpressure is tunable via a soft cap on the size of the sink’s buffer, and a period at which a worker should check that cap. These can be configured at the Riak console by setting application environment variables*” ….suffice it to say this helps out with map reduce in certain situations.
- **Additional IPv6 Support** – Riak Handoff and Protocol Buggers listen ala IPv6 now. Nuff’ said.
- **Luke removal** – Luke is completely and utterly gone now. Dead. Don’t look for Luke here.
- **Riaknostic** – This is now part of the default featureset instead of separate tooling.
- **SmartOS 1.8 Packages** – They’re available.
- Health Check – This is a pretty awesome system that’s been added. Basically it watches the system and enables and disables services based on conditions. It’s super easy, just flick the switch in the app.config.

  ```yml
  {enable_health_checks, true}
  ```
- **Reset Bucket Properties** – A quickie definition from the release notes “*The HTTP interface now supports resetting bucket properties to their default values. Bucket properties are stored in Riak’s ring structure that is gossiped around the cluster. Resetting bucket properties for buckets that are no longer used or that are using the default properties can reduce the amount of gossiped data.”*

There were also a lot of PRs and more that you can check out on Github. These are the main key features that are now available and ready for use in 1.3. Check em’ out, feel free to contact me or any of the team to ask questions, let us know your 2 cents or otherwise banter about. Cheers! Sometime in the coming days I’ll have a quick start, akin to what’s in the docs, but with some specific ops on some IaaS Providers. So keep reading, coming up soon.

Happy hacking!  \m/   \m/
