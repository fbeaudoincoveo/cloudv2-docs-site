---
layout: content-2-panel
title: Deleting Items from a Source
categories: migrated
---

# Deleting Items from a Source

**In this topic:**

-   [Deleting Old Items from a Source](#deleting-old-items-from-a-source)

The following procedure describes how to delete items (and if applicable their children) from a Coveo Cloud V2 push type source.

When you want to delete an item along with its children, you must set the deleteChildren parameter to true.

**Example:**

You can use the Push API to delete an email and its attachments.

 

1.  Get your organization and source IDs (see [Parameters and API Calls](https://developers.coveo.com/x/QokkAg)).
2.  Use the following API call:

    ```
    DELETE https://push.cloud.coveo.com/v1/organizations/<organizationId>/sources/<sourceId>/documents?documentId=<itemUri>&orderingId=<orderingId>&deleteChildren=<true|false>
    ```

    where you replace `<organizationId>`, `<sourceId>`, and `<itemUri>` with their real values. The `itemUri` must be a unique URI.

    > The orderingId is used by the indexer to delete all items having a URI starting with the specified pattern.

    > If no value is supplied, a timestamped ordering value is added internally to ensure that changes are performed in the order they were received.

    The deleteChildren parameter default value is false.

3.  Your call must include the following headers:

    | Key           | Value            |
    |---------------|------------------|
    | Authorization | Bearer           |
    | Content-Type  | application/json |

4.  Send your request and ensure it returns a 202 Success response code.

5.  In the administration console **Sources** page, validate that your item and its children are deleted.

## Deleting Old Items from a Source

The following procedure describes how to delete unrefreshed items based on their ordering ID.

Use this method to clean-up deleted items at the end of a Rebuild operation.

Set your source status to `REBUILD`.

1.  Use the following API call:

    ```
    POST https://push.cloud.coveo.com/v1/organizations/<organizationId>/sources/<sourceId>/status?sourceType=<REBUILD>
    ```

    where you replace `<organizationId>` and `<sourceId>` with their real values (see [Parameters and API Calls](https://developers.coveo.com/x/QokkAg)).

2.  Your call must include the following headers:

    | Key             | Value                      |
    |-----------------|----------------------------|
    | `Authorization` | `Bearer <a_valid_API_key>` |
    | `Content-Type`  | `application/json`         |

3.  Send your request and ensure it returns a `201 Success` response code.

4.  In the administration console Sources page, validate that your operation has been started.

Delete all items having an orderingId value lower than the one supplied.
Use the following API call:

```
DELETE https://push.cloud.coveo.com/v1/organizations/<organizationId>/sources/<sourceId>/documents/olderthan?orderingId=<orderingId>
```

where you replace `<organizationId>`, `<sourceId>`, and `<orderingId>` with their real values (see [Parameters and API Calls](https://developers.coveo.com/x/QokkAg)).

Include the same headers as in the previous precedure.

Send your request and ensure it returns a `202 Success` response code.

In the administration console Sources page, validate that your items are deleted.
