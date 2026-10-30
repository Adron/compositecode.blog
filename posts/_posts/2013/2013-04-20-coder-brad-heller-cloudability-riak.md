---
title: Coder Brad Heller, Cloudability & Riak
date: 2013-04-20 12:08:06 -0700
last_modified_at: 2013-04-20 12:08:06 -0700
permalink: /2013/04/20/coder-brad-heller-cloudability-riak/
slug: coder-brad-heller-cloudability-riak
wp_id: 8177
original_url: https://compositecode.blog/2013/04/20/coder-brad-heller-cloudability-riak/
categories:
- Unknown Code Ramblings
tags: []
excerpt: This coming April 29th (Monday) we’ll have Brad Heller coming in to give us the low down on how Cloudability has used Riak (click link meetup event). He sent me a short list outline of the topics he plans to hit. Here’s a few key data problems they’ve run into and how they’ve solved those problems …
---

This coming [April 29th (Monday) we’ll have Brad Heller coming in to give us the low down on how Cloudability has used Riak](http://www.meetup.com/Portland-Riak/events/105431422/) ([click link meetup event](http://www.meetup.com/Portland-Riak/events/105431422/)). He sent me a short list outline of the topics he plans to hit. Here’s a few key data problems they’ve run into and how they’ve solved those problems with Riak & other solutions.

[![](/images/adronhall.smugmug.com/Software/Meetups-N-Conferences/Portland-Riak/i-3PTK8Xk/0/M/Portland-Riak-M.png)](http://www.meetup.com/Portland-Riak/)

## @Cloudability

- What does Cloudability do?
- Why do we like Riak?
- Challenges of raw storage in our data pipeline.

- Idempotency
- Scale
- Reliability
  - S3 vs. Riak
- Queryable S3
- Maintain “State”
  - Data Pipelines: Specific problems.
  - Idempotency
- What has been processed?
- How to figure out what to reprocess?
  - Scaling this.
- Pipelines scale horizontally
- Backpressure / failure modes
  - How do we use Riak to address these?
  - Raw data goes directly in Riak (metadata record, raw data record)
  - 2i on metadata record to find what needs processing
  - 2i on metadata record to find stuff to reprocess.
  - Atomic writes: Let Riak assign keys.
- Duplicate Data is OK, idempotency maintained further down the chain.
- Don’t worry about collisions–last one wins.
- Predictable keys are helpful though.
  - Scale is built in!!
- Read/write throughput gets better with more nodes.
  - What we don’t use.
  - Online MapReduce.
  - Only use for backoffice processes
- When something isn’t indexed, identify bad data.
- Add index.
  - Key filtering
- Riak craps it’s pants.
  - Problems we’ve had
  - Ops is easy, but lots of unexpected behavior.
- Riak eats all memory, craps it’s pants.
  - Erlang is hard.
- Everyone on our team hates Erlang except me (Brad).
- Stacktraces will confuse you a lot at first.
  - Riak is “expensive” compared to S3.
- We run a ring of 5 m1.xlarge with EBS + provisioned IOPS.

That covers all the topics Brad wants to cover, which I’m sure that brings up a lot of questions already! So the presentation will be great and we’ll be sure to have a good chunk of time for questions and a few beers afterwards!

For more on Brad, give a follow on twitter [@bradhe](http://twitter.com/bradhe) and endorse him for random skill sets like *dishwasher programming* and *coffee cup holding* on [LinkedIn](http://www.linkedin.com/in/bradhe)! Also you can read

[![](/images/adronhall.smugmug.com/Software/Misc-Images/Just-Icons-and-Bits/i-ZrFwp9r/0/O/Vagrant-Chef-Cookbook-Missing.png)](https://cloudability.com/)Check out [Cloudability](https://cloudability.com/) for keeping tabs on your cloud compute spending. They are the leaders in helping companies manage their spend across many cloud offerings including [AWS, Github, Heroku, Softlayer, Engineyard and others](https://cloudability.com/clouds/).
