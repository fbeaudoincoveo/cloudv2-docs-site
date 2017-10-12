---
layout: content-2-panel
title: Applying an Indexing Pipeline Extension to a Source with the API
categories: migrated
slug: "6"
---

# Applying an Indexing Pipeline Extension to a Source with the API

> This is preliminary documentation for the Coveo Cloud V2 Indexing Pipeline Extension feature which is currently available in beta version.

The following procedure describes how to apply an indexing pipeline extension to every item of a Coveo Cloud V2 organization source using the Source API.

1.  If not already done, create an extension for your organization (see [Creating an Indexing Pipeline Extension with the API](https://developers.coveo.com/x/uQIvAg)).

2.  Apply your extension to your source.

    1.  Use the following API call:

        ```
        PUT https://platform.cloud.coveo.com/rest/organizations/<organizationId>/sources/<sourceId>/extensions?rebuild=<true|false>
        ```

        where you replace `<organizationId>` and `<sourceId>` with their real values (see [Parameters and API Calls](https://developers.coveo.com/x/QokkAg)). The `rebuild` parameter determines whether to rebuild the source following the extension change. The default value is `false`.

    2.  Your call must include the following HTTP headers:

        | Key             | Value                      |
        |-----------------|----------------------------|
        | `Authorization` | `Bearer <a_valid_API_key>` |
        | `Content-Type`  | `application/json`         |

    3.  Build the body of your request.

        **Example:**

        Enter a JSON in a format similar to the following example to apply a postconversion extension to a source of a given type.

        ```
        {
          "common": {
            "postConversionExtensions": [
              {
                "extensionId": "coveosearch-rlic35pr6jhvtx84ta855bdj5j",
                "parameters": {}
              }
            ]
          }
        }
        ```

        where the `extensionId` value is the `id` value that you got when you created the extension (see [Creating an Indexing Pipeline Extension with the API](https://developers.coveo.com/x/uQIvAg)).

        Replace `YOUR_SOURCE_TYPE` and `YOUR_SOURCE_PERMISSION_TYPE` with the appropriate values in uppercase (see Available Source Types and Source Permission Types).

        > When you want to apply a preconversion extension, replace `postConversionExtensions` with `preConversionExtensions`.

    4.  Optionally, add a condition to your extension. 
        The condition is part of the extension configuration, not in the extension Python script itself.  This way, the Coveo Cloud indexing pipeline loads and executes the extension only for items for which the condition evaluates to `True`, allowing to optimize crawling performances. 
        The condition syntax uses metadata values and operators (see [Indexing Pipeline Extension Condition Syntax Reference](https://developers.coveo.com/x/xwcvAg)). 

        **Example:**

        Enter a JSON in a format similar to the following example to apply a postconversion extension with a condition.

        ```
        {
          "common": {
            "postConversionExtensions": [
              {
                "condition": "%[meta1] == 'your_user_ID'",
                "extensionId": "coveosearch-rlic35pr6jhvtx84ta855bdj5j",
                "parameters": {
                  "metadata_name": "userId",
                  "metadata_value": "your_user_ID"
                }
              }
            ]
          }
        }
        ```

        where the `parameter` value is a collection of key value pairs that can be used to specify item property values.

        > This extension is executed only if the metadata value equals your\_user\_ID.

    5.  When your extension has several versions, you can specify the one that you want to apply to your source.

        **Example:**

        Enter a JSON in a format similar to the following example to specify a version.

        ```
        {
          "common": {
            "postConversionExtensions": [
              {
                
                "extensionId": "coveosearch-rlic35pr6jhvtx84ta855bdj5j",
                "parameters": {},
                "versionId": "your_version_ID"
              }
            ]
          }
        }
        ```

        where you replace `your_version_ID` with the `versionId` value that you got when you created or updated your extension (see [Get Versions](https://developers.coveo.com/x/twEvAg#ExtensionAPIReference-VersionsVersions)).

    6.  When you want to apply your extension a particular type of item, specify the item type to which you wish to apply your extension.

        **Example:**

        Enter a JSON in a format similar to the following example to specify an item type.

        ```
        {
          "items": {
            "your_item_type_name": {
              "postConversionExtensions": [
                {
                  "extensionId": "proddailyratlab-szek5zohljqnuuccbfwjqicne4",
                  "itemType": "your_item_type_name",
                  "parameters": {}
                }
              ]
            }
          }
        }
        ```

        where you replace `your_item_type_name` with the name of the item type to which you wish to apply your extension.

    7.  If you are ready to make your extension effective, set the `rebuild` parameter value to `true`.

        > You may want to update or even delete your extension. In such a case, set the `rebuild` parameter value to `false` to make the desired changes, and then rebuild your source to apply the extension changes.

    8.  Send your request.

    9.  In the administration console **Sources** page, in the**Edit a Source JSON Configuration:** \[**SourceName**\] panel of your source, validate that your extension is applied to your source (see Edit a Source JSON Configuration: \[SourceName\] - Panel).

        1.  In the **Edit a Source JSON Configuration:** \[**SourceName**\] panel of your source, ensure the **All** tab is selected.

        2.  Scroll down to the end of the **JSON configuration** box to validate that your extension is applied to your source.

            **Example**

            ```
            {
              ... 
              "preConversionExtensions": [],
              "postConversionExtensions": [
                {
                  "extensionId": "coveosearch-rlic35pr6jhvtx84ta855bdj5j",
                  "parameters": {}
                }
              ],
              ...
            }
            ```

3.   If not already done, rebuild your source to make your extension effective.
    1.  Use the following API call:

        ```
        POST https://platform.cloud.coveo.com/rest/organizations/<organizationId>/sources/<sourceId>/rebuild
        ```

        where you replace `<organizationId>` and `<sourceId>` with their real values (see [Parameters and API Calls](https://developers.coveo.com/x/QokkAg)).

    2.  Your call must include the same HTTP headers as in step 2b.
    3.  Send your request and ensure it returns a `201 Created` response code.

4.  Validate that your changes perform as expected.


