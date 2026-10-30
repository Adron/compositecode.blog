---
title: 'Some JavaScript API Coding With Restify & Express & Hacking it With cURL    …Segment #1 (with some Webstorm to boot)'
date: 2013-12-01 06:30:34 -0800
last_modified_at: 2014-01-31 05:22:43 -0800
permalink: /2013/12/01/some-javascript-api-coding-with-restify-express-hacking-it-with-curl-segment-1/
slug: some-javascript-api-coding-with-restify-express-hacking-it-with-curl-segment-1
wp_id: 9250
original_url: https://compositecode.blog/2013/12/01/some-javascript-api-coding-with-restify-express-hacking-it-with-curl-segment-1/
categories:
- How-to
- Javascript
tags:
- api
- express
- http
- http verbs
- javascript
- js
- node
- node.js
- nodejs
- rest
- rest web services
- restful
- restify
- services
- verbs
excerpt: So often I end up putting together some RESTful services (or the intent is to at least build them with that premise, but we all know how that ends up). The API URIs routing gets put together and one wants to take a crack at the service as soon as possible. Here’s a quick guide …
image: /wp-content/uploads/2013/11/photodune-1763424-global-code-xxl.jpg
---

So often I end up putting together some RESTful services (or the intent is to at least build them with that premise, but we all know how that ends up). The API URIs routing gets put together and one wants to take a crack at the service as soon as possible. Here’s a quick guide for using cURL to take some basic actions against the services and understand what you’re getting back.

The first thing to do is make sure you can run JavaScript, which means you have a computer. The second thing is to get cURL, which means you’re running some variant of Linux or UNIX. In most scenarios one would be running OS-X. The easiest way to determine if it is installed on your computer just open up a terminal and type ‘curl –help’. You should get a result with all the switches, which is almost always a bit of overload.

```bash
$ curl --help
Usage: curl [options...]
Options: (H) means HTTP/HTTPS only, (F) means FTP only
     --anyauth       Pick "any" authentication method (H)
 -a, --append        Append to target file when uploading (F/SFTP)
     --basic         Use HTTP Basic Authentication (H)
     --cacert FILE   CA certificate to verify peer against (SSL)
     --capath DIR    CA directory to verify peer against (SSL)
 -E, --cert CERT[:PASSWD] Client certificate file and password (SSL)
     --cert-type TYPE Certificate file type (DER/PEM/ENG) (SSL)
     --ciphers LIST  SSL ciphers to use (SSL)
     --compressed    Request compressed response (using deflate or gzip)
 -K, --config FILE   Specify which config file to read
     --connect-timeout SECONDS  Maximum time allowed for connection
 -C, --continue-at OFFSET  Resumed transfer offset
 -b, --cookie STRING/FILE  String or file to read cookies from (H)
 -c, --cookie-jar FILE  Write cookies to this file after operation (H)
     --create-dirs   Create necessary local directory hierarchy
     --crlf          Convert LF to CRLF in upload
     --crlfile FILE  Get a CRL list in PEM format from the given file
 -d, --data DATA     HTTP POST data (H)
     --data-ascii DATA  HTTP POST ASCII data (H)
     --data-binary DATA  HTTP POST binary data (H)
     --data-urlencode DATA  HTTP POST data url encoded (H)
     --delegation STRING GSS-API delegation permission
     --digest        Use HTTP Digest Authentication (H)
     --disable-eprt  Inhibit using EPRT or LPRT (F)
     --disable-epsv  Inhibit using EPSV (F)
 -D, --dump-header FILE  Write the headers to this file
     --egd-file FILE  EGD socket path for random data (SSL)
     --engine ENGINE  Crypto engine (SSL). "--engine list" for list
 -f, --fail          Fail silently (no output at all) on HTTP errors (H)
 -F, --form CONTENT  Specify HTTP multipart POST data (H)
     --form-string STRING  Specify HTTP multipart POST data (H)
     --ftp-account DATA  Account data string (F)
     --ftp-alternative-to-user COMMAND  String to replace "USER [name]" (F)
     --ftp-create-dirs  Create the remote dirs if not present (F)
     --ftp-method [MULTICWD/NOCWD/SINGLECWD] Control CWD usage (F)
     --ftp-pasv      Use PASV/EPSV instead of PORT (F)
 -P, --ftp-port ADR  Use PORT with given address instead of PASV (F)
     --ftp-skip-pasv-ip Skip the IP address for PASV (F)
     --ftp-pret      Send PRET before PASV (for drftpd) (F)
     --ftp-ssl-ccc   Send CCC after authenticating (F)
     --ftp-ssl-ccc-mode ACTIVE/PASSIVE  Set CCC mode (F)
     --ftp-ssl-control Require SSL/TLS for ftp login, clear for transfer (F)
 -G, --get           Send the -d data with a HTTP GET (H)...
```

