---
title: KubeCon Travel Report
date: 2017-12-15 17:14:44 -0800
last_modified_at: 2017-12-15 17:14:44 -0800
permalink: /2017/12/15/kubecon-travel-report/
slug: kubecon-travel-report
wp_id: 13623
original_url: https://compositecode.blog/2017/12/15/kubecon-travel-report/
categories:
- Unknown Code Ramblings
tags:
- Kubernetes
- Metaparticle
excerpt: KubeCon 2017 in Austin was great! Informative, entertaining, and overall a giant win for me and a whole lot of other people. KubeCon has officially entered into my “Will Return To Conferences” list. Austin also helped, as it’s a great city for tech conferences. It has a few issues of course, but overall it’s a …
---

KubeCon 2017 in Austin was great! Informative, entertaining, and overall a giant win for me and a whole lot of other people. KubeCon has officially entered into my “Will Return To Conferences” list. Austin also helped, as it’s a great city for tech conferences. It has a few issues of course, but overall it’s a spectacular city for technology conferences, rating much higher than Las Vegas, San Francisco, and a whole slew of other places in my book.

If you’re experienced, interested in getting involved with open source, or involved with site reliability and operations side of technology, KubeCon has become one of the preeminent conferences to attend. There are workshops, training, impromptu discussions, learning moments, presentations, and more. In addition the sponsor booths and showcase hall was hands down one of the best I’ve seen in more than a year or two. Music, food, and a good comfortable environment to meet, discuss, or just hack on new things in the showcase hall.

### High Points

As the conference started, I covered the keynotes for [day 1](http://blog.adron.me/articles/kubecon-dayone-keynotes/) and [day 2](http://blog.adron.me/articles/kubecon-daytwo-keynotes/). The keynotes were interesting. With great talking points from Kelsey Hightower, Michelle Noorali, and many others. But of all the topics two high points stood out; Metaparticle and the fact Kubernetes 1.9 is boring.

**Kubernetes 1.9, *BORING*!**

The idea that the 1.9 release of Kubernetes is boring is a little misleading. It’s more accurate to say that Kubernetes is in a solid enough state, with few changes, and the 1.9 release is the first of a new trend of fewer breaking changes, increased reliability, and all those things that make software ready for the prime time. As if Kubernetes wasn’t already ready for the prime time eh! This however really does set the new precedent for Kubernetes releases — expect to see the majority of changes, progress, and the like in the tertiary libraries, plugins, and surrounding software of the Kubernetes ecosystem.

**Metaparticle**

This project seems like a conversation I keep having with people. How to better deal with building systems, distributed systems specifically, and manage it all programmatically instead of oodles and oodles of configuration leaking out everywhere and breaching levels of concern. Yeah, Brendan has taken to coming up with a solution, by creating a general library solution around this. The solution he started he’s named [metaparticle](https://metaparticle.io/).

Within the last week between now and the conference I’ve found an article and code repo, and PR that I’ve found interesting about metaparticle. Here are a few I’ve collected:

- [Ryan Clair](https://medium.com/u/4ec598d7982)’s ([Twitter](https://twitter.com/ryandotclair)) [post on metaparticle](https://medium.com/@ryandotclair/an-interrogation-of-metaparticle-and-abstraction-layers-44ba2fe07b62) is excellent, delving into the topic thoroughly and explaining the context in which metaparticle has been created. He also voiced some thoughts about my exact concerns I had, which is, *is this the right abstraction layer*? Is it providing a clear separation of concerns or bleeding them together at the wrong point of interoperability? Great post Ryan. I’ll be thinking a lot more on the matter too.
- A Python Lib — > <https://github.com/metaparticle-io/package/tree/master/python>. The example looks straight forward enough too. A containerized application looks like this:

```
from metaparticle import Containerize

@Containerize(package={'name': 'testcontainer', 'repo': 'brendanburns', 'publish': True})
def main():
    print('hello world')

if __name__ == '__main__':
    main()
```

- A [PR for Golang support](https://github.com/metaparticle-io/package/pull/20)! Which looks like it’s been merged since.
- Gitter Chat which has an ongoing conversation going on about [metaparticle.io](https://gitter.im/metaparticle-io/Lobby). Check it out.

Overall I’m looking forward to the next KubeCon, and may even attempt to attend or speak at the Copenhagen KubeCon coming up. I’ll definitely be at the next KubeCon in the US, which should be easy since it’s in Seattle!
