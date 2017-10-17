---
slug: "87"
layout: content-2-panel
title: Logging into the Coveo Cloud V2 Platform
categories: migrated
toc: ccv2-dev
---

# Logging into the Coveo Cloud V2 Platform

You can log into the [Coveo Cloud V2 platform](Glossary_37585054.html#Glossary-CoveoCloudV2Platform)with any identity by authenticating with one of the supported identity providers (such as Google, Office 365, or Salesforce).

To log into the Coveo Cloud V2 platform:

1.  Direct your web browser to [https://platform.cloud.coveo.com](https://platform.cloud.coveo.com/). 
2.  Select the identity provider you want to use to log into the Coveo Cloud V2 platform (e.g., Google). 
    This action automatically redirects you to the corresponding authentication page.
3.  If you are not already logged into the selected identity provider, you must do so. 
    Once successfully authenticated, you are automatically redirected back to https://platform.cloud.coveo.com.
4.  If the identity you are authenticated as is already known by the Coveo Cloud V2 platform, you are now logged in.
    Assuming this identity grants you access to a Coveo Cloud V2 organization, the Coveo Cloud V2 administration console opens.
5.  Otherwise, in the **Customer Agreement and Privacy Policy** panel, consult and accept the Coveo Customer Agreement and Privacy Policy to continue.  
    The **You currently do not have access to any organizations** message appears, which is normal at this point.

Note:

> You will never actually have to "create an account" in the Coveo Cloud V2 platform.

> The first time you log into the platform using one of the supported identity providers, the identity you authenticate as is automatically registered in the platform. Thereafter, you only need to authenticate as this registered identity to log back into the platform.

**Example:**

-   Alice Smith logs into the Coveo Cloud V2 platform for the very first time. She decides to use Google as an identity provider.
-   Once Alice has successfully logged into her Google account (e.g., `asmith@example.com`), the Google identity provider forwards an OAuth2 token to the Coveo Cloud V2 platform.
-   The Coveo Cloud V2 platform validates this OAuth2 token and registers the `asmith@example.com-google` identity.
-   From now on, whenever Alice logs into the Coveo Cloud V2 platform using the Google identity provider to authenticate as the owner of the `asmith@example.com` Google account, she is recognized in the platform as the `asmith@example.com-google` identity.
-   If Alice subsequently decides to log into the platform using another identity provider, such as Office 365, the platform registers a new identity for this account (presumably `asmith@example.com-office365`).
-   Similarly, if Alice uses the Google identity provider to authenticate as the owner of another Google account (e.g., `asmith2@example.com`), the platform registers a new identity for this account (i.e., `asmith2@example.com-google`).


