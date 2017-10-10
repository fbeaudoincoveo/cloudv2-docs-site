---
layout: content-2-panel
title: Creating a Coveo Cloud V2 Organization
categories: migrated
---

# Creating a Coveo Cloud V2 Organization

One of the very first thing you need to do to start using the [Coveo Cloud V2 platform](Glossary_37585054.html#Glossary-CoveoCloudV2) is to create your [Coveo Cloud V2 organization](Glossary_37585054.html#Glossary-C).

Your organization will host your [sources](Glossary_37585054.html#Glossary-Source), security identity providers, [Coveo Machine Learning](Glossary_37585054.html#Glossary-CoveoMachineLearning) models, [Coveo Cloud usage analytics](Glossary_37585054.html#Glossary-CoveoCloudUsageAnalytics) data, and everything else you need to make your content searchable.  

You can use the [Create an organization](https://platformdev.cloud.coveo.com/docs?api=Platform#!/Organizations/rest_organizations_post) operation to set up a new Coveo Cloud V2 organization:

```
POST https://platform.cloud.coveo.com/rest/organizations?name={myOrganizationDisplayName}
Content-Type: application/json
Accept: application/json
Authorization: Bearer MyOAuth2Token
```

Ensure that:

-   You replace `{myOrganizationDisplayName}` in the query string by the display name you want to use for the new organization.

    > While you can always change your organization display name later, be aware that the original `name` value you specify when creating an organization will forever be part of the unique and permanent ID of that organization.

    > The organization ID is the lowercased original `name` value for that organization, stripped of any special characters and white spaces. A GUID or sequential number can be appended to the resulting string if an identical organization ID already exists in the Coveo Cloud V2 platform when the new organization is created.

-   You replace `MyOAuth2Token` in the `Authorization` header by an access token provided by the Coveo Cloud V2 platform (see [Getting Your Coveo Cloud V2 Platform Access Token](Getting_Your_Coveo_Cloud_V2_Platform_Access_Token)).

The body of a successful response contains the unique and permanent ID of the organization you just created. This value is important, as it is a required parameter in many Coveo Cloud V2 platform REST API operations. You can always retrieve this organization ID later (see [Getting the organizationId](Getting_the_organizationId)).

**Example:**

**201 Created**

```
{
  "id": "mycoveocloudv2organization"
} 
```


