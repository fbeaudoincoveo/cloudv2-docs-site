---
slug: "59"
layout: content-2-panel
title: Deleting an API Key
categories: migrated
---

# Deleting an API Key

It is good practice to create an API key with minimal privileges for one precise and exclusive purpose and delete this API key from the [Coveo Cloud V2 organization](Glossary_37585054.html#Glossary-CoveoCloudV2Organization) when it is no longer needed for that purpose. 

> You cannot undo an API key delete operation. If you are not entirely sure you should delete a specific API key, consider disabling it instead.

You can use the [Delete an api key](https://platform.cloud.coveo.com/docs?api=AuthorizationServer#!/Api32Keys/rest_organizations_paramId_apikeys_paramId_delete) operation to completely remove an API key from a specific Coveo Cloud V2 organization:

```
DELETE https://platform.cloud.coveo.com/rest/organizations/{organizationId}/apikeys/{apiKeyId}
Accept: application/json
Authorization: Bearer MyOAuth2Token
```

Ensure that:

-   You replace `{organizationId}` in the query string by the actual ID of the target Coveo Cloud V2 organization (see [Getting the organizationId](Getting_the_organizationId)).
-   You replace `{apiKeyId}` in the query string by the actual ID of the API key you want to delete (see [Getting the apiKeyId](Getting_the_apiKeyId)).
-   You replace `MyOAuth2Token` in the `Authorization` header by an access token that grants the privilege to edit API keys in the target organization (see [Getting Your Coveo Cloud V2 Platform Access Token](Getting_Your_Coveo_Cloud_V2_Platform_Access_Token) and [Getting the Privileges of an Access Token](Getting_the_Privileges_of_an_Access_Token)).

    Note:

    > It is not possible to authenticate this call using an API key, since an API key cannot have the privilege to edit or view other API keys.

A successful response has no content, but signifies that the API key corresponding to the `apiKeyId` you provide as a query string argument no longer exists in the target organization.

**Example:**

**204 No Content**

```
 
```


