---
title: Security and Authentication in Relational Databases
date: 2023-12-07 10:57:15 -0800
last_modified_at: 2023-12-07 14:18:16 -0800
permalink: /2023/12/07/security-and-authentication-in-relational-databases/
slug: security-and-authentication-in-relational-databases
wp_id: 67307
original_url: https://compositecode.blog/2023/12/07/security-and-authentication-in-relational-databases/
categories:
- Databases
tags:
- authentication
- database
- database authentication
- database security
- databases
- infosec
- relational database
- relational database management system
- security
excerpt: Explore the intricacies of security and authentication in relational databases with our comprehensive guide. Delve into the unique security architectures of SQL Server, Oracle, MariaDB/MySQL, and PostgreSQL. Understand how each system manages user setup, authentication methods, and role-based access control. Learn about the differences and similarities in their security models, from Windows Authentication in SQL Server to the role-based security of PostgreSQL. Our guide offers valuable insights into best practices for database security, ensuring a robust and secure environment for your data. Ideal for database administrators and developers, this post is a must-read for anyone looking to enhance their understanding of relational database security and authentication.
image: /wp-content/uploads/2023/12/database-security.jpg
---

This is a continuation of my posts on relational databases, started [here](/2023/08/22/designing-a-relational-database-data-modeling/). Previous posts on this theme, “[Data Modeling](/2023/08/22/designing-a-relational-database-data-modeling/)“, “[Let’s Talk About Database Schema](/2023/08/29/lets-talk-about-database-schema/)“, “[The Exasperating Topic of Database Indexes](/2023/09/06/the-exasperating-topic-of-database-indexes/)“, “[The Keys & Relationships of Relational Databases](/2023/09/18/the-keys-relationships-of-relational-databases/)“, “[Relational Database Query Optimization](/2023/09/20/relational-database-query-optimization/)“, “[Normalization in Relational Databases](/2023/09/26/normalization-in-relational-databases/)“, and “[Database (DB) Caching and DB Tertiary Caching](/2023/10/22/database-db-caching-and-db-tertiary-caching/)“.

#### Basic Security Architecture

Relational Database Management Systems (RDBMS) like SQL Server, Oracle, MariaDB/MySQL, and PostgreSQL are designed with robust security architectures. The core components typically include:

1. **Authentication**: Verifying the identity of users accessing the database.
2. **Authorization**: Determining what authenticated users are allowed to do.
3. **Access Control**: Implementing permissions and roles to manage user access.
4. **Encryption**: Protecting data at rest and in transit.
5. **Auditing and Logging**: Tracking access and changes to the database for security and compliance.

#### Authentication Mechanisms

Authentication is the first line of defense in database security. It ensures that only legitimate users can access the database. The primary methods include:

- **Username and Password**: The most common method, where users provide credentials that are verified against the database’s security system.
- **Integrated Security**: Leveraging the operating system or network security (like Windows Authentication in SQL Server) for user validation.
- **Certificates and Keys**: Using digital certificates or cryptographic keys for more secure authentication.

### Database-Specific Security and Authentication

#### SQL Server

- **Windows Authentication**: Integrates with Windows user accounts, providing a seamless and secure authentication mechanism.
- **SQL Server Authentication**: Involves creating specific database users and passwords.
- **Roles and Permissions**: SQL Server offers fixed server roles, fixed database roles, and user-defined roles for granular access control.
- **SSO Integration**: Supports integration with Active Directory for single sign-on capabilities.

#### Oracle

- **Oracle Database Authentication**: Users are authenticated by the database itself.
- **OS Authentication**: Oracle can use credentials from the operating system.
- **Roles and Privileges**: Oracle has a sophisticated role-based access control system, with predefined roles like DBA and user-defined roles.
- **Oracle Wallet**: For storing and managing credentials, enhancing security for automated login processes.

#### MariaDB/MySQL

