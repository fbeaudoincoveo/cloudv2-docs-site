---
slug: "110"
layout: content-2-panel
title: SAML Authentication
categories: migrated
---

# SAML Authentication

**In this topic:**

-   [Configuring SAML Authentication](#configuring-saml-authentication)
    -   [Configuring your SAML IdP](#configuring-your-saml-idp)
    -   [Obtaining the SAML Metadata](#obtaining-the-saml-metadata)
    -   [Creating a SAML Authentication Provider with the Coveo Search API](#creating-a-saml-authentication-provider-with-the-coveo-search-api)
-   [Testing the Setup](#testing-the-setup)
-   [Assigning More Than One Organization to Your Identity Provider](#assigning-more-than-one-organization-to-your-identity-provider)

Many Single Sign-On (SSO) systems use the SAML 2.0 standard to allow external services to rely on the authentication that a central Identity Provider (IdP) entity delivers. The Coveo Search API supports SAML authentication. In addition, the Coveo JavaScript Search Framework provides a component to enable SAML authentication in search pages (see the `AuthenticationProvider` component).

## Configuring SAML Authentication

Configuring SAML authentication involves configuring a SAML IdP and creating a SAML Authentication Provider using the Coveo Search API.

### Configuring your SAML IdP

Many implementations of the SAML 2.0 standard are available. Each implementation has its own distinct configuration process. See your product documentation for specific information on how to configure your IdP.

Specific instructions for certain identity providers are available

-   For **AD FS**, see [Configuring SAML for Use with AD FS](Configuring_SAML_for_Use_with_AD_FS)
-   For **Okta**, see [Configuring SAML for Use with Okta](Configuring_SAML_for_Use_with_Okta)

At some point during your IdP configuration process, you may have to specify the URL where to send the SAML assertions. This URL has the following format: `https://platform.cloud.coveo.com/rest/search/login/{provider}`, where you must replace `{provider}` with the `name` of your SAML authentication provider (see [Creating a SAML Authentication with the Coveo Search API](SAML_Authentication)).

During IdP configuration, it is also likely that you must define the username format to return when a user successfully authenticates. Make sure you select a format that suits your SAML authentication provider.

**Example:**

When using an `Active Directory` security provider, an acceptable username format would be `domain\user` or `user@domain`.

### Obtaining the SAML Metadata

Most of the configuration that the Coveo Search API requires comes from the SAML Metadata which your IdP can deliver (see [SAML Metadata](http://en.wikipedia.org/wiki/SAML_2.0#SAML_2.0_Metadata)). The metadata should be stored in an XML file that will be referenced in the [Windows Service Configuration File](https://developers.coveo.com/display/SearchREST/Windows+Service+Configuration+File).

### Creating a SAML Authentication Provider with the Coveo Search API

To configure a SAML authentication provider, you must send a `POST` request to `https://platform.cloud.coveo.com/rest/organizations/{organizationId}/authentication/saml` where you must replace `{organizationId}` by your Coveo Cloud V2 organization ID. The body of your `POST` request should look like the following example.

**Example:**

**Typical Body of a SAML Authentication Provider POST Request**

```
POST /rest/organizations/myorganizationid/authentication/saml HTTP/1.1
Host: platform.cloud.coveo.com
Content-Type: application/json
Authorization: Bearer MyOAuth2Token
 
{
  "name" : "mySAMLAuthenticationProvider",
  "provider" : "Active Directory",
  "assertionConsumerServiceUrl" : "https://platform.cloud.coveo.com/rest/search/login/mySAMLAuthenicationProvider",
  "metadata" : "<?xml version=\"1.0\" encoding=\"UTF-8\"?><md:EntityDescriptor xmlns:md=\"urn:oasis:names:tc:SAML:2.0:metadata\...",
  "relyingPartyIdentifier" : "https://www.platform.cloud.coveo.com",
  "expiration" : 3600000
}
```

Parameters

> `name` (string): Specifies the name of the SAML authentication provider. This value should match the last part of the assertionConsumerServiceUrl path.

> `provider` (string): Specifies the name of the security provider. This value should match the corresponding value from your IdP administration console.

> `assertionConsumerServiceUrl` (string): Specifies the URI where the browser should redirect after the user authenticates. The last part of the path of this value should match the `name` parameter value.

> `metadata` (string): Specifies the SAML XML Metadata (see [SAML Metadata](https://en.wikipedia.org/wiki/SAML_2.0#SAML_2.0_Metadata)). You can get this metadata from your IdP.

> `relyingPartyIdentifier` (string): Specifies the relying party identifier (see [Relying Party](https://www.oasis-open.org/committees/download.php/21111/saml-glossary-2.0-os.html#Relying%20Party)). This value should match the corresponding value from your IdP administration console. Specifying a value for this parameter is not mandatory when using Okta as an IdP.

> `expiration` (number): Specifies how much time (in milliseconds) it takes for the browser cookie that stores the SAML information to expire. If you set this parameter to 0, the cookie expires at the end of a browser session.

> Do not forget to escape all double quote (`"`) characters with backslashes (`\`) in the XML value of the `metadata` parameter.

>  Also remember to add the mandatory new lines (`\n`) in the certificate.

**Example:**

    <?xml version="1.0" encoding="UTF-8"?>

> becomes

    <?xml version=\"1.0\" encoding=\"UTF-8\"?>

> and

    <ds:X509Certificate>

      mUqDy0cEfgTDUGcUcFY1By4n9Y/VsBDFGiH0HwIDAQAB5A0GCSqGSIb3DQEBBQU4BCrTy147Fhcv

      s1GeQOQvibBc76Q6FuTGQaBrV00nYQByzr8T[...]

    </ds:X509Certificate>

> becomes

    <ds:X509Certificate>mUqDy0cEfgTDUGcUcFY1By4n9Y/VsBDFGiH0HwIDAQAB5A0GCSqGSIb3DQEBBQU4BCrTy147Fhcv\ns1GeQOQvibBc76Q6FuTGQaBrV00nYQByzr8T[...]</ds:X509Certificate>

A successful request returns a Status `201 Created` containing the `id` of the SAML authentication.

**Example:**

**A sample successful SAML authentication creation POST response**

```
Code: 201
 
{
  "id" : "g4t85744-769b-4885-p9w0-4m0hk49n674i"
}
```

You can create multiple SAML authentication providers if necessary. However, in most cases, a single SAML authentication provider is sufficient.

## Testing the Setup

Once you have created your SAML authentication provider using the Coveo Search API and configured your SAML IdP, you can test the setup by directing your browser to `https://platform.cloud.coveo.com/rest/search/login/{provider}`, where you must replace `{provider}` with the `name` of your SAML authentication provider (see [Creating a SAML Authentication Provider with the Coveo Search API](SAML_Authentication)). You should also specify your `access_token` in the query string.

If everything is setup properly, the Coveo Search API should return a `statusCode 200` containing a success message, along with the name of the user who authenticated.

**Example:**

**Testing the setup**

```
https://platform.cloud.coveo.com/rest/search/login/mySAMLAuthenicationProvider?access_token=wmLwtZwHv3LUf5W4G7X22PRjmROfyfOigdi-rnohxyeLw_9OldOGEeK3N-DBZZZydmjA1JWZ...
```

## Assigning More Than One Organization to Your Identity Provider

If you manage more than one Coveo Cloud V2 organization and have implemented SAML authentication for one of them, you might want to associate your other organization with your SAML authentication provider.

**Example:**

You have Coveo Cloud production and sandbox organizations, and want them to have an identical SAML authentication setup for testing purposes.

To associate another organization with your SAML authentication provider, first retrieve a list of the available organizations, and then update the target organization with the SAML authentication parameters.

1.  Ensure that the identity you entend to use to perform the following Coveo Cloud V2 API calls is a member of a group hat has a **View Organization** and an **Edit SAML identity provider** privilege in both organizations (see [Edit a Group: \[GroupName\] - Panel](http://www.coveo.com/go?dest=cloudhelp&lcid=9&context=296)).
2.  Ensure the SAML authentication configuration works as expected with your firts Coveo Cloud organization by testing your setup (see [Creating a SAML Authentication Provider with the Coveo Search API](SAML_Authentication) and [Testing the Setup](SAML_Authentication)). 
3.  Send a `GET` request to `https://platform.cloud.coveo.com/rest/organizations/{organizationId}/saml/availables` where you replace `{organizationId}` by the ID of your first Coveo Cloud V2 organization (see [Getting the organizationId](Getting_the_organizationId)).  
    A successful request returns a Status `200` containing the SAML authentication parameters for the specified organization and, and if any, other organizations using the same SAML autentication setup. The response body of your `GET` request should look like the following example.

    **Example:**

    **Typical Response Body of a SAML Authentication Provider GET Request**

    ```
     {
        "displayName": "MySAMLIdP",
        "entityId": "http://www.identityprovider.com/exkabcurm887FmOwOc0h7",
        "id": "xbjfnpsw4fw2yxvb2vmc5n2pty",
        "postBindingEndpoint": "https://mycompany.identityprovider.com/app/mycompany_identityproviderapp/exkabcurm887FmOwOc0h7/sso/saml",
        "x509Certificate": "MIIDpDCCAoygAwIBAgIGAVZbyf2L..."
        "organizationIds": [
          {
            "displayName": "organization1",
            "id": "organization1"
          }
        ],
      }
    ```

4.  Using the `GET` request response body, fill the body of a `PUT` request to `https://platform.cloud.coveo.com/rest/organizations/{organizationId}/saml/identityprovider` where you replace `{organizationId}` by the ID of your other Coveo Cloud V2 organization  (see [Getting the organizationId](Getting_the_organizationId)). 
    In the `PUT` request body, ensure to include the ID for both your first and your second organization. The organization `displayName`, however, is not required. The body of your `PUT` request should look like the following example.

    **Example:**

    **Typical Body of a SAML Authentication Provider PUT Request**

    ```
    {
      "displayName": "MySAMLIdP",
      "entityId": "http://www.identityprovider.com/exkabcurm887FmOwOc0h7",
      "id": "xbjfnpsw4fw2yxvb2vmc5n2pty",
      "organizationIds": [
        {
              "id": "organizationId1"
        },
     {
               "id": "organizationId2"
        }
      ],
      "postBindingEndpoint": "https://mycompany.identityprovider.com/app/mycompany_identityproviderapp/exkabcurm887FmOwOc0h7/sso/saml",
      "x509Certificate": "MIIDpDCCAoygAwIBAgIGAVZbyf2L..."
    }
    ```

    A successful request returns a Status `200` containing the parameters you entered in the request body and your second organization is updated.

5.  Test the SAML authentication setup in the updated organization.


