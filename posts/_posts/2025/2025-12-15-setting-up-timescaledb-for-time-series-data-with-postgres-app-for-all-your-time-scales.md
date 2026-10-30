---
title: Setting Up TimescaleDB for Time Series Data with Postgres.app for all your “Time Scales”!
date: 2025-12-15 06:15:00 -0800
last_modified_at: 2026-01-03 16:19:20 -0800
permalink: /2025/12/15/setting-up-timescaledb-for-time-series-data-with-postgres-app-for-all-your-time-scales/
slug: setting-up-timescaledb-for-time-series-data-with-postgres-app-for-all-your-time-scales
wp_id: 73831
original_url: https://compositecode.blog/2025/12/15/setting-up-timescaledb-for-time-series-data-with-postgres-app-for-all-your-time-scales/
categories:
- Databases
tags:
- database
- postgres
- postgresql
excerpt: I used an image from The Geological Society of America‘s “Time Scale” but this isn’t about that, but it kind of is and I’ll have a future post about using TimescaleDB to organize “Time Scale” like this, but that’ll be a little bit in the future. For now, I posted that Time Scale for the …
image: /wp-content/uploads/2025/12/CleanShot-2025-12-14-at-23.21.58@2x.png
---

I used an image from [The Geological Society of America](https://www.geosociety.org/)‘s “Time Scale” but this isn’t about that, but it kind of is and I’ll have a future post about using TimescaleDB to organize “Time Scale” like this, but that’ll be a little bit in the future. For now, I posted that Time Scale for the LOLz. 🤙🏻

I’ve been using TimescaleDB for time-series data on and off for a while now. I recently fired up Postgres.app for local development. It’s one of the cleanest ways to get PostgreSQL running on macOS, and adding TimescaleDB is surprisingly straightforward once you know where to look.

Time-series data is everywhere—sensor readings, application metrics, user events, IoT data. Regular PostgreSQL can handle it, but once you’re dealing with millions of rows, you’ll notice queries slowing down. TimescaleDB solves this by turning your time-series tables into hypertables that automatically partition by time, compress old data, and optimize queries. The best part? It’s still PostgreSQL, so all your existing tools and SQL knowledge work exactly the same.

I’ve built enough dashboards and monitoring systems to know when you need proper time-series handling versus when you can get away with a regular table and a good index. Once you’re dealing with millions of rows and need to query across time ranges efficiently, TimescaleDB is worth the setup.

This assumes you already have Postgres.app installed and running PostgreSQL 18. If you don’t, check out my [Postgres.app setup guide](PostgreSQL%20Local%20Dev%20Setup%20with%20Postgres.app.md) first. Make sure you’re running PostgreSQL 18—you can check the version in Postgres.app’s server status or by running `psql --version` in your terminal.

Here’s what Postgres.app looks like when it’s running. You can see PostgreSQL 18 is active on port 5432 with the default databases ready to go.

[![Postgres.app](/wp-content/uploads/2025/12/postgresql18-app.png)](/wp-content/uploads/2025/12/postgresql18-app.png)

*Postgres.app*

## Installing TimescaleDB

Postgres.app offers TimescaleDB as a downloadable extension installer. This is way cleaner than trying to build it from source or messing with Homebrew—just download and double-click.

Head over to the [Postgres.app Extensions page](https://postgresapp.com/extensions/) and grab the **TimescaleDB package for PostgreSQL 18**. Look for the one labeled “built for PostgreSQL 18” (currently timescaledb 2.23.1). It’s a `.pkg` file that handles everything automatically.

[![Wizard for installing timescaledb 2.23.1.](/wp-content/uploads/2025/12/installing-.png)](/wp-content/uploads/2025/12/installing-.png)

*Wizard for installing timescaledb 2.23.1.*

Once you download it, double-click the `.pkg` installer and follow the prompts. The installer shows you’re installing timescaledb 2.23.1 for PostgreSQL 18 and handles everything: it drops the extension files into `~/Library/Application Support/Postgres/Extensions/18/` and configures PostgreSQL 18 to find them. Postgres.app automatically configures the search paths for extensions installed in this location, so there’s no manual configuration needed.

After installation, restart Postgres.app (stop and start the PostgreSQL 18 server in the app). The extension is now available and ready to enable.

## Setting Up Your First Time Series Database

Let’s create a database for time-series data. I’ll use **metrics** as an example, but name it whatever fits your project:

```
createdb metrics
```

Connect to it:

```
psql metrics
```

[![Postgres.app running the psql CLI app.](/wp-content/uploads/2025/12/postgresql18-app-cli.png)](/wp-content/uploads/2025/12/postgresql18-app-cli.png)

*Postgres.app running the psql CLI app.*

You’ll see `psql (18.1 (Postgres.app))` confirming you’re connected to PostgreSQL 18 via Postgres.app. Nice and clean.

## Enabling TimescaleDB

Inside your database, enable the extension:

```
CREATE EXTENSION IF NOT EXISTS timescaledb;
```

Verify it’s installed:

```
SELECT default_version, installed_version FROM pg_available_extensions WHERE name = 'timescaledb';
```

[![Checking that timescale is installed via psql.](/wp-content/uploads/2025/12/check-for-teimscale.png)](/wp-content/uploads/2025/12/check-for-teimscale.png)

*Checking that timescale is installed via psql.*

You should see both versions listed. If you get an error about the library not being found, make sure you restarted Postgres.app after installing the extension package. I’ve forgotten this step more than once.

## Creating Your First Hypertable

Hypertables are where TimescaleDB gets interesting. They look like regular tables but automatically partition by time behind the scenes. You write queries like normal, but TimescaleDB handles the partitioning magic.

Let’s create a simple metrics table:

```
CREATE TABLE sensor_readings (
    time TIMESTAMPTZ NOT NULL,
    sensor_id INTEGER NOT NULL,
    temperature DOUBLE PRECISION,
    humidity DOUBLE PRECISION,
    pressure DOUBLE PRECISION
);
```

Now convert it to a hypertable by specifying the time column:

```
SELECT create_hypertable('sensor_readings', 'time');
```

That’s it. TimescaleDB automatically creates partitions (chunks) based on time intervals. By default, it creates 7-day chunks, which works well for most use cases. You can customize this if you need different chunk sizes, but the defaults are usually fine.

## Testing It Out

Let’s add some sample data to see it in action:

```
INSERT INTO sensor_readings (time, sensor_id, temperature, humidity, pressure)
VALUES
    (NOW() - INTERVAL '1 hour', 1, 72.5, 45.2, 1013.25),
    (NOW() - INTERVAL '30 minutes', 1, 73.1, 45.8, 1013.30),
    (NOW(), 1, 73.5, 46.1, 1013.35);
```

Query it like a regular table:

```
SELECT * FROM sensor_readings ORDER BY time DESC;
```

Works exactly like a normal PostgreSQL table. The difference is what happens as your data grows—queries stay fast because TimescaleDB only scans the relevant chunks.

## Useful TimescaleDB Features I Actually Use

### Continuous Aggregates

These are materialized views that automatically refresh. I use them all the time for dashboards:

```
CREATE MATERIALIZED VIEW hourly_avg_temperature
WITH (timescaledb.continuous) AS
SELECT
    time_bucket('1 hour', time) AS hour,
    sensor_id,
    AVG(temperature) AS avg_temp,
    MAX(temperature) AS max_temp,
    MIN(temperature) AS min_temp
FROM sensor_readings
GROUP BY hour, sensor_id;
```

The `time_bucket()` function is TimescaleDB-specific and groups data by time intervals. Continuous aggregates refresh incrementally, so you’re not recomputing everything every time. This is what makes dashboards fast even with massive datasets.

### Compression

Enable compression on older data to save space:

```
ALTER TABLE sensor_readings SET (
    timescaledb.compress,
    timescaledb.compress_segmentby = 'sensor_id'
);

SELECT add_compression_policy('sensor_readings', INTERVAL '7 days');
```

This compresses data older than 7 days automatically. TimescaleDB’s compression is impressive—I’ve seen 90%+ compression rates in practice. That sensor data you’re collecting every second? It takes up a fraction of the space it would in a regular PostgreSQL table.

### Retention Policies

Automatically drop old data:

```
SELECT add_retention_policy('sensor_readings', INTERVAL '90 days');
```

This keeps only the last 90 days of data, dropping older chunks automatically. No cron jobs, no manual cleanup scripts. TimescaleDB handles it.

## Connection Strings

Your connection string stays the same as regular PostgreSQL:

```
postgres://<your-macos-username>@localhost:5432/metrics
```

Example:

```
postgres://adron@localhost:5432/metrics
```

All your existing PostgreSQL tooling works. TimescaleDB is just an extension, so `psql`, `pg_dump`, ORMs, and migration tools all work exactly as before. I’ve used it with Rails, Django, Node.js—everything just works.

## DDL Patterns I Keep Coming Back To

Here are some patterns I use regularly for time-series tables:

### Basic Metrics Table

```
CREATE TABLE metrics (
    time TIMESTAMPTZ NOT NULL,
    metric_name TEXT NOT NULL,
    value DOUBLE PRECISION NOT NULL,
    tags JSONB
);

SELECT create_hypertable('metrics', 'time');
CREATE INDEX idx_metrics_name_time ON metrics (metric_name, time DESC);
```

The JSONB `tags` column is handy for storing arbitrary metadata. TimescaleDB handles JSONB just fine.

### Events Table

```
CREATE TABLE events (
    time TIMESTAMPTZ NOT NULL,
    event_type TEXT NOT NULL,
    user_id INTEGER,
    properties JSONB
);

SELECT create_hypertable('events', 'time');
CREATE INDEX idx_events_type_time ON events (event_type, time DESC);
CREATE INDEX idx_events_user_time ON events (user_id, time DESC) WHERE user_id IS NOT NULL;
```

The partial index on `user_id` saves space when you have a lot of NULL values.

### Multi-Sensor Table

```
CREATE TABLE sensor_data (
    time TIMESTAMPTZ NOT NULL,
    device_id TEXT NOT NULL,
    sensor_type TEXT NOT NULL,
    reading DOUBLE PRECISION NOT NULL,
    metadata JSONB
);

SELECT create_hypertable('sensor_data', 'time');
CREATE INDEX idx_sensor_device_time ON sensor_data (device_id, time DESC);
CREATE INDEX idx_sensor_type_time ON sensor_data (sensor_type, time DESC);
```

This pattern works well when you’re collecting data from multiple devices with different sensor types.

## Local Development vs. Production: Postgres.app vs. tigerData

When you’re ready to deploy to production, you’ll likely use a managed TimescaleDB service like **tigerData** (or Timescale Cloud, AWS RDS with TimescaleDB, etc.). I’ve used both local Postgres.app and managed services, and here’s what’s different.

### What You Get with Postgres.app (Local Development)

You manage everything locally. You install the extension, configure databases, and handle backups yourself. It’s perfect for development because you can experiment, break things, and reset without consequences. Your data lives on your Mac, so there’s no network latency and no per-hour billing.

Postgres.app runs one PostgreSQL server on your machine. You’re limited by your Mac’s resources—CPU, memory, and disk space. For development, this is fine. For production workloads handling millions of inserts per second, you’ll hit limits.

You handle backups, updates, monitoring, and scaling yourself. Postgres.app doesn’t automatically scale or replicate. If your Mac crashes, your database goes down. This is fine for local dev, but production needs high availability.

### What You Get with tigerData (Production Deployment)

tigerData handles the operational overhead: backups, updates, monitoring, scaling, and high availability. You don’t manage servers, disk space, or replication. You just connect and use TimescaleDB. This is what you pay for—someone else handles the ops so you can focus on your application.

Managed services like tigerData offer distributed hypertables and read replicas. You can scale reads across multiple nodes and distribute hypertables across data nodes. Your local Postgres.app can’t do this—it’s a single instance. For production workloads that need to handle massive scale, managed services provide the infrastructure.

You get automated backups, point-in-time recovery, monitoring dashboards, alerting, and support. tigerData handles the complexity of running TimescaleDB at scale, including managing compression policies, continuous aggregates, and retention policies across distributed systems.

Your application connects over the network, so there’s latency. You pay per hour or per resource usage. For development, this adds friction and cost. For production, the managed infrastructure is worth it.

### Performance: What TimescaleDB Actually Does

The performance improvements aren’t marketing fluff. Here’s what TimescaleDB provides that regular PostgreSQL doesn’t:

**Query performance.** Benchmarks show TimescaleDB can execute queries 1,000x to 14,000x faster than standard PostgreSQL for time-series workloads, depending on query complexity. I’ve seen queries that take 2,400 milliseconds in PostgreSQL run in 45 milliseconds with TimescaleDB—that’s a 53x improvement. Time-based aggregations run 61% faster because TimescaleDB’s query planner understands time-series patterns and optimizes accordingly.

**Insert performance at scale.** With 1 billion rows, PostgreSQL’s insert rate drops to around 5,000 rows per second as indexes become too large for memory. TimescaleDB maintains 111,000 rows per second at the same scale—over 20x higher insert rates. The automatic partitioning keeps indexes small and in memory, so insert performance stays consistent as your data grows.

**Storage efficiency.** TimescaleDB’s columnar compression reduces storage by **90% or more**. In benchmarks, 1 billion rows that take 89 GB in PostgreSQL compress down to 8.7 GB with TimescaleDB. Compression happens automatically on older chunks, so you’re not managing archive tables or separate storage systems.

**Automatic partitioning.** Regular PostgreSQL requires manual partition management. TimescaleDB’s hypertables automatically partition data into time-based chunks. Queries that would crawl on a regular table stay fast even as your data grows into billions of rows because TimescaleDB only scans relevant chunks.

**Continuous aggregates.** Pre-computed materialized views that refresh incrementally. Instead of running expensive aggregations every time, TimescaleDB maintains them automatically. This is what makes dashboards fast even with massive datasets.

The core TimescaleDB features work the same locally and in production. Hypertables, compression, continuous aggregates, and retention policies behave identically. The difference is scale, availability, and who manages the infrastructure. Use Postgres.app for development, tigerData (or similar) for production.

## The Downsides

TimescaleDB adds complexity to your stack. You’re managing an extension that needs to be installed and maintained. The automatic partitioning (hypertables) is powerful but adds another layer to understand when debugging. If you’re dealing with small datasets or simple time-series needs, regular PostgreSQL 18 with proper indexing might be enough.

There’s a learning curve. Continuous aggregates, compression policies, and retention policies are powerful but require understanding when and how to use them. You’ll need to learn TimescaleDB-specific functions like `time_bucket()` and `create_hypertable()`, though they’re straightforward once you get the hang of them.

Resource consumption can increase. Advanced features like continuous aggregates and compression do use CPU and memory. For small datasets, this overhead might not be worth it. But once you’re dealing with millions of rows, the performance gains far outweigh the resource costs.

Extension compatibility isn’t universal. While TimescaleDB works with most PostgreSQL extensions, some edge cases exist. If you’re using obscure extensions or have complex extension dependencies, test thoroughly before committing to TimescaleDB in production.

For teams that need strict production parity or can’t install extensions, you might need Docker or a managed TimescaleDB service instead. But for local development with Postgres.app on PostgreSQL 18, the downloadable extension installer makes it painless—just download, double-click, restart, and you’re ready to go.

## And That’s It

You now have TimescaleDB running on Postgres.app with PostgreSQL 18. Your time-series tables will automatically partition, compress old data, and handle millions of rows efficiently. All while staying in the PostgreSQL ecosystem you already know.

The hypertable abstraction means you write queries like normal, but TimescaleDB handles the partitioning magic behind the scenes. No manual partition management, no complex maintenance scripts—just create the hypertable and start inserting data.

If you need more advanced features like distributed hypertables, custom chunk intervals, or background job scheduling, then TimescaleDB documentation covers those. But for most time-series workloads, what’s here gets you 90% of the way there.

## References

- Adding these shortly, I accidentally deleted them and am re-collecting them. 😬
