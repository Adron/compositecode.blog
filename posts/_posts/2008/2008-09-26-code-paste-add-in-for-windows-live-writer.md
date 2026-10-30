---
title: Code Paste Add In for Windows Live Writer
date: 2008-09-26 04:54:40 -0700
last_modified_at: 2012-09-24 19:15:53 -0700
permalink: /2008/09/26/code-paste-add-in-for-windows-live-writer/
slug: code-paste-add-in-for-windows-live-writer
wp_id: 219
original_url: https://compositecode.blog/2008/09/26/code-paste-add-in-for-windows-live-writer/
categories:
- .NET Bits
- How-to
tags: []
excerpt: UPDATED 10/25/2008 Code Sections Formatting Fixed With CSS What I’m using is available Plugin Collection for Windows Live Writer on Codeplex. This comes in real useful when getting code into a blog entry. Because straight pasting really doesn’t do so well for readability. So here are my test code pastes. A basic view in C#. …
---

*[**UPDATED 10/25/2008 Code Sections Formatting Fixed With CSS**](http://www.adronbhall.com/blogs/technology__software_development/post/2008/10/25/Code-Sections-Formatting-Fixed-With-CSS.aspx)*

What I’m using is available [Plugin Collection for Windows Live Writer](http://www.codeplex.com/wlwplugincollection) on [Codeplex](http://www.codeplex.com/).  This comes in real useful when getting code into a blog entry.  Because straight pasting really doesn’t do so well for readability.

So here are my test code pastes.  A basic view in C#.

```
   1:  using System;
   2:  using System.ComponentModel;
   3:  using System.Windows.Forms;
   4:  using Microsoft.Practices.Unity;
   5:  using Tsr.SeatingSystem.Controller;
   6:  using Tsr.SeatingSystem.Controller.Views;
   7:  using Tsr.SeatingSystem.WinForm.Properties;
   8:  using Tsr.SeatingSystem.WinForm.Seating;
   9:
  10:  namespace Tsr.SeatingSystem.WinForm
  11:  {
  12:      public partial class SeatingSystemMainView : Form, ISeatingSystemMainView
  13:      {
  14:          private TsrController controller;
  15:
  16:          public SeatingSystemMainView()
  17:          {
  18:              InitializeComponent();
  19:              Icon = Resources.Clock;
  20:          }
  21:
  22:          [Dependency]
  23:          public TsrController Controller
  24:          {
  25:              get { return controller; }
  26:              set
  27:              {
  28:                  controller = value;
  29:                  controller.SetSeatingSystemMainView(this);
  30:              }
  31:          }
  32:
  33:          #region View Events & Raise Events
  34:
  35:          public event EventHandler SeatingSystemMainView_Load;
  36:          public event EventHandler ExitToolStripMenuItem_Click;
  37:          public event EventHandler TicketingToolStripMenuItem_Click;
  38:          public event EventHandler SeatingToolStripMenuItem_Click;
  39:          public event EventHandler ReservationsToolStripMenuItem_Click;
  40:          public event EventHandler OptionsToolStripMenuItem_Click;
  41:          public event EventHandler AboutToolStripMenuItem_Click;
  42:          public event PropertyChangedEventHandler PropertyChanged;
```

Some basic SQL.

```
   1:  /****** Object:  View [dbo].[tmtUserListing]    Script Date: 07/06/2008 01:27:11 ******/
   2:  IF  EXISTS (SELECT * FROM sys.views WHERE object_id = OBJECT_ID(N'[dbo].[tmtUserListing]'))
   3:  DROP VIEW [dbo].[tmtUserListing]
   4:  GO
   5:  /****** Object:  View [dbo].[tmtUserListing]    Script Date: 07/06/2008 01:27:11 ******/
   6:  SET ANSI_NULLS ON
   7:  GO
   8:  SET QUOTED_IDENTIFIER ON
   9:  GO
  10:  IF NOT EXISTS (SELECT * FROM sys.views WHERE object_id = OBJECT_ID(N'[dbo].[tmtUserListing]'))
  11:  EXEC dbo.sp_executesql @statement = N'CREATE VIEW dbo.tmtUserListing
  12:  AS
  13:  SELECT     dbo.tmtUsers.UserId, GrandCentral.dbo.aspnet_Users.UserName
  14:  FROM         dbo.tmtUsers LEFT OUTER JOIN
  15:                        GrandCentral.dbo.aspnet_Users ON dbo.tmtUsers.UserId = GrandCentral.dbo.aspnet_Users.UserId
  16:  '
  17:  GO
```

Some XAML (Which technically isn’t on the list, but I formatted it via HTML)

```
   1:  <UserControl x:Class="SecurityAdministratorWpf.Login"
   2:      xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation"
   3:      xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
   4:      Height="225" Width="410">
   5:      <Grid>
   6:          <Button Height="23"
   7:                  HorizontalAlignment="Right"
   8:                  Margin="0,0,28,15"
   9:                  Name="buttonLogin"
  10:                  VerticalAlignment="Bottom"
  11:                  Width="75"
  12:                  ToolTip="Click to login.">Login</Button>
  13:      </Grid>
  14:  </UserControl>
```

Some HTML

```
   1:  <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
   2:  <html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en">
   3:  <head runat="server">
   4:      <link rel="stylesheet" href="default.css" type="text/css" />
   5:      <link rel="shortcut icon" href="~/pics/blogengine.ico" type="image/x-icon" />
   6:  </head>
   7:  <body>
   8:      <form id="Form1" runat="server">
   9:      <div class="outerouter">
  10:          <div class="outer-container">
  11:              <div class="inner-container">
  12:                  <div class="header">
  13:                      <div class="title">
  14:                          <div class="sitename">
  15:                              <a href="~/" runat="server">
  16:                                  <%=BlogSettings.Instance.Name %></a></div>
  17:                          <div class="sitenameshadow">
  18:                              <%=BlogSettings.Instance.Name %></div>
  19:                          <div class="slogan">
  20:                              <%=BlogSettings.Instance.Description %></div>
  21:                      </div>
  22:                  </div>
  23:                  <div class="path">
  24:                      <div class="left">
  25:                          <ul>
  26:                              <li>
  27:                                  <asp:HyperLink ID="HlHome" NavigateUrl="~/default.aspx" runat="server">Home</asp:HyperLink></li>
  28:                              <li class="page_item">
  29:                                  <asp:HyperLink ID="HlArchive" NavigateUrl="~/archive.aspx" runat="server">Archive</asp:HyperLink></li>
  30:                              <li class="page_item">
  31:                                  <asp:HyperLink ID="hlContact" NavigateUrl="~/contact.aspx" runat="server">Cont
act</asp:HyperLink></li>
  32:                          </ul>
  33:                      </div>
  34:                      <div class="right">
  35:                          <a href="<%=Utils.FeedUrl %>">Subscribe to My Feed<asp:Image ID="RssIconImage1" runat="Server"
  36:                              Width="24px" Height="24px" AlternateText="RSS Feed" ImageAlign="AbsMiddle" Style="margin: 0 0 0 10px" /></a>
  37:                      </div>
  38:                      <div class="clearer">
  39:                      </div>
  40:                  </div>
  41:                  <% if (Page.User.Identity.IsAuthenticated)
  42:                     { %>
  43:                  <div class="adminpath">
  44:                      <h2>
  45:                          Admin:</h2>
  46:                      <uc1:menu ID="Menu1" runat="server" />
  47:                  </div>
  48:                  <%} %>
  49:                  <div class="main">
  50:                      <div class="content">
  51:                          <asp:ContentPlaceHolder ID="cphBody" runat="server" />
  52:                      </div>
  53:                      <div class="navigation">
  54:                          <blog:SearchOnSearch ID="SearchOnSearch1" runat="server" MaxResults="3" Headline="You searched for"
  55:                              Text="Here are some results for the search term on this website" />
  56:                          <div class="block">
  57:                              <h2>
  58:                                  Search</h2>
  59:                              <blog:SearchBox ID="SearchBox1" runat="server" />
  60:                          </div>
  61:                          <div class="block">
  62:                              <h2>
  63:                                  Tags</h2>
  64:                              <blog:TagCloud ID="TagCloud1" runat="server" />
  65:                          </div>
  66:                          <div class="block">
  67:                              <h2>
  68:
       Categories</h2>
  69:                              <blog:CategoryList ID="CategoryList1" ShowRssIcon="true" runat="Server" />
  70:                          </div>
  71:                          <div class="block">
  72:                              <h2>
  73:                                  Archive</h2>
  74:                              <blog:MonthList ID="MonthList1" runat="Server" />
  75:                          </div>
  76:                          <div class="block">
  77:                              <h2>
  78:                                  Blogroll</h2>
  79:                              <blog:Blogroll ID="Blogroll1" runat="server" />
  80:                          </div>
  81:                          <div class="block">
  82:                              <h2>
  83:                                  Disclaimer</h2>
  84:                              <p>
  85:                                  The opinions expressed herein are my own personal opinions and do not represent
  86:                                  my employer's view in anyway.</p>
  87:                              <p>
  88:                                  &copy; Copyright
  89:                                  <%=DateTime.Now.Year %></p>
  90:                          </div>
  91:                      </div>
  92:                      <div class="clearer">
  93:                          &nbsp;</div>
  94:                  </div>
  95:                  <div class="footer">
  96:                      <div class="left">
  97:                          <div>
  98:                              Powered by <a href="http://www.dotnetblogengine.net/" target="_blank">BlogEngine.NET</a>
  99:                              <%=BlogSettings.Instance.Version() %>
 100:                              | Design by <a href="http://michael.sivers.co.uk">Michael Sivers</a>
 101:                          </div>
 102:                      </div>
 103:                      <div class="right">
 104:                          <asp:LoginStatus ID="LoginStatus1" runat="Server" LoginText="Sign in" LogoutText="Sign out"
 105:                              EnableViewState="false" />
 106:                      </div
>
 107:                      <div class="clearer">
 108:                      </div>
 109:                  </div>
 110:              </div>
 111:          </div>
 112:      </div>
 113:      </form>
 114:  </body>
 115:  </html>
```
