---
slug: "64"
layout: content-2-panel
title: Document Object Python API Reference
categories: migrated
---

# Document Object Python API Reference

**In this topic:**

-   [Get URI](#get-uri)
-   [Get Metadata](#get-metadata)
-   [Get Metadata Value](#get-metadata-value)
    -   [Parameters](#parameters)
-   [Add Metadata](#add-metadata)
-   [Log](#log)
    -   [Parameters](#parameters)
    -   [Script Example](#script-example)
    -   [Output](#output)
-   [Get Permissions](#get-permissions)
-   [Clear Permissions](#clear-permissions)
-   [Add Allowed Permission](#add-allowed-permission)
    -   [Parameters](#parameters)
-   [Add Denied Permission](#add-denied-permission)
    -   [Parameters](#parameters)
-   [Set Permissions](#set-permissions)
-   [Get Data Streams](#get-data-streams)
    -   [Parameters](#parameters)
-   [Add Data Stream](#add-data-stream)
-   [Reject](#reject)
-   [Document Object JSON Schema](#document-object-json-schema)

Creating an indexing pipeline extension implies writing Python code that uses the `document` object to manipulate item properties (see Creating an Indexing Pipeline Extension with the API and Coveo Cloud V2 Indexing Pipeline). 

This topic provides reference information describing the object methods and their parameters.

## Get URI

This method is used to get the item URI.

```
document.uri
```

## Get Metadata

This method is used to get all item metadata.

```
document.get_meta_data()
```

It returns a list of `MetaDataValue` objects (see [Document Object JSON Schema](Document_Object_Python_API_Reference)).

```
[MetaDataValue]
```

## Get Metadata Value

Used to get a metadata for a given origin.

```
document.get_meta_data_value('name', 'origin', True|False)
```

### Parameters

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
<td><code>name</code></td>
<td>The name of the metadata</td>
</tr>
<tr class="even">
<td><code>origin</code></td>
<td><p>[Optional] The metadata value set by either one of the following components:</p>
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
<td><code>crawler</code></td>
<td><p>The metadata value set during the Crawling stage</p></td>
</tr>
<tr class="even">
<td><code>converter</code></td>
<td>The metadata value set during the Processing stage</td>
</tr>
<tr class="odd">
<td><code>mapping</code></td>
<td><p>The metadata value set during the Mapping stage</p></td>
</tr>
</tbody>
</table>
</div>
<p>If no value is supplied and the reverse value is <code>True</code>, the most recent origin is considered, i.e. <code>crawler</code> in preconversion and <code>mapping</code> in postconversion.</p></td>
</tr>
<tr class="odd">
<td><code>reverse</code></td>
<td><p>[Optional] Boolean used to determine whether to get the metadata origin in reverse order or not. The default value is <code>True</code>, meaning that the value is fetched from the latest indexing pipeline stage with a non-empty value.</p></td>
</tr>
</tbody>
</table>

It returns a list of strings.

```
[strings]
```

## Add Metadata

Used to add an item metadata.

Replace `metadata_name` and `metadata_value` with the chosen values.

```
document.add_meta_data({'metadata_name':'metadata_value'})
```

Used to unset an item metadata.

```
document.add_meta_data({'metadata_name':''})
```

## Log

Use this method in your extension script to tag source items with a relevant indexing message that is sent to the Coveo Cloud V2 source logs. Log messages are useful when you want to edit, debug or troubleshoot an extension scripts. For instance, it is a common practice to use the try/catch or try/except block to log an error as a string in the source logs. It is recommended to use the `Log` method since outputting text to a field as a form of logging can be a serious index bloat. For instance, using the [Get Metadata](Document_Object_Python_API_Reference) method to output the metadata content to a field is a bad practice.

```
log(message, severity='Normal')
```

### Parameters

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th>Parameter</th>
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><code>message</code></td>
<td><strong>Required</strong>: string</td>
<td><p>The message that you want to log when applying an extension script.</p></td>
</tr>
<tr class="even">
<td><code>severity</code></td>
<td>string</td>
<td><p>Optionaly used to indicate the message severity type.</p>
<p>Default value is <code>Normal</code>.</p>
<p>The allowed case insensitive severity values are:</p>
<ul>
<li><code>Debug</code></li>
<li><code>Detail</code></li>
<li><code>Error</code></li>
<li><code>Fatal</code></li>
<li><code>Important</code></li>
<li><code>Normal</code></li>
<li><code>Notification</code></li>
<li><code>Warning</code></li>
</ul></td>
</tr>
</tbody>
</table>

### Script Example

This script example uses the `Log` method twice. First, the `try` block modifies the metadata before logging a success message. When the `try` block fails, the `except` block catches the exception and sends a log containing the error message.

```
fulltitle = document.get_meta_data_value('titleselection','crawler',True);
  
try:
    # modifying fulltitle variable
    fulltitle = fulltitle[0]
  
    # logging a meaningful success message
    log('added metadata value to title: ' + fulltitle)
  
# catching all exceptions and logging them as a string for debugging purposes
except Exception as e:
    log(str(e),'Error')
```

### Output

In the preceding extension script, the first occurrence of the `Log` method is called when the script runs without raising an error. In this particular case, the second argument is missing as the default value `Normal` is used to define the log message severity. The log message generated by the extension script can be seen in an added subsection named **Logs**.

![](attachments/37585540/37552631.png)

In the preceding extension script, the second occurrence of the `Log` method is called when an exception is raised. This exception is caught and sends a message to document the error in the **Logs** subsection.

![](attachments/36635449/37552626.png)

> Applying an extension populates the documentLogEntries.meta.logs field that contains all log messages and severity type strings. This field length is limited to approximately 4K characters, after which the content is truncated. When the added length of multiple log messages gets over the limit, it is still possible to view all the messages that fits within the limit but the log message that sits on the limit is replaced with a truncated... mention as the following messages are ignored. For instance, when a very long string gets over the limit, even if it represents the one and only log that applies to your extension, the whole string is replaced with the truncated... mention.

```
{
    "documentLogEntries": [
        {
            "id": "http://www.example.com/",
            "organizationId": "myorganization",
            "sourceId": "qqotfbbttohttrnva4ebwykbe4-myorganization",
            "resourceId": "myorganization-tb5qadfyqqv2mrdtn2gde5kcpi",
            "task": "EXTENSION",
            "operation": "ADD",
            "result": "COMPLETED",
            "datetime": "2017-08-17T13:01:36.852Z",
            "requestId": "976520a8-f569-45d9-b252-48e6aea544d5",
            "meta": {
                "duration": "0.0559999",
                "logs": "truncated..."
            }
        }
    ]
}
```

> ![](attachments/36635449/37552845.png)

## Get Permissions

Used to get all item permissions.

```
document.get_permissions()
```

It returns a list of `PermissionLevel` objects (see [Document Object JSON Schema](Document_Object_Python_API_Reference)).

```
[PermissionLevel]
```

## Clear Permissions

Used to clear all item permissions.

```
document.clear_permissions()
```

## Add Allowed Permission

Used to add an allowed security identity.

```
document.add_allowed('identity', 'identity_type', 'security_provider', {})
```

### Parameters

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
<td><code>identity</code></td>
<td>The name of the allowed security identity to add</td>
</tr>
<tr class="even">
<td><code>identity_type</code></td>
<td><p>The security identity type can be:</p>
<ul>
<li><code>user</code></li>
<li><code>group</code></li>
<li><code>virtualgroup</code></li>
<li><code>unknown</code></li>
</ul></td>
</tr>
<tr class="odd">
<td><code>security_provider</code></td>
<td>The name of the security identity provider</td>
</tr>
<tr class="even">
<td><code>additional_info</code></td>
<td>A collection of key value pairs that can be used to uniquely identify the security identity.</td>
</tr>
</tbody>
</table>

## Add Denied Permission

Used to add a denied security identity.

```
document.add_denied('identity', 'identity_type', 'security_provider', {})
```

### Parameters

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
<td><code>identity</code></td>
<td>The name of the denied security identity to add</td>
</tr>
<tr class="even">
<td><code>identity_type</code></td>
<td><p>The security identity type can be:</p>
<ul>
<li><code>user</code></li>
<li><code>group</code></li>
<li><code>virtualgroup</code></li>
<li><code>unknown</code></li>
</ul></td>
</tr>
<tr class="odd">
<td><code>security_provider</code></td>
<td>The name of the security identity provider</td>
</tr>
<tr class="even">
<td><code>additional_info</code></td>
<td>A collection of key value pairs that can be used to uniquely identify the security identity.</td>
</tr>
</tbody>
</table>

## Set Permissions

Used to set item permissions.

```
document.set_permissions([permission_levels])
```

The permission model complexity can range from allowing full anonymous access to requiring the resolution of permissions for several permission levels, each containing one or more permissions sets.

**Example**

```
level1 = document.PermissionLevel(
    name='level_name',
    permission_sets=[
        # Allow everyone (*@*) to access the item
        document.PermissionSet(
            name='set_name',
            allow_anonymous=False,
            allowed_permissions=[
                document.Permission(
                    identity='*@*',
                    identity_type='user',
                    security_provider='Email Security Provider'
                )
            ]
        )
    ]
)
level2 = document.PermissionLevel(
    name='level_name',
    permission_sets=[
        # Allow a specific group to access the item
        document.PermissionSet(
            name='set_name',
            allow_anonymous=False,
            allowed_permissions=[
                document.Permission(
                    identity='Developers1',
                    identity_type='group',
                    security_provider='Email Security Provider'
                )
            ]
        ),
        # Allow anonymous users to access the item
        document.PermissionSet(
            name='set_name',
            allow_anonymous=True,
            denied_permissions=[
                document.Permission(
                    identity='Developers2',
                    identity_type='group',
                    security_provider='Email Security Provider'
                )
            ]
        )
    ]
)
# Set item permissions
document.set_permissions([level1, level2])
```

## Get Data Streams

You can optionally read an item data streams in cases where you need to read or modify these streams. Include and process a data stream only when you need it to optimize indexing performances.  

Used to get the item data streams. 

```
document.get_data_streams()
```

Used to get a data stream for a given origin.

```
document.get_data_stream('name', 'origin', True|False)
```

Tip:

>  For Web and Sitemap type sources, it is recommended to use the web scrapping feature rather than extensions to do common HTML content processing such as excluding sections and extracting metadata (see [Web Scraping Configuration](http://www.coveo.com/go?dest=cloudhelp&lcid=9&context=277)).

### Parameters

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
<td>name</td>
<td><p>The available item data streams are:</p>
<ul>
<li><p><code>documentdata</code>The complete item binary content extracted by the Crawling stage of the indexing pipeline (see Coveo Cloud V2 Indexing Pipeline).</p>
<div class="panel" style="border-width: 1px;">
<div class="panelHeader" style="border-bottom-width: 1px;">
<strong>Example:</strong>
</div>
<div class="panelContent">
<p>The documentdata of a PDF file is the actual PDF file.</p>
<p>The documentdata of a web page is the page HTML markup.</p>
</div>
</div>
<p>You may want to retrieve the documentdata of an item in a Preconversion extension in rare cases where you want to modify the original item content.</p>
<div class="panel" style="border-width: 1px;">
<div class="panelHeader" style="border-bottom-width: 1px;">
<strong>Example:</strong>
</div>
<div class="panelContent">
You indexed scanned items that are saved as image files. You want to index the text content of the images. You use a preconversion extension to read each image <code>documentdata</code>, send it to a third party optical character recognition service (OCR) service, and save the returned text back in the documentdata so that the Processing stage can prepare the text content for the Indexing stage.
</div>
</div>
<p>Getting the <code>documentdata</code> can significantly degrade indexing performances because each item binary data has to be fetched, decompressed, and decrypted.<br />
There is generally no point to get and modify the <code>documentdata</code> in a postconversion extension because the Indexing stage does not process it.</p>
<div class="aui-message hint shadowed information-macro">
<div class="message-content">
<blockquote>
In the Coveo Cloud administration console <strong>Add/Edit an Extension</strong> panel, the documentdata is referred to as the <strong>Original file</strong>.
</blockquote>
</div>
</div></li>
<li><p><code>body_text</code><br />
The complete textual content of an item extracted by the converter in the Processing stage of the indexing pipeline (see <a href="http://www.coveo.com/go?dest=cloudhelp&amp;lcid=9&amp;context=336">Coveo Cloud V2 Indexing Pipeline</a> ).<br />
You can get the <code>body_text</code> of each item in a postconversion extensions for rare cases where you want to access and possibly modify the item text content.<br />
There is no point in getting and modifying the <code>body_text</code> in a preconversion extension because the Processing stage would overwrite it.</p>
<div class="aui-message hint shadowed information-macro has-no-icon">
<p>Note:</p>
<div class="message-content">
<blockquote>
For index size and performance optimization, the <code>body_text</code> is limited in size to 50 MB. This means that for rare items with larger <code>body_text</code>, the exceeding text will not be indexed, and therefore not searchable.
</blockquote>
</div>
</div>
<p></p></li>
<li><p><code>body_html</code><br />
The complete HTML representation of an item created by the converter in the Processing stage of the indexing pipeline (see Coveo Cloud V2 Indexing Pipeline ). The body_html appears in the Quick View of a search result item. You can get the body_html of each item in a postconversion extensions for cases where you want to access and possibly modify the item text content.</p>
<div class="panel" style="border-width: 1px;">
<div class="panelHeader" style="border-bottom-width: 1px;">
<strong>Example:</strong>
</div>
<div class="panelContent">
<p>Your source indexes a question and answer website. Each question and each answer is indexed as a separate item even if they can come from the same HTML page. Your indexed items do not have the <code>&lt;head&gt;</code> elements from the original HTML page and therefore are missing resources such as CSS. Consequently, the Quick View for these items does not look good.</p>
<p>You get the <code>body_html</code> in an extension and inject the appropriate <code>&lt;head&gt;</code> elements.</p>
</div>
</div>
<p>There is no point in getting and modifying the <code>body_html</code> in a preconversion extension because the Processing stage would overwrite it.</p>
<div class="aui-message hint shadowed information-macro has-no-icon">
<p>Notes:</p>
<div class="message-content">
<blockquote>
When you can define your desired body_html content as a static HTML markup containing metadata placeholders, it is generally simpler to use a mapping on the body field (see Add/Edit Mapping).
</blockquote>
<blockquote>
For index size and performance optimization, the body_html is limited in size to 10 MB. This means that the Quick View of items with larger body_html will be truncated.
</blockquote>
</div>
</div></li>
<li><p><code>$thumbnail$</code><br />
The thumbnail image created by the converter in the Processing stage of the indexing pipeline for specific file types ( Microsoft Word, Excel, PowerPoint, and Visio as well as many image file types such as JPG, BMP, GIF, TIF, PSD, PNG... ).<br />
You can get the $thumbnail$ in a postconversion extension in the rare cases where you want to modify the thumbnail or extract information from the thumbnail image. Your thumbnail image can have any size, resolution or format (as long as a browser can display it), but it is a good practice to stick to a normalize image size and resolution.</p>
<div class="aui-message hint shadowed information-macro">
<div class="message-content">
<blockquote>
If you want to overwrite the thumbnail (or create one) you do not need to get the $thumbnail$.
</blockquote>
</div>
</div>
<p></p></li>
</ul></td>
</tr>
<tr class="even">
<td>origin</td>
<td><p>[Optional] The metadata value set by either one of the following components:</p>
<div class="table-wrap">
<table>
<thead>
<tr class="header">
<th>Name</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><code>crawler</code></td>
<td>The stream value set during the Crawling stage</td>
</tr>
<tr class="even">
<td><code>converter</code></td>
<td>The stream value set during the Processing stage</td>
</tr>
<tr class="odd">
<td><code>mapping</code></td>
<td>The stream value set during the Mapping stage</td>
</tr>
</tbody>
</table>
</div>
<p>If no value is supplied and the reverse value is True, the most recent origin is considered, i.e. <code>crawler</code> in preconversion and <code>mapping</code> in postconversion.</p></td>
</tr>
<tr class="odd">
<td><code>reverse</code></td>
<td>[Optional] Boolean used to determine whether to get the stream origin in reverse order or not. The default value is <code>True</code>, meaning that the stream is fetched from the latest indexing pipeline stage with a non-empty stream.</td>
</tr>
</tbody>
</table>

It returns a stream of in-memory bytes (see [Python Buffered Streams](https://docs.python.org/2/library/io.html#buffered-streams)).

## Add Data Stream

Used to add a data stream.

```
document.add_data_stream(stream)
```

**Example**

```
# Import the requests library to perform API calls
import requests
 
extracted_text = [x.strip('\\r\\n\\t') for x in document.get_data_stream('body_text', 'converter').readlines() if x.strip('\\r\\n\\t')]
 
# Override the HTML of the item
html = document.DataStream('body_html')
html.write(requests.get('http://your_item').text)
 
# Override the text with part of the original item
text = document.DataStream('body_text')
text.write('This is a test.')
text.write(extracted_text[0])
 
# Override the thumbnail of the item
thumbnail = document.DataStream('$thumbnail$')
thumbnail.write(requests.get('path/to/your/image.png').content)
 
document.add_data_stream(html)
document.add_data_stream(text)
document.add_data_stream(thumbnail)
```

## Reject

Used to set the item as rejected.

```
document.reject()
```

## Document Object JSON Schema

The `Document` object can be represented with the following JSON schema.

```
{
    "$schema": "http://json-schema.org/draft-04/schema#",
    "definitions": {  
        "MetaDataValue": {
            "type":"object",
            "properties": {
                "origin": {
                    "type": "string"
                },
                "values": {
                    "type": "object",
                    "properties": {
                        "key": {
                            "type": "string"
                        },
                        "value": {
                            "type": "array",
                            "items": {
                                "type": "string"
                            }
                        }
                    }
                }
            } 
        },
        "Permission": {
            "type":"object",
            "properties": {
                "identity": {
                    "type": "string"
                },
                "identity_type": {
                    "type": "string"
                },        
                "security_provider": {
                    "type": "string"
                    "enum": ["user", "group", "virtualgroup", "unknown"]
                },                
                "additional_info": {
                    "type": "object",
                    "properties": {
                        "key": {
                            "type": "string"
                        },
                        "value": {
                            "type": "string"
                        }
                    }
                }        
            }
        },
        "PermissionSet": {
            "type":"object",
            "properties": {
                "name": {
                    "type": "string"
                },
                "allow_anonymous": {
                    "type": "boolean"
                },        
                "allowed_permissions": {
                    "type": "array",
                    "items": {
                         "$ref": "#/definitions/Permission"
                    }            
                },                
                "denied_permissions": {
                    "type": "array",
                    "items": {
                         "$ref": "#/definitions/Permission"
                    }            
                }                           
            }
        },
        "PermissionLevel": {
            "type":"object",
            "properties": {
                "name": {
                    "type": "string"
                },
                "permission_sets": {
                    "type": "array",
                    "items": {
                         "$ref": "#/definitions/PermissionSet"
                    }            
                }                                
            }
        },
        "DataStream": {
            "type":"object",
            "properties": {
                "name": {
                    "type": "string"
                },
                "origin": {
                    "type": "string"
                }
            }
        },
        "Document": {
            "type":"object",
            "properties": {
                "uri": {
                  "type": "string",
                },
                "meta_data": {
                    "type": "array",
                    "items": {
                         "$ref": "#/definitions/MetaDataValue"
                    }            
                },                                
                "permissions": {
                    "type": "array",
                    "items": {
                         "$ref": "#/definitions/PermissionLevel"
                    }            
                },                
                "data_streams": {
                    "type": "array",
                    "items": {
                         "$ref": "#/definitions/DataStream"
                    }            
                }                
            }
        }                
    }        
}
```

## Attachments:

![](images/icons/bullet_blue.gif){width="8" height="8"} [image2017-8-14 12:7:42.png](attachments/36635449/37552624.png) (image/png)
![](images/icons/bullet_blue.gif){width="8" height="8"} [image2017-8-14 12:13:40.png](attachments/36635449/37552625.png) (image/png)
![](images/icons/bullet_blue.gif){width="8" height="8"} [image2017-8-14 12:24:16.png](attachments/36635449/37552626.png) (image/png)
![](images/icons/bullet_blue.gif){width="8" height="8"} [image2017-8-17 9:44:34.png](attachments/36635449/37552842.png) (image/png)
![](images/icons/bullet_blue.gif){width="8" height="8"} [image2017-8-17 9:47:18.png](attachments/36635449/37552843.png) (image/png)
![](images/icons/bullet_blue.gif){width="8" height="8"} [image2017-8-17 9:49:29.png](attachments/36635449/37552844.png) (image/png)
![](images/icons/bullet_blue.gif){width="8" height="8"} [image2017-8-17 9:49:51.png](attachments/36635449/37552845.png) (image/png)

