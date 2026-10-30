---
title: Windows Azure ASP.NET MVC 2 Role with Silverlight
date: 2010-05-13 06:37:00 -0700
last_modified_at: 2010-07-01 22:00:58 -0700
permalink: /2010/05/13/windows-azure-aspnet-mvc-2-role-with-silverlight/
slug: windows-azure-aspnet-mvc-2-role-with-silverlight
wp_id: 23
original_url: https://compositecode.blog/2010/05/13/windows-azure-aspnet-mvc-2-role-with-silverlight/
categories:
- Cloud Speak
- How-to
tags: []
excerpt: I was working through some scenarios recently with Azure and Silverlight. I immediately decided a quick walk through for setting up a Silverlight Application running in an ASP.NET MVC 2 Application would be a cool project. This walk through I have Visual Studio 2010, Silverlight 4, and the Azure SDK all installed. If you need …
---

I was working through some scenarios recently with [Azure](http://www.microsoft.com/windowsazure) and [Silverlight](http://www.microsoft.com/silverlight).  I immediately decided a quick walk through for setting up a [Silverlight](http://www.microsoft.com/silverlight) Application running in an ASP.NET MVC 2 Application would be a cool project.

This walk through I have Visual Studio 2010, [Silverlight](http://www.microsoft.com/silverlight) 4, and the Azure SDK all installed.  If you need to download any of those go get em? now.

Launch Visual Studio 2010 and start a new project.  Click on the section for cloud templates as shown below.

![](/images/adronhall.smugmug.com/Software/Software-Development/silverlightcloud/PuttingSilverlightInTheCloud/863354116_7xsPU-M.png)

After you name the project, the dialog for what type of Windows Azure Cloud Service Role will display.  I selected ASP.NET MVC 2 Web Role, which adds the MvcWebRole1 Project to the Cloud Service Solution.

![](/images/adronhall.smugmug.com/Software/Software-Development/silverlightcloud/PuttingSilverlightInTheCloud/863353939_D5vat-M.png)

Since I selected the ASP.NET MVC 2 Project type, it immediately prompts for a unit test project.  Because I just want to get everything running first, I will probably be unit testing the Silverlight and just using the MVC Project as a host for the Silverlight for now, and because I would prefer to just add the unit test project later, I am going to select no here.

![](/images/adronhall.smugmug.com/Software/Software-Development/silverlightcloud/PuttingSilverlightInTheCloud/863354002_Q7qCV-M.png)

Once you’ve created the ASP.NET MVC 2 project to host the [Silverlight](http://www.microsoft.com/silverlight), then create another new project.  Select the [Silverlight](http://www.microsoft.com/silverlight) section under the Installed Templates in the Add New Project dialog.  Then select [Silverlight](http://www.microsoft.com/silverlight) Application.

![](/images/adronhall.smugmug.com/Software/Software-Development/silverlightcloud/PuttingSilverlightInTheCloud/863422908_3YYC9-M.png)

The next dialog that comes up will inquire about using the existing ASP.NET MVC Application I just created, which I do want it to use that so I leave it checked.  The options section however I do not want to check RIA Web Services, do not want a test page added to the project, and I want [Silverlight](http://www.microsoft.com/silverlight) debugging enabled so I leave that checked.  Once those options are appropriately set, just click on OK and the Silverlight Project will be added to the overall solution.

![](/images/adronhall.smugmug.com/Software/Software-Development/silverlightcloud/PuttingSilverlightInTheCloud/863422937_zHEXX-M.png)

The next steps now are to get the [Silverlight](http://www.microsoft.com/silverlight) object appropriately embedded in the web page.  First open up the Site.Master file in the ASP.NET MVC 2 Project located under the Veiws/Shared/ location.  After you open the file review the content of the <header></header> section.  In that section add another <contentplaceholder></contentplaceholder> tag as shown in the code snippet below.

```html
<head runat="server">

    <link rel="stylesheet" type="text/css" href="../../Content/Site.css" />
    <asp:contentplaceholder id="HeaderContent" runat="server">  </asp:contentplaceholder>
```

i usually put it toward the bottom of the header section.  it just seems the <title></title> should be on the top of the section and i like to keep it that way.

now open up the index.aspx page under the asp.net mvc 2 project located in the views/home/ directory.  when you open up that file add a <asp:content><asp:content> tag as shown in the next snippet.

```html
<asp:content id="content1" runat="server" contentplaceholderid="titlecontent">
    home page </asp:content>   <asp:content id="headercontent" runat="server" contentplaceholderid="headercontent">   </asp:content>   <asp:content id="content2" runat="server" contentplaceholderid="maincontent">
    <h2>&lt;%= html.encode(viewdata[&quot;message&quot;]) %&gt;</h2>
    <p>
        to learn more about asp.net mvc visit <a title="ASP.NET MVC Website" href="http://asp.net/mvc">http://asp.net/mvc</a>. </p></asp:content>
```

In that center tag, I am now going to add what is needed to appropriately embed the [Silverlight](http://www.microsoft.com/silverlight) obj object into the page.  The first thing I needed is a reference to the Silverlight.js file.

```html
<script type="text/javascript" src="Silverlight.js"></script>
```

After that comes a bit of nitty gritty Javascript.  I create another tag (and for those in the know, this is exactly like the generated code that is dumped into the \*.html page generated with any Silverlight Project if you select to "add a test page that references the application".  The complete Javascript is below.

```csharp
function onSilverlightError(sender, args) {
    var appSource = &quot;&quot;;
    if (sender != null &amp;&amp; sender != 0) {
        appSource = sender.getHost().Source;
    }   var errorType = args.ErrorType;
    var iErrorCode = args.ErrorCode;   if (errorType == &quot;ImageError&quot; || errorType == &quot;MediaError&quot;) {
        return;
    }   var errMsg = &quot;Unhandled Error
            in Silverlight Application &quot; + appSource + &quot;\n&quot;;   errMsg += &quot;Code: &quot; + iErrorCode + &quot; \n&quot;;
    errMsg += &quot;Category: &quot; + errorType + &quot; \n&quot;;
    errMsg += &quot;Message: &quot; + args.ErrorMessage + &quot; \n&quot;;   if (errorType == &quot;ParserError&quot;) {
        errMsg += &quot;File: &quot; + args.xamlFile + &quot; \n&quot;;
        errMsg += &quot;Line: &quot; + args.lineNumber + &quot; \n&quot;;
        errMsg += &quot;Position: &quot; + args.charPosition + &quot; \n&quot;;
    }
    else if (errorType == &quot;RuntimeError&quot;) {
        if (args.lineNumber != 0) {
            errMsg += &quot;Line: &quot; + args.lineNumber + &quot; \n&quot;;
            errMsg += &quot;Position: &quot; + args.charPosition + &quot; \n&quot;;
        }
        errMsg += &quot;MethodName: &quot; + args.methodName + &quot; \n&quot;;
    }   throw new Error(errMsg);
}
```

I literally, since it seems to work fine, just use what is populated in the automatically generated page.  After getting the appropriate Javascript into place I put the actual Silverlight Object Embed code into the HTML itself.  Just so I know the positioning and for final verification when running the application I insert the embed code just below the Index.aspx page message.  As shown below.

```html
<asp:content id="Content2" runat="server" contentplaceholderid="MainContent">
    <h2>
        &lt;%= Html.Encode(ViewData[&quot;Message&quot;]) %&gt;</h2>
    <p>
        To learn more about ASP.NET MVC visit <a title="ASP.NET MVC Website" href="http://asp.net/mvc">http://asp.net/mvc</a>. </p><div id="silverlightControlHost">
        <object data="data:application/x-silverlight-2," type="application/x-silverlight-2"
            width="100%" height="100%">
            <param name="source" value="ClientBin/CloudySilverlight.xap" />
            <param name="onError" value="onSilverlightError" />
            <param name="background" value="white" />
            <param name="minRuntimeVersion" value="4.0.50401.0" />
            <param name="autoUpgrade" value="true" />
            <a href="http://go.microsoft.com/fwlink/?LinkID=149156&amp;v=4.0.50401.0" style="text-decoration: none">
                <img src="http://go.microsoft.com/fwlink/?LinkId=161376" alt="Get Microsoft Silverlight" style="border-style:
            none" />
            </a>
        </object><iframe style="border-right-width: 0px; width: 0px; border-top-width: 0px; border-bottom-width: 0px; height: 0px; visibility: hidden; border-left-width: 0px" id="_sl_historyFrame"></iframe></div></asp:content>
```

I then open up the [Silverlight](http://www.microsoft.com/silverlight) Project MainPage.xaml.  Just to make it visibly obvious that the [Silverlight](http://www.microsoft.com/silverlight) Application is running in the page, I added a button as shown below.

```html
&lt;?XML:NAMESPACE PREFIX = [default] http://schemas.microsoft.com/winfx/2006/xaml/presentation NS = &quot;http://schemas.microsoft.com/winfx/2006/xaml/presentation&quot; /&gt;<usercontrol xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation" d:designwidth="400" d:designheight="300" mc:ignorable="d" xmlns:mc="http://schemas.openxmlformats.org/markup-compatibility/2006" xmlns:d="http://schemas.microsoft.com/expression/blend/2008" xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml" x:class="CloudySilverlight.MainPage">   <grid background="White" x:name="LayoutRoot">
        <button name="button1" click="button1_Click" width="75" verticalalignment="Top" margin="48,40,0,0" horizontalalignment="Left" height="23" content="Button">
    </grid>
</usercontrol>
```

Just for kicks, I added a message box that would popup, just to show executing functionality
also.

```csharp
private void button1_Click(object sender, RoutedEventArgs e)
{
    MessageBox.Show(&quot;It runs in the cloud!&quot;);
}
```

I then executed the ASP.NET MVC 2 and could see the Silverlight Application in page.  With a quick click of the button, I got a message box.  Success!ight 4, and the latest Azure
SDK, this is actually a ridiculously easy process.

Navigate to the Azure Cloud Services web site.

![](/images/adronhall.smugmug.com/Software/Software-Development/silverlightcloud/PuttingSilverlightInTheCloud/864591375_ujQxq-M.png)

Once that is open go back in Visual Studio and right click on the cloud project
and select publish.

![](/images/adronhall.smugmug.com/Software/Software-Development/silverlightcloud/PuttingSilverlightInTheCloud/864591759_pBgJm-M.png)

This will publish two files into a directory.  Copy that directory so you can
easily paste it into the Azure Cloud Services web site.  You’ll have to click
on the application role in the cloud (I will have another blog entry soon about
where, how, and best practices in the cloud).

![](/images/adronhall.smugmug.com/Software/Software-Development/silverlightcloud/PuttingSilverlightInTheCloud/864591430_YNNAi-M.png)

In the text boxes shown, select the application package file and the configuration
file and place them in the appropriate text boxes.  This is the part were it
comes in handy to have copied the directory path of the file location.  That
way when you click on browser you can just paste that in, then hit enter.  The two files will be listed and you can select the appropriate file.

Once that is done, name the service deployment.  Then click on publish.  After a minute or so you will see the following screen.

![](/images/adronhall.smugmug.com/Software/Software-Development/silverlightcloud/PuttingSilverlightInTheCloud/864591448_hv6Di-M.png)

Now click on run.  Once the MvcWebRole1 goes green (the little light symbol
to the left of the status) click on the Web Site URL.  Be patient during this
process too, it could take a minute or two.  The [Silverlight](http://www.microsoft.com/silverlight) application should again come up just like you
ran it on your local machine.

Once staging is up and running, click on the circular icon with two arrows to move
staging to production.  Once you are done make sure the green light is again
go for the production deploy, then click on the Web Site URL to verify the site
is working.  At this point I had a successful development, staging, and production
deployment.

Thanks for reading, hope this was helpful.  I have more Windows Azure and other
cloud related material coming, so stay tuned.
