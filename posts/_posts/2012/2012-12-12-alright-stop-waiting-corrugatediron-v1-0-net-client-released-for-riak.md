---
title: Alright Stop Waiting, CorrugatedIron v1.0 .NET Client released for Riak!
date: 2012-12-12 13:02:06 -0800
last_modified_at: 2012-12-12 13:02:06 -0800
permalink: /2012/12/12/alright-stop-waiting-corrugatediron-v1-0-net-client-released-for-riak/
slug: alright-stop-waiting-corrugatediron-v1-0-net-client-released-for-riak
wp_id: 7211
original_url: https://compositecode.blog/2012/12/12/alright-stop-waiting-corrugatediron-v1-0-net-client-released-for-riak/
categories:
- .NET Bits
- Distributed Things
tags:
- .NET
- corrugatediron
- distributed database
- dotnet
- nosql
- riak
excerpt: 'I’ll kick right off with all the specifics: Jeremiah did a blog entry on today’s release titled “Just one more thing… Introducing Corrugated Iron v1.0“. Github CorrugatedIron Project Site for Corrugated Iron Riak Database & Github Repo CorrugatedIron Installation CorrugatedIron on Nuget Samples on Github Send a congrats out to the team duo of OJ @TheColonial …'
---

[![](/images/adronhall.smugmug.com/Software/Software-Development/Basho-Misc/i-w8GRHNt/0/O/nugeticon.png)](http://corrugatediron.org/)I’ll kick right off with all the specifics:  Jeremiah did a blog entry on today’s release titled “[Just one more thing…  Introducing Corrugated Iron v1.0](http://www.brentozar.com/archive/2011/07/just-one-more-thing-introducing-corrugatediron/)“.

- [Github CorrugatedIron](https://github.com/DistributedNonsense/CorrugatedIron)
- [Project Site for Corrugated Iron](http://corrugatediron.org/)
- [Riak Database](http://basho.com/products/riak-overview/) & [Github Repo](https://github.com/basho/riak)
- [CorrugatedIron Installation](http://corrugatediron.org/documentation/Basics.Installation.html)
- [CorrugatedIron on Nuget](http://nuget.org/packages/CorrugatedIron)
- [Samples on Github](https://github.com/DistributedNonsense/CorrugatedIron.Samples)

[![](/images/adronhall.smugmug.com/Software/Software-Development/Basho-Misc/i-V4vn3xW/0/O/riak-powered-dark.png)](http://basho.com/products/riak-overview/)Send a congrats out to the team duo of OJ [@TheColonial](https://twitter.com/TheColonial) & Jeremiah [@peschkaj](http://twitter.com/peschkaj) via Twitter. Check out the [.NET Rocks Podcast with Jeremiah talking with Carl and Richard about storing data in Riak](http://www.dotnetrocks.com/default.aspx?showNum=701). Also check out [Adrian Hills’ article on getting up and running via Nuget with Corrugated Iron in Visual Studio](http://architects.dzone.com/articles/playin-around-riak-and-net), ping him on Twitter [@AdaTheDev](http://twitter.com/AdaTheDev).

So no excuses in .NET land to write some apps that are hard core data centric and capable based on the power of Riak! There are tons of features. You can read about them yourself via the README.md file on the CorrugatedIron Repository, but I wanted to post the features right here so you get an idea of the feature rich capabilities of the library. In addition, it does indeed work on Linux & OS-X with Mono. So don’t let Windows get in your way! 🙂

## Current Features

*♥: denotes availability of both blocking and asynchronous APIs*
*«: denotes availability of both streaming and non-streaming APIs*

- Riak cluster support:
  - One or more nodes in the cluster.
  - Load-balancing and **pooling** of connections across the nodes.
    - Currently only round-robin is supported, more strategies to come later.
  - Per-node configuration for:
    - Host Name (purely used for identification).
    - Host Address.
    - PBC Port.
    - HTTP/REST Port.
    - Pool Size.
    - Timeout parameters.
- Server ping.    ♥
- Get server information/version.    ♥
- Simple Get/Put/Delete operations.    ♥
- Bulk Get/Put/Delete operations.    ♥
- List buckets.    ♥
- List keys.    ♥  «
- Semi-fluent Map/Reduce.    ♥  «
- Link walking.    ♥
- Delete buckets.    ♥
- Set/Get bucket properties.    ♥
- Batch operations on a single connection.
  - Each time a Client function is called resulting in communication with the Riak cluster, a connection is pulled from a pool on a given node. In most use-cases this functionality is fine as it is often single-shot calls that are made. There are, however, cases where many operations will happen at once. Rather than forcing the user to make multiple calls to the client, resulting in multiple connection acquisitions behind the scenes, the user can use the Batch interface to make many calls on a single connection. This also reduces the overhead of setting the client ID on each call.
  - Because a batch operation reuses a single connection only a subset of the client API is available for batch actions. The functions that are excluded are the asynchronous functions.
- Graceful degrades to HTTP/REST API when the request isn’t supported via Protocol Buffers.
- Configurable via `web.config`, `app.config` or a custom configuration file.

**CorrugatedIron works with .NET 4.0 on Windows and Mono on Linux and OSX.**
