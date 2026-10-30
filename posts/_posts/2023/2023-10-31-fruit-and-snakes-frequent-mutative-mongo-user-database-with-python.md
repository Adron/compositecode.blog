---
title: 'Fruit and Snakes: Frequent Mutative Mongo User Database with Python'
date: 2023-10-31 11:04:17 -0700
last_modified_at: 2023-12-07 10:08:50 -0800
permalink: /2023/10/31/fruit-and-snakes-frequent-mutative-mongo-user-database-with-python/
slug: fruit-and-snakes-frequent-mutative-mongo-user-database-with-python
wp_id: 67019
original_url: https://compositecode.blog/2023/10/31/fruit-and-snakes-frequent-mutative-mongo-user-database-with-python/
categories:
- Coding Adventures
- Databases
- python
tags:
- chaos
- mongo
- mongodb
- python
excerpt: I recently aimed to create a GraphQL API for a Mongo database, allowing users to query and modify collections, documents, and fields. Before starting, I needed an environment to simulate this process. This article discusses creating a test bed for this purpose.
image: /wp-content/uploads/2023/10/feet-standing-on-asphalt-with-multitude-of-arrows-2022-11-16-17-06-28-utc.jpg
---

The end results of this code base are used in another post I made, titled “[Java Time with Introspective GraphQL on Chaos Database AKA Pre- Refactor Prototype Mutating Database Spring Boot Java Hack App](/2023/12/01/java-time-with-introspective-graphql-on-chaos-database-aka-pre-refactor-prototype-mutating-database-spring-boot-java-hack-app/)“.

Recently I had a singular mission to build a GraphQL API against a Mongo database where the idea is, one could query the underlying collections, documents, and fields with the assumption that users would be adding or possibly removing said collections, documents, and fields as they needed.

That sounds somewhat straight forward enough, but before even getting started with the GraphQL API I really needed some type of environment that would mimic this process. That is what this article is about, creating a test bed for this criteria.

## The Mongo Database & Environment

First thing I did was setup a new Python environment using `virtualenv`. I wrote about that a bit in the past if you want to dig into that deeper, the post is available [here](/2019/12/25/unbreaking-python-through-virtual-environments/).

```
virtualenv fruit_schema_watcher
```

