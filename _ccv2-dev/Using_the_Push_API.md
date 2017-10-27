---
slug: "124"
layout: content-2-panel
title: Using the Push API
categories: migrated
---

# Using the Push API

In a Coveo Cloud V2 organization, sources of a given type are typically populated by their associated Coveo Cloud crawler designed to pull content from a specific system type. 

When the [Coveo Cloud V2 Administration Console](https://platform.cloud.coveo.com/admin/#/content/sources/new) does not include a source type for a given cloud or on-premises system, developers can use the Push API to push the content from the system into a Coveo Cloud V2 organization source.

When the content of your system is secured, meaning that system items are accessible only by specific authenticated users or groups members, you can also use the Push API to push permissions associated with each item. In this case, you must also create an identity provider associated with your source to which you must push identities, groups and their members, as well as identity mappings (see [Creating an Identity Provider for a Secured Push Type Source](Creating_an_Identity_Provider_for_a_Secured_Push_Type_Source)). 

**To use the Push API**

1.  Ensure your Coveo Cloud V2 environment allows you to use the Push API:
    1.  Ensure your Coveo Cloud V2 organization license includes **Push** sources. 
        In the administration console [Settings](https://platform.cloud.coveo.com/admin/#/organization/settings) page, ensure that the **Push** source type is enabled. 
        If it is not the case, contact your Coveo Sales representative to get the Push source type included in your Coveo Cloud organization license. 
    2.  Get an API key.
        In the Coveo Cloud V2 administration console API Keys page, create an API key for which you select Edit for the Sources privilege (see API Keys - Page). 

2.  Create a push type source (see [Creating a Push Type Source](Creating_a_Push_Type_Source)). 
3.  When your content is secured, create an identity provider for your source (see Creating an Identity Provider for a Secured Push Type Source). 
4.  Write code that uses the Push API to add, update, or delete items to the push type source individually or in batch (see Pushing Items to a Source and Batch Pushing Encrypted Files and Permissions to a Source).
    When your process populates the source for the first time or updates it, your code typical main steps are: 
    1.  Push to the source the new, modified, or staled (to be removed from the source) items, and if applicable, the associated permissions.
    2.  When your content is secured, push new, modified, staled identities (users, groups, mappings) to your identity provider.

5.  Optionally create custom index fields. 
    When you push metadata for which no existing index field is a good match to be mapped, create appropriate custom fields using the Coveo Cloud V2 administration console Fields page (see Fields - Page). 
6.  Optionally map metadata to index fields.
    A metadata that has the same name (case sensitive) as a source field is automatically mapped. 
    When a metadata name does not match the name of the standard or custom field to which it must be mapped. 
    You can add a mapping to your source using the Coveo Cloud V2 administration console **Mapping** tab of a source (see [Add/Edit a Mapping to/of \[SourceName\] - Panel](http://www.coveo.com/go?dest=ccv2ac&context=47)). 

