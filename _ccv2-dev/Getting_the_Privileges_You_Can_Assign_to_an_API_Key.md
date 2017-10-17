---
slug: "70"
layout: content-2-panel
title: Getting the Privileges You Can Assign to an API Key
categories: migrated
---

# Getting the Privileges You Can Assign to an API Key

A Coveo Cloud V2 API key is granted a set of privileges which are only valid within the confines of a specific [Coveo Cloud V2 organization](Glossary_37585054.html#Glossary-CoveoCloudV2Organization) (see [Privileges](http://www.coveo.com/go?dest=cloudhelp&lcid=9&context=300)). 

You can use the [Get all possible privileges for api keys in the selected organization](https://platform.cloud.coveo.com/docs?api=AuthorizationServer#!/Organization32Privileges/rest_organizations_paramId_privileges_apikeys_get) call to retrieve the list of values which are assignable to the `privileges` parameter when you create an API Key (see [Creating an API Key](Creating_an_API_Key)):

```
GET https://platform.cloud.coveo.com/rest/organizations/{organizationId}/privileges/apikeys
Accept: application/json
Authorization: Bearer MyOAuth2Token
```

Ensure that:

-   You replace `{organizationId}` in the path by the actual ID of the target Coveo Cloud V2 organization (see [Getting the organizationId](https://developers.coveo.com/display/CloudPlatform/Getting+the+organizationId)).
-   You replace `MyOAuth2Token` in the `Authorization` header by an access token that grants you the privilege to view API keys in the target organization (see [Getting Your Coveo Cloud V2 Platform Access Token](Getting_Your_Coveo_Cloud_V2_Platform_Access_Token)). 

    Note:

    > It is not possible to authenticate this call using an API key, since an API key cannot have the privilege to edit or view other API keys.

The body of a successful response contains the list of all privileges which are individually assignable to any API key in the Coveo Cloud V2 organization matching the `organizationId` you provide as a path argument.

Note:

> The most important properties of an API key privilege are its `targetDomain`, `owner`, and `type` (see [Valid Privilege owner, targetDomain, and type Combinations](Valid_Privilege_owner,_targetDomain,_and_type_Combinations)). You do not need to specify the `targetIds` and `global` properties of the privileges you include in the `privileges` parameter when you create an API key.

**Example:**

**200 OK**

```
[
  {
    "targetDomain": "AUTHENTICATION_EDITOR",
    "targetIds": [],
    "owner": "SEARCH_API",
    "global": false
  },
  {
    "type": "EDIT",
    "targetDomain": "ON_PREMISE_ADMINISTRATION",
    "targetIds": [],
    "owner": "PLATFORM",
    "global": false
  },
  ...
]
```


