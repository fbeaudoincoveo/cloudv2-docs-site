---
slug: "100"
layout: content-2-panel
title: Push API Reference
categories: migrated
---

# Push API Reference

**In this topic:**

-   [Source Resource](#source-resource)
    -   [Set source status](#set-source-status)
        -   [Command](#command)
        -   [Parameters](#parameters)
        -   [Response codes](#response-codes)
-   [Document Resource](#document-resource)
    -   [Add or update single item](#add-or-update-single-item)
        -   [Command](#command)
        -   [Parameters](#parameters)
        -   [Response codes](#response-codes)
    -   [Delete single item (and optionally, its children)](#delete-single-item-(and-optionally,-its-children))
        -   [Command](#command)
        -   [Parameters](#parameters)
        -   [Response codes](#response-codes)
    -   [Delete items older than value](#delete-items-older-than-value)
        -   [Command](#command)
        -   [Parameters](#parameters)
        -   [Response codes](#response-codes)
    -   [Add, update, and/or delete batch of items](#add,-update,-and/or-delete-batch-of-items)
        -   [Command](#command)
        -   [Parameters](#parameters)
        -   [Response codes](#response-codes)
-   [File Resource](#file-resource)
    -   [Get large file container](#get-large-file-container)
        -   [Command](#command)
        -   [Parameters](#parameters)
        -   [Response codes](#response-codes)
-   [Identity Resource](#identity-resource)
    -   [Add or update single identity](#add-or-update-single-identity)
        -   [Command](#command)
        -   [Parameters](#parameters)
        -   [Response codes](#response-codes)
    -   [Delete single identity](#delete-single-identity)
        -   [Command](#command)
        -   [Parameters](#parameters)
        -   [Response codes](#response-codes)
    -   [Delete identities older than value](#delete-identities-older-than-value)
        -   [Command](#command)
        -   [Parameters](#parameters)
        -   [Response codes](#response-codes)
    -   [Add or update single mapped identity](#add-or-update-single-mapped-identity)
        -   [Command](#command)
        -   [Parameters](#parameters)
        -   [Response codes](#response-codes)
    -   [Add, update, and/or delete batch of identities](#add,-update,-and/or-delete-batch-of-identities)
        -   [Command](#command)
        -   [Parameters](#parameters)
        -   [Response codes](#response-codes)
-   [JSON Document](#json-document)
    -   [Supported Data Structure](#supported-data-structure)
    -   [JSON Document Reserved Key Names](#json-document-reserved-key-names)
-   [JSON Identity](#json-identity)
    -   [Parameters](#parameters)
-   [Call Example](#call-example)
    -   [Comparison to Elastic](#comparison-to-elastic)

The Push API allows you to *push* items, permissions, and security identities into a Coveo Cloud V2 index, rather than *pulling* content using standard Coveo connectors and crawlers (see [Using the Push API](Using_the_Push_API)).

This API is especially useful when you need to index content from a cloud or on-premises system for which the Coveo Cloud V2 platform offers no source type.

This topic provides reference information describing the available Push API operations.

Additional Push API resources

-   Swagger generated documentation:
    The Push API Swagger generated documentation is particularly useful to test calls.
    Go to <https://platform.cloud.coveo.com/docs?api=PushApi>.
-   Step by step tutorials (see [Pushing Items to a Source](https://developers.coveo.com/x/iIQAAg) and [Batch Pushing Encrypted Files and Permissions to a Source](Batch_Pushing_Encrypted_Files_and_Permissions_to_a_Source)).

 

All Push API calls must include the following HTTP headers:

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
<td><p><code>Authorization</code></p></td>
<td><p><code>Bearer &lt;a_valid_API_key_or_OAuth2_token&gt;</code></p>
<div class="aui-message success shadowed information-macro">
<p>Tip</p>
<div class="message-content">
<blockquote>
When you create a Push source through the Coveo Cloud V2 administration console to, you can select the <strong>Create an API key</strong> check box to easily get an API key authorized to push content to sources.
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

## Source Resource

Exposes a service to modify the status of a Push source, effectively creating activity logs for this source.

Activities are used to group item operations performed on a given source. The Coveo Cloud V2 administration console uses activity data to provide statistics and information about the inner workings of a source.

### Set source status

Sets the current status of a Push source. This allows you to update the activity logs of the Push source (and consequently, the activity indicators in the Coveo Cloud V2 administration console).

Pushing an "active" source status (i.e., `REBUILD`, `REFRESH`, or `INCREMENTAL`) creates an activity. Pushing the `IDLE` status terminates the ongoing activity and marks it as completed.

Best practice

>  Before adding, updating, or deleting items in a Push source, you should set its status to either `REBUILD`, `REFRESH`, or `INCREMENTAL`, depending on the scale of the update. You should then set its status back to `IDLE` when the update process is over.

#### Command

```
POST https://push.cloud.coveo.com/v1/organizations/<organizationId>/sources/<sourceId>/status?statusType=<statusType>
```

#### Parameters

<table>
<colgroup>
<col width="20%" />
<col width="20%" />
<col width="20%" />
<col width="20%" />
<col width="20%" />
</colgroup>
<thead>
<tr class="header">
<th>Parameter</th>
<th>In</th>
<th>Type</th>
<th>Description</th>
<th>Sample value</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><code>organizationId</code></p></td>
<td>Path</td>
<td>string</td>
<td><p><strong>Required.</strong></p>
<p>The unique identifier of the target Coveo Cloud V2 organization.</p></td>
<td><pre><code>myorganizationid</code></pre></td>
</tr>
<tr class="even">
<td><p><code>sourceId</code></p></td>
<td>Path</td>
<td>string</td>
<td><p><strong>Required.</strong></p>
<p>The unique identifier of the target Push source.</p></td>
<td><pre><code>myorganizationid-veta6vcbq5onxgj5nsiiaske5e</code></pre></td>
</tr>
<tr class="odd">
<td><p><code>statusType</code></p></td>
<td>Query</td>
<td>string (enum)</td>
<td><p><strong>Required.</strong></p>
<p>The status to set the Push source to.</p>
<p>Valid values:</p>
<ul>
<li><p><code>REBUILD</code></p></li>
<li><p><code>REFRESH</code></p></li>
<li><p><code>INCREMENTAL</code></p></li>
<li><p><code>IDLE</code></p></li>
</ul>
<p>Those values are case insensitive.</p></td>
<td><code>REBUILD</code></td>
</tr>
</tbody>
</table>

#### Response codes

See [Troubleshooting Push API Error Codes](Troubleshooting_Push_API_Error_Codes).

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Code</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><code>201</code></p></td>
<td><p><code>Success</code> - An activity of the specified type has been started.</p></td>
</tr>
<tr class="even">
<td><p><code>401</code></p></td>
<td><p><code>Unauthorized</code> - The supplied authorization token is invalid or does not allow access to the required resource.</p></td>
</tr>
<tr class="odd">
<td><code>429</code></td>
<td><code>TooManyRequests</code> - Too many requests have been sent in a given amount of time.</td>
</tr>
<tr class="even">
<td><code>504</code></td>
<td><code>Timeout</code> - The request took too much time to execute.</td>
</tr>
</tbody>
</table>

## Document Resource

Exposes services to add, update, and/or delete items in a Push source.

### Add or update single item

Adds or updates a single item and/or its related permissions in a Push source (see Pushing Items to a Source).

#### Command

 

```
PUT https://push.cloud.coveo.com/v1/organizations/<organizationId>/sources/<sourceId>/documents?documentId=<documentId>
 
{
  <DocumentBody>
}
```

#### Parameters

<table>
<colgroup>
<col width="20%" />
<col width="20%" />
<col width="20%" />
<col width="20%" />
<col width="20%" />
</colgroup>
<thead>
<tr class="header">
<th>Parameter</th>
<th>In</th>
<th>Type</th>
<th>Description</th>
<th>Sample value</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><code>organizationId</code></p></td>
<td>Path</td>
<td>string</td>
<td><p><strong>Required.</strong></p>
<p>The unique identifier of the target Coveo Cloud V2 organization.</p></td>
<td><pre><code>myorganizationid</code></pre></td>
</tr>
<tr class="even">
<td><p><code>sourceId</code></p></td>
<td>Path</td>
<td>string</td>
<td><p><strong>Required.</strong></p>
<p>The unique identifier of the target Push source.</p></td>
<td><pre><code>myorganizationid-veta6vcbq5onxgj5nsiiaske5e</code></pre></td>
</tr>
<tr class="odd">
<td><p><code>documentId</code></p></td>
<td>Query</td>
<td>string</td>
<td><p><strong>Required.</strong></p>
<p>The unique identifier of the item. Must be the item URI.</p></td>
<td><code>http://www.example.com/</code></td>
</tr>
<tr class="even">
<td><p><code>orderingId</code></p></td>
<td>Query</td>
<td>unsigned long</td>
<td><p>A value indicating the order of arrival (the &quot;age&quot;) of the push operation in the index. A lower value, indicates an &quot;older&quot; operation.</p>
<p>By default, the service automatically sets this parameter to the current number of milliseconds since Unix Epoch.</p>
<div class="aui-message hint shadowed information-macro">
<div class="message-content">
<blockquote>
You could manually specify your own <code>orderingId</code> values to ensure that all pushes which are part of a given refresh or rebuild operation are assigned the same <code>orderingId</code>. Doing so would arguably make the <a href="Push_API_Reference">Delete items older than value</a> and <a href="Push_API_Reference">Delete identities older than value</a> operations easier to use and more predictable, since you would know precisely which set of pushes you are deleting. The Coveo for Sitecore integration uses this approach.
</blockquote>
<blockquote>
If you want to refresh a previously pushed item, the new <code>orderingId</code> you provide must be higher than the previous <code>orderingId</code>. Otherwise, the refresh will be rejected.
</blockquote>
</div>
</div>
<p>See <a href="Understanding_the_orderingId_Parameter">Understanding the orderingId Parameter</a>.</p></td>
<td><code>1497448742564</code></td>
</tr>
<tr class="odd">
<td><code>compressionType</code></td>
<td>Query</td>
<td>string (enum)</td>
<td><p>The type of compression, if the content is being pushed as compressed binary data (i.e., the <code>DocumentBody</code> contains a <code>CompressedBinaryData</code> key-value pair).</p>
<p>Possible values are:</p>
<ul>
<li><code>Deflate</code></li>
<li><code>GZip</code></li>
<li><code>LZMA</code></li>
<li><code>Uncompressed</code></li>
<li><code>ZLib</code></li>
</ul>
<p>Those values are case sensitive.</p>
<div class="aui-message warning shadowed information-macro">
<p>Note</p>
<div class="message-content">
<blockquote>
If you specify <code>Uncompressed</code> as a <code>compressionType</code>, the content you push in the <code>CompressedBinaryData</code> attribute of the <code>DocumentBody</code> must still be base64 encoded.
</blockquote>
</div>
</div>
<p>Default value is <code>ZLib</code>.</p></td>
<td><code>GZip</code></td>
</tr>
<tr class="even">
<td><p>DocumentBody</p></td>
<td>Body</td>
<td><a href="Push_API_Reference">DocumentBody</a></td>
<td><p><strong>Required.</strong></p>
<p>The data structure to push.</p>
<p><strong>Model:</strong></p>
<p> See <a href="Push_API_Reference">JSON Document</a>.</p></td>
<td>See <a href="Push_API_Reference">JSON Document</a>.</td>
</tr>
</tbody>
</table>

#### Response codes

See [Troubleshooting Push API Error Codes](Troubleshooting_Push_API_Error_Codes).

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Code</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><code>202</code></p></td>
<td><p><code>Success</code> - The item was successfully pushed into the indexing pipeline.</p>
<div class="aui-message warning shadowed information-macro">
<div class="message-content">
<blockquote>
A <code>202 Success</code> response does not imply that the item was successfully indexed. In fact, the indexing pipeline could still reject the item.
</blockquote>
<blockquote>
Also, remember that processing a push operation can take a variable amount of time (see <a href="Understanding_Push_API_Processing_Delay">Understanding Push API Processing Delay</a>).
</blockquote>
<blockquote>
If you want to know the current status of a push operation, you must consult the source logs.
</blockquote>
</div>
</div></td>
</tr>
<tr class="even">
<td><p><code>400</code></p></td>
<td><p><code>BadRequest</code> - The request contains invalid data.</p></td>
</tr>
<tr class="odd">
<td><p><code>401</code></p></td>
<td><p><code>Unauthorized</code> - The supplied authorization token is invalid or does not allow access to the required resource.</p></td>
</tr>
<tr class="even">
<td><code>413</code></td>
<td><p><code>TooLarge</code> - The request contains an item that is too large to be processed.</p>
<p>In such a case, use the method with the <a href="Push_API_Reference"><code>CompressedBinaryDataFileId</code></a> reserved key to transfer large files.</p></td>
</tr>
<tr class="odd">
<td><code>429</code></td>
<td><code>TooManyRequests</code> - Too many requests have been sent in a given amount of time.</td>
</tr>
<tr class="even">
<td><p><code>504</code></p></td>
<td><p><code>Timeout</code> - The request took too much time to execute.</p></td>
</tr>
</tbody>
</table>

### Delete single item (and optionally, its children)

Deletes a specific item, and optionally its children, from a Push source.

#### Command

 

```
DELETE https://push.cloud.coveo.com/v1/organizations/<organizationId>/sources/<sourceId>/documents?documentId=<documentId>
```

#### Parameters

<table>
<colgroup>
<col width="20%" />
<col width="20%" />
<col width="20%" />
<col width="20%" />
<col width="20%" />
</colgroup>
<thead>
<tr class="header">
<th>Parameter</th>
<th>In</th>
<th>Type</th>
<th>Description</th>
<th>Sample value</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><code>organizationId</code></p></td>
<td>Path</td>
<td>string</td>
<td><p><strong>Required.</strong></p>
<p>The unique identifier of the target Coveo Cloud V2 organization.</p></td>
<td><pre><code>myorganizationid</code></pre></td>
</tr>
<tr class="even">
<td><p><code>sourceId</code></p></td>
<td>Path</td>
<td>string</td>
<td><p><strong>Required.</strong></p>
<p>The unique identifier of the target Push source.</p></td>
<td><pre><code>myorganizationid-veta6vcbq5onxgj5nsiiaske5e</code></pre></td>
</tr>
<tr class="odd">
<td><p><code>documentId</code></p></td>
<td>Query</td>
<td>string</td>
<td><p><strong>Required.</strong></p>
<p>The unique identifier of the item. Must be the item URI.</p></td>
<td><code>http://www.example.com/</code></td>
</tr>
<tr class="even">
<td><p><code>orderingId</code></p></td>
<td>Query</td>
<td>unsigned long</td>
<td><p>A value indicating the order of arrival (the &quot;age&quot;) of the push operation in the index. A lower value, indicates an &quot;older&quot; operation.</p>
<p>By default, the service automatically sets this parameter to the current number of milliseconds since Unix Epoch.</p>
<div class="aui-message hint shadowed information-macro">
<div class="message-content">
<blockquote>
You could manually specify your own <code>orderingId</code> values to ensure that all pushes which are part of a given refresh or rebuild operation are assigned the same <code>orderingId</code>. Doing so would arguably make the <a href="Push_API_Reference">Delete items older than value</a> and <a href="Push_API_Reference">Delete identities older than value</a> operations easier to use and more predictable, since you would know precisely which set of pushes you are deleting. The Coveo for Sitecore integration uses this approach.
</blockquote>
<blockquote>
If you want to refresh a previously pushed item, the new <code>orderingId</code> you provide must be higher than the previous <code>orderingId</code>. Otherwise, the refresh will be rejected.
</blockquote>
</div>
</div>
<p>See <a href="Understanding_the_orderingId_Parameter">Understanding the orderingId Parameter</a>.</p></td>
<td><code>1497448742564</code></td>
</tr>
<tr class="odd">
<td><code>deleteChildren</code></td>
<td>Query</td>
<td>boolean</td>
<td><p>Whether to delete the item children.</p>
<p>Default value is false.</p></td>
<td><code>true</code></td>
</tr>
</tbody>
</table>

#### Response codes

See [Troubleshooting Push API Error Codes](Troubleshooting_Push_API_Error_Codes).

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Code</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><code>202</code></p></td>
<td><p><code>Success</code> - The Push API has sucessfully received the delete request.</p>
<div class="aui-message warning shadowed information-macro">
<div class="message-content">
<blockquote>
A <code>202 Success</code> response does not imply that the items were successfully deleted from the target organization source. In fact, the delete operation could still fail due to invalid parameters.
</blockquote>
<blockquote>
If you want to know the current status of a delete item operation, you must consult the source logs.
</blockquote>
</div>
</div></td>
</tr>
<tr class="even">
<td><p><code>401</code></p></td>
<td><p><code>Unauthorized</code> - The supplied authorization token is invalid or does not allow access to the required resource.</p></td>
</tr>
<tr class="odd">
<td><code>429</code></td>
<td><code>TooManyRequests</code> - Too many requests have been sent in a given amount of time.</td>
</tr>
<tr class="even">
<td><p><code>504</code></p></td>
<td><p><code>Timeout</code> - The request took too much time to execute.</p></td>
</tr>
</tbody>
</table>

### Delete items older than value

Removes all items whose `orderingId` is "older" (lesser) than the specified value from the Push source. You should typically use this method to clean-up deleted items at the end of a `REBUILD` operation (see Set source status).

#### Command

```
DELETE https://push.cloud.coveo.com/v1/organizations/<organizationId>/sources/<sourceId>/documents/olderthan?orderingId=<orderingId>
```

#### Parameters

<table>
<colgroup>
<col width="20%" />
<col width="20%" />
<col width="20%" />
<col width="20%" />
<col width="20%" />
</colgroup>
<thead>
<tr class="header">
<th>Parameter</th>
<th>In</th>
<th>Type</th>
<th>Description</th>
<th>Sample value</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><code>organizationId</code></td>
<td>Path</td>
<td>string</td>
<td><p><strong>Required.</strong></p>
<p>The unique identifier of the target Coveo Cloud V2 organization.</p></td>
<td><pre><code>myorganizationid</code></pre></td>
</tr>
<tr class="even">
<td><code>sourceId</code></td>
<td>Path</td>
<td>string</td>
<td><p><strong>Required.</strong></p>
<p>The unique identifier of the target Push source.</p></td>
<td><pre><code>myorganizationid-veta6vcbq5onxgj5nsiiaske5e</code></pre></td>
</tr>
<tr class="odd">
<td><code>orderingId</code></td>
<td>Query</td>
<td>unsigned long</td>
<td><p>Required.</p>
<p>The unique identifier which determines whether to delete an item. Any item whose <code>orderingId</code> is &quot;older&quot; (lesser) than this value will be removed from the Push source.</p>
<p>See Understanding the orderingId Parameter.</p></td>
<td><code>1497448742564</code></td>
</tr>
<tr class="even">
<td><code>queueDelay</code></td>
<td>Query</td>
<td>unsigned integer</td>
<td><p>A grace period (in minutes) to ensure that all items remaining in the document processing manager (see Coveo Cloud V2 Indexing Pipeline) have been added to the Push source before actually starting the deleting process. This prevents deleted items from inadvertently reappearing in the Push source if they were also being processed by the DPM (because of a REFRESH operation, for instance).</p>
<p>Default value is 15.</p></td>
<td><code>10</code></td>
</tr>
</tbody>
</table>

#### Response codes

See [Troubleshooting Push API Error Codes](Troubleshooting_Push_API_Error_Codes).

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Code</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><code>202</code></td>
<td><p><code>Success</code> - The Push API has successfully received the delete request.</p>
<div class="aui-message warning shadowed information-macro">
<div class="message-content">
<blockquote>
A <code>202 Success</code> response does not imply that the items were successfully deleted from the target organization source. In fact, the delete operation could still fail due to invalid parameters.
</blockquote>
<blockquote>
If you want to know the status of a delete operation, you must consult the source logs.
</blockquote>
</div>
</div></td>
</tr>
<tr class="even">
<td><code>401</code></td>
<td>Unauthorized - The supplied authorization token is invalid or does not allow access to the required resource.</td>
</tr>
<tr class="odd">
<td><code>429</code></td>
<td>TooManyRequests - Too many requests have been sent in a given amount of time.</td>
</tr>
<tr class="even">
<td><code>504</code></td>
<td>Timeout - The request took too much time to execute.</td>
</tr>
</tbody>
</table>

### Add, update, and/or delete batch of items

Adds, updates, and/or deletes a large number of encrypted items in a Push source with a single request (see [Batch Pushing Encrypted Files and Permissions to a Source](Batch_Pushing_Encrypted_Files_and_Permissions_to_a_Source)).

#### Command

```
PUT http://push.cloud.coveo.com/v1/organizations/<organizationId>/sources/<sourceId>/documents/batch?fileId=<fileId>
```

#### Parameters

<table>
<colgroup>
<col width="20%" />
<col width="20%" />
<col width="20%" />
<col width="20%" />
<col width="20%" />
</colgroup>
<thead>
<tr class="header">
<th>Parameter</th>
<th>In</th>
<th>Type</th>
<th>Description</th>
<th>Sample value</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><code>organizationId</code></td>
<td>Path</td>
<td>string</td>
<td><p><strong>Required.</strong></p>
<p>The unique identifier of the target Coveo Cloud V2 organization.</p></td>
<td><pre><code>myorganizationid</code></pre></td>
</tr>
<tr class="even">
<td><code>sourceId</code></td>
<td>Path</td>
<td>string</td>
<td><p><strong>Required.</strong></p>
<p>The unique identifier of the target Push source.</p></td>
<td><pre><code>myorganizationid-veta6vcbq5onxgj5nsiiaske5e</code></pre></td>
</tr>
<tr class="odd">
<td><code>fileId</code></td>
<td>Query</td>
<td>string</td>
<td><p><strong>Required.</strong></p>
<p>The unique identifier of the file.</p>
<p>You can get this identifier using the <a href="Push_API_Reference">Get a large file container</a> method.</p></td>
<td><code>d22778ca-7f42-4e13-9d9a-47d01bce866c</code></td>
</tr>
<tr class="even">
<td><code>orderingId</code></td>
<td>Query</td>
<td>unsigned long</td>
<td><p>A value indicating the order of arrival (the &quot;age&quot;) of the push operation in the index. A lower value, indicates an &quot;older&quot; operation.</p>
<p>By default, the service automatically sets this parameter to the current number of milliseconds since Unix Epoch.</p>
<div class="aui-message hint shadowed information-macro">
<div class="message-content">
<blockquote>
You could manually specify your own <code>orderingId</code> values to ensure that all pushes which are part of a given refresh or rebuild operation are assigned the same <code>orderingId</code>. Doing so would arguably make the <a href="Push_API_Reference">Delete items older than value</a> and <a href="Push_API_Reference">Delete identities older than value</a> operations easier to use and more predictable, since you would know precisely which set of pushes you are deleting. The Coveo for Sitecore integration uses this approach.
</blockquote>
<blockquote>
If you want to refresh a previously pushed item, the new <code>orderingId</code> you provide must be higher than the previous <code>orderingId</code>. Otherwise, the refresh will be rejected.
</blockquote>
</div>
</div>
<p>See <a href="Understanding_the_orderingId_Parameter">Understanding the orderingId Parameter</a> .</p></td>
<td><code>1497448742564</code></td>
</tr>
</tbody>
</table>

#### Response codes

See [Troubleshooting Push API Error Codes](Troubleshooting_Push_API_Error_Codes).

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Code</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><code>202</code></td>
<td><p><code>Success</code> - The batch of items was successfully pushed into the indexing pipeline.</p>
<div class="aui-message warning shadowed information-macro">
<div class="message-content">
<blockquote>
A <code>202 Success</code> response does not imply that the entire batch of items was successfully indexed. In fact, the indexing pipeline could still reject some, or all of the items.
</blockquote>
<blockquote>
Also, remember that processing a push operation can take a variable amount of time (see <a href="Understanding_Push_API_Processing_Delay">Understanding Push API Processing Delay</a>).
</blockquote>
<blockquote>
If you want to know the current status of a push operation, you must consult the source logs.
</blockquote>
</div>
</div></td>
</tr>
<tr class="even">
<td><code>400</code></td>
<td>BadRequest - The request contains invalid data.</td>
</tr>
<tr class="odd">
<td><code>401</code></td>
<td>Unauthorized - The supplied authorization token is invalid or does not allow access to the required resource.</td>
</tr>
<tr class="even">
<td><code>413</code></td>
<td>TooLarge - The request is too large to be processed.</td>
</tr>
<tr class="odd">
<td><code>429</code></td>
<td><code>TooManyRequests</code> - Too many requests have been sent in a given amount of time.</td>
</tr>
<tr class="even">
<td><code>504</code></td>
<td><code>Timeout</code> - The request took too must time to execute.</td>
</tr>
</tbody>
</table>

## File Resource

Exposes a service to get access to a private, encrypted Amazon S3 file container.

### Get large file container

Gets a presigned Amazon S3 `uploadUri`, as well as a unique `fileId`.

The `uploadUri` grants you access to a private, encrypted Amazon S3 file container where you can safely upload content you wish to push into a Coveo Cloud V2 index. Once the content has been successfully pushed into the Coveo Cloud V2 indexing pipeline, the Amazon S3 file container is automatically deleted.

Note

> The `uploadUri` expires after 60 minutes.

Using this method is necessary when you need to push a single large item (5 MB or more), or a batch of items and/or permissions (see [Batch Pushing Encrypted Files and Permissions to a Source](Batch_Pushing_Encrypted_Files_and_Permissions_to_a_Source)).

#### Command

```
POST http://push.cloud.coveo.com/v1/organizations/<organizationId>/files
```

#### Parameters

<table>
<colgroup>
<col width="25%" />
<col width="25%" />
<col width="25%" />
<col width="25%" />
</colgroup>
<thead>
<tr class="header">
<th>Parameter</th>
<th>In</th>
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><code>organizationId</code></td>
<td>Path</td>
<td>string</td>
<td><p><strong>Required.</strong></p>
<p>The unique identifier of the target Coveo Cloud V2 organization.</p></td>
</tr>
</tbody>
</table>

#### Response codes

See [Troubleshooting Push API Error Codes](Troubleshooting_Push_API_Error_Codes).

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Code</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><code>201</code></td>
<td><p><code>Success</code> - Access to a private file container was created.</p>
<p><strong>Response schema:</strong></p>
<div class="table-wrap">
<table>
<thead>
<tr class="header">
<th>Attribute</th>
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><code>uploadUri</code></td>
<td>string</td>
<td>The presigned URI of a private, encrypted Amazon S3 file container.</td>
</tr>
<tr class="even">
<td><code>fileId</code></td>
<td>string</td>
<td>The unique identifier of the encrypted Amazon S3 file container.</td>
</tr>
</tbody>
</table>
</div>
<div class="panel" style="border-width: 1px;">
<div class="panelHeader" style="border-bottom-width: 1px;">
<strong>Sample response:</strong>
</div>
<div class="panelContent">
<div class="code panel pdl" style="border-width: 1px;">
<div class="codeContent panelContent pdl">
<pre style="font-size:12px;"><code>{
  &quot;uploadUri&quot; : &quot;https://s3.amazonaws.com/coveo-nprod-customerdata/proda/blobstore/myorganizationid/d22778ca-7f42-4e13-9d9a-47d01bce866c[...]&quot;,
  &quot;fileId&quot; : &quot;d22778ca-7f42-4e13-9d9a-47d01bce866c&quot;
}</code></pre>
</div>
</div>
</div>
</div></td>
</tr>
<tr class="even">
<td><code>401</code></td>
<td><code>Unauthorized</code> - The supplied authorization token is invalid or does not allow access to the required resource.</td>
</tr>
<tr class="odd">
<td><code>429</code></td>
<td><code>TooManyRequests</code> - Too many requests have been sent in a given amount of time.</td>
</tr>
<tr class="even">
<td><code>504</code></td>
<td><code>GatewayTimeout</code> - The request took too much time to execute.</td>
</tr>
</tbody>
</table>

## 
Identity Resource

Exposes services to provision security identity providers in order to be able to resolve external system permissions and items (see Creating an Identity Provider for a Secured Push Type Source and Pushing Identities to an Identity Provider).

### Add or update single identity

Adds or updates a single security identity in a Coveo Cloud V2 security identity provider. 

#### Command

 

```
PUT http://push.cloud.coveo.com/v1/organizations/<organizationId>/providers/<providerId>/permissions
 
{
  <IdentityBody>
}
```

#### Parameters

<table>
<colgroup>
<col width="20%" />
<col width="20%" />
<col width="20%" />
<col width="20%" />
<col width="20%" />
</colgroup>
<thead>
<tr class="header">
<th>Parameter</th>
<th>In</th>
<th>Type</th>
<th>Description</th>
<th>Sample value</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><code>organizationId</code></td>
<td>Path</td>
<td>string</td>
<td><p><strong>Required.</strong></p>
<p>The unique identifier of the target Coveo Cloud V2 organization.</p></td>
<td><pre><code>myorganizationid</code></pre></td>
</tr>
<tr class="even">
<td><code>providerId</code></td>
<td>Path</td>
<td>string</td>
<td><p><strong>Required.</strong></p>
<p>The unique identifier of the target security identity provider.</p></td>
<td><code>MyPushSourceSecurityIdentitiyProvider</code></td>
</tr>
<tr class="odd">
<td><code>orderingId</code></td>
<td>Query</td>
<td>unsigned long</td>
<td><p>A value indicating the order of arrival (the &quot;age&quot;) of the push operation in the index. A lower value, indicates an &quot;older&quot; operation.</p>
<p>By default, the service automatically sets this parameter to the current number of milliseconds since Unix Epoch.</p>
<div class="aui-message hint shadowed information-macro">
<div class="message-content">
<blockquote>
You could manually specify your own <code>orderingId</code> values to ensure that all pushes which are part of a given refresh or rebuild operation are assigned the same <code>orderingId</code>. Doing so would arguably make the <a href="Push_API_Reference">Delete items older than value</a> and <a href="Push_API_Reference">Delete identities older than value</a> operations easier to use and more predictable, since you would know precisely which set of pushes you are deleting. The Coveo for Sitecore integration uses this approach.
</blockquote>
<blockquote>
If you want to refresh a previously pushed item, the new <code>orderingId</code> you provide must be higher than the previous <code>orderingId</code>. Otherwise, the refresh will be rejected.
</blockquote>
</div>
</div>
<p>See <a href="Understanding_the_orderingId_Parameter">Understanding the orderingId Parameter</a>).</p></td>
<td><code>1497448742564</code></td>
</tr>
<tr class="even">
<td><code>IdentityBody</code></td>
<td>Body</td>
<td>IdentityBody</td>
<td><p><strong>Required.</strong></p>
<p>The security identity to add or update.</p>
<p><strong>Model:</strong></p>
<p><strong>IdentityBody</strong></p>
<div class="table-wrap">
<table>
<colgroup>
<col width="25%" />
<col width="25%" />
<col width="25%" />
<col width="25%" />
</colgroup>
<thead>
<tr class="header">
<th>Attribute</th>
<th>Type</th>
<th>Description</th>
<th>Sample value</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><code>Identity</code></td>
<td><a href="Push_API_Reference">Identity</a></td>
<td>The identity.</td>
<td>See <a href="Push_API_Reference">JSON Identity</a>.</td>
</tr>
<tr class="even">
<td><code>Members</code></td>
<td>Array&lt;<a href="Push_API_Reference">Identity</a>&gt;</td>
<td>The list of identities which are part of the identity (assuming the identity is a group).</td>
<td>See <a href="Push_API_Reference">JSON Identity</a>.</td>
</tr>
<tr class="odd">
<td><code>WellKnowns</code></td>
<td>Array&lt;<a href="Push_API_Reference">Identity</a>&gt;</td>
<td><p>The list of security identity roles which the identity belongs to.</p>
<p> <code>WellKnowns</code> can be seen as groups whose members are defined &quot;the other way around&quot;. Normally, instead of explicitly specifying the list of members of a well-known identity in its definition, you specify whether a certain identity belongs to a certain well-known in the definition of this &quot;member&quot; identity.</p>
<p> For instance, suppose you define a <code>GROUP</code> identity called <code>Everyone</code>. Rather than ensuring that the list of members in the <code>Everyone</code> group definition does indeed include everyone (i.e., all identities), you could ensure that each individual identity includes the <code>Everyone</code> identity in its list of <code>WellKnowns</code>.</p></td>
<td>See <a href="Push_API_Reference">JSON Identity</a>.</td>
</tr>
</tbody>
</table>
</div>
<p><strong>Identity</strong></p>
<p>See JSON Identity.</p></td>
<td><div class="code panel pdl" style="border-width: 1px;">
<div class="codeContent panelContent pdl">
<pre style="font-size:12px;"><code>{
  &quot;Identity&quot; : {
    &quot;AdditionalInfo&quot; : {},
    &quot;Type&quot; : &quot;GROUP&quot;,
    &quot;Name&quot; : &quot;UX&quot;
  },
  &quot;Members&quot; : [
    {
      &quot;AdditionalInfo&quot; : {},
      &quot;Type&quot; : &quot;USER&quot;,
      &quot;Name&quot; : &quot;Alice Smith&quot;
    },
    {
      &quot;AdditionalInfo&quot; : {},
      &quot;Type&quot; : &quot;USER&quot;,
      &quot;Name&quot; : &quot;Bob Jones&quot;
    }
  ],
  &quot;WellKnowns&quot; : [
    {
      &quot;AdditionalInfo&quot; : {},
      &quot;Type&quot; : &quot;VIRTUAL_GROUP&quot;,
      &quot;Name&quot; : &quot;Everyone&quot;
    }
  ]
}</code></pre>
</div>
</div></td>
</tr>
</tbody>
</table>

#### Response codes

See [Troubleshooting Push API Error Codes](Troubleshooting_Push_API_Error_Codes).

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Code</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><code>202</code></td>
<td><p>Success - The add or update identity request was successfully forwarded to an intermediary service. When the security cache refreshes, it will query this service to get the updated security identity expansions.</p></td>
</tr>
<tr class="even">
<td><code>400</code></td>
<td>BadRequest - The request contains invalid data.</td>
</tr>
<tr class="odd">
<td><code>401</code></td>
<td>Unauthorized - The supplied authorization token is invalid or does not allow access to the required resource.</td>
</tr>
<tr class="even">
<td><code>413</code></td>
<td><code>TooLarge</code> - The request is too large to be processed.</td>
</tr>
<tr class="odd">
<td><code>429</code></td>
<td><code>TooManyRequests</code> - Too many requests have been sent in a given amount of time.</td>
</tr>
<tr class="even">
<td><code>504</code></td>
<td>Timeout - The request took too much time to execute.</td>
</tr>
</tbody>
</table>

### Delete single identity

Deletes a single security identity from a security identity provider.

#### Command

```
DELETE http://push.cloud.coveo.com/v1/organizations/<organizationId>/providers/<providerId>/permissions
 
{
  <BaseIdentityBody>
}
```

#### Parameters

<table>
<colgroup>
<col width="20%" />
<col width="20%" />
<col width="20%" />
<col width="20%" />
<col width="20%" />
</colgroup>
<thead>
<tr class="header">
<th>Parameter</th>
<th>In</th>
<th>Type</th>
<th>Description</th>
<th>Sample value</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><code>organizationId</code></td>
<td>Path</td>
<td>string</td>
<td><p><strong>Required.</strong></p>
<p>The unique identifier of the target Coveo Cloud V2 organization.</p></td>
<td><pre><code>myorganizationid</code></pre></td>
</tr>
<tr class="even">
<td><code>providerId</code></td>
<td>Path</td>
<td>string</td>
<td><p><strong>Required.</strong></p>
<p>The unique identifier of the target security identity provider.</p></td>
<td><code>MyPushSourceSecurityIdentitiyProvider</code></td>
</tr>
<tr class="odd">
<td><code>orderingId</code></td>
<td>Query</td>
<td>unsigned long</td>
<td><p>A value indicating the order of arrival (the &quot;age&quot;) of the push operation in the index. A lower value, indicates an &quot;older&quot; operation.</p>
<p>By default, the service automatically sets this parameter to the current number of milliseconds since Unix Epoch.</p>
<div class="aui-message hint shadowed information-macro">
<div class="message-content">
<blockquote>
You could manually specify your own <code>orderingId</code> values to ensure that all pushes which are part of a given refresh or rebuild operation are assigned the same <code>orderingId</code>. Doing so would arguably make the <a href="Push_API_Reference">Delete items older than value</a> and <a href="Push_API_Reference">Delete identities older than value</a> operations easier to use and more predictable, since you would know precisely which set of pushes you are deleting. The Coveo for Sitecore integration uses this approach.
</blockquote>
<blockquote>
If you want to refresh a previously pushed item, the new <code>orderingId</code> you provide must be higher than the previous <code>orderingId</code>. Otherwise, the refresh will be rejected.
</blockquote>
</div>
</div>
<p>See <a href="Understanding_the_orderingId_Parameter">Understanding the orderingId Parameter</a>.</p></td>
<td><code>1497448742564</code></td>
</tr>
<tr class="even">
<td><code>BaseIdentityBody</code></td>
<td>Body</td>
<td><a href="Push_API_Reference">Identity</a></td>
<td><p><strong>Required.</strong></p>
<p>The security identity to delete.</p>
<p><strong>Model:</strong></p>
<p>See <a href="Push_API_Reference">JSON Identity</a><strong>.</strong></p></td>
<td><div class="code panel pdl" style="border-width: 1px;">
<div class="codeContent panelContent pdl">
<pre style="font-size:12px;"><code>{
  &quot;AdditionalInfo&quot; : {},
  &quot;Type&quot; : &quot;USER&quot;,
  &quot;Name&quot; : &quot;Alice Smith&quot;
}</code></pre>
</div>
</div></td>
</tr>
</tbody>
</table>

#### Response codes

See [Troubleshooting Push API Error Codes](Troubleshooting_Push_API_Error_Codes).

| Code  | Description                                                                                                                                                                                                 |
|-------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `202` | Success - The delete identity request was successfully forwarded to an intermediary service. When the security cache refreshes, it will query this service to get the updated security identity expansions. |
| `400` | BadRequest - The request contains invalid data.                                                                                                                                                             |
| `401` | Unauthorized - The supplied authorization token is invalid or doesn't allow access to the required resource.                                                                                                |
| `429` | `TooManyRequests` - Too many requests have been sent in a given amount of time.                                                                                                                             |
| `504` | Timeout - The request took too much time to execute .                                                                                                                                                       |

### Delete identities older than value

Deletes all identities which are older than a specified `orderingId` from a security identity provider.

#### Command

```
DELETE http://push.cloud.coveo.com/v1/organizations/<organizationId>/providers/<providerId>/permissions/olderthan?orderingId=<orderingId>
```

#### Parameters

<table>
<colgroup>
<col width="20%" />
<col width="20%" />
<col width="20%" />
<col width="20%" />
<col width="20%" />
</colgroup>
<thead>
<tr class="header">
<th>Parameter</th>
<th>In</th>
<th>Type</th>
<th>Description</th>
<th>Sample value</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><code>organizationId</code></td>
<td>Path</td>
<td>string</td>
<td><p><strong>Required.</strong></p>
<p>The unique identifier of the target Coveo Cloud V2 organization.</p></td>
<td><pre><code>myorganizationid</code></pre></td>
</tr>
<tr class="even">
<td><code>providerId</code></td>
<td>Path</td>
<td>string</td>
<td><p><strong>Required.</strong></p>
<p>The unique identifier of the target security identity provider.</p></td>
<td><code>MyPushSourceSecurityIdentitiyProvider</code></td>
</tr>
<tr class="odd">
<td><code>orderingId</code></td>
<td>Query</td>
<td>unsigned long</td>
<td><p><strong>Required.</strong></p>
<p>The unique identifier which determines whether to delete a security identity. Any identity in the security identity provider whose <code>orderingId</code> is &quot;older&quot; (lesser) than this value will be deleted.</p>
<p>See Understanding the orderingId Parameter.</p></td>
<td><code>1497448742564</code></td>
</tr>
</tbody>
</table>

#### Response codes

| Code  | Description                                                                                                                                                                                                   |
|-------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `202` | Success - The delete identities request was successfully forwarded to an intermediary service. When the security cache refreshes, it will query this service to get the updated security identity expansions. |
| `400` | BadRequest - The supplied authorization token is invalid or doesn't allow access to the required resource.                                                                                                    |
| `429` | `TooManyRequests` - Too many requests have been sent in a given amount of time.                                                                                                                               |
| `504` | Timeout - The request took too much time to execute .                                                                                                                                                         |

### Add or update single mapped identity

Adds or updates a single mapped security identity in a security identity provider.

#### Command

```
PUT http://push.cloud.coveo.com/v1/organizations/<organizationId>/providers/<providerId>/mappings
 
{
  <MappedIdentityBody>
}
```

#### Parameters

<table>
<colgroup>
<col width="20%" />
<col width="20%" />
<col width="20%" />
<col width="20%" />
<col width="20%" />
</colgroup>
<thead>
<tr class="header">
<th>Parameter</th>
<th>In</th>
<th>Type</th>
<th>Description</th>
<th>Sample value</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><code>organizationId</code></td>
<td>Path</td>
<td>string</td>
<td><p><strong>Required.</strong></p>
<p>The unique identifier of the target Coveo Cloud V2 organization.</p></td>
<td><pre><code>myorganizationid</code></pre></td>
</tr>
<tr class="even">
<td><code>providerId</code></td>
<td>Path</td>
<td>string</td>
<td><p><strong>Required.</strong></p>
<p>The unique identifier of the target security identity provider.</p></td>
<td><code>MyPushSourceSecurityIdentitiyProvider</code></td>
</tr>
<tr class="odd">
<td><code>orderingId</code></td>
<td>Query</td>
<td>unsigned long</td>
<td><p>A value indicating the order of arrival (the &quot;age&quot;) of the push operation in the index. A lower value, indicates an &quot;older&quot; operation.</p>
<p>By default, the service automatically sets this parameter to the current number of milliseconds since Unix Epoch.</p>
<div class="aui-message hint shadowed information-macro">
<div class="message-content">
<blockquote>
You could manually specify your own <code>orderingId</code> values to ensure that all pushes which are part of a given refresh or rebuild operation are assigned the same <code>orderingId</code>. Doing so would arguably make the <a href="Push_API_Reference">Delete items older than value</a> and <a href="Push_API_Reference">Delete identities older than value</a> operations easier to use and more predictable, since you would know precisely which set of pushes you are deleting. The Coveo for Sitecore integration uses this approach.
</blockquote>
<blockquote>
If you want to refresh a previously pushed item, the new <code>orderingId</code> you provide must be higher than the previous <code>orderingId</code>. Otherwise, the refresh will be rejected.
</blockquote>
</div>
</div>
<p>See <a href="Understanding_the_orderingId_Parameter">Understanding the orderingId Parameter</a>.</p></td>
<td><code>1497448742564</code></td>
</tr>
<tr class="even">
<td> </td>
<td> </td>
<td>MappedIdentityBody</td>
<td><p><strong>Required.</strong></p>
<p>The target identity, and the list of source identities to map the target identity with.</p>
<p><strong>MappedIdentityBody:</strong></p>
<div class="table-wrap">
<table>
<colgroup>
<col width="25%" />
<col width="25%" />
<col width="25%" />
<col width="25%" />
</colgroup>
<thead>
<tr class="header">
<th>Attribute</th>
<th>Type</th>
<th>Description</th>
<th>Sample value</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><code>WellKnowns</code></td>
<td>Array&lt;<a href="Push_API_Reference">Identity</a>&gt;</td>
<td><p>The list of security identity roles which the target identity belongs to.</p>
<p><code>WellKnowns</code> can be seen as groups whose members are defined &quot;the other way around&quot;. Normally, instead of explicitly specifying the list of members of a well-known identity in its definition, you specify whether a certain identity belongs to a certain well-known in the definition of this &quot;member&quot; identity.</p>
<p>For instance, suppose you define a <code>GROUP</code> identity called <code>Everyone</code>. Rather than ensuring that the list of members in the <code>Everyone</code> group definition does indeed include everyone (i.e., all identities), you could ensure that each individual identity includes the <code>Everyone</code> identity in its list of <code>WellKnowns</code>.</p></td>
<td>See <a href="Push_API_Reference">JSON Identity</a>.</td>
</tr>
<tr class="even">
<td><code>Mappings</code></td>
<td>Array&lt;MappedIdentity&gt;</td>
<td>The list of source identities to map the target identity with.</td>
<td>See <a href="Push_API_Reference">MappedIdentity</a>.</td>
</tr>
<tr class="odd">
<td><code>Identity</code></td>
<td><a href="Push_API_Reference">Identity</a></td>
<td>The identity.</td>
<td>See <a href="Push_API_Reference">JSON Identity</a>.</td>
</tr>
</tbody>
</table>
</div>
<p><strong>Identity:</strong></p>
<p>See JSON Identity.</p>
<p><strong>MappedIdentity:</strong></p>
<div class="table-wrap">
<table>
<colgroup>
<col width="25%" />
<col width="25%" />
<col width="25%" />
<col width="25%" />
</colgroup>
<thead>
<tr class="header">
<th>Attribute</th>
<th>Type</th>
<th>Description</th>
<th>Sample value</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><code>AdditionalInfo</code></td>
<td>object</td>
<td><p>An object which can contain any additional information you wish to provide about the identity in the form of key-value pairs.</p></td>
<td><div class="code panel pdl" style="border-width: 1px;">
<div class="codeContent panelContent pdl">
<pre style="font-size:12px;"><code>{
  &quot;key1&quot; : &quot;value 1&quot;,
  &quot;key2&quot; : &quot;value 2&quot;,
  &quot;keyN&quot; : &quot;value N&quot;
}</code></pre>
</div>
</div></td>
</tr>
<tr class="even">
<td><code>Type</code></td>
<td>string (enum)</td>
<td><p>The type of the identity.</p>
<p>Valid values:</p>
<ul>
<li><code>UNKNOWN</code></li>
<li><code>USER</code><br />
Defines a single user.</li>
<li><code>GROUP</code><br />
Defines an existing group of identities within the indexed system. Individual members of this group can be of any valid identity <code>Type</code> (<code>USER</code>, <code>GROUP</code>, or <code>VIRTUAL_GROUP</code>).</li>
<li><code>VIRTUAL_GROUP</code><br />
Defines a group that does not exist within the indexed system. Mechanically, a <code>VIRTUAL_GROUP</code> is identical to a <code>GROUP</code>.</li>
</ul>
<p>Those values are case sensitive.</p></td>
<td><code>GROUP</code></td>
</tr>
<tr class="odd">
<td><code>Name</code></td>
<td>string</td>
<td>The name of the identity. This name needs to be unique across the entire system.</td>
<td><code>asmith@example.com</code></td>
</tr>
<tr class="even">
<td><code>Provider</code></td>
<td>string</td>
<td><p>The unique identifier of the cascading security identity provider which contains the source identity to map the target identity with.</p>
<div class="aui-message warning shadowed information-macro">
<p>Note</p>
<div class="message-content">
<blockquote>
 You only need to specify a value for this parameter if your security identity provider has multiple cascading providers.
</blockquote>
</div>
</div></td>
<td><code>Email Security Provider</code></td>
</tr>
</tbody>
</table>
</div></td>
<td><div class="code panel pdl" style="border-width: 1px;">
<div class="codeContent panelContent pdl">
<pre style="font-size:12px;"><code>{
  &quot;WellKnowns&quot; : [
    {
      &quot;AdditionalInfo&quot; : {},
      &quot;Type&quot; : &quot;VIRTUAL_GROUP&quot;,
      &quot;Name&quot; : &quot;Everyone&quot;
    }
  ],
  &quot;Mappings&quot; : [
    {
      &quot;AdditionalInfo&quot; : {},
      &quot;Type&quot; : &quot;USER&quot;,
      &quot;Name&quot; : &quot;asmith@example.com&quot;,
      &quot;Provider&quot; : &quot;Email Security Provider&quot;
    }
  ],
  &quot;Identity&quot; : {
    &quot;AdditionalInfo&quot; : {},
    &quot;Type&quot; : &quot;USER&quot;,
    &quot;Name&quot; : &quot;Alice Smith&quot;
  }
}</code></pre>
</div>
</div></td>
</tr>
</tbody>
</table>

#### Response codes

See [Troubleshooting Push API Error Codes](Troubleshooting_Push_API_Error_Codes).

| Code  | Description                                                                                                                                                                                                               |
|-------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `202` | Success - The add or update mapped identity request was successfully forwarded to an intermediary service. When the security cache refreshes, it will query this service to get the updated security identity expansions. |
| `400` | BadRequest - The request contains invalid data.                                                                                                                                                                           |
| `401` | Unauthorized - The supplied authorization token is invalid or doesn't allow access to the required resource.                                                                                                              |
| `413` | TooLarge - The request is too large to be processed.                                                                                                                                                                      |
| `429` | `TooManyRequests` - Too many requests have been sent in a given amount of time.                                                                                                                                           |
| `504` | Timeout - The request took too much time to execute.                                                                                                                                                                      |

### Add, update, and/or delete batch of identities

Adds, updates, and/or deletes a large number of identities in a security identity provider with a single request.

#### Command

```
PUT http://push.cloud.coveo.com/v1/organizations/<organizationId>/providers/<providerId>/permissions/batch?fileId=<fileId>
```

#### Parameters

<table>
<colgroup>
<col width="20%" />
<col width="20%" />
<col width="20%" />
<col width="20%" />
<col width="20%" />
</colgroup>
<thead>
<tr class="header">
<th>Parameter</th>
<th>In</th>
<th>Type</th>
<th>Description</th>
<th>Sample value</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><code>organizationId</code></td>
<td>Path</td>
<td>string</td>
<td><p><strong>Required.</strong></p>
<p>The unique identifier of the target Coveo Cloud V2 organization.</p></td>
<td><pre><code>myorganizationid</code></pre></td>
</tr>
<tr class="even">
<td><code>providerId</code></td>
<td>Path</td>
<td>string</td>
<td><p><strong>Required.</strong></p>
<p>The unique identifier of the target security identity provider.</p></td>
<td><code>MyPushSourceSecurityIdentitiyProvider</code></td>
</tr>
<tr class="odd">
<td><code>fileId</code></td>
<td>Query</td>
<td>string</td>
<td><p><strong>Required.</strong></p>
<p>The unique identifier of the file.</p>
<p>You can get this identifier using the <a href="Push_API_Reference">Get a large file container</a> method.</p></td>
<td><code>d22778ca-7f42-4e13-9d9a-47d01bce866c</code></td>
</tr>
<tr class="even">
<td><code>orderingId</code></td>
<td>Query</td>
<td>unsigned long</td>
<td><p>A value indicating the order of arrival (the &quot;age&quot;) of the push operation in the index. A lower value, indicates an &quot;older&quot; operation.</p>
<p>By default, the service automatically sets this parameter to the current number of milliseconds since Unix Epoch.</p>
<div class="aui-message hint shadowed information-macro">
<div class="message-content">
<blockquote>
You could manually specify your own <code>orderingId</code> values to ensure that all pushes which are part of a given refresh or rebuild operation are assigned the same <code>orderingId</code>. Doing so would arguably make the <a href="Push_API_Reference">Delete items older than value</a> and <a href="Push_API_Reference">Delete identities older than value</a> operations easier to use and more predictable, since you would know precisely which set of pushes you are deleting. The Coveo for Sitecore integration uses this approach.
</blockquote>
<blockquote>
If you want to refresh a previously pushed item, the new <code>orderingId</code> you provide must be higher than the previous <code>orderingId</code>. Otherwise, the refresh will be rejected.
</blockquote>
</div>
</div>
<p>See <a href="Understanding_the_orderingId_Parameter">Understanding the orderingId Parameter</a>.</p></td>
<td><code>1497448742564</code></td>
</tr>
</tbody>
</table>

#### Response codes

See [Troubleshooting Push API Error Codes](Troubleshooting_Push_API_Error_Codes).

| Code  | Description                                                                                                                                                                                                                       |
|-------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `202` | Success - The add, update, and/or delete identity requests were successfully forwarded to an intermediary service. When the security cache refreshes, it will query this service to get the updated security identity expansions. |
| `400` | BadRequest - The request contains invalid data.                                                                                                                                                                                   |
| `401` | Unauthorized - The supplied authorization token is invalid or doesn't allow access to the required resource.                                                                                                                      |
| `413` | TooLarge - The request is too large to be processed.                                                                                                                                                                              |
| `429` | `TooManyRequests` - Too many requests have been sent in a given amount of time.                                                                                                                                                   |
| `504` | Timeout - The request took too much time to execute.                                                                                                                                                                              |

 

## JSON Document

A JSON document supplied in the body of a call represents the structure of the data used to add content into an Index.

The document is a collection of key-value pairs where each key represents a metadata, and each value can be a primitive type (string, a number, a date, etc.) that must match the defined field data type which the metadata will be mapped to.

> Each metadata in the JSON document must be unique. Metadata are case-insensitive (e.g., the Push API considers mykey, MyKey, myKey, MYKEY, etc. as identical).

> This implies that you can never use a reserved keyword as a distinct metadata, even if you somehow alter its case.

### Supported Data Structure

-   Single Value Field

    Single value field can be represented in the form of:

    ```
    "key" : "value"
    ```

-   Multi-Value Field

    Multi-value field can be represented in the form of:

    ```
    "key" : [
      "value1",
      "value2",
      "value3"
    ]
    ```

-   Sub-Object

    Sub-objects are not supported by the Coveo Cloud V2 index:

     

    Sub-objects are not supported

    ```
    "key" : {
      [ ... ]
    }
    ```

### JSON Document Reserved Key Names

<table>
<colgroup>
<col width="25%" />
<col width="25%" />
<col width="25%" />
<col width="25%" />
</colgroup>
<thead>
<tr class="header">
<th>Key</th>
<th>Type</th>
<th>Description</th>
<th>Sample value</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><code>CompressedBinaryData</code></td>
<td>byte</td>
<td><p>The original binary item content, compressed using one of the supported compression types (Deflate, GZip, LZMA, Uncompressed, or ZLib), and then Base64 encoded.</p>
<p>You can use this parameter when you are pushing a compressed binary item (such as XML/HTML, PDF, Word, or binary) whose size is less than 5 MB.</p>
<p>Whenever you are pushing an item whose size is 5 MB or more, use the <code>CompressedBinaryDataFileId</code>property instead.</p>
<p>If you are pushing less than 5 MB of textual (non-binary) content, you can use the <code>Data</code> property instead.</p></td>
<td><code>eJxzrUjMLchJBQAK4ALN</code></td>
</tr>
<tr class="even">
<td><code>CompressedBinaryDataFileId</code></td>
<td>string</td>
<td><p>The Amazon S3 key which uniquely identifies the file container where the original compressed (Deflate, GZip, LZMA, Uncompressed, or ZLib) binary item content has been uploaded.</p>
<p>You can get this key using the <a href="Push_API_Reference">Get large file container</a> method.</p>
<p>Whenever you are pushing compressed binary items (such as XML/HTML, PDF, Word, or binary) whose size is 5 MB and over, you should use this property rather than <code>CompressedBinaryData</code>.</p>
<p>If you are pushing less than 5 MB of textual (non-binary) content, you can use the <code>Data</code> property instead.</p>
<p>In summary, using this key involves three distinct calls (see <a href="Pushing_Items_to_a_Source">Pushing Items to a Source</a>):</p>
<ol>
<li><p>A POST to get a pre-signed Amazon S3 <code>uploadUri</code> and a <code>fileId</code> (see <a href="Push_API_Reference">Get large file container</a>).</p></li>
<li><p>A PUT to the <code>uploadUri</code> to push the binary compressed content (not Base64 encoded) of the item to Amason S3.</p></li>
<li><p>A PUT with the <code>documentId</code> being the item URI, and the <code>fileId</code> in the <code>CompressedBinaryDataFileId</code> key.  The Coveo Cloud V2 platform takes care of everything, removing your file from Amazon S3 when the push is completed (see <a href="Push_API_Reference">Add or update single item</a> and <a href="Push_API_Reference">Add, update, and/or delete batch of items</a>). </p></li>
</ol></td>
<td><code>d22778ca-7f42-4e13-9d9a-47d01bce866c</code></td>
</tr>
<tr class="odd">
<td><code>ParendId</code></td>
<td>string</td>
<td><p>The unique identifier (URI) of the parent item. Specifying a value for this key creates a relationship between the attachment item (child) and its parent item. This value also ensures that a parent and all of its attachments will be routed in the same index slice.</p>
<div class="aui-message warning shadowed information-macro">
<p>Note</p>
<div class="message-content">
<blockquote>
The Push API only allows one level of attachment per item (i.e., the Push API does not support attachments within attachments).
</blockquote>
</div>
</div></td>
<td><code>http://www.example.com/</code></td>
</tr>
<tr class="even">
<td><code>FileExtension</code></td>
<td>string</td>
<td><p>The file extension of the data you are pushing. This is useful when pushing a compressed item. The converter uses this information to identify how to correctly process the item.</p>
<p>Values must include the preceding . character</p></td>
<td><p><code>.html</code></p></td>
</tr>
<tr class="odd">
<td><code>Data</code></td>
<td>string</td>
<td><p>The textual (non-binary) content of the item.</p>
<p>Whenever you are pushing a compressed binary item (such as XML/HTML, PDF, Word, or binary), you should use the <code>CompressedBinaryData</code> or <code>CompressedBinaryDataFileId</code> attribute instead, depending on the content size.</p></td>
<td><code>&quot;This domain is established to be used for illustrative examples in documents. You may use this domain in examples without prior coordination or asking for permission.&quot;</code></td>
</tr>
<tr class="even">
<td><code>Permissions</code></td>
<td>array&lt;PermissionsSetsModel&gt;</td>
<td><p>The list of permission sets for this item.</p>
<p>This is useful when item based security is required (i.e., when security is not configured at the source level).</p>
<p><strong>Model:</strong></p>
<p><strong>PermissionsSetsModel</strong></p>
<div class="table-wrap">
<table>
<colgroup>
<col width="25%" />
<col width="25%" />
<col width="25%" />
<col width="25%" />
</colgroup>
<thead>
<tr class="header">
<th>Attribute</th>
<th>Type</th>
<th>Description</th>
<th>Sample value</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><code>AllowAnonymous</code></td>
<td>boolean</td>
<td><p>Whether to allow anonymous users in this permission set.</p>
<p>Default value is <code>false</code>.</p></td>
<td><code>true</code></td>
</tr>
<tr class="even">
<td><code>AllowedPermissions</code></td>
<td>array&lt;PermissionIdentityModel&gt;</td>
<td>The list of allowed permissions for this permission set.</td>
<td>See <a href="Push_API_Reference">PermissionsIdentityModel</a>.</td>
</tr>
<tr class="odd">
<td><code>DeniedPermissions</code></td>
<td>array&lt;PermissionIdentityModel&gt;</td>
<td>The list of denied permissions for this permission set.</td>
<td>See PermissionsIdentityModel.</td>
</tr>
</tbody>
</table>
</div>
<p><strong>PermissionIdentityModel</strong></p>
<div class="table-wrap">
<table>
<colgroup>
<col width="25%" />
<col width="25%" />
<col width="25%" />
<col width="25%" />
</colgroup>
<thead>
<tr class="header">
<th>Attribute</th>
<th>Type</th>
<th>Description</th>
<th>Sample value</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><code>Identity</code></td>
<td>string</td>
<td>The name of the identity. This name needs to be unique across the entire system.</td>
<td><code>asmith@example.com</code></td>
</tr>
<tr class="even">
<td><code>IdentityType</code></td>
<td>string (enum)</td>
<td><p>The type of the identity.</p>
<p>Valid values:</p>
<ul>
<li><code>UNKNOWN</code></li>
<li><code>USER</code><br />
Defines a single user.</li>
<li><code>GROUP</code><br />
Defines an existing group of identities within the indexed system. Individual members of this group can be of any valid identity <code>Type</code> (<code>USER</code>, <code>GROUP</code>, or <code>VIRTUAL_GROUP</code>).</li>
<li><code>VIRTUAL_GROUP</code><br />
Defines a group that does not exist within the indexed system. Mechanically, a <code>VIRTUAL_GROUP</code> is identical to a <code>GROUP</code>.</li>
</ul>
<p>Those values are case insensitive.</p></td>
<td><code>USER</code></td>
</tr>
</tbody>
</table>
</div></td>
<td><div class="code panel pdl" style="border-width: 1px;">
<div class="codeContent panelContent pdl">
<pre style="font-size:12px;"><code>[
  {
    &quot;AllowAnonymous&quot; : false,
    &quot;AllowedPermissions&quot; : [
      {
        &quot;Identity&quot; : &quot;asmith@example.com&quot;,
        &quot;IdentityType&quot; : &quot;USER&quot;
      }
    ],
    &quot;DeniedPermissions&quot; : [
      {
        &quot;Identity&quot; : &quot;deprecated_users,
        &quot;IdentityType&quot; : &quot;GROUP&quot;
      }
    ]
  }
]</code></pre>
</div>
</div></td>
</tr>
</tbody>
</table>

In addition, the following key names are also reserved:

-   `documentId`
    The unique identifier of the item. Must be the item URI.

    If you are pushing a single item, it is useless to specify a value for this key, since documentId is a required query parameter for this call (see Add or update single item). Nevertheless, if you specify a value for this key in the DocumentBody, you must ensure this value precisely matches that of the documentId query string parameter.

    Specifying a value for this key only becomes necessary when you are pushing a batch of items (see Add, update, and/or delete batch of items).

-   `orderingId`

    A value indicating the order of arrival of the push operation in the index.

    By default, the service automatically sets this parameter to the current number of milliseconds since Unix Epoch when the push operation is made.

    > You could manually specify your own `orderingId` values to ensure that all pushes which are part of a given refresh or rebuild operation are assigned the same `orderingId`. Doing so would arguably make the [Delete items older than value](Push_API_Reference) and [Delete identities older than value](Push_API_Reference) operations easier to use and more predictable, since you would know precisely which set of pushes you are deleting. The Coveo for Sitecore integration uses this approach.

    > If you want to refresh a previously pushed item, the new `orderingId` you provide must be higher than the previous `orderingId`. Otherwise, the refresh will be rejected.

## JSON Identity

A JSON identity supplied in the call BODY represents the structure of the data used to add/update/delete a unique security identity into an identity provider.

**Example:**

```
{
  "Name" : "Alice Smith",
  "Type" : "USER",
  "AdditionalInfo": {
    "key1" : "value 1",
    "key2" : "value 2",
    "keyn" : "value n"
  }
}
```

### Parameters

<table>
<colgroup>
<col width="25%" />
<col width="25%" />
<col width="25%" />
<col width="25%" />
</colgroup>
<thead>
<tr class="header">
<th>Attribute</th>
<th>Type</th>
<th>Description</th>
<th>Sample value</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><code>AdditionalInfo</code></td>
<td>object</td>
<td><p>An object which can contain any additional information you wish to provide about the identity in the form of key-value pairs.</p></td>
<td><div class="code panel pdl" style="border-width: 1px;">
<div class="codeContent panelContent pdl">
<pre style="font-size:12px;"><code>{
  &quot;key1&quot; : &quot;value 1&quot;,
  &quot;key2&quot; : &quot;value 2&quot;,
  &quot;keyN&quot; : &quot;value N&quot;
}</code></pre>
</div>
</div></td>
</tr>
<tr class="even">
<td><code>Type</code></td>
<td>string (enum)</td>
<td><p>The type of the identity.</p>
<p>Valid values:</p>
<ul>
<li><code>UNKNOWN</code><br />
Defines an identity whose type is unknown.</li>
<li><code>USER</code><br />
Defines a single user.</li>
<li><code>GROUP</code><br />
Defines an existing group of identities within the indexed system. Individual members of this group can be of any valid identity <code>Type</code> (<code>UNKNOWN</code>, <code>USER</code>, <code>GROUP</code>, or <code>VIRTUAL_GROUP</code>).</li>
<li><code>VIRTUAL_GROUP</code><br />
Defines a group that does not exist within the indexed system. Mechanically, a <code>VIRTUAL_GROUP</code> is identical to a <code>GROUP</code>.</li>
</ul>
<p>Those values are case insensitive.</p></td>
<td><code>USER</code></td>
</tr>
<tr class="odd">
<td><code>Name</code></td>
<td>string</td>
<td>The name of the identity. This name needs to be unique across the entire system.</td>
<td><code>asmith@example.com</code></td>
</tr>
</tbody>
</table>

## Call Example

```
PUT  http://push.cloud.coveo.com/v1/organizations/mycoveoorg/sources/mycoveoorg-qowj5lnc2lqhm/documents?orderingId=42&documentId=http://www.salesforce.com/org:organization/object:Account/record:00160534000z9v9yAAA
 
{
  "AccountNumber" : 1567,
  "Name" : "Nasdaq",
  "Phone" : "1-212-401-8700",
  "title" : "Nasdaq",
  "Website" : "www.nasdaqonx.com",
  "Industry" : "Finance",
  "CreatedDate" : "2014-05-16T00:51:37.000+0000",
  "BillingStreet" : "165 Broadway",
  "BillingCity" : "New York",
  "BillingState" : "NY",
  "BillingCountry" : "United States",
  "BillingPostalCode" : "10006-1404",
  "Tags" : [
    "Account",
    "Finance"
  ],
  "Data" : "Account information regarding the NASDAQ client",
  "Permissions" : [
    {
      "AllowAnonymous" : false,
      "AllowedPermissions" : [
        {
          "Type" : "VIRTUAL_GROUP",
          "Name" : "ViewAll:Irrelevant:"
        },
        {
          "Type" : "VIRTUAL_GROUP",
          "Name" : "ObjectAccess:ViewAllRecordsProfiles:Account"
        },
          "Type" : "VIRTUAL_GROUP",
          "Name": "ObjectAccess:ReadRecordsProfiles:Account"
        },
        {
          "Type" : "VIRTUAL_GROUP",
          "Name" : "ObjectAccess:ReadRecordsPermissionSets:Account"
        }
      ],
      "DeniedPermissions" : [
        {
          "Type" : "USER",
          "Identity" : "tjones"
        }
      ]
    }
  ]
}
```

### Comparison to Elastic

URIs used by Elastic to manipulate the content of its index has the following format:

```
<REST Verb>  http://<Node>:<Port>/<Index>/<Type>/<ID>
```

Attributes:

-   `<Index>`
    Coveo Cloud V2 offers a single index per organization, thus the `OrganizationId` should be used to represent the destination index.

-   `<Type>`
    Coveo does not have any concept that matches the Elastic `Type` attribute which is used to represent an item type. Coveo uses the `sourceId` to group similar items.

-   &lt;ID&gt;
    Numerical `Id` that is used to uniquely identify an item. Coveo Cloud V2 must use the full URI to uniquely represent an item.

You should also note that no permission concept exists within Elastic, thus the item pushed into it index does not have the Permissions attribute. Everything else matches, though.

```
PUT http://cloud.coveo.com/Salesforce/Account/1
 
{
 "Uri":"http://www.salesforce.com/org:organization/object:Account/record:0016000000z9v9yAAA"
 "AccountNumber":1567
 "Name":"Nasdaq",
 "Phone":"1-212-401-8700",
 "title":"Nasdaq",
 "Website":"www.nasdaqonx.com",
 "Industry":"Finance",
 "CreatedDate":"2014-05-16T00:51:37.000+0000",
 "BillingStreet":"165 Broadway",
 "BillingCity":"New York",
 "BillingState":"NY",
 "BillingCountry":"United States",
 "BillingPostalCode":"10006-1404",
 "Tags":[
     "Account",
     "Finance"
 ],
 "Data":"Account information regarding the NASDAQ client"
}
```


