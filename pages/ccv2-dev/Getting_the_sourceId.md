---
layout: content-2-panel
title: Getting the sourceId
categories: migrated
---

# Getting the sourceId

The `sourceId`  is the unique identifier of a Coveo Cloud V2 [source](Glossary_37585054.html#Glossary-Source). `sourceId` values are typically in the following format: `organizationId-GUID`.

**Example:**

If your organization ID is `myorganization` and the source GUID is `w6nds7q6ry6qanihwgy56ssexa`, then the `sourceId` value is:

`myorganization-w6nds7q6ry6qanihwgy56ssexa`

Many [Coveo Cloud V2 platform](Glossary_37585054.html#Glossary-CoveoCloudV2Platform) REST API methods require that you provide a value for the `sourceId` parameter.

You can use the [Get all sources](https://platform.cloud.coveo.com/docs?api=Source#!/Sources/rest_organizations_paramId_sources_get) call to find the `sourceId` of any source in a specific [Coveo Cloud V2 organization](Glossary_37585054.html#Glossary-CoveoCloudV2Organization): 

```
GET https://platform.cloud.coveo.com/rest/organizations/{organizationId}/sources
Accept: application/json
Authorization: Bearer MyAccessToken
```

Ensure that:

-   You replace `{organizationId}` in the path by the actual ID of the target Coveo Cloud V2 organization (see [Getting the organizationId](Getting_the_organizationId)).
-   You replace `MyAccessToken` in the `Authorization` header by an access token that grants the **Sources - View** privilege in the target organization (see [Creating an API Key](Creating_an_API_Key), [Getting the Privileges of an Access Token](Getting_the_Privileges_of_an_Access_Token), and [Getting Your Coveo Cloud V2 Platform Access Token](Getting_Your_Coveo_Cloud_V2_Platform_Access_Token)).

The body of a successful response contains information about each source in the Coveo Cloud V2 organization that corresponds to the `organizationId` you provide as a path argument.

To find the `sourceId`:

1.  In the response body, look for the source whose `sourceId` you want to retrieve.
2.  Get the `id` property value, which is the `sourceId` of that source. 

    **Example:**

    **200 OK**

    ```
    [
      {
        "sourceType": "PUSH",
        "id": "mycoveocloudv2organization-w6nds7q6ry6qanihwgy56ssexa", // This is the `sourceId` of the `MyCoveoCloudV2PushSource` source.
        "name": "MyCoveoCloudV2PushSource",
        "owner": "asmith@example.com",
        "sourceVisibility": "SHARED",
        [ ... ]
      },
      [ ... ]
    ]
    ```

Note:

> `id` and `name` are the only properties whose value cannot change after a source is created, so you can safely use a source `name` to search for its `id`.


