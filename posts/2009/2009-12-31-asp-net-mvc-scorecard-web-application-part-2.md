---
title: ASP.NET MVC Scorecard Web Application – Part 2
date: 2009-12-31 00:06:00 +0000
last_modified_at: 2009-12-31 00:06:00 +0000
permalink: /2009/12/31/asp-net-mvc-scorecard-web-application-part-2/
slug: asp-net-mvc-scorecard-web-application-part-2
wp_id: 678
original_url: https://compositecode.blog/2009/12/31/asp-net-mvc-scorecard-web-application-part-2/
categories:
- Uncategorized Bits
tags: []
excerpt: Alright, time to add some actual functionality to this thing. First I want a report showing up on the scorecard page that has already been created. I don’t really care what it displays, just want to get it working and displaying. I will get one report working and then pull up others and connect them …
---

Alright, time to add some actual functionality to this thing.  First I want a report showing up on the scorecard page that has already been created.  I don’t really care what it displays, just want to get it working and displaying.  I will get one report working and then pull up others and connect them with actual data from the Model.

[![](/images/adronhall.smugmug.com/Software/Software-Development/ASPNET-MVC/ChartSamplesthumb1/750977818_xnUV4-M.jpg)](http://code.msdn.microsoft.com/mschart)First things first I grabbed the [MS Charting controls](http://code.msdn.microsoft.com/mschart), which you will need to follow along with this section of code.  I assume for the rest of this entry that the charting controls are installed.

First off I created some nice fake data in a DataTable.  The object I created is below.  This is located in the Models path for now.  Just to get this mocked up.

```
public class ReportSampleData
{
    public ReportSampleData()
    {
        SampleData = new DataTable("Adron's Sample Data");

        SampleData.Columns.Add(new DataColumn("Col1"));
        SampleData.Columns.Add(new DataColumn("Col2"));
        SampleData.Columns.Add(new DataColumn("Col3"));
        SampleData.Columns.Add(new DataColumn("Col4"));

        DataRow dr1 = SampleData.NewRow();
        dr1[0] = "Sample Set 1";
        dr1[1] = 14;
        dr1[2] = 13;
        dr1[3] = 10;
        DataRow dr2 = SampleData.NewRow();
        dr2[0] = "Sample Set 2";
        dr2[1] = 15;
        dr2[2] = 13;
        dr2[3] = 12;
        DataRow dr3 = SampleData.NewRow();
        dr3[0] = "Sample Set 2";
        dr3[1] = 17;
        dr3[2] = 11;
        dr3[3] = 9;

        SampleData.Rows.Add(dr1);
        SampleData.Rows.Add(dr2);
        SampleData.Rows.Add(dr3);
    }

    public DataTable SampleData { get; set; }
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

Once I created the fake data, I dropped in the chart control into the Display.aspx view under the Scorecard Directory of the views.

```
<%@ Page Language="C#" MasterPageFile="~/Views/Shared/Site.Master" Inherits="System.Web.Mvc.ViewPage" %>

<%@ Register Assembly="System.Web.DataVisualization, Version=3.5.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35"
    Namespace="System.Web.UI.DataVisualization.Charting" TagPrefix="asp" %>
<asp:Content ID="Content1" ContentPlaceHolderID="TitleContent" runat="server">
    Scorecard
</asp:Content>
<asp:Content ID="Content2" ContentPlaceHolderID="MainContent" runat="server">
    <form id="form1" runat="server">
    <h2>
        Scorecard
    </h2>
    <%
        using (Chart chartColumns = new Chart())
        {
            chartColumns.Width = 412;
            chartColumns.Height = 296;
            chartColumns.RenderType = RenderType.ImageTag;

            chartColumns.Palette = ChartColorPalette.None;
            Title t = new Title("Column Bar Chart",
                Docking.Top,
                new System.Drawing.Font("Verdana, Helvetica, Sans-Serif", 14, System.Drawing.FontStyle.Bold),
                System.Drawing.Color.FromArgb(26, 59, 105));
            chartColumns.Titles.Add(t);
            chartColumns.ChartAreas.Add("Series 1");

            // create a couple of series
            chartColumns.Series.Add("Series 1");
            chartColumns.Series.Add("Series 2");

            // add points to series 1
            foreach (int value in (List<int>)ViewData["Chart"])
            {
                chartColumns.Series["Series 1"].Points.AddY(value + DateTime.Now.Second);
            }

            // add points to series 2
            foreach (int value in (List<int>)ViewData["Chart"])
            {
                chartColumns.Series["Series 2"].Points.AddY(value + DateTime.Now.Minute);
            }

            chartColumns.Legends.Add("Legend1");
            chartColumns.BorderSkin.SkinStyle = BorderSkinStyle.None;

            // Render chart control
            chartColumns.Page = this;
            HtmlTextWriter writer = new HtmlTextWriter(Page.Response.Output);
            chartColumns.RenderControl(writer);
        }
    %>
    </form>
</asp:Content>
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

Once that was finished the final step is to toss in the controller the view data.

```
public ActionResult Display()
{
    ViewData["Chart"] = new List<int>() {4, 6, 12, 3, 11};
    return View("Display");
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

Now run the app and check out the page.  You should see a chart like that shown below.  (Click for larger image)

[![](/images/adronhall.smugmug.com/Software/Software-Development/ASPNET-MVC/12-27-2009-5-01-05-PM/751056555_2Apxm-S.png)](http://adronhall.smugmug.com/Software/Software-Development/ASPNET-MVC/10762817_JvDef#751056555_2Apxm-A-LB)

That covers the second part of this series.  I will have another addition up soon, tying even more bits together.

[![Shout it](http://dotnetshoutout.com/image.axd?url=http%3A%2F%2Fwww.adronbhall.com%2Fblogs%2Ftechnology__software_development%2Fpost%2F2009%2F12%2F31%2FASPNET-MVC-Scorecard-Web-Application-Part-2.aspx)](http://dotnetshoutout.com/ASPNET-MVC-Scorecard-Web-Application-Part-2)

[![kick it on DotNetKicks.com](http://www.dotnetkicks.com/Services/Images/KickItImageGenerator.ashx?url=http%3a%2f%2fwww.adronbhall.com%2fblogs%2ftechnology__software_development%2fpost%2f2009%2f12%2f31%2fASPNET-MVC-Scorecard-Web-Application-Part-2.aspx&bgcolor=3333FF&cfgcolor=CC3300)](http://www.dotnetkicks.com/kick/?url=http%3a%2f%2fwww.adronbhall.com%2fblogs%2ftechnology__software_development%2fpost%2f2009%2f12%2f31%2fASPNET-MVC-Scorecard-Web-Application-Part-2.aspx)
