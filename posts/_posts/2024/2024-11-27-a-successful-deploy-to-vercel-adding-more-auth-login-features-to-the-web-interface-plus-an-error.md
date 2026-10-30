---
title: A Successful Deploy to Vercel + Adding More Auth & Login Features to The Web Interface (Plus an Error!)
date: 2024-11-27 10:30:00 -0800
last_modified_at: 2024-12-09 09:55:33 -0800
permalink: /2024/11/27/a-successful-deploy-to-vercel-adding-more-auth-login-features-to-the-web-interface-plus-an-error/
slug: a-successful-deploy-to-vercel-adding-more-auth-login-features-to-the-web-interface-plus-an-error
wp_id: 70310
original_url: https://compositecode.blog/2024/11/27/a-successful-deploy-to-vercel-adding-more-auth-login-features-to-the-web-interface-plus-an-error/
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
excerpt: In the last few posts I knocked out a slew of initial work. Much of it was just to get things up and running and make sure the database was live, the site was live, and that there was a good connection between the two. I did this by building the first basic login page …
image: /wp-content/uploads/2024/11/IMG_8669.jpeg
---

In the last few posts I knocked out a slew of initial work. Much of it was just to get things up and running and make sure the database was live, the site was live, and that there was a good connection between the two. I did this by building the first basic login page with a dashboard that just shows that the user is logged in, along with a few pages to display general static content. That can be found in:

1. [Building “Adron’s Core Platform”: Starting a React App on Vercel](/2024/11/26/building-adrons-core-platform-starting-a-react-app-on-vercel/)
2. [Getting a Vercel PostgreSQL Database and Basic Authentication Operational](/2024/11/26/getting-a-vercel-postgresql-database-and-basic-authentication-operational/)
3. [The Confederacy of Errors Starting With Next Auth; Error, Error, npm ERR!](/2024/11/26/the-confederacy-of-errors-starting-with-next-auth-error-error-npm-err/)

The tasks I’ll accomplish in the following post:

1. I want a horizontal menu across the top that will link to the dashboard, login, and about page.
2. I want an account creation page.
3. I want to make sure that I set things up for the post-login action to be a redirect to the dashboard page.

### Adding a Horizontal Menu

For this menu I’m going to add a div with links, assign it as a flex space (css), and add the pertinent links. The changed ./src/app/components/Navigation.tsx with changes looks like this now.

```
'use client';

import Link from 'next/link';
import { usePathname } from 'next/navigation';

export default function Navigation() {
  const pathname = usePathname();

  const isActive = (path: string) => {
    return pathname === path ? 'bg-indigo-700' : '';
  };

  return (
    <nav className="bg-indigo-600 p-4">
      <div className="container mx-auto">
        <div className="flex items-center justify-between">
          <div className="flex space-x-4">
            <Link href="/"
              className={`text-white px-3 py-2 rounded-md text-sm font-medium ${isActive('/')}`}>
              Home
            </Link>
            <Link href="/dashboard"
              className={`text-white px-3 py-2 rounded-md text-sm font-medium ${isActive('/dashboard')}`}>
              Dashboard
            </Link>
            <Link href="/login"
              className={`text-white px-3 py-2 rounded-md text-sm font-medium ${isActive('/login')}`}>
              Login
            </Link>
            <Link href="/about"
              className={`text-white px-3 py-2 rounded-md text-sm font-medium ${isActive('/about')}`}>
              About
            </Link>
          </div>
        </div>
      </div>
    </nav>
  );
}
```

Next up is a tweak to *./src/app/layout.tsx*.

```
import type { Metadata } from 'next';
import { Inter } from 'next/font/google';
import './globals.css';
import Navigation from './components/Navigation';

const inter = Inter({ subsets: ['latin'] });

export const metadata: Metadata = {
  title: "Adron's Core Platform",
  description: 'Core platform application',
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body className={inter.className}>
        <Navigation />
        {children}
      </body>
    </html>
  );
}
```

