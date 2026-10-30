---
title: Chat GPT-4 SQL Refactoring for PostgreSQL
date: 2023-10-25 19:57:37 -0700
last_modified_at: 2023-10-25 19:57:37 -0700
permalink: /2023/10/25/chat-gpt-4-sql-refactoring-for-postgresql/
slug: chat-gpt-4-sql-refactoring-for-postgresql
wp_id: 66938
original_url: https://compositecode.blog/2023/10/25/chat-gpt-4-sql-refactoring-for-postgresql/
categories:
- App Building
- Databases
- Music Collectors
tags:
- data model
- database
- database refactor
- entity model
- entity model diagram
- relational database
- relational database design
excerpt: I wanted to do some refactoring to the previous SQL DDL I put together for music collectors. To add a little twist to the refactor I decided to do it all with Chat GPT-4 to see how it would do. This is the result!
image: /wp-content/uploads/2023/10/database-refactor.jpg
---

Just recently I wrote up a [post about a multi-tenant database for music collectors](/2023/10/23/building-a-multi-tenant-music-collectors-database/). That SQL was the first draft I put together to cover some of the basic data points and relations the database would need to have to provide the multi-tenant capabilities. However, there are a number of refactorings that I’d like done before I get started developing against this particular database. For this, I could just go through the refactorings with something like DataGrip or one of the other IDEs or other tools that I’ve used. But instead, for this exercise I decided why not give Chat GPT-4 algo a shot?

***This is my experience refactoring SQL with Chat GPT-4***.

Fired up the site and logged in.

[![](/wp-content/uploads/2023/10/CleanShot-2023-10-25-at-10.47.14.gif)](/wp-content/uploads/2023/10/CleanShot-2023-10-25-at-10.47.14.gif)

I started with the [exact SQL from the previous post](/2023/10/23/building-a-multi-tenant-music-collectors-database/). Several of the things I wanted refactored immediately included:

- I want to have the SERIAL data type changed to UUID.
- I want the VARCHAR(255) changed to a VARCHAR(120)

I started off with this first refactoring by asking for the following via the Chat-GPT prompt.

```
For the following SQL, rewrite it so that all the SERIAL types are changed to UUID types.

CREATE TABLE "tenants" (
  "tenant_id" SERIAL PRIMARY KEY,
  "name" VARCHAR(255) NOT NULL,
  "created" TIMESTAMP DEFAULT (CURRENT_TIMESTAMP),
  "updated" TIMESTAMP DEFAULT (CURRENT_TIMESTAMP),
  "notes" TEXT,
  "message" TEXT
);

...all the other SQL here...
```

After about a minute it wrapped up doing the refactor, but something extra happened that I did not expect. As it did this, it had inferred that this was obviously a request that is PostgreSQL specific. Being such, it also swapped the default settings for the different identity columns and finished up the post with this.

[![](/wp-content/uploads/2023/10/CleanShot-2023-10-25-at-12.27.41.png)](/wp-content/uploads/2023/10/CleanShot-2023-10-25-at-12.27.41.png)

That’s rather interesting, consider that one would indeed need to have pgcrypto installed to be able to setup identity columns like this `"id" UUID PRIMARY KEY DEFAULT uuid_generate_v4()`. A very useful addition! This AI thing might be useful yet!

Next up fired off the refactor to *replace the VARCHAR(255) with VARCHAR(120)* to see how that would unfold. The result was, simply put, the refactor that was requested. No extra extensions, suggestions, or otherwise, which in this case makes sense.

## Genres, The Complexity and Heaviness of The Concept. #IYKYK

One of the things, among the bands table, I had added a column simply titled “genre”. After some thought I realized that this was a mistake! A big mistake for those that are interested in determining, to the Nth degree, what genre a particular album or song or band fits into. So I gave it some thought, and requested a refactor to the AI to see what I’d get.

My request read as

```
For the genres in the bands table, remove that and create a table for genres, with an elephant ear relationship back to itself to allow for a nested hierarchy of genre and sub-genres, then add the audit tables you've added for the other tables.
```

The result from that gave me the following `CREATE TABLE` addition to the overall DDL.

```
CREATE TABLE "genres" (
  "genre_id" UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  "parent_genre" UUID,
  "genre" VARCHAR(120),
  "created" TIMESTAMP DEFAULT (CURRENT_TIMESTAMP),
  "updated" TIMESTAMP DEFAULT (CURRENT_TIMESTAMP),
  "notes" TEXT,
  "message" TEXT
);
```

