---
title: Vue.js Studies Day 6 – Beyond “Getting Started”
date: 2023-02-02 19:43:38 -0800
last_modified_at: 2023-02-02 19:43:38 -0800
permalink: /2023/02/02/vue-js-studies-day-6-beyond-getting-started/
slug: vue-js-studies-day-6-beyond-getting-started
wp_id: 65764
original_url: https://compositecode.blog/2023/02/02/vue-js-studies-day-6-beyond-getting-started/
categories:
- Javascript
- Vue.js
tags:
- javascript
- vue
- vuejs
excerpt: The previous post to this one, just included some definitions to ensure I’ve covered the core topics as I’m moving along. Before that I covered getting a project app started in day 3 and day 2 posts. Before that I covered the curriculum flow I’m covering in these studies. Now that I’ve covered a number …
image: /wp-content/uploads/2023/01/vuejs-dailies-header.png
---

The previous post to this one, just included [some definitions](/2023/01/13/day-4-studies-web-related-things/) to ensure I’ve covered the core topics as I’m moving along. Before that I covered getting a project app started in [day 3](/2023/01/12/vue-js-studies-day-3-more-ways-to-get-started/) and [day 2](/2023/01/04/vue-js-studies-day-2-getting-started-installed-creating-an-app/) posts. Before that I covered the [curriculum flow](/2023/01/03/vue-js-day-1-studies/) I’m covering in these studies.

Now that I’ve covered a number of ways to get started with a Vue project with; [JetBrains WebStorm](/2023/01/12/vue-js-studies-day-3-more-ways-to-get-started/), [hand crafted artisanal](/2023/01/04/vue-js-studies-day-2-getting-started-installed-creating-an-app/), or [via NPM](/2023/01/04/vue-js-studies-day-2-getting-started-installed-creating-an-app/) it’s time to start covering the basics of how to build an app using Vue.js. I’ll be using the WebStorm IDE for development but will still call out where or what I’d need to do if I were working from the terminal with something else. By using the WebStorm IDE, I’ll also be starting from the generated app that the IDE created for me.

## main.js

Starting in the `src` directory of the project, let’s cover a few of the key parts of this project of the application as created. First, we have a **main.js** file. In that file is the following code. This little bit of code is what is responsible for working with the Virtual DOM to mount the application to it for rendering the page we eventually see.

```
import { createApp } from 'vue'
import App from './App.vue'

import './assets/main.css'

createApp(App).mount('#app')
```

The first two lines import two variables from the ‘vue’ library called `createApp` and create an `App` object from ‘./App.vue’ template. Then the third import is just pulling in the `main.css` file. The fourth line uses the `createApp` operatig on the `App` object to `.mount` the application at the point of the `#app` anchor in the template App.vue. That leads to needing to take a look at App.vue to see what exactly the vue app is mounted to.

***NOTE**: I’m not 100% sure I’m describing this as precisely as I should, as the blog entry details, this is day 4 of Vue.js studies. I’d started in the past once or twice, and have done a ton of web dev over the years, but Vue.js is largely new to me. So if you see something worded incorrectly or oddly, please comment with questions or corrections.*

## App.vue

The App.vue file for the WebStorm generation seems to have a bit more from the other apps generated from other tooling. Whatever the case, let’s pick this apart and learn what is which and which is what in this file.

```
<script setup>
import HelloWorld from './components/HelloWorld.vue'
import TheWelcome from './components/TheWelcome.vue'
</script>

<template>
  <header>
    <img alt="Vue logo" class="logo" src="./assets/logo.svg" width="125" height="125" />

    <div class="wrapper">
      <HelloWorld msg="You did it!" />
    </div>
  </header>

  <main>
    <TheWelcome />
  </main>
</template>

<style scoped>
header {
  line-height: 1.5;
}

.logo {
  display: block;
  margin: 0 auto 2rem;
}

@media (min-width: 1024px) {
  header {
    display: flex;
    place-items: center;
    padding-right: calc(var(--section-gap) / 2);
  }

  .logo {
    margin: 0 2rem 0 0;
  }

  header .wrapper {
    display: flex;
    place-items: flex-start;
    flex-wrap: wrap;
  }
}
</style>
```

Right at the beginning of the App.vue file there is a `<script setup></script>` section that imports two other components that are located in the components directory that the App.vue file is located in. This is the HellowWorld.vue and TheWelcome.vue components. There is a third component, the WelcomeItem.vue component, in the component directory along with an icons directory.

With all of these assets now ready, clicking on the play or debug buttons in WebStorm will issue to the command to execute and display the app in the default browser. I’ll cover more of the assets as we get to each of them, for now I’m going to move along and get into some components and all.

[![](/wp-content/uploads/2023/01/CleanShot-2023-01-30-at-15.13.07.png)](/wp-content/uploads/2023/01/CleanShot-2023-01-30-at-15.13.07.png)

When the IDE (or you do manually) launches the browser to display the app it will look like this.

[![](/wp-content/uploads/2023/01/CleanShot-2023-01-30-at-15.20.11.png)](/wp-content/uploads/2023/01/CleanShot-2023-01-30-at-15.20.11.png)

## Checkpoint: Vue App Operational

This is a good time to checkpoint. If you’ve been following along and everything is as shown above, we’re good to move along to the next steps. If not, then something is amiss, probably broken, and that needs resolved first. If you’ve run into a problem at this point, leave a comment with a description of the issue and I’ll endeavor to help you resolve the problem. Otherwise, moving along to some edits and checking out Vue.js’s features and capabilities.

Once the next post is live, I’ll add the link here to that post… it’s coming soon!
