---
title: Put Stuff in Your Windows Azure Junk Trunk – ASP.NET MVC Application
date: 2011-02-10 05:19:07 -0800
last_modified_at: 2011-02-15 14:47:00 -0800
permalink: /2011/02/10/windows-azure-junk-trunk-part-2/
slug: windows-azure-junk-trunk-part-2
wp_id: 2240
original_url: https://compositecode.blog/2011/02/10/windows-azure-junk-trunk-part-2/
categories:
- Azure
- How-to
tags:
- azure
- BLOB
- cloud
- cloud computing
- cloud storage
- microsoft
- web role
- windows azure
- windows azure blob
- windows azure queue
- windows azure table
- worker role
excerpt: If you haven’t read Part 1 of this series, you’ll need to in order to follow along with the JunkTrunk Repository. Open the solution up if you haven’t already and navigate to the Models Folder within the ASP.NET MVC JunkTrunk Project. In the folder add another class titled FileItemModel.cs and BlobModel.cs. Add the following properties to the FileItemModel.
---

If you haven’t read [Part 1](/2011/02/07/windows-azure-junk-trunk-part-1/) of this series ([part 3 click here](/2011/02/14/windows-azure-junk-trunk-part-3/)), you’ll need to in order to follow along with the *JunkTrunk* Repository.  Open the solution up if you haven’t already and navigate to the Models Folder within the ASP.NET MVC *JunkTrunk* Project.  In the folder add another class titled F*ileItemModel.cs* and *BlobModel.cs*. Add the following properties to the *FileItemModel*.

```csharp
public class FileItemModel
{
    public Guid ResourceId { get; set; }
    public string ResourceLocation { get; set; }
    public DateTime UploadedOn { get; set; }
}
```

Add the following property to the *BlobModel* and inherit from the *FileItemModel* Class.

```csharp
public class BlobModel : FileItemModel
{
    public Stream BlobFile { get; set; }
}
```

Next add a new class file titled *FileBlobManager.cs* and add the following code to the class.

```csharp
public class FileBlobManager
{
    public void PutFile(BlobModel blobModel)
    {
        var blobFileName = string.Format("{0}-{1}", DateTime.Now.ToString("yyyyMMdd"), blobModel.ResourceLocation);
        var blobUri = Blob.PutBlob(blobModel.BlobFile, blobFileName);

        Table.Add(
                new BlobMeta
                {
                    Date = DateTime.Now,
                    ResourceUri = blobUri,
                    RowKey = Guid.NewGuid().ToString()
                });
    }

    public BlobModel GetFile(Guid key)
    {
        var blobMetaData = Table.GetMetaData(key);
        var blobFileModel =
            new BlobModel
            {
                UploadedOn = blobMetaData.Date,
                BlobFile = Blob.GetBlob(blobMetaData.ResourceUri),
                ResourceLocation = blobMetaData.ResourceUri
            };
        return blobFileModel;
    }

    public List GetBlobFileList()
    {
        var blobList = Table.GetAll();

        return blobList.Select(
            metaData => new FileItemModel
            {
                ResourceId = Guid.Parse(metaData.RowKey),
                ResourceLocation = metaData.ResourceUri,
                UploadedOn = metaData.Date
            }).ToList();
    }

    public void Delete(string identifier)
    {
        Table.DeleteMetaDataAndBlob(Guid.Parse(identifier));
    }
}
```

Now that the repository, management, and models are all complete the focus can turn to the controller and the views of the application. At this point the break down of each data element within the data transfer object and the movement of the data back and forth becomes very important to the overall architecture. One of the things to remember is that the application should not pass back and forth data such as URIs or other long easy to hack strings. This is a good place to include Guids or if necessary integer values that identify the data that is getting created, updated, or deleted. This helps to simplify the UI and help decrease the chance of various injection attacks. The next step is to open up the HomeController and add code to complete each of the functional steps for the site.

