---
title: Beyond CRUD n’ Cruft Data-Modeling
date: 2019-11-25 14:31:17 -0800
last_modified_at: 2020-06-26 15:20:20 -0700
permalink: /2019/11/25/beyond-crud-n-cruft-data-modeling/
slug: beyond-crud-n-cruft-data-modeling
wp_id: 16531
original_url: https://compositecode.blog/2019/11/25/beyond-crud-n-cruft-data-modeling/
categories:
- Databases
- Trains
tags:
- crud
- data
- data modeling
- data schema
- passenger trains
- railroads
- schema
- schema design
- train
excerpt: I dig through a lot of internet results and blog entries that show CRUD data modeling all the time. A lot of these blog entries and documentation are pretty solid. Unfortunately, rarely do we end up with data that is accurately or precisely modeled the way it ought to be or the way we would …
image: /wp-content/uploads/2019/11/img_0743-x3.jpg
---

I dig through a lot of internet results and blog entries that show CRUD data modeling all the time. A lot of these blog entries and documentation are pretty solid. Unfortunately, rarely do we end up with data that is accurately or precisely modeled the way it ought to be or the way we would ideally use it. In this post I’m going to take some sample elements of data and model it out for various uses. Then reconstitute that data into different structures for various uses within microservices, loading, reading, both in normalized form and denormalized form.

## The Domain: Railroad Systems & Services

The domain I chose for this particular example is the entire global spectrum of rail services. Imagine if you would a system that can track all the trains in the world, or even just the trains in a particular area of the world, like the United States. In the United States the trains can be broken down into logical structures of data for various things like freight trains and passenger trains. Trains operated under a particular operator like Amtrak, Union Pacific, or Norfolk Southern, and their respective consists that the train is made up of. Let’s get into some particular word definitions to fully detail this domain.

- **Train** – A train is an engine, or motorized unit, that generally pulls other cargo or passenger units.
- **Engine** – An engine is a specialized unit that is used to pull or push a train.
- **Consist** – A consist is the description, or list, of units that make up a train. Often referred to as the *train consist*.
- **![IMG_3575-X4.jpg](/wp-content/uploads/2019/11/img_3575-x4.jpg)Passenger Car** – A vehicle unit within a consist used to carry passengers, in which passengers are one or more humans being carried between origin and destination.
- **Freight Car** – A vehicle unit within a consist to carry freight of some type. This could be coal, wood, iron, general goods, or other items.
- **Schedule** – This is a list of time points that a train will depart and/or arrive from through the course of a trip.
- **Trip** – A journey from a designated origin to a designated destination.
- **Time Point** – This is an entry item in a schedule which provides some detail around the departure or arrival, or both, of a train traveling along a schedule that is on a trip. A time point is also a specific detailed geographic location within a a trip.
- **Destination** – A point along a trip, in which a train arrives at and may depart from, or the final arrival point in a trip that the train arrives at but marks the trip complete.
- **Origin** – A geographic and time based point that marks the beginning of a trip.
- **Load** – The content, either persons or cargo, that are carried on a particular train or on a particular unit within a train consist.
- **Class I Railroad** – The metrics in which a Class I Railroad is defined has changed numerous times over the years, but the quick summary is Class I railroads today are the largest rail service providers in the United States, meeting service, revenue, and other various measurements. There are also Class II and Class III railroads, again, meeting various metrics that over the years have changed.

