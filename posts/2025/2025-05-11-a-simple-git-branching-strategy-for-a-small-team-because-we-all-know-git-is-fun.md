---
title: A Simple Git Branching Strategy for a Small Team (Because We All Know Git Is Fun!)
date: 2025-05-11 12:22:16 -0700
last_modified_at: 2025-06-04 13:37:42 -0700
permalink: /2025/05/11/a-simple-git-branching-strategy-for-a-small-team-because-we-all-know-git-is-fun/
slug: a-simple-git-branching-strategy-for-a-small-team-because-we-all-know-git-is-fun
wp_id: 71998
original_url: https://compositecode.blog/2025/05/11/a-simple-git-branching-strategy-for-a-small-team-because-we-all-know-git-is-fun/
categories:
- Coding Adventures
- Programming
tags:
- coding
- git
- git flow
- git practices
- programming
- source control
excerpt: For small development teams, a straightforward Git strategy is crucial to avoid merge conflicts. Focus on utilizing only main and feature branches to keep the workflow efficient. Regular rebasing and meaningful commits are essential for maintaining a clean history. Emphasize collaboration through pull requests, and ensure code reviews are part of the process.
image: /wp-content/uploads/2025/05/git-things.png
---

Git. It’s the tool that makes some of us developers wonder why they didn’t become a carpenter. But let’s face it: Git is here to stay. And for a small team—like, say, 3-4 developers working on the same codebase—getting your branching strategy right can be the difference between smooth sailing and a storm of merge conflicts that will make you question every decision you’ve ever made in life.

So let’s dive into a “simple” strategy for keeping Git under control. No complex workflows, no corporate jargon—just a few solid, time-tested practices to keep you from drowning in source control hell. Because seriously, git is actually super easy and a thousand times better than all the garbage attempts at source control that came before.

### The Core Branches (Yes, There Are Only Two You Really Need)

If you’re working on a small team, you don’t need to be fancy. Forget about multiple branches for every single thing under the sun—just stick with **`main`** and **feature branches**. That’s it. Keep it simple. We don’t need a thousand different integration branches or some mythical `release` branch. Keep it neat.

- **`main`**: This is your production-ready code. The one branch that should always work, always deployable, and always sacred. No exceptions.
- **Feature branches**: These are where the magic happens. New features, bug fixes, the stuff that makes your app worth using. Each feature gets its own branch. Think of it like a sandbox—do whatever you want there, but don’t drag your mess into `main`.

## Example 1: The Plain Old Feature Branch (The Easy Way)

#### Step-by-Step Workflow:

**1. Create a New Feature Branch**

So, you’re ready to tackle the “super urgent” login page. (Because, obviously, it’s the thing that will single-handedly change the world.) Start by creating a feature branch off of `main`.

**Git Command:**

```
git checkout main           # Get on main first. Always. Always.
git pull origin main         # Update your local main. It's not a suggestion.
git checkout -b feature/login-page  # Create the login page branch. It's happening.
```

Congratulations, you now have a feature branch named `feature/login-page`. You’re officially “working” now.

**2. Do Your Thing**

You know what you need to do here—build the UI, write the logic, cry when it doesn’t work. Just get it done. Don’t forget to commit regularly. Like every time you reach a new milestone. Don’t let that “work in progress” rot sit there uncommitted for days because… well, we all know what happens when you do that.

**Git Command:**

```
git add .                    # Add files. If you're unsure, just add everything.
git commit -m "Add login form UI"  # Commit. It's that simple.
```

**Pro Tip**: Commit early, commit often. Don’t wait until you’ve implemented the moon and then try to remember what you were doing. It’s the little things that kill productivity—and Git conflicts.

**3. Rebase, Not Merge (But Maybe Merge Later)**

Here’s where things get a little spicy. While you’re working on your feature, other people are also doing their thing on their feature branches. Now, normally, this wouldn’t matter. Except that Git has this sneaky habit of merging things you didn’t expect—so you’ll want to keep your branch up-to-date by rebasing it onto `main`.

