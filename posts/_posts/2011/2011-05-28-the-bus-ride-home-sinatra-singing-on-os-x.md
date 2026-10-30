---
title: The Bus Ride Home, Sinatra Singing on OS-X
date: 2011-05-28 19:05:58 -0700
last_modified_at: 2011-05-28 17:45:59 -0700
permalink: /2011/05/28/the-bus-ride-home-sinatra-singing-on-os-x/
slug: the-bus-ride-home-sinatra-singing-on-os-x
wp_id: 2886
original_url: https://compositecode.blog/2011/05/28/the-bus-ride-home-sinatra-singing-on-os-x/
categories:
- How-to
- Ruby on Rails Bits
tags:
- heroku
- os-x
- ruby
- ruby on rails
- rubymine
- sinatra
excerpt: This is just a quick getting started I walked through to get Sinatra going on OS-X. 1sudo gem install sinatra 2sudo gem install shotgun 3sudo gem install haml 4sudo gem install unicorn After installing these things I created a new folder in a Rubymine Project. New Empty Project in Rubymine I added a Ruby Class named SinatraSingsOsx to the project. I then realized that Rubymine did not detect that I had installed Sinatra, so I did a quick find in Rubymine to find and get it synced/installed so that Rubymine was aware of the gems.
---

This is just a quick getting started I walked through to get Sinatra going on OS-X.

```bash
sudo gem install sinatra
sudo gem install shotgun
sudo gem install haml
sudo gem install unicorn
```

After installing these things I created a new folder in a Rubymine Project.

[![New Empty Project in Rubymine](/images/adronhall.smugmug.com/Software/Software-Development/Sinatra-Singing-OS-X/i-cfmVwWd/0/O/Screen-shot-2011-05-28-at.png "New Empty Project in Rubymine")](http://adronhall.smugmug.com/Software/Software-Development/Sinatra-Singing-OS-X/17267233_2Sz8PZ#1311049163_cfmVwWd-A-LB)

*New Empty Project in Rubymine*

I added a Ruby Class named SinatraSingsOsx to the project. I then realized that Rubymine did not detect that I had installed Sinatra, so I did a quick find in Rubymine to find and get it synced/installed so that Rubymine was aware of the gems.

[![Rubymine IDE](/images/adronhall.smugmug.com/Software/Software-Development/Sinatra-Singing-OS-X/i-SHtHMZh/0/S/Screen-shot-2011-05-28-at-S.png "Rubymine IDE")](http://adronhall.smugmug.com/Software/Software-Development/Sinatra-Singing-OS-X/17267233_2Sz8PZ#1311100925_SHtHMZh-O-LB)

*Rubymine IDE*

Using the gem quick install in Rubymine I chose the documentation and dependent gems.

[![Rubymine Gem Quick Install](/images/adronhall.smugmug.com/Software/Software-Development/Sinatra-Singing-OS-X/i-cGxsLBD/0/O/Screen-shot-2011-05-28-at.png "Rubymine Gem Quick Install")](http://adronhall.smugmug.com/Software/Software-Development/Sinatra-Singing-OS-X/17267233_2Sz8PZ#1311100923_pmMV5k8-O-LB)

*Rubymine Gem Quick Install*

Once those were synced up I added the following Ruby Code to the file I created in the project.

```ruby
require 'rubygems'
require 'sinatra'

get '/' do
  "Verified: Server is up and running!"
end
```

I then right clicked on the ruby file and selected the “Run the sinatra\_singing\_osx” which starts up the webrick web server and such.

[![Rubymine Run Page Dialog](/images/adronhall.smugmug.com/Software/Software-Development/Sinatra-Singing-OS-X/i-rHWTS9R/0/S/Screen-shot-2011-05-28-at-S.png "Rubymine Run Page Dialog")](http://adronhall.smugmug.com/Software/Software-Development/Sinatra-Singing-OS-X/17267233_2Sz8PZ#1311218382_rHWTS9R-O-LB)

*Rubymine Run Page Dialog*

Then navigate to <http://localhost:4567> and you’ll see the results of the code.

[![Sinatra Web Application Running in Chrome](/images/adronhall.smugmug.com/Software/Software-Development/Sinatra-Singing-OS-X/i-Ncxrt5W/0/S/Screen-shot-2011-05-28-at-S.png "Sinatra Web Application Running in Chrome")](http://adronhall.smugmug.com/Software/Software-Development/Sinatra-Singing-OS-X/17267233_2Sz8PZ#1311218383_Ncxrt5W-O-LB)

*Sinatra Web Application Running in Chrome*

Now that I’ve run the application in Rubymine I wanted to do the same with Shotgun using the same Ruby code. The first thing I needed to do was stop the server running that Rubymine had launched. If you look at the bottom of the IDE you’ll see the window displaying the current server status.

[![Web Server Executing](/images/adronhall.smugmug.com/Software/Software-Development/Sinatra-Singing-OS-X/i-3p8M7hL/0/S/Screen-shot-2011-05-28-at-S.png "Web Server Executing")](http://adronhall.smugmug.com/Software/Software-Development/Sinatra-Singing-OS-X/17267233_2Sz8PZ#1311225212_3p8M7hL-O-LB)

*Web Server Executing*

On the left hand side of this status window click on the large red button. This will stop the service. To verify just scroll to the bottom of this status window and you will see the message “*Process finished with exit code 1*“.

Now that I had the server cleaned up and stopped, I started a terminal again and navigated to the directory that the \*.rb file is in that I want to start (host/run/execute, I’m not really sure what the appropriate word would really be at this point). So once at the appropriate path (machineName:SinatraSingingOSX adron$) I typed:

```bash
shotgun -p 4567 sinatra_singing_osx.rb
```

Once this executes the same server that Rubymine uses, the WEBrick, will startup the application again. I launched the browser to assure this ran as expected and got the same results as if running it through Rubymine. I guess, it all really depends, want to just start building and checking things out or want to build with an IDE like Rubymine. It all really boils down to taste and what you’re working with. I’ve been going back and forth between pure text editor and IDE just to familiarize myself with both avenues of using Rails and coding with Ruby.

After the verification I hit Ctrl + C to stop the web server. This basically works on the msysgit in Windows, on OS-X, or on whatever distro of Linux you have running. The cool thing is, so does Rubymine. I figured if I was going to work toward familiarization of an IDE and using the terminal I’d use commands and IDEs that would work on whatever OS I’m running. It’s all good synergies that way. 🙂

I wanted to keep this entry pretty short. With that in mind I simply logged what I worked on while en route home on the bus one evening. So on the next bus ride I’m going to tackle getting some specific notes with Sinatra, getting this all pushed into [Heroku](http://www.heroku.com) (of course, I’m all about the Cloud, you didn’t think I’d put it up on a shared host did you!) Until then, chow.
