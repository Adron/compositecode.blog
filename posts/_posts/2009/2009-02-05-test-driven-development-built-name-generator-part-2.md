---
title: Test Driven Development Built Name Generator Part 2
date: 2009-02-05 02:18:42 -0800
last_modified_at: 2013-09-05 19:09:33 -0700
permalink: /2009/02/05/test-driven-development-built-name-generator-part-2/
slug: test-driven-development-built-name-generator-part-2
wp_id: 583
original_url: https://compositecode.blog/2009/02/05/test-driven-development-built-name-generator-part-2/
categories:
- .NET Bits
- How-to
- Testing
tags:
- bdd
- behavior driven development
- tdd
- test
- test driven development
- testing
excerpt: Part 1, Part 3. Alright, time to tear into getting that name data imported into the database. To review the previous entry check out part 1. Next I set the Windows App Project I added in part 1 to be the startup project. After that I created a screen that looks like the image below (click …
---

[Part 1](/2009/02/04/test-driven-development-built-name-generator-part-1/), [Part 3](/2009/02/13/test-driven-development-built-name-generator-part-3/).

Alright, time to tear into getting that name data imported into the database.  To review the previous entry check out [part 1](/2009/02/04/test-driven-development-built-name-generator-part-1/).

Next I set the Windows App Project I added in [part 1](/2009/02/04/test-driven-development-built-name-generator-part-1/) to be the startup project.  After that I created a screen that looks like the image below (click to see larger image).

[![](/images/adronhall.smugmug.com/photos/464369132_woo7x-S.png)](http://adronhall.smugmug.com/gallery/7227152_BavAD#464369132_woo7x)

Also add an open file dialog control.  Next double click on the Process button and add the following code.  Make sure not to miss the instantiation of the names list property in the initialization.

```csharp
using System;
using System.Collections.Generic;
using System.IO;
using System.Text.RegularExpressions;
using System.Windows.Forms;

namespace TextFileImporter
{
    public partial class Form1 : Form
     {
         public Form1()
         {
             InitializeComponent();
             Names = new List();
         }

         private List Names { get; set; }

         private void buttonProcessFile_Click(object sender, EventArgs e)
         {
            if (openFile.ShowDialog() == DialogResult.OK)
            {
                if (File.Exists(openFile.FileName))
                {
                    TextReader tr = new StreamReader(openFile.FileName);
                    textProcessedFile.Text = tr.ReadToEnd();
                    tr.Close();
                    // Cleanup text.
                    textProcessedFile.Text = ProcessName(textProcessedFile.Text);
                }
                else
                {
                    MessageBox.Show("Select a file that exists.", "File doesn't exist.", MessageBoxButtons.OK,
                                    MessageBoxIcon.Information, MessageBoxDefaultButton.Button1);
                }
            }
        }

        private string ProcessName(string textBody)
        {
            var regex = new Regex("[^A-Z']+");
            textBody = regex.Replace(textBody, " ");

            foreach (var s in textBody.Split(Convert.ToChar(" ")))
            {
                Names.Add(s);
            }

            return textBody;
        }
    }
}
```

With the beauty of those regular expressions the files will parse appropriately in about 1-5 seconds.  Next we need a way to write this data into the database.  I did this by adding a Class Project named *Generator.Core* and added a folder called *Model*.

[![](/images/adronhall.smugmug.com/photos/466793052_iiSAX-S.png)](http://adronhall.smugmug.com/gallery/7227152_BavAD#466793052_iiSAX)

In the Model Directory I added a new ADO.NET Entity Framework Model.  The images below show my steps through the wizard.

- [![Wizard # 1 - Adding Data Model.](/images/adronhall.smugmug.com/photos/466793261_u9hMt-Th.png)](http://adronhall.smugmug.com/gallery/7227152_BavAD#466793261_u9hMt#466793261-A-LB "Wizard # 1 - Adding Data Model.")Wizard # 1 – Adding Data Model.
- [![Wizard # 2 - Adding Data Model.](/images/adronhall.smugmug.com/photos/466793279_S45j7-Th.png)](http://adronhall.smugmug.com/gallery/7227152_BavAD#466793279_S45j7#466793279-A-LB "Wizard # 2 - Adding Data Model.")Wizard # 2 – Adding Data Model.
- [![Wizard # 3 - Adding Data Model.](/images/adronhall.smugmug.com/photos/466793432_WZPg2-Th.png)](http://adronhall.smugmug.com/gallery/7227152_BavAD#466793432_WZPg2#466793432-A-LB "Wizard # 3 - Adding Data Model.")Wizard # 3 – Adding Data Model.
- [![Wizard # 4 - Adding Data Model.](/images/adronhall.smugmug.com/photos/466794009_bG2oQ-Th.png)](http://adronhall.smugmug.com/gallery/7227152_BavAD#466794009_bG2oQ#466794009-A-LB "Wizard # 4 - Adding Data Model.")Wizard # 4 – Adding Data Model.
- [![Wizard # 5 - Adding Data Model.](/images/adronhall.smugmug.com/photos/466794024_N6MnJ-Th.png)](http://adronhall.smugmug.com/gallery/7227152_BavAD#466794024_N6MnJ#466794024-A-LB "Wizard # 5 - Adding Data Model.")Wizard # 5 – Adding Data Model.

.smugcontainer div {overflow: hidden;line-height: 1.1;margin-top: 10px;font-family: verdana, arial, lucida, sans-serif;font-size: 85%;background-color1: rgb(20, 20, 20);}
.smugimg li {float: left;display: block;width: 160px;height: 200px;background-position: 50% 50%;margin-right: 10px;margin-bottom: 10px;}
.smugimg li img {width: auto; height: auto; border: solid 1px #aaa; background: #555; padding: 2px; vertical-align: middle;}
.smugimg a {display: block;text-align: center;text-decoration: none; color1: rgb(240,240,240);}
.smugimg a:hover img {border: 3px solid #6da6d1; padding: 0px;}

.smugcontainer div {overflow: hidden;line-height: 1.1;margin-top: 10px;font-family: verdana, arial, lucida, sans-serif;font-size: 85%;background-color1: rgb(20, 20, 20);}
.smugimg li {float: left;display: block;width: 160px;height: 200px;background-position: 50% 50%;margin-right: 10px;margin-bottom: 10px;}
.smugimg li img {width: auto; height: auto; border: solid 1px #aaa; background: #555; padding: 2px; vertical-align: middle;}
.smugimg a {display: block;text-align: center;text-decoration: none; color1: rgb(240,240,240);}
.smugimg a:hover img {border: 3px solid #6da6d1; padding: 0px;}

At the end I also deleted the *Class1.cs* file from the project.

I then added a reference to the *Generator.Core Project* in the *TextFileImporter Application Project*.  Next add an application configuration file to the *TextFileImporter Project* with the following configuration section.

```xml
<?xml version="1.0" encoding="utf-8"?>
<configuration>
  <connectionStrings>
    <add name="GeneratorEntities" connectionString="metadata=res://*/Model.Data.csdl|res://*/Model.Data.ssdl|res://*/Model.Data.msl;provider=System.Data.SqlClient;provider connection string=&quot;Data Source=.\carriage;Initial Catalog=Generator;Integrated Security=True;Pooling=False;MultipleActiveResultSets=True&quot;" providerName="System.Data.EntityClient" />
   </connectionStrings>
 </configuration>
```

At the last minute, and to make sure anyone following along with these instructions is really paying attention, I made a minor change to the database table.  I changed the column *Type* to a data type of nvarchar(50).  I then updated the *Data.edmx* file in the *Generator.Core Project*.  To do this open up the file and right click anywhere in the white space around the model.  Then click on *Update Model from Database…*.  Now, as things go, the stupid model didn’t update for me.  This is something that seems to occur very frequetly with the ADO.NET Entity Framework Model Files.  Since it didn’t update I had to manually right click on the *Type Property* and then set the *Type* of the *Type* (yes I know, redundant naming) to *String*.

So if anyone from Microsoft is reading this, the entity model files are STILL broken for some reason.  It’s been about 6 months since the entity framework and such where in beta and they still behave in many ways like they’re in beta, please fix this.  k thx bye.

Next I double clicked the Save (buttonSaveToDb) button and entered the following code to write the file data into the database.

```csharp
private void buttonSaveToDb_Click(object sender, EventArgs e)
{
    if (comboNameType.Text == string.Empty)
    {
        MessageBox.Show("Select a type of name.", "Select Name", MessageBoxButtons.OK,
                        MessageBoxIcon.Information, MessageBoxDefaultButton.Button1);
    }
    else
    {
        // TODO Write to DB.
        var generatorEntities = new GeneratorEntities();
        foreach (var name in Names)
        {
            var newName =
                new Names
                    {
                        NameId = Guid.NewGuid(),
                        Name = name,
                        Type = comboNameType.Text
                    };
            generatorEntities.AddToNames(newName);
        }
        generatorEntities.SaveChanges(true);
    }
}
```

Then a quick reference and that finishes up the *TextFileImporter Project*.

```csharp
using Generator.Core.Model;
```

Now mind you, I broke TDD principles because this app was merely a utility, would be used a few times, and above all breaks isolation and crosses boundaries.  A good rule is to not write tests for a project like this.  Unless you feel it absolutely necessary then I wouldn’t even think of it.

Now run the application and open and import each of the three files into the database.  This will give us the data we need for the next step of our random name generator.