As a little lagniappe, I’ve decided to add content to the about page at *./src/app/about/page.tsx*.

```
export default function About() {
  return (
    <main className="flex min-h-screen flex-col items-center p-24">
      <div className="max-w-2xl">
        <h1 className="text-4xl font-bold mb-6">About</h1>
        <div className="prose">
          <p className="text-lg mb-4">
            Welcome to Adron&apos;s Core Platform, a modern web application built with Next.js,
            TypeScript, and PostgreSQL.
          </p>
          <p className="text-lg">
            This platform demonstrates secure authentication, database integration,
            and modern web development practices.
          </p>
        </div>
      </div>
    </main>
  );
}
```

I also decided, on one of the `npm run dev` viewing cycles, I wanted something else for the general front page description so made these additions to `./src/app/page.tsx`.

```
export default function Home() {
  return (
    <main className="flex min-h-screen flex-col items-center p-24">
      <div className="max-w-4xl mx-auto">
        <h1 className="text-4xl font-bold mb-6">
          Adron&apos;s Core Platform
        </h1>

        <section className="mb-8">
          <h2 className="text-2xl font-semibold mb-4">Your Central Command for Development Tools</h2>
          <p className="text-lg mb-4">
            Welcome to the Core Platform - your centralized hub for managing and accessing Adron&apos;s suite of development tools and applications. This platform provides unified access control, monitoring, and integration capabilities across all tools in the ecosystem.
          </p>
        </section>

        <section className="grid grid-cols-1 md:grid-cols-2 gap-6 mb-8">
          <div className="p-6 bg-white rounded-lg shadow-md">
            <h3 className="text-xl font-semibold mb-3">Unified Access</h3>
            <p>Single sign-on capabilities for seamless access to all integrated tools and services in the Adron&apos;s Tools ecosystem.</p>
          </div>

          <div className="p-6 bg-white rounded-lg shadow-md">
            <h3 className="text-xl font-semibold mb-3">Centralized Management</h3>
            <p>Monitor usage, manage permissions, and configure integrations for your development toolkit from one location.</p>
          </div>

          <div className="p-6 bg-white rounded-lg shadow-md">
            <h3 className="text-xl font-semibold mb-3">Tool Integration</h3>
            <p>Connect and manage your development workflow across multiple tools with seamless integration capabilities.</p>
          </div>

          <div className="p-6 bg-white rounded-lg shadow-md">
            <h3 className="text-xl font-semibold mb-3">Usage Analytics</h3>
            <p>Track and analyze your tool usage patterns to optimize your development workflow and resource allocation.</p>
          </div>
        </section>

        <section className="text-center">
          <p className="text-lg">
            Ready to streamline your development workflow?
            <a href="/login" className="text-indigo-600 hover:text-indigo-800 ml-2 font-semibold">
              Sign in to get started
            </a>
          </p>
        </section>
      </div>
    </main>
  );
}
```

All those changes and static additions done and it’s time for a build. Which then… drumroll… threw an import error in the ./src/app/lib/auth.ts file! I just keep conjuring these things up left and right. Eventually I’ll get all the wires uncrossed.

```
./src/app/lib/auth.ts:2:0
Module not found: Can't resolve '@auth/prisma-adapter'
  1 | import { PrismaClient } from '@prisma/client';
> 2 | import { PrismaAdapter } from '@auth/prisma-adapter';
  3 | import { compare } from 'bcryptjs';
  4 | import NextAuth from 'next-auth';
  5 | import CredentialsProvider from 'next-auth/providers/credentials';

https://nextjs.org/docs/messages/module-not-found

Import trace for requested module:
./src/middleware.ts
```

I wasn’t sure why this seemed to throw an error during the build, but it seemed fine when I just ran `npm run dev` a few second before. Whatever the case is, gotta have a good build to be able to ship it to Vercel. So spelunking for a fix I went. My first attempt was simply to just add the dependency again with `npm install @auth/prisma-adapter`.

