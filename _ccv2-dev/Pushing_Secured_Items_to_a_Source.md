---
slug: "104"
layout: content-2-panel
title: Pushing Secured Items to a Source
categories: migrated
---

# Pushing Secured Items to a Source

When you want to push items with permissions, your BODY must also include a Permissions parameter to indicate who (users, groups, or virtual groups) is allowed to view your secured items in Coveo search results.

The following procedure describes how to add or update secured items.

1.  If not already done, add a secured push type source and create an API key (see Sources - Page).
2.  Get the organization and source IDs (see [Parameters and API Calls](https://developers.coveo.com/x/QokkAg)).
3.  Use the following API call:

    ```
    PUT https://push.cloud.coveo.com/v1/organizations/<organizationId>/sources/<sourceId>/documents?documentId=<itemUri>
    ```

    where you replace ,  and  with their real values. The documentId must be a unique URI.

4.  Your call must include the following headers:

    | Key           | Value            |
    |---------------|------------------|
    | Authorization | Bearer           |
    | Content-Type  | application/json |

5.  Enter a BODY in a format similar to the following example to push a web page:

    **Example**

    ```
    {
      "FileExtension":".html", 
      "CompressedBinaryData": encodeddata,
      
      "Permissions": [{
          "PermissionSets": [{
              "AllowAnonymous": false,
              "AllowedPermissions": [{
                  "IdentityType": "User",
                  "Identity": "allowed@coveo.com"
              },
              { ...
              }],
              "DeniedPermissions": [{
                  "IdentityType": "User",
                  "Identity": "denied@coveo.com"
              },
              { ...
              }]
          }]
      }]
    }
    ```

    where the CompressedBinaryData contains the compressed and Base64 encoded content to be indexed for the item.

6.  Send your request and ensure it returns a 202 Success response.

    > If you get a 413 TooLarge error, use the CompressedBinaryDataFileId key (see Pushing Large Items to a Source).

7.  In the administration console **Sources** page, validate that your items are indexed.

#### What's Next

Push identities, group members, and identity mappings to an identity provider (see [Pushing Identities to an Identity Provider](https://developers.coveo.com/x/JoodAg)).
