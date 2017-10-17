---
slug: "75"
layout: content-2-panel
title: Grouping Parents and Children
categories: migrated
---

# Grouping Parents and Children

This is a postconversion extension script sample.

```
def get_flattened_meta():
    flattened = dict()
    for m in document.get_meta_data():
        for metadata_name, metadata_values in m.values.iteritems():
            flattened[meta_name.lower()] = metadata_values

    normalized = dict()
    for metadata_name, metadata_values in flattened.iteritems():
        if len(metadata_values) == 1:
            normalized[metadata_name] = metadata_values[0]
        elif len(metadata_values) > 1:
            normalized[metadata_name] = ";".join([str(value) for value in metadata_values])
    return normalized
 
def folding_setup_one (meta, trigger):
    source_type = meta["sourcetype"] if "sourcetype" in meta else ""
    source_name = str(meta["source"]).replace(" +", "") if "source" in meta else ""
    matches = re.match("/([a-z]+):(\d+)\/[a-z]+:\d+$/i", meta["printableuri"])
    if matches and len(matches) > 1:
        parent_doc_type = matches.group(1)
        parent_id = matches.group(2)
    else:
        parent_doc_type = ""
        parent_id = ""
    return "".join([source_type, source_name, parent_doc_type, parent_id])

def folding_setup_two (meta, trigger):
    if "replyCount" in meta:
        if int(meta["replyCount"]) <= trigger:
            return ""
    source_type = meta["sourcetype"] if "sourcetype" in meta else ""
    source_name = str(meta["source"]).replace(" +", "") if "source" in meta else ""
    document_type = meta["itemtype"] if "itemtype" in meta else ""
    id = meta["id"] if "id" in meta else ""
    return "".join([source_type, source_name, item_type, id])

def folding_setup_three (meta, trigger):
    if "commentcount" in meta:
        if int(meta["commentcount"]) <= trigger:
            return ""
    source_type = meta["sourcetype"] if "sourcetype" in meta else ""
    source_name = str(meta["source"]).replace(" +", "") if "source" in meta else ""
    document_type = meta["itemtype"] if "itemtype" in meta else ""
    id = meta["id"] if "id" in meta else ""
    return "".join([source_type, source_name, item_type, id])
 
folding_setup = {
    "child1": folding_setup_one,
    "child2": folding_setup_one,
    "child3": folding_setup_one,
    "parent1": folding_setup_two,
    "parent2": folding_setup_two,
    "parent3": folding_setup_two,
    "parent4": folding_setup_three,
    "parent5": folding_setup_three
}

meta_data = get_flattened_meta()

item_values = document.get_meta_data_value(itemtype)
if itemtype_values:
    # Generate @foldFoldingField and @foldChildField to support CoveoFolding components to group together parents with children
    document.add_meta_data({"foldfoldingfield":folding_setup[meta_data["itemtype"]](meta_data, -1)})
    document.add_meta_data({"foldchildfield":folding_setup[meta_data["itemtype"]](meta_data, 0)})
```