```csharp
[HandleError]
public class HomeController : Controller
{
    public ActionResult Index()
    {
        ViewData["Message"] = "Welcome to the Windows Azure Blob Storing ASP.NET MVC Web Application!";
        var fileBlobManager = new FileBlobManager();
        var fileItemModels = fileBlobManager.GetBlobFileList();
        return View(fileItemModels);
    }

    public ActionResult About()
    {
        return View();
    }

    public ActionResult Upload()
    {
       return View();
    }

    public ActionResult UploadFile()
    {
        foreach (string inputTagName in Request.Files)
        {
            var file = Request.Files[inputTagName];

            if (file.ContentLength > 0)
            {
                var blobFileModel =
                    new BlobModel
                        {
                            BlobFile = file.InputStream,
                            UploadedOn = DateTime.Now,
                            ResourceLocation = Path.GetFileName(file.FileName)
                        };

                var fileBlobManager = new FileBlobManager();
                fileBlobManager.PutFile(blobFileModel);
            }
        }

        return RedirectToAction("Index", "Home");
    }

    public ActionResult Delete(string identifier)
    {
        var fileBlobManager = new FileBlobManager();
        fileBlobManager.Delete(identifier);
        return RedirectToAction("Index", "Home");
    }
}
```

The view hasn’t been created for the Upload just yet, so the method will cause a build error at this point. But before I add a view for this action, I’ll cover what has been created for the controller.

The Index Action I’ve changed moderately to have a list of the Blobs that are stored in the Windows Azure Blob Storage. This will be pulled from the manager class that we created earlier and passed into the view for rendering. I also, just for cosmetic reasons, changed the default display message passed into the ViewData so that the application would have something displayed more relevant to the application.

The About message I just left as is. The Upload action simply returns what will be a view we create.

The UploadFile Action checks for files within the request, builds up the model and then puts the model into storage via the manager.

The last method is the Delete Action that instantiates the manager and then calls a delete against the storage. This action then in turn traces back through, finds the Table & Blob Entities that are related to the specific blob and deletes both from the respective Windows Azure Storage Table and Blob Mediums.

The next step is to get the various views updated or added to enable the upload and deletion of the blob items.

Add a view titled Upload.aspx to the Home Folder of the Views within the *JunkTrunk* Project.

