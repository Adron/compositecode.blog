---
title: 'Quick Answers: What is the UUID column type good for and what exactly is a UUID?'
date: 2021-04-14 16:46:10 -0700
last_modified_at: 2021-04-14 16:46:10 -0700
permalink: /2021/04/14/quick-answers-what-is-the-uuid/
slug: quick-answers-what-is-the-uuid
wp_id: 63687
original_url: https://compositecode.blog/2021/04/14/quick-answers-what-is-the-uuid/
categories:
- Databases
tags:
- data types
- graphql
- guid
- postgres
- uuid
excerpt: The question has come up a few times recently about what UUIDs are and what they’re good for. In this quick answers post I explain what they are and provide reference links to further material, as well as a Hasura Short video to implementation and use in Postgres & Hasura.
image: /wp-content/uploads/2021/04/CleanShot-2021-04-14-at-16.45.29.png
---

The question has come up a few times recently about what UUIDs are and what they’re good for. In this quick answers post I explain what they are and provide reference links to further material, as well as a Hasura Short video to implementation and use in Postgres & Hasura.

## A Hasura Bit

<iframe allowfullscreen="true" class="youtube-player" height="486" loading="lazy" sandbox="allow-scripts allow-same-origin allow-popups allow-presentation allow-popups-to-escape-sandbox" src="https://www.youtube.com/embed/tQ8AaQyKKFk?version=3&amp;rel=1&amp;showsearch=0&amp;showinfo=1&amp;iv_load_policy=1&amp;fs=1&amp;hl=en-US&amp;autohide=2&amp;wmode=transparent" style="border:0;" width="863"></iframe>

*“A Hasura Bit – What sit he UUID column type good for and what exactly is a UUID?” video.*

## UUID

*UUID* stands for a universally unique identifier. Another term which is common for a UUID, is the *GUID*, or globally unique identifier, which is the common term Microsoft created for their UUIDs. Just know, that a GUID is a UUID, it’s just company naming convention vs the standard industry naming convention.

UUIDs are standardized by the Open Software Foundation (OSF) as part of the Distributed Computer Environment (DCE). Specifically UUID are designed and used from an USO/IEC spec, which if you’d like to know more about the standards they’re based on check out the Wikipedia page @ <https://en.wikipedia.org/wiki/Universally_unique_identifier>

## UUID Format

The canonical textual representation, the 16 octets of a UUID are represented as 32 hexadecimal (base-016) digits. They’re displayed across five groups separated by hyphens in 8-4-4-4-12 format. Even though there are 32 hexadecimal digits, this makes a total of 36 characters for format display. If storing as a string for example, the string needs to be able to hold 36 characters.

## Uses for a UUID

The first key use case for a UUID is to have something generate the UUID to use it as a completely unique value for use with a subset of related data. UUIDs are prefect for primary keys in a database, or simply any type of key to ensure uniqueness across a system.

UUIDs can be generated from many different origin points too without any significant concern for collision (i.e. duplicate UUIDs). For example, the database itself has database functions that enable the generation of a UUID at time of a data row’s insertion, as a default value. This means a client inserting data wouldn’t need to generate that UUID. However this can be flipped over to the client side as a responsibility and the client side development stack (i.e. like [Go UUID generation](/2018/05/14/uuid-solutions-w-go/)) can generate the UUID. Which then enables the creation of a primary key entity being created with a UUID as the primary key, that can then be used to create what would be foreign key items and so on down the chain of a relationship. Then once all of these are created on the client side they can all be inserted in a batch, and even if ordered appropriately can be made transactional to ensure the integrity of the data.
