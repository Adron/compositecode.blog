---
title: Unbreaking Python Through Virtual Environments
date: 2019-12-25 11:16:21 -0800
last_modified_at: 2020-04-16 09:16:44 -0700
permalink: /2019/12/25/unbreaking-python-through-virtual-environments/
slug: unbreaking-python-through-virtual-environments
wp_id: 16635
original_url: https://compositecode.blog/2019/12/25/unbreaking-python-through-virtual-environments/
categories:
- python
tags:
- beginners
- programming
- python
- tutorial
- virtualenv
excerpt: I wrote some days ago a post “Getting Started With Python Right!“. In this post I wrote about what I’d found to be the best way to setup MacOS for Python development. In it I also added links and a few details to get a Windows or Linux machine setup right for Python development. However, …
image: /wp-content/uploads/2019/12/thrashing-code-python.jpg
---

I wrote some days ago a post “[Getting Started With Python Right!](/2019/12/23/getting-started-with-python-right/)“. In this post I wrote about what I’d found to be the best way to setup MacOS for Python development. In it I also added links and a few details to get a Windows or Linux machine setup right for Python development.

However, there’s more, as [@tlockney (Thomas Lockney)](https://twitter.com/tlockney) pointed out in a comment! He detailed,

> 1. Since you’re using pyenv, the version of pip you use should always be the one associated with the current version of Python, which won’t be the case when you later switch versions.
> 2. People who aren’t clear on what’s going on will likely copy the code you included verbatim, so instead of aliasing the version of pip referenced in the pyenv path, it’s going to always point at the brew installed version.
> 3. You really should use virtualenv for pretty much everything and try to avoid ever installing libraries into your global Python environment. If you need tools accessible outside a virtualenv, check out pipx.

The tool I was using in that previous post `pyenv` does several things:

- The ability to change the global Python version on a per-user basis.
- Provide support for per-project Python versions.
- Allow override of the Python version with an environment variable.
- Search command for multiple Python versions at a time.

It appears, that `pyenv` should take care of what I need to have done. But as Thomas points out the version of pip gets out of sync with pyenv depending on use when versions are switched. He then pointed out that the pip being referenced will be out of sync with the installed brew version. Finally, that `virtualenv` could be used for everything and avoid installing libraries into the global Python environment.

So what does `virtualenv` do exactly? This tool sets up a project by creating an isolated project specific environment. This way versions, modules, and related elements of the Python stack don’t conflict with other projects that may require different versions or modules.

Now, with the normal oddities of Python environments this tool, like Homebrew, installs pip also. But one can also use pip to install virtualenv. As with most modules, additions, and related things in Python there’s always something to conflated in setup and use in the environment. For example, and for completeness, let’s review some specific warnings for use of virtualenv. These warnings are even listed in the docs called out at the top of the [installation steps](https://virtualenv.pypa.io/en/latest/installation/). I’ve paraphrased them, for completeness, in short.

1. Use virtualenv-1.9 or greater.
2. Advise against pip 1.3.

If the steps were followed from the previous article, then the environment is in good shape. To get virtualenv installed issue the following install request with pip.

## Step 1 Install virtualenv

```
pip install virtualenv
```

From there, `virtualenv` is ready to use to setup environments. The basic command is

## Step 2 Setup a New Environement

```
virtualenv <dir>
```

where `<dir>` is the directory to setup an environment in. Issue the command against a directory and the results will display the following results.

```
$ virtualenv python-env-examples
Using base prefix '/Users/adron/.pyenv/versions/3.7.3'
New python executable in /Users/adron/Codez/python-env-examples/bin/python3.7
Also creating executable in /Users/adron/Codez/python-env-examples/bin/python
Installing setuptools, pip, wheel...
done.
```

Once this is done, that provides the following capabilities for the environment.

- `/python-env-examples/lib` and `/python-env-examples/include` now exist and contain libs for the environment, with `/python-env-examples/lib/pythonX.X/site-packages` being the location that will now receive any packages that are installed to the environment.
- a `bin` directory is created for executables to live including a new python executable. We can even use this directory’s path to run a script by issuing `/python-env-examples/bin/python` or use the specific environment for a `pip install`. Check the specific versions in that directory with `python --version` and `pip -V` to determine what version is setup in that particular environment. This also can be used to determine the difference between the system Python that is setup versus the specific environment.

That’s a lot and a bit cumbersome to understand at first glance. This now provides a clean virtual environment based on a singular directory as root in which to work in. It’s a great idea to navigate around and explore all the pieces that are setup in the directory. One could almost think of this virtual environment like it’s a Docker container. An isolated, stand alone environment in which to run Python tooling.

## Step 3 Activate The Environment

The final step I’ll discuss is activating the environment. To do this I navigate to /python-env-examples/bin and source the `activate` script. It is important to choose the right activate script for your operating system. A list against the `bin` directory and we can see the other options available.

```
> ls
activate         activate.ps1     easy_install     pip3             python-config    wheel
activate.csh     activate.xsh     easy_install-3.7 pip3.7           python3
activate.fish    activate_this.py pip              python           python3.7
```

The activate.ps1 is for powershell, there are other options for various shell options for different operating systems here. Along with the pip and python versions. For my use, I’m going to `source ./activate`.

```
source ./activate
```

Now if `python --version` and `which python` is executed the version and path is of the version of Python used in the `virtualenv` setup environment. This can be extremely useful on Windows or if you want to run an environment completely autonomous of any pre-installed or non-existing environments.

Let’s say you’ve done this but still want the system Python, just simply deactive the setup. To do this run the deactivate script. There shouldn’t be any reason to source this file, just run it as shown.

```
deactivate
```

Now we’re ready to run some Python and have adequate management options for the environments to run that code in. Enjoy!
