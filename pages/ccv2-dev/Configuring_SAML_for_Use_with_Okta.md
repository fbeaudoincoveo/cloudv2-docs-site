---
layout: content-2-panel
title: Configuring SAML for Use with Okta
categories: migrated
---

# Configuring SAML for Use with Okta

**In this topic:**

-   [Adding an Application in Okta](#adding-an-application-in-okta)
-   [Downloading the XML Metadata](#downloading-the-xml-metadata)
-   [Creating an Okta SAML Authentication Provider with the Coveo Search API](#creating-an-okta-saml-authentication-provider-with-the-coveo-search-api)

## Adding an Application in Okta

To use Okta to perform authentication for the Coveo Search API through SAML 2.0, you need to add an **Application** in the Okta administration site. Follow these steps:

1.  Open the Okta Administration site.
2.  Click the **Add Application** shortcut.
3.  Click **Create New App**.
4.  In the popup, select **SAML 2.0**, and then click **Create**.
5.  Enter a suitable name of the application (e.g., `Coveo Search API`).
6.  Check the **Do not display application icon to users** checkbox.
7.  Click **Next**.
8.  In **Single sign on URL**, enter the URL of the page used to login to your SAML authentication provider.

    **Example:**

    If the `name` of your SAML authentication provider is `mySamlProvider`, the resulting **Single sign on URL** is `https://platform.cloud.coveo.com/rest/search/login/mySamlProvider`.

9.  In **Audience URI**, enter a suitable relying party identifier.

    **Example:**

    A good choice when specifying the **Audience URI** value is to use the Coveo Cloud V2 Platform hostname (i.e., `https://platform.cloud.coveo.com`).

10. Click **Next** and finish the wizard.

## Downloading the XML Metadata

The XML metadata is a file that you can download from an identity provider (in this case Okta). It contains information such as the certificates that validate the responses (see [SAML 2.0 Metadata](https://en.wikipedia.org/wiki/SAML_2.0#SAML_2.0_Metadata)).  You need to set the content of this file as the value of the `metadata` parameter when you create your SAML authentication (see [SAML Authentication - Creating a SAML Authentication Provider with the Coveo Search API](https://developers.coveo.com/x/pw8vAg#SAMLAuthentication-CreatingASAMLAuthenticationProviderWithTheCoveoSearchAPI)).

When viewing your application in Okta administration, under the **Sign On** tab, locate the **Identity Provider metadata** link and use it to download the XML metadata.

## Creating an Okta SAML Authentication Provider with the Coveo Search API

You can follow the standard guidelines when creating a SAML authentication provider with Okta as an IdP (see [SAML Authentication - Creating a SAML Authentication Provider with the Coveo Search API](https://developers.coveo.com/x/pw8vAg#SAMLAuthentication-CreatingASAMLAuthenticationProviderWithTheCoveoSearchAPI)).

Keep in mind that the value of the `assertionConsumerServiceUrl` parameter should match the value of the **Single sign on URL** (see [Single sign on URL](Configuring_SAML_for_Use_with_Okta)), and the value of the `relyingPartyIdentifier` parameter should match that of the **Audience URI**(see [Audience URI](Configuring_SAML_for_Use_with_Okta)).

> Specifying a value for the `relyingPartyIdentifier` parameter is not mandatory when using Okta as an IdP.

You can also test your setup by following the standard guidelines (see [SAML Authentication - Testing the Setup](https://developers.coveo.com/x/pw8vAg#SAMLAuthentication-TestingtheSetup)).
