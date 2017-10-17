---
slug: "84"
layout: content-2-panel
title: Inspecting All Available Metadata Values
categories: migrated
---

# Inspecting All Available Metadata Values

When you start working with a source, you may want to know all the metadata key/value pairs that are extracted by indexing pipeline stages so that you can take advantage of them. This can be used, for example, to create useful facets in your search interfaces.  

The indexing pipeline extension script sample below can help you discover your source metadata. The script reads all available metadata for each source item and writes the metadata key/value pairs in JSON format in a new metadata named `allmetadatavalues`.  

> You must apply this script to a source only temporarily to allow you to inspect available metadata, and then remove it. This is because the  `allmetadatavalues` significantly increases the size of a source an may affect your index performance.

> For very large sources such as ones taking several hours or even days to rebuild, consider creating a temporary source crawling only a small but representative subset of the same repository, and add the extension to this source, which should rebuild much faster. Remember that the indexing pipeline stages may extract different metadata for different item types in a repository.

> Do not use this script in cases where there is a very large number of metadata (&gt;1000) as can be the case with Coveo for Sitecore.

**Postconversion Extension Script Sample**

```
import json
values = dict()
type = ''
for m in document.get_meta_data():
    type = ':' + m.origin
    for metadata_name, metadata_value in m.values.iteritems():
        values[metadata_name+type] = metadata_value
# Add the allmetadatavalues metadata
document.add_meta_data({"allmetadatavalues": json.dumps(values)})
```

Typical usage of this script:

1.  Apply the script to the source for which you want to inspect available metadata and their origin. 
2.  Create a field  (such as one named  `allmetadatavalues`) and add a mapping to your source to map the  `allmetadatavalues` metadata to your field. 
3.  Rebuild your source. 
4.  In the Coveo Cloud administration console [Content Browser](https://platform.cloud.coveo.com/admin/#/content/browser/) page:
    1.  In the **Source** facet, select your source. 
    2.  Double-click one or more items, and in the **Fields** tab look at the content of the allmetadatavalues field to discover your source available metadata. 

        > Consider copying and pasting the `allmetadatavalues` JSON in a text editor, reformat its content in a more readable form, and then save JSON samples for key source items to a folder of your choice.

5.  When you are done, remove the script from the source and rebuild the source.