[![Upload View](/images/adronhall.smugmug.com/Software/Software-Development/Windows-Azure-Table-Blob-Queue/06fig07/1178841879_Q3cht-S.png "Upload View")](http://adronhall.smugmug.com/Software/Software-Development/Windows-Azure-Table-Blob-Queue/15711067_tbF6t#1178841879_Q3cht-O-LB)

*Upload View*

First change the inherits value for the view from System.Web.Mvc.ViewPage to System.Web.Mvc.ViewPage. After that add the following HTML to the view.

```html
<asp:Content ID="Content1" ContentPlaceHolderID="TitleContent" runat="server">
	Upload an Image
</asp:Content>
<asp:Content ID="Content2" ContentPlaceHolderID="MainContent" runat="server">
	<h2>
		Upload</h2>
	<% using (Html.BeginForm("UploadFile", "Home", FormMethod.Post,
        new { enctype = "multipart/form-data" }))
	   {%>
	<%: Html.ValidationSummary(true) %>
	<fieldset>
		<legend>Fields</legend>

		<div class="editor-label">
			Select file to upload to Windows Azure Blob Storage:
		</div>
		<div class="editor-field">
			<input type="file" id="fileUpload" name="fileUpload" />
		</div>
		<p>
			<input type="submit" value="Upload" />
		</p>
	</fieldset>
	<% } %>
	<div>
		<%: Html.ActionLink("Back to List", "Index") %>
	</div>
</asp:Content>
```

After adding the HTML, then change the HTML in the Index.aspx View to have an action link for navigating to the upload page and for viewing the list of uploaded Blobs. Change the inherits first form System.Web.Mvc.ViewPage to System.Web.Mvc.ViewPage<IEnumerable>. The rest of the changes are listed below.

```html
<asp:Content ID="Content1" ContentPlaceHolderID="TitleContent" runat="server">
    Home Page
</asp:Content>
<asp:Content ID="Content2" ContentPlaceHolderID="MainContent" runat="server">
    <h2>
        <%: ViewData["Message"] %></h2>
    <p>
        <%: Html.ActionLink("Upload", "Upload", "Home") %>
        a file to Windows Azure Blob Storage.
    </p>
    Existing Files:<br />
    <table>
        <tr>
            <th>
            </th>
            <th>
                FileName
            </th>
            <th>
                DownloadedOn
            </th>
        </tr>
        <% foreach (var item in Model)
           { %>
        <tr>
            <td>
                <%: Html.ActionLink("Delete", "Delete",
                new { identifier = item.ResourceId })%>
            </td>
            <td>
                <%: item.ResourceLocation %>
            </td>
            <td>
                <%: String.Format("{0:g}", item.UploadedOn) %>
            </td>
        </tr>
        <% } %>
    </table>
</asp:Content>
```

Make sure the Windows Azure Project is set as the startup project and click on F5 to run the application. The following page should display first.

[![The Home Page o' Junk Trunk](/images/adronhall.smugmug.com/Software/Software-Development/Windows-Azure-Table-Blob-Queue/06fig08/1178863402_DN3M9-S.png "The Home Page o' Junk Trunk")](http://adronhall.smugmug.com/Software/Software-Development/Windows-Azure-Table-Blob-Queue/15711067_tbF6t#1178863402_DN3M9-O-LB)

*The Home Page o' Junk Trunk*

Click through on it to go to the upload page.

[![Selecting an Image to Put in The Junk Trunk](/images/adronhall.smugmug.com/Software/Software-Development/Windows-Azure-Table-Blob-Queue/06fig09/1178863411_Ciyo6-S.png "Selecting an Image to Put in The Junk Trunk")](http://adronhall.smugmug.com/Software/Software-Development/Windows-Azure-Table-Blob-Queue/15711067_tbF6t#1178863411_Ciyo6-O-LB)

*Selecting an Image to Put in The Junk Trunk*

On the upload page select and image to upload and then click on upload. This will then upload the image and redirect appropriately to the home page.

[![The Image in the Junk Trunk](/images/adronhall.smugmug.com/Software/Software-Development/Windows-Azure-Table-Blob-Queue/06fig10/1178863398_B8Ahy-S.png "The Image in the Junk Trunk")](http://adronhall.smugmug.com/Software/Software-Development/Windows-Azure-Table-Blob-Queue/15711067_tbF6t#1178863398_B8Ahy-O-LB)

*The Image in the Junk Trunk*

On the home page the list should now have the uploaded blob image listed. Click delete to delete the image. When deleted the table and the blob itself will be removed from the Windows Azure Storage. To see that the data & image are being uploaded open up the Server Explorer within Visual Studio 2010.

[![Visual Studio 2010 Server Explorer](/images/adronhall.smugmug.com/Software/Software-Development/Windows-Azure-Table-Blob-Queue/06fig11/1178877649_XEBZm-O.png "Visual Studio 2010 Server Explorer")](http://adronhall.smugmug.com/Software/Software-Development/Windows-Azure-Table-Blob-Queue/15711067_tbF6t#1178877649_XEBZm-A-LB)

*Visual Studio 2010 Server Explorer*

View the data by opening up the Windows Azure Storage tree. Double click on either of the storage mediums to view table or blob data.

[![Windows Azure Storage](/images/adronhall.smugmug.com/Software/Software-Development/Windows-Azure-Table-Blob-Queue/06fig12/1178877655_5bgdi-S.png "Windows Azure Storage")](http://adronhall.smugmug.com/Software/Software-Development/Windows-Azure-Table-Blob-Queue/15711067_tbF6t#1178877655_5bgdi-O-LB)

*Windows Azure Storage*
