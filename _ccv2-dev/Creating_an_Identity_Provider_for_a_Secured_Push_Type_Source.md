---
slug: "56"
layout: content-2-panel
title: Creating an Identity Provider for a Secured Push Type Source
categories: migrated
---

# Creating an Identity Provider for a Secured Push Type Source

When the content of a system that you want to make searchable is secured, meaning that system items are accessible only by specific authenticated users or groups members, you can also use the Push API to push permissions associated with each item into the source. In this case, you must however also create an identity provider that you associate with your source.

The identity provider role is to hold known identities for the indexed system, and expand group members and identity mappings. When a user performs a query, the identity provider adds to the query the groups to which the user belongs as well as mapped identities so that he or she can see all items that are secured with these groups and these identities. You must therefore populate and update the identity provider using the Push API (see [Pushing Permissions to a Secured Source](https://developers.coveo.com/x/JoodAg)). 

The following procedure describes how to create a Coveo Cloud V2 identity provider and associate it to a specific source. 

1.  If not already done, create a secured push type source and get an API key:

    1.  From the administration console (see Add/Edit a Push Source - Panel)
    2.  From the API (see [Creating a Push Type Source](https://developers.coveo.com/x/uIQAAg))

2.  Get the `organizationId` and `sourceId` (see [Parameters and API Calls](https://developers.coveo.com/x/QokkAg)).

3.  Create your identity provider for your secured source.

    1.  Use the following API call:

        ```
        PUT https://platform.cloud.coveo.com/rest/organizations/{organizationId}/securityproviders/{securityProviderName}
        ```

        and replace `{organizationId}` by your `organizationId`.

        Choose a meaningful name (such as one including the name of the source to which it is associated) for your security provider to replace `{securityProviderName}`.

    2.  Your call must include the following headers:

        <table>
        <colgroup>
        <col width="50%" />
        <col width="50%" />
        </colgroup>
        <thead>
        <tr class="header">
        <th>Key</th>
        <th>Value</th>
        </tr>
        </thead>
        <tbody>
        <tr class="odd">
        <td><code>Authorization</code></td>
        <td><p><code>Bearer valid_API_key value&gt;</code></p>
        <div class="aui-message warning shadowed information-macro">
        <div class="message-content">
        <blockquote>
        Ensure that the API key you got has the minimal privileges to work with the API.
        </blockquote>
        <blockquote>
        In the administration console, under <strong>Organization</strong>, access the<strong>API Keys</strong> page, select your API key, and in the <strong>Privileges</strong> tab, select the <strong>Edit</strong> check box for the <strong>Security identity providers</strong> privilege.
        </blockquote>
        </div>
        </div></td>
        </tr>
        <tr class="even">
        <td><code>Content-Type</code></td>
        <td><code>application/json</code></td>
        </tr>
        </tbody>
        </table>

    3.  Enter a JSON as shown in the following example:

        ```
        {
          "name" : "security_identity_provider_name",
          "nodeRequired": false,
          "type": "EXPANDED",
          "referencedBy": [{
              "id": "source_ID",
              "type": "SOURCE"
            }],
          "cascadingSecurityProviders": {
               "Email Security Provider": {
                    "name": "Email Security Provider",
                    "type": "EMAIL"
                }
           }
        }
        ```

        where you replace `security_identity_provider_name` and `source_ID` by their real values.
        It is generally recommended to include the `cascadingSecurityProviders` to cascade your security provider to the `Email Security Provider` so that identities sharing the same email will be mapped.

        **Example:**

        Your Coveo Cloud organization includes secured sources for Active Directory, Salesforce, and your push content. Your users have a distinct account in each system. Their Active Directory includes their corporate email addresses that will be cascaded to the `Email Security Provider`, their Salesforce account name is their corporate email address, and you push identities to your secured push type source with the associated corporate email address.

        When a user is authenticated in the search page with any of these 3 identities, because the identity provider of the 3 sources resolve to the common email, he will be able to see items he is authorized to see from any of these sources.

    4.  Send your request.
    5.  In the administration console **Security Identities** page, validate that your identity provider is created (appearing in the list of providers) and associated to your source.

     

## Attachments:

![](images/icons/bullet_blue.gif){width="8" height="8"} [image2016-6-16 16:21:13.png](attachments/35490354/35455305.png) (image/png)

