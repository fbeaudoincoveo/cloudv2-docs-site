---
layout: content-2-panel
title: Extension API Reference
categories: migrated
---

# Extension API Reference

**In this topic:**

-   [Extension Resource](#extension-resource)
    -   [Add Extension](#add-extension)
        -   [Command](#command)
            -   [Parameters](#parameters)
            -   [Response codes](#response-codes)
    -   [Update Extension](#update-extension)
        -   [Command](#command)
            -   [Parameters](#parameters)
            -   [Response codes](#response-codes)
    -   [Delete Extension](#delete-extension)
        -   [Command](#command)
            -   [Parameters](#parameters)
            -   [Response codes](#response-codes)
    -   [Get Extensions](#get-extensions)
        -   [Command](#command)
            -   [Parameters](#parameters)
            -   [Response codes](#response-codes)
    -   [Get Extension](#get-extension)
        -   [Command](#command)
            -   [Parameters](#parameters)
            -   [Response codes](#response-codes)
    -   [Get Versions](#get-versions)
        -   [Command](#command)
            -   [Parameters](#parameters)
            -   [Response codes](#response-codes)
    -   [Get Version](#get-version)
        -   [Command](#command)
            -   [Parameters](#parameters)
            -   [Response codes](#response-codes)
-   [JSON Extension](#json-extension)
    -   [Parameters](#parameters)

The Extension API allows developers to add, update and delete Coveo Cloud V2 indexing pipeline extensions (see [Coveo Cloud V2 Indexing Pipeline Extensions](https://developers.coveo.com/x/sAAvAg)).

This topic provides reference information describing available Coveo Cloud V2 Extension API calls.

Note:

> Other Extension API resources:

-   Swagger generated documentation
    The Extension API Swagger generated documentation is particularly useful to test calls.
    Go to <https://platform.cloud.coveo.com/docs> site, and then in the header drop-down list, select **Extension**.

<!-- -->

-   Step by step instructions (see Creating an Indexing Pipeline Extension with the API and Applying an Indexing Pipeline Extension to a Source with the API)

 

All Extension API calls must include the following HTTP headers:

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
<td><p><code>Bearer </code></p>
<p>In the administration console <strong>API Keys</strong> page, add an API key for which you select the <strong>Edit</strong> check box for the <strong>Extensions</strong> privilege (see Add an API key).</p></td>
</tr>
<tr class="even">
<td><code>Content-Type</code></td>
<td><code>application/json</code></td>
</tr>
</tbody>
</table>

## Extension Resource

### Add Extension

This call is used to create an extension for an organization (see [Creating an Indexing Pipeline Extension with the API](https://developers.coveo.com/x/uQIvAg)).

#### Command

```
POST https://platform.cloud.coveo.com/rest/organizations/{organizationId}/extensions extensionModel
```

##### Parameters

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Parameter</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><code>organizationId</code></td>
<td>Unique organization identifier</td>
</tr>
<tr class="even">
<td><code>extensionModel</code></td>
<td><p>The body of the extension to be added</p></td>
</tr>
</tbody>
</table>

##### Response codes

| Code  | Description                                                                                     |
|-------|-------------------------------------------------------------------------------------------------|
| `201` | `Created` - The extension is created.                                                           |
| `401` | `Unauthorized` - The requested resource requires user authentication.                           |
| `403` | `Forbidden` - The supplied authorization token does not allow access to the requested resource. |
| `404` | `Not Found` - The requested resource could not be found.                                        |

### Update Extension

Used to update an existing extension.

#### Command

```
PUT https://platform.cloud.coveo.com/rest/organizations/{organizationId}/extensions/{extensionId} extensionModel
```

##### Parameters

| Parameter        | Description                             |
|------------------|-----------------------------------------|
| `organizationId` | Unique organization identifier          |
| `extensionId`    | Unique extension identifier             |
| `extensionModel` | The body of the extension to be updated |

##### Response codes

| Code  | Description                                                                                     |
|-------|-------------------------------------------------------------------------------------------------|
| `201` | `Created` - The extension is updated.                                                           |
| `401` | `Unauthorized` - The requested resource requires user authentication.                           |
| `403` | `Forbidden` - The supplied authorization token does not allow access to the requested resource. |
| `404` | `Not Found` - The requested resource could not be found.                                        |

### Delete Extension

Used to delete an unused extension.

> Extensions that have been applied to a source cannot be deleted.

#### Command

```
DELETE https://platform.cloud.coveo.com/rest/organizations/{organizationId}/extensions/{extensionId}
```

##### Parameters

| Parameter        | Description                    |
|------------------|--------------------------------|
| `organizationId` | Unique organization identifier |
| `extensionId`    | Unique extension identifier    |

##### Response codes

| Code | Description                                                                                     |
|------|-------------------------------------------------------------------------------------------------|
| 200  | `OK` - The extension is deleted.                                                                |
| 204  | `No Content` - The request does not return any content.                                         |
| 401  | `Unauthorized` - The requested resource requires user authentication.                           |
| 403  | `Forbidden` - The supplied authorization token does not allow access to the requested resource. |

### Get Extensions

Used to get all extensions for an organization.

#### Command

```
GET https://platform.cloud.coveo.com/rest/organizations/{organizationId}/extensions
```

##### Parameters

| Parameter        | Description                    |
|------------------|--------------------------------|
| `organizationId` | Unique organization identifier |

##### Response codes

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
<td><code>200</code></td>
<td><p><code>OK</code> - The request returns all the extensions.</p></td>
</tr>
<tr class="even">
<td><code>401</code></td>
<td><code>Unauthorized</code> - The requested resource requires user authentication.</td>
</tr>
<tr class="odd">
<td><code>403</code></td>
<td><code>Forbidden</code> - The supplied authorization token does not allow access to the requested resource.</td>
</tr>
<tr class="even">
<td><code>404</code></td>
<td><code>Not Found</code> - The requested resource could not be found.</td>
</tr>
</tbody>
</table>

### Get Extension

Used to get a single extension.

#### Command

```
GET https://platform.cloud.coveo.com/rest/organizations/{organizationId}/extensions/{extensionId}
```

##### Parameters

| Parameter        | Description                    |
|------------------|--------------------------------|
| `organizationId` | Unique organization identifier |
| `extensionId`    | Unique extension identifier    |

##### Response codes

| Code  | Description                                                                                     |
|-------|-------------------------------------------------------------------------------------------------|
| `200` | `OK` - The request returns the extension.                                                       |
| `401` | `Unauthorized` - The requested resource requires user authentication.                           |
| `403` | `Forbidden` - The supplied authorization token does not allow access to the requested resource. |
| `404` | `Not Found` - The requested resource could not be found.                                        |

The command returns the source(s) to which the extension is applied.

### Get Versions

Used to get all versions of an extension based on its `extensionId`. Ordered by descending date.

#### Command

```
GET https://platform.cloud.coveo.com/rest/organizations/{organizationId}/extensions/{extensionId}/versions
```

##### Parameters

| Parameter        | Description                    |
|------------------|--------------------------------|
| `organizationId` | Unique organization identifier |
| `extensionId`    | Unique extension identifier    |

##### Response codes

| Code  | Description                                                                                     |
|-------|-------------------------------------------------------------------------------------------------|
| `200` | `OK` - The request returns the extension versions.                                              |
| `401` | `Unauthorized` - The requested resource requires user authentication.                           |
| `403` | `Forbidden` - The supplied authorization token does not allow access to the requested resource. |
| `404` | `Not Found` - The requested resource could not be found.                                        |

### Get Version

Used to get a specific version of an extension.

#### Command

```
GET https://platform.cloud.coveo.com/rest/organizations/{organizationId}/extensions/{extensionId}/versions/{versionId}
```

##### Parameters

| Parameter        | Description                    |
|------------------|--------------------------------|
| `organizationId` | Unique organization identifier |
| `extensionId`    | Unique extension identifier    |
| `versionId`      | Unique version identifier      |

##### Response codes

| Code  | Description                                                                                     |
|-------|-------------------------------------------------------------------------------------------------|
| `200` | `OK` - The request returns the extension version.                                               |
| `401` | `Unauthorized` - The requested resource requires user authentication.                           |
| `403` | `Forbidden` - The supplied authorization token does not allow access to the requested resource. |
| `404` | `Not Found` - The requested resource could not be found.                                        |

## 
JSON Extension

A JSON extension supplied in the call `BODY` represents the structure of the data used to add or update an extension.

```
{
 "content": "string", 
 "description": "string",
 "name": "string",
 "requiredDataStreams": [
 "BODY_TEXT"
 ]
}
```

### Parameters

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
<td><code>name</code></td>
<td><p>The name of the extension</p></td>
</tr>
<tr class="even">
<td><code>description</code></td>
<td><p>The description of the extension</p></td>
</tr>
<tr class="odd">
<td><code>content</code></td>
<td><p>The body of the extension (user script), written in Python using the <code>document</code> object</p></td>
</tr>
<tr class="even">
<td><code>requiredDataStreams</code></td>
<td><p>[Optional] Additional item data that the extension needs to access:</p>
<div class="table-wrap">
<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Name</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><code>BODY_TEXT</code></td>
<td>Used to override the text of the item in postconversion</td>
</tr>
<tr class="even">
<td><code>BODY_HTML</code></td>
<td>Used to override the HTML (Quick View) of the item in postconversion</td>
</tr>
<tr class="odd">
<td><code>THUMBNAIL</code></td>
<td>Used to override the thumbnail of the item in postconversion</td>
</tr>
<tr class="even">
<td><code>DOCUMENT_DATA</code></td>
<td><p>Used to modify the original item either in preconversion or postconversion</p></td>
</tr>
</tbody>
</table>
</div></td>
</tr>
</tbody>
</table>


