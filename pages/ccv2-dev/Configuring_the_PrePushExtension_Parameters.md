---
layout: content-2-panel
title: Configuring the PrePushExtension Parameters
categories: migrated
---

# Configuring the PrePushExtension Parameters

You can change the JSON of an item to be pushed by adding the PrePushExtension parameter to your connector configuration file.

1.  In the connector configuration file, in the parameter section, add the following code:

    ```
    { "parameters": { "PrePushExtension": { "value": "c:\\script\\extension.py" } } ... }
    ```

2.  Validate that extension.py looks like this:

    ```
    # This sample adds a metadata. 
    def do_extension(body): 
        body['NewMetadata'] = "new_metadata_value" 
        return body
    ```

    The entry point method name must be do\_extension.

 