The new code file, for full copy-ability, now reads like this with minor import changes at the top.

```
import { PrismaClient } from '@prisma/client';
import NextAuth from 'next-auth';
import CredentialsProvider from 'next-auth/providers/credentials';
import { compare } from 'bcryptjs';

const prisma = new PrismaClient();

export const { auth, signIn, signOut } = NextAuth({
  pages: {
    signIn: '/login',
  },
  session: {
    strategy: 'jwt'
  },
  providers: [
    CredentialsProvider({
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
  ]
});
```

That got me back to an operable state to test what I have so far. However, I did want to make full quality assurance style manual testing possible, so I still needed the page to create an account with.

### Create An Account Page

I create another page at *./src/app/create-account/page.tsx* and wrote it up with the following code.

```
'use client';

import { useState } from 'react';
import { useRouter } from 'next/navigation';

export default function CreateAccount() {
  const router = useRouter();
  const [error, setError] = useState('');
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    setLoading(true);
    setError('');

    const formData = new FormData(e.currentTarget);
    const data = {
      username: formData.get('username'),
      email: formData.get('email'),
      password: formData.get('password'),
      confirmPassword: formData.get('confirmPassword'),
    };

    if (data.password !== data.confirmPassword) {
      setError('Passwords do not match');
      setLoading(false);
      return;
    }

    try {
      const response = await fetch('/api/register', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          username: data.username,
          email: data.email,
          password: data.password,
        }),
      });

      if (!response.ok) {
        const errorData = await response.json();
        throw new Error(errorData.error || 'Failed to create account');
      }

      router.push('/login');
    } catch (err) {
      setError(err instanceof Error ? err.message : 'An error occurred');
    } finally {
      setLoading(false);
    }
  };

  return (
    <main className="flex min-h-screen flex-col items-center justify-center p-24">
      <div className="w-full max-w-md space-y-8">
        <div>
          <h2 className="mt-6 text-center text-3xl font-bold tracking-tight">
            Create your account
          </h2>
          <p className="mt-2 text-center text-sm text-gray-600">
            Join Adron&apos;s Core Platform
          </p>
        </div>

        <form className="mt-8 space-y-6" onSubmit={handleSubmit}>
          <div className="space-y-4 rounded-md">
            <div>
              <label htmlFor="username" className="block text-sm font-medium text-gray-700">
                Username
              </label>
              <input
                id="username"
                name="username"
                type="text"
                required
                className="relative block w-full rounded-md border-0 p-2 text-gray-900 ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-indigo-600"
                placeholder="Choose a username"
              />
            </div>

            <div>
              <label htmlFor="email" className="block text-sm font-medium text-gray-700">
                Email address
              </label>
              <input
                id="email"
                name="email"
                type="email"
                required
                className="relative block w-full rounded-md border-0 p-2 text-gray-900 ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-indigo-600"
                placeholder="you@example.com"
              />
            </div>

            <div>
              <label htmlFor="password" className="block text-sm font-medium text-gray-700">
                Password
              </label>
              <input
                id="password"
                name="password"
                type="password"
                required
                className="relative block w-full rounded-md border-0 p-2 text-gray-900 ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-indigo-600"
                placeholder="Create a strong password"
              />
            </div>

            <div>
              <label htmlFor="confirmPassword" className="block text-sm font-medium text-gray-700">
                Confirm Password
              </label>
              <input
                id="confirmPassword"
                name="confirmPassword"
                type="password"
                required
                className="relative block w-full rounded-md border-0 p-2 text-gray-900 ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-indigo-600"
                placeholder="Confirm your password"
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
            {loading ? 'Creating account...' : 'Create Account'}
          </button>
        </form>
      </div>
    </main>
  );
}
```

Then in the ./src/app/components/Navigation.tsx component added a link to this new page.

