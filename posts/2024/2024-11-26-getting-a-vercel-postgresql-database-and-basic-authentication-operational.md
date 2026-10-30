---
title: Getting a Vercel PostgreSQL Database and Basic Authentication Operational
date: 2024-11-26 11:08:00 -0800
last_modified_at: 2024-11-26 13:30:10 -0800
permalink: /2024/11/26/getting-a-vercel-postgresql-database-and-basic-authentication-operational/
slug: getting-a-vercel-postgresql-database-and-basic-authentication-operational
wp_id: 70311
original_url: https://compositecode.blog/2024/11/26/getting-a-vercel-postgresql-database-and-basic-authentication-operational/
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
excerpt: The post outlines the step-by-step process of setting up a React application using Next.js and PostgreSQL on Vercel, including database configuration, authentication with Prisma, and troubleshooting dependency errors. It highlights the importance of environment variables and concludes by stressing the need for correct configuration to ensure proper app functionality and user access.
image: /wp-content/uploads/2024/11/IMG_8668.jpeg
---

*Quick links to all posts in the series and related at end of this post.*

In the last post I’ve detailed getting started with setup of a basic React App using Next.js and deploying it to Vercel using their respective command line tooling. That post is [Building “Adron’s Core Platform”: Starting a React App on Vercel](/2024/11/19/building-adrons-core-platform-starting-a-react-app-on-vercel/).

### Database Time – Getting a PostgreSQL Database

First, I setup the database in Vercel. Navigate to ***Storage***.

[![](/wp-content/uploads/2024/11/CleanShot-2024-11-19-at-10.41.28.png)](/wp-content/uploads/2024/11/CleanShot-2024-11-19-at-10.41.28.png)

Next I clicked on “Create” next to the Neon option.

[![](/wp-content/uploads/2024/11/CleanShot-2024-11-19-at-10.42.43.png)](/wp-content/uploads/2024/11/CleanShot-2024-11-19-at-10.42.43.png)

The next prompt form will appear. I went with PostgreSQL (Neon) database, as shown, then the closest region (mine is Portland).

[![](/wp-content/uploads/2024/11/CleanShot-2024-11-19-at-12.16.05.png)](/wp-content/uploads/2024/11/CleanShot-2024-11-19-at-12.16.05.png)

Then clicked “Continue” and “Create” again and the database was created.

Now an environment variable will be needed in Vercel and I’ll need to setup the local environment variable too in the .env and .env.local files. To add the Vercel environment variable this command gets that done.

```
vercel env add POSTGRES_URL
```

When I initiate this command it prompts for the value of the key value pair being added. However, in this case, as seems to be the case now on Vercel, the variable was already created and the value inserted into the environment variable. I suppose Vercel and Neon have really upped the level of integration there and made it even more seamless. Whatever is going on behind the curtains these days, that’s rad, but you would likely want to know and check your environment variables.

To check out the variables for the project, I navigate to the projects list, then click on the specific project.

[![](/wp-content/uploads/2024/11/CleanShot-2024-11-19-at-12.18.48.png)](/wp-content/uploads/2024/11/CleanShot-2024-11-19-at-12.18.48.png)

This changes the menu items across the top of screen to reflect the options for the particular project. I can then click on “Settings” and the left hand options now have the “Environment Variables” for the project.

[![](/wp-content/uploads/2024/11/CleanShot-2024-11-19-at-12.21.04.png)](/wp-content/uploads/2024/11/CleanShot-2024-11-19-at-12.21.04.png)

Once I navigated there I can now see the entire list of environment variables. Which I’ve took a partial screen grab of below.

[![](/wp-content/uploads/2024/11/CleanShot-2024-11-19-at-12.22.01.png)](/wp-content/uploads/2024/11/CleanShot-2024-11-19-at-12.22.01.png)

I took note at this point, that the integration puts a ***lot*** of environment variables into the project and assigns them their particular values. This is very useful for a number of reasons and it is something that is really important to know!

### Prisma & The Database Schema Migration

I’m also going to use Prisma. What I’ll need for this is a schema file, that can be added in the root of the project at *prisma/schema.prisma*. After adding the folder and file, I’ve added the following schema to the file as a first step.

```
generator client {
  provider = "prisma-client-js"
}

datasource db {
  provider = "postgresql"
  url      = env("POSTGRES_URL")
}

model User {
  id        String   @id @default(cuid())
  email     String   @unique
  username  String   @unique
  password  String
  createdAt DateTime @default(now())
  updatedAt DateTime @updatedAt
}
```

