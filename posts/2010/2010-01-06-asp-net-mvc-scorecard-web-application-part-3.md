---
title: ASP.NET MVC Scorecard Web Application – Part 3
date: 2010-01-06 00:02:00 +0000
last_modified_at: 2010-01-06 00:02:00 +0000
permalink: /2010/01/06/asp-net-mvc-scorecard-web-application-part-3/
slug: asp-net-mvc-scorecard-web-application-part-3
wp_id: 681
original_url: https://compositecode.blog/2010/01/06/asp-net-mvc-scorecard-web-application-part-3/
categories:
- Uncategorized Bits
tags: []
excerpt: In this entry I want to cover a helper I wrote and some other bits to simplify creating charts for the scorecard application. One of the things I wanted to do was get rid of the excessive amount of code needed in the view to generate various charts. Since at some point I wanted to …
---

In this entry I want to cover a helper I wrote and some other bits to simplify creating charts for the scorecard application.

One of the things I wanted to do was get rid of the excessive amount of code needed in the view to generate various charts.  Since at some point I wanted to be able to dynamically create charts based on user input, I figured what better time than now to start chiseling out a helper class for displaying the charts.

Take the pie chart I created in the last entry.  The code in the view looked like this.

```
using (Chart chartPie = new Chart())
{
    double[] yValues = (double[])ViewData["TopCountryCounts"];
    string[] xValues = (string[])ViewData["TopCountries"];

    Title t = new Title("Pie Chart Representation",
        Docking.Top,
        new System.Drawing.Font("Verdana, Helvetica, Sans-Serif", 14, System.Drawing.FontStyle.Bold),
        System.Drawing.Color.FromArgb(26, 59, 105));
    chartPie.Titles.Add(t);
    chartPie.ChartAreas.Add("Default");

    // create a couple of series
    chartPie.Series.Add("Default");
    chartPie.Series["Default"].Points.DataBindXY(xValues, yValues);

    // Set Doughnut chart type
    chartPie.Series["Default"].ChartType = SeriesChartType.Pie;

    // Set labels style
    chartPie.Series["Default"]["PieLabelStyle"] = "Inside";
    // Set Doughnut radius percentage
    chartPie.Series["Default"]["DoughnutRadius"] = "40";
    // Explode data point with label "USA"
    chartPie.Series["Default"].Points[3]["Exploded"] = "true";

    chartPie.Width = 400;
    chartPie.Height = 300;
    chartPie.Page = this;
    HtmlTextWriter writer = new HtmlTextWriter(Page.Response.Output);
    chartPie.RenderControl(writer);
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

At 31 lines of code, I was not really stoked about this.  A lot of this, such as creating the title, the chart area, and having a series was something that would be needed by most charts.  With that I went to work writing a set of tests to test the helper class.

```
public const string title = "Chart Title";
public double[] YValues = {3};
public string[] XValues = {"X Value"};

