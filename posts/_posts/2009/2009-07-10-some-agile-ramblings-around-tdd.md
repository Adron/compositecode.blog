---
title: Some Agile Ramblings Around TDD
date: 2009-07-10 18:01:46 -0700
last_modified_at: 2009-07-10 18:01:46 -0700
permalink: /2009/07/10/some-agile-ramblings-around-tdd/
slug: some-agile-ramblings-around-tdd
wp_id: 654
original_url: https://compositecode.blog/2009/07/10/some-agile-ramblings-around-tdd/
categories:
- Uncategorized Bits
tags: []
excerpt: Got a question recently, from multiple people regarding test driven development. One simply asked why TDD is not the standard (as in way to develop). Another person asked me how spending more time writing tests speeds things up over time. Well, I will cover a bit of that real quick and try to explain my …
---

Got a question recently, from multiple people regarding test driven development.  One simply asked why TDD is not the standard (as in way to develop).  Another person asked me how spending more time writing tests speeds things up over time.  Well, I will cover a bit of that real quick and try to explain my 2 cents on the whole practice.

What is test driven development?  The practice entails developing a test, which fails (because obviously you?ve written it first).  Once you have written the test you then create the initial skeleton that will get that test to pass.  Here is a crude a basic example.  I am using [NUnit](http://www.nunit.org/) for these examples, so if you don’t have it, go get it or whatever your test framework of choice is.

First you write the test which will fail.  Also known as getting the "red light".

```
    [TestFixture]
    public class RamblingsTests
    {
        [Test]
        public void InstantiateRambling()
        {
            Rambling rambling = new Rambling("I'm talking here and all.");
            Assert.IsNotNull(rambling);
        }
    }
```

.csharpcode, .csharpcode pre
{
font-size: small;
color: black;
font-family: consolas, “Courier New”, courier, monospace;
background-color: #ffffff;
/\*white-space: pre;\*/
}
.csharpcode pre { margin: 0em; }
.csharpcode .rem { color: #008000; }
.csharpcode .kwrd { color: #0000ff; }
.csharpcode .str { color: #006080; }
.csharpcode .op { color: #0000c0; }
.csharpcode .preproc { color: #cc6633; }
.csharpcode .asp { background-color: #ffff00; }
.csharpcode .html { color: #800000; }
.csharpcode .attr { color: #ff0000; }
.csharpcode .alt
{
background-color: #f4f4f4;
width: 100%;
margin: 0em;
}
.csharpcode .lnum { color: #606060; }

Next you flesh out the actual class, which if you have the appropriate refactoring tools and awesome stuff like [ReSharper](http://www.jetbrains.com/resharper/index.html) takes about 5 seconds ? literally.

```
    public class Rambling
    {
        public Rambling(string s)
        {
            throw new NotImplementedException();
        }
    }
```

.csharpcode, .csharpcode pre
{
font-size: small;
color: black;
font-family: consolas, “Courier New”, courier, monospace;
background-color: #ffffff;
/\*white-space: pre;\*/
}
.csharpcode pre { margin: 0em; }
.csharpcode .rem { color: #008000; }
.csharpcode .kwrd { color: #0000ff; }
.csharpcode .str { color: #006080; }
.csharpcode .op { color: #0000c0; }
.csharpcode .preproc { color: #cc6633; }
.csharpcode .asp { background-color: #ffff00; }
.csharpcode .html { color: #800000; }
.csharpcode .attr { color: #ff0000; }
.csharpcode .alt
{
background-color: #f4f4f4;
width: 100%;
margin: 0em;
}
.csharpcode .lnum { color: #606060; }

Now when we run this we can see it fail.

[![](/images/adronhall.smugmug.com/photos/587705635_Gzrds-M.png)](http://adronhall.smugmug.com/gallery/8866692_eEytQ#587705635_Gzrds)

Of course to get the test to pass, we simply can get rid of the exception being thrown!  So I do that next and we get a nice green light.

Now the class is pretty useless, so I will add a simple feature next.  But I will follow true TDD style practice.  I will not just whack some code onto the object, we’ll immediately lose the effectiveness of TDD if we just break the process and start cramming code, no matter how small, into the class we’ve just created.  So I have a test instead;

```
    [Test]
    public void ConfirmRamblingIsRambled()
    {
        Rambling rambling = new Rambling("More rambling is occurring here.");
        Assert.IsNotEmpty(rambling.Text);
    }
```

.csharpcode, .csharpcode pre
{
font-size: small;
color: black;
font-family: consolas, “Courier New”, courier, monospace;
background-color: #ffffff;
/\*white-space: pre;\*/
}
.csharpcode pre { margin: 0em; }
.csharpcode .rem { color: #008000; }
.csharpcode .kwrd { color: #0000ff; }
.csharpcode .str { color: #006080; }
.csharpcode .op { color: #0000c0; }
.csharpcode .preproc { color: #cc6633; }
.csharpcode .asp { background-color: #ffff00; }
.csharpcode .html { color: #800000; }
.csharpcode .attr { color: #ff0000; }
.csharpcode .alt
{
background-color: #f4f4f4;
width: 100%;
margin: 0em;
}
.csharpcode .lnum { color: #606060; }

Running that fails so immediately I will add the code to get a good green light.

```
    public class Rambling
    {
        public Rambling(string s)
        {
            Text = s;
        }

        public string Text { get; set; }
    }
```

.csharpcode, .csharpcode pre
{
font-size: small;
color: black;
font-family: consolas, “Courier New”, courier, monospace;
background-color: #ffffff;
/\*white-space: pre;\*/
}
.csharpcode pre { margin: 0em; }
.csharpcode .rem { color: #008000; }
.csharpcode .kwrd { color: #0000ff; }
.csharpcode .str { color: #006080; }
.csharpcode .op { color: #0000c0; }
.csharpcode .preproc { color: #cc6633; }
.csharpcode .asp { background-color: #ffff00; }
.csharpcode .html { color: #800000; }
.csharpcode .attr { color: #ff0000; }
.csharpcode .alt
{
background-color: #f4f4f4;
width: 100%;
margin: 0em;
}
.csharpcode .lnum { color: #606060; }

Now there is a class, that can be instantiated by passing a string parameter in, and the parameter is then assigned to the Text property which can be retrieved after instantiation.

What else do we have?  We also have immediate regression if any changes are made.  We have the confidence that we know each part works & that nothing got *fat fingered* in.  Now let us imagine we had to do a bit of editing to the Rambling instantiation so that some business logic occurs after the text is passed in as a parameter.  In other words, we’ll imagine we have a refactor or *change requirement* to make.

Let us say we wanted to check and make sure there was always going to be at least a period on the end of any Ramble’s Text property.  Now of course that is super easy but don’t go messing the flow up and adding the functionality yet, first add a test.

```
        [Test]
        public void ConfirmRambleHasPunctuation()
        {
            Rambling rambling = new Rambling("Another rambling ramble.");
            Assert.IsTrue(rambling.Text.EndsWith("."));
        }

        [Test]
        public void ConfirmRambleGetsPunctuation()
        {
            Rambling rambling = new Rambling("Another typing rambling ramble");
            Assert.IsTrue(rambling.Text.EndsWith("."));
        }
```

.csharpcode, .csharpcode pre
{
font-size: small;
color: black;
font-family: consolas, “Courier New”, courier, monospace;
background-color: #ffffff;
/\*white-space: pre;\*/
}
.csharpcode pre { margin: 0em; }
.csharpcode .rem { color: #008000; }
.csharpcode .kwrd { color: #0000ff; }
.csharpcode .str { color: #006080; }
.csharpcode .op { color: #0000c0; }
.csharpcode .preproc { color: #cc6633; }
.csharpcode .asp { background-color: #ffff00; }
.csharpcode .html { color: #800000; }
.csharpcode .attr { color: #ff0000; }
.csharpcode .alt
{
background-color: #f4f4f4;
width: 100%;
margin: 0em;
}
.csharpcode .lnum { color: #606060; }

.csharpcode, .csharpcode pre
{
font-size: small;
color: black;
font-family: consolas, “Courier New”, courier, monospace;
background-color: #ffffff;
/\*white-space: pre;\*/
}
.csharpcode pre { margin: 0em; }
.csharpcode .rem { color: #008000; }
.csharpcode .kwrd { color: #0000ff; }
.csharpcode .str { color: #006080; }
.csharpcode .op { color: #0000c0; }
.csharpcode .preproc { color: #cc6633; }
.csharpcode .asp { background-color: #ffff00; }
.csharpcode .html { color: #800000; }
.csharpcode .attr { color: #ff0000; }
.csharpcode .alt
{
background-color: #f4f4f4;
width: 100%;
margin: 0em;
}
.csharpcode .lnum { color: #606060; }

I’ve written two tests above.  It might seem silly or excessive in this scenario, but think if this was some serious heavy duty business logic that had all types of processing going on.  You would want to check more than just one or two scenarios and at least cover most of what one might think up.  Of course Quality Assurance hits the outliers, but no developer should ever be submitting code to QA that has stupid bugs ? ESPECIALLY if it can be resolved via TDD or even test after development.  EVERYONE should be writing tests for their code ? even if they end up not quite meeting the standards of isolated, testable units ? write tests!  When you get into the practice, getting them into isolated testable units gets easier and easier.  So we’ve got two tests now to confirm that the Text Property will end with a period even if the instantiation string parameter isn’t passed with any.

Here is the addition to the code to get green lights on both tests.

```
    public class Rambling
    {
        public Rambling(string s)
        {
            if(!s.EndsWith("."))
                s += ".";
            Text = s;
        }

        public string Text { get; set; }
    }
```

.csharpcode, .csharpcode pre
{
font-size: small;
color: black;
font-family: consolas, “Courier New”, courier, monospace;
background-color: #ffffff;
/\*white-space: pre;\*/
}
.csharpcode pre { margin: 0em; }
.csharpcode .rem { color: #008000; }
.csharpcode .kwrd { color: #0000ff; }
.csharpcode .str { color: #006080; }
.csharpcode .op { color: #0000c0; }
.csharpcode .preproc { color: #cc6633; }
.csharpcode .asp { background-color: #ffff00; }
.csharpcode .html { color: #800000; }
.csharpcode .attr { color: #ff0000; }
.csharpcode .alt
{
background-color: #f4f4f4;
width: 100%;
margin: 0em;
}
.csharpcode .lnum { color: #606060; }

Now we have 4 green lights.  Life is good and our code is tested.

[![](/images/adronhall.smugmug.com/photos/587705652_ctjdx-O.png)](http://adronhall.smugmug.com/gallery/8866692_eEytQ#587705652_ctjdx)

I have a really hard time why some developers seem to just not test their code.  Sometimes it is the management, sometimes other work environment issues, but as for core functional legitimate reasons I can’t find any to not write unit tests.

Some people have brought up not needing to write tests for code that works based solely off of configuration settings, such as from a Web.Config, and I can agree with that.  At most, write a test to verify you’re prepared for a configuration setting not being available that you think might be.  Beyond that, no point in going over ground already traversed – one would hope – with thorough QA and respective resources.

**Time Consumption Issues**

Now as some of you, especially if you worked through these examples, or even wrote up some of your own you will have noticed that it took more time than if you just wrote the code.  Yeah, on this insanely easy, kindergarten example it did take more time.  But seriously, think about it for a minute, when you’re in the heat of coding (especially if you aren’t paired up) will you actually catch each little mistake?  Maybe during the build of the code, maybe afterwards you might.  Will you actually not miss every single detail and be absolutely sure you get every business rule and detail into the logic?  I would not put trust in anyone to do so.  After 12+ years of software development, I have yet to see someone write code well if they aren’t testing the hell out of it at the same time.  The cleanest, fastest, most well organized code I have ever seen has come from developers working within the TDD mindset & process.  The only individuals I have ever seen produce better code are developers that pair program.

?but I am not going to go into the pair programming paradigm, that is for another entry another day.

TDD drastically increases the quality and integrity of your code.  With higher quality you do not have to take as many steps to refactor, you do not worry as much about quality once the practice is in your head.  The quality comes from the refactorings you do commit and improvements only go up from there.  Using TDD you will eventually find, no matter how hard headed one is in the beginning, that you will vastly increase your code quality and significantly decrease you’re actual post writing QA bugs, rewrites, and all those other assorted annoyances than a good developer should keep minimized.

As for the project planners, it might seem like it takes a while to write tests, but when you see those QA cycles shorten, the code quality increase, and eventually ? yes, I promise ? the legitimate velocity of development increase and then ? drum roll please ? sustain, you’ll be thankful that you or your developers in the team are practicing TDD.

I personally, can barely imagine a world in which I skip tests.  I’ve honestly tried in the past couple years a couple times to stop testing ? just to have a flashback to when I started coding ya know 😉 – and have ended up providing a prime example why you do ***NOT*** skip unit testing.  Unfortunately I wasn’t prepared for the first failure from not testing, and it took the second "I command you not to test cuz it’s ruining my project plan" bull shit to be prepared to basically test anyway and then show how the non-tested code doesn’t hold up against the unit tested code base.

There are of course pitfalls, and a lot of them, as with anything and developers have to work diligently to avoid them.  At some time in the future I’ll elaborate on those also.  For now I’m going to jump from this and into my thoughts on why some environments do not test still, even with the ever growing mountain of evidence that you’re insane not to.

**Fear and Courage**

Unfortunately most development teams have, if they are EXTREMELY lucky, at least one super motivated and above average developer.  Once in a very rare time a team will have 2 or more.  But if the team has average, weak, or super strong developers no matter testing should be done.  Even if one is just out of college and not really a strong developer yet, they can still take the torch and push for good practices.  This is where the big question comes for any developer no matter what level ? ***do they have the courage?*** The fear often overrides one’s ability to step up and get testing put into practice among a team.  Above all, step up and have the courage.

Anyway, that’s all the writing I have for the topic right now, got some [#strangelovelive](http://www.livestream.com/strangelovelive) to watch and some code to hack out.  Hope this provides some insight into the issues & problems in getting good TDD practice kick started in a development environment among a team.  I’ll definitely have a lot more to say soon as I’ve routinely been joining more and more conversations regarding the [Agile](http://en.wikipedia.org/wiki/Agile_software_development) and specifically the TDD practice.
