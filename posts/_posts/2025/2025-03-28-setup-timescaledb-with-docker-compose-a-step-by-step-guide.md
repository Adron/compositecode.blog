---
title: 'Setup TimescaleDB with Docker Compose: A Step-by-Step Guide'
date: 2025-03-28 14:56:16 -0700
last_modified_at: 2025-03-31 09:42:43 -0700
permalink: /2025/03/28/setup-timescaledb-with-docker-compose-a-step-by-step-guide/
slug: setup-timescaledb-with-docker-compose-a-step-by-step-guide
wp_id: 71631
original_url: https://compositecode.blog/2025/03/28/setup-timescaledb-with-docker-compose-a-step-by-step-guide/
categories:
- Databases
- Development Machine Environment
- Docker
tags:
- docker
- docker compose
- postgres
- postgresql
- time series
- timescale
excerpt: This tutorial demonstrates how to set up and use TimescaleDB with Docker Compose, detailing prerequisites, installation steps, and basic operations including creating hypertables and querying data. It also covers running multiple PostgreSQL instances on different ports for simultaneous project management while maintaining system organization and resource efficiency.
image: /wp-content/uploads/2025/03/pexels-photo-1095602.jpeg
---

This tutorial will guide you through setting up and using TimescaleDB using Docker Compose.

### Prerequisites

- Docker installed on your system
- Docker Compose installed on your system

### Getting Started

1. **Start the TimescaleDB Container**

   Navigate to the directory containing the `docker-compose.yml` file and run:

   ```bash
   docker-compose up -d
   ```

   This will start TimescaleDB in detached mode. The database will be accessible on port 5432.
2. **Connection Details**

   - Host: localhost
   - Port: 5432
   - Database: timescale
   - Username: timescale
   - Password: timescale
3. **Verify the Installation**

   You can connect to the database using psql or any PostgreSQL client:

   ```bash
   docker exec -it timescale-timescaledb-1 psql -U timescale -d timescale
   ```

   Once connected, you can verify TimescaleDB is properly installed:

   ```sql
   SELECT default_version, installed_extensions FROM pg_available_extensions WHERE name = 'timescaledb';
   ```

4. **Create Your First Hypertable**

   ```sql
   -- Create a regular table
   CREATE TABLE sensor_data (
       time        TIMESTAMPTZ       NOT NULL,
       sensor_id   TEXT             NOT NULL,
       temperature DOUBLE PRECISION  NULL,
       humidity    DOUBLE PRECISION  NULL
   );

   -- Convert it to a hypertable
   SELECT create_hypertable('sensor_data', 'time');

   -- Create an index
   CREATE INDEX ON sensor_data (sensor_id, time DESC);
   ```
5. **Insert Some Test Data**

   ```sql
   -- Insert sample data
   INSERT INTO sensor_data (time, sensor_id, temperature, humidity)
   VALUES
       (NOW(), 'sensor_1', 23.5, 45.0),
       (NOW(), 'sensor_2', 24.1, 46.2),
       (NOW(), 'sensor_1', 23.8, 45.5);
   ```
6. **Query Your Data**

   ```sql
   -- Basic query
   SELECT * FROM sensor_data ORDER BY time DESC;

   -- Time-bucket query (aggregate data into 1-hour buckets)
   SELECT time_bucket('1 hour', time) AS hour,
          sensor_id,
          avg(temperature) as avg_temp,
          avg(humidity) as avg_humidity
   FROM sensor_data
   GROUP BY hour, sensor_id
   ORDER BY hour DESC;
   ```

### Stopping the Database

To stop the TimescaleDB container:

```bash
docker-compose down
```

To stop the container and remove the volume (this will delete all data):

```bash
docker-compose down -v
```

### Additional Resources

- [TimescaleDB Documentation](https://docs.timescale.com/#TimescaleDB)
- [TimescaleDB GitHub Repository](https://github.com/timescale/timescaledb)
- [PostgreSQL Documentation](https://www.postgresql.org/docs/)

## A Little Lagniappe: Running Multiple PostgreSQL Instances

[![](/wp-content/uploads/2025/03/CleanShot-2025-03-31-at-09.41.53@2x.png)](/wp-content/uploads/2025/03/CleanShot-2025-03-31-at-09.41.53@2x.png)

Hey, here’s a common scenario you might run into. You’re working on multiple projects (because who isn’t these days?), and you’ve already got a PostgreSQL instance running on the default port 5432. In my case, I’ve got a core platform database running there:

```bash
$ docker ps | grep 5432
96e464b414f0   postgres:latest   "docker-entrypoint.s…"   Up 8 days   0.0.0.0:5432->5432/tcp   a-core-platform-db
```

No problem! PostgreSQL (and by extension, TimescaleDB) is perfectly happy running on different ports. Here’s how we handle this:

1. **Check Your Ports First**

   ```bash
   $ lsof -i :5432
   # This will show you what's using the default PostgreSQL port
   ```
2. **Modify the Port Mapping**
   Instead of the standard port mapping, we’ll shift TimescaleDB to 5433:

   ```yaml
   ports:
     - "5433:5432"
   ```

   Note that we’re mapping port 5433 on the host to 5432 in the container. The container still thinks it’s using 5432 (PostgreSQL’s default), but we access it through 5433 on our machine.
3. **Connection Details**
   Now you’ve got two separate PostgreSQL instances:

   - Core Platform DB: localhost:5432
   - TimescaleDB: localhost:5433
4. **Using Different Ports in Your Tools**

   - psql: `psql -h localhost -p 5433 -U timescale timescale`
   - Connection strings: `postgresql://timescale:timescale@localhost:5433/timescale`
   - GUI tools: Just remember to use port 5433 for TimescaleDB connections

**This setup is perfect for:**

- Running multiple projects simultaneously
- Testing different PostgreSQL-based databases
- Keeping your development environments isolated
- Not breaking existing applications that expect PostgreSQL on 5432

Remember, you can run as many PostgreSQL instances as you want (well, as many as your system resources allow), just make sure each one has its own port. I’ve seen setups with half a dozen different PostgreSQL instances, each serving a different purpose. Just keep track of what’s running where!
