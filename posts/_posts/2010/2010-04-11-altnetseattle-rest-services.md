---
title: '#altnetseattle – REST Services'
date: 2010-04-11 09:07:53 -0700
last_modified_at: 2010-10-04 11:19:40 -0700
permalink: /2010/04/11/altnetseattle-rest-services/
slug: altnetseattle-rest-services
wp_id: 712
original_url: https://compositecode.blog/2010/04/11/altnetseattle-rest-services/
categories:
- Conferences
tags:
- altnet
excerpt: Below are the notes I made in the REST Architecture Session I helped kick off with Andrew. RSS, ATOM, and such needed for better discovery. i.e. there still is a need for some type of discovery. Difficult is modeling behaviors in a RESTful way. ?? Invoking some type of state against an object. For instance …
---

Below are the notes I made in the REST Architecture Session I helped kick off with Andrew.

- RSS, ATOM, and such needed for better discovery.  i.e. there still is a need for some type of discovery.
- Difficult is modeling behaviors in a RESTful way.  ??  Invoking some type of state against an object.  For instance in the case of a POST vs. a GET.  The GET is easy, comes back as is, but what about a POST, which often changes some state or something.
- Challenge is doing multiple workflows with stateful workflows.  How does batch work.  Maybe model the batch as a resource.
- Frameworks aren?t particularly part of REST, REST is REST.  But point argued that REST is modeled, or part of modeling a state machine of some sort? ?
- Nothing is 100% reliable w/ REST ? comparisons drawn with TCP/IP.  Sufficient probability is made however for the communications, but the idea of a possible failure has to be built into the usage model of REST.
- Ruby on Rails / RESTfully, and others used.  What were their issues, what do they do.  ATOM feeds, object serialized, using LINQ to XML w/ this.  No state machine libraries.
- Idempotent areas around REST and single change POST changes are inherent in the architecture.
- REST ? one of the constrained languages is for the interaction w/ the system.  Limiting what can be done on the resources.  – disagreement, there is no agreed upon REST verbs.
- Sam Ruby ? RESTful services.  Expanded the verbs within REST/HTTP pushes you off the web.  Of the existing verbs POST leaves the most up for debate.
- Robert Reem used Factory to deal with the POST to handle the new state.  The POST identifying what it just did by the return.
- Different states are put into POST, so that new prospective verbs, without creating verbs for REST/HTTP can be used to advantage without breaking universal clients.
- Biggest issue with REST services is their lack of state, yet it is also one of their biggest strengths.  What happens is that the client takes up the often onerous task of handling all state, state machines, and other extraneous resource management.  All the GETs, POSTs, DELETEs, INSERTs get all pushed into abstraction.  My 2 cents is that this in a way ends up pushing a huge proprietary burden onto the REST services often removing the point of REST to be simple and to the point.
- WADL does provide discovery and some state control (sort of?)
- Statement made, “WADL” isn’t needed.  The JSON, XML, or other client side returned data handles this.

I then applied the law of 2 feet rule for myself and headed to finish up these notes, post to the [Wiki](http://altnetseattle.pbworks.com/), and figure out what I was going to do next.  For the original [Wiki entry](http://altnetseattle.pbworks.com/REST-Architecture) check it out [here](http://altnetseattle.pbworks.com/REST-Architecture).

I will be adding more to this post with a subsequent post.  Please do feel free to post your thoughts and ideas about this, as I am sure everyone in the session will have more for elaboration.
