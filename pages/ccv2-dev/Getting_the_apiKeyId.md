---
layout: content-2-panel
title: Getting the apiKeyId
categories: migrated
---

# Getting the apiKeyId

The `apiKeyId` is a required parameter in any Coveo Cloud V2 platform REST API operation that interacts with a single specific API key.

You can use the [Get all api keys for this organization](https://platform.cloud.coveo.com/docs?api=AuthorizationServer#!/Api32Keys/rest_organizations_paramId_apikeys_get) operation to find the `apiKeyId` of an API key in a specific [Coveo Cloud V2 organization](Glossary_37585054.html#Glossary-CoveoCloudV2Organization):

```
GET https://platform.cloud.coveo.com/rest/organizations/{organizationId}/apiKeys
Accept: application/json
Authorization: Bearer MyOAuth2Token
```

Ensure that:

-   You replace `{organizationId}` in the path by the actual ID of the target Coveo Cloud V2 organization (see [Getting the organizationId](https://developers.coveo.com/display/CloudPlatform/Getting+the+organizationId)).
-   You replace `MyOAuth2Token` in the `Authorization` header by an access token that grants you the privilege to view API keys in the target organization (see [Getting Your Coveo Cloud V2 Platform Access Token](Getting_Your_Coveo_Cloud_V2_Platform_Access_Token) and [Getting the Privileges of an Access Token](Getting_the_Privileges_of_an_Access_Token)).

    Note:

    > It is not possible to authenticate this call using an API key, since an API key cannot have the privilege to edit or view other API keys.

The body of a successful response contains information about all API keys in the target Coveo Cloud V2 organization.

To find the `apiKeyId`:

1.  In the response body, use the `displayName` or `description` parameter values to find the API key for which you want to get the `apiKeyId`. 
2.  Copy for the `id` property value of the API key.

    **Example:**

    **200 OK**

    ```
    [
      {
        "id": "wduuqg3ip2c3i3gpopapxhcgxe", // This is the `apiKeyId` of the `My Source API Key` API key.
        "value": "**********-****-****-****-********1b3e",
        "organizationId": "mycoveocloudv2organization",
        "displayName": "My Source API Key",
        "description": "An API key to edit and view sources.",
        ...
      },
      ...
    ] 
    ```

 
