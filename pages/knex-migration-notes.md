---
layout: page
title: knex Migration Notes
date: 2014-09-29 15:47:40 -0700
last_modified_at: 2018-04-19 15:12:32 -0700
permalink: /knex-migration-notes/
slug: knex-migration-notes
wp_id: 10295
original_url: https://compositecode.blog/knex-migration-notes/
---

Migrate

```bash
knex migrate:latest
```

Rollback

```bash
knex migrate:rollback
```

Migrate/Rollback to a specific Environment

```bash
knex migrate:latest --env test
```
