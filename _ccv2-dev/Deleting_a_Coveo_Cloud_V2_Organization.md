---
slug: "58"
layout: content-2-panel
title: Deleting a Coveo Cloud V2 Organization
categories: migrated
---

# Deleting a Coveo Cloud V2 Organization

You will typically rarely (if ever) need to delete a [Coveo Cloud V2 organization](Glossary_37585054.html#Glossary-CoveoCloudV2Organization), unless you originally created this organization for a specific purpose such as testing, and this purpose is now finished. In such a case, deleting the "obsolete" organization is a good practice.

Important:

> Deleting a Coveo Cloud V2 organization is permanent and irreversible. Make sure you know what you are doing before you perform this call.

You can use the [Delete an organization](https://platform.cloud.coveo.com/docs?api=Platform#!/Organizations/rest_organizations_paramId_delete) operation to permanently remove a specific Coveo Cloud V2 organization from the [Coveo Cloud V2 platform](Glossary_37585054.html#Glossary-CoveoCloudV2Platform).

```
DELETE https://platform.cloud.coveo.com/rest/organizations/{organizationId}
Accept: application/json
Authorization: Bearer MyAccessToken
```

Ensure that:

-   You replace `{organizationId}` in the path by the actual ID of the target Coveo Cloud V2 organization (see [Getting the organizationId](https://developers.coveo.com/display/CloudPlatform/Getting+the+organizationId)).
-   You replace `MyAccessToken` in the `Authorization` header by an access token that grants the **Organization - Edit** privilege in the target organization (see [Creating an API Key](https://developers.coveo.com/display/CloudPlatform/Creating+an+API+Key), [Getting the Privileges of an Access Token](https://developers.coveo.com/display/CloudPlatform/Getting+the+Privileges+of+an+Access+Token), and [Getting Your Coveo Cloud V2 Platform Access Token](https://developers.coveo.com/display/CloudPlatform/Getting+Your+Coveo+Cloud+V2+Platform+Access+Token)).

A successful response has no content, but signifies that the target organization no longer exists in the Coveo Cloud V2 platform.

**Example:**

**204 No Content**

```
 
```


