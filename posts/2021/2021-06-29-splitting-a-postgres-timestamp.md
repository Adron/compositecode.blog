---
title: Splitting a Postgres Timestamp with Generated Columns & GraphQL Query with Hasura
date: 2021-06-29 22:55:57 -0700
last_modified_at: 2021-06-29 22:55:57 -0700
permalink: /2021/06/29/splitting-a-postgres-timestamp/
slug: splitting-a-postgres-timestamp
wp_id: 64043
original_url: https://compositecode.blog/2021/06/29/splitting-a-postgres-timestamp/
categories:
- Databases
tags:
- database
- graphql
- hasura
- postgres
- sql
excerpt: Recently I created a video short on how to split out a timestamp column for Hasura. This included the SQL for Postgres via a schema migration and also details on how this appears in the Hasura user interface. You can check out the video here.
image: /wp-content/uploads/2020/04/devto-programming.jpg
---

Recently I created a video short on how to split out a timestamp column for Hasura. This included the SQL for Postgres via a schema migration and also details on how this appears in the Hasura user interface. You can check out the video here.

<iframe allowfullscreen="true" class="youtube-player" height="486" loading="lazy" sandbox="allow-scripts allow-same-origin allow-popups allow-presentation allow-popups-to-escape-sandbox" src="https://www.youtube.com/embed/i4clYumFacM?version=3&amp;rel=1&amp;showsearch=0&amp;showinfo=1&amp;iv_load_policy=1&amp;fs=1&amp;hl=en-US&amp;autohide=2&amp;wmode=transparent" style="border:0;" width="863"></iframe>

The break out of what I show in the video is available in a Github repository also.

<https://github.com/Adron/graphql-relational-concept-mapping>

## Postgres Table Creation SQL

Here is the specific database query that creates the table with the timestamp being broken out to the year, month, and day as generated column data.

```
create table standard_relational_model.users_data
(
    user_id uuid PRIMARY KEY,
    address_id uuid,
    signup_date timestamp DEFAULT now(),
    year int  GENERATED ALWAYS AS (date_part('year', signup_date)) STORED,
    month int  GENERATED ALWAYS AS (date_part('month', signup_date)) STORED,
    day int  GENERATED ALWAYS AS (date_part('day', signup_date)) STORED,
    points int,
    details jsonb
);
```

In this SQL the `signup_date` column is the timestamp column that I want split out to year, month, and day. I’ve set it up with a default function call of `now()` just to seed the column and not require entry when inserting a new row. With that seed, then the generated columns of year, month, and day use the `date_part()` function to extract the particular value out of the `signup_date` column and store it in the respective column.

The other columns are just there for other references.

## The Hasura Console

In the Hasura Console those columns would look something like this.

[![](/wp-content/uploads/2021/06/hasura-console.png)](/wp-content/uploads/2021/06/hasura-console.png)

Notice the syntax displayed for these is different than the migration that created them.

```
date_part('day'::text, signup_date)
```

The above of course is for day, and each respective part is designated by month, year, etc.

When the data is added to the table the results return as follow with GraphQL and results.

### GraphQL

The query.

```
query MyQuery {
   users_data {
    signup_date
    year
    month
    day
  }
}
```

The results.

```
{
  "data": {
    "users_data": [
      {
        "signup_date": "1999-04-21T00:00:00",
        "year": 1999,
        "month": 4,
        "day": 21
      },

            ... etc ...

      {
        "signup_date": "2007-01-02T00:00:00",
        "year": 2007,
        "month": 1,
        "day": 2
      },
      {
        "signup_date": "2021-06-29T00:09:48.359247",
        "year": 2021,
        "month": 6,
        "day": 29
      }
    ]
  }
}
```

### SQL

The query.

```
select signup_date, year, month, day
from standard_relational_model.users_data;
```

The results.

```
1999-04-21 00:00:00.000000,1999,4,21
2012-07-04 00:00:00.000000,2012,7,4
2019-06-24 00:00:00.000000,2019,6,24
2013-03-07 00:00:00.000000,2013,3,7
2007-01-02 00:00:00.000000,2007,1,2
2021-06-29 00:09:48.359247,2021,6,29
```

That is how to build generated columns in Postgres and how they’re available via Hasura to expose via GraphQL!
