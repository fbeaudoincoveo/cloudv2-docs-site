---
slug: "69"
layout: content-2-panel
title: Getting the Privileges of an Access Token
categories: migrated
---

# Getting the Privileges of an Access Token

When you perform a [Coveo Cloud V2 platform](Glossary_37585054.html#Glossary-C) REST API operation call, you must ensure that the access token you use to authenticate your API call minimally grants you the privileges which are required to access the endpoint (see [Privileges](http://www.coveo.com/go?dest=cloudhelp&lcid=9&context=300)). Otherwise the call typically returns a `401 UNAUTHORIZED` response.

You can use the [Get all organization privileges for the access token](https://platform.cloud.coveo.com/docs?api=AuthorizationServer#!/Organization32Privileges/rest_organizations_paramId_privileges_token_post) operation to retrieve the list of privileges which are granted to a certain access token (OAuth2 token, Coveo Cloud V2 API key, or JWT search token) in the scope of a specific [Coveo Cloud V2 organization](Glossary_37585054.html#Glossary-CoveoCloudV2O):

```
POST https://platform.cloud.coveo.com/rest/organizations/{organizationId}/privileges/token?accessToken={accessToken}
Accept: application/json
Content-Type: application-json
Authorization: Bearer MyAccessToken
```

Ensure that:

-   You replace `{organizationId}` in the path by the actual ID of the target Coveo Cloud V2 organization (see [Getting the organizationId](https://developers.coveo.com/display/CloudPlatform/Getting+the+organizationId)).
-   You replace `{accessToken}` in the query string by the access token whose privileges you want to retrieve.
-   You replace `MyAccessToken` in the `Authorization` header by a valid access token. This access token does not need to have any privileges in the target organization.

The body of a successful response contains the list of privileges granted by the token that corresponds to the `accessToken` you provide as a query string argument (see [Valid Privilege owner, targetDomain, and type Combinations](Valid_Privilege_owner,_targetDomain,_and_type_Combinations)). Those privileges only apply within the confines of the target organization.

**Example:**

**200 OK**

```
[
  {
    "targetDomain": "EXECUTE_QUERY",
    "targetIds": [],
    "owner": "SEARCH_API",
    "global": false
  },
  {
    "type": "EDIT",
    "targetDomain": "ANALYTICS_DATA",
    "targetIds": [],
    "owner": "USAGE_ANALYTICS",
    "global": false
  }
]
```


