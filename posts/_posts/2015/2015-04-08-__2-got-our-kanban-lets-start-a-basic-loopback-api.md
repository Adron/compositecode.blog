---
title: __2 “Starting a Basic Loopback API & Continuous Integration”
date: 2015-04-08 07:15:00 -0700
last_modified_at: 2015-04-06 12:41:36 -0700
permalink: /2015/04/08/__2-got-our-kanban-lets-start-a-basic-loopback-api/
slug: __2-got-our-kanban-lets-start-a-basic-loopback-api
wp_id: 10858
original_url: https://compositecode.blog/2015/04/08/__2-got-our-kanban-lets-start-a-basic-loopback-api/
categories:
- Architecture
- Code Stories
- How-to
- Node.js Things
- nodejs
- ThrashingCode
tags:
- javascript
- node
- node.js
- nodejs
- thrashing code
- thrashingcode
excerpt: 'In this article Keartida is going to dive into setting up a basic Loopback API project and get a build of that project running on a continuous integration service. In this example she’s going to get the project setup with Codeship. Prerequisites: Be sure, whichever system you are using, to have a C++ compiler installed. …'
image: /wp-content/uploads/2015/03/cut2.jpg
---

In this article Keartida is going to dive into setting up a basic Loopback API project and get a build of that project running on a continuous integration service. In this example she’s going to get the project setup with Codeship.

**Prerequisites:**