Don’t get intimidated! It goes on and on and on, but just know it’s installed if you see all these goodies. If you don’t get the results above, then installing cURL is the next step. I’ll leave that to you. Here’s some links to download and get started however.

- [cURL Download](http://curl.haxx.se/download.html)
- [How to install cURL with Homebrew](http://apple.stackexchange.com/questions/95855/how-to-install-curl-on-osx-with-brew)

Next you’ll of course need Node.js and Restify installed. I’ll assume you have Node.js installed. Create a directory and in that directory just run the following command.

```bash
npm install restify
```

Next create a file called server.js in that directory you’ve just installed restify in. Here’s the initial JavaScript code for that file that I’ve used to put together for the first few examples of using cURL.

```javascript
var restify = require('restify');

function respond(req, res, next) {
    res.send('hello ' + req.params.name);
}

var server = restify.createServer();
server.get('/hello/:name', respond);
server.head('/hello/:name', respond);

server.listen(8080, function() {
    console.log('%s listening at %s', server.name, server.url);
});
```

Ok, now to run this with node.js just issue the command to launch node.js with this file that was just created.

```bash
node server.js
restify listening at http://0.0.0.0:8080
```

## Getting Get

Now the service is running on port 8080 against 0.0.0.0. To check out what a standard GET verb will do in a browser, open up a browser and navigate to <http://0.0.0.0:8080>.

![Browsing the GET response via Chrome.](https://photos.adron.me/Software/Software-Development/Orchestrateio-Hacking/i-24DfVNH/0/O/0.0.0.0_8080.png)

*Browsing the GET response via Chrome.*

You’ll see this in the browser window. Just straight plain text too. If you look at source, this is all you get back. Now open up a terminal and run the following cURL command to execute a GET against the URI & port. This is the most basic cURL command one can make. It is simply issuing a GET request against the URI and will display the body of the response.

```bash
curl 0.0.0.0:8080
```

The response will be similar to this for the particular request.

```bash
{"code":"ResourceNotFound","message":"/ does not exist"}
```

Your terminal will probably stick the subsequent prompt at the end of the result too, because the result doesn’t end in a newline. Beware of that, your prompt hasn’t disappeared. 😉

To get a little more information you can get the header of the response dumped into the terminal with a -i. The -i option stands for –include, to include the header. Issue the command as either line shown below.

```bash
curl -i http://0.0.0.0:8080
curl --include http://0.0.0.0:8080
```

The response will be provide a little bit more about what is going on.

```bash
HTTP/1.1 404 Not Found
Content-Type: application/json
Content-Length: 56
Date: Wed, 27 Nov 2013 00:27:36 GMT
Connection: keep-alive

{"code":"ResourceNotFound","message":"/ does not exist"}
```

With this response the actual response error code number is shown. In this case we have a 404, which points us to the problem with this curl request. The server isn’t returning anything to our curl request. If we look at the code, we can see that the ‘get’ route is setup as ‘/hello/:name’ which means that the domain root is only looking at <http://url_root/hello/someName> for a request to be made in order to return a response.

```javascript
var server = restify.createServer();
server.get('/hello/:name', respond);
server.head('/hello/:name', respond);
```

Issue a command against the server now with the following curl request.

```bash
curl -i http://0.0.0.0:8080/hello/Adron
```

The response should come back as an actual response with content.

```bash
HTTP/1.1 200 OK
Content-Type: application/json
Content-Length: 13
Date: Wed, 27 Nov 2013 00:34:04 GMT
Connection: keep-alive

"hello Adron"
```

Here the content is returned as “hello Adron” and the header returns a 200. The content type is application/json format with the length returned as 13. Note also the connection is set to keep-alive. Let’s dive into that.

If we change the connection type, which is important for many scenarios, we have to send extra header information to ask for the response to be returned accordingly. In order to do that we can pass the -H or –header option in with the curl request. If the command is issued with an -i and -H as shown below the result will be as follows.

```
curl -iH "connection: close" http://0.0.0.0:8080/hello/Adron
HTTP/1.1 200 OK
Content-Type: application/json
Content-Length: 13
Date: Wed, 27 Nov 2013 00:41:07 GMT
Connection: close

"hello Adron"
```

If we take away the -i we’ll just get the response, which is “hello Adron” and wouldn’t get the header, which now returns Connection: close in the response. By default, curl sets the connection as keep-alive, but in order to make the request return right away the connection needs to be issued a request for it to close. By setting the -H or –header value of connection to close, we get the response immediately. With restify, it is also important to note that it checks if the user agent is curl.

If it is curl the connection header to close and removes the content-length header. However I’ve experienced that restify is not doing this in all circumstances or that the use of curl is being changed in some of my usage. So don’t always assume that this will be the case. The safest bet is to set the connection closed when done. Thus, adding -H or –header and setting connection to close with a “Connection: close”.

## Beyond Basic Get

Ok, so that’s a pretty solid use of GET with cURL. Let’s dive into some puts and deletes with a get or two thrown in for comparison. Change the executing code to the code shown in the server.js file below.

```javascript
var restify = require('restify');

function send(req, res, next) {
    res.send('hello ' + req.params.name);
    return next();
}

var server = restify.createServer();
server.post('/hello', function create(req, res, next) {
    res.send(201, Math.random().toString(36).substr(3, 8));
    return next();
});
server.put('/hello', send);
server.get('/hello/:name', send);
server.head('/hello/:name', send);
server.del('hello/:name', function rm(req, res, next) {
    res.send(204);
    return next();
});

server.listen(8080, function() {
    console.log('%s listening at %s', server.name, server.url);
});
```

The first section of code to check out is around the function send.

```javascript
function send(req, res, next) {
    res.send('hello ' + req.params.name);
    return next();
}
```

This function is setup to take req, res, and then handle next. The req is the request, the res is the response and the next is for issuing to return and continue with the result. The next bit of code starts the server with the restify.createServer();. Just below that there are several handlers that are setup.

```javascript
server.post('/hello', function create(req, res, next) {
    res.send(201, Math.random().toString(36).substr(3, 8));
    return next();
});
server.put('/hello', send);
server.get('/hello/:name', send);
server.head('/hello/:name', send);
server.del('hello/:name', function rm(req, res, next) {
    res.send(204);
    return next();
});
```

Now at this point I got a little sidetracked writing this blog entry. But I thought to myself, “hell, I’m just figuring out some parts of Webstorm, I ought to blog a little about it!” So, here’s…

## A Little Webstorm Love

[![Webstorm and cURL. Click the image for a full size image.](https://photos.adron.me/Software/Software-Development/Orchestrateio-Hacking/i-TcL4TTq/0/L/webstorm%20quickie-L.png)](https://photos.adron.me/Software/Software-Development/Orchestrateio-Hacking/i-TcL4TTq/0/O/webstorm%20quickie.png)

*Webstorm and cURL. Click the image for a full size image.*

Before continuing on I wanted to cover a few tidbits of the Jetbrains Webstorm IDE. I often switch back and forth between the Sublime/Terminal combo and the Webstorm IDE. The really cool thing about this IDE is that it actually has a Terminal built in, color coding and autocomplete of the code, refactoring, and file and folder viewer and a whole slew of other features. In the image above that I’ve included there are four neon pointers that are displaying some of the key functionality that I’m using to work through this blog entry with cURL and Restify.

The arrows, from left to right are pointing to the following IDE elements. The first is pointing to the javascript files storgie.js and starter.js which I added specifically to show the git status colors. Each color reflect if the file is new (green), has changes (light blue) or is committed with no changes (white). The second arrow is just pointing to the general folder structure. Here you can see the hidden .\* files like the .gitignore and .npmignore and also easy to dig through the node\_modules directory. Webstorm also uses the node\_modules directory to provide extra information and autocomplete to the code as you work through your coding session. The next arrow is pointing out the terminal in the editor, which is where I’m working up the curl examples in this blog entry. Then of course the color coded starter.js file that is one of the working examples. Webstorm, simply, is pretty sweet. I’m looking to do some more walk throughs and work sessions with the editor in the near future. So if interested, be sure to keep reading and subscribe, I’ll be sure to post any links to wherever the material ends up right here.

## Now, back to the cURLing. 😉

After I toyed around with Webstorm and bit to get it work in a way that was efficient for me to use it for developing these APIs I stumbled into an idea. I’d provide a page for the APIs that could be located at the root of the API service such as <http://api.blagh.com>. The APIs would still be a restful type schema like <http://api.blagh.com/thing/create> or <http://api.blagh.com/thing/destroy> but at the very root would be a kind of docs. Maybe this could just be a status page even. Whatever the case, there needs to be something at <http://api.blagh.com> so I decided right then and there I’d switch to express.js to build the rest of the API services. Restify is fine and all but for this, it seemed like express would have all of the pieces I need for this.

Just to boot, I then read a few articles about express being faster such as [this one](http://blog.perfectapi.com/2012/benchmarking-apis-using-perfectapi-vs-express.js-vs-restify.js/). But then I read this [issue on github](https://github.com/mcavage/node-restify/issues/176) and almost thought, “maybe I should keep using restify” but then I thought, “dammit, just get it done the way you want it built” so it was back to express. It’s easy enough to change this later so I just got back to coding, albeit with express now. So keep reading and in the next day or two I’ll have part two of this series on using cURL to hack at your APIs.

Enjoy the composite coding & cheers!

References:

- [Restify](http://mcavage.me/node-restify/)
- [Express](http://expressjs.com/)
- [Node.js](http://www.nodejs.org/)
