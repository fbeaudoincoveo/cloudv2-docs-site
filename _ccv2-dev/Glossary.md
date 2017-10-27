---
slug: "74"
layout: content-2-panel
title: Glossary
categories: migrated
---

# Glossary

**In this topic:**

-   [activity](#activity)
-   [administration console](#administration-console)
-   [advanced query expression](#advanced-query-expression)
-   [aq](#aq)
-   [basic query expression](#basic-query-expression)
-   [constant query expression](#constant-query-expression)
-   [Coveo Cloud query pipeline](#coveo-cloud%C2%A0query-pipeline)
-   [Coveo Cloud query syntax](#coveo-cloud-query-syntax)
-   [Coveo Cloud usage analytics](#coveo-cloud-usage-analytics)
-   [Coveo Cloud V2 administration console](#coveo-cloud-v2-administration-console)
-   [Coveo Cloud V2 indexing pipeline](#coveo-cloud-v2-indexing-pipeline)
-   [Coveo Cloud V2 organization](#coveo-cloud-v2-organization)
-   [Coveo Cloud V2 platform](#coveo-cloud-v2-platform)
-   [Coveo JavaScript Search Framework](#coveo-javascript-search-framework)
-   [Coveo Machine Learning](#coveo-machine-learning)
-   [cq](#cq)
-   [disjunctive query expression](#disjunctive%C2%A0query-expression)
-   [dq](#dq)
-   [feature](#feature)
-   [field](#field)
-   [index](#index)
-   [Indexing Pipeline](#indexing-pipeline)
-   [indexing pipeline extension](#indexing-pipeline-extension)
-   [item](#item)
-   [JavaScript Search](#javascript-search)
-   [JsSearch](#jssearch)
-   [JS UI](#js-ui)
-   [organization](#organization)
-   [pipeline](#pipeline)
-   [q](#q)
-   [QPL](#qpl)
-   [query](#query)
-   [query function](#query-function)
-   [query pipeline](#query-pipeline)
-   [query pipeline feature](#query-pipeline-feature)
-   [query pipeline language](#query-pipeline-language)
-   [query pipeline statement](#query-pipeline-statement)
-   [ranking function](#ranking-function)
-   [Search UI](#search-ui)
-   [source](#source)
-   [statement](#statement)
-   [usage analytics](#usage-analytics)

The Coveo Cloud V2 glossary defines Coveo Cloud related terms, expressions, abbreviations as well as concepts, products, components,  modules, or features.

> The glossary, currently incomplete, is a work in progress.

## activity

An *activity* is an event related to a specific [Coveo Cloud V2 platform](Glossary) concept such as a [source](Glossary), a [field](Glossary), an [indexing pipeline extension](Glossary), etc. (see [Activity - Panel](http://www.coveo.com/go?dest=cloudhelp&lcid=9&context=260)).

## administration console

See [Coveo Cloud V2 administration console](Glossary). 

## advanced query expression

The *advanced query expression* is a part of the larger [query](Glossary) expression (the `aq` value) that is typically hidden to the end-user and  generated by code based on various rules such as facet selections. 

## aq

See [advanced query expression](Glossary).

## basic query expression

The *basic query expression* is the part of the larger [query](Glossary) expression (the `q` value) that typically comes from end user input, such as when a user is typing keywords in a search box.

## constant query expression

The *constant query expression* is a part of the larger [query](Glossary) expression (the `cq` value) similar to the [advanced query expression](Glossary), but that must hold expressions such as a search scope that are constant for all users of a specific search interface or search tab.  The results of evaluating those expressions are kept in a special index cache to avoid re-evaluating them on each query. 

## Coveo Cloud query pipeline

A Coveo Cloud query pipeline is a conditionally applied Search API set of query pipeline features that can be defined to modify a query (see What Is a Query Pipeline?). 

## Coveo Cloud query syntax

The *Coveo Cloud query syntax* is the set of semantic rules that allows a user to compose an advanced [query](Glossary) to send to the Search API (see [Coveo Cloud Query Syntax Reference](http://www.coveo.com/go?dest=cloudhelp&lcid=9&context=357)).

## Coveo Cloud usage analytics

The *Coveo Cloud usage analytics* is a cloud service that records user interactions sent from Coveo search interfaces (and optionally page views from web) content allowing administrators to monitor Coveo solution usage (see [Coveo Cloud Usage Analytics](http://www.coveo.com/go?dest=cloudhelp&lcid=9&context=89)).

The usage analytics data also feeds [Coveo Machine Learning](Glossary) models that are learning user behavior to suggest more relevant content. 

## Coveo Cloud V2 administration console

The *Coveo Cloud V2 administration console* is a web application that allows an administrator to manage a Coveo Cloud V2 organization from a graphical user interface (see Coveo Cloud V2 Administration Console ).

The administration console relies on all of the REST API services exposed by the Coveo Cloud V2 platform. 

## Coveo Cloud V2 indexing pipeline

The *Coveo Cloud V2 Indexing Pipeline* is the process through which each [source](Glossary) [item](Glossary) goes when it is indexed in a [Coveo Cloud V2 organization](Glossary) (see [Coveo Cloud V2 Indexing Pipeline](http://www.coveo.com/go?dest=cloudhelp&lcid=9&context=336)). 

## Coveo Cloud V2 organization

A *Coveo Cloud V2 organization* is a single tenant instance hosting data and [Coveo Cloud V2 platform](Glossary) service configurations allowing a company/corporation/organization to make multiple public and private enterprise content securely searchable with optimized relevance powered by [Coveo Cloud usage analytics](Glossary) and [Coveo Machine Learning](Glossary) (see  [Organization - Section](http://www.coveo.com/go?dest=cloudhelp&lcid=9&context=294)). 

## Coveo Cloud V2 platform

 

The *Coveo Cloud V2 platform* is an enterprise-class native cloud SaaS/PaaS solution that provides a unified and secure way to search for contextually relevant content across multiple enterprise systems (see  [Coveo Cloud V2](http://www.coveo.com/go?dest=cloudhelp&lcid=9&context=231)). The platform relies on [Coveo Cloud usage analytics](Glossary) data to yield machine learning powered recommendations. The platform embraces the concepts of micro-services and scalability, allowing users to expand their search solution as their business grows.

## Coveo JavaScript Search Framework

The *Coveo JavaScript Search Framework* is an open-source set of components (such as a search box, facets, a search result list, sort options) that you can assemble to easily build a feature-rich HTML search page getting results from a Coveo [index](Glossary) (see [JavaScript Search Framework Home](https://developers.coveo.com/display/JsSearchV1/JavaScript+Search+Framework+Home)). 

The Coveo JavaScript search page sends search requests to the Search API to get [query](Glossary) results, and sends events to the Usage Analytics Write API to log [Coveo Cloud usage analytics](Glossary) data. 

## Coveo Machine Learning

*Coveo Machine Learning* is an artificial intelligence (AI) based cloud service hosting machine learning models used to provide more relevant content (see [Coveo Machine Learning](http://www.coveo.com/go?dest=cloudhelp&lcid=9&context=177)).

The models learn from [Coveo Cloud usage analytics](Glossary) data and validate with the Coveo Cloud [index](Glossary) that the querying user has the permission to view each recommended [item](Glossary).

## cq

See [constant query expression](Glossary).

## disjunctive query expression

The *disjunctive query expression* is the part of the larger [query](Glossary) expression (the `dq` value) that is merged with the other expression parts using an `OR` boolean operator. 

## dq

See [disjunctive query expression](Glossary).

## feature

See [query pipeline feature](Glossary).

## field

A *field* is a Coveo Cloud V2 organization data container populated with a metadata value type (string, integer, float, or date/time) to provide specific information about an [item](Glossary) while it passes through the [Coveo Cloud V2 indexing pipeline](Glossary) stages (see [Fields - Page](http://www.coveo.com/go?dest=cloudhelp&lcid=9&context=287)). 

## index

An *index* is a data struture allowing to quickly return [items](Glossary) matching a specific [query](Glossary). 

## Indexing Pipeline

See [Coveo Cloud V2 indexing pipeline](Glossary).

## indexing pipeline extension

An *indexing pipeline extension* is a script defined in your [Coveo Cloud V2 organization](Glossary) that can be applied to one or more [source](Glossary)s to modify how [item](Glossary)s are indexed (see [Coveo Cloud V2 Indexing Pipeline Extensions](Coveo_Cloud_V2_Indexing_Pipeline_Extensions)).  

An administrator can manage indexing pipeline extensions from the [Coveo Cloud V2 administration console](Glossary) (see [Extensions - Page](http://www.coveo.com/go?dest=cloudhelp&lcid=9&context=326)). 

## item

An *item* is a [source](Glossary) [index](Glossary) element (such as a document or an object) originally from an enterprise system that can be returned as a single search result. 

## JavaScript Search

See [Coveo JavaScript Search Framework](Glossary). 

## JsSearch

See [Coveo JavaScript Search Framework](Glossary). 

## JS UI

See [Coveo JavaScript Search Framework](Glossary). 

## organization

See Coveo Cloud V2 organization

## pipeline

See [Coveo Cloud V2 indexing pipeline](Glossary).

See [Coveo Cloud query pipeline](Glossary).

## q

See [basic query expression](Glossary).

## QPL

See [Query Pipeline Language](Glossary).

## query

A *query* is a set of one or more expressions sent to a service such as an [index](Glossary) to return matching relevant [items](Glossary). 

## query function

A *query function *is a mathematical expression evaluated against each [item](Glossary) returned by a [query](Glossary), and whose output is stored in a dynamic, temporary [field](Glossary) generated at query time (see [Query Function](https://developers.coveo.com/display/SearchREST/Query+Function)).

## query pipeline

See [Coveo Cloud query pipeline](Glossary).

## query pipeline feature

A *query pipeline feature* is a [query pipeline statement](Glossary) expressing a meaningful action in the [Coveo Cloud query pipeline](Glossary), such as a [Coveo Machine Learning](Glossary) model, a thesaurus rule, a featured result rule, a ranking weights rule, etc.

## query pipeline language

The *query pipeline language*, also known as QPL (pronounced *qupel*) is a simple language to express the various [query pipeline features](Glossary) supported by the [Coveo Cloud query pipeline](Glossary) (see [Query Pipeline Language (QPL)](https://developers.coveo.com/pages/viewpage.action?pageId=18350826)).

## query pipeline statement

A *query pipeline statement* is an expression constructed using [query pipeline language](Glossary) building blocks such as primitive types, lists, conditions, objects, etc.

## ranking function

A *ranking function* is a mathematical expression evaluated against each [item](Glossary) returned by a [query](Glossary), and whose output is added to the ranking score of the current item (see [Ranking Function](https://developers.coveo.com/display/SearchREST/Ranking+Function)). 

## Search UI

The name of the [Coveo JavaScript Search Framework](Glossary) GitHub repository (see [search-ui](https://github.com/coveo/search-ui)). 

## source

A source is a Coveo Cloud V2 index container holding all items related to a specific enterprise system such as Google Drive, Web, or SharePoint (see [Sources - Page](http://www.coveo.com/go?dest=cloudhelp&lcid=9&context=256)).

## statement

See query pipeline statement.

## usage analytics

See Coveo Cloud usage analytics. 