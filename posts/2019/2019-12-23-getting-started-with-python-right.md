---
title: Getting Started With Python Right!
date: 2019-12-23 16:29:09 -0800
last_modified_at: 2020-04-16 09:16:51 -0700
permalink: /2019/12/23/getting-started-with-python-right/
slug: getting-started-with-python-right
wp_id: 16632
original_url: https://compositecode.blog/2019/12/23/getting-started-with-python-right/
categories:
- python
tags:
- beginners
- programming
- python
- tutorial
excerpt: I’ve gone through a gazillion ways to setup Python, ensure I’ve gotten the right version installed on MacOS. This is a quick guide I’ve put together if you’re getting started or looking at a more defacto set way to get it installed. I’ve added links for Linux and Windows too, but specifically cover MacOS in this post.
image: /wp-content/uploads/2019/12/thrashing-code-python.jpg
---

> [UPDATE POST](/2019/12/25/unbreaking-python-through-virtual-environments/) Added details about virtualenv to complement this post, per Thomas’ comment in the comments section below! Read this post for MacOS specific system Python setup, then read that for more options on how to set things up right!

Recently I sat down to get started on some Python work, specifically on MacOS. I’ve written code in Python before and tried out 2.x and 3.x before. I’m going with 3.x for this and upcoming articles but one thing became apparent. The Python tech stack is still ferociously fragmented in a number of ways, and this post is to provide some clarity if this is your first endeavor into the stack.

First off, 2.7 and 3.8 are the versions that exist in some state as the *latest versions*. 2.7 is obviously not the latest but is still installed, coded in, and used in a vast number of projects where Python is used. On MacOS for example, it’s the default still, and it should be left alone and the latest installed with appropriate Python environment, PIP for dependency, and related ecosystem necessities. As I walk through these steps, that’s important to know.

Whatever the system environment starting, check out what is on the machine. If on Windows, it’s safe to bet there is nothing on the machine. On Linux or MacOS there will be some version of Python already installed. Running `python --version` to determine which version of the language is installed.

If you have a version you can then check out `which python` to figure out where it is installed. This can come in handy if things get a bit confusing, or verifying where the install is currently setup or pointing to within the file structure.

## First Step: Get a tool to install Python

On MacOS get [brew](https://brew.sh/) before doing anything else. For details on Windows check out the [docs here](https://docs.python.org/3/using/windows.html). There’s also a great Digital Ocean post by Lisa Tagliaferri “[How to Install python 3 and Set Up a Local Programming Environment on Windows 10](https://www.digitalocean.com/community/tutorials/how-to-install-python-3-and-set-up-a-local-programming-environment-on-windows-10)” if you’re installig Python 3 on Windows 10. For Linux specifically check out these [docs](https://docs.python.org/3/using/unix.html).

Once brew is installed issue the command to install the “Simple Python Version Management” [pyenv](https://github.com/pyenv/pyenv). If this app gives flashbacks to Ruby, it is indeed forked from [rbenv](https://github.com/rbenv/rbenv) so there’s that.

```
brew install pyenv
```

## Second Step: Install the Latest Python

With pyenv install a sepcific version of Python with the following command.

```
pyenv install 3.8.0
```

If there is a new version, install that version instead. On MacOS there is also, of course, already version 2.7 but with pyenv it’ll get the appropriate pieces remapped so that this latest can become the defacto used Python version to work with. To get pyenv to setup this latest installed version us the CLI to set it as the global Python.

```
pyenv global 3.8.0
```

One final step to ensure pyenv can be used when and where necessary, now and ongoing in development needs, set the following in your .zshrc.

```
echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n  eval "$(pyenv init -)"\nfi' >> ~/.zshrc
```

If you’re using bash still, make the change accordingly to your `~/.bash_profile`.

```
echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n  eval "$(pyenv init -)"\nfi' >> ~/.bash_profile
```

## Third Step: Get PIP Installed.

To check the version of `pip` run `pip -V`. This command not only shows you which version of pip is installed, but also what version of Python pip is installed to oeprate on (with/on/at/to??). The command and result would look something like this.

```
pip -V
pip 19.0.3 from /Users/adron/.pyenv/versions/3.7.3/lib/python3.7/site-packages/pip (python 3.7)
```

Technically, when brew (Homebrew) installed the latest Python has also installed pip and it should be mapped accordingly as shown above in the `pip -V` command. However this can be set correctly if it isn’t mapped already. Get the path where pip3 is installed by issuing a which command.

```
which pip3
```

The path returned, likely `/usr/local/bin/pip3`, add it to a command to echo it into the startup script of your choice. For example, to add it to the zshrc file.

```
echo "alias pip=/usr/local/bin/pip3" >> ~/.zshrc
```

If using bash add it as such.

```
echo "alias pip=/usr/local/bin/pip3" >> ~/.bash_profile
```

## Fourth Step: Run Some Python Code!

Alright, now that this is done, let’s run some actual Python code and make sure things are installed and setup correctly. For this I created a directory I simply called `python-examples.py`. Then added the first line of code, a simple print statement.

```python
print("Hello World! BOOM!")

print("These examples point out how these variables can be declared and printed.")
```

Executing that, just by executing the file `python python_examples.py` and the following results display.

```
Hello World! BOOM!
These examples point out how these variables can be declared and printed.
```

Alright, with that confirmed, we’re all set for further Python development! Enjoy!

#### References:

- [Python Docs](https://docs.python.org/3/)
- [Python v3 Tutorial](https://docs.python.org/3/tutorial/index.html)
- Not discussed here, but I love the JetBrains IDE’s, and they’ve got one for Python called [PyCharm](https://www.jetbrains.com/pycharm/).
- More details about setting up and other ways to put things together by Matthew Broberg [@mbbroberg](https://twitter.com/mbbroberg) and Moshe Zadka [@moshezadka](https://twitter.com/moshezadka) in the post “[The Right and Wrong Way to Set Python 3 as Default on the Mac](https://opensource.com/article/19/5/python-3-default-mac)“.

My Blog! I have a personal blog at [https://compositecode.blog/](/) that you can also subscribe to where I post additional collected material, thoughts, music, meetups, conferences, videos (like [Twitch](https://twitch.tv/adronhall/)), open source projects, database work, data science, and much more.
