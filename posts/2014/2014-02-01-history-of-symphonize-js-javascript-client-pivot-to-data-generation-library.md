---
title: History of Symphonize.js – JavaScript Client Pivot to Data Generation Library
date: 2014-02-01 06:47:24 -0800
last_modified_at: 2014-02-04 14:30:58 -0800
permalink: /2014/02/01/history-of-symphonize-js-javascript-client-pivot-to-data-generation-library/
slug: history-of-symphonize-js-javascript-client-pivot-to-data-generation-library
wp_id: 9544
original_url: https://compositecode.blog/2014/02/01/history-of-symphonize-js-javascript-client-pivot-to-data-generation-library/
categories:
- Community
- Databases
- Distributed Things
- How-to
- Javascript
- Node.js Things
- Orchestrate.io
tags:
- chance.js
- configuration
- configuration json
- data
- databases
- distributed database
- graph
- graph data
- graph store
- javascript
- json
- key
- key value
- key value data
- keyvalue
- node
- node.js
- nodejs
- orchestrate
- orchestrate.io
- orchestrateio
- symphonize
- symphonize.js
- value
excerpt: '…the history of symphonize.js So Far! NOTE: If you just want to check out the code bits, scroll down to the sub-title #symphonize #hacking. Also important to note I’m putting the library through a fairly big refactor at the moment so that everything aligns with the documentation that I’ve recently created. So many things may not …'
image: /wp-content/uploads/2014/01/javascript-logo.png
---

