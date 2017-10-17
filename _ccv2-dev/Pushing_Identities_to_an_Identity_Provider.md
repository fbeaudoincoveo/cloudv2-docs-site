---
slug: "101"
layout: content-2-panel
title: Pushing Identities to an Identity Provider
categories: migrated
---

# Pushing Identities to an Identity Provider

In this topic: /\*\*/ Deleting a Security Identity from your Identity Provider Deleting Old Identities

When you push items with permissions to a secured push type source, you must also push the identities, groups/members, and identity mappings to the associated identity provider that you created for this source (see Creating an Identity Provider for a Secured Push Type Source). On each source item, permissions are expressed as unique security identities (USER, GROUP, or VIRTUAL\_GROUP) allowed or denied to view secured content in Coveo search results. When an authenticated user performs a query, search results only include items that are allowed for the identity, mapped identities, and/or groups the user belongs to.

This topic describes how to push system identities.

1.  If not already done, create a secured push type source and get an API key
    1.  from the administration console (see [Add/Edit a Push Source - Panel](http://www.coveo.com/go?dest=ccv2ac&context=53)), or
    2.  using the API (see [Creating a Push Type Source](https://developers.coveo.com/x/uIQAAg)).

2.  If not already done, create an identity provider that can be provisioned using the Push API (see [Creating an Identity Provider for a Secured Source](https://developers.coveo.com/x/MoodAg)).
3.  Push a security identity to your identity provider.
    1.  Use the following API call:

        ```
        PUT https://push.cloud.coveo.com/v1/organizations/<organizationId>/providers/<providerId>/permissions?orderingId=<orderingId>
        ```

        where you replace `<organizationId>` and `<providerId>` by their real values. The `<providerId>` is simply the provider ID as returned when you created your identity provider (e.g., `-uzkeyume65j7hbcxboldbssglq`).
        The `orderingId` is only required when you want to delete identities which are "older" than a certain timestamp.

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
        Ensure that the API key you use has the right privileges to work with the API. 
        </blockquote>
        <blockquote>
        In the administration console, under <strong>Organization</strong>, access the<strong>API Keys</strong> page, select your API key, and in the <strong>Privileges</strong> tab, select the <strong>Edit</strong> check boxes for the <strong>Security identities</strong> and the <strong>Security identity providers</strong> privileges.
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

    3.  Enter a JSON in a format similar to the following example to add a `USER` identity:

        ```
        {
            "Identity": {
                "Name": "identity_name",
                "Type": "USER",
                "AdditionalInfo": {}
            }
        }
        ```

        The `identity_name` needs to be unique across the entire system.
        The `Type` parameter value must be in uppercase. The possible values are:

        1.  `UNKOWN`
            Defines an identity whose type is unknown.
        2.  `USER`
            Defines a single user.
        3.  `GROUP`
            Defines an existing group of identities within the indexed system. Individual members of this group can be of any valid identity `Type` (`USER`, `GROUP`, or `VIRTUAL_GROUP`).
        4.  `VIRTUAL_GROUP`
            Defines a group that does not exist within the indexed system. Mechanically, a `VIRTUAL_GROUP` is identical to a `GROUP`.

    4.  Enter a JSON in a format similar to the following example to add a group for which the members are already pushed (see [Batch Pushing Identities to an Identity Provider](https://developers.coveo.com/x/5YcdAg)):

        ```
        {
            "Identity": {
                "Name": "UX_Team",
                "Type": "GROUP",
                "AdditionalInfo": {}
            },
            "Members": [{
                "Name": "designer1",
                "Type": "USER",
                "AdditionalInfo": {}
            },
            {
                "Name": "designer2",
                "Type": "USER",
                "AdditionalInfo": {}
            }],
            "WellKnowns": [{
                "Name": "Everyone",
                "Type": "GROUP",
                "AdditionalInfo": {}
            }]
        }
        ```

        The `WellKnowns` parameter is optional.

        > `WellKnowns` are groups whose members are defined "the other way around". Normally, instead of explicitly specifying the list of members of a well-known identity in its definition, you specify whether a certain identity belongs to a certain well-known in the definition of this "member" identity.

        > For instance, suppose you define a `GROUP` identity called `Everyone`. Rather than ensuring that the list of members in the `Everyone` group definition does indeed include everyone (i.e., all identities), you could ensure that each individual identity includes the `Everyone` identity in its list of `WellKnowns`.

    5.  Send your request.

4.  Push mapped identities:
    1.  Use the following API call:

        ```
        PUT https://push.cloud.coveo.com/v1/organizations/<organizationId>/providers/<providerId>/mappings?orderingId=<orderingId>
        ```

        where you replace `<organizationId>` and `<providerId>` by their real values.

    2.  Include the following headers:

        | Key             | Value                            |
        |-----------------|----------------------------------|
        | `Authorization` | `Bearer <a_valid_API_key value>` |
        | `Content-Type`  | `application/json`               |

    3.  Enter a JSON in a format similar to the following example.

        **Example:**

        All users in the system you are indexing with the push source are employees of your company. All identities have a user name in the form `FirstnameFamilyname` and an email in the form `FirstnameFamilyname@mycompany.com`. You want to ensure that the user names are mapped to their emails so you push mappings similar to the following one for each user.

        ```
        {
            "Identity": {
                "Name": "FirstnameFamilyname",
                "Type": "USER",
                "AdditionalInfo": {}
            },
            "Mappings": [{
                "Name": "FirstnameFamilyname@mycompany.com",
                "Provider": "Email Security Provider",
                "Type": "USER"
                "AdditionalInfo": {}
            }],
            "WellKnowns": [{
                "Name": "Everyone",
                "Type": "GROUP",
                "AdditionalInfo": {}
            }]
        }
        ```

        where the `Provider` value is the name of the security identity provider into which the mapped identity will be pushed.

        > Do not confuse this value with the value of the providerId parameter.

        The `WellKnowns` parameter is optional.

    4.  Send your request.

5.  In the administration console **Security Identities** page, validate that your security identity is pushed to your identity provider, monitoring the number in the **Identities** column increase.

## Deleting a Security Identity from your Identity Provider

1.  Use the following API call:

    ```
    DELETE https://push.cloud.coveo.com/v1/organizations/<organizationId>/providers/<providerId>/permissions
    ```

    where you replace `<organizationId>` and `<providerId>` by their real values.

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
    <td><p><code>Bearer &lt;a_valid_API_key value&gt;</code></p></td>
    </tr>
    <tr class="even">
    <td><code>Content-Type</code></td>
    <td><code>application/json</code></td>
    </tr>
    </tbody>
    </table>

3.  Enter a JSON in a format similar to the following example.

    ```
    {
      "Identity": {
        "Name": "identity_name",
        "Type": "USER",
        "AdditionalInfo": {}
      }
    }
    ```

    and replace `identity_name` by the name of the identity that you want to delete.

4.  Send your request.
5.  In the administration console **Security identities** page, validate that your security identity is deleted from your identity provider. 

## Deleting Old Identities

This API call allows all identities older than the orderingId that you got from the previous calls to be deleted from the provider.

1.  Use the following API call:

    ```
    DELETE https://push.cloud.coveo.com/v1/organizations/<organizationId>/providers/<providerId>/permissions/olderthan?orderingId=<orderingId>
    ```

    where you replace `<organizationId>` and `<providerId>` by their real values. The `orderingId` is generated by the previous calls.

    > The `operationId` parameter is still supported.

    > When both `orderingId` and `operationId` (deprecated) are specified, the `orderingId` parameter has precedence over the deprecated` operationId` parameter.

2.  Your call must include the following headers:

    | Key             | Value              |
    |-----------------|--------------------|
    | `Authorization` | `Bearer `          |
    | `Content-Type`  | `application/json` |

3.  Send your request.

4.  Validate that your old identities have been deleted from your identity provider. 

 
