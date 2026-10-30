---
title: What’s The Practice with Rider & .NET Solutions/Projects? How to resolve IDE errors?
date: 2024-05-19 11:59:18 -0700
last_modified_at: 2024-05-19 11:59:18 -0700
permalink: /2024/05/19/whats-the-practice-with-rider-net-solutions-projects-how-to-resolve-ide-errors/
slug: whats-the-practice-with-rider-net-solutions-projects-how-to-resolve-ide-errors
wp_id: 68536
original_url: https://compositecode.blog/2024/05/19/whats-the-practice-with-rider-net-solutions-projects-how-to-resolve-ide-errors/
categories:
- .NET Bits
- c#
- Unknown Code Ramblings
tags:
- c#
- dotnet
- dotnet IDE
- ide
- jetbrains
- jetbrains rider
- Rider
excerpt: The writer discusses setting up a .NET solution and respective projects, highlighting issues with file management in different IDEs. They typically create an empty solution, add a class library and test project, and handle extra files like .gitignore and README.md. They also face problems with awareness in the IDE when using an “Open a Folder Solution.”
image: /wp-content/uploads/2024/05/top-image.png
---

Alright, I’ve fought with these kinds of things since the inception of .NET, the key difference now is that there are the variances in .NET versions and also IDEs. The question is, how should I setup my solution and respective projects?

## First – .NET Solution

Usually what I do is create an empty solution. Name it, check the options accordingly to create a directory and make it a Git repository.

[![](/wp-content/uploads/2024/05/CleanShot-2024-05-19-at-11.27.14@2x.png)](/wp-content/uploads/2024/05/CleanShot-2024-05-19-at-11.27.14@2x.png)

Then, as a kind of general practice I create a class library to build out logic and what not, and add a test project and then whatever the interface is going to be. That might be a web app, a GUI, or console as I’ve got selected here. Sometimes, if useful I go ahead and create a Dockerfile.

[![](/wp-content/uploads/2024/05/CleanShot-2024-05-19-at-11.29.24@2x.png)](/wp-content/uploads/2024/05/CleanShot-2024-05-19-at-11.29.24@2x.png)

At this point, there are a few key problems I always bump into. Obviously, since I have a repo I need a .gitignore file, preferably a README.md, and maybe even a license file right? How does one add, so that the IDE is aware of them, any extra files at the *solution level*? What I usually do here, is use the terminal to just build out the solution level files, but then the IDE doesn’t know about them. Similar problems come up in the other .NET IDEs like Visual Studio and such.

[![](/wp-content/uploads/2024/05/CleanShot-2024-05-19-at-11.31.26@2x.png)](/wp-content/uploads/2024/05/CleanShot-2024-05-19-at-11.31.26@2x.png)

## Second – Open a Folder Solution

The second type of solution I find myself creating is started by opening a repo folder.

[![](/wp-content/uploads/2024/05/CleanShot-2024-05-19-at-11.50.45@2x.png)](/wp-content/uploads/2024/05/CleanShot-2024-05-19-at-11.50.45@2x.png)

Empty, with nothing else that looks like this.

[![](/wp-content/uploads/2024/05/CleanShot-2024-05-19-at-11.51.22@2x.png)](/wp-content/uploads/2024/05/CleanShot-2024-05-19-at-11.51.22@2x.png)

Creating a .gitignore and other respective files is easy at this point. As a right click will allow me to do just that. I’ve also added some projects.

[![](/wp-content/uploads/2024/05/CleanShot-2024-05-19-at-11.53.59@2x.png)](/wp-content/uploads/2024/05/CleanShot-2024-05-19-at-11.53.59@2x.png)

At this point everything works great. As you can see below the runner is wired up, the IDE is aware of the tests, and runners are available for that.

[![](/wp-content/uploads/2024/05/CleanShot-2024-05-19-at-11.55.22@2x.png)](/wp-content/uploads/2024/05/CleanShot-2024-05-19-at-11.55.22@2x.png)

One problem I’ve run into however with this technique, is sometimes I close this type of project – one started by merely opening the folder – and all this awareness just disappears. On the same machine, same folder, no deletion of the .idea folder or anything like that. It just loses all the awareness.

So my question is, which method do you use to start a project and how to do you, fellow .NET coders, work around these types of issues?