…the history of [symphonize.js](https://github.com/Adron/symphonize) So Far!

**NOTE:** If you just want to check out the code bits, scroll down to the sub-title ***#symphonize #hacking***. Also important to note I’m putting the library through a fairly big refactor at the moment so that everything aligns with the documentation that I’ve recently created. So many things may not be implemented, but we’re moving toward v0.1.0, which will be a functional implementation of the library available via npm based entirely on the documentation and specs that I outline after the history.

## A Short History

I started the symphonize.js project back on the 1st of November. Originally I started the project as a [client driver library](/2013/11/01/orchestrateio-javascript-client-library/) for [Orchestrate.io](http://orchestrate.io), but within a day Chris Molozian commented and pointed out that there was already a client driver library for Orchestrate.io available that Steve Kaliski (Github [@sjkaliski](https://github.com/sjkaliski) and Twitter [@stevekaliski](https://twitter.com/stevekaliski) and <http://stevekaliski.com/>) had coded called logically [orchestrate.js](https://github.com/Bowery/orchestrate.js). Since this was available I did a [pivot to symphonize.js being a data generation project](/2013/11/18/hacking-some-code-and-project-pivots/) instead.

[![The comment that enabled symphonize.js to pivot from client driver to data generation library.](https://photos.adron.me/Software/Software-Development/Symphonize/i-QBk45qd/0/M/Orchestrate_io_JavaScript_Client_Library___Composite_Code-M.png "The comment that enabled symphonize.js to pivot from client driver to data generation library.")](/2013/11/01/orchestrateio-javascript-client-library/#comment-203757)

*The comment that made me realize symphonize.js should pivot from client driver to data generation library.*

## The Official Start of Symphonize.js

[![](https://photos.adron.me/Software/Software-Development/Symphonize/i-qpwqkkP/0/S/npm-S.png)](https://npmjs.org/package/symphonize)After that start and quick pivot I posted a blog with Orchestrate.io titled “[Test Data Builder Symphonize.js With Chance.js (1/3)](http://blog.orchestrate.io/blog/7/test-data-builder-symphonizejs-with-chancejs)” to officially start the project. In that post I covered key value and graph basics, with a dive into using [chance.js](http://chancejs.com/) and orchestrate.js with examples. Near the same time I also posted a related blog on [publishing an NPM module, which is the deployment focus of Symphonize.js](/2013/11/03/how-to-build-an-npm-package-beginning-the-symphonize-project/).

## Reasons Reasoning

[![](https://photos.adron.me/Software/Software-Development/Symphonize/i-NkXsMS5/0/O/graph-example1.png)](http://blog.orchestrate.io/blog/7/test-data-builder-symphonizejs-with-chancejs)There are two main reasons why I chose Orchestrate.io and a data generation library as the two things I wanted to combine. The first, is I knew the orchestrate.io team and really dug what they were building. I wanted to work with it and check out how well it would work for my use cases in the future. The ability to go sit down, discuss with them what they were building was great (which I interviewed Matt Heitzenroder [@roder](https://twitter.com/roder) that you can watch *[Orchestrate.io, Stop Dealing With the Database Infrastructure!](/2013/10/22/orchestrate-io-to-the-death-of-database-infrastructure/)*) The second reason is that my own startup that I’m co-founding with Aaron Gray ([@agray](http://twitter.com/agray)) needed to use key value and graph data storage of some type, somewhere. Orchestrate.io looked like a perfect fit. After some research, giving it a go, it fit very well into what we are building.

## CRUD, cURL Hacking & Next Steps

Early December I knocked out two support articles about testing APIs with cURL in [*Some JavaScript API Coding With Restify & Express & Hacking it With cURL …Segment #1 (with some Webstorm to boot)*](/2013/12/01/some-javascript-api-coding-with-restify-express-hacking-it-with-curl-segment-1/) and *[Some JavaScript API Coding With Restify & Express & Hacking it With cURL …Segment #2](/2013/12/08/some-javascript-api-coding-with-restify-express-hacking-it-with-curl-segment-2/)* and an article on the Orchestrate.io Blog for part 2 of that series titled [*Symphonize Some Create, Read, Update & Delete [CRUD] via Orchestrate.js (2/3)*](http://blog.orchestrate.io/blog/12/create-read-update-delete-crud).

December then rolled into the standard holiday doldrums and slowdowns. So fast forward to January post a few rounds of beer and good tidings and I got the 3rd in the series published titled [Getting Serious With Symphony.js – JavaScript TDD/BDD Coding Practices (3/3)](http://blog.orchestrate.io/blog/3/g8mnf0f3tdf6sezl44i8e7wpddkhrt). The post doesn’t speak too much to symphony.js usage but instead my efforts to use TDD or BDD practices in trying to write the library.

Slowly I made progress in building the library and finally it’s in a mostly releasable state now. I use this library daily in working with the code base for Deconstructed and imagine I’ll use it ongoing for many other projects. I hope others might be able to find uses for it too and maybe even add capabilities or ideas. Just ping me via Twitter [@adron](http://twitter.com/adron) or Github [@adron](https://github.com/adron), [add an issue on Github](https://github.com/Adron/symphonize/issues/new) and I’ll be happy to accept pull requests for new features, code refactoring, add you to the project or whatever else you’re interested in.

## #symphonize #hacking

[![](https://photos.adron.me/Software/Software-Development/Symphonize/i-nB8K3Cf/0/S/SymphonizeOrchestrateBowery-S.png)](https://github.com/Adron/symphonize) Now for the nitty gritty. If you’re up for using or contributing to the project check out the [symphonize.js github pages site](http://adron.github.io/symphonize/) first. It’s got all the information to help get you kick started. However, you can keep reading as I’ve included much of the information there along with the examples from the [README.md](https://github.com/Adron/symphonize/blob/master/README.md) below.

**NOTE:** As I mentioned at the top of this blog entry, the funcitonal implementation of code isn’t available via npm just yet, myself and some others are ripping through a good refactor to align the implementation fo the library with the rewritten and newly available documentation – included blow and at the github pages.

***How to use this project in one of your projects.***

```bash
npm install symphonize
```

***How to setup this project for development.***

First fork the repository located at <https://github.com/Adron/symphonize>.

```javascript
git clone git@github.com:YourUserName/symphonize.git
cd symphonize
npm install
```

## Using The Library

The intended usage is to invocate the JavaScript object and then call generate. That’s it, a super simple process. The code would look like this:

```javascript
var Symphonize = require('../bin/symphonize');
var symphonize = new Symphonize();
```

The basic constructor invocation like this utilizes the generate.json file to generate data from. To inject the json configuration programmatically just inject the json configuration information via the constructor.

```javascript
var configJson = {"schema":"keyvalue"};

var Symphonize = require('../bin/symphonize');
var symphonize = new Symphonize();
```

Once the Symphonize data generator has been created call the generate() method as shown.

```javascript
symphonize.generate();
```

That’s basically it. But you say, it’s supposed to do X, Y or Z. Well that’s where the json configuration data comes into play. In the configuration data you can set the data fields and what they’ll generate, what type of data will be generated, the specific schema, how many records to create and more.

## generate.json

The library comes with the generate.json file already setup with a working example. Currently the generation file looks like this:

```javascript
{
    "schema": "keyvalue", /* keyvalue, graph, event, geo */
        "count": 20, /* X values to generate. */
    "write_source": "console", /* console, orchestrateio and whatever other data sources that might come up. */
    "fields": {
            /* generates a random name. */
            "fieldName": "name",
            /* generates a random dice roll of a d20. */
            "fieldTwo": "d20",
            /* A single lorum ipsum random statement is genereated. */
            "fieldSentence": "sentence",
            /* A random guid is generated. */
            "fieldGuid": "guid"    }
}
```

**Configuration File Definitions**

Each of the configuration options that are available have a default in the configuration file. The default is listed in italics with each definition of the configuration option listed below.

- “*schema*” : This is used to select what type of data structure type is going to be generated. The default is*keyvalue* for this option.
- “*count*” : This provides the total records that are to be generated by the library. The default is *1* for this option.
- “*write\_source*” : This provides the location to output the generated data to. The default is *console* for this option.
- “*fields*” : This is a JSON field within the JSON configuration file that provides configuration options around the fields, number of fields and their respective data to generate. The default is *one field*, with a default data type of *guid*. Each of the respective entries in this JSON option is a self contained JSON name and value pair. This then looks simply like this (which is also shown above in part):

  ```javascript
  {
      "someBoolean": "boolean",
      "someChar": "character",
      "aFloat": "float",
      "GetAnInt": "integer",
      "fieldTwo": "d20",
      "diceRollD10": "d10",
      "_string": {
          "fieldName": "NameOfFieldForString",
          "length": 5,
          "pool": "abcdefgh"
      },
      "_sentence": {
          "fieldName": "NameOfFiledOfSentences",
          "sentence": "5"
      },
      "fieldGuid": "guid"
  }
  ```
- **Fields Configuration**: For each of the fields you can either set the field to a particular data type or leave it empty. If the field name and value pair is left empty then the field defaults to *guid*. The types of data to generate for fields are listed below. These listed are all simple field and data generation types. More complex nested generation types are listed below under *Complex Field Configuration* below the simple section.
  - “*boolean*“: This generates a boolean value of true or false.
  - “*character*“: This generates a single character, such as ‘1’, ‘g’ or ‘N’.
  - “*float*“: This generates a float value, similar to something like -211920142886.5024.
  - “*integer*“: This generates an integer value, similar to something like 1, 14 or 24032.
  - “*d4*“: This generates a random integer value based on a dice roll of one four sided dice. The integer range being 1-10.
  - “*d6*“: This generates a random integer value based on a dice roll of one six sided dice. The integer range being 1-10.
  - “*d8*“: This generates a random integer value based on a dice roll of one eight sided dice. The integer range being 1-10.
  - “*d10*“: This generates a random integer value based on a dice roll of one ten sided dice. The integer range being 1-10.
  - “*d12*“: This generates a random integer value based on a dice roll of one twelve sided dice. The integer range being 1-10.
  - “*d20*“: This generates a random integer value based on a dice roll of one twenty sided dice. The integer range being 1-20.
  - “*d30*“: This generates a random integer value based on a dice roll of one thirty sided dice. The integer range being 1-10.
  - “*d100*“: This generates a random integer value based on a dice roll of one hundred sided dice. The integer range being 1-10.
  - “*guid*“: This generates a random globally unique identifier. This value would be similar to ‘F0D8368D-85E2-54FB-73C4-2D60374295E3’, ‘e0aa6c0d-0af3-485d-b31a-21db00922517’ or ‘1627f683-efeb-4db8-8174-a5f2e3378c87’.
- **Complex Field Configuration**: Some fields require more complex configuration for data generation, simply because the data needs some baseline of what the range or length of the values need to be. The following list details each of these. It is also important to note that these complex field configurations do not have defaults, each value must be set in the JSON configuration or an error will be thrown detailing that a complex field type wasn’t designated. Each of these complex field types is a JSON name and value parameter. The name is the passed in data type with a preceding underscore ‘\_’ to generate with the value having the configuration parameters for that particular data type.
  - “*\_string*“: This generates string data based on a *length* and *pool* parameters. Required fields for this include *fieldName*, *length* and *pool*. The JSON would look like this:

    ```javascript
    "_string": {
        "fieldName": "NameOfFieldForString",
        "length": 5,
        "pool": "abcdefgh"
    }
    ```

    Samples of the result would look like this for the field; ‘abdef’, ‘hgcde’ or ‘ahdfg’.
  - “*\_hash*“: This generates a hash based on the *length* and *upper* parameters. Required fields for this included *fieldName*, *length* and *upper*. The JSON would look like this:

    ```javascript
    "_hash": {
        "fieldName": "HashFieldName",
        "length": 25,
        "casing": 'upper'
    }
    ```

    Samples of the result would look like this for the field: ‘e5162f27da96ed8e1ae51def1ba643b91d2581d8’ or ‘3F2EB3FB85D88984C1EC4F46A3DBE740B5E0E56E’.
  - “*\_name”: This generates a name based on the *middle*, \*middle*initial\* and *prefix* parameters. Required fields for this included *fieldName*, *middle*, *middle\_initial* and *prefix*. The JSON would look like this:

    ```javascript
    "_name": {
        "fieldName": "nameFieldName",
        "middle": true,
        "middle_initial": true,
        "prefix": true
    }
    ```

    Samples of the result would look like this for the field: ‘Dafi Vatemi’, ‘Nelgatwu Powuku Heup’, ‘Ezme I Iza’, ‘Doctor Suosat Am’, ‘Mrs. Suosat Am’ or ‘Mr. Suosat Am’.

So that covers the kick start of how eventually you’ll be able to setup, use and generate data. Until then, jump into the project and give us a hand.

After this, more examples on the way, cheers!
