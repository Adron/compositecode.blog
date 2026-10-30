---
title: The Best Collected Details on the GraphQL Specification – Overview & Language
date: 2021-12-29 11:37:26 -0800
last_modified_at: 2022-10-06 12:38:57 -0700
permalink: /2021/12/29/the-best-collected-details-on-the-graphql-specification-overview-language/
slug: the-best-collected-details-on-the-graphql-specification-overview-language
wp_id: 64680
original_url: https://compositecode.blog/2021/12/29/the-best-collected-details-on-the-graphql-specification-overview-language/
categories:
- graphql
tags:
- api
- graphql
- graphql specification
- javascript
- json
- programming
excerpt: GraphQL, a query language and execution engine is described in this specification based on capabilities and requirements of data models for client-server applications. This article details and elaborates on the specification, the features and capabilities of GraphQL and… The Humans Every aspect of languages and specifications are created with context of an end user human. The specification is a project by…
image: /wp-content/uploads/2021/12/specifications.png
---

GraphQL, a query language and execution engine is described in this specification based on capabilities and requirements of data models for client-server applications. This article details and elaborates on the specification, the features and capabilities of GraphQL and implementations. I hope this collection of details around the GraphQL Specification can be used as a reference and launch point into learning about GraphQL use, implementation – server and client side – and ongoing references during future specification additions or changes!

## The Humans