Another thing I want to do is setup basic authentication. This makes a perfect first step in getting a database built, setup, and connectivity proofed out. I’ll go ahead and add pertinent dependencies to get all that done.

```
npm install @prisma/client bcryptjs
npm install prisma --save-dev
npm install next-auth
npm install @types/bcryptjs --save-dev
```

Now I can initialize the schema in the database with Prisma. This will add the tables and calumns for the schema setup in the *schema.prisma* file.

```
npx prisma generate
npx prisma db push
```

Now I need to setup the authentication configuration, code, and related collateral.

I’ll setup the authentication code first in *./src/app/lib/auth.ts*.

My understanding that this file, plus a lot of others that I’ll be adding are done so under convention and assumption that they are added in a particular place. I won’t deviate from this convention based approach. For now at least, so if you are following along and deviate from the locations and names of the files, you may find yourself spiraling into a list of errors.

The auth.ts file that I coded up looks like this on completion.

```
import { PrismaClient } from '@prisma/client';
import { PrismaAdapter } from '@auth/prisma-adapter';
import { compare } from 'bcryptjs';
import NextAuth from 'next-auth';
import CredentialsProvider from 'next-auth/providers/credentials';

const prisma = new PrismaClient();

export const {
  handlers: { GET, POST },
  auth,
  signIn,
  signOut,
} = NextAuth({
  adapter: PrismaAdapter(prisma),
  session: {
    strategy: 'jwt'
  },
  pages: {
    signIn: '/login',
  },
  providers: [
    CredentialsProvider({
      name: 'Credentials',
      credentials: {
        username: { label: "Username", type: "text" },
        password: { label: "Password", type: "password" }
      },
      async authorize(credentials) {
        if (!credentials?.username || !credentials?.password) {
          return null;
        }

        const user = await prisma.user.findUnique({
          where: {
            username: credentials.username
          }
        });

        if (!user) {
          return null;
        }

        const isPasswordValid = await compare(credentials.password, user.password);

        if (!isPasswordValid) {
          return null;
        }

        return {
          id: user.id,
          email: user.email,
          username: user.username
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

Next up I’ll need a login page. This I’ll add to *./src/app/login/page.tsx*.

```
'use client';

import { useState } from 'react';
import { signIn } from 'next-auth/react';
import { useRouter } from 'next/navigation';

