---
layout: content-2-panel
title: Troubleshooting Push API Error Codes
categories: migrated
---

# Troubleshooting Push API Error Codes

**In this topic:**

-   [400 INVALID\_JSON](#400-invalid_json)
-   [401 UNAUTHORIZED](#401-unauthorized)
-   [401 INVALID\_TOKEN](#401-invalid_token)
-   [403 ACCESS\_DENIED](#403%C2%A0access_denied)
-   [404 ORGANIZATION\_NOT\_FOUND](#404%C2%A0organization_not_found)
-   [412 SOURCE\_DOES\_NOT\_EXIST](#412%C2%A0source_does_not_exist)
-   [412 MISSING\_PARAMETER](#412-missing_parameter)
-   [412 INVALID\_PARAMETER](#412-invalid_parameter)
-   [413 Request Entity Too Large](#413-request-entity-too-large)
-   [415 UNSUPPORTED\_MEDIA\_TYPE](#415%C2%A0unsupported_media_type)
-   [429 TOO\_MANY\_REQUESTS](#429%C2%A0too_many_requests)
-   [50X](#50x)

This topic explains why you may be getting certain error codes when using the Push API, and provides you with some of the most common ways to handle those errors.

## 400 INVALID\_JSON

**Why Am I Getting This Error?**

The body of your Push API call may be incorrectly formatted, or it may lack certain required key-value pairs.

**What Should I Do?**

-   Use a JSON validation tool to ensure that the body of your call is valid JSON.
-   If you are pushing [items](Glossary_37585054.html#Glossary-Item), ensure that the JSON document is correctly formatted (see [Push API Reference - JSON Document](Push-API-Reference_33588348.html#PushAPIReference-PushAPIReference-JSONDocJSONDocument)).

    Reminder

    > The JSON document must not contain any duplicate keys or sub-objects.

-   If you are pushing an uncompressed item, ensure that the JSON document minimally includes the `Data` key-value pair.
-   If you are pushing a small compressed item (less than 5 megabytes), ensure that the JSON document minimally includes the `CompressedBinaryData` key-value pair.
-   If you are pushing a batch of items or a single large compressed item (5 megabytes or more), ensure that the JSON document minimally includes the `CompressedBinaryDataFileId` key-value pair.

## 401 UNAUTHORIZED

**Why Am I Getting This Error?**

You are trying to make an unauthenticated Push API call.

**What Should I Do?**

Ensure that you include the `Authorization: Bearer MyAccessToken` header in your call. Replace `MyAccessToken` with an actual [Coveo Cloud V2 platform](Glossary_37585054.html#Glossary-Cove) OAuth2 token (see [Getting Your Coveo Cloud V2 Platform Access Token](Getting_Your_Coveo_Cloud_V2_Platform_Access_Token)) or API key with the required privileges (see [Creating an API Key](Creating_an_API_Key)).

## 401 INVALID\_TOKEN

**Why Am I Getting This Error?**

The Coveo Cloud V2 platform does not recognize the access token you are using to authenticate your Push API call.

**What Should I Do?**

-   If you are using an OAuth2 token to authenticate your call, this token may be expired. Try again using a fresh Coveo Cloud V2 platform OAuth2 token (see [Getting Your Coveo Cloud V2 Platform Access Token](Getting_Your_Coveo_Cloud_V2_Platform_Access_Token)).
-   If you are using an API key to authenticate your call, this key may have been disabled or deleted in the target [Coveo Cloud V2 organization](Glossary_37585054.html#Glossary-C), or your IP address may not have access to this key. Ask an administrator to modify the API key accordingly, or to create a new API key with the required privileges for you.

## 403 ACCESS\_DENIED

**Why Am I Getting This Error?**

The access token you are using to authenticate your Push API call does not grant you sufficient privileges to perform the operation.

**What Should I Do?**

-   If you are using an OAuth2 token to authenticate your call, your identity probably does not have the required privileges in the target Coveo Cloud V2 organization. Ask an administrator to grant you those privileges. Alternatively, the administrator could create an API key with the required privileges for you.
-   If you are using an API key to authenticate your call, this API key probably does not have the required privileges. Ask an administrator to modify the API key accordingly, or to create a new API key with the required privileges for you.

## 404 ORGANIZATION\_NOT\_FOUND

**Why Am I Getting This Error?**

The Coveo Cloud V2 platform does not recognize the `organizationId` you provided as an argument when making your Push API call.

**What Should I Do?**

Ensure that you have correctly spelled the `organizationId` of the target Coveo Cloud V2 organization (see [Getting the organizationId](Getting_the_organizationId)).

## 412 SOURCE\_DOES\_NOT\_EXIST

**Why Am I Getting This Error?**

The Coveo Cloud V2 platform does not recognize the `sourceId` you provided as an argument when making your Push API call.

**What Should I Do?**

-   Ensure that you have correctly spelled the `sourceId` of the target [source](Glossary_37585054.html#Glossary-Source) (see [Getting the sourceId](Getting_the_sourceId)).

-   Ensure that the source you want to push content into has been successfully created in the target Coveo Cloud V2 organization.

    Reminder

    > Creating the very first source in a new Coveo Cloud V2 organization usually takes around 10 minutes, since this organization needs to be provisioned first.

    > Once the organization has been successfully provisioned, though, creating subsequent sources should only take a few seconds.

## 412 MISSING\_PARAMETER

**Why Am I Getting This Error?**

You did not provide a value for at least one of the required parameters of your Push API call.

**What Should I Do?**

Ensure that you pass a valid argument for all of the required parameters of the call.

## 412 INVALID\_PARAMETER

**Why Am I Getting This Error?**

At least one of the arguments you provided when making your Push API call is invalid.

**What Should I Do?**

Ensure that all arguments you pass when making your call are of the expected type (i.e., boolean, integer, long, etc.).

## 413 Request Entity Too Large

**Why Am I Getting This Error?**

You are trying to perform a push operation whose total size exceeds the allowed limit (see [Push API Limits](Push_API_Limits)).

**What Should I Do?**

-   If you are pushing a single compressed or uncompressed item whose size exceeds 5 megabytes, use a large file container to push the item, rather than directly providing its `Data` or `CompressedBinaryData` in the body of the call (see [Pushing Large Items to a Source](Pushing_Large_Items_to_a_Source)).
-   If you are pushing a batch of items whose total size exceeds 256 megabytes, try pushing smaller batches.
-   If you are using a large file container to push a single large item whose uncompressed size exceeds 256 megabytes, try compressing the item using one of the supported algorithms (Deflate, GZip, LZMA, or ZLib) before pushing it again.

## 415 UNSUPPORTED\_MEDIA\_TYPE

**Why Am I Getting This Error?**

You are trying to make a Push API call using the wrong content type.

**What Should I Do?**

In most cases, ensure that you include the `Content-Type: application/json` header when making your call. The only exception is when you are uploading content to an AWS container. In this specific case, you must include the `Content-Type: application/octet-stream` and `x-amz-server-side-encryption: AES256` headers instead.

## 429 TOO\_MANY\_REQUESTS

**Why Am I Getting This Error?**

You have exceeded the maximum number of Push API calls you can make in a given amount of time. Consequently, your calls are now being throttled by the service. If you are getting this error when pushing batches of items, it is also possible that some your calls are being throttled by AWS (see[Error Handling Patterns in API Gateway and AWS Lambda](https://aws.amazon.com/blogs/compute/error-handling-patterns-in-amazon-api-gateway-and-aws-lambda/)). In any case, your code is probably trying to push items too fast.

**What Should I Do?**

Wait until your calls are no longer being throttled before using the service again (this may take up to a week). In the future, ensure that you make Push API calls at a slower pace (see [Push API limits](Push_API_Limits)).

## 50X

**Why Am I Getting This Error?**

You have triggered an unhandled error, or there is an issue with the Push API service itself, or with AWS (see[ Error Handling Patterns in API Gateway and AWS Lambda](https://aws.amazon.com/blogs/compute/error-handling-patterns-in-amazon-api-gateway-and-aws-lambda/)).

**What Should I Do?**

-   If you are obviously not responsible for the error, try performing the operation again. AWS issues typically resolve themselves within a few moments.
-   You can monitor the status of Coveo Cloud V2 platform services from [status.cloud.coveo.com](http://status.cloud.coveo.com).