Every aspect of languages and specifications are created with context of an end user human. The specification is a project by the [Joint Development Foundation](https://www.jointdevelopment.org), with a current [Working Group](https://github.com/graphql/graphql-wg) charter that includes the IP policy governing all working group deliverables (i.e. new features, changes of spec, source code, and datasets, etc). To join the [Working Group](https://github.com/graphql/graphql-wg) there are details for [membership](https://github.com/graphql/graphql-wg/tree/main/membership) and [details in the agreement](https://github.com/graphql/graphql-wg/blob/main/membership/GraphQL-Specification_Membership-2021-01-25-PREVIEW.pdf) for joining the efforts of the group.

## Licensing, Notation, Grammar, & Syntax

Current licensing for the GraphQL Specification and related [Working Group](https://github.com/graphql/graphql-wg) deliverables fall under the [Open Web Foundation Agreement 1.0 Mode](https://www.openwebfoundation.org/the-agreements/the-owf-1-0-agreements-granted-claims/owf-contributor-license-agreement-1-0-copyright-and-patent) (Patent and Copyright).

The syntax grammar and related specifics are laid out in the document, which for this article it isn’t necessary to dig through the specifics of this. The research done and collected for this article has that covered for you dear reader, however if you do dig into the specification itself I strongly suggest reading these to insure you specifically know what is represented by what.

## Description of GraphQL

The specification starts off with a detailed description of GraphQL. More detailed than a lot of descriptions that one would find in articles on the topic, which makes it extremely valuable for anyone who wants to really get a rich and thorough understanding of GraphQL. The first sentence of the October 2021 Edition of the specification provides a great high level definition,

> …a query language and execution engine originally created at Facebook in 2012 for describing the capabilities and requirements of data models for client-server applications.

A few things outside of the spec you’ll read often is, "GraphQL is a query language similar to SQL", which is true, but not. I’ve even seen descriptions like "GraphQL is a programming language" which is a hard no. Taking the specification description provides clarity around some of these simplified definitions that could leave one confused.

GraphQL, as defined, is not a programming language and not capable of arbitrary computation. This is important to note, as many of the platforms and services that provide GraphQL APIs could lead one to think that GraphQL is providing much of the functionality in these platforms, when really it is merely the facade and presentation via API of the capabilities of the underlying systems and platforms (re: [Hasura](https://hasura.io), [AppSync](https://aws.amazon.com/appsync/), [Astra](https://www.datastax.com/products/datastax-astra), [Atlas](https://www.mongodb.com/atlas), [Dgraph](https://dgraph.io), [Contentful](https://www.contentful.com), [GraphCMS](https://hygraph.com/) (now [Hygraph](https://hygraph.com/)), etc).

Enough about what GraphQL isn’t per the spec, what does define GraphQL? Reading the design principles behind the specification provide a much clearer idea of what GraphQL is intended to do.

- Product-centric – The idea behind GraphQL is focused on the product first. With emphasis around what the user interface, and specifically the front-end engineers, want and need for display and interaction with an application’s data. Extending this it behooves one to design GraphQL APIs around data storage mechanisms that encourage this type of user interface first, and arguably even user experience first design practices. This often includes databases like Dynamo DB, Apache Cassandra, or AWS Neptune as systems that necessitate designing from the front end into the data. Where as it draws conflicts on those that try to follow tightly coupled database first design practices with systems like relational databases. However, that identified as a characteristic, note that it doesn’t preclude design first practices – like GraphQL is designed for – with databases like relational databases. It just provides an avenue of conflict for those that want data first design since that is an entrenched practice with relational databases.
- Hierarchical – GraphQL is oriented toward the creation of and manipulation of hierarchical views. So much that GraphQL requests are structured as such.
- Strong-typing – Every GraphQL service defines an application-specific type system and requests are made in that context. This design principle is also why one will find regular use of TypeScript with GraphQL, specifically in the JavaScript web world. The two are matched very well to manage and extend strong-types to the systems using the GraphQL API. This also extends well, albeit with more mapping specifics needed to ensure types match. This design principle provides a solid level of type safety for GraphQL use within application development.
- Client-specified response – Based on this design pattern GraphQL provides a published capability for how clients will, or can, access the API. These requests provide field-level granularity. With that provided, the client can then provide exactly what it needs to retrieve from this field-level granularity. This particular characteristic is what gives GraphQL it’s famed
- Introspective – The ability to introspect against an API and derive what is available, and in many cases derive how or what to do with what is available, is a very powerful feature of GraphQL APIs. All of the intricate power of SOA Architectures without the conflagrations of XML, SOAP, and WSDLs. Arguably, one could say that GraphQL is SOA right? Ok, getting off in the weeds here, let’s keep rolling!

## Language

Clients accessing the GraphQL API use the GraphQL Query Language. These requests are referred to as documents. These documents can contain one of the operations available from a GraphQL API: queries, mutations, or subscription, as well as fragments that allow for various data requirements reuse.

The GraphQL document follows a particular processing paradigm. First the document is converted into tokens and ignored tokens. This is done scanning left to right, repeatedly taking the next possible *sequence of code-points* allowed by the lexical grammar as the next token. This produces the AST (**A**bstract **S**yntax **T**ree). There are other specifics to how the document is processed, but from a usage perspective the primary paradigm of tokens, ignored tokens, and processing order are sometimes helpful to know about the processing of the GraphQL Document.

So far, this covers sections 1 and the start of section 2. The other parts of section 2.x cover a wide range of what the document can use and be made of from a source text perspective, which Unicode characters, that it needs to be Unicode, can have and utilizes white space and line terminators to improve legibility, and other characteristics that can be assumed, since almost every text formatted document type in the industry uses this today.

2.1.4 covers comments, which are important to note that the comment character is the `#` sign. 2.1.5 describes the role of insignificant commas, those that provide readability such as stylistic use of either trailing commas or line terminators as list delimiters.

2.1.6 is about ***Lexical Tokens***, where we get into one of the two key elements of the overall GraphQL document. A Lexical Token is made up of several kinds of indivisible lexical grammar. These tokens can be separated by Ignored Tokens. The Lexical Tokens consist of the following:

Token ::
Punctuator
Name
InValue
FloatValue
StringValue

2.1.7 is about ***Ignored Tokens***, the element that can be used to improve readability and separated between Lexical Tokens. Ignored Tokens are Unicode BOM, white space, line terminator, comments, or comma.

Within a token, there are ***punctuators***, made up of *one* the following:

*! $ & ( ) … : = @ [ ] { | }*

Names in 2.1.9 are defined as alphanumeric characters and the underscore. These are case-sensitive letters thus `word`, `Word`, and `WORD` are entirely different names.

The next key element of the language are the Operations (defined in 2.3). There are three specific operations:

1. query
2. mutation
3. subscription

An example, inclusive of additional tokens would look something like this.

```javascript
mutation {
  getThisWidget(widgetId: 666) {
	widget {
	  widgetValues
	}
  }
}
```

A special case is shorthand, provided for the query operation. In this case, if the only operation in a GraphQL Document is a query, the query operation keyword can be left out. So an example would be that this

```javascript
query {
	widget {
		widgetValues
	}
}
```

would end up looking like this.

```javascript
{
	widget {
		widgetValues
	}
}
```

In 2.4 ***Selection Sets*** are defined as "*An operation selects the set of information it needs, and will receive exactly that information and nothing more, avoiding over-fetching and under-fetching data*" which is of course one of the key feature-sets of GraphQL. The idea of minimizing or eliminating over- or under-fetching of data is a very strong selling point! A query, for example

```javascript
{
	id
	train
	railroad
}
```

would only return exactly the data shown, eliminating excess across the wire to the client. Elaborating on this, imagine the underlying table or database storing not just the id, train, and railroad, but the inception of the railroad, extra peripheral details, maybe some extra key codes, or other information. Querying all of the data would look like this.

```
{
	id
	train
	railroad
	inceptionDate
	details
	peripheralDetails
	keyCodeA
	keyCodeB
	keyCodeC
	information
}
```

This of course, would get all of the data, but pending we don’t need all of that, fetching only the key fields we need with the absolute minimal amount of language syntax is a feature set, and strength of GraphQL.

Each of the Selection Sets, as in the examples above, is made up of Fields (2.5 in spec). Each field is either a discrete piece of data, complex data, or relationship to other data.

This example shows a discrete piece of data that is being requested.

```javascript
{
	train {
		namedTrain
	}
}
```

This discrete request would return a value that would provide the named trains of the train type.

Then a complex type in a query might look like this.

```javascript
{
	train {
		startDate {
			day
			month
			year
		}
	}
}
```

Even though one could use a date field as a singular discrete piece of data, in this example startDate is a complex type with the parts of the starting date for the train type being broken out to day, month, and year.

Another might have a correlative relationship that looks similar to the above discrete data example, except there are the nested values of the related element.

```javascript
{
	train {
		namedTrain
		startDate {
			year
		}
		railroads {
			foundingYear
			history
		}
	}
}
```

In the above example, we are specifically fetching only the year of the complex type startDate, and returning the related object railroad that has correlative related values foundingYear and history.

From a conceptual point of view, fields are functions that return a value. GraphQL doesn’t dictate what or how that function would execute to return that value, only that the value would be returned. The underlying function would many times need an argument passed to identify the field value to return, in this case ***Arguments*** are implemented through an argument list in parenthesis attached to the field identifier.

```javascript
{
	train(id: 1) {
		namedTrain
	}
}
```

In this example the train retrieved has an id equal to 1, which will return a singular train with the field namedTrain returned. Let’s say the train had a certain seat type that could be returned based on various parameters.

```javascript
{
	train(id: 1, seatClass: 1) {
		namedTrain
		seats {
			passengerCar
			number
		}
	}
}
```

The return list of seats for the train would consist of the seat and passenger car the seat is in, based on the seatClass equaling 1.

Another way to build results is with the Field Alias specification (2.7). Imagine you want to return a field with a picture of the train at thumbnail size and display size.

```javascript
{
	train(id: 1) {
		smallTrainImage: trainPic(imageType: "thumbnail")
		fullsizeTrainImage: trainPic(imageType: "display")
	}
}
```

This example would return the thumbnail size image, stored as field trainPic, in the smallTrainImage field alias. The fullsizeTrainImage field alias providing the return field for the trainPic that is matched to display imageType.

Another example, similarly focused on the above might be providing return the types of seats that are available for a particular train divided into the 1st, 2nd, and 3rd class named as firstClass, businessClass, and coachClass seats accordingly.

```javascript
{
	train(id: 1) {
		namedTrain
		firstClass: seats(seatClass: 1) {
			passengerCar
			number
		}
		businessClass: seats(seatClass: 2) {
			passengerCar
			number
		}
		coachClass: seats(seatClass: 3) {
			passengerCar
			number
		}
	}
}
```

The above also display the concept described in 2.8 ***Fragments***. Fragments allo for the reuse of common repeated selects of fields, reducing duplicated text in the document.

In the above this also provides further accentuation and focus to the aforementioned *Selection Sections* fetching specificity. Most specifically stated, providing more options to prevent needless round-trips, excess data per request, and preventing getting too little data and requiring those extra round trips. Fetching problems mitigated!

A sub section of a subsection, for the language section of the specification is on ***Type Conditions*** 2.8.1 and ***Inline Fragments*** 2.8.2. Fragments must specify the type they apply to, cannot be specified on any input value, and only return values when the concrete type of the object matches the type fragment. Fragments can also be defined inline to a selection set. This conditionally includes fields at runtime based on their type.

```javascript
query FragmentTyping {
	trainConsist(handles: ["baggage", "passenger"]) {
		handle
		...baggageFragment
		...passengerFragment
	}
}

fragment baggageFragment on BaggageUnit {
	baggageUnits {
		count
	}
}

fragment passengerFragment on PassengerUnit {
	passengerUnits {
		count
	}
}
```

With a result that would look like this.

```javascript
{
  "profiles": [
    {
      "handle": "baggage",
      "baggageUnits": { "count": 1 }
    },
    {
      "handle": "passenger",
      "passengerUnits": { "count": 11 }
    }
  ]
}
```

Something similar could be done with inline fragments too. Additionally Inline Fragments can be used to apply a directive too. More on that and this later!

***Input Values***, starting in section 2.9 have a number of sub section defining the characteristic and features of Input Values. Field and directive argument accept input values with literal primitives. Input Values can include scalars, enumeration values, lists, or input objects. Another ability of Input Values is to define them as variables. For each of these there are numerous semantic details. The following breakdown are the specific core details of note for the values.

- 2.9.1 Int Value – This value is specified as a decimal point or exponent, no leading zero, and can be negative.
- 2.9.2 Float Value – Floats include either a decimal point or exponent or both can be negative, and no leading zero.
- 2.9.3 Boolean Value – Simple, either *true* or *false*.
- 2.9.4 String Value – Strings are sequences of characters wrapped in quotation marks (i.e. "This is a string value that is a sentence."). There can also be block strings, across multiple lines using three quotes to start and end on the line before and after the string text. As shown here “`"""
  The text goes here just after the starting quotes.

then some more text.

last line… then followed by the three quotes.
"""“`.

- 2.9.5 Null Value – `null` which is kind of nuff’ said. Sometimes, just like in databases, I’m not entirely sure how I feel about null being included in so many things.
- 2.9.6 Enum Value – These values are represented as unquoted names, and recommended to be all caps.
- 2.9.7 List Value – Wrapped by square-brackets (i.e. brackets vs. braces) [ ]. Commas are optional for separation and readability. Both [1, 2, 3] and [1 2 3] are the same.
- 2.9.8 Input Object Value – These are unordered lists wrapped in curly-braces (i.e. braces, vs brackets) { }. These are referred to as object literals and might look like `{ name: Benjamin }` or `{ price: 4.39 }`.

Variables for Input Values are for parameterized for reuse. An example would look like this.

```javascript
query getTrainsList($inceptionYear: Int) {
	train {
		id
		namedTrain
		details
	}
}
```

***Type references*** (2.11) are types of data used for arguments and variables, can be lists of another input type, or non-null variant of any other input type.

Even though 2.12 is a minimal section in the specification, it’s a hugely powerful feature that is used extensively in various GraphQL services options, which is ***Directives***. Directives provide a way to define runtime execution and type validation behavior in a GraphQL document that is different than specification based behaviors. Directives have a name with arguments listed of whichever input types. They can also describe additional information for types, fields, fragments, and operations. New configuration options for example could be setup via Directives.

Note Directive order is significant. For example these two examples could have difference resolutions:

```javascript
type Freight
	@addFreight(source: "farmSystems")
	@excludeFreight(source: "toxicities") {
	name: String
}
```

```javascript
type Freight
	@excludeFreight(source: "toxicities")
	@addFreight(source: "lightCars"){
	name: String
}
```

That wraps up GraphQL section 1 and 2, covering the core language. Next up is the type system, schema, and related topics in section 3 of the specification. Notes coming soon!

> Reference <https://spec.graphql.org> specifically October 2021 Edition.
