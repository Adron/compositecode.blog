---
title: Steaming Up The Engine for The Rails
date: 2011-11-22 15:17:56 -0800
last_modified_at: 2011-11-22 15:17:56 -0800
permalink: /2011/11/22/steaming_up_the_engine/
slug: steaming_up_the_engine
wp_id: 4345
original_url: https://compositecode.blog/2011/11/22/steaming_up_the_engine/
categories:
- How-to
- Ruby on Rails Bits
tags:
- rails
- ruby
excerpt: I’ve been digging through and playing with the Rails Framework now for about 4 months with intent (I guess I’ve read about it, learned about, but not played with it for well over 4 years). I’ve gained a pretty good familiarity with the parts of the framework. Below, I’ve laid out some of the key things that I’ve done over and over just to become familiar with the commands, organization, and other elements within the framework. These also, in this specific order, is what I’ve found works best for getting a Ruby on Rails Application Project kick started (on a *nix based machine, the rvm commands will however not work on Windows, you’ll need to find a respective replacement). …click through to read more…
---

I’ve been digging through and playing with the Rails Framework now for about 4 months with intent (I guess I’ve read about it, learned about, but not played with it for well over 4 years). I’ve gained a pretty good familiarity with the parts of the framework. Below, I’ve laid out some of the key things that I’ve done over and over just to become familiar with the commands, organization, and other elements within the framework. These also, in this specific order, is what I’ve found works best for getting a Ruby on Rails Application Project kick started (on a \*nix based machine, the rvm commands will however not work on Windows, you’ll need to find a respective replacement).

```bash
$ mkdir steaming_up_the_engine
$ cd steaming_up_the_engine
$ rvm --rvmrc --create 1.9.2@steaming_up_the_engine
$ cd ..
$ cd steaming_up_the_engine
$ cd ..
$ rails new steaming_up_the_engine -T
$ open .
$ cd steaming_up_the_engine
$ git init
$ mate .gitignore
```

…edit and save the .gitignore file with whatever additions you may need or want…

```bash
$ git -A
$ git commit -m 'first commit.'
$ rm public/index.html
$ rails generate rspec:install
```

…edit your Gemfile(See below Gemfile for contents)…

```bash
$ rails generate controller home index contact about
$ git rm -r spec/views
$ git rm -r spec/helpers
$ mate config/routes.rb
```

…edit the routes.rb so there is the index page handling the root page…

Gemfile (Located in *~/projectRoot/Gemfile*)

```ruby
source 'http://rubygems.org&#8217;

gem 'rails'
gem 'sqlite3'

group :development do
  gem 'rspec-rails'
end

group :test do
  gem 'rspec-rails'
  gem 'webrat'
end

group :assets do
  gem 'sass-rails',   '~> 3.1.4'
  gem 'coffee-rails', '~> 3.1.1'
  gem 'uglifier', '>= 1.0.3'
end

gem 'jquery-rails'
```

route.rb file.

```ruby
SteamingUpTheEngine::Application.routes.draw do
  get "home/index"
  get "home/about"
  get "home/contact"
  root :to => 'home#index'
end
```

***mkdir*** creates a new directory called steaming\_up\_the\_engine.

***cd steaming\_up\_the\_engine*** moves the active working directory of the terminal/bash to steaming\_up\_the\_engine (i.e. cd stands for change directory).

***rvm*** is the rvm application command, –rvmrc is the feature being created, –create is the command to issue on the feature.  1.9.2 is the version of Ruby that will be used for the project and the name after the @ is the name of the project itself. For more information about the rvmrc script check out my previous [entry](/2011/10/31/keeping-your-rails-projects-organized-right/) or the [rvm site on rvmrc](http://beginrescueend.com/workflow/rvmrc/).

The action to ***cd ..*** moves out of the directory and then ***cd steaming\_up\_the\_engine*** moves back in to initiate the script that the rvm command created for us. After that, the working directory is moved back outside of the application folder.

***rails*** is simply the rails framework application command, ***new*** tells the application to create a new rails application based on the framework, and ***-T*** is a switch to prevent any tests from being generated.

***open .*** actually opens the Finder to view the just created project in the working directory. The screenshot below is the Finder with the newly created rails app.

[![Finder showing the newly created Rails Application in a column display.](/images/adronhall.smugmug.com/Software/Software-Development/Getting-Muscle-Memory-Around/i-tSFBDj9/0/O/Screen-shot-2011-11-18-at.png "Finder showing the newly created Rails Application in a column display.")](http://adronhall.smugmug.com/Software/Software-Development/Getting-Muscle-Memory-Around/20153886_CMqKGh/1591261709_tSFBDj9#1591261709_tSFBDj9-A-LB)

*Finder showing the newly created Rails Application in a column display.*

Again move back into the application working directory.

***git init*** initializes a local git repository for the project.

***mate .gitignore*** opens up the .gitignore file that was created by the rails command for editing.  mate is the command for the TextMate Application. If you don’t have TextMate, then you would have to change mate to a command that relates to whatever you use to edit your code files. Check out my previous [blog entry](/2011/10/31/keeping-your-rails-projects-organized-right/) for a sample .gitignore file.

***git -A*** adds all new files for commit to the local git repository.

***git commit -m ‘first commit’*** actually commits the new project to the git repository.

***rm public/index.html*** removes the default static page that displays if the application is run at this point. I never need it, but it does come in handy sometimes if you’re troubleshooting if a server runs and just want to deploy something to verify you’re doing it right (such as to [EngineYard](http://www.engineyard.com) or [Heroku](http://www.heroku.com)).

rspec can be setup and configured to run in your Rails project with the rails command ***rails generate rspec:install***. If the rspec gem isn’t already in your project, remember to ***gem install rspec*** or add it to the gemfile and run ***bundle install***.

The first of these commands that actually starts building the site is the rails generator command. ***rails generate controller Pages home contact*** creates the pages, controllers, and routes for the pages. Because the rspec has been configured for the project, when rails generates the controller and pages tests will be created in the spec directory.

After the creation of those pages remove the unnecessary test files in helpers and views under spec. ***git rm -r spec/views*** and ***git rm -r spec/helpers*** will get rid of these files.

Now you’re ready to really get started actually building something in those pages. Enjoy!
