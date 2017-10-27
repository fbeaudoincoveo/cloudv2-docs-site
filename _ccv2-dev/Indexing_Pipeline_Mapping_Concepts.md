---
slug: "83"
layout: content-2-panel
title: Indexing Pipeline Mapping Concepts
categories: migrated
---

# Indexing Pipeline Mapping Concepts

**In this topic:**

-   [Metadata Origin](#metadata-origin)
-   [Item Types](#item-types)
-   [Mapping Rules](#mapping-rules)
    -   [Mapping Rules Application Order](#mapping-rules-application-order)
    -   [Mapping Rule Syntax Examples](#mapping-rule-syntax-examples)

This topic defines the concepts that will help you better understand how the indexing pipeline mapping feature works.

## Metadata Origin

Metadata origin feature is used when mapping a metadata to a field (see [Add/Edit Mappings](http://www.coveo.com/go?dest=cloudhelp&lcid=9&context=285)) or when applying python extension scripts (see [Applying an Extension to a Source](http://www.coveo.com/go?dest=cloudhelp&lcid=9&context=335)). Since a metadata value can change at each stage during the indexing pipeline process, the metadata origin feature is used to access metadata value at a specified indexing stage. By default, retrieving a metadata value without declaring a specific origin returns a metadata value after the whole indexing pipeline process (see [Coveo Cloud V2 Indexing Pipeline](http://www.coveo.com/go?dest=cloudhelp&lcid=9&context=336)). The possible origin values are `crawler`, `converter`, and `mapping`. 

| Meta origin | Code example       | Returns the `author` metadata value as it comes out of ...                      |
|-------------|--------------------|---------------------------------------------------------------------------------|
| crawler     | `author:crawler`   | ... the crawler/scraper module, and before the pre-conversion extension applies |
| converter   | `author:converter` | ... the pre-conversion scripts, and before the mappings applies                 |
| mapping     | `author:mapping`   | ... the mapping process, and before the post-conversion extension applies       |
| default     | `author`           | ... the post-conversion extension                                               |

The following table shows how metadata origin can be used to access different values:

| Stage     | Value Before Modification | Modification                                                          | Value After Modification | Metadata Origin Used to Access the Value    |
|-----------|---------------------------|-----------------------------------------------------------------------|--------------------------|---------------------------------------------|
| crawler   |                           | A crawler retrieves the original author value                         | John Smith               | [author:crawler](http://authorcrawler/)     |
| converter | John Smith                | A pre-conversion script only keeps the first letter of the first name | J. Smith                 | [author:converter](http://authorconverter/) |
| mapping   | J. Smith                  | A mapping process uses literal string "Coveo" to change author value  | Coveo                    | [author:mapping](http://authormapping/)     |
| default   | Coveo                     | A post-conversion script returns uppercase string                     | COVEO                    | author                                      |

> If you do not have multiple origins to differentiate, or if you would like to use the last value added by the pipeline for your metadata, the origin can be omitted.

## Item Types

Coveo Cloud V2 organization sources typically come with built-in item types used to divide items into logical subsets, such as `Video`, `Account`, `User` etc.

**Example:**

In the context of YouTube, videos might be associated to the `Video` or `Playlist` types.

You can also create custom item types using the Source API Mappings resource (see [Source API Mappings Resource Usage Overview](https://developers.coveo.com/x/awwvAg)).

> Push (and Coveo for Sitecore sources because they use the Push API to index items) do not have out-of-the-box item types.

## Mapping Rules

Mapping rules essentially tell the indexing pipeline mapping stage the value of the system item metadata content or specific value(s) to be used to populate a given field for each source item (see Mapping Rules Syntax Reference).

There are two mapping rule types:

-   Common rules are applied to every item of a source.
-   Specific rules are only applied to specific items (see [Item Types](Indexing_Pipeline_Mapping_Concepts)).

Currently, you do not need to add a mapping rule for an item metadata with a name exactly matching (case sensitive) your index field name. They are automatically mapped.

### Mapping Rules Application Order

It is a good practice to have multiple explicitly ordered rules instead of multiple rules for the same field (see [Mapping Rules Hierarchy](http://www.coveo.com/go?dest=cloudhelp&lcid=9&context=339)).

**Example:**

`%[firstname] %[lastname], %[username], Anonymous, %[department]`

When two mapping rules exist for the same field, they are applied alphabetically in descending order.

### Mapping Rule Syntax Examples

Each Coveo Cloud V2 source JSON configuration has a **Mappings** section listing all the mapping rules to apply to the source items during the indexing pipeline mapping stage (see Differences Between the Source JSON Mappings Configuration and the Response JSON Body Formats).

The following section presents examples of mapping rules using simple and sophisticated syntax.

**Examples:**

This rule maps a single metadata to an index field for every item of a source.

```
  {
    "id": "rule_ID",
    "kind": "COMMON",
    "fieldName": "author",
    "extractionMethod": "METADATA",
    "content": "%[username]"
  }
```

Maps a metadata with a value set during a specific indexing pipeline stage.

```
  {
    "id": "rule_ID",
    "kind": "COMMON",
    "fieldName": "author",
    "extractionMethod": "METADATA",
    "content": "%[username:metadata_origin]"
  }
```

Maps the metadata `user:name` with a value set during a specific indexing pipeline stage.

```
  {
    "id": "rule_ID",
    "kind": "COMMON",
    "fieldName": "author,
    "extractionMethod": "METADATA",
    "content": "%[user:name_with_colon:metadata_origin]"
  }
```

Maps a metadata with any special characters that you want to use.

```
  {
    "id": "rule_ID",
    "kind": "COMMON",
    "fieldName": "author",
    "extractionMethod": "LITERAL",
    "content": "•·.·´¯`·.·•%[username]•·.·´¯`·.·•"
  }
```

Maps the literal string `%[username]`.

```
  {
    "id": "rule_ID",
    "kind": "COMMON",
    "fieldName": "author",
    "extractionMethod": "LITERAL",
    "content": "%[%[username]]"
  }
```

Maps the literal string `username]]]]]`.

```
  {
    "id": "rule_ID",
    "kind": "COMMON",
    "fieldName": "author",
    "extractionMethod": "LITERAL",
    "content": "%[username]]]]]]"
  }
```

Maps the literal string `Anonymous`.

```
  {
    "id": "rule_ID",
    "kind": "COMMON",
    "fieldName": "author",
    "extractionMethod": "LITERAL",
    "content": "Anonymous"
  }
```

Maps the literal string `Mr. %[firstname] %[lastname]`.

```
  {
    "id": "rule_ID",
    "kind": "COMMON",
    "fieldName": "author",
    "extractionMethod": "LITERAL",
    "content": "Mr. %[firstname] %[lastname]"
  }
```

Maps the literal string `%[firstname] %[lastname]`.

```
  {
    "id": "rule_ID",
    "kind": "COMMON",
    "fieldName": "author",
    "extractionMethod": "LITERAL",
    "content": "%[firstname] %[lastname]"
  }
```

Remove a common field mapping for a specific item type.

```
  {
    "id": "rule_ID",
    "kind": "MAPPING",
    "type": "video",
    "fieldName": "author",
    "extractionMethod": "LITERAL",
    "content": " "
  }
```