Simple, to the point, and exactly what I’d asked for. On this third refactor request, another perfect score. Next up, I needed to have some tables that would utilize a relationship to this particular table itself. I provided Chat GPT-4 the following request,

```
In above SQL, create a table for a many to many relationship between the 'bands' table and the 'genres' table so that a user can associate multiple genres to a single band and by relation many bands to a genre.
```

Again, the result was spot on.

[![](/wp-content/uploads/2023/10/CleanShot-2023-10-25-at-18.58.15.png)](/wp-content/uploads/2023/10/CleanShot-2023-10-25-at-18.58.15.png)

I was a little hesitant since the table was just set out as an independent result. I decided to try asking for Chat GPT-4 to write out the full SQL with the added table.

```
In above SQL, write out all of the existing SQL and add a table for a many to many relationship between the 'bands' table and the 'genres' table so that a user can associate multiple genres to a single band and by relation many bands to a genre.
```

This worked, but for some odd reason I ended up with an additional rogue table called “band\_genres” which only had the audit columns and absolutely nothing else in that table. I decided to ask for the same SQL result but exclude that table.

```
In the last answer, write out all the SQL again but exclude the "band_genres" table.
```

That got things cleaned back up and ready for the next refactor. For that, I requested the following list of changes. Largely to see what would happen if I asked for more than one thing to be done in a request.

```
Copy the previous SQL and print it out again, but make the following changes:

1. Add to the tenant table the following columns: organization, website, and founding_date with their pertinent data types.
2. Change the duration data type in the songs table to be of type int.
3. For the column songwriter in the songs table change it to relate by id to the band_members in a many to many table so that a song can have multiple writers.
```

With those changes in place I decided to really check on the validity of the SQL that Chat GPT-4 had written up. The end result was this SQL.