- **Standard Authentication**: Username and password-based, with the option of using SHA256 for password encryption.
- **Pluggable Authentication**: Supports external authentication methods like PAM (Pluggable Authentication Modules) or Windows native authentication.
- **Role-Based Access Control**: Introduced in later versions, allowing for more flexible and manageable permissions.
- **SSL/TLS Encryption**: For securing connections between the client and the server.

#### PostgreSQL

- **Role-Based Authentication**: PostgreSQL uses roles to handle both authentication and authorization.
- **Password Authentication**: Supports MD5 or SCRAM-SHA-256 for password encryption.
- **Peer Authentication**: For local connections, relying on OS user credentials.
- **SSO Integration**: Can integrate with external authentication systems like Kerberos.

## Elaboration of Database Security Options

In the following section I’ll elaborate on and detail the basic setup for a user account for each of these databases. The intent, is to provide the basic first step into usage of the particular database. Often the root account is setup and use for examples. But It is *always* good, as a first step with a database system, to setup a user account for interactions with the database.

## First to bat, SQL Server

Delving deeper into the SQL Server options, focusing on how a user would be set up in the database. SQL Server offers a comprehensive security model that includes both authentication (verifying who can connect) and authorization (controlling what they can do once connected).

### Setting Up a User in SQL Server

#### 1. Choosing the Authentication Mode

SQL Server supports two authentication modes:

- **Windows Authentication Mode**: This is the recommended method for its ease of use and security. It leverages Windows user accounts, meaning the database trusts the Windows credentials without needing separate SQL Server credentials.
- **Mixed Mode (Windows Authentication and SQL Server Authentication)**: This mode supports both Windows authentication and SQL Server authentication, where users can log in with a username and password created within SQL Server.

#### 2. Creating a New User

Here’s a step-by-step process for creating a new user in SQL Server:

1. **Open SQL Server Management Studio (SSMS)**: Connect to your SQL Server instance.
2. **Choose Authentication Mode**:

- For Windows Authentication, the user account is typically managed by an IT administrator in Active Directory.
- For SQL Server Authentication, you’ll create a new SQL Server login.

3. **Create a New Login (for SQL Server Authentication)**:

- Navigate to the “Security” folder at the server level, right-click on “Logins”, and select “New Login”.
- Enter a login name, select “SQL Server authentication”, and enter a password.
- Set password policy options (enforce password policy, expiration, etc.).

4. **Assign Server Roles (Optional)**:

- In the login creation window, you can assign server-level roles like sysadmin, dbcreator, or securityadmin.

5. **Map the User to a Database**:

- In the “User Mapping” page, select the databases the user should have access to.
- Specify database-level roles like db\_datareader, db\_datawriter, or db\_owner for each database.

6. **Create User in the Database (if using Windows Authentication or for additional control)**:

- In SSMS, expand the desired database, navigate to the “Security” folder, right-click on “Users”, and select “New User”.
- For Windows Authentication, select “Windows user”. For SQL Server Authentication, select “SQL user with login”.
- Enter the username and map it to the previously created login.

7. **Assign Permissions**:

- Assign specific permissions like SELECT, INSERT, UPDATE, DELETE on database objects as needed.

8. **Save the Configuration**: Click “OK” to create the user with the specified settings.

#### 3. Testing the User Account

- **Log in via SSMS**: Try logging in with the new user credentials to ensure that the setup is correct.
- **Verify Permissions**: Check if the user can access the appropriate database objects and perform the allowed operations.

### Best Practices

- **Principle of Least Privilege**: Always assign the minimum necessary permissions to each user.
- **Regularly Review and Update Permissions**: As roles and responsibilities change, update the permissions accordingly.
- **Monitor User Activity**: Use SQL Server’s auditing features to track user actions and identify any unauthorized access or anomalies.

## Next Up, Oracle

Setting up a user in an Oracle database involves several key steps, focusing on both authentication and authorization. Oracle’s security model is robust and offers a range of options for managing users and their access to database resources.

### Setting Up a User in Oracle Database

#### 1. Choosing the Authentication Method

Oracle supports several authentication methods:

