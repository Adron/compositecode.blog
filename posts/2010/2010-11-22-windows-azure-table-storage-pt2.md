---
title: Windows Azure Table Storage Part 2
date: 2010-11-22 05:15:04 -0800
last_modified_at: 2010-11-20 18:37:04 -0800
permalink: /2010/11/22/windows-azure-table-storage-pt2/
slug: windows-azure-table-storage-pt2
wp_id: 1796
original_url: https://compositecode.blog/2010/11/22/windows-azure-table-storage-pt2/
categories:
- Azure
- How-to
tags: []
excerpt: In the first part of this two part series I reviewed what table storage in Windows Azure is. In addition I began a how-to for setting up an ASP.NET MVC 2 Web Application for accessing the Windows Azure Table Storage (sounds like keyword soup all of a sudden!). This sample so far is enough to run against the Windows Azure Dev Fabric. However I still need to setup the creation, update, and deletion views for the site, so without further ado, let’s roll.
---

In the first part of this two part series I reviewed what table storage in Windows Azure is. In addition I began a how-to for setting up an ASP.NET MVC 2 Web Application for accessing the Windows Azure Table Storage (sounds like keyword soup all of a sudden!). This sample so far is enough to run against the Windows Azure Dev Fabric. However I still need to setup the creation, update, and deletion views for the site, so without further ado, let’s roll.