```
<Link href="/create-account"
  className={`text-white px-3 py-2 rounded-md text-sm font-medium ${isActive('/create-account')}`}>
  Create Account
</Link>
```

From this point I also made some tweaks to the *./src/app/login/page.tsx* page where I set the redirect on sign in to true, the callbackUrl to `/dashboard`, and removed the manual `router.push()` since NextAuth handles that redirect now. With those changes the page now looks like this.

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
        redirect: true,
        callbackUrl: '/dashboard'
      });

      if (result?.error) {
        setError('Invalid username or password');
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

Finally a few tweaks to the *./src/middleware.ts* code.

```
import NextAuth from 'next-auth';
import authConfig from './app/auth.config';

export const { auth: middleware } = NextAuth(authConfig);

export const config = {
  matcher: ['/((?!api|_next/static|_next/image|favicon.ico).*)'],
};
```

After toying around I realized I also needed a ./src/app/api/auth/[…nextauth]/route.ts code file too in order to get the redirect to work correctly.

```
import { GET, POST } from '../../../lib/auth';

export { GET, POST };
```

Also, for good measure, in case I missed any minute changes with all these steps and error troubleshooting, here is what my final auth.ts and auth.config.ts file looks like at this point.

The *./src/app/lib/auth.ts* code.

```
import NextAuth from 'next-auth';
import CredentialsProvider from 'next-auth/providers/credentials';
import { compare } from 'bcryptjs';
import { PrismaClient } from '@prisma/client';

const prisma = new PrismaClient();

export const { handlers: { GET, POST }, auth } = NextAuth({
  providers: [
    CredentialsProvider({
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
          username: user.username,
        };
      }
    })
  ],
  pages: {
    signIn: '/login',
  },
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
  },
  session: {
    strategy: "jwt"
  }
});
```

Finally the *./src/app/auth.config.ts*.

```
import type { NextAuthConfig } from 'next-auth';

export default {
  pages: {
    signIn: '/login',
  },
  callbacks: {
    authorized({ auth, request: { nextUrl } }) {
      const isLoggedIn = !!auth?.user;
      const isOnDashboard = nextUrl.pathname.startsWith('/dashboard');

      if (isOnDashboard) {
        if (isLoggedIn) return true;
        return false;
      }
      return true;
    },
  },
  providers: [],
} satisfies NextAuthConfig;
```

At this point, low and behold, I did another build, which broke, and had committed so saw the same break in Vercel. The error as Vercel logs had it showed as this.

```
Linting and checking validity of types ...
15:10:43.210
 ⨯ ESLint: Failed to load config "next/typescript" to extend from. Referenced from: /vercel/path0/.eslintrc.json
15:10:44.757
Failed to compile.
15:10:44.757
15:10:44.757
./src/app/dashboard/page.tsx:16:78
15:10:44.757
Type error: Property 'username' does not exist on type 'User'.
15:10:44.757
15:10:44.758
 14 | <h1 className="text-4xl font-bold mb-8">Dashboard</h1>
15:10:44.758
 15 | <div className="bg-white shadow rounded-lg p-6">
15:10:44.758
> 16 | <h2 className="text-2xl font-semibold mb-4">Welcome, {session.user.username}!</h2>
15:10:44.758
 | ^
15:10:44.758
 17 | <p className="text-gray-600">You are successfully logged in.</p>
15:10:44.758
 18 | </div>
15:10:44.758
 19 | </div>
15:10:44.826
Error: Command "npm run build" exited with 1
```

I realized quickly, I’ve got a user type messed up, and possibly need to fix or update the ESLint situation. First thing, I’ll fix the types. Added a *./src/types/next-auth.d.ts* file and updated the dashboard file at *./src/app/dashboard/page.tsx* to solve the type issue.

The *./src/types/next-auth.d.ts* declaration.

```
import NextAuth from "next-auth";

declare module "next-auth" {
  interface User {
    username: string;
    email: string;
    id: string;
  }

  interface Session {
    user: User & {
      username: string;
    };
  }
}
```

The *./src/app/dashboard/page.tsx* modification.

```
import { auth } from '../lib/auth';
import { redirect } from 'next/navigation';

export default async function Dashboard() {
  const session = await auth();

  if (!session?.user) {
    redirect('/login');
  }

  return (
    <main className="flex min-h-screen flex-col items-center p-24">
      <div className="w-full max-w-4xl">
        <h1 className="text-4xl font-bold mb-8">Dashboard</h1>
        <div className="bg-white shadow rounded-lg p-6">
          <h2 className="text-2xl font-semibold mb-4">
            Welcome, {session.user?.username || 'User'}!
          </h2>
          <p className="text-gray-600">You are successfully logged in.</p>
        </div>
      </div>
    </main>
  );
}
```

Now time to update to resolve the ESLint situation. I opened up the *.eslintrc.json* file and changed those contents to this.

```
{
  "extends": [
    "next",
    "next/core-web-vitals"
  ],
  "rules": {
    "@next/next/no-html-link-for-pages": "off"
  }
}
```

Then wrapped up these modifications with some final change to *tsconfig.json*.

```
{
  "compilerOptions": {
    "target": "es5",
    "lib": ["dom", "dom.iterable", "esnext"],
    "allowJs": true,
    "skipLibCheck": true,
    "strict": true,
    "noEmit": true,
    "esModuleInterop": true,
    "module": "esnext",
    "moduleResolution": "bundler",
    "resolveJsonModule": true,
    "isolatedModules": true,
    "jsx": "preserve",
    "incremental": true,
    "plugins": [
      {
        "name": "next"
      }
    ],
    "paths": {
      "@/*": ["./src/*"]
    }
  },
  "include": ["next-env.d.ts", "**/*.ts", "**/*.tsx", "src/types/**/*.ts", ".next/types/**/*.ts"],
  "exclude": ["node_modules"]
}
```

Now to clean up and get dependencies fresh. First a `rm -rf .next` then `npm install` and now another, fingers crossed, `npm run build`. The build at this point threw me another error, which again fingers crossed hopefully this is the last one!

```
./src/app/lib/auth.ts:22:13
Type error: Type '{}' is not assignable to type 'string'.
  20 |         const user = await prisma.user.findUnique({
  21 |           where: {
> 22 |             username: credentials.username
     |             ^
  23 |           }
  24 |         });
  25 |
```

Looking at it, that seems an easy fix. I’m not even sure how or why I wrote that up that way, but whatever, it’s fixin’ time! I need to fix a type definition for credentials in the authorize function, some type annotations for session and token callbacks, and another RTFMing moment of fixing the NextAuthConfig type and the satisfies operator, and explicitly type the session parameters. Maybe. I could be wrong, but let’s see. That’s after the first long read of the code again. Changes all seem to be needed in the *./src/app/lib/auth.ts* file, and after all of these changes it looks like this.

```
import NextAuth from 'next-auth';
import CredentialsProvider from 'next-auth/providers/credentials';
import { compare } from 'bcryptjs';
import { PrismaClient } from '@prisma/client';
import type { NextAuthConfig } from 'next-auth';

const prisma = new PrismaClient();

export const { handlers: { GET, POST }, auth } = NextAuth({
  providers: [
    CredentialsProvider({
      credentials: {
        username: { label: "Username", type: "text" },
        password: { label: "Password", type: "password" }
      },
      async authorize(credentials) {
        if (!credentials?.username || !credentials?.password) {
          return null;
        }

        const username = credentials.username as string;
        const password = credentials.password as string;

        const user = await prisma.user.findUnique({
          where: { username }
        });

        if (!user) {
          return null;
        }

        const isPasswordValid = await compare(password, user.password);

        if (!isPasswordValid) {
          return null;
        }

        return {
          id: user.id,
          email: user.email,
          username: user.username,
        };
      }
    })
  ],
  pages: {
    signIn: '/login',
  },
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
  },
  session: {
    strategy: "jwt"
  }
} satisfies NextAuthConfig);
```

Now another `npm run build`.

Ok, built locally, let’s push with `vercel`. Oh joy of joys!

```
at Ba (/vercel/path0/node_modules/@prisma/client/runtime/library.js:33:69)
15:18:29.640
 at new t (/vercel/path0/node_modules/@prisma/client/runtime/library.js:130:739)
15:18:29.640
 at 904 (/vercel/path0/.next/server/app/api/register/route.js:1:552)
15:18:29.640
 at t (/vercel/path0/.next/server/webpack-runtime.js:1:143)
15:18:29.640
 at t (/vercel/path0/.next/server/app/api/register/route.js:1:2228)
15:18:29.641
 at /vercel/path0/.next/server/app/api/register/route.js:1:2258
15:18:29.641
 at t.X (/vercel/path0/.next/server/webpack-runtime.js:1:1285)
15:18:29.641
 at /vercel/path0/.next/server/app/api/register/route.js:1:2241
15:18:29.641
 at Object.<anonymous> (/vercel/path0/.next/server/app/api/register/route.js:1:2284)
15:18:29.641
 at Module._compile (node:internal/modules/cjs/loader:1469:14) {
15:18:29.641
 clientVersion: '5.22.0',
15:18:29.641
 errorCode: undefined
15:18:29.642
}
15:18:29.647
15:18:29.647
> Build error occurred
15:18:29.647
Error: Failed to collect page data for /api/register
15:18:29.647
 at /vercel/path0/node_modules/next/dist/build/utils.js:1217:15
15:18:29.647
 at process.processTicksAndRejections (node:internal/process/task_queues:95:5) {
15:18:29.647
 type: 'Error'
15:18:29.647
}
15:18:29.713
Error: Command "npm run build" exited with 1
15:18:29.950
```

This looks very Prisma related. Probably a configuration issue of sorts? I did a little sleuthing and it looks like if I add a step via the `vercel.json` file (added to root of the project) I could set it up like this.

```
{
  "buildCommand": "prisma generate && next build",
  "installCommand": "npm install",
  "framework": "nextjs"
}
```

Then update the Prisma schema with edge compatible settings, create a client that’s edge compatible too, and update the ole auth.ts file again. With those changes I end up with a *./prisma/schema.prisma* file like this.

```
generator client {
  provider = "prisma-client-js"
  previewFeatures = ["driverAdapters"]
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

The ./src/lib/prisma.ts file that looks like this.

```
import { PrismaClient } from '@prisma/client'

const globalForPrisma = globalThis as unknown as {
  prisma: PrismaClient | undefined
}

export const prisma =
  globalForPrisma.prisma ??
  new PrismaClient({
    log: ['query'],
  })

if (process.env.NODE_ENV !== 'production') globalForPrisma.prisma = prisma
```

Last an auth file at ./src/app/lib/auth.ts that ends up with minor modifications and looks like this now.

```
import NextAuth from 'next-auth';
import CredentialsProvider from 'next-auth/providers/credentials';
import { compare } from 'bcryptjs';
import type { NextAuthConfig } from 'next-auth';
import { prisma } from '@/lib/prisma';

export const { handlers: { GET, POST }, auth } = NextAuth({
  providers: [
    CredentialsProvider({
      credentials: {
        username: { label: "Username", type: "text" },
        password: { label: "Password", type: "password" }
      },
      async authorize(credentials) {
        if (!credentials?.username || !credentials?.password) {
          return null;
        }

        const username = credentials.username as string;
        const password = credentials.password as string;

        const user = await prisma.user.findUnique({
          where: { username }
        });

        if (!user) {
          return null;
        }

        const isPasswordValid = await compare(password, user.password);

        if (!isPasswordValid) {
          return null;
        }

        return {
          id: user.id,
          email: user.email,
          username: user.username,
        };
      }
    })
  ],
  pages: {
    signIn: '/login',
  },
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
  },
  session: {
    strategy: "jwt"
  }
} satisfies NextAuthConfig);
```

Looking through the package.json file I made sure all my versions were what I’d set em’ to for legacy compatibility and all the other steps from this series, during the resolution of the many errors, it looks like this now.

```
{
  "name": "adrons-core-platform",
  "version": "0.1.0",
  "private": true,
  "scripts": {
    "dev": "next dev",
    "build": "prisma generate && next build",
    "start": "next start",
    "lint": "next lint",
    "postinstall": "prisma generate"
  },
  "dependencies": {
    "@prisma/client": "^5.22.0",
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
    "prisma": "^5.22.0",
    "tailwindcss": "^3.3.5",
    "typescript": "^5.3.2"
  }
}
```

Wrapped that up with commit and pushed it.

```
git add .
git commit -m "Fix Prisma configuration for Vercel deployment"
git push
```

With that I’ve now got Prisma generate added to the build process, created a proper Prisma client (yeah, that was a solid hour of RTFMing that, dear reader, you can now skip with the example above), updated the build config specifically for Vercel with the vercel.json file, and added edge-compatible settings to Prisma. Yay for more uses of the word \*edge\* to mean various things. But I digress, THE BUILD WORKED!

I did a little test and things appeared to work, but I wanted one more change to this effort. I still wanted a logoff item in the navigation and wanted it to show pertinent to the state of being logged in or logged out.

### Setting up Logoff

Navigation will need changes, so I updated that file with changes to show or hide the pertinent options based on session state. My *./src/app/components/Navigation.tsx* now looks like this.

```
'use client';

