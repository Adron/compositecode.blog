---
title: 'Building “Adron’s Core Platform”: Starting a React App on Vercel'
date: 2024-11-26 08:02:00 -0800
last_modified_at: 2024-11-26 13:25:27 -0800
permalink: /2024/11/26/building-adrons-core-platform-starting-a-react-app-on-vercel/
slug: building-adrons-core-platform-starting-a-react-app-on-vercel
wp_id: 70312
original_url: https://compositecode.blog/2024/11/26/building-adrons-core-platform-starting-a-react-app-on-vercel/
categories:
- App Building
- Coding Adventures
- Coding Patterns & Practices
- Collectors' Tune Tracker
tags:
- coding
- database
- javascript
- programming
- react
- vercel
excerpt: adron shares updates on their Collector’s Tune Tracker project, focusing on learning React and Vercel. They outline prerequisites, project setup, and initial code implementation. After establishing a Next.js application and making necessary corrections, they successfully deploy it on Vercel. Future posts will address database integration.
image: /wp-content/uploads/2024/11/IMG_8667.jpeg
---

*Quick links to all posts in the series and related at end of this post.*

There have been a number of changes in my Collector’s Tune Tracker endeavor since I wrote up the first posts for the effort with: [Building a Multi-Tenant Music Collector’s Database](/2023/10/23/building-a-multi-tenant-music-collectors-database/), [Starting a New Project – Let’s Choose the Tech](/2024/02/15/starting-a-new-project-lets-choose-a-tech-stack/), and [Software Development: Getting Started by Getting Organized](/2024/05/02/software-development-getting-started-by-getting-organized/). This is a continuation of that effort. I’ll go into the differences in a later post about those first posts and how I got to this point here today. But for this post specifically, and the next few, I’ll be focusing on getting a project started with [React](https://react.dev/) and [Vercel](https://vercel.com/).

I’ll write these following an approach that is based in the following:

- Suffice to say, I’m a bit rusty with my React.
- I’m completely unfamiliar with Vercel. In these posts that’s about to change however.

There are also a few prerequisites. I’m working through this on an M1 Mac, using iTerm, and largely Visual Studio Code. That and a whole lot of documentation. The following are some other prerequisites that would help if you want to follow along with what I’m going to build.

### Prerequisites

- Brew – <https://brew.sh/>
- Git – <https://git-scm.com/downloads/mac>
- Node.js via nvm – <https://github.com/nvm-sh/nvm> – check out my post [here](/2018/07/16/setting-up-a-dev-machine-for-node-js/) or this [old video](https://youtu.be/pLJanpjIrM0).
- [Github Account](https://github.com) – I’m [@Adron](https://github.com/adron) on Github.
  - [Github’s command line tool](https://cli.github.com/) `brew install gh`
- [Vercel Account](https://vercel.com) – Similarly you’ll need a Vercel account.
  - [Vercel’s command line tool](https://vercel.com/docs/cli) `npm install -g vercel`

## Rolling Into Things

Right off, let’s get the project started with the ole `npx`. The steps I went through involve the following – I just added comments inline to describe what I did or what setting options I went with for prompts.

```
# Create a new directory and navigate into it
mkdir adrons-core-platform
cd adrons-core-platform

# Initialize a new Next.js project
npx create-next-app@latest . --typescript --tailwind --eslint

# During setup, answer the following prompts:
# Would you like to use TypeScript? » Yes
# All other options I left default.

# Initialize git repository
git init
git add .
git commit -m "Initial commit: Next.js boilerplate setup for Adron."

# Create GitHub repository and push code
gh repo create adrons-core-platform --public --source=. --remote=origin
git push -u origin main
```

Next up I opened up the main page in Visual Studio Code and replaced what was there with the following code and markup.

```
export default function Home() {
  return (
    <main className="flex min-h-screen flex-col items-center justify-center p-24">
      <h1 className="text-4xl font-bold mb-4">
        Hello World!
      </h1>
      <p className="text-xl">
        Welcome to Adron's Core Platform
      </p>
    </main>
  );
}
```

NOTE: This is the first step, and already there’s an ESLint issue, do you see it? Don’t worry, I’ll show the correct and fix below.

At this point, I made sure I was logged into vercel with `vercel login`. Next I followed that with the simple deployment command of `vercel`. Since this is the first deploy I got prompted with a bunch of questions.

1. Setup and deploy? >> yes
2. Which scope? >> Select your Vercel account.
3. Link to existing project? >> no
4. What’s your project’s name? >> adrons-core-platform
5. In which directory is the code located? >> `./`
6. Want to modify these settings? >> no

The deployment will then initiate and provide deployment URLs, detect that this is a Next.js project, build the application, then finally deploy it to Vercel’s infrastructure.

To make future deployments easier, the configuration will be saved in a .vercel directory, which should be added to your .gitignore file. In addition to this, at this point in any project creation I always go ahead and add another entry too: `.vercel` and `.DS_Store`.

This time however, when I went to go add these two values I noticed that the generation of the app already added these to the .gitignore file. That makes for one less step at startup, I made a mental note at this point and moved on.

At this point I also added the repository to this project in Vercel. To do this, follow these steps:

1. Go to <https://vercel.com/dashboard>
2. Click “Add New Project”
3. Select the Github repository. In this case it would be `adrons-core-platform`.
4. Click on “Import”
5. For now I kept all the settings default and clicked on “Deploy” just to initiate another deploy.

For example, let’s say I made another change or two. Now when I issue the following:

```
git add .
git commit -m "Update homepage content"
git push origin main
```

I’ll get a deploy from the commit. To verify the deploy, you can follow one of these paths:

1. Check the Vercel dashboard for deployment status.
2. Visit the project URL, which in this case would be `https://adrons-core-platform.vercel.app`.
3. Check deployment log with `vercel logs`.

While I did this locally I didn’t run a build, thus ESLint didn’t run. But it launched the site locally and I could view it at localhost:3000. That’s all great, but because I setup the push to kick off a deployment on Vercel, the instructions on the deployment server starts an `npm run build` which does run ESLint and triggers this warning. I asked about, and you may have already noticed what would happen.

```
Failed to compile.
18:26:28.505
18:26:28.505
./src/app/page.tsx
18:26:28.505
8:25 Error: ' can be escaped with &apos;, &lsquo;, &#39;, &rsquo;. react/no-unescaped-entities
```

I knew quickly what happened here. I have my name showing ownership of the site in the welcome message `"Welcome to Adron's Core Platform"`. Well, the `'` isn’t escaped, which is done to maintain the integrity of displayed text vs. markup in page, and for other reasons. In this case the fix was real easy. I just changed the welcome message to include the escape sequence in the string like this `Welcome to Adron&apos;s Core Platform`.

However that said, if you’d prefer to have dirty ole `'` in your strings, then you can turn off the ESLint rule using an entry in the .eslintrc.json file like this.

```
  "rules": {
    "react/no-unescaped-entities": "off"
  }
```

I recommitted that and did a push.

```
git add .
git commit -m "Fix: escaped apostrophe in text"
git push origin main
vercel
```

Now I’ve got a site that works with zero errors in the build.

This was the first step, just getting an initial site put together, sketelon code, a basic welcome message, and getting the build and deployment pipeline setup with Vercel. In the next post I’ll continue forward and get a [Vercel Database](https://vercel.com/docs/storage/vercel-postgres) (i.e. [Neon Database](https://neon.tech)) setup and deployed with an initial schema. Stay tuned, subscribe, and I’ll catch you next post.

## Quick Links to Related Posts & Series Posts

**OG Posts on [adron.tools](https://adron.tools) and [Collector’s Tune Tracker](https://adron.github.io/collectorstunetracker/)**

The trio of initial posts that kicked off this entire effort. Things have changed tremendously from these original posts, but they provide much of the root reasoning around getting this series and these apps built!

- [Building a Multi-Tenant Music Collector’s Database](/2023/10/23/building-a-multi-tenant-music-collectors-database/)
- [Starting a New Project – Let’s Choose the Tech](/2024/02/15/starting-a-new-project-lets-choose-a-tech-stack/)
- [Software Development: Getting Started by Getting Organized](/2024/05/02/software-development-getting-started-by-getting-organized/).

**Subsequent Posts**

- Publishing [Getting a Vercel PostgreSQL Database and Basic Authentication Operational](/2024/11/26/getting-a-vercel-postgresql-database-and-basic-authentication-operational/) ~3ish hours after this post.
