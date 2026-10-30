---
title: WE DID IT! DataStax Astra is GA
date: 2020-05-13 15:19:51 -0700
last_modified_at: 2020-05-13 22:51:09 -0700
permalink: /2020/05/13/we-did-it-datastax-astra-is-ga/
slug: we-did-it-datastax-astra-is-ga
wp_id: 16892
original_url: https://compositecode.blog/2020/05/13/we-did-it-datastax-astra-is-ga/
categories:
- .NET Bits
- cassandra
- golang
- Java
- Javascript
tags:
- api
- astra
- database as a service
- datastax
- datastax astra
- dbaas
- graphql
- graphql api
- rest api
- services
excerpt: Yesterday we finally went full GA (Generally Available) with DataStax Astra. For the quick TLDR think of it as Apache Cassandra that you can spin up as a service and use in about a minute. I, as I wrote about some months ago, joined the engineering team to help build out the system! I quickly got to reconnoitering the role and working toward build out of features, which now are available to you!
image: /wp-content/uploads/2020/05/earth.jpg
---

Yesterday we finally went full GA (General Availability) with [DataStax Astra](https://www.datastax.com/products/datastax-astra). For the quick TLDR think of it as Apache Cassandra that you can spin up as a service and use in about a minute. I, as I wrote about some months ago, [joined the engineering team](/2019/12/20/career-update-back-to-engineering/) to help build out the system! I quickly got to [reconnoitering the role](/2019/12/30/how-to-reconnoiter-a-new-role/) and working toward build out of features, which now are available to you!

With Astra, if you’ve used Apache Cassandra or DataStax Enterprise you can use the same drivers or CQL you’re familiar with. But with Astra there are two additional capabilities we’ve just released to use in connecting to and working with your databases:

- Astra REST API
- Astra GraphQL API

With the REST API there are a number of capabilities to add a table, return a list of all the tables, return content of a table, and delete a table. In addition to tables, there is functionality to retrieve, retrieve all, add, update, and delete columns. All of the standard [CRUD (Create, Read, Update, and Delete)](https://en.wikipedia.org/wiki/Create,_read,_update_and_delete) commands can also be performed.

For the GraphQL API it gives you the ability to perform CRUD actions and query with filters using the GraphQL syntax.

## Authorization Token

To use either of these services, the first thing you’ll need is to create one of Astra’s time based authorization tokens. These tokens work until 30 minutes after the last call made with the token. Once expired a new token must be created. To create a token an HTTP POST to the API can be made, passing several header values, and username and password in the body of a POST request.

For an example of retrieving an authorization token I’ve put together a cURL request below. To get the URL for your database navigate to the Astra dashboard, and on the summary screen of any database the API Access URL’s are listed.

```
curl --request POST \
  --url https://12c3bb24-e2df-4db3-b993-14707303e57c-us-east1.apps.astra.datastax.com/api/rest/v1/auth \
  --header 'accept: */*' \
  --header 'content-type: application/json' \
  --header 'x-cassandra-request-id: 24cc6f6f-c1d9-4d4e-a4d3-e34c7d8b148a' \
  --data '{"username":"betterbot","password":"betterbot"}'
```

A successful request will return a result with the auth token that looks like this.

```
{"authToken":"9a38437f-7e03-49a8-bc5d-b4e305d7c1e8"}
```

With that authorization token we can now call actions against the REST, or GraphQL APIs.

## Creating a Table via the Astra REST API

To create a table, we need a few key elements: The table name, whether it should create if a table exists or not, and column definitions with at least one column as a primary key. This is done by using JSON to pass this schema to the REST API. Here’s an example of some JSON that can be used to create a table.

```
'{"name":"products","ifNotExists":true,"columnDefinitions":
  [ {"name":"id","typeDefinition":"uuid","static":false},
    {"name":"name","typeDefinition":"text","static":false},
    {"name":"description","typeDefinition":"text","static":false},
    {"name":"price","typeDefinition":"decimal","static":false},
    {"name":"created","typeDefinition":"timestamp","static":false}],"primaryKey":
    {"partitionKey":["id"]},"tableOptions":{"defaultTimeToLive":0}}'
```

To use this JSON to create a table, just add the pertinent headers, insert your keyspace into the URL, and the `x-cassandra-token` and POST this data to the REST API end point. A cURL request to create the table would look like this.

```
curl --request POST \
  --url https://12c3bb24-e2df-4db3-b993-14707303e57c-us-east1.apps.astra.datastax.com/api/rest/v1/keyspaces/betterbotz/tables \
  --header 'accept: */*' \
  --header 'content-type: application/json' \
  --header 'x-cassandra-request-id: 07e37064-b265-4618-94ce-1c4606f584f9' \
  --header 'x-cassandra-token: ' \
  --data '{"name":"products","ifNotExists":true,"columnDefinitions":
  [ {"name":"id","typeDefinition":"uuid","static":false},
    {"name":"name","typeDefinition":"text","static":false},
    {"name":"description","typeDefinition":"text","static":false},
    {"name":"price","typeDefinition":"decimal","static":false},
    {"name":"created","typeDefinition":"timestamp","static":false}],"primaryKey":
    {"partitionKey":["id"]},"tableOptions":{"defaultTimeToLive":0}}'
```

## Adding data via a GraphQL Mutation

At this point, with a data created, we can add, update, or delete data. The sample curl statement I’ve put together here is a sample GraphQL mutation to add a record to the `products` table.

```
curl --request POST \
  --url https://ba965c97-86f1-4d38-8cne-58qa1d2209a1-us-east1.apps.astra.datastax.com/api/rest/v1/keyspaces/betterbotz/tables/orders/rows \
  --header 'accept: application/json' \
  --header 'content-type: application/json' \
  --header 'x-cassandra-request-id: xyzaa27b-de8e-4afc-8431-8f06a326047d' \
  --header 'x-cassandra-token: 3ad1ca6a-62pq-4e1b-b273-4c08ea334909' \
  --data-raw '{"query":"mutation {superarms: insertProducts(value:{id:\"65cad0df-4fc8-42df-90e5-4effcd221ef7\"\n name:\"Arm Spec A1\" description:\"Powerful Robot Arm Spec A.\"price: \"9999.99\" created: \"2012-04-23T18:25:43.511Z\"}){value {name description price created}}}","variables":{}}'
```

For some other examples issuing a GraphQL mutation to add a record, just for good measure.

### Go

```go
package main

import (
  "fmt"
  "strings"
  "net/http"
  "io/ioutil"
)

func main() {

  url := "https://32c3bb24-e2df-4db3-b993-14707303e57c-us-east1.apps.astra.datastax.com/api/graphql"
  method := "POST"

  payload := strings.NewReader("{\"query\":\"mutation {superarms: updateProducts(value: {id:\\\"65cad0df-4fc8-42df-90e5-4effcd221ef7\\\" name:\\\"Arm Spec A3 [Newly Updated]\\\" description:\\\"Powerful Robot Arm Spec A3.\\\" price: \\\"19999.99\\\" created: \\\"2012-04-23T18:25:43.511Z\\\" }){value {id name description price created}}}\",\"variables\":{}}")

  client := &http.Client {
  }
  req, err := http.NewRequest(method, url, payload)

  if err != nil {
    fmt.Println(err)
  }
  req.Header.Add("accept", "*/*")
  req.Header.Add("content-type", "application/json")
  req.Header.Add("X-Cassandra-Token", "e85b3021-fb89-4f43-9ba6-a64a49ba5f68")
  req.Header.Add("Content-Type", "application/json")

  res, err := client.Do(req)
  defer res.Body.Close()
  body, err := ioutil.ReadAll(res.Body)

  fmt.Println(string(body))
}
```

### Python

```python
import requests

url = "https://32c3bb24-e2df-4db3-b993-14707303e57c-us-east1.apps.astra.datastax.com/api/graphql"

payload = "{\"query\":\"mutation {superarms: updateProducts(value: {id:\\\"65cad0df-4fc8-42df-90e5-4effcd221ef7\\\" name:\\\"Arm Spec A3 [Newly Updated]\\\" description:\\\"Powerful Robot Arm Spec A3.\\\" price: \\\"19999.99\\\" created: \\\"2012-04-23T18:25:43.511Z\\\" }){value {id name description price created}}}\",\"variables\":{}}"
headers = {
  'accept': '*/*',
  'content-type': 'application/json',
  'X-Cassandra-Token': 'e85b3021-fb89-4f43-9ba6-a64a49ba5f68',
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data = payload)

print(response.text.encode('utf8'))
```

### Java

```java
OkHttpClient client = new OkHttpClient().newBuilder()
  .build();
MediaType mediaType = MediaType.parse("application/json");
RequestBody body = RequestBody.create(mediaType, "{\"query\":\"mutation {superarms: updateProducts(value: {id:\\\"65cad0df-4fc8-42df-90e5-4effcd221ef7\\\" name:\\\"Arm Spec A3 [Newly Updated]\\\" description:\\\"Powerful Robot Arm Spec A3.\\\" price: \\\"19999.99\\\" created: \\\"2012-04-23T18:25:43.511Z\\\" }){value {id name description price created}}}\",\"variables\":{}}");
Request request = new Request.Builder()
  .url("https://32c3bb24-e2df-4db3-b993-14707303e57c-us-east1.apps.astra.datastax.com/api/graphql")
  .method("POST", body)
  .addHeader("accept", "*/*")
  .addHeader("content-type", "application/json")
  .addHeader("X-Cassandra-Token", "e85b3021-fb89-4f43-9ba6-a64a49ba5f68")
  .addHeader("Content-Type", "application/json")
  .build();
Response response = client.newCall(request).execute();
```

### and C#!

```csharp
var client = new RestClient("https://32c3bb24-e2df-4db3-b993-14707303e57c-us-east1.apps.astra.datastax.com/api/graphql");
client.Timeout = -1;
var request = new RestRequest(Method.POST);
request.AddHeader("accept", "*/*");
request.AddHeader("content-type", "application/json");
request.AddHeader("X-Cassandra-Token", "e85b3021-fb89-4f43-9ba6-a64a49ba5f68");
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\"query\":\"mutation {superarms: updateProducts(value: {id:\\\"65cad0df-4fc8-42df-90e5-4effcd221ef7\\\" name:\\\"Arm Spec A3 [Newly Updated]\\\" description:\\\"Powerful Robot Arm Spec A3.\\\" price: \\\"19999.99\\\" created: \\\"2012-04-23T18:25:43.511Z\\\" }){value {id name description price created}}}\",\"variables\":{}}",
           ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
Console.WriteLine(response.Content);
```

With that short tour, check out your free database today @ <https://astra.datastax.com/register>! Feel free to ping me on Twitter [@Adron](https://twitter.com/Adron) or here in comments, I’m open to and would love to discuss your experience!
