---
layout: content-2-panel
title: Getting Your Coveo Cloud V2 Platform Access Token
categories: migrated
toc: ccv2-dev
---

# Getting Your Coveo Cloud V2 Platform Access Token

Whenever you successfully log into the [Coveo Cloud V2 platform](Glossary_37585054.html#Glossary-CoveoCloudV2Platform), the platform automatically generates or refreshes an access token for you. This token is valid for four hours, and is linked to the identity with which you are authenticated in the platform.

If your identity has access to a [Coveo Cloud V2 organization](Glossary_37585054.html#Glossary-CoveoCloudV2Organization), you can use this token to authenticate calls to any of the Coveo Cloud V2 platform REST API operations for which your identity has the required privileges in this organization.

Otherwise, you can still use this token to call certain global Coveo Cloud V2 platform REST API operations, such as the one that allows you to create an organization (see [Creating a Coveo Cloud V2 Organization](Creating_a_Coveo_Cloud_V2_Organization)).

To get your Coveo Cloud V2 platform access token:

1.  In your web browser, open your developer tools.
2.  Log into the Coveo Cloud V2 platform (see [Logging into the Coveo Cloud V2 Platform](Logging_into_the_Coveo_Cloud_V2_Platform)).
3.  In your developer tools, typically under the **Storage** or **Application** tab, locate and inspect the `https://platform.cloud.coveo.com` cookie.
    In this cookie, the `access_token` field value is your Coveo Cloud V2 platform access token.

