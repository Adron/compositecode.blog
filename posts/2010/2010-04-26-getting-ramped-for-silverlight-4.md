---
title: Getting Ramped for Silverlight 4
date: 2010-04-26 09:18:00 +0000
last_modified_at: 2010-07-23 11:40:13 -0700
permalink: /2010/04/26/getting-ramped-for-silverlight-4/
slug: getting-ramped-for-silverlight-4
wp_id: 724
original_url: https://compositecode.blog/2010/04/26/getting-ramped-for-silverlight-4/
categories:
- How-to
tags:
- expression blend
- silverlight
excerpt: Here is a quick walk through of setting up your Silverlight 4 development environment. The first assumed step is that you have Visual Studio 2010 already installed and any appropriate patches. Then download the following in order and install each. Silverlight 4 Tools RC2 for Visual Studio and Silverlight 4 RTW Expression Blend 4 Release …
---

Here is a quick walk through of setting up your [Silverlight](http://www.microsoft.com/silverlight) 4 development environment.  The first assumed step is that you have Visual Studio 2010 already installed and any appropriate patches.  Then download the following in order and install each.

- [Silverlight 4 Tools RC2 for Visual Studio and Silverlight 4 RTW](http://go.microsoft.com/fwlink/?LinkID=177428)
- [Expression Blend 4 Release Candidate](http://go.microsoft.com/fwlink/?LinkId=169446)
- [Silverlight Toolkit](http://silverlight.codeplex.com) – Not necessary, but lots of good bits in this download.
- [WCF RIA Services](http://www.silverlight.net/getstarted/riaservices/) – This is also not necessary, but you should grab it just in case anyway.

Once each of these are installed jump into Visual Studio 2010.  Start a new Silverlight 4 Project by going to File -> New -> Project -> and select the Silverlight Project Templates.  Here you’ll see a new list of projects that are specific to the above listed downloads.

- Silverlight Business Application
- WCF RIA Service Class Library
- Silverlight Unit Test Application

One way to confirm (and what I am going to display here in this entry) Silverlight 4 is installed ok is to select the Silverlight Application Template and start a new project.

![](/images/adronhall.smugmug.com/Software/Project-Tidbits/silverlight4installation/Silverlight-4-001/847618070_Jqt6L-M.png)

On the next screen you will see some of the standard options.  I always go with the ASP.NET MVC Option and with these new installations I am going to select Silverlight 4 (should be selected already) from the drop down and check the Enable WCF RIA Services check box.

![](/images/adronhall.smugmug.com/Software/Project-Tidbits/silverlight4installation/Silverlight-4-002/847618068_W4a9f-M.png)

I also, for good measure, always create a unit test project for the ASP.NET MVC Project that will host the Silverlight Application Project.  When all is setup, the Solutions Explorer should look like what is shown below.

![](/images/adronhall.smugmug.com/Software/Project-Tidbits/silverlight4installation/Silverlight-4-003/847618083_PTYXG-M.png)

Add the following code to the XAML of the MainPage.xaml of the Silverlight Project.

```html
<UserControl x:Class="Silverlight4.MainPage"
    xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation"
    xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
    xmlns:d="http://schemas.microsoft.com/expression/blend/2008"
    xmlns:mc="http://schemas.openxmlformats.org/markup-compatibility/2006"
    mc:Ignorable="d"
    d:DesignHeight="300" d:DesignWidth="400">
    <Grid x:Name="LayoutRoot" Background="White">
        <TextBlock x:Name="textBlockTest" Text="Hello World!" />
    </Grid>
</UserControl>
```

Now execute the project, if all runs well you have installed Silverlight 4 successfully.

![](/images/adronhall.smugmug.com/Software/Project-Tidbits/silverlight4installation/Silverlight-4-004/847618124_QqGEt-M.png)

Bam!  Silverlight 4 ready to go!  I will have more on Silverlight 4 very soon, as I will be starting a project (personal) and blogging it as I work through it.  Also, if you run into any issues I would like to read about them, so please comment.  I had a few issues and also had some design time rendering issues in the VS 2010 IDE when I installed these bits at first.
