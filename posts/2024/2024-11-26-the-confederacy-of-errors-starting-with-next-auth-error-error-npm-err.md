---
title: The Confederacy of Errors Starting With Next Auth; Error, Error, npm ERR!
date: 2024-11-26 18:01:00 -0800
last_modified_at: 2024-11-24 10:27:22 -0800
permalink: /2024/11/26/the-confederacy-of-errors-starting-with-next-auth-error-error-npm-err/
slug: the-confederacy-of-errors-starting-with-next-auth-error-error-npm-err
wp_id: 70455
original_url: https://compositecode.blog/2024/11/26/the-confederacy-of-errors-starting-with-next-auth-error-error-npm-err/
categories:
- App Building
- Coding Adventures
- Coding Patterns & Practices
- Collectors' Tune Tracker
- Javascript
tags:
- coding
- database
- javascript
- programming
- react
- vercel
excerpt: The author faced a dependency conflict while developing an app using Next.js and React. They resolved issues by uninstalling and reinstalling packages, updating configuration files, and moving to JavaScript for Next.js config. After several attempts, the author successfully executed the app, gaining functionality to manage authentication and navigate to a dashboard.
image: /wp-content/uploads/2024/10/screamy-2.jpg
---

In the interim while I was getting to the next stage of this app, I ran into (*what was I doing?* 🤷🏼‍♂️) this error.

```
npm ERR! code ERESOLVE
npm ERR! ERESOLVE could not resolve
npm ERR!
npm ERR! While resolving: next-auth@4.24.10
npm ERR! Found: react@19.0.0-rc-66855b96-20241106
npm ERR! node_modules/react
npm ERR!   react@"19.0.0-rc-66855b96-20241106" from the root project
npm ERR!   peer react@"^18.2.0 || 19.0.0-rc-66855b96-20241106" from next@15.0.3
npm ERR!   node_modules/next
npm ERR!     next@"15.0.3" from the root project
npm ERR!     peer next@"^12.2.5 || ^13 || ^14 || ^15" from next-auth@4.24.10
npm ERR!     node_modules/next-auth
npm ERR!       next-auth@"^4.24.10" from the root project
npm ERR!   2 more (react-dom, styled-jsx)
npm ERR!
npm ERR! Could not resolve dependency:
npm ERR! peer react@"^17.0.2 || ^18" from next-auth@4.24.10
npm ERR! node_modules/next-auth
npm ERR!   next-auth@"^4.24.10" from the root project
npm ERR!
npm ERR! Conflicting peer dependency: react@18.3.1
npm ERR! node_modules/react
npm ERR!   peer react@"^17.0.2 || ^18" from next-auth@4.24.10
npm ERR!   node_modules/next-auth
npm ERR!     next-auth@"^4.24.10" from the root project
npm ERR!
npm ERR! Fix the upstream dependency conflict, or retry
npm ERR! this command with --force or --legacy-peer-deps
npm ERR! to accept an incorrect (and potentially broken) dependency resolution.
```

As with these dependency issue errors I was getting, which seems to be somewhat common with React these days (or maybe just most of web development!), I went about fixing it with the following steps.

First I removed the existing next-auth installation.

```
npm uninstall next-auth
```

Next I installed the beta version of next auth that supports Next.js 15 and React 19 (yes, I RTFMed (i.e. Read The Fucking Manual) a bit and read some other things to finally get to that conclusion).

```
npm install next-auth@5.0.0-beta.4
```

Just for good measure I did a cache clear too.

```
npm cache clean --force
rm -rf node_modules package-lock.json
```

Reinstalled the dependency.

```
npm install
npm install next-auth@5.0.0-beta.4
```

I fiddled around a bit more RTFMing and realized I need to also update my auth, middleware, and config. First up was the *./src/app/auth.ts* code to update. The complete file with the tweaks now looks like this.

```
import NextAuth from "next-auth";
import { authConfig } from "./auth.config";
import Credentials from "next-auth/providers/credentials";
import { PrismaClient } from '@prisma/client';
import { compare } from 'bcryptjs';

const prisma = new PrismaClient();

export const { auth, signIn, signOut } = NextAuth({
  ...authConfig,
  providers: [
    Credentials({
      async authorize(credentials) {
        const { username, password } = credentials as {
          username: string;
          password: string;
        };

        const user = await prisma.user.findUnique({
          where: { username }
        });

        if (!user) return null;

        const isPasswordValid = await compare(password, user.password);

        if (!isPasswordValid) return null;

        return {
          id: user.id,
          email: user.email,
          username: user.username,
        };
      }
    })
  ],
  callbacks: {
    async jwt({ token, user }) {
      if (user) {
        token.username = user.username;
      }
      return token;
    },
    async session({ session, token }) {
      if (token && session.user) {
        session.user.username = token.username as string;
      }
      return session;
    }
  }
});
```