Next up I created a [git repo](https://github.com/Adron/fruit_schema_watcher) with `git init` then added a [README.md](https://github.com/Adron/fruit_schema_watcher/blob/main/README.md), [LICENSE](https://github.com/Adron/fruit_schema_watcher/blob/main/LICENSE) (MIT), and [.gitignore](https://github.com/Adron/fruit_schema_watcher/blob/main/.gitignore) file. The next obvious thing was the need for a Mongo database! I went to cracking on a docker-compose file, which formed up to look like this.

```
version: '3.1'

services:
  mongo:
    image: mongo:latest
    container_name: mongodb_container
    ports:
      - "27017:27017"
    environment:
      MONGO_INITDB_ROOT_USERNAME: root
      MONGO_INITDB_ROOT_PASSWORD: examplepass
    volumes:
      - mongo-data:/data/db

volumes:
  mongo-data:
```

With that server running, I went ahead and created a database called test manually. I’d just do all the work from here on out with that particular database.

## The Python Code Base

**Note**: I’ll be following up this post with a *refactoring* post. Don’t get up in arms about code quality, this was the *making it work* stage and I’ve got opinions and thoughts about how things need to end up for longevity.

The first bit of code I started working on putting together was something to generate a few things that I would need:

- the ability to generate a somewhat readable word.
- a random collection name, etc.

The two things translate into creating a semi-readable collection name and document for the collection. First thing up was to create some code that would give me that semi-readable word.

```
def generate_readable_word(length):
    vowels = "aeiou"
    consonants = "bcdfghjklmnpqrstvwxyz"
    if length == 0:
        return ""

    word = ""
    if random.choice([True, False]):
        word += random.choice(consonants)
    else:
        word += random.choice(vowels)

    for _ in range(length - 1):
        if word[-1] in vowels:
            word += random.choice(consonants)
        else:
            word += random.choice(vowels)

    return word
```

I wasn’t sure if I just wanted to pick from a random dictionary of words, and have a *word* file or actually generate made up words. Obviously, with the code above, I decided to opt for generating a made up word. I’d pass in the length, just a random number of some reasonable size for a made up word, and then go about placing consonants and vowels accordingly until I had this semi-readable word.

Next up was to create a randomly put together document I could insert into a collection. That looked a bit wild but after some munging of the code, I ended up with this.

```
def random_collection_collateral():
    collection_columns = []
    number_of_columns = random.randint(1, 10)
    if number_of_columns == 10:
        number_of_columns = random.randint(42, 99)

    data = {}
    for i in range(number_of_columns):
        column_name = generate_readable_word(random.randint(5, 12))
        collection_columns.append(column_name)
        data[column_name] = generate_readable_word(random.randint(10, 20))
        print(column_name + " added.")

    json_data = json.dumps(data)
    print(json_data)
    return json_data
```

While writing up this code, I started breaking things out to different files for a little organization. My intent of course, is to go back and refactor as soon as I get things into a general working state that makes a little bit of sense. The previous two code snippets I put in a file called word\_generator.py, and this next snippet of code I put in a file called database\_actions.py. Again, I’d eventually refactor these into a more refined state, but this way I at least have a quick generally organized bit of code.

In the database\_actions.py I wanted to put the specific calls that would be made to the database. Not really a data layer, but sort of a data layer. That code shaped up to work like this:

```
def the_deluge_of_chaos():
    mongo_collection = generate_readable_word(5)
    collection_document = random_collection_collateral()

    client = MongoClient('mongodb://root:examplepass@localhost:27017')
    db = client['test']

    db.create_collection(mongo_collection)
    collection = db[mongo_collection]
    print(mongo_collection + " has been created.")

    collection_document = eval(collection_document)

    collection.insert_one(collection_document)
    print(collection_document)
    print("...has been created.")

    client.close()
```

In this code I put together the collection and document, and then make the connection, create the collection, then insert the document into the collection. I do like how the Python library interacts with the collection and document object for Mongo, it is a pretty slick implementation.

The divergent naturally nested object hierarchy of the underlying BSON comes out in the object in object array relation which makes for a pretty logical flow to deal with documents in the collection. It also lends to making an interesting setup if you end up with multiple documents with different structures to them. However, stay privy to this as it can also lead to discrepency of logic and a confusing interaction with the underlying database since one doesn’t have an automatic kind of filter, from an object perspective, and about which set of documents (i.e. objects) one is dealing with from the database perspective. Anyway, more on that in a subsequent post!

## Chaos Service

Next up I want to have the service run and every few seconds execute an addition of a random number of collections and their initial document added to the database. I created a file called chaos.py and added a short little snippet to run `the_deluge_of_chaos()` a number of times.

```
from database_actions import the_deluge_of_chaos
import random

def the_deluge():
    range_of_chaos = random.randint(1, 3)
    for i in range(range_of_chaos):
        the_deluge_of_chaos()
```

Now the service itself. I broke this out into a file called service.py with a class for the definition of the service.

```
class FiveSecondService:
    def __init__(self):
        self._stop_event = threading.Event()
        self._thread = threading.Thread(target=self._run)

    def start(self):
        """Start the service."""
        self._stop_event.clear()
        self._thread.start()

    def stop(self):
        """Stop the service."""
        self._stop_event.set()
        self._thread.join()

    def _run(self):
        while not self._stop_event.is_set():
            start_time = time.time()
            self.execute_code()

            elapsed_time = time.time() - start_time
            time_to_sleep = max(0, 5 - elapsed_time)
            time.sleep(time_to_sleep)

    def execute_code(self):
        # This is the part that runs every 5 seconds.
        the_deluge()
        print("Code executed at:", time.strftime('%Y-%m-%d %H:%M:%S'))
```

After this I added the section for execution of the service.

```
if __name__ == "__main__":
    service = FiveSecondService()
    try:
        service.start()
        while True:
            time.sleep(1)  # Keep the main thread alive
    except KeyboardInterrupt:
        service.stop()
        print("Service stopped.")
```

A few important things to note include the fact that this doesn’t really work the way I thought it would. The keyboard interrupt still requires a Ctrl+C to stop execution, which means I could just take out the try except and have it just run until I stop it via break. However I’ve left this bit of code in as something that mostly works, but I’ll debug and refactor it once this is up and running.

## Summary

With all this done and implemented (check out this repo [db-chaos-freeze-v1-pre-refactor](https://github.com/Adron/fruit_schema_watcher/tree/db-chaos-freeze-v1-pre-refactor) branch here for the full project as discussed in this post) I’ve now got a service that will randomly generate a collection name, build out a simple document, and add that collection to a MongoDB and insert the document every 5 seconds. Perfecto!

In the next post I’ll show you how I’ve put together a system to provide the ability to query against this ever change Mongo Database! Until then, happy thrashing code! 🤘🏻

## References

- The repository: [fruit\_schema\_watcher](https://github.com/Adron/fruit_schema_watcher) for this post.
- Python [installation post](/2019/12/23/getting-started-with-python-right/) and [my basic setup](/2020/05/27/language-stack-installation-for-python-go/) (with videos + Go).
- [Basic use of Flask](/2019/12/27/using-pythons-flask-to-build-a-basic-api-creating-the-didactic-engine-flask/).
- The post, where I build a query GraphQL API to this particular database with Java Spring Boot, is available as [Java Time with Introspective GraphQL on Chaos Database AKA Pre- Refactor Prototype Mutating Database Spring Boot Java Hack App](/2023/12/01/java-time-with-introspective-graphql-on-chaos-database-aka-pre-refactor-prototype-mutating-database-spring-boot-java-hack-app/).
