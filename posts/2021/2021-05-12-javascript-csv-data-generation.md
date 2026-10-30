---
title: Dynamic Data Generation with JavaScript
date: 2021-05-12 17:09:05 -0700
last_modified_at: 2021-05-12 17:09:05 -0700
permalink: /2021/05/12/javascript-csv-data-generation/
slug: javascript-csv-data-generation
wp_id: 63810
original_url: https://compositecode.blog/2021/05/12/javascript-csv-data-generation/
categories:
- Databases
- Javascript
tags:
- csv
- data generation
- hasura
- javascript
- postgres
- postgresql
excerpt: I coded up some JavaScript to generate some data for a table recently and it seemed relatively useful, so here it is ready to use as you may. (The complete js file is below the description of the individual code segments below). This file simple data generation is something I put together to create a csv for some quick data imports into a database (Postgres, SQL Server, or anything you may want). With that in mind, I added the libraries and initialized the repo with the libraries I would need.
image: /wp-content/uploads/2021/05/javascript-sizing-n-things.jpg
---

This video shows the process detailed below in this blog entry, to provide the choice of video or a quick read! 👍🏻😁

<iframe allowfullscreen="true" class="youtube-player" height="486" loading="lazy" sandbox="allow-scripts allow-same-origin allow-popups allow-presentation allow-popups-to-escape-sandbox" src="https://www.youtube.com/embed/U2El5fOz5l4?version=3&amp;rel=1&amp;showsearch=0&amp;showinfo=1&amp;iv_load_policy=1&amp;fs=1&amp;hl=en-US&amp;autohide=2&amp;wmode=transparent" style="border:0;" width="863"></iframe>

I coded up some JavaScript to generate some data for a table recently and it seemed relatively useful, so here it is ready to use as you may. (The complete js file is below the description of the individual code segments below). This file simple data generation is something I put together to create a csv for some quick data imports into a database (Postgres, SQL Server, or anything you may want). With that in mind, I added the libraries and initialized the repo with the libraries I would need.

```
npm install faker
npm install fs
```

```
faker = require('faker');
fs = require('fs');
```

Next up I included the column row of data for the csv. I decided to go ahead and setup the variable at this point, as it would be needed as I would add the rest of the csv data to the variable itself. There is probably a faster way to do this, but this was the quickest path from the perspective of getting something working right now.

After the colum row, I also setup the base 8 UUIDs that would related to the project\_id values to randomly use throughout data generation. The idea behind this is that the project\_id values are the range of values that would be in the data that Subhendu would have, and all the ip and other recorded data would be recorded with and related to a specific project\_id. I used a UUID generation site to generate these first 8 values, that site is available [here](https://guidgenerator.com/online-guid-generator.aspx).

After that I went ahead and added the for loop that would be used to step through and generate each record.

```
var data = "id,country,ip,created_at,updated_at,project_id\n";
let project_ids = [
    'c16f6dd8-facb-406f-90d9-45529f4c8eb7',
    'b6dcbc07-e237-402a-bf11-12bf2226c243',
    '33f45cab-0e14-4830-a51c-fd44a62d1adc',
    '5d390c9e-2cfa-471d-953d-f6727972aeba',
    'd6ef3dfd-9596-4391-b0ef-3d7a8a1a6d10',
    'e72c0ed8-d649-4c53-97c5-da793d7a8228',
    'bf020fd2-2514-4709-8108-a2810e61c503',
    'ead66a4a-968a-448c-a796-51c6a1da0c20'];

for (var i = 0; i < 500000; i++) {
    // TODO: Generation will go here.
}
```

The next thing that I wanted to sort out are the two dates. One would be the created\_at value and the other the updated\_at value. The updated\_at date needed to show as occurring after the created\_at date, for obvious reasons. To make sure I could get this calculated I added a function to perform the randomization! First two functions to get additions for days and hours, then getting the random value to add for each, then getting the calculated dates.

```
function addDays(datetime, days) {
    let date = new Date(datetime.valueOf());
    date.setDate(date.getDate() + days);
    return date;
}

function addHours(datetime, hours) {
    let time = new Date(datetime.valueOf())
    time.setTime(time.getTime() + (hours*60*60*1000));
    return time;
}

var days = faker.datatype.number({min:0, max:7})
var hours = faker.datatype.number({min:0, max:24})

var updated_at = new Date(faker.date.past())
var created_at = addHours(addDays(updated_at, -days), -hours)
```

With the date time stamps setup for the row data generation I moved on to selecting the specific project\_id for the row.

```
var proj_id = project_ids[faker.datatype.number({min:0, max: 7})]
```

One other thing that I knew I’d need to do is filter for the `'` or `,` values located in the countries that would be selected. The way I clean that data to ensure it doesn’t break the SQL bulk import process is kind of cheap and in production data I wouldn’t do this, but it works great for generated data like this.

```
var cleanCountry = faker.address.country().replace(",", " ").replace("'", " ")
```

If you’re curious why I’m calculating these before I do the general data generation and set the row up, I like to keep the row of actual data calls to either a set variable assignment or at most one dot level deep in my calls. As you’ll see now in the row level data being generated below.

```
data2 +=
    faker.datatype.uuid() + "," +
    cleanCountry + "," +
    faker.internet.ip() + "," +
    created_at.toISOString() + "," +
    updated_at.toISOString() + "," +
    proj_id + "\n"
```

Now the last step is to create the file for all these csv rows.

```
fs.writeFile('kundu_table_data.csv', data, function (err) {
  if (err) return console.log(err);
  console.log('Data file written.');
});
```

The results.
