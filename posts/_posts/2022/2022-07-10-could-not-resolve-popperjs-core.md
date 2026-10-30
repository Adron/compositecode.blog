---
title: Could not resolve “@popperjs/core”
date: 2022-07-10 01:52:50 -0700
last_modified_at: 2022-07-10 01:52:50 -0700
permalink: /2022/07/10/could-not-resolve-popperjs-core/
slug: could-not-resolve-popperjs-core
wp_id: 65460
original_url: https://compositecode.blog/2022/07/10/could-not-resolve-popperjs-core/
categories:
- Javascript
- Node.js Things
- nodejs
tags:
- javascript
- node.js
- nodejs
- npm
- popperjs
- popperjs/core
image: /wp-content/uploads/2022/07/error.png
---

I keep getting this error on running dev. Albeit it doesn’t appear I’m getting it in production.

I run.

```shell
npm run dev
```

Then everything appears to be ok, with the standard message like this from vite.

```shell
  vite v2.9.9 dev server running at:

  > Local: http://localhost:3000/
  > Network: use `--host` to expose

  ready in 740ms.
```

But then, once I navigate to the site to check things out.

```shell
X [ERROR] Could not resolve "@popperjs/core"

    node_modules/bootstrap/dist/js/bootstrap.esm.js:6:24:
      6 │ import * as Popper from '@popperjs/core';
        ╵                         ~~~~~~~~~~~~~~~~

  You can mark the path "@popperjs/core" as external to exclude it from the bundle, which will
  remove this error.
```

…and this error annoyingly crops up.

```shell
11:36:23 PM [vite] error while updating dependencies:
Error: Build failed with 1 error:
node_modules/bootstrap/dist/js/bootstrap.esm.js:6:24: ERROR: Could not resolve "@popperjs/core"
    at failureErrorWithLog (C:\Users\Adron Hall\Codez\estuary\node_modules\esbuild\lib\main.js:1603:15)
    at C:\Users\Adron Hall\Codez\estuary\node_modules\esbuild\lib\main.js:1249:28
    at runOnEndCallbacks (C:\Users\Adron Hall\Codez\estuary\node_modules\esbuild\lib\main.js:1034:63)
    at buildResponseToResult (C:\Users\Adron Hall\Codez\estuary\node_modules\esbuild\lib\main.js:1247:7)
    at C:\Users\Adron Hall\Codez\estuary\node_modules\esbuild\lib\main.js:1356:14
    at C:\Users\Adron Hall\Codez\estuary\node_modules\esbuild\lib\main.js:666:9
    at handleIncomingPacket (C:\Users\Adron Hall\Codez\estuary\node_modules\esbuild\lib\main.js:763:9)
    at Socket.readFromStdout (C:\Users\Adron Hall\Codez\estuary\node_modules\esbuild\lib\main.js:632:7)
    at Socket.emit (events.js:315:20)
    at addChunk (_stream_readable.js:309:12)
Vite Error, /node_modules/.vite/deps/pinia.js?v=72977742 optimized info should be defined
Vite Error, /node_modules/.vite/deps/bootstrap.js?v=14c3224a optimized info should be defined
Vite Error, /node_modules/.vite/deps/pinia.js?v=72977742 optimized info should be defined
Vite Error, /node_modules/.vite/deps/pinia.js?v=72977742 optimized info should be defined (x2)

...
```

…and on and on and on goes these errors. For whatever reason, even though `npm install` has been run once just get to the point of running `npm run dev`, there needs to be a subsequent, specifically executed `npm install @popperjs/core` to install this particular dependency that throws this error.

So that’s it, that’s your fix. Cheers!
