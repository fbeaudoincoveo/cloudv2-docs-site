---
layout: content-2-panel
title: Parameters and API Calls
categories: migrated
---

# Parameters and API Calls

**In this topic:**

-   [Organization ID](#organization-id)
-   [Source ID](#source-id)
-   [File ID and Upload URI](#file-id-and-upload-uri)

A developer may need to provide a value for the following parameters in order to use Coveo Cloud V2 APIs.

## Organization ID

In the Coveo Cloud V2 administration console **Settings** page, in the **Organization** tab, copy the organization **Organization ID** value.

**Example:**

When the original organization name is **Coveo Search**, the `organizationId` is `coveosearch`.

## Source ID

In the Coveo Cloud V2 administration console **Sources** page:

-   Select the desired source, and then copy the sourceId that appear under the source name.

    **Example:**

    As shown in the following capture for which the original organization name is **Coveo Search**, the `sourceId` for this source is coveosearch-syaj2elbj4nlkwybxgxz2l2bdi.

    ![](attachments/35490354/35455305.png)

     

<!-- -->

-   When you edit your source, you can also copy the sourceId from the administration console URL in the browser address bar.

    **Example:**

    `https://platform.cloud.coveo.com/admin/#coveosearch/content/sources/coveosearch-syaj2elbj4nlkwybxgxz2l2bdi/configuration/`

## File ID and Upload URI

1.  Get the `fileId` from the following Push API call:

    ```
    POST https://push.cloud.coveo.com/v1/organizations/{organizationId}/files
    ```

    where you replace `{organizationId}` with your own organizationId.

2.  Your call must include the following headers:

    | Key             | Value              |
    |-----------------|--------------------|
    | `Authorization` | `Bearer `          |
    | `Content-Type`  | `application/json` |

3.  Send your request.

    It returns a presigned Amazon S3 uploadUri and a fileId.

    **Example**

    ```
    {
      "uploadUri": "https://s3.amazonaws.com/coveo-nprod-customerdata/proda/blobstore/coveosearch/60e285b1-58ec-5625-c5c4-53cd2434c19f?x-amz-security-token=FQoDYXdzEKX%2Fici..."
      "fileId": "60e285b1-58ec-5625-c5c4-53cd2434c19f"
    }
    ```

    > The `uploadUri` is valid only for 1 hour.


