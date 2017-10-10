---
layout: content-2-panel
title: Creating an Indexing Pipeline Extension with the API
categories: migrated
---

# Creating an Indexing Pipeline Extension with the API

The following procedure describes how to create an indexing pipeline extension for a Coveo Cloud V2 organization using the Extension API (see [Extension API Reference](https://developers.coveo.com/x/twEvAg)). 

In the administration console **API Keys** page, add an API key for which you select the **Edit** check box for the **Extensions** privilege (see [Add an API key](https://onlinehelp.coveo.com/en/cloud/api_access.htm#Add_an_API_Key)).

Create an extension for your organization.

1.  Use the following API call:

    ```
    POST https://platform.cloud.coveo.com/rest/organizations/<organizationId>/extensions
    ```

    where you replace `<organizationId>` with its corresponding value (see [Parameters and API Calls](https://developers.coveo.com/x/QokkAg)).

2.  Your call must include the following HTTP headers:

    | Key             | Value                      |
    |-----------------|----------------------------|
    | `Authorization` | `Bearer <a_valid_API_key>` |
    | `Content-Type`  | `application/json`         |

3.  The body is a JSON Extension (see [JSON Extension](https://developers.coveo.com/x/twEvAg#ExtensionAPIReference-JSONExtensionJSONExtension)).

    **Example:**

    Enter a JSON in a format similar to the following example to add a metadata.

    ```
    {
     "content": "document.add_meta_data({'userId':'your_user_ID'})",
     "description": "This extension adds a metadata...",
     "name": "Adding the userId metadata"
    }
    ```

    where the `content` value is the body of your extension (user script), written in Python using the `document` object (see [Document Object Python API Reference](https://developers.coveo.com/x/OQMvAg)).

    You must name and describe your extension.

    > Choose a meaningful name (such as the name of the task that you want to perform) to identify your extension.

4.  Send your request.
    It returns something like this:

    **Example**

    ```
    {
      "content": "document.add_meta_data({'userId':'your_user_ID'})",
      "description": "This extension adds a metadata...",
      "enabled": true,
      "id": "coveosearch-rlic35pr6jhvtx84ta855bdj5j",
      "lastModified": 2588768294677,
      "name": "Adding the userId metadata",
      "versionId": "e3AOSVbGdwYus82z3gduTVPRqbXzidJg",
      "status": {
        "durationHealth": {
          "healthIndicator": "UNKNOWN"
        },
        "dailyStatistics": {
          "averageDurationInSeconds": 0,
          "numberOfExecutions": 0,
          "numberOfSkips": 0,
          "numberOfTimeouts": 0
        },
        "disabledStatus": {},
        "timeoutHealth": {
          "healthIndicator": "UNKNOWN"
        }
      }
    }
    ```

    where the `id` value is your unique extension identifier (`extensionId`).

In the administration console **Activity Browser** page, validate that your extension has succeeded (see Activity Browser - Page).

1.  In the **Sections** facet, select **Content**. 
2.  In the **Resource Types** facet that is now available, select **Extension**.
3.  In the Resources facet, select your extension ID.
4.  In the Result column, validate that your operation is Successful. 

5.  Click an extension activity to see additional information on your extension.

#### What's Next

Apply your extension to a source (see [Applying an Indexing Pipeline Extension to a Source with the API](https://developers.coveo.com/x/IQMvAg)).
