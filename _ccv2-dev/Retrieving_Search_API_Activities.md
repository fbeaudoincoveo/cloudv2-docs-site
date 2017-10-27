---
slug: "108"
layout: content-2-panel
title: Retrieving Search API Activities
categories: migrated
---

# Retrieving Search API Activities

The Search API automatically logs [activities](Glossary_37585054.html#Glossary-Activity) in your [Coveo Cloud V2 organization](Glossary_37585054.html#Glossary-CoveoCloudV2Organization). For instance, when you create, update, or delete any [query pipeline statement](Glossary_37585054.html#Glossary-QueryPipelineStatement) or hosted search page, the service logs a corresponding activity.

You can use the [Get public activities related to an organization](https://platform.cloud.coveo.com/docs?api=Activity#!/Activities/rest_organizations_paramId_activities_public_post) operation to retrieve Search API related activities in a specific Coveo Cloud V2 organization:

```
POST https://platform.cloud.cove.com/rest/organizations/{organizationId}/activities/public
Content-Type: application/json
Accept: application/json
Authorization: Bearer MyAccessToken
 
{
  "sections": [
    "SEARCH"
  ]
}
```

Ensure that:

-   You replace `{organizationId}` in the path by the actual ID of the target Coveo Cloud V2 organization (see [Getting the organizationId](https://developers.coveo.com/display/CloudPlatform/Getting+the+organizationId)).
-   You replace `MyAccessToken` in the `Authorization` header by an access token that grants you the the **Activities - View** privilege in the target organization (see [Creating an API Key](Creating_an_API_Key) and [Getting the Privileges of an Access Token](Getting_the_Privileges_of_an_Access_Token)).

The body of a successful response contains information about Search API activities retrieved in the target organization.

Note:

> By default, this operation returns the most recent activities, up to a maximum of 100 entries.

> If you want, you can:

-   Retrieve more (or less) entries, using the `perPage` query parameter (e.g., specifying `perPage=500` would retrieve up to 500 entries per "page")
-   Retrieve a specific "page" of activities, using the `page` query parameter (e.g., specifying `page=2` would retrieve the second "page" of entries)
-   Only retrieve activities created in a specific date range, using the `from` and `to` query parameters (e.g., specifying `from=2017-08-28T00:00:00.000Z&to=2017-08-29T00:00:00.000Z` would retrieve activities logged between the 28th and 29th of August, 2017).

**Example:**

**200 OK**

```
{
  "items": [
    {
      "id": "89a40c4dbc7c45089844ae4c41e4652d",
      "operation": "CREATE",
      "state": "EXECUTED",
      "result": "SUCCESS",
      "content": {
        ...
      },
      "createDate": 1504016444278,
      ...
      "triggeredBy": {
      },
      "organizationId": "mycoveocloudv2organization",
      "resourceId": "bd153778-3e51-4a8f-bec2-03cf4708d656",
      "resourceName": "My Hosted Search Page",
      "resourceType": "SEARCH_PAGE",
      "section": "SEARCH"
    },
    ...
  ],
  "totalPages: 4,
  "totalEntries": 350 
}
```


