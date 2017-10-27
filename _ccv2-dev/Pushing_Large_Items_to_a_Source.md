---
slug: "103"
layout: content-2-panel
title: Pushing Large Items to a Source
categories: migrated
---

# Pushing Large Items to a Source

The following procedure describes how to add or update large items into a Coveo Cloud V2 push type source using the following APIs:

-   Push API (see [Push API Usage Overview](https://developers.coveo.com/x/toQAAg))
-   Amazon API Gateway (see http://docs.aws.amazon.com/apigateway/api-reference/)

Use this method whenever your compressed (zlib) content is larger than 5 MB.

> Consider reducing this limit when the size of the rest of your uncompressed JSON becomes significant, like if you include hundreds of custom fields.

 

1.  If not already done, add a push type source and create an API key (see Sources - Page).

2.  Get all the required parameters (see [Parameters and API Calls](https://developers.coveo.com/x/QokkAg)).

    1.  Organization and source IDs
    2.  File ID and upload URI

3.  Upload your compressed content to Amazon S3 via Postman.

    1.  Launch Postman.

    2.  Set the method to PUT and enter the `uploadUri` into the **request URL** box as shown in the following example:

        **Example**

        ```
        PUT https://s3.amazonaws.com/coveo-nprod-customerdata/proda/blobstore/mycoveoorg/60e285b1-58ec-5625-c5c4-53cd2434c19f?x-amz-security-token=FQoDYXdzEKX%2Fici...
        ```

        > This call is not available from <https://platform.cloud.coveo.com/docs>.

    3.  Your call must include the following headers:

        | Key                            | Value                      |
        |--------------------------------|----------------------------|
        | `Content-Type`                 | `application/octet-stream` |
        | `x-amz-server-side-encryption` | `AES256`                   |

        > Any mismatch with the expected upload request will result in a generic **403 Access Denied** error.

    4.  The `BODY` is directly your compressed content (see <https://www.getpostman.com/docs/requests#binary>).

    5.  Send your request and ensure it returns a **200 OK** code response.

4.  Push your items from Amazon S3 to your source.
    Use the same call as in the other procedures:

    ```
    PUT https://push.cloud.coveo.com/v1/organizations/<organizationId>/sources/<sourceId>/documents?documentId=<itemUri>
    ```

    where you replace `<organizationId>`, `<sourceId>` and `<itemUri>` with their real values. The `itemUri` must be a unique URI.

    **Example:**

    PUT https://push.cloud.coveo.com/v1/organizations/mycoveoorg/sources/mycoveoorg-rlj7km73nqqmi/documents?documentId=http://mydocument

5.  Your call must include the following headers:

    | Key             | Value                      |
    |-----------------|----------------------------|
    | `Authorization` | `Bearer <a_valid_API_key>` |
    | `Content-Type`  | `application/json`         |

6.  Enter a `BODY` in a format similar to the following example to push a web page:

    **Example**

    ```
    {
        'FileExtension':'.html',
        'CompressedBinaryDataFileId': 'e2e4b52d-c47-4254-a812-4e9d32db0725'
    }
    ```

    where the `CompressedBinaryDataFileId` value is the `fileId`.

7.  Send your request and ensure it returns a `202 Success` response.

8.  Validate that your items are pushed to your source.

    > If you do not see your content in the administration console **Content Browser** page, your request(s) may contain invalid data (see <https://www.getpostman.com/docs/requests>).


