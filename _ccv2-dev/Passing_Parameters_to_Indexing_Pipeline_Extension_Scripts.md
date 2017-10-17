---
slug: "93"
layout: content-2-panel
title: Passing Parameters to Indexing Pipeline Extension Scripts
categories: migrated
---

# Passing Parameters to Indexing Pipeline Extension Scripts

You can use indexing pipeline extension Python scripts to customize how items are indexed. You may need to process items from more than one source with very similar code, where only one or a few aspects vary from one source to another. You can duplicate the extension and adapt the code for each source, but a better practice is to rather pass parameters (see [Indexing Pipeline Extension Parameters](Indexing_Pipeline_Extension_Parameters)). 

The following procedure describes how to pass parameters in an indexing pipeline extension script using the Extension API (see [Extension API Reference](https://developers.coveo.com/x/twEvAg)).

1.  For a given indexing pipeline extension that you want to reuse with two or more sources, identify the input values that can vary from one source to another (see [Creating an Indexing Pipeline Extension with the API](https://developers.coveo.com/display/CloudPlatform/Creating+an+Indexing+Pipeline+Extension+with+the+API)). 
2.  In the source JSON configuration part where you assign the extension to the source, for each variable input you identified, define key-value pairs for the context of this source  (see [Applying an Extension to a Source](https://developers.coveo.com/display/CloudPlatform/Applying+an+Indexing+Pipeline+Extension+to+a+Source+with+the+API)).

    **Example:**

    In the administration console, assign parameter values while applying the extension to the source.

    ```
    [
      {
        "actionOnError": "SKIP_EXTENSION",
        "extensionId": "myorganization-xc56kss5iazmlq4irhndj52ns4",
        "parameters": {
          "metadataName": "websiteSection",
          "metadataValue": "intranet"
        }
      }
    ]
    ```

    Once you define parameters in the source JSON configuration, they become available to your script in a `parameters` object.

     

3.  In a Python extension script, get your contextual values and inject them in variables.  

    **Example:**

    Consider the following extension script that gets the `websiteSection` and `intranet` values. For each item, the extension script adds a metadata name and value with the `metadataName` and `metadataValue` parameters that can be contextually changed with any source.

    ```
    name = parameters['metadataName']
    value = parameters['metadataValue']
    document.add_meta_data({name:value})
    log('Added metadata ' + name + ' with value ' + value)
    ```

4.  Optionally, use the Extension API to test the result (see [Test an extension](https://platform.cloud.coveo.com/docs?api=Extension#!/Indexing32Pipeline32Extensions/rest_organizations_paramId_extensions_paramId_test_post)). The use of the test call returns a JSON formatted document object. In the document.metadata section, you can validate that addMetadataWithParameters extension script adds the metadata value intranet to the metadata name websiteSection. Furthermore, the logs section shows the result of the log call in the extension script and the result.status section validates the operation success.

    **Example:**

    ```
    {
        "document": {
            "metadata": [
                {
                    "origin": "Extension tester",
                    "values": {}
                },
                {
                    "origin": "addMetadataWithParameters",
                    "values": {
                        "websiteSection": [
                            "intranet"
                        ]
                    }
                }
            ],
            "dataStreams": [],
            "permissions": []
        },
        "logs": [
            {
                "severity": "NORMAL",
                "comment": "Added metadata intranet with value websiteSection"
            }
        ],
        "dataStreamUris": [],
        "duration": 0.004000055,
        "result": {
            "status": "SUCCESS"
        }
    }
    ```

    > Since all unmapped metadatas are not kept when indexing an item, and because testing an extension has access to an item from the index, only indexed metadatas are available when using Test an extension API call.

    Tip:

    >  You can also use the Coveo Labs [pipeline-extension-manager](https://github.com/coveo-labs/pipeline-extension-manager) to more easily test your extension on specific items.

5.  Rebuild the source to run the extension.

6.  Validate that your source items were modified as expected following your extension parameters.  

