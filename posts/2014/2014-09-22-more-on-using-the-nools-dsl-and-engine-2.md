---
title: More on Using the Nools DSL and Engine…
date: 2014-09-22 10:02:12 -0700
last_modified_at: 2020-04-13 16:45:48 -0700
permalink: /2014/09/22/more-on-using-the-nools-dsl-and-engine-2/
slug: more-on-using-the-nools-dsl-and-engine-2
wp_id: 10284
original_url: https://compositecode.blog/2014/09/22/more-on-using-the-nools-dsl-and-engine-2/
categories:
- How-to
- Javascript
- Node.js Things
tags:
- business rules
- domain-specific language
- node
- node.js
- nodejs
- rules
- rules processing
excerpt: 'Nools Objects In the helloworld.nools object there is a single object defined called Message. This object has two elements defined; the text property and the constructor. The specific object definition is shown below. define Message { text : ”, constructor : function(message){ this.text = message; } } This object can now be referred …'
image: /wp-content/uploads/2014/01/javascript-logo.png
---

## **Nools Objects**

In the *helloworld.nools* object there is a single object defined called *Message*. This object has two elements defined; the text property and the constructor. The specific object definition is shown below.

```javascript
define Message {
text : ",
constructor : function(message){
this.text = message;
}
}
```

This object can now be referred to by name throughout the nools file. The other way to reference this object is to call the getDefined function from the flow object that is being used in code processing the business rules. In the nools language any javascript has can be put inside the define blog. By defining the constructor as shown, it overrides the default constructor behavior.

**Nools Rules**

In the nools DSL writing a rule consists of the following format.

```javascript
rule <name> {
when {<constraints>}
then {<action>}
}
```

Let’s take a look at some of the example rules from the previous blog entry [Learning “nools” Rules Engine](/2014/09/20/learning-nools-rules-engine/) and break those down. The first example is the *Hello* rule.

```javascript
rule Hello {
when {
m : Message m.text =~ /^hello(\s*world)?$/;
}
then {
modify(m, function(){this.text += " goodbye";});
}
}
```

In this rule when the content starts with the word hello then the rule is set to modify the text of the object to append goodbye. So if I sent a message of ‘hello’ the message would become ‘hello goodbye’. As an example, modify the code in server.js as I’ve done below.

```javascript
var nools = require ('nools');
var ruleFilePath = __dirname + "/rules/helloworld.nools";
var flow = nools.compile (ruleFilePath);
var session = flow.getSession ();

var Message = flow.getDefined ("message");

session.assert (new Message ("hello"));
session.assert (new Message ("hello or goodbye"));
session.assert (new Message ("hello world"));
session.assert (new Message ("goodbye"));

session.match();
```

In the code above I’ve added four new message objects to have the rules process against. In each of these the Hello rules would process these four messages and produce output with a call of the *match()* function. When executing the code to compile and process the nools rules run *node server.js* command. The output then returns the following.

```javascript
$ node server.js
goodbye
hello world goodbye
hello or goodbye
hello goodbye
```

Each of the messages, even though entered in a particular order, returns the process results of the objects in reverse order. In this case the message ‘hello’ becomes ‘hello world’, ‘hello or goodbye’ remains ‘hello or goodbye’, ‘hello world’ becomes ‘hello world goodbye’ and last ‘goodbye’ is left untouched since it doesn’t start with ‘hello’. The other rule *Goodbye*, shown below, is also processed for each match.

```javascript
rule Goodbye {
when {
m : Message m.text =~ /.*goodbye$/;
}
then {
console.log(m.text);
}
}
```

But since the first rule *Hello* processes, rule two actually runs every time (*since post the Hello rule every message ends with goodbye*) and displays the results based on the *Goodbye* rule.

That covers nools objects and rules. Stay tuned and there will be more on the nools from me in the near future. Cheers!
