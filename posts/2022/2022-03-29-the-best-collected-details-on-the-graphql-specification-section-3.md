---
title: The Best Collected Details on the GraphQL Specification, Section 3
date: 2022-03-29 19:36:15 -0700
last_modified_at: 2022-03-29 19:36:15 -0700
permalink: /2022/03/29/the-best-collected-details-on-the-graphql-specification-section-3/
slug: the-best-collected-details-on-the-graphql-specification-section-3
wp_id: 65204
original_url: https://compositecode.blog/2022/03/29/the-best-collected-details-on-the-graphql-specification-section-3/
categories:
- graphql
- Javascript
tags:
- graphql
- javascript
- json
- specification
excerpt: This is the second part to a collection of notes and details, think of this as the cliff notes of the GraphQL Spec. Onward to section 3 of the spec… The GraphQL type system is described in section 3 of the specification.
image: /wp-content/uploads/2022/03/spec-section3.png
---

> References [https://spec.graphql.org](https://spec.graphql.org/) specifically October 2021 Edition.

This is the second part (the [first part covered the overview and language of GraphQL](/2021/12/29/the-best-collected-details-on-the-graphql-specification-overview-language/)) to a collection of notes and details, think of this as the cliff notes of the GraphQL Spec. Onward to section 3 of the spec…

The GraphQL type system is described in section 3 of the specification. Per the specification itself,

> The GraphQl Type system describes the capabilities of a GraphQL service and is used to determine if a requested operation is valid, to guarantee the type of response results, and describes the input types of variables to determine if values provided at request time are valid.

This feature of the specification for the GraphQL language uses Interface Definition Language (IDL) to describe the type system. This can be used by tools to provide utility function as client code genration or boot-strapping. In a lot of the services and products around GraphQL like AppSync, Hasura, and others you’ll see this specifically in action. Tools that only execute requests can only allow TypeSystemDocument and disallow ExecuteDefintion or TypeSystemExtension to prevent extensions of the type system. If you do this be sure to provide a descriptive error for consumers of your data!

The section continues and we’ll get into each subsection, but this will be out of order as the specification ordering is a little out of sequence. The first few elements of the specification are the core type system elements: Schema, Types, Scalars, Objects, Interfaces, Unions, Enums, Input Objects, List, and Directives. After each of those the wrap up for section 3 of the specification will include Non-Null, Type System Extensions, and Descriptions.

Subsection 3.3 covers ***Schema***. A GraphQL’s type system capabilities are defined and outlined in a service schema. This section is broken out to 3.3.1 Root Operation Types and 3.3.2 Schema Extension.

The ***Root Operation Type*** identifies a query, mutation, and subscription. The **query** root operation type must be provided and be of object type. The **mutation** root oepration type is optional and if not provided, does not support a mutation. If it is provided it also is an object type. The **subscription** root type is also optional similar to a mutations, and if provided must be an object type too.

For example with a type defined query like this

```
type Query {
  yourExcellentField: String
}
```

can be queried like this

```
query {
	yourExcellentField
}
```

or a mutation like this.

```
mutation {
	getAnExcellentField() {
		yourExcellentField
	}
}
```

Additionally when developing a GraphQL doc a schema must be declared. An example would look something like this.

```
schema {
	query: thisMyRootTypeQuery
	mutation: thisMyRootTypeMutation
	mutation: anotherRootTypeMutation
}

type thisMyRootTypeQuery {
	coolField: String
	aRadField: Int
}

type thisMyRootTypeMutation {
	thisField(thatField: String): String
}

type anotherRootTypeMutation {
	anotherField(andThisField: Int): String
}
```

***Schema Extensions*** represent a scehma extended from the original schema. This schema would add additional operational types and directives to the existing original schema.

Validation follows:

- The Schema must already be defined.
- Any non-repeatable directives provided must not already apply to the original Schema.

***Types*** are defined in 3.4 and are the basic core unit in any GraphQL Schema. These are broken into 3.4.1 Wrapping Types, 3.4.2 Input and Output Types, and 3.4.3 Type Extensions.

The core of GraphQL schema exist of types, six named and two wrapping types. The basic type is a Scalar, representing a primitive value like a string or integer. Object types define a set of fields, each being a type in the system or arbitrary type heirarchy. Interface types defines a list of fields where the object implementing the interface must meet the contract of those types being available (Harkens from Object Oriented Programming). A Union definse a list of possible types, where one of the types must be returned, similarly to an interface but with the variable nature of which will be returned. Finally there is the Input Object Type, which allows for the definition of exactly what data is expected for input.

The wrapping types (3.4.1 in the spec) are types used to describe both the values accepted as input and values output by fields. Some types can be used as either input or output, like scalars, and others have obvious input or output only use like the Input Object Type.

Type Extensions (3.4.3) represent a GraphQL type which has been extended from an original type.

Scalars represent primitive leaf values in the GraphQL type system in the form of a hierarchical tree; the leaves are typically scalar, but can also be enum or null values. There are a number of built in scalar types:

- Int – A 32 bit numeric non-fractional value.
- Float – A double-precision finite value as specified in [IEEE 754](https://en.wikipedia.org/wiki/IEEE_754).
- String – Text data, represented as a sequence fo Unicode code points.
- Boolean – This scalar type represents *true* or *false*. Response formats should use a built-in boolean type if supported, otherwise they should use integers 1 and 0.
- ID – The ID scalar type represents a unique identifier. GraphQL is agnostic to ID format, and serializes to string to ensure consistency across formats ID could represent from auto-increment number to large 128-bit random numbers, base64 encoded values, or a [UUID/GUID](/2021/04/14/quick-answers-what-is-the-uuid/).

Custom scalars may be used, for example a UUID scalar could be used. Another useful scalar would be something like URL. Both could be serialized as a string but still gauranteed to meet both of the particular types. When defining custom scalars a scalar specification URL is set with @specifiedBy directive or the specifiedByURL introspection field. The URL must link to a human readable spec of data format, serialization, and coercion rules for the scalar. For example the UUID or URL scalar types.

```
scalar UUID @specifiedBy(url: "https://tools.ietf.org/html/rfc4122")
scalar URL @specifiedBy(url: "https://tools.ietf.org/html/rfc3986")
```

The custom scalars should also include a summary and examples in their description.

Objects, described in section 3.6, are hierarchical and composed, describing a tree of information. Scalar types define the leafs, Objects describe the intermedia levels of heirarchical operations. For example, and object:

```
type Creature {
  name: String
  age: Int
}
```

A query of that object type would look like this.

```
{
  name
  age
}
```

With the results returned.

```
{
  "name": "Frankie the Creature from the Lagoon",
  "age": 6039
},
{
  "name": "Earl the Pearl",
  "age": 90912
}
```

A query with just a subset asking for just the names.

```
{
  "name": "Frankie the Creature from the Lagoon"
},
{
  "name": "Earl the Pearl"
}
```

A field can also relate to another object, even back to itself, as shown in this example. In addition there is an added relationship to the CreatureImage type that is defined as such.

```
type Creature {
  name: String
  age: Int
  parent: Creature
  picture: CreatureImage
}

type CreatureImage {
  name: String
  path: String!
  size: Int
}
```

For the related objects, when querying, the nested object but have the fields to return designated. For example.

```
{
  name
  parent {
    name
  }
  picture {
    name
  }
}
```

When fields are requested during queries they are result mapped conceptually in order the same in which execution occurs. Excluding fragments for which the type doesn’t apply and fields or framents skipped with `@skip` or `@include` directives. A direct example would be that if two fields, let’s say `field1` and `field2` are queried, the resulting JSON should return `{"field1":<value>, "field2":<value>}`.

Other features of objects are defined in ***Field Arguments*** 3.6.1 and ***Field Deprecation*** 3.6.2. With Field arguments a field can have an argument, optionally specified, added such as

```
type Railcar {
  name: String
  picture(size: Int): Url
  load(weight: Int): String
}
```

Field deprecation can be designated to show that a field is or should be no longer used.

```
type Railcar {
  name: String
  unsprungWeight: Int @deprecated
}
```

Finally, ***Object Extensions*** 3.6.3 define a way to represent a type which has already been declared. For example if there is a type declared called Book.

```
type Book {
  id ID!
  title String!
}
```

Then the schema is extended by another API or service, can extend the Book type like this.

```
extend type Book {
  pageCount Int
  description String
  printDate Date
}
```

The extension can also involve interfaces or directives, and might even exclude any additional fields and only interfaces or directives. For example something like `extend type Book @someImportantDirective`.

In section 3.7 the specification delves into ***Interfaces***. Interfaces represet a list of named fields and respective arguments. Fields on an Interface have the same rules as fields on an object type, and are used to setup a contract in which an object type will meet. Object types can also have multiple interfaces.

```
interface BookBase {
  title: String
  published: Date
}

interface BookCategorization {
  name: String
}

type Book implements BookBase & BookCategorization {
  id: ID!
  title: String
  published: Date
  name: String
}
```

This particular Book type could be similarly declared where the category is declared as the Interface `BookCategorization`.

```
type Book implements BookBase {
  id: ID!
  title: String
  published: Date
  category: BookCategorization
}
```

This would then have queries that, respectively, would look like this. The first example could even be confusing since `name` doesn’t specifically, without looking at the data itself, pinpoint that it is of category in this query.

```
{
  id
  title
  published
  name
}
```

This second query however, shows clearly that `name`, since it is part of the field type `BookCategorzation` with a field of its own called `name`, it is clearly seen at the name of the category.

```
{
  id
  title
  published
  category {
    name
  }
}
```

Interfaces can also implement interfaces.

```
interface BookBase implements BookCategorization {
  ... etc etc ...
}
```

Several other important details about interfaces in GraphQL include:

- Interfaces must also not contain cyclic references or implement themselves.
- Like Object Types, interfaces can also be extended.

***Unions*** are defined in section 3.8. GraphQL Unions are an object that can vary between what a list of Object types. It provides for no guaranteed fields between the types. An example would be two types, a Plane type and an Automobile type, brought together as a Union as the VehicleResult, like this.

```
union VehicleResult = Plane | Automobile

type Plane {
  id ID!
  type String
  range Int
  passengerCount Int
  wingFormat String
  fuelWeight Int
}

type Automobile {
  id ID!
  type String
  range Int
  wheelCount Int
  fuelCarried Int
}
```

***Enums*** described in 3.9 and ***Enum Extensions*** in 3.9.1 are fairly straight forward. An example of an enum would look like this.

```
enum Direction {
  INBOUND
  OUTBOUND
}
```

An enum extension would look like this.

```
extend enum Direction {
  STATIONARY
  DEPLOYED
  INCIDENT
}
```

Input Objects are one of the fascinating parts of GraphQL, in that they’re in many ways like types objects, but specifically for input. For example, an input object for entering a train schedule. Here I’ve setup the input object to use several type objects defined below.

```
type TimePoint {
  id ID!
  hour Int!
  minute Int!
  order Int!
  dwell Int
  details String
}

type Station {
  id ID!
  station String
  address String
  state String
  phone String
}

input TrainSchedule {
  arrival: TimePoint
  departure: TimePoint
  station: Station
}
```

An odd characteristic of input objects is that circular references are allowed in an input object. The following examples are directly from the specification. This first one is circularly-referenced as the self and value field can respectively be omitted and/or null.

```
input Example {
  self: Example
  value: String
}
```

This example follows where self may be an empty list. Where it’s a little confusing to me honestly, when you have bangs for required but I suppose the double bang is a negation of sorts… I’ve yet to ascertain how that works in the spec at this point.

```
input Example {
  self: [Example!]!
  value: String
}
```

Input objects can also, similarly to type objects and such, like `extend input` and add fields following the rules as per input objects.

A GraphQL ***List***, per 3.11, is a collection type declaring the type of each item. The values are serialized as ordered lists, where items are serialized per item type.

```
type Query {
 train(id: ID!): Train
 trains(direction: Direction): [Train!]!
}

type Train {
  id ID!
  name String!
  direction Direction!
  details String
}

enum Direction {
  INBOUND
  OUTBOUND
}
```

Directives, as described in section 3.13, are a rather advanced custom feature of GraphQL. They extend the capability of GraphQL in a significant way. They are used to annotate parts of the GraphQL document to note that the annoted part is to be validated and executed in a different way by a client tool or code generator. As you can imagine, basically opening up the whole compute space to what processing could be done!

There are several built in directives, that any GraphQL implementation should support: `@skip` and `@include`. If the type system definition language is supported by the GraphQL implementation than the implemenation must support `@deprecated` and should support the `@specifiedBy` directive. Beyond this directives can be up to the creator.

An example might look like this.

```
directive @doCoolThings on FIELD

fragment SomeCoolThing on TheCoolType {
  field @doCoolThings
}
```

But alas, a full blog post on the range and scope of examples around directives will be due, with that hopefully these *quick notes* on section 3 of the GraphQL specification where useful. At least, if anything, a few minutes faster than reading the actual specification since I’ve done that for you dear reader! Cheers. 🤙🏻
