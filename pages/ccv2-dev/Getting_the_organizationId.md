---
layout: content-2-panel
title: Getting the organizationId
categories: migrated
---

# Getting the organizationId

The `organizationId` is the unique and permanent identifier of a [Coveo Cloud V2 organization](Glossary_37585054.html#Glossary-CoveoCloudV2Organization). The `organizationId` value is the lowercased original display name of the organization, stripped of any special characters and spaces. A sequential number or GUID is added as a suffix if the resulting ID already exists in the [Coveo Cloud V2 platform](Glossary_37585054.html#Glossary-CoveoClou).

**Example:**

Your Coveo Cloud V2 organization is created with **My Coveo Search Org** as a display name. However, the resulting `organizationId` value is `mycoveosearchorg2` because `mycoveosearchorg` is the ID of another organization that already existed in the Coveo Cloud V2 platform when your organization was created.

Note:

> Coveo Cloud V2 administrators can change an organization display name whenever they want, but the `organizationId` value is permanent. Consequently, the `organizationId` can be completely different from the current organization display name.

Many Coveo Cloud V2 platform REST API methods require that you provide a value for the `organizationId` parameter.

You can use the [Get all organizations](https://platform.cloud.coveo.com/docs?api=Platform#!/Organizations/rest_organizations_get) operation to find the `organizationId` of a Coveo Cloud V2 organization: 

```
GET https://platform.cloud.coveo.com/rest/organizations
Accept: application/json
Authorization: Bearer MyAccessToken
```

Ensure that:

-   You replace `MyAccessToken` in the `Authorization` header by an access token that grants you the **Organization - View** privilege (see [Creating an API Key](Creating_an_API_Key), [Getting the Privileges of an Access Token](Getting_the_Privileges_of_an_Access_Token), and [Getting Your Coveo Cloud V2 Platform Access Token](Getting_Your_Coveo_Cloud_V2_Platform_Access_Token)).

The body of a successful response contains information about the Coveo Cloud V2 organization (or organizations) your access token allows you to view.

Note:

> If you authenticate this call using an OAuth2 access token whose associated identity has the **Organization - View** privilege for more than one Coveo Cloud V2 organization, the body of a successful response contains information about each of those organizations.

> Otherwise, if you authenticate this call using a valid API key, the body of a successful response only contains information about the organization this API key was created in.

To find the `organizationId`, in the response body, look for the `id` property value of the Coveo Cloud V2 organization.

**Example:**

**200 OK**

```
[
  {
    "createdDate": 1460705726000,
    "displayName": "My Coveo Cloud V2 Organization",
    "emailNotificationsEnabled": false,
    "id": "mycoveocloudv2organization", // This is the `organizationId` of the `My Coveo Cloud V2 Organization` organization.
    "owner": {
      "email": "asmith@example.com"
    },
    "readOnly": false
  }
]
```