- Be sure, whichever system you are using, to have a C++ compiler installed. For Windows that usually means installing Visual Studio or something, on OS-X install XCode and the Developer Tools. On Ubuntu the GCC compiler and other options exist. For instructions on OS-X and Linux check out [installing compiler tools](http://docs.strongloop.com/display/SL/Installing+compiler+tools).
- [Ubuntu](https://github.com/Adron/nodejs-training-prerequisites/blob/master/Ubuntu/terminal.md)
- [OS-X](https://github.com/Adron/nodejs-training-prerequisites/blob/master/OS-X/terminal.md)
- For windows, I’d highly suggest setting up a VM of Ubuntu to do any work with Loopback, Node.js, or follow along with this material. It’s possible on Windows, but there are a number of things that are lacking. If you still want to make a go of using Windows, here are some initial [setup steps here](https://github.com/Adron/nodejs-training-prerequisites/blob/master/Windows/terminal.md).

**Nice to Haves:**

- [git-flow](/2014/12/01/git-flow/) – works on any bash, handles the branching and merging. Very nice scripts to have.
- [bashit](http://compositecode.com/2014/10/09/bashit-just-a-custom-bash-prompt-setup-for-git/) – Adding more information to the bash prompt (works on OS-X, not Ubuntu or Windows Bash)

## Loopback

Loopback is an extensible Node.js framework built on [Express](http://expressjs.com/). The key features of the framework focus around generation of RESTful API end points based on models. The model objects can be created from a database, hand coded, generated, or otherwise built for the specific project as [data-transfer object](http://martinfowler.com/eaaCatalog/dataTransferObject.html) style models or whatever you would need for a project. It is important to note that the object models could be setup to also perform and follow architectural patterns similar to the [domain model](http://martinfowler.com/eaaCatalog/domainModel.html) pattern, a semblance to the [active record](http://www.martinfowler.com/eaaCatalog/activeRecord.html), or other patterns. It is really up to the architectural demands of the application being developed and developer choice.

Loopback also has a number of other features, capabilities to add middleware, a GUI to view and manage models, connections, and other capabilities and plugins available. But enough about what it is, let’s dive into the steps Keartida used to get the project up and running. The first thing she did was setup a sample project, just to see how the framework would behave and to work through the intro-tutorials: “[Getting started with Loopback](http://docs.strongloop.com/display/public/LB/Getting+started+with+LoopBack)” and “[Getting started part II](http://docs.strongloop.com/display/public/LB/Getting+started+part+II)“. The repository that she built is available on github at [sample\_loopback\_application](https://github.com/ThrashingCode/sample_loopback_application).

For this particular implementation Keartida started off with a simple installation of Loopback and creating an application. The first thing she had to do was set the directories ‘*/usr/local/bin*‘ and ‘*/usr/local/lib/node\_modules*‘ with write permissions.

```bash
sudo chown -R $USER /usr/local/bin
sudo chown -R $USER /usr/local/lib/node_modules
```

…and then install strongloop (which comes with loopback).

```bash
npm install -g strongloop
```

Once that was installed the Strongloop Loopback tools are ready for use. To create an application Keartida then ran the follow command.

```bash
slc loopback
```

Which then provides the fella ready to help create the application in ASCII art.

```bash
slc loopback

     _-----_
    |       |    .--------------------------.
    |--(o)--|    |  Let's create a LoopBack |
   `---------´   |       application!       |
    ( _´U`_ )    '--------------------------'
    /___A___\
     |  ~  |
   __'.___.'__
 ´   `  |° ´ Y `

? What's the name of your application? sample_loopback_application
```

If you hit enter at this point the helper continues onward with the name ‘coder-swap’. Once the site is generated, verify by running the following command.

```bash
slc run .
```

If you navigate in a browser to the explorer path shown, you’ll see a page like this.

[![Strongloop API Explorer @ 0.0.0.0:3000/explorer/](https://photos.adron.me/photos/i-5KXgLw5/0/O/i-5KXgLw5.png)](https://photos.adron.me/photos/i-5KXgLw5/0/O/i-5KXgLw5.png)

*Strongloop API Explorer @ 0.0.0.0:3000/explorer/*

## Codeship

Now that Keartida had knocked out the generation of the initial application skeleton and had something that was running. The next step toward continuous delivery was to get a build server setup. That’s where [CodeShip](https://codeship.com) comes into play. It’s important to note that CodeShip is much more than merely a build server. CodeShip will also do basic deployments, execute scripts as needed, run tests, and related capabilities are all wrapped neatly into their service.

Navigate to their site and login. If you don’t have an account already, complete that step first. The site uses Github identities so it’ll enable you to just log in as I detail below once you have an account.

[![Sign In](https://photos.adron.me/photos/i-KtwmSmF/0/X2/i-KtwmSmF-X2.png)](https://photos.adron.me/photos/i-KtwmSmF/0/X2/i-KtwmSmF-X2.png)

*Sign In*

Next the screen will provide the option to sign in with either Github or Bitbucket. Pick your poison, but for this mission that the Thrashing Code Team is on, we’ll be using Github.

[![Github or Bitbucket](https://photos.adron.me/photos/i-8fwnWqP/0/X2/i-8fwnWqP-X2.png)](https://photos.adron.me/photos/i-8fwnWqP/0/X2/i-8fwnWqP-X2.png)

*Github or Bitbucket*

Next Github will ask you to authorize the application (CodeShip).

[![Authorization Page](https://photos.adron.me/photos/i-zP7wd8T/0/O/i-zP7wd8T.png)](https://photos.adron.me/photos/i-zP7wd8T/0/O/i-zP7wd8T.png)

*Authorization Page*

When done then the screen to create a build is presented.

[![Build Page](https://photos.adron.me/photos/i-Sm9DGJW/0/O/i-Sm9DGJW.png)](https://photos.adron.me/photos/i-Sm9DGJW/0/O/i-Sm9DGJW.png)

*Build Page*

From there click on “*Let’s do it! Create my first project!*” to get a build started. From there the service will prompt you to connect to your repository service. In this case, again, Keartida selected Github since the Thrashing Code Team has their code on github.

[![Choosing Github Repository](https://photos.adron.me/photos/i-hRppn6m/0/O/i-hRppn6m.png)](https://photos.adron.me/photos/i-hRppn6m/0/O/i-hRppn6m.png)

*Choosing Github Repository*

It is important to note however, that just because we chose a Github repository at this stage for this particular build it doesn’t mean we can select a bitbucket repository for subsequent builds.

Next, select the repository to build.

[![Repository selection.](https://photos.adron.me/photos/i-9CGPKVc/0/O/i-9CGPKVc.png)](https://photos.adron.me/photos/i-9CGPKVc/0/O/i-9CGPKVc.png)

*Repository selection.*

The next task is to select what type of stack to build, in this case we’re building a node.js stack, so Keartida selected node.js from the dropdown. This automatically populated the Setup Commands box with some default commands.

[![Selecting the framework stack for the build.](https://photos.adron.me/photos/i-V3FCnz3/0/O/i-V3FCnz3.png)](https://photos.adron.me/photos/i-V3FCnz3/0/O/i-V3FCnz3.png)

*Selecting the framework stack for the build.*

Scrolling down there’s also a box for builds, eventually we’ll get some tests running using mocha and other libraries, but for now clear out the test box contents completely.

[![Clear this box out for now.](https://photos.adron.me/photos/i-V52HZQH/0/O/i-V52HZQH.png)](https://photos.adron.me/photos/i-V52HZQH/0/O/i-V52HZQH.png)

*Clear this box out for now.*

Once done, click on the “Save and go to dashboard” button. The dashboard will then be displayed with no currently completed builds.

[![Build Dashboard](https://photos.adron.me/photos/i-q5bd39W/0/O/i-q5bd39W.png)](https://photos.adron.me/photos/i-q5bd39W/0/O/i-q5bd39W.png)

*Build Dashboard*

Keartida accepted the [pull request](https://github.com/ThrashingCode/coder-swap/pull/13) this one time, circumventing our normal merge practice of getting a +1 from each other to get the build rolling. The build, should succeed. If it doesn’t, it’s time to troubleshoot, but more on the troubleshooting later. For now, celebrate in a functional continuous integration setup with a skeleton loopback project completed.

## Getting The Team Added

You might have noted, Keartida got the build setup based on her forked repository. That’s all fine and dandy but anybody else on the team in github can’t see her build. What we still need is a team build. So when somebody from the team sets up the build for the ThrashingCode/coder-swap project in CodeShip we can all see it.

[![Team Settings](https://photos.adron.me/photos/i-tm26Lv4/0/O/i-tm26Lv4.png)](https://photos.adron.me/photos/i-tm26Lv4/0/O/i-tm26Lv4.png)

*Team Settings*

[![The Team to add to the ThrashingCode/coder-swap build.](https://photos.adron.me/photos/i-RhSDZkX/0/O/i-RhSDZkX.png)](https://photos.adron.me/photos/i-RhSDZkX/0/O/i-RhSDZkX.png)

*The Team to add to the ThrashingCode/coder-swap build.*

Once added, I kicked off a build and both Keartida and I could then see the build running.

[![Keartida's view...](https://photos.adron.me/photos/i-3hPvg2L/0/O/i-3hPvg2L.png)](https://photos.adron.me/photos/i-3hPvg2L/0/O/i-3hPvg2L.png)

*Keartida’s view…*

[![My view... ](https://photos.adron.me/photos/i-KxPjWgg/0/O/i-KxPjWgg.png)](https://photos.adron.me/photos/i-KxPjWgg/0/O/i-KxPjWgg.png)

*My view…*

[Links for other parts of this series…](http://compositecode.com/docs/thrashing-code-projects/)
