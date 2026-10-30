---
title: Your Bus Is NOT Here! But We’re Working On It…
date: 2011-11-19 11:49:37 -0800
last_modified_at: 2011-11-20 00:52:24 -0800
permalink: /2011/11/19/your-bus-is-not-here-but-were-working-on-it/
slug: your-bus-is-not-here-but-were-working-on-it
wp_id: 4371
original_url: https://compositecode.blog/2011/11/19/your-bus-is-not-here-but-were-working-on-it/
categories:
- Conferences
- Javascript
- Meetups n' Such
- Ruby on Rails Bits
tags:
- gem
- gemisntall
- geoloqi
- ruby
- ruby on rails
- shotgun
- sinatra
excerpt: But myself and fellow hacker & Geoloqi Crew put something together to figure out where the bus is. Nothing super fancy, but the idea is solid. We wanted to get a simple mobile application put together that would identify where it is, what the closest bus stop is, and pull up the next arriving bus(es) …
---

But myself and fellow hacker & Geoloqi Crew put something together to figure out where the bus is. Nothing super fancy, but the idea is solid. We wanted to get a simple mobile application put together that would identify where it is, what the closest bus stop is, and pull up the next arriving bus(es) for that stop. We were throwing in a few other ideas, such as pulling up specific stops based on your favorites or even specific buses at that route based on your preferred routes.

Pat ([@patrickarlt](https://twitter.com/#!/patrickarlt)) & I ([@adron](https://twitter.com/#!/adron)) started out by pulling in the [GTFS](http://developer.trimet.org/GTFS.shtml) data from TriMet. I setup a basic import to turn all the stop locations in the [GTFS](http://developer.trimet.org/GTFS.shtml) data into a Place within a layer within [Geoloqi](https://developers.geoloqi.com/). Pat setup a URL that could be used to call down the latest X arriving buses. Then we combined forces figuring out how to efficiently get all of the 7000+ bus stops into Geoloqi. That proved a little bit more of an issue than we thought. Not a huge issue, but one that got Kyle ([@kyledrake](https://twitter.com/#!/kyledrake)) and Aaron ([@aaronpk](https://twitter.com/#!/aaronpk)) Coding some fast batch solutions to get it all into [Geoloqi](https://developers.geoloqi.com/) while Pat & I handled the application.

On Sunday we’re lined up to get the application into a MVP (Minimally Viable Product) state. We’re hoping to be able to maybe even use it tomorrow in at least a simple way. From that point forward we’ll hopefully move past the MVP into other functionality! 🙂

Another thing to note, is that with our basic implementation we’re using [GTFS](http://code.google.com/transit/spec/transit_feed_specification.html) data. This is a data format that is standardized and used by many of the agencies around the country. So technically any transit agency, as long as they have a way to return their route arrivals, can be setup to use our application we’re building. Some of the other GTFS data can be retrieved here;

- [San Francisco MUNI](http://www.sfmta.com/cms/asystem/transitdata.php)
- [San Francisco BART](http://www.bart.gov/schedules/developers/gtfs.aspx)
- [San Francisco Caltrain](http://www.caltrain.com/schedules/Mobile_Device_Schedules.html)

To check out more, hit up Google’s page on GTFS data sources:  <http://code.google.com/p/googletransitdatafeed/wiki/PublicFeeds>

Day one of the hackathon has been seriously kick ass! I’ve had a blast and heard some great ideas, seen some great code, even working demo results, and seen amazing skills applied all around! At this juncture, I’m exhausted, got a little more to code, and ready for day 2 of hacking!