- **Database Authentication**: Users are authenticated by the Oracle database itself, using a username and password stored in the database.
- **Operating System Authentication**: Oracle can authenticate users based on their operating system login credentials.
- **Network Authentication**: Using network services like Kerberos or RADIUS.

#### 2. Creating a New User

Here’s a step-by-step guide to creating a new user in Oracle:

1. **Connect to the Database**:

- Use a database client tool like SQL\*Plus, SQL Developer, or any other tool that can execute SQL against an Oracle database.
- Connect as a user with administrative privileges (like SYS or SYSTEM).

2. **Create a New User**:

- Execute the `CREATE USER` command. For example:
  `sql CREATE USER new_user IDENTIFIED BY password;`
- `new_user` is the username, and `password` is the password you assign to the user.

3. **Grant Privileges**:

- Users are created with no privileges. You need to grant them explicitly.
- Grant necessary system privileges, object privileges, and roles. For example:
  `sql GRANT CREATE SESSION TO new_user;`
- `CREATE SESSION` privilege allows the user to connect to the database.
- For more specific tasks, like creating tables or views, additional privileges like `CREATE TABLE` or `CREATE VIEW` are required.

4. **Assign Quota on Tablespaces** (Optional):

- If the user needs to create objects in a tablespace, assign a quota. For example:
  `sql ALTER USER new_user QUOTA 100M ON users;`
- This command allows `new_user` to use up to 100MB of storage in the `users` tablespace.

5. **Configure Profile and Password Settings** (Optional):

- Oracle allows the configuration of user profiles to manage resource limits and password policies.
- For example, to assign a profile to a user:
  `sql ALTER USER new_user PROFILE default;`

#### 3. Testing the User Account

- **Log in with the New User Credentials**:
- Use SQL\*Plus or another client tool to test the new user login.
- Example command:
  `sql CONNECT new_user/password;`

### Best Practices

- **Principle of Least Privilege**: Grant only the necessary privileges to each user.
- **Regularly Review User Privileges**: Periodically review and adjust user privileges as needed.
- **Use Roles for Managing Privileges**: Create roles for groups of privileges and assign these roles to users, simplifying privilege management.
- **Monitor User Activity**: Utilize Oracle’s auditing features to track user actions and identify security issues.

## MariaDB/MySQL

MariaDB and MySQL are closely related database systems, with MariaDB originally forking from MySQL. While they share many similarities, especially in basic operations like user management, there are some differences in features and implementation. Let’s explore how to set up a user in both MariaDB and MySQL, highlighting any notable differences.

### Setting Up a User in MariaDB/MySQL

#### Basic Steps for User Creation

1. **Connect to the Database**:

- Use a command-line tool like `mysql` or a database management tool like phpMyAdmin.
- Connect as a user with administrative privileges (typically ‘root’).

2. **Create a New User**:

- The syntax for creating a user is generally the same in both MariaDB and MySQL:
  `sql CREATE USER 'username'@'host' IDENTIFIED BY 'password';`
- Replace `username`, `host`, and `password` with the desired values. `host` specifies where the user can connect from and can be an IP, a hostname, or `'%'` for any host.

3. **Grant Privileges**:

- Users are created with no privileges. You need to explicitly grant them.
- Grant necessary privileges using the `GRANT` statement. For example:
  `sql GRANT ALL PRIVILEGES ON database_name.* TO 'username'@'host';`
- This command grants all privileges on `database_name` to the new user.

4. **Apply the Changes**:

- Execute the `FLUSH PRIVILEGES` command to reload the grant tables and apply the new privileges.

5. **Testing the User Account**:

- Test the new user account by logging in:
  `bash mysql -u username -p -h host`

#### Differences Between MariaDB and MySQL

- **Authentication Plugins**:
  - MariaDB and MySQL support different authentication plugins. MariaDB includes some additional plugins like `ed25519` for passwordless authentication, which are not available in MySQL.
  - MySQL 8.0 uses `caching_sha2_password` as the default authentication plugin, while MariaDB uses `mysql_native_password`.