import Link from 'next/link';
import { usePathname } from 'next/navigation';
import { signOut, useSession } from 'next-auth/react';
import { useRouter } from 'next/navigation';

export default function Navigation() {
  const pathname = usePathname();
  const { data: session, status } = useSession();
  const router = useRouter();

  const isActive = (path: string) => {
    return pathname === path ? 'bg-indigo-700' : '';
  };

  const handleLogout = async () => {
    await signOut({ redirect: true, callbackUrl: '/' });
  };

  return (
    <nav className="bg-indigo-600 p-4">
      <div className="container mx-auto">
        <div className="flex items-center justify-between">
          <div className="flex space-x-4">
            <Link href="/"
              className={`text-white px-3 py-2 rounded-md text-sm font-medium ${isActive('/')}`}>
              Home
            </Link>
            <Link href="/dashboard"
              className={`text-white px-3 py-2 rounded-md text-sm font-medium ${isActive('/dashboard')}`}>
              Dashboard
            </Link>
            {!session ? (
              <>
                <Link href="/login"
                  className={`text-white px-3 py-2 rounded-md text-sm font-medium ${isActive('/login')}`}>
                  Login
                </Link>
                <Link href="/create-account"
                  className={`text-white px-3 py-2 rounded-md text-sm font-medium ${isActive('/create-account')}`}>
                  Create Account
                </Link>
              </>
            ) : (
              <button
                onClick={handleLogout}
                className="text-white px-3 py-2 rounded-md text-sm font-medium hover:bg-indigo-700"
              >
                Logout
              </button>
            )}
            <Link href="/about"
              className={`text-white px-3 py-2 rounded-md text-sm font-medium ${isActive('/about')}`}>
              About
            </Link>
          </div>
          {session && (
            <div className="text-white text-sm">
              Welcome, {session.user?.username}
            </div>
          )}
        </div>
      </div>
    </nav>
  );
}
```

Next I wrote some code in a *./src/app/providers.tsx* file.

```
'use client';