```
CREATE TABLE "tenants" (
  "tenant_id" UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  "name" VARCHAR(120) NOT NULL,
  "organization" VARCHAR(120),
  "website" VARCHAR(120),
  "founding_date" DATE,
  "created" TIMESTAMP DEFAULT (CURRENT_TIMESTAMP),
  "updated" TIMESTAMP DEFAULT (CURRENT_TIMESTAMP),
  "notes" TEXT,
  "message" TEXT
);

CREATE TABLE "users" (
  "user_id" UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  "tenant_id" UUID,
  "username" VARCHAR(120) NOT NULL,
  "password" VARCHAR(120) NOT NULL,
  "created" TIMESTAMP DEFAULT (CURRENT_TIMESTAMP),
  "updated" TIMESTAMP DEFAULT (CURRENT_TIMESTAMP),
  "notes" TEXT,
  "message" TEXT
);

CREATE TABLE "roles" (
  "role_id" UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  "tenant_id" UUID,
  "name" VARCHAR(120) NOT NULL,
  "can_add" BOOLEAN DEFAULT FALSE,
  "can_edit" BOOLEAN DEFAULT FALSE,
  "can_delete" BOOLEAN DEFAULT FALSE,
  "created" TIMESTAMP DEFAULT (CURRENT_TIMESTAMP),
  "updated" TIMESTAMP DEFAULT (CURRENT_TIMESTAMP),
  "notes" TEXT,
  "message" TEXT
);

CREATE TABLE "user_roles" (
  "user_id" UUID,
  "role_id" UUID,
  PRIMARY KEY ("user_id", "role_id")
);

CREATE TABLE "musicians" (
  "musician_id" UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  "tenant_id" UUID,
  "name" VARCHAR(120) NOT NULL,
  "date_of_birth" DATE,
  "biography" TEXT,
  "created" TIMESTAMP DEFAULT (CURRENT_TIMESTAMP),
  "updated" TIMESTAMP DEFAULT (CURRENT_TIMESTAMP),
  "notes" TEXT,
  "message" TEXT
);

CREATE TABLE "bands" (
  "band_id" UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  "tenant_id" UUID,
  "name" VARCHAR(120) NOT NULL,
  "formation_date" DATE,
  "country_of_origin" VARCHAR(120),
  "city_of_origin" VARCHAR(120),
  "active_status" BOOLEAN DEFAULT TRUE,
  "biography" TEXT,
  "website" VARCHAR(120),
  "social_media_links" TEXT,
  "label" VARCHAR(120),
  "discography" TEXT,
  "manager_name" VARCHAR(120),
  "contact_email" VARCHAR(120),
  "created" TIMESTAMP DEFAULT (CURRENT_TIMESTAMP),
  "updated" TIMESTAMP DEFAULT (CURRENT_TIMESTAMP),
  "notes" TEXT,
  "message" TEXT
);

CREATE TABLE "genres" (
  "genre_id" UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  "parent_genre" UUID,
  "genre" VARCHAR(120),
  "created" TIMESTAMP DEFAULT (CURRENT_TIMESTAMP),
  "updated" TIMESTAMP DEFAULT (CURRENT_TIMESTAMP),
  "notes" TEXT,
  "message" TEXT
);

CREATE TABLE "band_members" (
  "band_member_id" UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  "band_id" UUID,
  "musician_id" UUID,
  "start_date" DATE,
  "end_date" DATE,
  "contribution" TEXT,
  "created" TIMESTAMP DEFAULT (CURRENT_TIMESTAMP),
  "updated" TIMESTAMP DEFAULT (CURRENT_TIMESTAMP),
  "notes" TEXT,
  "message" TEXT
);

CREATE TABLE "albums" (
  "album_id" UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  "band_id" UUID,
  "title" VARCHAR(120) NOT NULL,
  "release_date" DATE,
  "created" TIMESTAMP DEFAULT (CURRENT_TIMESTAMP),
  "updated" TIMESTAMP DEFAULT (CURRENT_TIMESTAMP),
  "notes" TEXT,
  "message" TEXT
);

CREATE TABLE "songs" (
  "song_id" UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  "album_id" UUID,
  "title" VARCHAR(120) NOT NULL,
  "duration" INT,
  "created" TIMESTAMP DEFAULT (CURRENT_TIMESTAMP),
  "updated" TIMESTAMP DEFAULT (CURRENT_TIMESTAMP),
  "notes" TEXT,
  "message" TEXT
);

-- New table for many-to-many relationship between bands and genres
CREATE TABLE "band_genre_association" (
  "band_id" UUID REFERENCES "bands" ("band_id"),
  "genre_id" UUID REFERENCES "genres" ("genre_id"),
  PRIMARY KEY ("band_id", "genre_id")
);

-- New table for many-to-many relationship between songs and band_members (songwriters)
CREATE TABLE "songwriters_association" (
  "song_id" UUID REFERENCES "songs" ("song_id"),
  "band_member_id" UUID REFERENCES "band_members" ("band_member_id"),
  PRIMARY KEY ("song_id", "band_member_id")
);

ALTER TABLE "users" ADD FOREIGN KEY ("tenant_id") REFERENCES "tenants" ("tenant_id");

ALTER TABLE "roles" ADD FOREIGN KEY ("tenant_id") REFERENCES "tenants" ("tenant_id");

ALTER TABLE "user_roles" ADD FOREIGN KEY ("user_id") REFERENCES "users" ("user_id");

ALTER TABLE "user_roles" ADD FOREIGN KEY ("role_id") REFERENCES "roles" ("role_id");

ALTER TABLE "musicians" ADD FOREIGN KEY ("tenant_id") REFERENCES "tenants" ("tenant_id");

ALTER TABLE "bands" ADD FOREIGN KEY ("tenant_id") REFERENCES "tenants" ("tenant_id");

ALTER TABLE "band_members" ADD FOREIGN KEY ("band_id") REFERENCES "bands" ("band_id");

ALTER TABLE "band_members" ADD FOREIGN KEY ("musician_id") REFERENCES "musicians" ("musician_id");

ALTER TABLE "albums" ADD FOREIGN KEY ("band_id") REFERENCES "bands" ("band_id");

ALTER TABLE "songs" ADD FOREIGN KEY ("album_id") REFERENCES "albums" ("album_id");
```

I imported this back into [dbdiagram.io](https://dbdiagram.io/) and everything checked out, test validation passed and the import succeeded. After tweaking the colors of the table header titles in the entity diagram for the tenant and user tables and then the business domain, i.e. the music album collection tables, things looked like this.

[![](/wp-content/uploads/2023/10/image-2.png)](/wp-content/uploads/2023/10/image-2.png)

Got any other suggestions? Additions, removals, edits, or otherwise? Let me know.

With that, the next post I’ll dive into building out an API for this particular database. Stay tuned, be sure to subscribe here to catch any new updates!
