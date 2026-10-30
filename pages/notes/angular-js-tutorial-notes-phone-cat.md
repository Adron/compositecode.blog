---
layout: page
title: 'Angular.js Tutorial Notes :: phone-cat'
date: 2014-01-08 16:02:24 -0800
last_modified_at: 2014-01-12 13:43:35 -0800
permalink: /notes/angular-js-tutorial-notes-phone-cat/
slug: angular-js-tutorial-notes-phone-cat
wp_id: 9484
original_url: https://compositecode.blog/notes/angular-js-tutorial-notes-phone-cat/
---

Back to [Full Notes Listing](http://compositecode.com/write-up-series/notes/).

Getting started just add:

```html
<script type="text/javascript" src="blaghblagh/lib/angular/angular.js"></script>
```

Then ng-app that sucker like this:

```html
<html ng-app>
```

The ng-app attribute represents an Angular directive named ngApp.

Angular uses *name-with-dashes* for its custom attributes and camelCase for the corresponding directives that implements them). This is used for the html element so Angular knows this to be the root element of the application. This gives the ability to make the whole web page an Angular app or just a certain part of the page.

For more on the [ngApp (docs link)](http://docs.angularjs.org/api/ng.directive:ngApp) directive in module ng. For more information on [directives (docs link)](http://docs.angularjs.org/guide/directive).

Short summary of directives is they attach to a DOM element (attribute, element name or CSS class) and tell Angular’s HTML compiler to treat it as such. Some of the key built in directives include ngBind, ngModel and ngView. Directives can be created just like controllers and services.

DI – Yup, dependency injection part gazillion. A popular pattern indeed. For more [check out the docs](http://docs.angularjs.org/guide/di), a collection of information I gathered [6 years ago on DI](/2008/06/25/di-ioc-and-loose-coupling/) and there’s a [ton more out there](https://www.google.com/#q=dependency%20injection).

## Bootstrapping

Yo, don’t mistake bootstrapping via Angular for [bootstrapping with bootstrap](http://getbootstrap.com/).

The ngApp is used to do most bootstrapping, but sometimes manual bootstrapping needs to be done. Doing [manual bootstrapping](http://docs.angularjs.org/guide/bootstrap) has several options including things like deferred bootstrapping. Bootstrapping is used in context of DI in this sense, so read up on DI to get a better idea of what exactly bootstrapping is doing.

Steps of the bootstrap:

1. The injector that will be used for dependency injection is created.
2. The injector will then create the root scope that will be the context for the model of the application.
3. Angular will then build the DOM starting at the ngApp root element and process directives and bindings as reached.

Once things are bootstrapped Angular will wait for incoming browser events and look for anything that might change the model. Once such an event occurs it detects if it caused a change and upon finding a change will incur them through update of the bindings.

## Model-view-controller

This is in the same realm of DI for me, so I’m gonna skip notes on this. Been there, done that so many times. For more information about MVC however, check out this: [Model View Controller ie MVC](http://en.wikipedia.org/wiki/Model%E2%80%93View%E2%80%93Controller) and [the Angular.js Cookbook Tic-tac-toe Example](http://docs.angularjs.org/cookbook/mvc?board=,,%3B,,%3B,,%2FX) and [Step 2 of the Intro to Angular](http://docs.angularjs.org/tutorial/step_02).