import { SessionProvider } from 'next-auth/react';

export default function Providers({ children }: { children: React.ReactNode }) {
  return <SessionProvider>{children}</SessionProvider>;
}
```

Then an addition to *./src/app/layout.tsx*.

```
import type { Metadata } from 'next';
import { Inter } from 'next/font/google';
import './globals.css';
import Navigation from './components/Navigation';
import Providers from './providers';

const inter = Inter({ subsets: ['latin'] });

export const metadata: Metadata = {
  title: "Adron's Core Platform",
  description: 'Core platform application',
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body className={inter.className}>
        <Providers>
          <Navigation />
          {children}
        </Providers>
      </body>
    </html>
  );
}
```

The key additions for this bit of code included:

- added a session state management using `useSession` hook.
- conditionally rendering the login/create account or logout based on session status.
- added a welcom message with the username when logged in.
- implemented the logout functionality that redirects to the home page.
- added SessionProvider to make auth state available

With that I added the NEXTAUTH\_URL in the .env, added it to Vercel, and ensured the login page had the right settings. The .env file addition just included `NEXTAUTH_URL="https://adron.tools"` and `NEXT_PUBLIC_BASE_URL="https://adron.tools"`, on Vercel I set the environment variable `NEXT_PUBLIC_BASE_URL=https://adron.tools`, and then the next.config.js file I tweaked with this.

