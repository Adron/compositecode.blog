---
title: Code Paste Formatting Fixed With CSS
date: 2008-10-24 19:25:32 +0000
last_modified_at: 2008-10-24 19:25:32 +0000
permalink: /2008/10/24/code-paste-formatting-fixed-with-css/
slug: code-paste-formatting-fixed-with-css
wp_id: 201
original_url: https://compositecode.blog/2008/10/24/code-paste-formatting-fixed-with-css/
categories:
- Uncategorized Bits
tags: []
excerpt: 'You’ll have to look back and check out my entry on how to get code displayed on a blog entry nice n’ smooth. I did however add some CSS that cleaned up the display on the blog. That snippet is below. 1: .csharpcode 2: { 3: padding: 5px; 4: margin: 5px; 5: border: medium solid …'
---

You’ll have to [look back](http://www.adronbhall.com/blogs/technology__software_development/post/2008/09/26/Code-Paste-Add-In-for-Windows-Live-Writer.aspx) and check out my entry on how to get code displayed on a blog entry nice n’ smooth.  I did however add some CSS that cleaned up the display on the blog.  That snippet is below.

```
   1:  .csharpcode
   2:  {
   3:      padding: 5px;
   4:      margin: 5px;
   5:      border: medium solid #d0eb55;
   6:      overflow: scroll;
   7:  }
   8:  .csharpcode, .csharpcode pre
   9:  {
  10:      padding: 4px;
  11:      margin: 4px;
  12:      font-size: 1em;
  13:      color: #fff;
  14:      font-family: Consolas, "Courier New" , Courier, Monospace;
  15:      background-color: #414141;
  16:      line-height: 1.1em;
  17:      width: 720px;
  18:  }
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
