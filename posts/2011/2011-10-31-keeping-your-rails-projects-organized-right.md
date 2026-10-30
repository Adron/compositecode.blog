---
title: Keeping Your Rails Projects Organized Right!
date: 2011-10-31 00:08:02 -0700
last_modified_at: 2011-11-18 16:19:33 -0800
permalink: /2011/10/31/keeping-your-rails-projects-organized-right/
slug: keeping-your-rails-projects-organized-right
wp_id: 4171
original_url: https://compositecode.blog/2011/10/31/keeping-your-rails-projects-organized-right/
categories:
- How-to
- Ruby on Rails Bits
tags:
- branch
- branching
- git
- merge
- merging
- rails
- rebase
- rebasing
- ruby
- ruby environment manager
- ruby on rails
- rvm
excerpt: 'I’ve been working with Rails now for about 3 months. At first I jumped right in like a bull in a china shop. I have since, suffered the frustration of doing so. I’ve experimented on OS-X, Windows, and Linux (primarily the Ubuntu Distro). Among these three operating systems, getting up and running with rails is a breeze. Sure, I’ve wrecked more than a few apps I started, blown to smithereens a few machine images, and been generally destructive – but that’s not a bad way to learn at all. 😉 Through this trundling, I’ve come to find there are a few things that should be reviewed and learned thoroughly before smashing into the china shop (i.e. rails or Ruby for that matter). One of these tools is RVM. Another is Git. These tools, without doubt or question, you MUST LEARN! There is just too much value in both of these tools to try to ignore either one. First a quick description of each: Git – Git is a source control server and respective client software. RVM – Ruby enVironment Manager – RVM, sometimes referred to as the Ruby Version Manager also, is a way to maintain the various gems and other environment settings that are used for a particular project. It enables switching back and forth between versions of ruby, keeping ruby updated, and much much more. In .NET, think of it as choosing which version of .NET to use, except with more power to go beyond just merely choosing which version. These two tools are pivotal in having a smooth, consistent, and understandable workflow. There is one other issue for Windows users here though, RVM does not and will not ever run on Windows. One can however install cygwin to get it running or they can use Pik.'
---

I’ve been working with Rails now for about 3 months. At first I jumped right in like a bull in a china shop. I have since, suffered the frustration of doing so. I’ve experimented on OS-X, Windows, and Linux (primarily the Ubuntu Distro). Among these three operating systems, getting up and running with rails is a breeze. Sure, I’ve wrecked more than a few apps I started, blown to smithereens a few machine images, and been generally destructive – but that’s not a bad way to learn at all. 😉

Through this trundling, I’ve come to find there are a few things that should be reviewed and learned thoroughly before smashing into the china shop (i.e. rails or Ruby for that matter). One of these tools is RVM. Another is Git. These tools, without doubt or question, you MUST LEARN! There is just too much value in both of these tools to try to ignore either one. First a quick description of each:

