---
title: Integration Test in a Build?
date: 2008-06-19 07:56:38 +0000
last_modified_at: 2008-06-19 07:56:38 +0000
permalink: /2008/06/19/integration-test-in-a-build/
slug: integration-test-in-a-build
wp_id: 281
original_url: https://compositecode.blog/2008/06/19/integration-test-in-a-build/
categories:
- Uncategorized Bits
tags: []
excerpt: Integration tests are dependant tests that go across boundaries; database to the data layer, UI to the client layer, Model Layer of the MVC to the Something Layer, and the list goes on. These tests are not something that can be added to a build solution without first getting the various segments actually “running”. We …
---

Integration tests are dependant tests that go across boundaries; database to the data layer, UI to the client layer, Model Layer of the MVC to the Something Layer, and the list goes on.  These tests are not something that can be added to a build solution without first getting the various segments actually “running”.  We then end up with several different issues;

- With the assumption that the unit tests pass, the integration tests should then fire.  This is a fairly straight forward need, have ordered tests run.  Unit tests always go first and then integration tests.  What is the best way to set this up?
- How does one launch things like Web Services, setup Databases, etc to test to in an integration point of view.  Something that can be repeated time and time again in a reliable fashion.  I’ve been using TeamCity, but in general how does one go about getting an application to actually deploy?

The best solution that I’ve come up with so far is to have the unit tests in the building solution and separate the integration tests into the actual Setup/Deploy/\*.msi Solution.  When that solution is built, it needs to verify and deploy/setup the various parts of the application.  Since it is part of the functional requirement of this solution to be able to be deployed, the integration tests are “almost” a large scale application level “unit test”.  Right?  Ok, so maybe I’m thinking to creatively but it should work.

I’ll be putting a solution together to do just that and will find out then.

Technorati Tags: [Integration](http://technorati.com/tags/Integration),[Unit Test](http://technorati.com/tags/Unit%20Test),[Integration Test](http://technorati.com/tags/Integration%20Test),[Deploy](http://technorati.com/tags/Deploy),[Setup](http://technorati.com/tags/Setup),[Test](http://technorati.com/tags/Test)

del.icio.us Tags: [Integration](http://del.icio.us/popular/Integration),[Unit Test](http://del.icio.us/popular/Unit%20Test),[Integration Test](http://del.icio.us/popular/Integration%20Test),[Deploy](http://del.icio.us/popular/Deploy),[Setup](http://del.icio.us/popular/Setup),[Test](http://del.icio.us/popular/Test)
