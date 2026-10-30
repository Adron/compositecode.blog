---
title: 'Getting Github : JavaScript Libraries Spilled EVERYWHERE! Series #003'
date: 2013-03-17 19:27:21 -0700
last_modified_at: 2013-03-26 17:44:33 -0700
permalink: /2013/03/17/getting-github-javascript-libraries-spilled-everywhere-series-003/
slug: getting-github-javascript-libraries-spilled-everywhere-series-003
wp_id: 7833
original_url: https://compositecode.blog/2013/03/17/getting-github-javascript-libraries-spilled-everywhere-series-003/
categories:
- How-to
- Javascript
- Node.js Things
tags:
- api
- gh3
- github
- github api
- javascript
- javascript library
- library
- node
- node.js
- nodejs
excerpt: 'This is an ongoing effort putting together some JavaScript app code on client and on server that started with blog entry series #001 and #002. This how-to is going to kind of go all over the place. My goal is to get github data. The question however is, how and with what. I knew there …'
---

This is an ongoing effort putting together some JavaScript app code on client and on server that started with blog entry series [#001](/2012/10/14/js-libs-everywhere-001/) and [#002](/2012/10/20/javascript-libraries-spilled-everywhere-series-002/).

![](/images/adronhall.smugmug.com/Software/Misc-Images/Bad-Resume/i-s2d7HmT/0/S/javascript-S.png)This how-to is going to kind of go all over the place. My goal is to get github data. The question however is, how and with what. I knew there were some available libraries, so writing straight and pulling straight off of the API myself seemed like it would be unnecessary work.

The github API documentation is located at <http://developer.github.com/v3/> with the list of client libraries for ease of access listed at <http://developer.github.com/v3/libraries/>. The first two that I forked and cloned were the [gh3](https://github.com/k33g/gh3) and npm installed the [octonode](https://github.com/ajaxorg/node-github) and [node-github](https://github.com/ajaxorg/node-github) libraries.

## Node.js Based Github Libraries

The two node based projects install via npm, as things go with node and were super easy. The first one I gave a test drive to is the <https://github.com/ajaxorg/node-github> project. I forked it and dove right in.

```bash
$ npm install github
npm http GET https://registry.npmjs.org/github
npm http 200 https://registry.npmjs.org/github
npm http GET https://registry.npmjs.org/github/-/github-0.1.8.tgz
npm http 200 https://registry.npmjs.org/github/-/github-0.1.8.tgz
$
```

After that quick install I took a stab at the test code they have in the README.md.

```javascript
var GitHubApi = require("github");

var github = new GitHubApi({
    // required
    version: "3.0.0",
    // optional
    timeout: 5000
});
github.user.getFollowingFromUser({
    user: "adron"
}, function(err, res) {
    console.log(JSON.stringify(res));
});
```

This worked all well and good, so I moved on to some other examples. The following example however needed authentication. To authenticate you’ll need to add the little snippet below with the username and password. However there’s also a Oauth token method you can use too, which I’ve not documented below. To check out other auth methods check out the [documentation](http://ajaxorg.github.com/node-github/#Client.prototype.authenticate).

```javascript
var GitHubApi = require("github");

var github = new GitHubApi({
    version: "3.0.0", timeout: 5000,
});

github.authenticate({
    type: "basic",
    username: "adron",
    password: "yoTurkiesGetYourOwn"
});

github.orgs.get({
	org: "Basho"
}, function(err, res){
	console.log(res);
});
```

The result is prefect for putting together a good display page or something of the organizations.

```bash
$ node adron_test.js
{ login: 'basho',
  id: 176293,
  url: 'https://api.github.com/orgs/basho&#8217;,
  repos_url: 'https://api.github.com/orgs/basho/repos&#8217;,
  events_url: 'https://api.github.com/orgs/basho/events&#8217;,
  members_url: 'https://api.github.com/orgs/basho/members{/member}',
  public_members_url: 'https://api.github.com/orgs/basho/public_members{/member}',
  avatar_url: 'https://secure.gravatar.com/avatar/ce5141b78d2fe237e8bfba49d6aff405?d=https://a248.e.akamai.net/assets.github.com%2Fimages%2Fgravatars%2Fgravatar-org-420.png&#8217;,
  name: 'Basho Technologies',
  company: Basho,
  blog: 'http://basho.com/blog/&#8217;,
  location: 'Cambridge, MA',
  email: null,
  public_repos: 105,
  public_gists: 0,
  followers: 0,
  following: 0,
  html_url: 'https://github.com/basho&#8217;,
  created_at: '2010-01-04T19:05:19Z',
  updated_at: '2013-03-17T20:29:09Z',
  type: 'Organization',
  total_private_repos: YYY,
  owned_private_repos: XXX,
  private_gists: 0,
  disk_usage: 788016,
  collaborators: 0,
  billing_email: 'not_a_valid_address@basho.com',
  plan: { name: 'platinum', space: 62914560, private_repos: billions },
  meta: { 'x-ratelimit-limit': '5000', 'x-ratelimit-remaining': 'azillion' }
}
```

Now at this point there’s a few significant problems. Setting up tests of the integration variety for this library gets real tricky because you need to authenticate, or at least I do for the data that I want. This doesn’t bode well for sending any integration tests or otherwise to Travis-CI or otherwise. So even though this library works, and would be processed on the server-side and not on the client side, having it as a non-tested part of the code base bothers me a bit. What’s a good way to setup tests to verify that things are working? I’ll get that figured out shortly and it’ll have to be another blog entry, maybe. For now though, let’s jump into the client side library and see how it functions.

## Client Side JavaScript Github

For the client side I started testing around with the [gh3 library](https://github.com/k33g/gh3). It has two dependencies, jQuery and Underscore.js. jQuery is likely always going to be in your projects. Underscore.js is also pretty common, but sometimes you’ll find you’ll need to go [download the library](https://github.com/documentcloud/underscore). Upon download and getting the additional libraries I needed installed, I gave the default sample a shot.

```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>gh3 Sample</title>
</head>
<body>
    <ul id="user"></ul>
</body>
<script src="js/jquery-1.7.1.min.js"></script>
<script src="js/underscore-min.js"></script>
<script src="js/gh3.js"></script>
<script>
	var adron = new Gh3.User("adron")
	,	userInfos = $("#user");

	adron.fetch(function (err, resUser){
		if(err) {
			throw "outch ..."
		}
		console.log(adron, resUser);
		_.each(_.keys(resUser), function (prop) {
			userInfos.append(
				$('<li>').append(prop+" : "+resUser[prop])
			);
		});
	});
</script>
</html>
```

This worked pretty seamlessly. Also it got me thinking, “what do I really want to do with the github library?” If it’s a server side service, obviously I’d want to use the Node.js libraries probably. However if it is client side data I want, is it even ideal that the server side actually pull the data anyway? The other issues around cross site scripting and related matters come into play too if it is a client side script, but this might be, even in spite of that, just what I needed. For now, that left me with some solid things to think about. But I was done for now… so until next entry, cheers!
