---
title: Last Night’s Cafe Racer Ruby on Rails Meetup; Kilt Lifter, EngineYard, Heroku and a Ruby Tone
date: 2011-09-20 16:53:00 -0700
last_modified_at: 2011-09-25 10:45:47 -0700
permalink: /2011/09/20/last-nights-cafe-race-ruby-on-rails-meetup-kilt-lifter-engineyard-heroku-and-a-ruby-tone/
slug: last-nights-cafe-race-ruby-on-rails-meetup-kilt-lifter-engineyard-heroku-and-a-ruby-tone
wp_id: 3887
original_url: https://compositecode.blog/2011/09/20/last-nights-cafe-race-ruby-on-rails-meetup-kilt-lifter-engineyard-heroku-and-a-ruby-tone/
categories:
- Coding Adventures
- Ruby on Rails Bits
tags:
- cafe racer
- kilt lifter
- rails
- ruby
- ruby on rails
excerpt: 'This evening at the Cafe Racer Ruby on Rails meetupI knocked out these specific tasks. Kilt Lifter by Pike Brewing Company Drank a solid tasty Kilt Lifter. Created a sample beginning application, with standard migrations, and errata, and made two simple models with respective scaffolding. Deployed the beginnings of a sample application to Heroku. Deployed the beginnings of a sample application to EngineYard. For Kilt Lifter information, click on the image at the right. If you live in the northwest, you know what’s up with the beer capital of the world (i.e. Portland, and the northwest in general, for info see here). We love our beer up here in these parts, we love it with a passion and it shows with more brewpubs, beer options, varieties, home brews, and other flavors than anywhere else in the world. No, I did not mis-state that, the northwest has more than anywhere else in the world, almost by an order of magnitude! More than Germany, Ireland, England, the East Coast of the US, and the list goes on. So if you’re up for a beer and some coding, or just a beer, head to the northwest! We’ll have a few for ya to taste. 😉 The initial Ruby on Rails Application I created I started with RubyMine from Jetbrains. Simply a File -> New Project -> Rails Application, etc, etc. I worked through some of the issues with fellow rubiests and railers at the meetup. We did run into a confusing and nasty issue with Postgresql. Why was I installing Postgresql you ask? Well I was trying to do a deployment to Heroku, which provides a free shared instance of postgresql. I gotta admit, of all the things that Heroku makes absurdly easy, setting up a database is not one of them. Maybe I’m missing a bit, but I don’t know what the instance of the server is, what the username or password is, or anything of that sort. It isn’t all that intuitive that you have to add the database as an add-on either. At least, it wasn’t to the 3-4 of us that were working on it. The other problem I ran into was what process I should actually use to install Postgresql. The firsts thing I tried to do was submit the “gem install pg” which ended with a completely wonky description. The error message read as: $ sudo gem install pg Building native extensions. This could take a while… ERROR: Error installing pg: ERROR: Failed to build gem native extension. /System/Library/Frameworks/Ruby.framework/Versions/1.8/usr/bin/ruby extconf.rb install pg extconf.rb:1: command not found: pg_config –version ERROR: can’t find pg_config. HINT: Make sure pg_config is in your PATH … I found a fix, here put together by Graham Ashton. Thanks Graham! Meanwhile I dived into EngineYard and got the application up and running in short order. I have to say I am much impressed by the increased visibility into what’s going on with EngineYard. Heroku seems to hide just a bit too much. Add to that their over-reliance on AWS East and not geographically dispersing the platform, I’m leaning even heavier on suggesting EngineYard for startups and companies that want a cloud provider platform to build to. Once the applications I’ve been working on get to a certain state, I’ll be providing a write up regarding the applications. However, until then, feel free to follow me on Twitter and Github or jump in fork my code and send me a pull request. 🙂 Kilt Lifter by Pike Brewing Company Drank a solid tasty Kilt Lifter. Created a sample beginning application, with standard migrations, and errata, and made two simple models with respective scaffolding. Deployed the beginnings of a sample application to Heroku. Deployed the beginnings of a sample application to EngineYard. For Kilt Lifter information, click on the image at the right. If you live in the northwest, you know what’s up with the beer capital of the world (i.e. Portland, and the northwest in general). We love our beer up here in these parts, we love it with a passion and it shows with more brewpubs, beer options, varieties, home brews, and other flavors than anywhere else in the world. No, I did not mis-state that, the northwest has more than anywhere else in the world, almost by an order of magnitude! More than Germany, Ireland, England, the East Coast of the US, and the list goes on. So if you’re up for a beer and some coding, or just a beer, head to the northwest! We’ll have a few for ya to taste. 😉 The initial Ruby on Rails Application I created I started with RubyMine from Jetbrains. Simply a File -> New Project -> Rails Application, etc, etc. I worked through some of the issues with fellow rubiests and railers at the meetup. We did run into a confusing and nasty issue with Postgresql. Why was I installing Postgresql you ask? Well I was trying to do a deployment to Heroku, which provides a free shared instance of postgresql. I gotta admit, of all the things that Heroku makes absurdly easy, setting up a database is not one of them. Maybe I’m missing a bit, but I don’t know what the instance of the server is, what the username or password is, or anything of that sort. It isn’t all that intuitive that you have to add the database as an add-on either. At least, it wasn’t to the 3-4 of us that were working on it. The other problem I ran into was what process I should actually use to install Postgresql. The firsts thing I tried to do was submit the “gem install pg” which ended with a completely wonky description. The error message read as: $ sudo gem install pg Building native extensions. This could take a while… ERROR: Error installing pg: ERROR: Failed to build gem native extension. /System/Library/Frameworks/Ruby.framework/Versions/1.8/usr/bin/ruby extconf.rb install pg extconf.rb:1: command not found: pg_config –version ERROR: can’t find pg_config. HINT: Make sure pg_config is in your PATH … I found a fix, here put together by Graham Ashton. Thanks Graham! Meanwhile I dived into EngineYard and got the application up and running in short order. I have to say I am much impressed by the increased visibility into what’s going on with EngineYard. Heroku seems to hide just a bit too much. Add to that their over-reliance on AWS East and not geographically dispersing the platform, I’m leaning even heavier on suggesting EngineYard for startups and companies that want a cloud provider platform to build to. Once the applications I’ve been working on get to a certain state, I’ll be providing a write up regarding the applications. However, until then, feel free to follow me on Twitter and Github or jump in fork my code and send me a pull request. 🙂'
---

