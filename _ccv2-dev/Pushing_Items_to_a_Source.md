---
slug: "102"
layout: content-2-panel
title: Pushing Items to a Source
categories: migrated
---

# Pushing Items to a Source

This topic describes how to add or update items into a Coveo Cloud V2 push type source using the Push API (see [Using the Push API](Using_the_Push_API)). 

1.  Create or ensure that you have a Coveo Cloud V2 push type source (see [Creating a Push Type Source](Creating_a_Push_Type_Source)). 
2.  Build your REST request to push an item to your source as follows: 

    Note:

    > Review the following documentation to learn the details to build and test the Push API calls:

    -   [Push API Reference](Push_API_Reference)

    -   Go to https://platform.cloud.coveo.com/docs and then selecting PushAPI in the header drop-down list. 

    The call to add or update an item in its minimal form is:

    ```
    PUT https://push.cloud.coveo.com/v1/organizations/<organizationId>/sources/<sourceId>/documents?documentId=<itemUri> BODY
    ```

     

    1.  Your call must include the following HTTP headers:

        <table>
        <colgroup>
        <col width="50%" />
        <col width="50%" />
        </colgroup>
        <thead>
        <tr class="header">
        <th><div>
        Key
        </div></th>
        <th><div>
        Value
        </div></th>
        </tr>
        </thead>
        <tbody>
        <tr class="odd">
        <td><p><code>Authorization</code></p></td>
        <td><p>A valid API key which can be created in the Coveo Cloud V2 <strong>API Keys</strong> page</p>
        <div class="aui-message hint shadowed information-macro has-no-icon">
        <p>Note:</p>
        <div class="message-content">
        <blockquote>
        For test purposes, you can access the Coveo Cloud V2 administration console and, using your browser developer tools, copy the temporary token from the <code>access_token</code> cookie. The <code>Authorization</code> key value would be of the form:
        </blockquote>
        <blockquote>
        <code>Bearer &lt;access_token value&gt;</code>
        </blockquote>
        </div>
        </div></td>
        </tr>
        <tr class="even">
        <td><code>content-type</code></td>
        <td><code>application/json</code></td>
        </tr>
        </tbody>
        </table>

    2.  You can get the `<organizationId>` and `<sourceId>` values from the **Push API URL** administration console parameter when you edit your source:

        1.  In the [Coveo Cloud V2 administration console](https://platform.cloud.coveo.com), under **Search content**, select **Sources**.
        2.  In the **Sources** page, select your push type source, and then click **Edit**. 
        3.  While in the **Edit a \[source type\] source** panel, under the **Push API URL** parameter, click **Copy to clipboard**, and then paste the URL that is in the following form in a text editor: 

            ```
            https://push.cloud.coveo.com/v1/organizations/<organizationID>/sources/<sourceID>/documents
            ```

            **Example:**

                https://push.cloud.coveo.com/v1/organizations/mycoveoorg/sources/mycoveoorg-rlj7km73nqqmi/documents

        4.  Note the `<organizationID>` and `<sourceID>` values.

        The `<itemUri>` must be a unique item URI. 

        This is important, otherwise the call returns a `201 Success` code, but the item will not be indexed, without further errors. 

        **Example:**

            PUT https://push.cloud.coveo.com/v1/organizations/mycoveoorg/sources/mycoveoorg-rlj7km73nqqmi/documents?documentId=http://myitem

        > Do not use hashes in the endpath.

    3.  The `BODY` is a JSON document (see [JSON Document](https://developers.coveo.com/x/fIQAAg#PushAPIDefinition-JSONDocJSONDocument)). 

        You can specify the content to index using two methods:

        -   Small plain text (Data reserved key)

            When your item contains a small amount of plain text, use the `Data` reserved key to pass the content to be indexed. 

            **Example:**

            A minimal BODY content to include, illustrated for a small plain text sample: 

            ```
            {
                "FileExtension":".txt",
                "Data": "This is the only content that will be indexed for this item."
            }
            ```

            OR

        -   Compressed encoded content  (CompressedBinaryData reserved key)

            Use this method whenever the content includes anything other than plain text, such as XML/HTML markup or binary content.

            Your data must be compressed using one of the supported compression types (Deflate, GZip, LZMA, Uncompressed, or ZLib), and then Base64 encoded. Uncompressed content must still be Base64 encoded.

            **Example:**

            A typical minimal BODY content to include, illustrated for a web page (see [Push API Reference](https://developers.coveo.com/x/fIQAAg)): 

            ```
            {
                "FileExtension":".html",
                "CompressedBinaryData": encodeddata
            }
            ```

            where `CompressedBinaryData` contains the compressed and Base64 encoded content to be indexed for the item (in the encodeddata variable in the above example). 

            Notes:

            > The `FileExtension` key is important as its value determines the converter used to index the content.

            > You should also include values for the following standard fields:

            ```
            {
                'author': 'Doc Team',
                'size': 3659,
                'date': '2016-01-11 21:23:14',
                'indexeddate': '2016-02-07 04:02:23'
            }
            ```

            > The `author` value will end up in the `author` (and `@sysauthor`) field.

            > The `size` value will end up in the `size` (and `@syssize`) field. It must contain a integer value representing the original size of indexed item in bytes.

            > The date value will end up in the date (and @sysdate) field.

            > The indexeddate value will end up in the indexeddate (and @sysindexeddate) field.

            > All dates values must be in UTC time string in the form `'yyyy-mm-dd hh:mm:ss'`.

            >  

            > You do not need to add mappings for the above standard fields and neither for any other standard and custom fields for which the name exactly matches (case sensitive) your metadata names. They will automatically be mapped.

            > You can of course add any custom metadata in this JSON BODY. Ensure that the value type matches that of the field to which it is mapped.

            > Fields prefixed with `sys` are standard fields duplicated by the REST Search API to ensure compatibility with JavaScript Search interfaces developed for Coveo Cloud V1 or on-premises Coveo Enterprise Search 7 indexes.

            >  

            > When your source is a secured type, you must include the `Permissions` section to indicate who (User, group, VirtualGroups) can see the item (see [Pushing Secured Items to a Source](https://developers.coveo.com/x/QQAvAg)).

3.  Perform your call(s) to push item(s).

    It is a good practice to start by pushing one item or just a few items and validate the results before processing a large number of items (see [Batch Pushing Encrypted Files in a Batch](https://developers.coveo.com/x/5YcdAg)).

    Notes:

    > There is always a delay of about 300 ms to process incoming Push API calls. When no or not enough idle Lambda functions are up, there can be an additional provisioning delay of a few seconds (see [Understanding Push API Processing Delay](Understanding_Push_API_Processing_Delay)). You could therefore occasionally get `504 Timeout` errors. Implement a retry mechanism.

    > In the Coveo Cloud Administration Console, the **Activity of Source** panel will report source status changes, but the **Outcome** column always indicates **No items processed** even you successively push one or more items.

4.  When your source is secured, you must also push identities, group members, and identity mappings to your identity provider (see Pushing Identities to an Identity Provider).

5.  Access the Coveo Cloud V2 administration console.

    -   <https://platform.cloud.coveo.com>

6.  In the administration console, validate that the item(s) are indexed:

    1.  In the Sources page, within a few minutes you can see the number of processed items in the Status column, or watch the \[Nb\] items value increase in the Content column (see Understanding Push API Processing Delay). If you update items (push again items), the number will not increase. 

    2.  In the Content browser page:

        1.  In the Source facet, select your source.

        2.  In the search results, look for your added or updated items.

        3.  Validate that they are indexed as expected by looking at the Quick View. Click Details to see and validate the fields and their values. 

#### What's Next

Consider creating custom fields and adding mappings to map metadata to your Coveo Cloud V2 index fields. 

1.  When no existing index field is appropriate for your metadata, first create an appropriate index-wide custom field.

2.  In your custom source, when metadata names do not exactly match corresponding standard or custom index field names, add mappings for standard or custom fields. 

3.  Push already indexed items again to your source to make mappings effective.


