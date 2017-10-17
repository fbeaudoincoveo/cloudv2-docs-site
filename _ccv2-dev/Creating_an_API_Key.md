---
slug: "55"
layout: content-2-panel
title: Creating an API Key
categories: migrated
---

# Creating an API Key

Almost all [Coveo Cloud V2 platform](Glossary_37585054.html#Glossary-CoveoCloudV2Platform) REST API operations require authentication. In most cases, you can authenticate a call using either an OAuth2 access token (see [Getting Your Coveo Cloud V2 Platform Access Token](Getting_Your_Coveo_Cloud_V2_Platform_Access_Token)) or an API key with the required privileges.

You can use the [Create a new api key for this organization](https://platform.cloud.coveo.com/docs?api=AuthorizationServer#!/Api32Keys/rest_organizations_paramId_apikeys_post) operation to create an API key with certain privileges in a specific [Coveo Cloud V2 organization](Glossary_37585054.html#Glossary-CoveoCloudV2Organization): 

```
POST https://platform.cloud.coveo.com/rest/organizations/{organizationId}/apikeys
Accept: application/json
Content-Type: application/json
Authorization: Bearer MyOAuth2Token
 
{
  "description": "My API key description",
  "displayName": "My API key display name",
  "enabled": true,
  "privileges": [
    {
      "owner": "OWNER",
      "targetDomain": "MY_TARGET_DOMAIN",
      "type": "TYPE"
    },
    ...
  ]
}
```

Ensure that:

-   You replace `{organizationId}` in the path by the actual ID of the target Coveo Cloud V2 organization (see [Getting the organizationId](Getting_the_organizationId)).
-   You replace `MyOAuth2Token` in the `Authorization` header by an access token that grants you the privilege to edit API keys in the target organization (see [Getting Your Coveo Cloud V2 Platform Access Token](Getting_Your_Coveo_Cloud_V2_Platform_Access_Token) and [Getting the Privileges of an Access Token](Getting_the_Privileges_of_an_Access_Token)).

    Note:

    > It is not possible to authenticate this call using an API key, since an API key cannot have the privilege to edit or view other API keys.

-   You set the `enabled` property to `true`  in the request body when you want the new API key to work right away. 

-   You specify a valid `owner`, `targetDomain`, and possibly a `type` for each privilege you want to grant the API key (see [Getting the Privileges You Can Assign to an API Key](Getting_the_Privileges_You_Can_Assign_to_an_API_Key) and [Valid owner, targetDomain, and Type Value Combinations for Privileges](Valid_Privilege_owner,_targetDomain,_and_type_Combinations)).

    Best practice:

    > Although optional, you should also specify an adequate `displayName`, summarizing the API key purpose, and a `description`, indicating when, for who, and for what purpose you are creating the API key. This information will greatly help whoever manages API keys for this organization.

The body of a successful response contains information about the API key you just created.

-   You can use the `id` property to later edit or delete the API key. You can always get this value back once the API key has been created (see [Getting the apiKeyId](Getting_the_apiKeyId)).
-   The `value` property contains the API key itself.

    Important:

    > The API key creation call response body is your unique occasion to get the API key `value`. It is not possible to get it again.

    > If you fail to get the `value`,  delete the unused lost key, and create another one (see [Deleting an API Key](Deleting_an_API_Key)).

**Example:**

**201 Created**

```
{
  "id": "wduuqg3ip2c3i3gpopapxhcgxe",
  "value": "xx590a182c-5045-4914-a00b-1f4099581b3e",
  "organizationId": "mycoveocloudv2organization",
  "displayName": "My Source API Key",
  "description": "An API key to edit and view sources.",
  "privileges": [
    {
      "type": "EDIT",
      "targetDomain": "SOURCE",
      "targetIds": [],
      "owner": "PLATFORM"
    },
    {
      "type": "VIEW",
      "targetDomain": "SOURCE",
      "targetIds": [],
      "owner": "PLATFORM"
    }
  ]
}
```


