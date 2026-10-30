---
title: Conflicts of Building a Real World Example Application Starter Kit
date: 2018-12-27 09:15:25 -0800
last_modified_at: 2018-12-26 23:12:00 -0800
permalink: /2018/12/27/conflicts-of-building-a-real-world-example-application-starter-kit/
slug: conflicts-of-building-a-real-world-example-application-starter-kit
wp_id: 15084
original_url: https://compositecode.blog/2018/12/27/conflicts-of-building-a-real-world-example-application-starter-kit/
categories:
- Coding Adventures
- Trains
tags:
- code starter kit
- distributed database starter kit
- distributed databases
- real world applications
- reservation system
- ticket
- ticket sales
excerpt: As I dug through a number of JavaScript user interface frameworks lately, reading a number of posts, and building a more informed opinion. All this to decide which one I should use for a sample application for some starter kits. One post I read hit home that it does need to be a bit more …
image: /wp-content/uploads/2018/12/train-layout-top.jpg
---

As I dug through a number of [JavaScript user interface frameworks lately](/2018/12/26/the-state-of-javascript-frameworks-2019-a-top-5/), reading a number of posts, and building a more informed opinion. All this to decide which one I should use for a [sample application for some starter kits](/2018/12/21/creating-distributed-database-application-starter-kits/). One [post](https://medium.freecodecamp.org/a-real-world-comparison-of-front-end-frameworks-with-benchmarks-2018-update-e5760fb4a962) I read hit home that it does need to be a bit more complex than a todo app.

However, I’m still starting with a todo app anyway, but it’s going to turn into something else that is much more than a mere todo app. In this post I’m going to write up some of those larger plans and what complexities lie in wait – *dragons are indeed there* – for this more extensive real world app.

## Modernizing Real World US Passenger Rail Ticket Sales!

Ok, I picked this topic since it is one of the things I find frustrating in the United States. The passenger rail systems, pretty much all of them, are barely better than many 3rd world countries, let alone the developed nations. One of those elements that the United States falls far behind on is an effective, efficient, accurate, and useful ticketing and seat assignment system. Let’s talk about this particular problem for a moment and you’ll start to visualize the problems that exist with the current system.

### The Problem(s): Train Seating Options

![Siemens Charger engine waiting with Talgo train.](/wp-content/uploads/2018/12/1599px-Amtrak_Cascades_1401_-_Siemens_Charger_engine_at_King_Street_Station2C_Seattle2C_WA_-_01.jpg)

*Siemens Charger engine waiting with Talgo train.*

Getting people on and off of a transport system like a train, airplane, ferry, or other mode of transport isn’t a simple process. However, many times it doesn’t have to be as complex, wrought with error, confusion, or disarray as there often is in the United States. Let’s step back and focus on one particular set of trains, the four particular trains that leave form King Street Station in Seattle, Washington on an almost daily basis.

1. [Sound Transit](https://www.soundtransit.org/) Sounder – [[Stations](https://www.soundtransit.org/ride-with-us/stations/sounder-train-stations)] [[Fares](https://www.soundtransit.org/ride-with-us/how-to-pay/fares/sounder-train-fares)] [[Wikipedia](https://en.wikipedia.org/wiki/Sounder_commuter_rail)] This is a commuter route that has two lines:
   1. North Line – Seattle to Everett.
   2. South Line – Seattle to Tacoma, then onward to Lakewood.
2. [Amtrak Cascades](https://www.amtrakcascades.com/) – [[Wikipedia](https://en.wikipedia.org/wiki/Amtrak_Cascades)] Seattle is one of the major stops on the Cascades route, which starts in Eugene down in Oregon and traverses all the way into Canada to Vancouver.
3. [Amtrak Empire Build](https://www.amtrak.com/empire-builder-train) – [[Wikipedia](https://en.wikipedia.org/wiki/Empire_Builder)] This is one of the two Superliner cross country overnight trains that leaves Seattle, connects with a sister train in Spokane everyday from Portland, and then combines and travels all the way to Chicago!
4. [Amtrak Coast Starlight](https://www.amtrak.com/coast-starlight-train) – [[Wikipedia](https://en.wikipedia.org/wiki/Coast_Starlight)] This is one of the other Superliner cross country overnight trains. It departs from Seattle, travels south with a number of stops and eventually ends in Los Angeles.

These four trains use specific train equipment with a particular accommodations for ticket sales.

![One of the Amtrak Superliner Coach Car's seating layout.](/wp-content/uploads/2018/12/amtrak-diagram-superliner-coach.jpg)

*One of the Amtrak Superliner Coach Car’s seating layout. (Images found [here](http://www.craigmashburn.com/amtrakcardiagrams.html))*

The Sounder provides tickets via the Sound Transit System in the area, which is a relatively cheap, non-reserved seat, heavily used train. Often there’s standing room only. It’s one of those things, that if one could purchase a ticket and know if they’re getting a seat, or if the train is full or not, that would encourage or discourage use accordingly. Currently, you buy a ticket and just get on. Rarely are they even checked, there is no gated entry, it’s basically a free for all.

The Amtrak Cascades are a reserved seat system. You purchase a ticket with the contract agreement that you will be provided a seat – either business class or regular – upon boarding. Emphasis on upon boarding as this can cause great confusion when entering the station and attempting to determine how to pick up these seat assignments even though you’ve already purchased a ticket. It adds time to boarding, requires the train sits waiting longer, and passengers have to arrive much earlier than the train departure. Albeit, just for context this earlier arrival (~20-30 minutes before) is nothing compared to the horrors of airports (2 hour suggested arrival before departure), it’s still unnecessary if modern systems were used to provide a streamlined and more efficient boarding process.

![Amtrak Empire Builder](/wp-content/uploads/2018/12/2880px-Empire_Builder_40Two_Medicine_Trestle_28_2_Views_29.jpg)

*Amtrak Empire Builder*

The Amtrak Empire Builder and Coast Starlight are currently an interesting mix. Both trains have sleeping accommodations that give a reserved room number before boarding. A very efficient process indeed, something to aim for. Since one knows the car number and room number, one could theoretically just board without even being guided. The rest of the seats however, some 200-300 or more of them depending on the train, are reserved seats albeit one doesn’t receive the seat assignment until they arrive at the station. Again, causing unnecessary chaos.

## The Problem(s): Technology Deeper Dive

### Problem: Passenger Navigation to Seat Reservation

![Amtrak Cascades Bistro](/wp-content/uploads/2018/12/1920px-AmtrakCascadesDiner.jpg)

*Amtrak Cascades Bistro*

Every single one of the trains listed above: Amtrak Empire Builder, Amtrak Coast Starlight, Amtrak Cascades, and Sound Transit Sounder all have some similar characteristics that would make it cheap and relatively easy to implement a ticketing and seat reservation system. In all of the train equipment, whether Sounder Bombardier, Superliner, or Talgo Amtrak Cascades there are seat numbers and car numbers. This provides us a core basis in which to work, to make all of this processing much easier.

At each station where these trains stop, each car of each train stops at a particular point – or could be made to stop at a particular point – at each station. The Sounder trains for example all have floor mats at the station that read “Welcome Aboard”! This is another element we could use to navigate a particular seat reservation. Automating the process of not just assigning a seat, but providing the information on each ticket for where and exactly when each passenger should arrive at a particular point at the station.

Since the cars and stations all have known characteristics about where to be, where the train will arrive and depart from, and what car number and door position is at this can all be automated per train. This is a repeatable process. Something that easily meets the exact definition of why we build computer systems and automate things with computer systems!

### Problem: Equipment Changes, Modifiable Trains

Sometimes I’ve had conversations with what might change within the system. Almost all changes with a rail system are very known. From a disaster all the way to a simple everyday equipment change. For example, the train arriving may have an extra coach car or sleeper car on the Coast Starlight for some reason. Since we can build a system to model around the specific vehicles, and the vehicles numbers on a train can easily be set these changes can extrapolate out to tickets so they can be accurately assigned by a computer the day of. Changing equipment may take multiple minutes in the rail yard, but in the computer it’s a few keystrokes and it’s done. All tickets re-assigned, everything rebalanced, it’s almost as magical as a distributed database.

### Problem: Common Concurrency, Purchasing, and Related Issues

There are also a number of issues a proper ticketing and reservation system would have to cover, such as managing for multiple people attempting to buy the same seat at relatively the same time. A locking and concurrency mechanism will be needed, something that’s been solved before, so appropriate planning around this will solve the issue.

There are of course timing issues too, once a ticket is locked, eventing within the system should unlock it appropriately. These event based timers will be an interesting challenge too. Solved already, but fun that they’ll need solved again specifically for this system!

### Problem: Or Feature “See a Mountain”?

![Aerial view of mount Rainier](/wp-content/uploads/2018/12/Mount_Rainier_from_west.jpg)

*Aerial view of mount Rainier*

Some other things I’ve pondered include, the selling of some seats as choice preferences. For example, for the Empire Builder, Coast Starlight, and Cascades trains each have specific views that are easier or harder to see depending on the side of the train the accommodations are for. An example, if you’re facing west on the Coast Starlight you get all of the ocean views in southern California. If you’re on the east side, you get views of all the mountains like Rainier (*see above picture!*) and even Shasta if there is a full moon. Depending on these views and related characteristics, I’d happily pay a few bucks more to ensure I get a specific assignment or get to pick a specific assignment, so why not offer the ability to choose the seat for a specific fare?

![IMG_4090-XL](/wp-content/uploads/2018/12/IMG_4090-XL.jpg)

*The Puget Sound, traveling north out of Seattle on the Amtrak Cascades or Sound Transit Sounder north line.*

## Summary  & Next Steps

*Summary* – This is post one of many about the very distributed nature of purchasing tickets for one of the trains into and out of the city. As comparison with my todo app, this will definitely provide a very real world application option indeed! As soon as I wrap up the initial todo app samples, just to get started and provide details on how to get started I’m going to move on to building a *real*, *real world applications sample*, so *real* that it could be implemented by [Sound Transit](https://en.wikipedia.org/wiki/Sounder_commuter_rail), [Brightline](https://gobrightline.com/), [Virgin Rail](https://en.wikipedia.org/wiki/Virgin_Trains), [SNCF’s TGV](https://en.wikipedia.org/wiki/TGV), [Germany’s ICE](https://en.wikipedia.org/wiki/Intercity-Express), or even good ole’ Amtrak here in the United States.

*Next Steps* – Next up I’m going to finish up the todo applications, with the notion that they provide some starting points for people but also for this more complex real world application. I’ll also add some more details and thoughts, and would love to converse, discuss, contributions, or co-hack on this project. Maybe you’ll join me, onward, and may you enjoy this flanged wheel ride and code slinging adventure!
