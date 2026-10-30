---
title: Glassfish, Java, JSF and Explorations of IntelliJ IDEA 13
date: 2013-10-15 23:02:21 -0700
last_modified_at: 2013-10-15 23:20:36 -0700
permalink: /2013/10/15/glassfish-java-jsf-and-explorations-of-intellij-idea-13/
slug: glassfish-java-jsf-and-explorations-of-intellij-idea-13
wp_id: 9021
original_url: https://compositecode.blog/2013/10/15/glassfish-java-jsf-and-explorations-of-intellij-idea-13/
categories:
- How-to
- Java
tags:
- glassfish
- intellij
- intellij IDEA
- java
- java enterprise edition
- java server faces
- javaee
- jetbrains
- jsf
excerpt: I recently dove into working with some tooling at Jetbrains. The first thing I needed to take a dive into is the latest EAP of IntelliJ IDEA 13. If you do any sort of Java development you’ve definitely heard of IntelliJ, and if you work in other realms like C#, Node.js & JavaScript, Python or …
---

I recently dove into working with some tooling at Jetbrains. The first thing I needed to take a dive into is the latest [EAP](http://eap.jetbrains.com/) of [IntelliJ IDEA 13](http://confluence.jetbrains.com/display/IDEADEV/IDEA+13+EAP). If you do any sort of Java development you’ve definitely heard of [IntelliJ](http://www.jetbrains.com/idea/), and if you work in other realms like C#, Node.js & JavaScript, Python or other languages you’ve likely heard of other Jetbrains tools like [ReSharper](http://www.jetbrains.com/resharper/), [WebStorm](http://www.jetbrains.com/webstorm/) or [PHPStorm](http://www.jetbrains.com/phpstorm/), [Pycharm](http://www.jetbrains.com/pycharm/) or a host of the other IDEs that they produce. A few ways to describe their product line; solid, quality, useful and kick ass. But I digress, here’s a run down of the look into IntelliJ IDEA 13.

## Getting Something to Serve These Pages

[![](https://photos.adron.me/Software/Software-Development/IntelliJ-Explorations/i-xgMtGk2/0/O/glassfish.png)](https://glassfish.java.net/)[Glassfish 4.0](https://glassfish.java.net/) is the latest and greatest of the Glassfish Server. I downloaded and got the server up and running to use as a base to do local development off of. I had installed Glassfish 3.1.2 but realized rapidly that it just wasn’t a good idea. Thus, a piece of advice, stick to Glassfish 4.

When installing Glassfish 4. I ran into a recurring problem, which is obviously recurring far beyond my use. The installer has the error trapped with an intelligent response.

[![Click for full size image.](https://photos.adron.me/Software/Software-Development/IntelliJ-Explorations/i-h8Wf7cj/0/M/glassfish%2004-M.png)](https://photos.adron.me/Software/Software-Development/IntelliJ-Explorations/i-h8Wf7cj/0/O/glassfish%2004.png)

*Click for full size image.*

So thus the Glassfish doesn’t understand where the default installation location is for the JRE. Thus you’ll likely have to help it out and provide it the path via the -j switch. Your path will likely look like this:

```bash
"C:\Users\you\Downloads\glassfish-4.0-windows.exe" -j "C:\Program Files\Java\jre7"
```

Once that was taken care of Glassfish 4.0 installed just fine and I was on my way to some sample app building. On to that sample app building shortly, for now let’s talk about configuration of IntelliJ IDEA 13 to work with Glassfish as an application server and the respective bits to get going.

## IntelliJ IDEA 13 Configuration

Once you have IntelliJ IDEA 13 open, create a new project.

[![Welcome Screen for IntelliJ IDEA 13. Click for full size image.](https://photos.adron.me/Software/Software-Development/IntelliJ-Explorations/i-rVPJZgs/0/M/octo-bear-04-M.png)](https://photos.adron.me/Software/Software-Development/IntelliJ-Explorations/i-rVPJZgs/0/O/octo-bear-04.png)

*Welcome Screen for IntelliJ IDEA 13. Click for full size image.*

Once you click that, pending you’ve already configured IntelliJ IDEA you’ll see a screen display as shown below. If you haven’t configured it already, I’ll go through how to configure things after project creation. That way one can double back and configure the applications you might have already started or pulled from git or something without Glassfish or other servers being setup.

[![Glassfish and other things, already setup, available for options during project creation. Click for full size image.](https://photos.adron.me/Software/Software-Development/IntelliJ-Explorations/i-JnPsF8k/0/M/octo-bear-05-M.png "Glassfish and other things, already setup, available for options during project creation. Click for full size image.")](https://photos.adron.me/Software/Software-Development/IntelliJ-Explorations/i-JnPsF8k/0/O/octo-bear-05.png)

*Glassfish and other things, already setup, available for options during project creation. Click for full size image.*

Note the JavaEE Web Module selection, then set a project name, project location (or leave the default, it’ll fill in when you enter the project name), set the Project SDK. If one isn’t available you’ll need to setup the SDK via the New button. This will bring up a dialog that will allow you to point to the SDK path and IntelliJ will know which version is available. You can do this for additional versions also, but for this example I’ve just installed 1.7 and run with it. Next set the Application server to Glassfish 4.0.0. Next click on Finish, then you’re all set.

When setting up Glassfish a few other options I like to set are shown in the dialog below. This is my default Glassfish setup for *Local* development. I’ve set the default browser to launch after a build to Chrome. Set the application server to GlassFish 4.0.0. It might seem silly to have this selection on the GlassFish Server dialog, but when there are multiple versions available you may need to setup a different version for different configurations. Next, I often run the server locally without security username and password, so be sure to remove the admin username that is there for the default configuration.

[![Glassfish Local setup. Click for full size image.](https://photos.adron.me/Software/Software-Development/IntelliJ-Explorations/i-DVFGwCj/0/M/octo-bear-02-M.png)](https://photos.adron.me/Software/Software-Development/IntelliJ-Explorations/i-DVFGwCj/0/O/octo-bear-02.png)

*Glassfish Local setup. Click for full size image.*

One last thing that I do to myself when setting up JSF, is keep forgetting to add the appropriate option to GlassFish to run JSF Workflow Apps. To run these apps open up the application server configuration for glassfish itself and select the JSF framework library.

[![Selecting JSF. Click for full size image.](https://photos.adron.me/Software/Software-Development/IntelliJ-Explorations/i-hHkQ6Tk/0/M/troubleshooting%2003-M.png)](https://photos.adron.me/Software/Software-Development/IntelliJ-Explorations/i-hHkQ6Tk/0/O/troubleshooting%2003.png)

*Selecting JSF. Click for full size image.*

Now with the application created there is a list of files & libraries.

[![To the left you can view a number of files & libraries listed. Click for full size image.](https://photos.adron.me/Software/Software-Development/IntelliJ-Explorations/i-T9FmfK2/0/M/octo-bear-06-M.png)](https://photos.adron.me/Software/Software-Development/IntelliJ-Explorations/i-T9FmfK2/0/O/octo-bear-06.png)

*To the left you can view a number of files & libraries listed. Click for full size image.*

Just to make sure everything is wired up right and the application is able to run, double click on the index.jsp file and add some HTML content. I’ve set up my file like this just to get started.

```html
<%-- Created by IntelliJ IDEA. --%>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<html>
<head>
    <title>Octo Bear!</title>
</head>
<body>
<h1>Bears!</h1>

<p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla at iaculis eros. Cras eget aliquam mi, ut suscipit
    arcu. Suspendisse accumsan auctor tellus in condimentum. Integer interdum a neque eget pharetra. Mauris nec dolor
    ipsum. Quisque quis fermentum lorem. Sed tempor egestas dui, sed bibendum justo vulputate eget. Pellentesque tempus
    auctor tellus id aliquam. Lorem ipsum dolor sit amet, consectetur adipiscing elit. In erat leo, pharetra eget
    convallis ut, interdum et eros. Morbi in tortor id tellus tristique aliquet at non urna. Pellentesque habitant morbi
    tristique senectus et netus et malesuada fames ac turpis egestas.</p>
</body>
</html>
```

Now click on the run button in the top right corner of IntelliJ. You might hit this error if you’ve just installed Glassfish and moved straight to creating the project.

![Running the new project immediately after installing Glassfish.](https://photos.adron.me/Software/Software-Development/IntelliJ-Explorations/i-T6bnKgv/0/O/troubleshooting%2001.png)

*Running the new project immediately after installing Glassfish.*

Open up a browser and navigate to <http://localhost:4848/> to bring up the administration page for Glassfish 4.0.

[![Glassfish 4.0 Administration site. (click for full size image)](https://photos.adron.me/Software/Software-Development/IntelliJ-Explorations/i-9XhdNPB/0/M/troubleshooting%2002-M.png)](https://photos.adron.me/Software/Software-Development/IntelliJ-Explorations/i-9XhdNPB/0/O/troubleshooting%2002.png)

*Glassfish 4.0 Administration site. (click for full size image)*

Click on the server (Admin server) section that’s pointed to in the image above. A page will display that has a button to stop the Glassfish server. Click on stop and that will enable IntelliJ to take over and run the server instead. You’ll want IntelliJ to do this as it will manage the restart, redeploy, update of classes and resources during coding & running the web application. This is much easier than attempting to attach or otherwise manage the server during development.

That’s just a few of the tips and tricks to getting started with the latest IntelliJ IDEA 13 EAP IDE for Java. In my next article I’m going to dive into a few of IntelliJ IDEA 13’s newest features for JSF Workflow Faces Applications.
