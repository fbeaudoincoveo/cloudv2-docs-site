---
layout: content-2-panel
title: Configuring SAML for Use with AD FS
categories: migrated
---

# Configuring SAML for Use with AD FS

**In this topic:**

-   [Configuring a Relying Party Trust in AD FS](#configuring-a-relying-party-trust-in-ad-fs)
-   [Downloading the XML Metadata](#downloading-the-xml-metadata)
-   [Creating an AD FS SAML Authentication Provider with the Coveo Search API](#creating-an-ad-fs-saml-authentication-provider-with-the-coveo-search-api)

## Configuring a Relying Party Trust in AD FS

To use AD FS to perform authentication for the Coveo Search API through SAML 2.0, you first need to configure a **Relying Party Trust** in the AD FS MMC snap-in. Follow these steps:

1.  Open the **AD FS 2.0 Management** console.
2.  Expand the **Trust Relationships node.**
3.  Select **Relying Party Trusts.**
4.  In the panel on the right, click **Add Relying Party Trust**.
5.  in the wizard that opens, click **Start**.
6.  Select **Enter data about the relying party manually**, and then click **Next**.
7.  Enter an appropriate display name (e.g., `Coveo Search API`)**,** and then click **Next**.
8.  Select **AD FS 2.0 profile**, and then click **Next**.
9.  Click **Next** to skip specifying a token encryption certificate.
10. Check **Enable support for the SAML 2.0 WebSSO protocol**.

11. Enter the **Relying party SAML 2.0 SSO service URL**. This URL must point to to the Coveo Cloud Platform V2 REST Search API (i.e., https://platform.cloud.coveo.com/rest/search) and specify the path used to login to your SAML authentication provider (see [Creating a SAML Authentication Provider with the Coveo Search API](https://developers.coveo.com/x/pw8vAg#SAMLAuthentication-CreatingASAMLAuthenticationProviderWithTheCoveoSearchAPI)).

    **Example:**

    If the `name` of your SAML authentication provider is `mySAMLAuthenticationProvider`, the resulting **Relying party SAML 2.0 SSO service URL** is `https://platform.cloud.coveo.com/rest/search/login/mySAMLAuthenticationProvider`.

12. Click **Next**.

13. Enter the **Relying party trust identifier**. This can be any string, as long as it matches the value you specify for the `relyingPartyIdentifier` parameter of your SAML authentication provider.

    **Example:**

    A good choice when specifying the **Relying party trust identifier** value is to use the Coveo Cloud V2 Platform hostname (i.e., `https://platform.cloud.coveo.com`).

14. Click **Add**, and then **Next**.
15. Select **Permit all users to access this relying party**, and then click **Next**.
16. Click **Next**, check the **Open the Edit Claim Rules dialog for this relying party trust when the wizard closes**, and then click **Close**.
17. A new dialog box opens.
18. In the new dialog box that opens, in the **Issuance Transform Rules** tab, click the **Add Rule** button.
19. In the new wizard that opens, in the **Claim rule template**dropdown, select **Send LDAP Attributes as Claims**, and then click **Next**.
20. In **Claim rule name**, enter **Send Name ID**.
21. In the **Attribute store** dropdown, select **Active Directory**.
22. In the table below, select **SAM-Account-Name** in the left column, and **Name ID**in the right one.
23. Click **Finish**.
24. Close the dialog by clicking **OK**. 

## Downloading the XML Metadata

The XML metadata is a file that you can download from an identity provider (in this case AD FS). It contains information such as the certificates that validate the responses (see [SAML 2.0 Metadata](https://en.wikipedia.org/wiki/SAML_2.0#SAML_2.0_Metadata)). You need to set the content of this file as the value of the `metadata` parameter when you create your SAML authentication (see [Creating a SAML Authentication Provider with the Coveo Search API](https://developers.coveo.com/x/pw8vAg#SAMLAuthentication-CreatingASAMLAuthenticationProviderWithTheCoveoSearchAPI)).

On a typical AD FS setup, you can download the XML file from https://{myserver.domain.com}/FederationMetadata/2007-06/FederationMetadata.xml, where you must replace {myserver.domain.com} with the actual hostname of your AD FS server.

## Creating an AD FS SAML Authentication Provider with the Coveo Search API

You can follow the standard guidelines when creating a SAML authentication provider with AD FS as an IdP (see [Creating a SAML Authentication Provider with the Coveo Search API](https://developers.coveo.com/x/pw8vAg#SAMLAuthentication-CreatingASAMLAuthenticationProviderWithTheCoveoSearchAPI)).

Keep in mind that the value of the `assertionConsumerServiceUrl` parameter should match the value of the **Relying party SAML 2.0 SSO service URL** (see [Relying party SAML 2.0 SSO service URL](Configuring_SAML_for_Use_with_AD_FS)), and the value of the `relyingPartyIdentifier` parameter should match that of the **Relying party trust identifier**(see [Relying party trust identifier](Configuring_SAML_for_Use_with_AD_FS)).

You can also test your setup by following the standard guidelines (see [Testing the Setup](https://developers.coveo.com/x/pw8vAg#SAMLAuthentication-TestingtheSetup)).
