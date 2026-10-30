---
title: jQuery DOM Elements…
date: 2010-07-08 09:08:00 -0700
last_modified_at: 2010-07-08 09:46:12 -0700
permalink: /2010/07/08/jquery-dom-elements/
slug: jquery-dom-elements
wp_id: 166
original_url: https://compositecode.blog/2010/07/08/jquery-dom-elements/
categories:
- How-to
tags:
- javascript
- jquery
excerpt: Here’s the second dose of jQuery bits, with more to come in the near future. I’ve got a few primary things I am going to point out with today’s code. With jQuery getting a particular element, type of element, or the whole lot of a particular element is very easy. Single line of code easy.
---

Here’s the second dose of jQuery bits, with more to come in the near future.  I’ve got a few primary things I am going to point out with today’s code.  With jQuery getting a particular element, type of element, or the whole lot of a particular element is very easy.  Single line of code easy.

```html
    <p>
        This is a sample page to show some basic jQuery operations with the DOM.
    </p>
    <p>
        The unordered list below has two list items within. When the jQuery below executes
        however the number of list items is higher because the master page includes some
        list items also.
    </p>
    <ul>
        <li><a href="http://compositecode.com">Loosely Coupled Human Code Factory Blog</a>
        <li><a href="https://partner.microsoft.com/">Microsoft Partner Network</a>
    </li></ul>
    <p>
        First set of input controls in nested between the form elements.</p>
    <form>
    <input type="checkbox" name="" />
    <input type="radio" name="" />
    <input name="" />
    <input type="button" name="" />
    </form>
    <p>
        Second set of input controls in nested between the form elements.</p>
    <form>
    <input type="checkbox" name="" />
    <input type="radio" name="" />
    <input name="" />
    <input type="button" name="" />
    </form>
    <p>
        Third set of input controls that are within the body elements but not surrounded
        by anything else.</p>
    <input type="checkbox" name="" />
    <input type="radio" name="" />
    <input name="" />
    <input type="button" name="" />
    <p>
        This last snippet of HTML I setup to show how the filter method works.</p>
    <a class="lookingFor" href="#">link</a>
    <a class="lookingFor" href="#">link</a>
    <a href="#">
        link</a>
    <a class="lookingFor" href="#">link</a> <a class="lookingFor" href="#">link</a>
    <a href="#">_</a>
    <a href="#">link</a>
    <a href="#">link</a>
    <a href="#">link</a>

    <script type="text/javascript">

        var alertMessages;

        // alerts there are X elements of type <a> and X elements of type <li>.
        alertMessages = 'Page contains ' + jQuery('a').length + ' <a> elements and ' + jQuery('li').length + ' <li> elements.';

        // searches within all form elements using a wrapper for context.
        alertMessages += '\nselected ' + jQuery('input', $('form')).length + ' inputs';

        // searches the first form element using DOM reference as the context.
        alertMessages += '\nselected ' + jQuery('input', document.forms[0]).length + ' inputs';

        // search within the body element for all input elements using an expression.
        alertMessages += '\nselected ' + jQuery('input', 'body').length + ' inputs';

        // This finds the 4 links marked with the class lookingFor out of all the <a> elements in the page.
        alertMessages += '\n' + jQuery('a').filter('.lookingFor').length + ' lookingFor links'

        // This finds the 4 links marked with the class lookingFor out of all the <a> elements in the page,
        // however it does so with a function instead.
        alertMessages += '\n' + jQuery('a').filter(function (index) { return $(this).hasClass('lookingFor'); }).length + ' lookingFor links';

        alert(alertMessages);
    </script>
```

The first line that is parsed together for the alertMessages variable shows a simple usage of the jQuery Selector Engine.  The jQuery uses the Sizzle (<http://www.sizzlejs.com>) Engine for this.  There are other options for selector style functionality, but this is the famous jQuery way.

The second, third, and fourth lines assigning to alertMessages are a simple usage of the jQuery Selector to retrieve elements within a particular context.  Review the comments in the code above for the specifics of what is being selected.

The fifth line are selecting elements with a particular class property.  In this case I’ve called the class lookingFor.  The jQuery call is using a filter function to trace the DOM and find the particular elements by the criteria.

The sixth line applies another filter method using a function.  This is kind of like using a in line delegate in C#.  As with C#, use with caution as you’ll end up with snippets of code copied and pasted everwhere if you use the in line function ability too much.

[![Shout it](http://dotnetshoutout.com/image.axd?url=http%3A%2F%2Fcompositecode.com%2F2010%2F07%2F08%2Fjquery-dom-elements%2F)](http://dotnetshoutout.com/jQuery-DOM-Elements%E2%80%A6) [![kick it on DotNetKicks.com](http://www.dotnetkicks.com/Services/Images/KickItImageGenerator.ashx?url=http%3a%2f%2fcompositecode.com%2f2010%2f07%2f08%2fjquery-dom-elements%2f&bgcolor=3333FF&cfgcolor=CC3300)](http://www.dotnetkicks.com/kick/?url=http%3a%2f%2fcompositecode.com%2f2010%2f07%2f08%2fjquery-dom-elements%2f)
