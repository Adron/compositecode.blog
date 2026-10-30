---
title: 'Setting Up SQLite on Windows 11: A Guide for Developers'
date: 2024-08-28 10:18:17 -0700
last_modified_at: 2024-09-03 08:43:12 -0700
permalink: /2024/08/28/setting-up-sqlite-on-windows-11-a-guide-for-developers/
slug: setting-up-sqlite-on-windows-11-a-guide-for-developers
wp_id: 69720
original_url: https://compositecode.blog/2024/08/28/setting-up-sqlite-on-windows-11-a-guide-for-developers/
categories:
- Databases
tags:
- database
- development database
- in memory database
- sqlite
excerpt: SQLite is a lightweight, serverless, and self-contained database solution ideal for small-scale projects or testing. On Windows 11, it lacks native support but can be easily installed. Steps include downloading SQLite tools, setting up tooling, integrating with Go, and using it with .NET. This versatile database is a great choice for various projects on Windows 11.
image: /wp-content/uploads/2024/08/SQLite-Logo.wine_.coffee.png
---

SQLite is a remarkable database engine—lightweight, serverless, and self-contained. Whether you’re building a small-scale project or need a quick, zero-configuration database for testing, SQLite is your go-to solution. But before diving into SQLite with Go or .NET on Windows 11, it’s crucial to understand how Windows 11 is set up by default and what tools you need to make your development environment rock-solid.

## Windows 11 Default Setup: What You Need to Know

Windows 11 comes with some pre-installed tools and utilities, but when it comes to database work, you’re mostly on your own. The default setup lacks native support for databases like SQLite. Fortunately, Windows 11’s modern architecture and compatibility with a wide range of tools make it straightforward to configure.

### Key Points of Windows 11 Default Setup:

- **PowerShell**: Windows 11 ships with PowerShell, a powerful command-line shell that you’ll use frequently for installation and setup tasks.
- **Windows Subsystem for Linux (WSL)**: While not necessary for SQLite, WSL provides a Linux environment if you prefer to run SQLite commands in a Linux-like environment on Windows.
- **No Native Database Tools**: Windows 11 doesn’t include any database management tools by default, so you’ll need to install SQLite manually.

#### Step 1: Installing SQLite on Windows 11

The first step in getting started with SQLite is to install it. Here’s how you can do that:

1. **Download SQLite Tools**:

- Visit the official [SQLite Downloads page](https://sqlite.org/download.html).
- Under “Precompiled Binaries for Windows,” download the ZIP file containing the `sqlite3.exe` command-line shell.

1. **Extract and Place the Executable**:

- Extract the ZIP file to a directory of your choice, such as `C:\sqlite`.
- Add this directory to your system’s PATH environment variable:
  - Right-click on `This PC` → `Properties` → `Advanced system settings`.
  - Click `Environment Variables`.
  - In the `System variables` section, find `Path` and click `Edit`.
  - Add the path to your `C:\sqlite` directory.

1. **Verify Installation**:

- Open PowerShell or Command Prompt.
- Type `sqlite3` and press Enter. You should see the SQLite command prompt, confirming the installation was successful.

#### Step 2: Setting Up Tooling for SQLite

To work effectively with SQLite, especially when managing complex databases or working on larger projects, you’ll need more than just the command-line tool.

##### Recommended Tools:

- **DB Browser for SQLite**:
  - A graphical interface for SQLite that simplifies database management.
  - Download from [DB Browser for SQLite](https://sqlitebrowser.org/).
  - It provides an easy way to create, design, and edit SQLite databases.
- **SQLite Studio**:
  - Another GUI tool that offers advanced features like SQL query generation and database schema visualization.
  - Download from [SQLite Studio](https://sqlitestudio.pl/).

These tools are optional but highly recommended, especially if you’re new to SQLite or prefer a visual interface over command-line operations.

#### Step 3: Using SQLite with Go

If you’re working with Go, integrating SQLite into your project is straightforward. Here’s how to set it up:

1. **Install Go**:

- Ensure Go is installed. If not, download it from [golang.org](https://golang.org/dl/) and install it.

1. **Install the SQLite Driver for Go**:

- Use the following command to install the SQLite driver:
  `bash go get github.com/mattn/go-sqlite3`
- This driver allows you to interact with SQLite databases directly from Go.

1. **Write Your Go Code**:

- Here’s a quick example of using SQLite in Go:

```
package main

import (
    "database/sql"
    _ "github.com/mattn/go-sqlite3"
    "log"
)

func main() {
    db, err := sql.Open("sqlite3", "./test.db")
    if err != nil {
        log.Fatal(err)
    }
    defer db.Close()

    _, err = db.Exec("CREATE TABLE IF NOT EXISTS example (id INTEGER PRIMARY KEY, name TEXT)")
    if err != nil {
        log.Fatal(err)
    }
}
```

- This code snippet sets up a simple SQLite database and creates a table.

1. **Run Your Go Application**:

- Compile and run your application with `go run yourfile.go`. This will create an SQLite database named `test.db` in the current directory.

#### Step 4: Using SQLite with .NET

.NET provides excellent support for SQLite, allowing you to integrate it into your projects seamlessly. Here’s the setup:

1. **Install .NET SDK**:

- Ensure that you have the .NET SDK installed. Download it from the [Microsoft .NET website](https://dotnet.microsoft.com/download).

1. **Create a New .NET Project**:

- Create a new console or web application using the .NET CLI:
  `bash dotnet new console -n SQLiteDemo cd SQLiteDemo`

1. **Add the SQLite NuGet Package**:

- Install the `Microsoft.Data.Sqlite` package using the following command:
  `bash dotnet add package Microsoft.Data.Sqlite`

1. **Write Your .NET Code**:

- Here’s a quick example of using SQLite in a .NET application:

```
using Microsoft.Data.Sqlite;

class Program
{
    static void Main()
    {
        using var connection = new SqliteConnection("Data Source=sample.db");
        connection.Open();

        var command = connection.CreateCommand();
        command.CommandText =
        @"
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                name TEXT
            )
        ";
        command.ExecuteNonQuery();
    }
}
```

1. **Run Your .NET Application**:

- Compile and run your application with `dotnet run`. This will create an SQLite database named `sample.db` in the current directory.

#### Warp Up

Setting up SQLite on Windows 11 is easy with the right steps. Whether you’re working with Go, .NET, or another language, SQLite’s versatility makes it an excellent choice for a wide range of projects. With this guide, you’re well on your way to leveraging SQLite’s power in your development workflow on Windows 11.
