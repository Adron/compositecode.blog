---
title: 'A Clean, Production-Parity Way to Run PostgreSQL on macOS: Docker'
date: 2025-12-10 13:58:00 -0800
last_modified_at: 2026-01-03 16:17:47 -0800
permalink: /2025/12/10/a-clean-production-parity-way-to-run-postgresql-on-macos-docker/
slug: a-clean-production-parity-way-to-run-postgresql-on-macos-docker
wp_id: 73784
original_url: https://compositecode.blog/2025/12/10/a-clean-production-parity-way-to-run-postgresql-on-macos-docker/
categories:
- Databases
tags:
- database
- database administrator
- database development
- software development
excerpt: Docker provides production parity and isolation for PostgreSQL, allowing multiple instances and exact version matching. While it requires Docker Desktop and adds complexity, it ensures predictable, reproducible setups. Docker Compose simplifies version control and sharing configurations. For single-database development, alternatives like Postgres.app may be faster and simpler.
image: /wp-content/uploads/2025/11/pg-2.jpg
---

## Advantages

Docker gives you production parity and complete isolation. You can match exact PostgreSQL versions, run multiple instances simultaneously on different ports, and tear everything down with a single command. Docker Compose makes it easy to version control your database configuration and share it with your team. If you’re already using Docker for other services, PostgreSQL fits right into your existing workflow. Containers are predictable, reproducible, and never pollute your system with leftover installs.

## Disadvantages

Docker adds overhead and complexity compared to Postgres.app or native installation. You need Docker Desktop running, which consumes system resources. Containers can be slower than native installations, and you’ll need to manage volumes for data persistence. If you’re not already using Docker, this adds another tool to your stack. For simple single-database development, Postgres.app might be faster and easier.

Sometimes you need more than Postgres.app. Maybe you’re matching production versions exactly, running multiple PostgreSQL instances, or you want complete isolation between projects. Docker gives you that control without polluting your system with multiple PostgreSQL installs.

Docker-based PostgreSQL setups are predictable, reproducible, and easy to tear down. You get production parity without the headaches of managing multiple versions on your Mac. If you’re already using Docker for other services, this fits right into your workflow.

This is the short guide to getting PostgreSQL running in Docker, configured, and ready for an initial development database named **interlinedlist**.

## Prerequisites

You’ll need Docker Desktop installed. If you don’t have it:

[https://docker.com](https://www.docker.com/)

Download, install, and make sure Docker is running. You should see the Docker icon in your menu bar.

## Run PostgreSQL in Docker

The simplest way to get PostgreSQL running:

```
docker run --name postgres-interlinedlist \
  -e POSTGRES_PASSWORD=postgres \
  -e POSTGRES_USER=postgres \
  -e POSTGRES_DB=interlinedlist \
  -p 5432:5432 \
  -d postgres:16
```

This does a few things:

- Creates a container named `postgres-interlinedlist`
- Sets up a database called `interlinedlist` automatically
- Exposes PostgreSQL on port 5432 (standard)
- Runs PostgreSQL 16 in detached mode (`-d`)
- Uses the default `postgres` user with password `postgres`

If you need a different version, swap `postgres:16` for `postgres:15`, `postgres:14`, or whatever matches your production environment.

## Verify It’s Running

Check that your container is up:

```
docker ps | grep postgres-interlinedlist
```

You should see the container running. If you don’t, check logs:

```
docker logs postgres-interlinedlist
```

## Install the Command Line Tools

You’ll want `psql` available locally to connect to your Dockerized PostgreSQL. The easiest way is via Homebrew:

```
brew install postgresql@16
```

Or if you already have Postgres.app installed, you can use those tools. They’ll connect to Docker just fine.

Verify:

```
psql --version
```

## Connect to Your Database

Now connect to the database running in Docker:

```
psql -h localhost -U postgres -d interlinedlist
```

When prompted, enter the password: `postgres`

You’re in. Same PostgreSQL, just running in a container instead of directly on your Mac.

## Create a Local Superuser (Optional but Recommended)

If you want to use your macOS username instead of `postgres`:

```
psql -h localhost -U postgres -d interlinedlist
```

Then inside psql:

```
CREATE USER adron WITH SUPERUSER PASSWORD 'your-password';
GRANT ALL PRIVILEGES ON DATABASE interlinedlist TO adron;
\q
```

Now you can connect as yourself:

```
psql -h localhost -U adron -d interlinedlist
```

## Connection String

For most tooling and frameworks, the connection string will look like:

```
postgres://postgres:postgres@localhost:5432/interlinedlist
```

Or if you created your own user:

```
postgres://adron:your-password@localhost:5432/interlinedlist
```

Drop that into your `.env` file or wherever your project expects it.

## Managing Your Container

**Stop the container:**

```
docker stop postgres-interlinedlist
```

**Start it again:**

```
docker start postgres-interlinedlist
```

**Remove the container (this deletes your data):**

```
docker stop postgres-interlinedlist
docker rm postgres-interlinedlist
```

**View logs:**

```
docker logs postgres-interlinedlist
```

## Persisting Data

By default, Docker containers are ephemeral. If you remove the container, your data goes with it. To persist data between container restarts, use a volume:

```
docker run --name postgres-interlinedlist \
  -e POSTGRES_PASSWORD=postgres \
  -e POSTGRES_USER=postgres \
  -e POSTGRES_DB=interlinedlist \
  -p 5432:5432 \
  -v postgres-interlinedlist-data:/var/lib/postgresql/data \
  -d postgres:16
```

The `-v postgres-interlinedlist-data:/var/lib/postgresql/data` flag creates a Docker volume that persists even if you remove the container. Your data stays safe.

## Using Docker Compose (Recommended)

For anything more than a quick test, use Docker Compose. Create a `docker-compose.yml`:

```
version: '3.8'

services:
  postgres:
    image: postgres:16
    container_name: postgres-interlinedlist
    environment:
      POSTGRES_PASSWORD: postgres
      POSTGRES_USER: postgres
      POSTGRES_DB: interlinedlist
    ports:
      - "5432:5432"
    volumes:
      - postgres-interlinedlist-data:/var/lib/postgresql/data

volumes:
  postgres-interlinedlist-data:
```

Then:

```
docker-compose up -d
```

To stop:

```
docker-compose down
```

To stop and remove volumes (deletes data):

```
docker-compose down -v
```

Docker Compose keeps everything in one file, version-controlled, and easy to share with your team.

## Summary of Production-Parity with Docker

Docker gives you production parity, version control, and complete isolation. You can run multiple PostgreSQL versions simultaneously on different ports, match your production environment exactly, and tear everything down with a single command.

If you need more like multiple databases, extensions, seed scripts, or integration with other Docker services, Docker Compose makes it all straightforward. But for a single PostgreSQL instance that matches production, this gets you there fast.

The container runs when you need it, stops when you don’t, and never touches your system PostgreSQL installs. Clean, predictable, and exactly what you need for local development.
