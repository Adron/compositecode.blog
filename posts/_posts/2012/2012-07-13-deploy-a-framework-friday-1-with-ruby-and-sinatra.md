---
title: 'Deploy a Framework Friday #1 with Ruby and Sinatra'
date: 2012-07-13 04:15:26 -0700
last_modified_at: 2012-07-13 13:37:45 -0700
permalink: /2012/07/13/deploy-a-framework-friday-1-with-ruby-and-sinatra/
slug: deploy-a-framework-friday-1-with-ruby-and-sinatra
wp_id: 5989
original_url: https://compositecode.blog/2012/07/13/deploy-a-framework-friday-1-with-ruby-and-sinatra/
categories:
- Cloud Foundry
- Cloud Speak
- How-to
- Iron Foundry
- Platform (as a Service)
- Ruby on Rails Bits
tags:
- cloud
- cloud computing
- cloud foundry
- deploy
- deployment
- iron foundry
- paas
- platform as a service
- ruby
- sinatra
excerpt: Alright, just for fun I’m kicking off a new blog series. I’m going to publish a new “Deploy a Framework Friday” each week for about the next, well, bunch of weeks. There are a TON of frameworks that are available on PaaS Technologies. This first entry I’m going to implement a simple Sinatra app with …
---

Alright, just for fun I’m kicking off a new blog series. I’m going to publish a new “Deploy a Framework Friday” each week for about the next, well, bunch of weeks. There are a TON of frameworks that are available on PaaS Technologies.

This first entry I’m going to implement a simple Sinatra app with Ruby. Nothing fancy, simply a hello world and the respective deployment to a Cloud Foundry PaaS.

First, let’s whip out the super complex code (right, this isn’t complex, I just like sarcasm). The hello.rb file I created.

```ruby
require 'sinatra'

get '/' do
  "Hello World!"
end

get '/route' do
  "Hello from a route URI!"
end
```

Next add a Gemfile & respective Gemfile.lock as such.

Gemfile

```ruby
source "http://rubygems.org&quot;
gem 'sinatra'
```

Gemfile.lock

```ruby
GEM
  remote: http://rubygems.org/
  specs:
    rack (1.4.1)
    rack-protection (1.2.0)
      rack
    sinatra (1.3.2)
      rack (~> 1.3, >= 1.3.6)
      rack-protection (~> 1.2)
      tilt (~> 1.3, >= 1.3.3)
    tilt (1.3.3)

PLATFORMS
  ruby

DEPENDENCIES
  sinatra
```

Then deploy using the Cloud Foundry VMC.

```bash
vmc push
```

If you’ve forgotten, be sure to target and login first.

```bash
vmc target api.ironfoundry.me
vmc login
```

That does it. Yeah, not a whole lot to get started working on a Sinatra Project. For more information on Sinatra check out the main web presence here <http://www.sinatrarb.com/>.

For more information on [Cloud Foundry](http://www.cloudfoundry.org/) or [Iron Foundry](http://ironfoundry.org/) click on the respective link.

For the code sample, check out the working [“paasIt” code repo](https://github.com/Adron/paasIt) on [Github](http://www.github.com).

Next week I’ll do a baseline ASP.NET MVC 4 Application and get it deployed.