- **Roles**:
  - MariaDB has more advanced role-based access control (RBAC) features compared to MySQL. In MariaDB, you can create roles, assign privileges to roles, and then grant roles to users.
- **Password Expiry and Complexity**:
  - MySQL has features for password expiry and complexity requirements, which are less extensive in MariaDB.
- **System Versioned Tables**:
  - MariaDB supports system versioned tables, which MySQL does not. This feature isn’t directly related to user management but can impact how you manage data and user access over time.

### Best Practices

- **Principle of Least Privilege**: Grant only the necessary privileges to each user.
- **Regularly Review User Privileges**: Periodically review user privileges and adjust as necessary.
- **Use Strong Passwords**: Especially important if users can connect from remote hosts.
- **Monitor User Activity**: Implement auditing to track user actions and identify potential security issues.

## Wrapping Up, PostgreSQL!

Setting up a user in PostgreSQL involves a few key steps, focusing on user creation, privilege assignment, and optionally, role management. PostgreSQL uses a role-based security model, where a role can be a user, a group of users, or both, and can own database objects and have database privileges.

### Setting Up a User in PostgreSQL

#### 1. Connect to the Database

- Use a command-line tool like `psql` or a database management tool.
- Connect as a superuser or a user with the necessary privileges (typically ‘postgres’).

#### 2. Create a New Role/User

- In PostgreSQL, users are referred to as roles. To create a new user, you actually create a new role.
- Use the `CREATE ROLE` command with the `LOGIN` option to create a new user. For example:

```
  CREATE ROLE username WITH LOGIN PASSWORD 'password';
```

- Replace `username` and `password` with your desired values.

#### 3. Grant Privileges

- Newly created roles have no privileges by default.
- Grant specific privileges using the `GRANT` command. For example:

```
  GRANT CONNECT ON DATABASE database_name TO username;
```

- This command allows the user to connect to `database_name`.
- For more granular control, you can grant privileges on specific tables, schemas, or other database objects.

#### 4. Modify Role Attributes (Optional)

- PostgreSQL roles can have attributes that control their behavior. For example:
- `CREATEDB`: Allows the role to create databases.
- `SUPERUSER`: Grants all privileges automatically.
- To modify role attributes, use the `ALTER ROLE` command. For example:
  `sql ALTER ROLE username CREATEDB;`

#### 5. Testing the User Account

- Test the new user account by logging in:

```
  psql -U username -d database_name -h host -W
```

- Enter the password when prompted.

### PostgreSQL Role Management

- **Group Roles**: You can create roles that act as groups. Users (roles with the `LOGIN` attribute) can be added to these group roles.
- **Role Inheritance**: By default, roles inherit privileges from roles they are members of. This can be controlled with the `INHERIT` or `NOINHERIT` attributes.

### Best Practices

- **Principle of Least Privilege**: Only grant the necessary privileges to each role.
- **Use Role Groups**: Manage privileges more efficiently by creating roles for specific job functions and assigning users to these roles.
- **Regularly Review and Update Privileges**: As roles and responsibilities change, update the privileges accordingly.
- **Strong Password Policies**: Enforce strong password policies for roles with the `LOGIN` attribute.
- **Monitor Role Activity**: Use PostgreSQL’s logging and auditing features to track role activities and identify security issues.

## Security & Authentication Summary

In the realm of relational databases, security and authentication are paramount, with each major RDBMS offering its unique mechanisms and features. SQL Server leverages Windows Authentication for seamless integration with Windows user accounts, alongside SQL Server Authentication for database-specific credentials, and provides robust role-based access control. Oracle, with its sophisticated security model, offers database, OS, and network-based authentication, complemented by a comprehensive role and privilege system. MariaDB and MySQL, while sharing many similarities, differ in their authentication plugins and role-based access control, with MariaDB offering additional features like passwordless authentication. PostgreSQL employs a role-based security model where roles can function as users or groups, offering flexible privilege and role management. Across these systems, the principle of least privilege and regular review of user privileges are common best practices, ensuring a secure and well-managed database environment.