Next up the *./src/app/auth.config.ts*.

```
import type { NextAuthConfig } from "next-auth";

export const authConfig = {
  pages: {
    signIn: "/login",
  },
  callbacks: {
    authorized({ auth, request: { nextUrl } }) {
      const isLoggedIn = !!auth?.user;
      const isOnDashboard = nextUrl.pathname.startsWith('/dashboard');

      if (isOnDashboard) {
        if (isLoggedIn) return true;
        return false; // Redirect unauthenticated users to login page
      } else if (isLoggedIn) {
        return true;
      }
      return true;
    },
  },
  providers: [],
} satisfies NextAuthConfig;
```

Finally the *./src/middleware.ts* code.

```
import NextAuth from "next-auth";
import { authConfig } from "./app/auth.config";

export default NextAuth(authConfig).auth;

export const config = {
  matcher: ['/((?!api|_next/static|_next/image|favicon.ico).*)'],
};
```

I ran all that, hoping that it resolved the dependency issues but no go. I ran things (kind of stupidly after making the code changes) and the dependencies threw this nonsense at me.

```
npm ERR! code ERESOLVE
npm ERR! ERESOLVE could not resolve
npm ERR!
npm ERR! While resolving: next-auth@4.24.10
npm ERR! Found: react@19.0.0-rc-66855b96-20241106
npm ERR! node_modules/react
npm ERR!   react@"19.0.0-rc-66855b96-20241106" from the root project
npm ERR!   peer react@"^18.2.0 || 19.0.0-rc-66855b96-20241106" from next@15.0.3
npm ERR!   node_modules/next
npm ERR!     next@"15.0.3" from the root project
npm ERR!     peer next@"^12.2.5 || ^13 || ^14 || ^15" from next-auth@4.24.10
npm ERR!     node_modules/next-auth
npm ERR!       next-auth@"^4.24.10" from the root project
npm ERR!   2 more (react-dom, styled-jsx)
npm ERR!
npm ERR! Could not resolve dependency:
npm ERR! peer react@"^17.0.2 || ^18" from next-auth@4.24.10
npm ERR! node_modules/next-auth
npm ERR!   next-auth@"^4.24.10" from the root project
npm ERR!
npm ERR! Conflicting peer dependency: react@18.3.1
npm ERR! node_modules/react
npm ERR!   peer react@"^17.0.2 || ^18" from next-auth@4.24.10
npm ERR!   node_modules/next-auth
npm ERR!     next-auth@"^4.24.10" from the root project
npm ERR!
npm ERR! Fix the upstream dependency conflict, or retry
npm ERR! this command with --force or --legacy-peer-deps
npm ERR! to accept an incorrect (and potentially broken) dependency resolution.
```

I went ahead and deleted node modules and the lock file.

```
rm -rf node_modules package-lock.json
```

Then went after a dependency dependent dependencies list in my package.json dependency listing for dependency clarity!

```
{
  "name": "adrons-core-platform",
  "version": "0.1.0",
  "private": true,
  "scripts": {
    "dev": "next dev",
    "build": "next build",
    "start": "next start",
    "lint": "next lint"
  },
  "dependencies": {
    "@prisma/client": "^5.7.0",
    "bcryptjs": "^2.4.3",
    "next": "14.0.3",
    "next-auth": "5.0.0-beta.4",
    "react": "^18.2.0",
    "react-dom": "^18.2.0"
  },
  "devDependencies": {
    "@types/bcryptjs": "^2.4.6",
    "@types/node": "^20.10.0",
    "@types/react": "^18.2.39",
    "@types/react-dom": "^18.2.17",
    "autoprefixer": "^10.4.16",
    "eslint": "^8.54.0",
    "eslint-config-next": "14.0.3",
    "postcss": "^8.4.31",
    "prisma": "^5.7.0",
    "tailwindcss": "^3.3.5",
    "typescript": "^5.3.2"
  }
}
```

Then after that a legacy peer deps install.

```
npm install --legacy-peer-deps
```

Since I think I deviated the Prisma version, just to make sure, I also generated that again too.

```
npx prisma generate
```