> [Git](http://git-scm.com/) – Git is a source control server and respective client software.
>  
> [RVM – Ruby enVironment Manager](http://beginrescueend.com/) – RVM, sometimes referred to as the Ruby Version Manager also, is a way to maintain the various gems and other environment settings that are used for a particular project. It enables switching back and forth between versions of ruby, keeping ruby updated, and much much more.  In .NET, think of it as choosing which version of .NET to use, except with more power to go beyond just merely choosing which version. These two tools are pivotal in having a smooth, consistent, and understandable workflow. There is one other issue for Windows users here though, RVM does not and will not ever run on Windows. One can however install [cygwin](http://www.cygwin.com/) to get it running or they can use [Pik](https://github.com/vertiginous/pik).

## Workflows

Below I have a short workflow tutorial, which I’ve broken out to *getting started*, *working*, and *operational*.

### Getting Started

This is the first stage of any development project. Regardless of using PHP, Rails, .NET, Java, or whatever, there are certain things that need done. The key elements that I’ve found over the years include, not in any particular order;

- Setup source control
- Setup your environment
- Start your basic project

After each of these things are done, and working together properly, it’s time to get coding. 🙂  First, setup a directory that will be the home for the entire project.

```bash
$ mkdir sampleWorkflow
```

Next run the command to setup your environment for this specific project.

```bash
$ rvm --rvmrc --create 1.9.2@sampleWorkflow
$ cd ..
$ cd sampleWorkflow/
==============================================================================
= NOTICE                                                                     =
==============================================================================
= RVM has encountered a new or modified .rvmrc file in the current directory =
= This is a shell script and therefore may contain any shell commands.       =
=                                                                            =
= Examine the contents of this file carefully to be sure the contents are    =
= safe before trusting it! ( Choose v[iew] below to view the contents )      =
==============================================================================
Do you wish to trust this .rvmrc file? (/Users/adron/a_code/sampleWorkflow/.rvmrc)
y[es], n[o], v[iew], c[ancel]> yes
$ ruby -v
ruby 1.9.2p290 (2011-07-09 revision 32553) [x86_64-darwin10.8.0]
$
```

In the command above, rvm being the application, –rvmrc the parameter for what is being done, and –create is the command for the action to be taken. The 1.9.2 before the @ is the Ruby version and the value after the @ is the environment name, in this case being the same as the folder.

Once the command is run, move out and back into the folder to view how the rvmrc file will work. When you navigate into the directory again, the script will run, initiating the environment for Ruby 1.9.2. It will also ask to confirm if you trust the file. Running the ruby -v command to determine the version, will now display the active ruby version for this folder.

If you’re only using one version of Ruby, this might not seem that useful. But over time as you work with multiple projects, you will often find that different projects use different versions of Ruby. Sometimes 1.8.7 or jruby or rubinius. If that’s the case, rvm is a life saver in simplifying and keeping environments neatly organized.

Now that the environment is setup, we’ll need source control setup and as I generally prefer, an initial commit. Make sure to move into the directory that was just created. Issue the following git commands.

```bash
$ git init
Initialized empty Git repository in /Users/adron/a_code/sampleWorkflow/.git/
$
```

With our directory now intialized for git, it is best to get a git .gitignore file created. (I know, that’s a lot of get gittin). Use mate, or whatever your editor is you prefer, and create a .gitignore file.

```bash
$ mate .gitignore
```

At this point you’ll want to add something to the ignore file. I always start with the following basic files and folders to ignore. I’ve also written a short entry on what these files and folders are that I’m ignoring in the post [Gotta Get Git](/2011/09/09/gotta-get-git/).

```bash
#OS junk files
[Tt]humbs.db
*.DS_Store
.sass-cache/
.bundle

#Webstorm & Rubymine files
*.idea
.idea
.idea/

#Rails Heroku and other bits to ignore
*.sqlite3
db/*.sqlite3
public/system/*
.bundle
log/*.log
tmp/**/*
tmp/*
doc/api
doc/app
*.swp
*~
```

Once that is entered, save the file and close. Next we’ll do our first commit. This is always a good practice, then there are no accidental commits of files that aren’t needed. Also note, I did not exclude the rvmrc file, this is needed to insure clarity about the environment when cloning the repository in the future.

```bash
$ git add -A
$ git commit -m 'first commit'
[master (root-commit) ea81bed] first commit
 3 files changed, 131 insertions(+), 0 deletions(-)
 create mode 100644 .gitignore
 create mode 100644 .rvmrc
 create mode 100644 .rvmrc.10.29.2011-11:33:32
$
```

Now that this is recorded in source control history (not of course in the main repo, we’ll do that in a second) I like to go ahead and create the rails application. Move to a directory just below where the ‘sampleWorkflow’ directory is and create a rails application named the same thing. Since we already created the .gitignore file, we’ll be prompted to overwrite, which isn’t needed since the .gitignore is already setup correctly.

```bash
$ ls
sampleWorkflow		someOtherAppOrSomething
$ rails new sampleWorkflow
       exist
      create  README
      create  Rakefile
      create  config.ru
    conflict  .gitignore
Overwrite /Users/adron/a_code/sampleWorkflow/.gitignore? (enter "h" for help) [Ynaqdh] n
        skip  .gitignore
      create  Gemfile
      create  app
      create  app/assets/images/rails.png
      create  app/assets/javascripts/application.js
      create  app/assets/stylesheets/application.css
```

*…more stuff shows up…*

```bash
 create  tmp/cache
      create  tmp/cache/assets
      create  vendor/assets/stylesheets
      create  vendor/assets/stylesheets/.gitkeep
      create  vendor/plugins
      create  vendor/plugins/.gitkeep
         run  bundle install
Fetching source index for http://rubygems.org/
Using rake (0.9.2.2)
Using multi_json (1.0.3)
Using activesupport (3.1.1)
Using builder (3.0.0)
Using i18n (0.6.0)
Using activemodel (3.1.1)
Using erubis (2.7.0)
```

*…more stuff shows up…*

```bash
Using railties (3.1.1)
Using coffee-rails (3.1.1)
Using jquery-rails (1.0.16)
Using rails (3.1.1)
Using sass (3.1.10)
Using sass-rails (3.1.4)
Using sqlite3 (1.3.4)
Using turn (0.8.3)
Using uglifier (1.0.4)
Your bundle is complete! Use `bundle show [gemname]` to see where a bundled gem is installed.
```

…and then when finished do a commit of the recent additions.

```bash
$ git add -A
$ git commit -m 'Adding Rails 3.1 Project.'
```

Now add the appropriate remote sources for git and the project is ready for development.

```bash
$ git remote add origin git@github.com:Adron/Kata-Coding-in-Rails.git
$ git remote -v
origin	git@github.com:Adron/Kata-Coding-in-Rails.git (fetch)
origin	git@github.com:Adron/Kata-Coding-in-Rails.git (push)
```

The example, with extra example code in place, is available on @Github at <https://github.com/Adron/Kata-Coding-in-Rails>.

### Operational

On a regular basis, while coding, one wants to commit their regular work and push those changes to the server (@Github in this scenario). After every change, add the changes to the commit, then commit with a message as shown. When done, do a pull to insure everything is up to date and then a push.

```bash
$ git status
# On branch master
# Changes not staged for commit:
#   (use "git add ..." to update what will be committed)
#   (use "git checkout --- ..." to discard changes in working directory)
#
#	modified:   Gemfile
#
no changes added to commit (use "git add" and/or "git commit -a")
$ git add -A
$ git commit -m 'updated Gemfile.'
[master b06aa76] updated Gemfile.
 1 files changed, 0 insertions(+), 1 deletions(-)
$ git pull
Already up-to-date.
$ git push
Counting objects: 5, done.
Delta compression using up to 8 threads.
Compressing objects: 100% (3/3), done.
Writing objects: 100% (3/3), 289 bytes, done.
Total 3 (delta 2), reused 0 (delta 0)
To git@github.com:Adron/Kata-Coding-in-Rails.git
   6986cd0..b06aa76  master -> master
$
```

### Operational

This section, I’m going to primarily provide a bunch of links to specific instances of features for Git or RVM.

[Git Branching](http://book.git-scm.com/3_basic_branching_and_merging.html)

```bash
$ git checkout -b modify-branchSwitched to a new branch 'modify-branch'$ git branch  master* modify-branch
```

*…make some changes…*

```bash
$ git add -A
$ git commit -m 'committing a minor readme.md file change while in a branch.'
[modify-branch 726e770] committing a minor readme.md file change while in a branch.
 1 files changed, 3 insertions(+), 1 deletions(-)
$ git push
Everything up-to-date
$ git checkout master
Switched to branch 'master'
$ git merge modify-branch
Updating b967d4e..726e770
Fast-forward
 README.md |    4 +++-
 1 files changed, 3 insertions(+), 1 deletions(-)
$ git branch -d modify-branch
Deleted branch modify-branch (was 726e770).
$
```

Git Rebasing

- [Rebasing](http://book.git-scm.com/4_rebasing.html)
- [Interactive Rebasing](http://book.git-scm.com/4_interactive_rebasing.html)

Git Stashing

- [Stashes](http://book.git-scm.com/4_stashing.html)

Managing Gemsets

- [Basic of Gemsets](http://beginrescueend.com/gemsets/basics/)
- [Listing Gemsets](http://beginrescueend.com/gemsets/listing/)
- [Creating Gemsets](http://beginrescueend.com/gemsets/creating/)
- [Deleting Gemsets](http://beginrescueend.com/gemsets/deleting/)
- [RVM Best Practices](http://beginrescueend.com/rvm/best-practices/)
