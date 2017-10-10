---
layout: content-2-panel
title: Creating a Basic Shared Web Source
categories: migrated
---

# Creating a Basic Shared Web Source

A Web [source](Glossary_37585054.html#Glossary-Source) typically crawls the content of a single website, starting from the specified URL (or URLs), and then recursively following any hyperlink it finds in pages to discover the entire site (see Add/Edit Web Source - Panel). By default, a Web source schedule is set to rescan the website at midnight everyday.

You can use the [Create a source from simple configuration](https://platform.cloud.coveo.com/docs?api=Source#!/Sources/rest_organizations_paramId_sources_post) operation to create a basic shared Web source in a [Coveo Cloud V2 organization](Glossary_37585054.html#Glossary-CoveoCloudV2Organization):

```
POST https://platform.cloud.coveo.com/rest/organization/{organizationId}/sources
 
Content-Type: application/json
Accept: application/json
Authorization: Bearer MyAccessToken
 
{
  "sourceType": "WEB2",
  "name": "My web source",
  "sourceVisibility": "SHARED",
  "urls": [
    "http://www.example.com/"
  ]
}
```

Note:

> This introductory topic explains how create a Web source, which is why the `sourceType` value in the request body is `WEB2`. The [Coveo Cloud V2 platform](Glossary_37585054.html#Glossary-CoveoCloudV2Platform) also allows you to create many other types of sources (see [Possible sourceType Values](Possible_sourceType_Values)).

Ensure that:

-   You replace `{organizationId}` in the path by the actual ID of the target Coveo Cloud V2 organization (see [Getting the organizationId](Getting_the_organizationId)).
-   You replace `MyAccessToken` in the `Authorization` header by an access token that grants the privilege to edit sources in the target organization (see [Creating an API key](Creating_an_API_Key), [Getting the Privileges of an Access Token](Getting_the_Privileges_of_an_Access_Token), and [Getting Your Coveo Cloud V2 Platform Access Token](Getting_Your_Coveo_Cloud_V2_Platform_Access_Token)).
-   You specify an appropriate `name` for your source in the request body.

    Note:

    > You cannot change the name of a source once it has been created, so make sure the name you choose fits the content you intend to index with that source.

-   In the `urls` list, you specify one or more URLs from which to start crawling the pages to index with your source.

    Best Practice:

    > You should normally only index one website per web source.

The body of a successful response contains information about the source you just created. The `id` property value is important, as it is a required parameter in many Coveo Cloud V2 platform REST API operations. You can always retrieve this ID later (see [Getting the sourceId](Getting_the_sourceId)).

**Example:**

**201 Created**

```
{
  "sourceType": "WEB2",
  "id": "mycoveocloudv2organization-xtyq5ljb65btzsx2miknabccru",
  "name": "My web source",
  "owner": "asmith@example.com",
  "sourceVisibility": "SHARED",
  "information": {
    ...
  },
  ...
}
```


