---
title: HTML5 Feature Support Detection
date: 2011-08-05 05:35:51 -0700
last_modified_at: 2011-08-08 15:58:14 -0700
permalink: /2011/08/05/html5-feature-support-detection/
slug: html5-feature-support-detection
wp_id: 3512
original_url: https://compositecode.blog/2011/08/05/html5-feature-support-detection/
categories:
- Unknown Code Ramblings
tags: []
excerpt: 'HTML5 is a collect of individual features, that currently are either supported or not by the current array of browsers. The best approach I’ve found at this time, is to write for HTML5 and use other tools to downgrade graceful. The following are some detection techniques that are in use today: Input Types: HTML5 defines …'
---

HTML5 is a collect of individual features, that currently are either supported or not by the current array of browsers. The best approach I’ve found at this time, is to write for HTML5 and use other tools to downgrade graceful.

The following are some detection techniques that are in use today:

Input Types: HTML5 defines over a dozen new input types for use in web forms. For determining which of these new form elements is supported use the following code, per element (yes I know, that’s a pain in the ass, but you gotta do what you gotta do)

```javascript
var input = document.createElement("input");
input.setAttribute("type", "color");
return i.type !== "text";
```

Aha, but if you don’t want to write these input checks, Modernizr has a hash it builds to detect all of the new input types.

```javascript
if (!Modernizr.inputtypes.date) {
	// ?? <- See example of this.
}
```

Video Formats: Video formats, or codecs, is the algorithm which is used to encode video. Checking if a video element object has the canPlayType for a particular codec will determine support.

```javascript
function supports_video() {
    return !!document.createElement('video').canPlayType;
}
```

Again Modernizr can make this detection much simpler.

```javascript
if (Modernizr.video) {
	if (Modernizr.video.ogg) {

	} else if (Modernizr.video.h264) {
		// H.264
	}
}
```

Canvas: The canvas element is a resolution independent bitmap canvas which can be used for rendering graphs, game graphics, or other visual images on the fly. To check for canvas attempt to create a canvas element on the document object and retrieve the context. Context dictates if there is or is not context support.

```javascript
function supports_canvas() {
	return !!document.createElement('canvas').getContext;
}
```

Of course, there is a Modernizr Function to determine support too.

```javascript
if (Modernizr.canvastext) {
	// let's draw some text!
} else {
	// no native canvas text support available
}
```

Geolocation: Geolocation is the function of determining where you are by using the UP address, wireless network connection, cell tower, GPS software, or other device. The Geolocation Working Group is actually working on this feature, not particularly the HTML5 Working Group, but the feature is closely correlated to the entire HTM5 spec and is currently being integrated into most browsers.

The code snippet below can be used to determine if geolocation is available.

```javascript
function supports_geolocation() {
	return !!navigator.geolocation;
}
```

If you don’t want to write this particular function, you could also use the Modernizer Library.

```javascript
if (Modernizr.geolocation) {
	// process the location...
} else {
	// no native geolocation support, so start hacking!
}
```
