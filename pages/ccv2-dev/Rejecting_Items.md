---
layout: content-2-panel
title: Rejecting Items
categories: migrated
---

# Rejecting Items

This postconversion extension script sample rejects items.

**Postconversion Extension Script Sample**

```
 def get_flattened_meta():
    flattened = dict()
    for m in document.get_meta_data():
        for metadata_name, metadata_values in m.values.iteritems():
            flattened[metadata_name.lower()] = metadata_values

    normalized = dict()
    for metadata_name, metadata_values in flattened.iteritems():
        if len(metadata_values) == 1:
            normalized[metadata_name] = metadata_values[0]
        elif len(metadata_values) > 1:
            normalized[metadata_name] = ";".join([str(value) for value in metadata_values])
    return normalized
 
file_types = {
    "key1": "value1",
    "key2": "value2"
}

meta_data = get_flattened_meta()

document.add_meta_data({"metadata_name1":next((file_types[file_type] for file_type in file_types
                                                    if file_type in meta_data["filetype"]),
                                                    meta_data["filetype"] if "filetype" in meta_data else "UNKNOWN")})
# Reject personal sites URLs
if meta_data["metadata_name1"] == "REJECT" or \
   (meta_data["metadata_name1"] == "personal" in meta_data["printableuri"]):
    document.reject()
```


