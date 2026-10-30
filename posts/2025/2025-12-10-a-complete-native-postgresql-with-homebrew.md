---
title: 'A Complete Native PostgreSQL Setup on macOS: Homebrew and Launchd'
date: 2025-12-10 15:11:00 -0800
last_modified_at: 2026-01-03 16:17:45 -0800
permalink: /2025/12/10/a-complete-native-postgresql-with-homebrew/
slug: a-complete-native-postgresql-with-homebrew
wp_id: 73783
original_url: https://compositecode.blog/2025/12/10/a-complete-native-postgresql-with-homebrew/
categories:
- Databases
tags:
- database
- database administrator
- database development
- software development
excerpt: Native PostgreSQL installation on macOS provides optimal performance and control, allowing multiple versions to run concurrently. While Homebrew simplifies setup, managing the service requires knowledge of configurations and system settings. This approach is best for serious development but can be complex compared to alternatives like Postgres.app or Docker.
image: /wp-content/uploads/2025/11/pg-1.jpg
---

## Advantages

Native PostgreSQL installation gives you the best performance and the closest thing to a production Linux environment on macOS. You get full control over configuration, service management, and when PostgreSQL starts. Homebrew makes installation clean, and launchd handles service management reliably. You can run multiple PostgreSQL versions simultaneously on different ports, and you have direct access to all PostgreSQL files and configuration. This is the most flexible option for serious local development.

## Disadvantages

Native installation requires more setup and management than Postgres.app or Docker. You’re responsible for starting and stopping the service, configuring auto-start, and managing system-level settings. Updates require manual intervention, and you need to understand launchd and Homebrew service management. It’s easier to accidentally break things or create conflicts with other PostgreSQL installations. For developers who want simplicity, Postgres.app is easier. For those who want isolation and reproducibility, Docker might be better.

Sometimes you want PostgreSQL installed directly on your Mac. No containers, no apps. Just PostgreSQL running as a system service. This gives you the most control, the best performance, and the closest thing to a production Linux environment you’ll get on macOS.

The trade-off is you’re managing a system service. But if you know what you’re doing, it’s straightforward. Homebrew makes the installation painless, and macOS’s launchd handles the service management. You get full control over when it starts, how it’s configured, and what versions you’re running.

This is the complete guide to installing PostgreSQL natively on macOS, configuring it properly, managing the service, and setting up an initial development database named **interlinedlist**.

## Installation via Homebrew

Homebrew is the cleanest way to install PostgreSQL on macOS. If you don’t have Homebrew:

<https://brew.sh>

Install it, then install PostgreSQL:

```
brew install postgresql@16
```

This installs PostgreSQL 16. If you need a different version, swap `postgresql@16` for `postgresql@15`, `postgresql@14`, or whatever matches your production environment.

Homebrew installs PostgreSQL but doesn’t start it automatically. That’s intentional—you control when it runs.

## Start the Service

PostgreSQL on macOS runs as a launchd service. Start it:

```
brew services start postgresql@16
```

This starts PostgreSQL and configures it to start automatically on boot. If you don’t want it starting automatically, use:

```
brew services start postgresql@16 --no-autostart
```

Check if it’s running:

```
brew services list | grep postgresql
```

You should see `postgresql@16` listed as `started`.

## Verify It’s Running

Connect to PostgreSQL to verify everything works:

```
psql postgres
```

If you see a PostgreSQL prompt, you’re good. Type `\q` to exit.

## Create Your Initial Development Database

Create the database for your project:

```
createdb interlinedlist
```

Confirm it exists:

```
psql -l | grep interlinedlist
```

Connect to it:

```
psql interlinedlist
```

You’re in.

## Create a Local Superuser

By default, PostgreSQL creates a superuser matching your macOS username. If that doesn’t exist or you want to set it up explicitly:

```
createuser -s $USER
```

This creates a superuser with your macOS username. For local development, this keeps things simple. ORMs, migration tools, and scripts expect you to have full database privileges.

If you want a password for your user:

```
psql postgres
```

Then:

```
ALTER USER adron WITH PASSWORD 'your-password';
\q
```

## Connection String

For most tooling and frameworks, the connection string will look like:

```
postgres://adron@localhost:5432/interlinedlist
```

Or if you set a password:

```
postgres://adron:your-password@localhost:5432/interlinedlist
```

Drop that into your `.env` file or wherever your project expects it.

## Managing the Service

**Stop PostgreSQL:**

```
brew services stop postgresql@16
```

