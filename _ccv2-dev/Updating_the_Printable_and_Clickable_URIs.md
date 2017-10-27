---
slug: "123"
layout: content-2-panel
title: Updating the Printable and Clickable URIs
categories: migrated
---

# Updating the Printable and Clickable URIs

This preconversion extension script sample updates the item printable and clickable URIs.

**Preconversion Extension Script Sample**

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
 
def search_and_replace_from_list(string_replacement_list, initial_string, default_string):
    return reduce(lambda x, y: str(x).replace(y, string_replacement_list[y]),
                  string_replacement_list,
                  initial_string or default_string)

urls = {
    "key1":"value1",
    "key2":"value2"
}
 
meta_data = get_flattened_meta()

# Update the item printable URI (the URI the user sees on a search result).
document.add_meta_data({"printableuri":search_and_replace_from_list(urls, meta_data["printableuri"]
                               if "printableuri" in meta_data else "", "")})
# Update the item clickable URI (the URI that is opened when a user clickes on a search result title).
document.add_meta_data({"clickableuri":search_and_replace_from_list(urls, meta_data["clickableuri"]
                               if "clickableuri" in meta_data else "", "")})
```