[TestMethod]
public void InstantiateChartHelper()
{
    ChartHelper chartHelper = new ChartHelper("title", YValues, XValues, SeriesChartType.Pie);
    Assert.IsNotNull(chartHelper);
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

This first test and default values, that I assumed I would use for the other tests, got me a nice skeleton class & constructor.  I used [ReSharper](http://www.jetbrains.com/resharper/) to flesh it out a little and then went to writing the other tests.  Each contributing a bit more functionality to the overall class.  I have excluded the remaining tests from this blog entry, but they will be available when I provide the solution for download (that means keep reading and stay tuned).  The class however, that ended up with is below.

```
public class ChartHelper
{
    public ChartHelper(string chartTitle, IEnumerable<double> seriesValues, IEnumerable<string> seriesKeys, SeriesChartType chartType)
    {
        // Setup defaults.
        System.Drawing.Font font = new System.Drawing.Font("Verdana, Helvetica, Sans-Serif", 14, System.Drawing.FontStyle.Bold);
        System.Drawing.Color color = System.Drawing.Color.FromArgb(26, 59, 105);

        // Title
        Title title = new Title(chartTitle, Docking.Top, font, color);

        // Chart Area
        ChartArea chartArea = new ChartArea("DefaultChartArea");
        chartArea.Area3DStyle.Enable3D = true;

        // Series
        Series series = new Series("DefaultSeries");
        series.Points.DataBindXY(seriesKeys, seriesValues);
        series.ChartType = chartType;

        ResultingChart = new Chart();
        ResultingChart.Titles.Add(title);
        ResultingChart.ChartAreas.Add(chartArea);
        ResultingChart.Series.Add(series);

    }

    public Chart ResultingChart { get; set; }
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

As you can see, a nice simple class.  With this class I was then able to use to reduce my lines of code to 9 lines (including the multi-line instantiation, which I suppose could be one line, leaving me with 6).

```
Scorecard.Views.ChartHelper chartHelper = new Scorecard.Views.ChartHelper("Pie Chart Representation",
   (double[])ViewData["TopCountryCounts"],
   (string[])ViewData["TopCountries"],
   SeriesChartType.Pie);
Chart chartPieTwo = chartHelper.ResultingChart;

chartPieTwo.Page = this;
HtmlTextWriter writer1 = new HtmlTextWriter(Page.Response.Output);
chartPieTwo.RenderControl(writer1);
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

This now generates the following pie chart.

![](/images/adronhall.smugmug.com/Software/Software-Development/ASPNET-MVC/PieChart01/757062829_eFok5-M.png)

There are a few more defaults I want to set though, so I went ahead and added a logic section for pie charts as shown below, with the switch view to provide a bit of factory style magic.

```
ResultingChart = new Chart();

// Setup defaults.
System.Drawing.Font font = new System.Drawing.Font("Verdana, Helvetica, Sans-Serif", 14, System.Drawing.FontStyle.Bold);
System.Drawing.Color color = System.Drawing.Color.FromArgb(26, 59, 105);

// Title
Title title = new Title(chartTitle, Docking.Top, font, color);
ResultingChart.Titles.Add(title);

// Chart Area
ChartArea chartArea = new ChartArea("DefaultChartArea") {Area3DStyle = {Enable3D = true}};
ResultingChart.ChartAreas.Add(chartArea);

// Series
Series series = new Series("DefaultSeries");
series.Points.DataBindXY(seriesKeys, seriesValues);
series.ChartType = chartType;
ResultingChart.Series.Add(series);

// Legend
Legend legend = new Legend("DefaultLegend");
ResultingChart.Legends.Add(legend);

switch (chartType)
{
    case SeriesChartType.Bar:
        break;
    case SeriesChartType.Column:
        break;
    case SeriesChartType.Pie:
        series["PieLabelStyle"] = "Inside";
        ResultingChart.Legends[0].Docking = Docking.Bottom;
        ResultingChart.Legends[0].Enabled = true;
        break;
    case SeriesChartType.Funnel:
        break;
    case SeriesChartType.Line:
        break;
    default:
        throw new ArgumentOutOfRangeException("chartType");
}

ResultingChart.Width = 400;
ResultingChart.Height = 300;
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

Notice I also reorganized where some things where instantiated, such as the Chart Object, and organized the order according to each thing I needed to have for the chart.  Once I did this I ran and rendered the chart, which I was happy with for now.

![](/images/adronhall.smugmug.com/Software/Software-Development/ASPNET-MVC/PieChart02/757062830_L46Rv-M.png)

At this point I went back in and added some more charts to my scorecard view.  While I did this I noticed one last thing I ought to refactor.

```
<table>
<tr>
<td>
    <%
        Scorecard.Views.ChartHelper chartHelper = new Scorecard.Views.ChartHelper("Top Countries",
           (double[])ViewData["TopCountryCounts"],
           (string[])ViewData["TopCountries"],
           SeriesChartType.Pie);
        Chart chartPieTwo = chartHelper.ResultingChart;

        // Explode data point with label "USA"
        chartPieTwo.Series["DefaultSeries"].Points[3]["Exploded"] = "true";

        chartPieTwo.Page = this;
        HtmlTextWriter writer = new HtmlTextWriter(Page.Response.Output);
        chartPieTwo.RenderControl(writer);
    %>
</td>
<td>
    <%
        chartHelper = new Scorecard.Views.ChartHelper("View Cart Trend",
           (double[])ViewData["LineValues"],
           (string[])ViewData["TopEngines"],
           SeriesChartType.Line);

        Chart lineChart = chartHelper.ResultingChart;

        lineChart.Page = this;
        lineChart.RenderControl(writer);
    %>
</td>
</tr>
<tr>
<td>
    <%
        chartHelper = new Scorecard.Views.ChartHelper("Yesterday's Page Views",
         (double[])ViewData["ColumnStats"],
         (string[])ViewData["ColumnStatHeaders"],
         SeriesChartType.Column);

        Chart columnChart = chartHelper.ResultingChart;

        columnChart.Page = this;
        columnChart.RenderControl(writer);
    %>
</td>
<td>
    <%
        double[] theValues = (double[]) ViewData["ColumnStats"];
        double[] newValues = new double[]{0,0,0,0};
        int count = 0;
        foreach(double d in theValues)
        {
            newValues[count] += d*DateTime.DaysInMonth(DateTime.Now.Year, DateTime.Now.Month) +
                                DateTime.Now.Month + DateTime.Now.Millisecond;

            count++;
        }

        chartHelper = new Scorecard.Views.ChartHelper("Current Month Page Views",
    newValues,
    (string[])ViewData["ColumnStatHeaders"],
    SeriesChartType.Bar);

        Chart barChart = chartHelper.ResultingChart;

        barChart.Page = this;
        barChart.RenderControl(writer);
    %>
</td>
</tr>
</table>
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

I was assigning the page and rendering the control at every single section within my table.  I didn’t need to do that, so I went back and added a render method to the ChartHelper Class.

```
public void RenderChart(Page page)
{
    ResultingChart.Page = page;
    HtmlTextWriter writer = new HtmlTextWriter(page.Response.Output);
    ResultingChart.RenderControl(writer);
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

With a small change to the view I can now render each chart with one line of code.

```
chartHelper.RenderChart(this);
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

[![](/images/adronhall.smugmug.com/Software/Software-Development/ASPNET-MVC/PieChart03/757098525_U9Ckc-M.png)](http://adronhall.smugmug.com/Software/Software-Development/ASPNET-MVC/10762817_JvDef#751056555_2Apxm-A-LB)

Now that puts everything in a better situation.  Until the next part.  Happy coding.