**Git Command:**

```
git checkout main         # Get on `main` again, because that's your foundation.
git pull origin main       # Get the latest changes from `main`
git checkout feature/login-page  # Back to your feature branch.
git rebase main            # Keep it fresh by rebasing. The idea is to stay ahead.
```

**Important**: If you’re going to rebase, do it **regularly**. Don’t wait until the end of your feature development to rebase. This is where most of your merge conflicts will creep up on you—if you’re not rebasing iteratively, you’ll find yourself with a mess that’ll make a bad divorce look civil.

**Pro Tip**: Rebase often, especially when you’re working in parallel with other people. It keeps your history clean and less of a nightmare when you finally merge.

**4. Open a Pull Request (PR) for Code Review**

Yes, this is still a thing. Even though it’s just a small team, your code still needs a second pair of eyes. A pull request is a great way to get feedback (or to argue why you’re right, because let’s face it, you are). Don’t skip this step.

**GitHub Command (for PR creation)**:

- Go to GitHub (or whichever Git platform you use), and create a PR from `feature/login-page` to `main`.
- Assign reviewers (someone besides you, obviously).

**5. Merge Once Approved**

If the code looks good and has passed your team’s review process, it’s time to merge. Please, for the love of sanity, **squash commits** when merging. Keep that history clean. Git isn’t a place for hundreds of tiny commits like “Fix typo” or “Oops.” It’s a place for logical, meaningful changes.

**Git Command:**

```
git checkout main              # Get on `main`
git pull origin main            # Make sure `main` is up to date
git merge feature/login-page    # Merge that beautiful feature
git push origin main            # Push to the remote
```

**6. Delete the Feature Branch**

You’re done. Move on. Delete the branch. The feature has been merged, and you don’t need that branch hanging around anymore.

**Git Command:**

```
git branch -d feature/login-page  # Local cleanup
git push origin --delete feature/login-page  # Remote cleanup
```

## Example 2: Add `develop` If You’re Feeling Fancy

For those of you who think you need a little extra structure (I mean, you do you), we can throw in a `develop` branch. But let’s be clear: it’s not necessary for small teams unless you plan to add a lot of complexity later on.

The idea here is that `develop` serves as the staging ground before pushing everything to `main`.

**1. Setup the `develop` Branch**

If you’re starting from scratch, create `develop` from `main`. Once it’s there, you can pull from `main` into `develop` whenever needed.

**Git Command:**

```
git checkout main              # On `main`, always.
git pull origin main            # Update `main`
git checkout -b develop         # Create `develop`
git push origin develop         # Push `develop`
```

**2. Create Feature Branches from `develop`**

Any feature branch now gets created from `develop`, not `main`. So go ahead and create your new branches from `develop`.

**Git Command:**

```
git checkout develop            # On develop
git pull origin develop          # Keep `develop` fresh
git checkout -b feature/login-page  # Create a new feature branch
```

**3. Merge Feature Branches into `develop`**

Once your feature is done, instead of merging it into `main` directly, it gets merged into `develop` first.

**Git Command:**

```
git checkout develop            # Switch to develop
git pull origin develop          # Get latest from develop
git merge feature/login-page    # Merge feature
```

**4. Merge `develop` into `main` for Release**

Finally, when everything on `develop` is ready, you merge `develop` into `main` for production release.

**Git Command:**

```
git checkout main               # Switch to main
git pull origin main             # Keep it fresh
git merge develop               # Merge `develop` into `main`
git push origin main            # Push changes
```

### Keeping Your Branches Up to Date (Not Just Once)

Here’s the thing: if you’re **only** rebasing when you’re about to merge, you’re doing it wrong. Rebase your feature branch iteratively. No, seriously. It’s not something you do on the final day before your feature is done. If you’re working on a feature for more than a couple of days, update your branch **regularly**. Keep it fresh, keep it aligned with `main`.

**Git Command for Iterative Rebasing:**

```
git checkout feature/login-page    # Back to your feature branch
git fetch origin                   # Get latest updates
git rebase origin/main              # Rebase onto the updated `main`
```

