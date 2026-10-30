---
title: ReSharper, The Better Way, Is it Readable?
date: 2008-09-28 17:19:14 +0000
last_modified_at: 2010-09-08 09:56:00 -0700
permalink: /2008/09/28/resharper-the-better-way-is-it-readable/
slug: resharper-the-better-way-is-it-readable
wp_id: 217
original_url: https://compositecode.blog/2008/09/28/resharper-the-better-way-is-it-readable/
categories:
- Uncategorized Bits
tags: []
excerpt: While working through some client application services samples recently I was going through and doing a code review, of myself, to see how or were I might be causing myself duplication, have isolation issues, or am not testing something correctly. As I went through I found this little nugget of curiosity. The code started out …
---

While working through some client application services samples recently I was going through and doing a code review, of myself, to see how or were I might be causing myself duplication, have isolation issues, or am not testing something correctly.  As I went through I found this little nugget of curiosity.  The code started out like this:

```
   1:          public ClientFormsAuthenticationCredentials GetCredentials()
   2:          {
   3:              if (ShowDialog() == DialogResult.OK)
   4:              {
   5:                  return new ClientFormsAuthenticationCredentials(
   6:                      usernameTextBox.Text, passwordTextBox.Text,
   7:                      rememberMeCheckBox.Checked);
   8:              }
   9:              else
  10:              {
  11:                  return null;
  12:              }
  13:          }
```

The “If” in the statement above had the little straight line under it that ReSharper signifies it thinks you should change something.  I then hit Alt-Enter for the ResSharper menu to pop up.  It did and gave me an option for “Replace with ‘return'” and also a “Convert to ‘switch’ statement”.  I decided I’d select the first option, since it was given as the default option, and received the conversion below:

```
   1:          public ClientFormsAuthenticationCredentials GetCredentials()
   2:          {
   3:              return ShowDialog() == DialogResult.OK ? new ClientFormsAuthenticationCredentials(
   4:                                                           usernameTextBox.Text, passwordTextBox.Text,
   5:                                                           rememberMeCheckBox.Checked) : null;
   6:          }
```

There are a few things of note in the code.  First off, there are 7 less lines used.  Second, it doesn’t really seem to be easier to read nor does it layout exactly what is going on.  It almost seems to work against behavior driven development principles.  Last thing I noticed right off is that the formatting, lines, and spacing aren’t to my liking, and I fixed that by hitting a new line at the “new” keyword, did ReSharper’s cleanup code option and got this:

```
   1:          public ClientFormsAuthenticationCredentials GetCredentials()
   2:          {
   3:              return ShowDialog() == DialogResult.OK
   4:                         ?
   5:                             new ClientFormsAuthenticationCredentials(
   6:                                 usernameTextBox.Text, passwordTextBox.Text,
   7:                                 rememberMeCheckBox.Checked)
   8:                         : null;
   9:          }
```

Now we’re back up to 9 lines of code, not like the line count matters.  The second point though, is that it is a little easier to read.  The formatting was also a little bit better.  Overall though, I’m still not sure this is easier to read than the if then else statement above.  One thing I was curious about though, and haven’t checked into further, is what this will compile to.  Does the CLR actually end up with the same compiled code?  At some point I might dig it apart, but for now I know the later examples are the suggested way to do this now, and it does remove code that is redundant (such as the “else” keyword in the first code snippet above).  For now I’ve grown a bit more used to reading the later two examples, but they still just don’t jump out to explain what is going on.

Anybody else have an opinion on these three variances?  Got a favorite?
