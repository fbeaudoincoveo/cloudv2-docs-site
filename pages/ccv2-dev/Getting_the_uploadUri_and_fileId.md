---
layout: content-2-panel
title: Getting the uploadUri and fileId
categories: migrated
---

# Getting the uploadUri and fileId

An `uploadUri` and a `fileId` are respectively an Amazon S3 presigned URL and its associated unique file ID.

You need `uploadUri` and `fileId` values when you want to push a single large compressed item, or push a large number of items to a source (see [Pushing Large Items to a Source](Pushing_Large_Items_to_a_Source) and [Batch Pushing Encrypted Files and Permissions to a Source](Batch_Pushing_Encrypted_Files_and_Permissions_to_a_Source)). 

You can use the [Get a large file container](https://platform.cloud.coveo.com/docs?api=PushApi#!/file/post_organizations_organizationId_files) call to get an `uploadUri` and its corresponding `fileId`:

```
POST https://push.cloud.coveo.com/v1/organizations/{organizationId}/files
Content-Type: application/json
Accept: application/json
Authorization: Bearer MyAccessToken
```

Ensure that:

-   You replace `{organizationId}` in the path by the actual ID of the target Coveo Cloud V2 organization (see [Getting the organizationId](Getting_the_organizationId)).
-   You replace `MyAccessToken` in the `Authorization` header by an access token that grants the **Organization - View** privilege in the target organization (see [Getting Your Coveo Cloud V2 Platform Access Token](Getting_Your_Coveo_Cloud_V2_Platform_Access_Token), [Creating an API Key](Creating_an_API_Key), and [Getting the Privileges of an Access Token](Getting_the_Privileges_of_an_Access_Token)).

The body of a successful response contains the `uploadUri` and the `fileId` along with the headers which are required when sending a PUT request to the `uploadUri`. 

**Example:**

**201 Created**

```
{
  "uploadUri": "https://s3.amazonaws.com/coveo-nprod-customerdata/proda/blobstore/mycoveocloudv2organization/b5e8767e-8f0d-4a89-9095-1127915c89c7[...]",
  "fileId": "b5e8767e-8f0d-4a89-9095-1127915c89c7",
  "requiredHeaders": {
    "x-amz-server-side-encryption": "AES256",
    "Content-Type": "application/octet-stream"
  }
}
```