Then again, I ran the code and poof, of course I messed something up in the config file with all these steps. I got the following error.

```
/Users/adron/Codez/adrons-core-platform/node_modules/next/dist/server/config.js:778
            throw new Error(Configuring Next.js via '${(0, _path.basename)(nonJsPath)}' is not supported. Please replace the file with 'next.config.js' or 'next.config.mjs'.);
                  ^
Error: Configuring Next.js via 'next.config.ts' is not supported. Please replace the file with 'next.config.js' or 'next.config.mjs'.
    at loadConfig (/Users/adron/Codez/adrons-core-platform/node_modules/next/dist/server/config.js:778:19)
    at async nextDev (/Users/adron/Codez/adrons-core-platform/node_modules/next/dist/cli/next-dev.js:191:14)
    at async main (/Users/adron/Codez/adrons-core-platform/node_modules/next/dist/bin/next:150:5)
```

I’m about to throw something out the window at this point. A bit enraging really. But back to the troubleshooting. I went RTFMing and digging around and then, stumbling on the fact that Next.js doesn’t use TypeScript for its config file.

Really? All the other code is TypeScript but… oh whatever. Anyway.

```
mv next.config.ts next.config.js
```

The code is the same, cuz it was JavaScript, just had the \*.ts extension. At this point I ran another `npm run dev` and the clusterfuck continued.

[ *opening the window in preparation of throwing this thing out of it!!!* ]

I now have this error.

```
(node:80844) Warning: To load an ES module, set "type": "module" in the package.json or use the .mjs extension.
(Use node --trace-warnings ... to show where the warning was created)
/Users/adron/Codez/adrons-core-platform/next.config.js:1
import type { NextConfig } from "next";
^^^^^^
SyntaxError: Cannot use import statement outside a module
    at internalCompileFunction (node:internal/vm:77:18)
    at wrapSafe (node:internal/modules/cjs/loader:1288:20)
    at Module._compile (node:internal/modules/cjs/loader:1340:27)
    at Module._extensions..js (node:internal/modules/cjs/loader:1435:10)
    at Module.load (node:internal/modules/cjs/loader:1207:32)
    at Module._load (node:internal/modules/cjs/loader:1023:12)
    at cjsLoader (node:internal/modules/esm/translators:345:17)
    at ModuleWrap.<anonymous> (node:internal/modules/esm/translators:294:7)
    at ModuleJob.run (node:internal/modules/esm/module_job:218:25)
    at async ModuleLoader.import (node:internal/modules/esm/loader:329:24)
```

So back to digging up a solution. More searching and RTFMing and I get to the next step of this circling the drain mess. Looks like maybe my next.config.js file should have code that shapes up like this.

```
/** @type {import('next').NextConfig} */
const nextConfig = {
  reactStrictMode: true,
  swcMinify: true,
};

module.exports = nextConfig;
```

Fortunately for you dear ready, I’m into hour “goodness only knows” but if you’re following along, hopefully I’ve dead ended some of these for you. Because finally, at this point, with that confederacy of errors, I’ve finally got a successful execution with `npm run dev` and can login and see the dashboard!

Stay tuned, subscribe, and on the next post I’ll get into getting a logoff option on the menu bar and add some other features to this site on the way to making it truly useful. In the meantime, may you code build better than the code in this post! Cheers!

## Quick Links to Related Posts & Series Posts

**OG Posts on [adron.tools](https://adron.tools) and [Collector’s Tune Tracker](https://adron.github.io/collectorstunetracker/)**

The trio of initial posts that kicked off this entire effort. Things have changed tremendously from these original posts, but they provide much of the root reasoning around getting this series and these apps built!

- [Building a Multi-Tenant Music Collector’s Database](/2023/10/23/building-a-multi-tenant-music-collectors-database/)
- [Starting a New Project – Let’s Choose the Tech](/2024/02/15/starting-a-new-project-lets-choose-a-tech-stack/)
- [Software Development: Getting Started by Getting Organized](/2024/05/02/software-development-getting-started-by-getting-organized/).

**Previous Posts**

- [Building “Adron’s Core Platform”: Starting a React App on Vercel](/2024/11/19/building-adrons-core-platform-starting-a-react-app-on-vercel/)
- [Getting a Vercel PostgreSQL Database and Basic Authentication Operational](/2024/11/26/getting-a-vercel-postgresql-database-and-basic-authentication-operational/)

**Subsequent Posts**

- Coming real soon… the next stages.