> ***Trivia:*** Did you know that [Bill Gates is the largest shareholder of Canadian National Railway Company](https://en.m.wikipedia.org/wiki/Canadian_National_Railway)? He owns a massive 13% in the railroad operator as of 2019.

Now let’s get this modeled out into some usable schema. It’s important to note that whenever you receive data that you expect to actually use or display, it’s always in some type of format, schema, or other structured form. The idea that data is schemaless is a red herring and/or strawman argument when we’re trying to make something of the data. Building to a schemaless design just means you’re going to be dealing with voluminous garbage. There’s a reason that many systems, and in Comp Sci 101, they teach GIGO, or “*Garbage In Garbage Out*“!

In this scenario we’re going to keep the data cleaned up, but in the respective formats that give us the best availability and access to the data.

### Model 1 – Data Received

![banner4](/wp-content/uploads/2019/11/banner4.jpg)The following is how I managed to receive this data. Some collected from Wikipedia, some from specific systems, and some of it is generalized or made to just represent real systems. All of it is indeed representative of real railroads running train operations throughout the United States. Later, when data can be made available, we can add other nations and rail systems. For this post I’m going to focus solely on the United States.

The following are what are designated as “Class I” Railroads within the United States National Rail System.

- [Amtrak](https://www.amtrak.com/) – Intercity Passenger Rail for the United States and parts of Canada.
- ![IMG_7247-X3](/wp-content/uploads/2019/11/img_7247-x3.jpg)[Burlington Northern Santa Fe (BNSF)](https://www.bnsf.com/)
- [Norfolk Southern (NS)](http://www.nscorp.com/)
- [Union Pacific (UP)](https://www.up.com/)
- [CSX (CSX)](https://www.csx.com/)
- [Kansas City Southern (KCS)](https://www.kcsouthern.com/)
- [Canadian National (CN)](https://www.cn.ca/)
- [Canadian Pacific (CP)](https://www.cpr.ca/)

Just for fun I’m adding the following systems out here on the West Coast. When time allows, maybe I can add the east coast and Chicago systems. Which would give us a LOT more to work with! But for now this is enough.

- [Sounder](https://en.wikipedia.org/wiki/Sounder_commuter_rail) – Seattle Commuter Rail owned by Sound Transit and operated by BNSF.
- [Caltrain](https://en.wikipedia.org/wiki/Caltrain) – San Francisco to San Jose Commuter Rail.
- [Metrolink](https://en.wikipedia.org/wiki/Metrolink_(California)) – Los Angeles Commuter Rail.
- [Coaster](https://www.gonctd.com/services/coaster-commuter-rail/) – San Diego Commuter Rail operated by Bombardier Transportation.

> ***Trivia:*** Did you know that [Warren Buffet is the largest shareholder of the Burlington Northern Santa Fe (BNSF)](https://en.wikipedia.org/wiki/BNSF_Railway)? Well, technically he’s not just the largest shareholder but his firm Berkshire Hathaway (NYSE: BRK-B) bought BNSF in 2010 for $26.5 billion, the biggest acquisition Buffett has made.

Looking at this data I put together (*via some Twitch streams [here finding the dbschema tool](https://youtu.be/P6pPBt-Eams), [here learning about more maps, rail systems, and further schema design](https://youtu.be/e0bL4DePSvw), and I’ll write up the others in a future blog post*) a first shot at a data model around this. To do this I found this tool at <https://dbdiagram.io> to build out a schema by writing out the schema itself, here’s what I ended up with for now.

![diagram](/wp-content/uploads/2019/11/diagram.png)

*The dbdiagram Interface with Schema Configuration*

With that put together, the other cool feature this tool has is the option to generate the SQL for PostgreSQL, mySQL, or SQL Server. That’ll give me a perfect start for taking one of those and tweaking it for CQL. The end product looked like this for the first schema.

```
CREATE TABLE IF NOT EXISTS "Consist" (
  "id" uuid ,
  "trainId" uuid,
  "unitId" uuid,
  "details" text,
  PRIMARY KEY ("trainId", "unitId")
);

CREATE TABLE IF NOT EXISTS "Unit" (
  "id" uuid ,
  "typeId" uuid,
  "name" text,
  "started" date,
  "age" int,
  "mileage" int,
  "load" map<text,text>,
  "ladenWeight" int,
  "unitWeight" int,
  PRIMARY KEY ( id, "typeId", name, started )
);

CREATE TABLE IF NOT EXISTS "UnitType" (
  "id" uuid ,
  "name" text,
  "description" text,
  "unitLoadType" map<text,text>,
  PRIMARY KEY ( id, name )
);

CREATE TABLE IF NOT EXISTS "Operator" (
  "id" uuid ,
  "trainId" uuid,
  "railroadId" uuid,
  "details" text,
  PRIMARY KEY ( id, "trainId", "railroadId" )
);

CREATE TABLE IF NOT EXISTS "Railroad" (
  "id" uuid ,
  "name" text,
  "history" text,
  "description" text,
  "hqCity" text,
  "hqAddress" text,
  "homepage" text,
  "abbreviation" text,
  "serviceArea" text,
  "mapLink" text,
  PRIMARY KEY ( id, name, "hqCity", "serviceArea" )
);

CREATE TABLE IF NOT EXISTS "Schedule" (
  "id" uuid ,
  "timePointId" uuid,
  "name" text,
  primary key ( id, "timePointId", name )
);

CREATE TABLE IF NOT EXISTS "TimePoints" (
  "id" uuid ,
  "name" text,
  "type" text,
  "desription" text,
  "arrival" timestamp,
  "departure" timestamp,
  primary key ( id, name, type, arrival, departure )
);

CREATE TABLE IF NOT EXISTS "TrainSchedules" (
  "trainId" uuid,
  "scheduleId" uuid,
  primary key ( "trainId", "scheduleId" )
);

CREATE TABLE IF NOT EXISTS "dtTrainConsist" (
  "trainName" varchar,
  "operatorName" text,
  "trainStarted" date,
  "trainEnded" date,
  "trainDescription" text,
  "trainNotes" text,
  "unitName" text,
  "unitStarted" date,
  "unitAge" int,
  "unitMileage" int,
  "unitTypeName" text,
  "unitLadenWeight" int,
  "unitWeight" int,
  "unitLoad" map,
  primary key ( "trainName" )
);

CREATE TABLE IF NOT EXISTS "dtRailroadTrains" (
  "trainName" varchar,
  "operatorName" text,
  "trainStarted" date,
  "trainEnded" date,
  "trainDescription" text,
  "trainNotes" text,
  primary key ( "trainName" )
);
```

Alright now I’ve got some tables to work with. Some of these primary keys and other elements may need to change, I’ll need additional tables, but this again, is a rough draft of the schema design so far! With schema migrations written out and stored in a repo, and additional data for core tables available too it’ll be really quick and relatively painless to build out and tear down the database whenever I need it. I’ve also added below the following INSERT statements to get the initial load of data, as detailed in the above post, into the database. Once I get more of the data into these tables it’ll also dictate where changes need to occur, what additions should be made, and other table schema alterations.

### Model 1 – Inserting Data

First I need the railroads, which I’ve listed above, that I’m going to endeavor to collect data on. Let’s get all the big ones, plus the commuter lines I mentioned above added. Here’s the scripts for that.

```
INSERT INTO railroads."Railroad" (id, name, "hqCity", "serviceArea", description, history, "mapLink", "hqaddress", homepage, abbreviation, active)
VALUES (d2f92bf0-1d0e-461b-8758-8448703f6bd4,'Amtrak','Washington DC','US,CA','Intercity Passenger Rail for the United States and parts of Canada.', '', 'https://en.wikipedia.org/wiki/Amtrak#/media/File:Amtrak_network_map_2016.png', '400 North Capitol Street, NW, Washington DC', 'https://www.amtrak.com/', 'AMTK', true) IF NOT EXISTS;

INSERT INTO railroads."Railroad" (id, name, "hqCity", "serviceArea", description, history, "mapLink", "hqaddress", homepage, abbreviation, active)
VALUES (782ea70a-1db3-4973-9b89-b70ecdb07cce,'Alaskan Railroad','Anchorage','US','', '', 'https://en.wikipedia.org/wiki/Alaska_Railroad#/media/File:Alaska_Railroad_Map.PNG', 'P. O. Box 107500, Anchorage, Alaska 99510-7500', 'https://www.alaskarailroad.com/', 'ARR', true) IF NOT EXISTS;

INSERT INTO railroads."Railroad" (id, name, "hqCity", "serviceArea", description, history, "mapLink", "hqaddress", homepage, abbreviation, active)
VALUES (77f86288-60a1-469d-8dee-862ed8c9cd92, 'Burlington Northern Santa Fe', 'Fort Worth', 'US', '', '', 'https://en.wikipedia.org/wiki/BNSF_Railway#/media/File:BNSF_Railway_system_map.svg', '2650 Lou Menk Drive in TX, Fort Worth, 76131','https://www.bnsf.com/','BNSF', true) IF NOT EXISTS;

INSERT INTO railroads."Railroad" (id, name, "hqCity", "serviceArea", description, history, "mapLink", "hqaddress", homepage, abbreviation, active)
VALUES (be882dfb-6bc9-4d9e-bba0-0f65b3a9e6e0, 'Norfolk Southern', 'Norfolk', 'US', '', '', 'https://en.wikipedia.org/wiki/Norfolk_Southern_Railway#/media/File:Norfolk_Southern_Railway_system_map.svg', 'Norfolk, VA','http://www.nscorp.com/','NS', true) IF NOT EXISTS;

INSERT INTO railroads."Railroad" (id, name, "hqCity", "serviceArea", description, history, "mapLink", "hqaddress", homepage, abbreviation, active)
VALUES (f0914110-e4ff-499a-b4f1-27b4cb7b21ef, 'Union Pacific', 'Omaha', 'US', '', '', 'https://en.wikipedia.org/wiki/Union_Pacific_Railroad#/media/File:Union_Pacific_Railroad_system_map.svg', '1400 Douglas Street, Omaha, Nebraska 68179','https://www.up.com/','UP', true) IF NOT EXISTS;

INSERT INTO railroads."Railroad" (id, name, "hqCity", "serviceArea", description, history, "mapLink", "hqaddress", homepage, abbreviation, active)
VALUES (35819552-c1bc-44c9-ba41-c07ac920d046, 'CSX', 'Jacksonville', 'US', '', '', 'https://en.wikipedia.org/wiki/File:CSX_Transportation_system_map.svg', '500 Water Street, 15th Floor Jacksonville, FL 32202','https://www.csx.com/','CSX', true) IF NOT EXISTS;

INSERT INTO railroads."Railroad" (id, name, "hqCity", "serviceArea", description, history, "mapLink", "hqaddress", homepage, abbreviation, active)
VALUES (892b6ecc-272c-4b71-b575-356fec9b9377, 'Kansas City Southern', 'Kansas City', 'US,MX', '', '', 'https://en.wikipedia.org/wiki/Kansas_City_Southern_(company)#/media/File:Kansas_City_Southern_Railway_system_map.svg', '427 W 12th St, Kansas City, MO 64105', 'https://www.kcsouthern.com/', 'KCS', true) IF NOT EXISTS;

INSERT INTO railroads."Railroad" (id, name, "hqCity", "serviceArea", description, history, "mapLink", "hqaddress", homepage, abbreviation, active)
VALUES (0fcc2e09-a3c1-4a50-9ce2-adce93e3eaba, 'Canadian National', 'Montreal', 'CA,US', '', '', 'https://upload.wikimedia.org/wikipedia/commons/7/78/Canadian_National_System_Map.PNG', '935 de La Gauchetière Street West, Montreal, Quebec, H3B 2M9','https://www.cn.ca/','CN', true) IF NOT EXISTS;

INSERT INTO railroads."Railroad" (id, name, "hqCity", "serviceArea", description, history, "mapLink", "hqaddress", homepage, abbreviation, active)
VALUES (35836bb3-d7a3-49c6-9b08-2a1baa369fe9, 'Canadian Pacific', 'Calgary', 'CA,US', '', '', 'https://en.wikipedia.org/wiki/Canadian_Pacific_Railway#/media/File:Canadian_Pacific_System_Railmap.PNG', '7550 Ogden Dale Road S.E.. Calgary, Alberta T2C 4X9 Canada','https://www.cpr.ca/','CP', true) IF NOT EXISTS;

INSERT INTO railroads."Railroad" (id, name, "hqCity", "serviceArea", description, history, "mapLink", "hqaddress", homepage, abbreviation, active)
VALUES (c924c7a4-13cb-415e-9dcd-db38b0b6548c, 'Sounder', 'Seattle', 'Seattle Metro', '', '', 'https://s3.amazonaws.com/nycsubway.org/images/maps/soundermap.gif', '401 S. Jackson St. Seattle, WA 98104','https://www.soundtransit.org/','', true) IF NOT EXISTS;

INSERT INTO railroads."Railroad" (id, name, "hqCity", "serviceArea", description, history, "mapLink", "hqaddress", homepage, abbreviation, active)
VALUES (4a60a6a6-e0bf-4e23-8624-cafdee006994, 'Caltrain', 'San Carlos', 'San Francisco Metro', 'Commuter rail service from San Francisco to Gilroy.', '', 'http://www.caltrain.com/Assets/maps/Caltrain+Zone+Map.png', '1250 San Carlos Ave, San Carlos, CA 94070','http://www.caltrain.com/','', true) IF NOT EXISTS;

INSERT INTO railroads."Railroad" (id, name, "hqCity", "serviceArea", description, history, "mapLink", "hqaddress", homepage, abbreviation, active)
VALUES (e586e8ff-9865-4df3-b336-71be8e285609, 'Metrolink', 'Los Angeles', 'Los Angeles Metro', '', '', 'https://en.wikipedia.org/wiki/List_of_Metrolink_(California)_stations#/media/File:Metrolink_California_map_to_scale.png', '800 N. Alameda St., Los Angeles, CA 90012','https://www.metrolinktrains.com/','', true) IF NOT EXISTS;

INSERT INTO railroads."Railroad" (id, name, "hqCity", "serviceArea", description, history, "mapLink", "hqaddress", homepage, abbreviation, active)
VALUES (dd8ee187-21d7-4572-b7d8-7df65ca040db, 'Coaster', 'Oceanside', 'San Diego Metro', 'San Diego Metro commuter rail.', '', 'https://en.wikipedia.org/wiki/Coaster_(commuter_rail)#/media/File:San_Diego_commuter_rail_map.png', '205 South Tremont Street, Oceanside, CA','https://gonctd.com/','NCTD', true) IF NOT EXISTS;
```

To view the data once it is entered, I just ran a quick `SELECT * FROM railroads."Railroad"`. At this point I’ve got baseline list of railroads in the United States. Also for the baseline I’ve decided to add some well known passenger trains that have a routine consist, travel a known route, and can provide good examples for what a consist would be made up of. To put together a name train and its respective consist I need to populate several other tables with the pertinent information related ot the units within the consist and the types of units. For the initial set of named trains I’m going to enter, I’ve added the following unit types and units for building the initial train consists.

```
INSERT INTO railroads."UnitType" (id, name, description, "unitLoadType")
VALUES (db960405-dfa9-4010-b01a-2a0bbbfef27f,'Superliner Coach','62 seats upper level & 12 seats lower level.',{'passenger':'74'})  IF NOT EXISTS;

INSERT INTO railroads."UnitType" (id, name, description, "unitLoadType")
VALUES (cc38cc12-93dd-4975-a190-666001636411,'Superliner Coach','Amtrak California coach with 76 seats upper level & 20 seats lower level.',{'passenger':'96'})  IF NOT EXISTS;

INSERT INTO railroads."UnitType" (id, name, description, "unitLoadType")
VALUES (45ba7e8d-f954-45ba-a1f1-184eef21eebb,'Superliner Coach/Snack Bar','62 seats upper level & snack bar lower level.',{'passenger':'62'})  IF NOT EXISTS;

INSERT INTO railroads."UnitType" (id, name, description, "unitLoadType")
VALUES (77e57722-4186-4a74-9d6b-72e99a669944,'Superliner Coach/Baggage','78 seats upper level & baggage lower level.',{'passenger':'78'})  IF NOT EXISTS;

INSERT INTO railroads."UnitType" (id, name, description, "unitLoadType")
VALUES (aa1f0c6a-5bc4-4bff-8463-e5fbe4c4a753,'Superliner Dining','18 4-top Tables in the upper level with kitchen on the lower level.',{'passenger':'0'})  IF NOT EXISTS;

INSERT INTO railroads."UnitType" (id, name, description, "unitLoadType")
VALUES (94247de0-7f8f-41a0-b41d-9a330edd2c05,'Superliner Sightseer Lounge','8 4-top tables, 29 seats, and bar upper level, with 2 4-top tables, 2 large general seating tables, and snack bar lower level.',{'passenger':'0'})  IF NOT EXISTS;

INSERT INTO railroads."UnitType" (id, name, description, "unitLoadType")
VALUES (e82339ae-fabf-4467-8490-2302a728557a,'Superliner Sleeper','The standard Superliner sleeping car contains 14 roomettes, five bedrooms, a family bedroom, and an accessible bedroom.',{'passenger':'44'}) IF NOT EXISTS;

INSERT INTO railroads."UnitType" (id, name, description, "unitLoadType")
VALUES (69cc0e8b-b0a1-4899-aed4-e30cbf9e3098,'Superliner Deluxe Sleeper','The deluxe sleeping car contains ten bedrooms, four roomettes, a family bedroom, and an accessible bedroom.',{'passenger':'34'})  IF NOT EXISTS;

INSERT INTO railroads."UnitType" (id, name, description, "unitLoadType")
VALUES (e012517c-81be-4f48-9372-8c70912ac7ca,'Superliner Transition Sleeper','The transition is setup for crew and some overflow customer rooms with 17 roomettes.',{'passenger':'0'})  IF NOT EXISTS;

INSERT INTO railroads."UnitType" (id, name, description, "unitLoadType")
VALUES (7b1f0e4c-ca39-4f88-9424-412fca1e4299,'Pacific Parlour Car','8 plush lounge chairs, 2 inward seating areas (~6 people), 6 4-top tables, and bar kitchen upper level, 20 seat theater lower level.',{'passenger':'0'})  IF NOT EXISTS;

INSERT INTO railroads."UnitType" (id, name, description, "unitLoadType")
VALUES (3bd8c05d-7e23-4bba-b7b6-2e7ee29591b3,'Baggage','Baggage car for passenger trains.',{'passenger':'0'})  IF NOT EXISTS;
```

Now I’ve got the basic unit cars for the consist of most of Amtrak’s western fleet of trains. One more thing however, I need an engine for the model to work accurately. For this sample specifically I’m going to add the mainstay of the Amtrak fleet, the P42DC GENESIS.

```
INSERT INTO railroads."UnitType" (id, name, description, "unitLoadType")
VALUES (1995b4f2-5c93-4466-a54c-1d2838a587c2, 'P42DC GENESIS', 'The common power unit used by Amtrak. The GE P42DC is a ', {'power':'280.25 kN'});
```

Alright, that’s enough for today. You may note, if you’re big into 3NF or other normalization, that the data tables above are in various forms of normalization and denormalization. I’ll discuss the specific reasons and or some of the refactorings coming up more in subsequent blog entries as I get more of the work finished collecting this repository of data. To join me for live coding, data collection and more join me on [Twitch (Follow && || Subscribe!)](https://twitch.tv/adronhall/) where I’ll be live coding the next steps of this progress. Also, subscribe to the blog here, the subscription button is over the left or right or somewhere depending on the device you’re viewing the blog entry with, and of course I’m always toiling about on Twitter [@Adron](https://twitter.com/adron).