export default function Login() {
  const router = useRouter();
  const [error, setError] = useState('');
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    setLoading(true);
    setError('');

    const formData = new FormData(e.currentTarget);
    const username = formData.get('username') as string;
    const password = formData.get('password') as string;

    try {
      const result = await signIn('credentials', {
        username,
        password,
        redirect: false,
      });

      if (result?.error) {
        setError('Invalid username or password');
      } else {
        router.push('/dashboard');
      }
    } catch (err) {
      setError('An error occurred. Please try again.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <main className="flex min-h-screen flex-col items-center justify-center p-24">
      <div className="w-full max-w-md space-y-8">
        <div>
          <h2 className="mt-6 text-center text-3xl font-bold tracking-tight">
            Sign in to your account
          </h2>
        </div>
        <form className="mt-8 space-y-6" onSubmit={handleSubmit}>
          <div className="space-y-4 rounded-md shadow-sm">
            <div>
              <label htmlFor="username" className="sr-only">
                Username
              </label>
              <input
                id="username"
                name="username"
                type="text"
                required
                className="relative block w-full rounded-md border-0 p-2 text-gray-900 ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-indigo-600"
                placeholder="Username"
              />
            </div>
            <div>
              <label htmlFor="password" className="sr-only">
                Password
              </label>
              <input
                id="password"
                name="password"
                type="password"
                required
                className="relative block w-full rounded-md border-0 p-2 text-gray-900 ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-indigo-600"
                placeholder="Password"
              />
            </div>
          </div>

          {error && (
            <div className="text-red-500 text-center text-sm">
              {error}
            </div>
          )}

          <button
            type="submit"
            disabled={loading}
            className="group relative flex w-full justify-center rounded-md bg-indigo-600 px-3 py-2 text-sm font-semibold text-white hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600 disabled:opacity-50"
          >
            {loading ? 'Signing in...' : 'Sign in'}
          </button>
        </form>
      </div>
    </main>
  );
}
```

Now a dashboard page, which will just be a pretty empty page right now, just representing something that is protected from general view until someone has an account to login with. I’ll also set it up so that it is the default page the login redirects to.

Adding the page at *./src/app/dashboard/page.tsx* with the following code.

```
import { auth } from '../lib/auth';
import { redirect } from 'next/navigation';

export default async function Dashboard() {
  const session = await auth();

  if (!session?.user) {
    redirect('/login');
  }

  return (
    <main className="flex min-h-screen flex-col items-center justify-center p-24">
      <div className="w-full max-w-4xl">
        <h1 className="text-4xl font-bold mb-8">Dashboard</h1>
        <div className="bg-white shadow rounded-lg p-6">
          <h2 className="text-2xl font-semibold mb-4">Welcome, {session.user.username}!</h2>
          <p className="text-gray-600">You are successfully logged in.</p>
        </div>
      </div>
    </main>
  );
}
```

Next I’m going to need some middleware to manage things. After RTFMing a bit it seems like the middleware file should be at the root of src in *./src/middleware.ts*.

```
import { auth } from './app/lib/auth';
import { NextResponse } from 'next/server';
import type { NextRequest } from 'next/server';

export async function middleware(request: NextRequest) {
  const session = await auth();

  if (!session && request.nextUrl.pathname.startsWith('/dashboard')) {
    return NextResponse.redirect(new URL('/login', request.url));
  }

  return NextResponse.next();
}

export const config = {
  matcher: '/dashboard/:path*'
};
```

Then finally some route mapping in *./src/app/api/register/route.ts*.

```
import { PrismaClient } from '@prisma/client';
import { hash } from 'bcryptjs';
import { NextResponse } from 'next/server';

const prisma = new PrismaClient();

export async function POST(req: Request) {
  try {
    const { username, email, password } = await req.json();

    // Validate input
    if (!username || !email || !password) {
      return NextResponse.json(
        { error: 'Missing required fields' },
        { status: 400 }
      );
    }

    // Check if user already exists
    const existingUser = await prisma.user.findFirst({
      where: {
        OR: [
          { email },
          { username }
        ]
      }
    });

    if (existingUser) {
      return NextResponse.json(
        { error: 'User already exists' },
        { status: 400 }
      );
    }

    // Hash password
    const hashedPassword = await hash(password, 12);

    // Create user
    const user = await prisma.user.create({
      data: {
        username,
        email,
        password: hashedPassword,
      },
    });

    return NextResponse.json(
      {
        id: user.id,
        username: user.username,
        email: user.email,
      },
      { status: 201 }
    );
  } catch (error) {
    return NextResponse.json(
      { error: 'Internal server error' },
      { status: 500 }
    );
  }
}
```

The remaining elements include finally setting up the .env.local file I need, making sure Vercel has those environment variables, and then adding, committing, and pushing all of this to the repo.

The .env.local file should include the following, I’ve of course removed the secrets but this is what it comes out to.

```
POSTGRES_URL="your-neon-connection-string"
NEXTAUTH_SECRET="your-secret-key"
NEXTAUTH_URL="http://localhost:3000"
```

To push to Vercel if that still needed done would look like `vercel env add NEXTAUTH_SECRET` and  `vercel env add NEXTAUTH_URL`. Then finally getting the git gitted and the vercel call executed.

```
git add .
git commit -m "Add authentication and database integration"
git push origin main
vercel
```

Now I can navigate to /api/register endpoint to create a new user, then over to the /login page to log in to the system and access the /dashboard. However, with that ll done there are some immediate improvements I should make. Such as adding a page for registering instead of doing it via an endpoint.

Another thing I discovered with Prisma that is super useful is the studio. If I issue the `npx prisma studio` command an interface launches that provides a way to view and edit database records. I generally use DataGrip from JetBrains, but this is a great app itself – runs on localhost:5555 – that gives you the basic view and edit ability.

### ERROR! ERROR! ERROR! (The First Error)

I ran into some errors while working through this, and here are the quick resolutions if the pop up. The error looked like this.

```
npm install next-auth
npm ERR! code ERESOLVE
npm ERR! ERESOLVE unable to resolve dependency tree
npm ERR!
npm ERR! While resolving: adrons-core-platform@0.1.0
npm ERR! Found: react@19.0.0-rc-66855b96-20241106
npm ERR! node_modules/react
npm ERR!   react@"19.0.0-rc-66855b96-20241106" from the root project
npm ERR!   peer react@"^18.2.0 || 19.0.0-rc-66855b96-20241106" from next@15.0.3
npm ERR!   node_modules/next
npm ERR!     next@"15.0.3" from the root project
npm ERR!     peer next@"^12.2.5 || ^13 || ^14 || ^15" from next-auth@4.24.10
npm ERR!     node_modules/next-auth
npm ERR!       next-auth@"" from the root project
npm ERR!   1 more (react-dom)
npm ERR!
npm ERR! Could not resolve dependency:
npm ERR! peer react@"^17.0.2 || ^18" from next-auth@4.24.10
npm ERR! node_modules/next-auth
npm ERR!   next-auth@"" from the root project
npm ERR!
npm ERR! Fix the upstream dependency conflict, or retry
npm ERR! this command with --force or --legacy-peer-deps
npm ERR! to accept an incorrect (and potentially broken) dependency resolution.
npm ERR!
npm ERR!
npm ERR! For a full report see:
npm ERR! /Users/adron/.npm/_logs/2024-11-18T02_37_28_145Z-eresolve-report.txt

npm ERR! A complete log of this run can be found in: /Users/adron/.npm/_logs/2024-11-18T02_37_28_145Z-debug-0.log
```

This is a fairly common versioning and dependency issue related error. This one looked like a mismatch between React and Next-auth. Oh joy I thought, the exact two things I need to use for this post! Egads! But I toyed around with them and got the issues resolved pretty quickly.

I first ran `npm install next-auth --legacy-peer-deps` and then installed the remaining dependencies I needed.

```
npm install @prisma/client bcryptjs --legacy-peer-deps
npm install prisma --save-dev --legacy-peer-deps
npm install @types/bcryptjs --save-dev --legacy-peer-deps
```

Then I went about cleaning the npm cahce, deleting the node\_modules directory, and reinstalling the dependencies.

```
npm cache clean --force
rm -rf node_modules package-lock.json
npm install
```

Another thing I could have theoretically done here is set the specific versions via the install, but uninstalling and then reinstalling like this.

```
npm uninstall next-auth @prisma/client bcryptjs prisma @types/bcryptjs
npm install next-auth@5.0.0-beta.3 @prisma/client bcryptjs prisma @types/bcryptjs
```

### ERROR! ERROR! ERROR! (The second error)

Now it seemed like, when I got this error I just somehow typed the var wrong. But anyway, here is the error that I got.

```
Error: Prisma schema validation - (get-config wasm)
Error code: P1012
error: Environment variable not found: POSTGRES_URL.
  -->  prisma/schema.prisma:7
   |
 6 |   provider = "postgresql"
 7 |   url      = env("POSTGRES_URL")
   |
Validation Error Count: 1
[Context: getConfig]
Prisma CLI Version : 5.22.0
```

Basically I must have not added or typed POSTGRES\_URL correctly somewhere. I also figured maybe I needed a .env too in addition to the .env.local I added. So I went about correcting each of these things. I did a search for POSTGRES\_URL and didn’t find anything in particular. Immediately after that I went ahead and added a *.env* file with the following contents. Again, with pertinent secrets removed for the config below. (More details on NEXTAUTH\_SECRET and NEXTAUTH\_URL later in the post)

```
POSTGRES_URL="postgresql://your-username:your-password@your-host:5432/your-database"

NEXTAUTH_SECRET="your-secret-key-here"
NEXTAUTH_URL="http://localhost:3000"
```

I also checked that the .gitignore file had the pertinent values added.

```
# Local env files
.env
.env*.local
```

All that seemed to resolve the issue, and while I was at it I opted to write up a script to test and verify database connectivity. I added a `test-env.ts` file in a folder I added named `scripts` and added the following code.

```
import { PrismaClient } from '@prisma/client'

const prisma = new PrismaClient()

async function main() {
  try {
    // Attempt to connect to the database
    await prisma.$connect()
    console.log('Successfully connected to the database')
  } catch (error) {
    console.error('Failed to connect to the database:', error)
  } finally {
    await prisma.$disconnect()
  }
}

main()
```

I then executed that code with `npx ts-node scripts/test-env.ts`. I immediately then got another error! I was on a roll with the errors today.

```
import { PrismaClient } from '@prisma/client';
^^^^^^
SyntaxError: Cannot use import statement outside a module
    at internalCompileFunction (node:internal/vm:77:18)
    at wrapSafe (node:internal/modules/cjs/loader:1288:20)
    at Module._compile (node:internal/modules/cjs/loader:1340:27)
    at Module.m._compile (/Users/adron/.npm/_npx/1bf7c3c15bf47d04/node_modules/ts-node/src/index.ts:1618:23)
    at Module._extensions..js (node:internal/modules/cjs/loader:1435:10)
    at Object.require.extensions.<computed> [as .ts] (/Users/adron/.npm/_npx/1bf7c3c15bf47d04/node_modules/ts-node/src/index.ts:1621:12)
    at Module.load (node:internal/modules/cjs/loader:1207:32)
    at Function.Module._load (node:internal/modules/cjs/loader:1023:12)
    at Function.executeUserEntryPoint [as runMain] (node:internal/modules/run_main:135:12)
    at phase4 (/Users/adron/.npm/_npx/1bf7c3c15bf47d04/node_modules/ts-node/src/bin.ts:649:14)
```

I looked at the code and tweaked it just a bit to this.

```
const { PrismaClient } = require('@prisma/client');

const prisma = new PrismaClient();

async function main() {
  try {
    await prisma.$connect();
    console.log('Successfully connected to the database');
  } catch (error) {
    console.error('Failed to connect to the database:', error);
  } finally {
    await prisma.$disconnect();
  }
}

main();
```

I then also added a ./scripts/tsconfig.json file with the follwing.

```
{
  "compilerOptions": {
    "target": "ES2018",
    "module": "CommonJS",
    "lib": ["ES2018"],
    "strict": true,
    "esModuleInterop": true,
    "skipLibCheck": true,
    "forceConsistentCasingInFileNames": true
  }
}
```

I tried running the command again, but with the following `npx ts-node --project scripts/tsconfig.json scripts/test-env.ts` and that proved out the connection to the database. At this point, everything appears to be running and operational. I tried creating a user and logging in and everything flowed smoothly except for the redirect to the dashboard page after login and some other errors. I realized I’d not set NEXTAUTH\_SECRET and NEXTAUTH\_URL to their proper values, I’d completely forgotten about that!

For the NEXTAUTH\_SECRET I used `openssl rand -base64 32` to set that. Another option is to use node and run `node -e "console.log(crypto.randomBytes(32).toString('base64'))"`. Either of these commands will give you a solid value for the secret.

For the NEXTAUTH\_URL use <http://localhost:3000> for the local environment and <https://whatever-the-app-is-called.vercel.app> for the production deploy to Vercel.

With those final changes, after logging in, I manually typed in the path to the dashboard and it all worked! If you run into any URL path flakiness, be sure to check that the Vercel variables are set correctly when pushing to production. If these settings are off just a little, or if you’ve set a specific domain name, you’ll end up with time out errors or other issues. This is something I’ll cover in a subsequent post, so with that, until next time, my your coding all compile the first time!

Subscribe on the side bar, and continue this journey through errors and the chaos of Next.js dev with React on Vercel with PostgreSQL! Soon I’ll also be re-introducing the mutli-tenancy notions behind running multiple applications and also the core domain of my “Collector’s Tune Tracker” app!

## Quick Links to Related Posts & Series Posts

**OG Posts on [adron.tools](https://adron.tools) and [Collector’s Tune Tracker](https://adron.github.io/collectorstunetracker/)**

The trio of initial posts that kicked off this entire effort. Things have changed tremendously from these original posts, but they provide much of the root reasoning around getting this series and these apps built!

- [Building a Multi-Tenant Music Collector’s Database](/2023/10/23/building-a-multi-tenant-music-collectors-database/)
- [Starting a New Project – Let’s Choose the Tech](/2024/02/15/starting-a-new-project-lets-choose-a-tech-stack/)
- [Software Development: Getting Started by Getting Organized](/2024/05/02/software-development-getting-started-by-getting-organized/).

**Previous Posts**

- [Building “Adron’s Core Platform”: Starting a React App on Vercel](/2024/11/26/building-adrons-core-platform-starting-a-react-app-on-vercel/)

**Subsequent Posts**

- Publishing [The Confederacy of Errors Starting With Next Auth; Error, Error, npm ERR!](/2024/11/26/the-confederacy-of-errors-starting-with-next-auth-error-error-npm-err/) in about ~5 hours (final edits and all).