**Pro Tip**: If you’re working on a big feature, you’ll want to keep rebasing multiple times throughout the development process. Merge conflicts are inevitable, but iterative rebasing minimizes the pain. Don’t wait until your branch is a dozen commits deep and you have a literal battlefield of conflicts to resolve. Merge conflicts suck when you’re dealing with big chunks of code—small, manageable conflicts are much easier to wrangle.

## When Merge Conflicts Happen (And They Will)

Merge conflicts are the reality of any Git workflow. If you’re managing to avoid them, you’re either a wizard or lying. The key here is to keep conflicts small and easy to manage.

#### Example: A Merge Conflict Scenario

Let’s say you’re both working on the same section of code. You modify a function in your branch, and your teammate does the same in theirs. When it’s time to merge, Git will see two different versions of the same function and go, “Nope. You figure this out.”

**What To Do:**

**1. Rebase Your Branch**

Before attempting to merge, always rebase. This brings your branch up to date with `main`, minimizing large-scale conflicts and ensuring you’re working with the latest code.

**Git Command:**

```
git checkout feature/login-page  # Ensure you're on your feature branch
git fetch origin                 # Fetch latest updates from the repo
git rebase origin/main            # Rebase your feature onto `main`
```

**2. Handle the Conflict**
Git will point out the areas of conflict. Open those files, identify the conflict markers (they look like `<<<<<<<`, `=======`, and `>>>>>>>`), and manually decide which version of the code to keep.

**3. Resolve the Conflict**

After you’ve resolved the conflict, remove the conflict markers and commit the changes.

**Git Command:**

```
git add .                    # Stage the resolved files
git rebase --continue         # Continue the rebase after resolving
```

**4. Merge Your Branch (With Confidence)**

Now that you’ve successfully rebased and dealt with conflicts early, you can merge your feature into `main` or `develop` without fear of chaos.

**Git Command:**

```
git checkout main             # Switch to `main`
git merge feature/login-page  # Merge feature into `main`
```

### **Lagniappe: Interactive Rebasing (Because We’re Fancy Like That)**

Sometimes, your Git history could use a little tidying up. Enter **interactive rebasing**. This gem of a tool allows you to rewrite your commit history, squash multiple commits into one, reorder them, or even drop some unnecessary noise.

**Why You Should Care:**

- **Squash commits**: Combine several small, inconsequential commits into one meaningful one. Instead of having a long list of tiny “fix typo” commits, you can merge them into one “Fix typos across multiple files” commit.
- **Reorder commits**: If you realize you want a commit to appear earlier in the history (say, a refactor that should come before a feature implementation), interactive rebasing can handle that.
- **Edit commit messages**: You can also clean up commit messages that, at the time, seemed like a good idea but now, reading them, make you cringe.

**How to do it:**

1. Run the interactive rebase:

```
git rebase -i HEAD~5  # Rebase the last 5 commits
```

2. The editor will open, and you’ll see something like this:

```
pick f7f3f6d Add login form UI
pick 310154e Add form validation
pick 9b1f4fc Fix typo in login form
```

3. You can change `pick` to `squash` (or just `s`), which tells Git to squash commits together. For example:

```
pick f7f3f6d Add login form UI
squash 310154e Add form validation
squash 9b1f4fc Fix typo in login form
```

4. Save and exit. Git will now squash those commits into one.

**The Pro Tip**: Use interactive rebasing for cleaning up your commit history **before** merging to `main` or `develop`. It’ll make you look like a Git rockstar and keep your history from looking like a dumpster fire.

### You’re Welcome

In a small team, Git doesn’t need to be your worst nightmare. Stick to these simple branching practices, and you’ll save yourself countless hours of misery. Keep it to `main`, feature branches, and—if you’re really into over-complicating things—add a `develop` branch. Rebase regularly (and iteratively, please), commit often, and keep your history clean.

Oh, and remember: Git is a tool, not a religion. Don’t let it control your life, but definitely respect it.