Yesterday evening at the [Cafe Racer](http://maps.google.com/maps/place?q=cafe+race&hl=en&cid=6390701145359639987) [Ruby on Rails meetup](http://www.meetup.com/The-Seattle-Ruby-on-Rails-Developers-Meetup-Group/)I knocked out these specific tasks.

[![Kilt Lifter by Pike Brewing Company](/images/adronhall.smugmug.com/Software/Meetups-N-Conferences/Cafe-Race-Ruby-on-Rails-Meetup/i-d6QjnD5/0/O/pikekiltlifterlabel.gif "Kilt Lifter by Pike Brewing Company")](http://www.pikebrewing.com/)

*Kilt Lifter by Pike Brewing Company*

- Drank a solid tasty [Kilt Lifter](http://www.pikebrewing.com/beers_PikeKiltLifter.shtml).
- Created a sample beginning application, with standard migrations, and errata, and made two simple models with respective scaffolding.
- Deployed the beginnings of a sample application to [Heroku](http://www.heroku.com).
- Deployed the beginnings of a sample application to [EngineYard](http://www.engineyard.com).

[![](/images/adronhall.smugmug.com/Software/Meetups-N-Conferences/Cafe-Race-Ruby-on-Rails-Meetup/i-2Cr9gs3/0/S/CraftBreweriesPerCapitaUS-S.png)](http://en.wikipedia.org/wiki/Microbrewery)For Kilt Lifter information, click on the image at the right. If you live in the northwest, you know what’s up with the beer capital of the world (i.e. Portland, and the northwest in general, for info see [here](http://en.wikipedia.org/wiki/Microbrewery) or click on the image to the left). We love our beer up here in these parts, we love it with a passion and it shows with more brewpubs, beer options, varieties, home brews, and other flavors than anywhere else in the world. No, I did not mis-state that, the northwest has more than anywhere else in the world, almost by an order of magnitude!  More than Germany, Ireland, England, the East Coast of the US, and the list goes on. So if you’re up for a beer and some coding, or just a beer, head to the northwest! We’ll have a few for ya to taste. 😉

The initial [Ruby on Rails](http://rubyonrails.org/) Application I created I started with [RubyMine](http://www.jetbrains.com/ruby/) from [Jetbrains](http://www.jetbrains.com). Simply a File -> New Project -> Rails Application, etc, etc. I worked through some of the issues with fellow rubiests and railers at the meetup. We did run into a confusing and nasty issue with Postgresql. Why was I installing Postgresql you ask? Well I was trying to do a deployment to Heroku, which provides a free shared instance of postgresql. I gotta admit, of all the things that Heroku makes absurdly easy, setting up a database is not one of them. Maybe I’m missing a bit, but I don’t know what the instance of the server is, what the username or password is, or anything of that sort. It isn’t all that intuitive that you have to add the database as an add-on either. At least, it wasn’t to the 3-4 of us that were working on it.

The other problem I ran into was what process I should actually use to install Postgresql. The firsts thing I tried to do was submit the “gem install pg” which ended with a completely wonky description. The error message read as:

```bash
$ sudo gem install pg
Building native extensions.  This could take a while...
ERROR:  Error installing pg:
	ERROR: Failed to build gem native extension.

/System/Library/Frameworks/Ruby.framework/Versions/1.8/usr/bin/ruby extconf.rb install pg
extconf.rb:1: command not found: pg_config --version
ERROR: can't find pg_config.
HINT: Make sure pg_config is in your PATH
...
```

I found a fix, [here](http://effectif.com/databases/installing-pg-gem-on-mac) put together by [Graham Ashton](http://www.zerply.com/profile/grahamashton). Thanks Graham!

The fix involved simply to add a path variable…

```bash
$ PATH=$PATH:/Library/PostgreSQL/8.3/bin sudo gem install pg
```

Meanwhile I dived into EngineYard and got the application up and running in short order. I have to say I am much impressed by the increased visibility into what’s going on with EngineYard. Heroku seems to hide just a bit too much. Add to that their over-reliance on AWS East and not geographically dispersing the platform, I’m leaning even heavier on suggesting EngineYard for startups and companies that want a cloud provider platform to build to.

Once the applications I’ve been working on get to a certain state, I’ll be providing a write up regarding the applications. However, until then, feel free to follow me on [Twitter](https://twitter.com/#!/adron) and [Github](https://github.com/Adron) or jump in fork my code and send me a pull request.  🙂

Update: Just some images from the meetup.

[![Ruby on Rails meetup at Cafe Racer - Corner Table](/images/adronhall.smugmug.com/Software/Meetups-N-Conferences/Cafe-Race-Ruby-on-Rails-Meetup/i-gzx3bPz/0/S/IMAG1322-S.jpg "Ruby on Rails meetup at Cafe Racer - Corner Table")](http://adronhall.smugmug.com/Software/Meetups-N-Conferences/Cafe-Race-Ruby-on-Rails-Meetup/19114714_BNvm4g#1493030022_gzx3bPz-A-LB)

*Ruby on Rails meetup at Cafe Racer - Corner Table*

[![Ruby on Rails Meetup at Cafe Racer](/images/adronhall.smugmug.com/Software/Meetups-N-Conferences/Cafe-Race-Ruby-on-Rails-Meetup/i-VdS3P6R/0/S/IMAG1323-S.jpg "Ruby on Rails Meetup at Cafe Racer")](http://adronhall.smugmug.com/Software/Meetups-N-Conferences/Cafe-Race-Ruby-on-Rails-Meetup/19114714_BNvm4g#1493029570_VdS3P6R-A-LB)

*Ruby on Rails Meetup at Cafe Racer*