1. In the Storage directory of the ASP.NET MVC Web Application right click and select Add and then View. In the Add View Dialog select the Create a strongly-typed view option. From the View data class drop down select the EmailMergeManagement.Models.EmailMergeModel, select Create form the View content drop down box, and uncheck the Select master page check box. When complete the dialog should look as shown below.

   [![Add New View to Project Dialog](/images/adronhall.smugmug.com/Software/Software-Development/Windows-Azure-Table-Storage/06fig04/1096340496_gfwEH-O.png "Add New View to Project Dialog")](http://adronhall.smugmug.com/Software/Software-Development/Windows-Azure-Table-Storage/14716164_3msLb#1096340496_gfwEH-A-LB)

   *Add New View to Project Dialog*
2. Now right click and add another view using the same settings for Delete and name the view Delete.
3. Right click and add another view using the same settings for Details and name the view Details.
4. Right click and add another view for Edit and List, naming these views Edit and List respectively.  When done the Storage directory should have the following views; Create.aspx, Delete.aspx, Details.aspx, Edit.aspx, Index.aspx, and List.aspx.

Now the next steps are to setup a RoleEntryPoint class for the web role to handle a number of configuration and initializations of the storage table.  The first bit of this code will start the diagnostics connection string and wire up the event for the role environment changing.  After this the cloud storage account will have the configuration for the publisher set so the configuration settings can be used.  Finally the role environment setting will be setup so that it will recycle so that the latest settings and credentials will be used when executing.

5. Create a new class in the root of the ASP.NET MVC Web Application and call it EmailMergeWebAppRole.
6. Add the following code to the EmailMergeWebAppRole class.

```csharp
using System.Linq;
using Microsoft.WindowsAzure;
using Microsoft.WindowsAzure.Diagnostics;
using Microsoft.WindowsAzure.ServiceRuntime;

namespace EmailMergeManagement
{
    public class EmailMergeWebAppRole
    {
        public class WebRole : RoleEntryPoint
        {
            public override bool OnStart()
            {
                DiagnosticMonitor.Start("DiagnosticsConnectionString");
                RoleEnvironment.Changing += RoleEnvironmentChanging;
                CloudStorageAccount.
                    SetConfigurationSettingPublisher((configName, configSetter) =>
                {
                    configSetter(RoleEnvironment.
                        GetConfigurationSettingValue(configName));

                    RoleEnvironment.Changed += (sender, arg) =>
                    {
                        if (arg
                            .Changes
                            .OfType()
                            .Any((change) =>
                                (change.ConfigurationSettingName == configName)))
                        {
                            if (!configSetter(RoleEnvironment.
                                GetConfigurationSettingValue(configName)))
                            {
                                RoleEnvironment.RequestRecycle();
                            }
                        }
                    };
                });

                return base.OnStart();
            }

            private static void RoleEnvironmentChanging(object sender,
                RoleEnvironmentChangingEventArgs e)
            {
                if (e.Changes.Any(change =>
                    change is RoleEnvironmentConfigurationSettingChange))
                {
                    e.Cancel = true;
                }
            }
        }
    }
}
```

7. Now open up the StorageController class in the Controllers directory.
8. Add an action method for the List view with the following code.

```csharp
public ActionResult List()
{
    var emailMergeListing = new EmailMergeRepository().Select();
    return View(emailMergeListing);
}
```

9. Add the following two actions to the StorageController Class.

```csharp
public ActionResult Create()
{
    return View();
}

[AcceptVerbs(HttpVerbs.Post)]
public ActionResult Create(EmailMergeModel emailMergeModel)
{
    if (!ModelState.IsValid)
        return View();

    emailMergeModel.LastEditStamp = DateTime.Now;
    emailMergeModel.RowKey = Guid.NewGuid().ToString();

    var emailMergeRepository = new EmailMergeRepository();
    emailMergeRepository.Insert(emailMergeModel);

    return RedirectToAction("List");
}
```

10. On the Index.aspx view add some action links for the following commands.

```html
<ul>
	<li>Email Merge Items
        <%: Html.ActionLink("List", "List", "Storage") %>.</li>
	<li>
        <%: Html.ActionLink("Create", "Create", "Storage") %>
        a new Email Merge Item.</li>
</ul>
```

11. Open up the Create.aspx view and remove the following HTML & other related markup from the page.

```html
<div class="editor-label">
    <%: Html.LabelFor(model => model.LastEditStamp) %></div>
<div class="editor-field">
    <%: Html.TextBoxFor(model => model.LastEditStamp) %>
    <%: Html.ValidationMessageFor(model => model.LastEditStamp) %></div>
<div class="editor-label">
    <%: Html.LabelFor(model => model.Timestamp) %></div>
<div class="editor-field">
    <%: Html.TextBoxFor(model => model.Timestamp) %>
    <%: Html.ValidationMessageFor(model => model.Timestamp) %></div>
<div class="editor-label">
    <%: Html.LabelFor(model => model.PartitionKey) %></div>
<div class="editor-field">
    <%: Html.TextBoxFor(model => model.PartitionKey) %>
    <%: Html.ValidationMessageFor(model => model.PartitionKey) %></div>
<div class="editor-label">
    <%: Html.LabelFor(model => model.RowKey) %></div>
<div class="editor-field">
    <%: Html.TextBoxFor(model => model.RowKey) %>
    <%: Html.ValidationMessageFor(model => model.RowKey) %></div>
```

There is now enough collateral in the web application to run the application and create new EmailMergeModel items and view them with the list view. Click on F5 to run the application. The first page that should come up is show below.

[![Windows Azure Storage Samples Site Home Page](/images/adronhall.smugmug.com/Software/Software-Development/Windows-Azure-Table-Storage/06fig05/1096340517_V7rxd-S.png "Windows Azure Storage Samples Site Home Page")](http://adronhall.smugmug.com/Software/Software-Development/Windows-Azure-Table-Storage/14716164_3msLb#1096340517_V7rxd-A-LB)

*Windows Azure Storage Samples Site Home Page*

Click on the Windows Azure Table Storage link to navigate to the main view of the storage path. Here there is now the Create and List link. Click on the Create link and add a record to the table storage. The Create view will look like below when you run it.

[![Windows Azure Storage Samples Site Create Email Merge Listing](/images/adronhall.smugmug.com/Software/Software-Development/Windows-Azure-Table-Storage/06fig06/1096367907_ijHFp-O.png "Windows Azure Storage Samples Site Create Email Merge Listing")](http://adronhall.smugmug.com/Software/Software-Development/Windows-Azure-Table-Storage/14716164_3msLb#1096367907_ijHFp-O-LB)

*Windows Azure Storage Samples Site Create Email Merge Listing*

I’ve added a couple just for viewing purposes, with the List view now looking like this.

[![Windows Azure Storage Samples Site Listings](/images/adronhall.smugmug.com/Software/Software-Development/Windows-Azure-Table-Storage/06fig07/1096367909_VP3uT-S.png "Windows Azure Storage Samples Site Listings")](http://adronhall.smugmug.com/Software/Software-Development/Windows-Azure-Table-Storage/14716164_3msLb#1096367909_VP3uT-O-LB)

*Windows Azure Storage Samples Site Listings*

Well that’s a fully functional CRUD (CReate, Update, and Delete) Web Application running against Windows Azure.  With a details screen to boot.