```
/** @type {import('next').NextConfig} */
const nextConfig = {
  reactStrictMode: true,
  swcMinify: true,
  async redirects() {
    return [
      {
        source: '/:path*',
        has: [
          {
            type: 'host',
            value: 'adrons-core-platform.vercel.app',
          },
        ],
        destination: 'https://adron.tools/:path*',
        permanent: true,
      },
    ];
  },
};

module.exports = nextConfig;
```

I then wrapped up that effort with additions and updates to the *./src/app/login/page.tsx* page.

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
        redirect: true,
        callbackUrl: new URL('/dashboard', process.env.NEXT_PUBLIC_BASE_URL || 'https://adron.tools').toString()
      });

      if (result?.error) {
        setError('Invalid username or password');
      }
    } catch (err) {
      setError('An error occurred. Please try again.');
    } finally {
      setLoading(false);
    }
  };

  // ... rest of your component remains the same
}
```

After all that, and the previous posts, I finally had a basic authentication, create user, logoff feature, and a little lagniappe here and there. The big take away from all of this, is I now had a base, that was operable locally and on Vercel, to start iterating against to truly start adding some proper features. For that, stay tune, possibly subscribe so you get the upcoming posts, and I’ll catch you on the next string of errors and building code! It’ll be sooner than later! 🤘🏻

## Quick Links to Related Posts & Series Posts

**OG Posts on [adron.tools](https://adron.tools) and [Collector’s Tune Tracker](https://adron.github.io/collectorstunetracker/)**

The trio of initial posts that kicked off this entire effort. Things have changed tremendously from these original posts, but they provide much of the root reasoning around getting this series and these apps built!

- [Building a Multi-Tenant Music Collector’s Database](/2023/10/23/building-a-multi-tenant-music-collectors-database/)
- [Starting a New Project – Let’s Choose the Tech](/2024/02/15/starting-a-new-project-lets-choose-a-tech-stack/)
- [Software Development: Getting Started by Getting Organized](/2024/05/02/software-development-getting-started-by-getting-organized/).

**Previous Posts**

- [Building “Adron’s Core Platform”: Starting a React App on Vercel](/2024/11/19/building-adrons-core-platform-starting-a-react-app-on-vercel/)
- [Getting a Vercel PostgreSQL Database and Basic Authentication Operational](/2024/11/26/getting-a-vercel-postgresql-database-and-basic-authentication-operational/)
- [The Confederacy of Errors, Starting with Next Auth Error, Error, NPM ERR!](/2024/11/26/the-confederacy-of-errors-starting-with-next-auth-error-error-npm-err/)
