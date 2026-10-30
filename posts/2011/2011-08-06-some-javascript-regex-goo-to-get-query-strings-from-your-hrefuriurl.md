---
title: Some JavaScript + REGEX goo to get query strings from your HREF/URI/URL
date: 2011-08-06 01:22:16 -0700
last_modified_at: 2011-08-05 10:25:09 -0700
permalink: /2011/08/06/some-javascript-regex-goo-to-get-query-strings-from-your-hrefuriurl/
slug: some-javascript-regex-goo-to-get-query-strings-from-your-hrefuriurl
wp_id: 3520
original_url: https://compositecode.blog/2011/08/06/some-javascript-regex-goo-to-get-query-strings-from-your-hrefuriurl/
categories:
- How-to
- Javascript
- Unknown Code Ramblings
tags:
- href
- javascript
- query string
- querystring
- regex
- uri
- url
excerpt: I guess there is a library somewhere to do this, but I couldn’t find it fast enough so I spit this contraption out. It’s a function that grabs the value from a URI/URL query string. Yes, writing those nasty REGEXs about drove me nuts! 😉 Maybe I can save at least one soul out there some trouble. If you see an enhancement option or have ideas, please comment and let me know! function GiveMeTheQueryStringParameterValue(name) { name = name.replace(/[\[]/, “\\\[“).replace(/[\]]/, “\\\]”); var regex = new RegExp(“[\\?&]” + name + “=([^&#]*)”); var results = regex.exec(window.location.href); if (results == null) return “”; else return decodeURIComponent(results[1].replace(/\+/g, ” “)); }
---

I guess there is a library somewhere to do this, but I couldn’t find it fast enough so I spit this contraption out. It’s a function that grabs the value from a URI/URL query string. Yes, writing those nasty REGEXs about drove me nuts! 😉 Maybe I can save at least one soul out there some trouble. If you see an enhancement option or have ideas, please comment and let me know!

```javascript
function GiveMeTheQueryStringParameterValue(parameterName) {
    parameterName = parameterName.replace(/[\[]/, "\\\[").replace(/[\]]/, "\\\]");
    var regex = new RegExp("[\\?&]" + parameterName + "=([^&#]*)");
    var results = regex.exec(window.location.href);
    if (results == null)
        return "";
    else
        return decodeURIComponent(results[1].replace(/\+/g, " "));
}
```