**Start PostgreSQL:**

```
brew services start postgresql@16
```

**Restart PostgreSQL:**

```
brew services restart postgresql@16
```

**Check service status:**

```
brew services list
```

This shows all Homebrew-managed services and their status.

## Configure Auto-Start on Boot

By default, `brew services start` configures PostgreSQL to start automatically when your Mac boots. If you want to disable this:

```
brew services stop postgresql@16
launchctl unload ~/Library/LaunchAgents/homebrew.mxcl.postgresql@16.plist
```

To re-enable auto-start:

```
brew services start postgresql@16
```

Or manually:

```
launchctl load ~/Library/LaunchAgents/homebrew.mxcl.postgresql@16.plist
```

## Finding PostgreSQL Files

Homebrew installs PostgreSQL in a versioned directory:

**Binaries:**

```
/opt/homebrew/opt/postgresql@16/bin/
```

Or on Intel Macs:

```
/usr/local/opt/postgresql@16/bin/
```

**Data directory:**

```
/opt/homebrew/var/postgresql@16/
```

Or on Intel Macs:

```
/usr/local/var/postgresql@16/
```

**Configuration file:**

```
/opt/homebrew/var/postgresql@16/postgresql.conf
```

**Logs:**

```
/opt/homebrew/var/log/postgresql@16.log
```

## Updating PostgreSQL

When a new version is available:

```
brew upgrade postgresql@16
```

This upgrades PostgreSQL in place. Your data stays intact. After upgrading, restart the service:

```
brew services restart postgresql@16
```

## Multiple PostgreSQL Versions

You can run multiple PostgreSQL versions simultaneously on different ports. Install another version:

```
brew install postgresql@15
```

Configure it to run on a different port. Edit the configuration:

```
brew services stop postgresql@15
```

Edit `/opt/homebrew/var/postgresql@15/postgresql.conf` and change:

```
port = 5433
```

Start it:

```
brew services start postgresql@15
```

Now you have PostgreSQL 16 on port 5432 and PostgreSQL 15 on port 5433.

## Configuration Best Practices

For local development, you’ll want to adjust some PostgreSQL settings. Edit the config file:

```
nano /opt/homebrew/var/postgresql@16/postgresql.conf
```

Or use your preferred editor. Key settings for local dev:

```
# Increase shared buffers for better performance
shared_buffers = 256MB

# Increase work memory for complex queries
work_mem = 16MB

# Enable logging for debugging
logging_collector = on
log_directory = 'log'
log_filename = 'postgresql-%Y-%m-%d.log'
log_statement = 'all'  # Log all queries (useful for dev)

# Increase max connections if needed
max_connections = 100
```

After changing configuration, restart PostgreSQL:

```
brew services restart postgresql@16
```

## Backup and Restore

**Create a backup:**

```
pg_dump interlinedlist > interlinedlist_backup.sql
```

**Restore from backup:**

```
psql interlinedlist < interlinedlist_backup.sql
```

**Backup all databases:**

```
pg_dumpall > all_databases_backup.sql
```

## Common Issues and Solutions

**Port already in use:**

If port 5432 is already taken (maybe by Postgres.app or another PostgreSQL instance):

```
lsof -i :5432
```

Kill the process or change PostgreSQL’s port in the config file.

**Can’t connect:**

Check if PostgreSQL is running:

```
brew services list | grep postgresql
```

Check logs:

```
tail -f /opt/homebrew/var/log/postgresql@16.log
```

**Permission errors:**

Make sure your user owns the data directory:

```
sudo chown -R $(whoami) /opt/homebrew/var/postgresql@16
```

## Uninstalling PostgreSQL

If you need to remove PostgreSQL completely:

```
brew services stop postgresql@16
brew uninstall postgresql@16
```

This removes PostgreSQL but leaves your data directory intact. To remove data as well:

```
rm -rf /opt/homebrew/var/postgresql@16
```

## Summary of Native PostgreSQL Setup

Native PostgreSQL on macOS gives you full control. You manage the service, configure it exactly how you want, and run multiple versions if needed. It’s the closest thing to a production Linux environment you’ll get on a Mac.

Homebrew handles the installation cleanly, launchd manages the service reliably, and you get all the PostgreSQL tools you need without any abstraction layers. For serious local development that needs to match production, this is the way to go.

The service starts when you boot (or doesn’t, if you configure it that way), runs in the background, and stays out of your way until you need it. Clean, predictable, and exactly what you’d expect from a native system service.
