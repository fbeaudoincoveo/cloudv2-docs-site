---
slug: "89"
layout: content-2-panel
title: Modifying Date
categories: migrated
---

# Modifying Date

This postconversion extension script sample modifies the item date.

**Postconversion Extension Script Sample**

```
from dateutil.parser import parse
from dateutil.relativedelta import relativedelta
from datetime import datetime, date
import re
 
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
 
def convert_date(date_string, default):
    try:
        return parse(date_string) - relativedelta(years=1)
    except ValueError:
        return default

def parse_date_with_trigger(date_string, default):
    try:
        return parse(date_string) if parse(date_string) > datetime(1960, 1, 1) else parse(date_string)
    except ValueError:
        return default
 
meta_data = get_flattened_meta()
 
# When the metadata is wrong and you don't have any date, it puts it one year before
document.add_meta_data({"Date":str(parse_date_with_trigger(meta_data["modificationdate"], date.today()) \
                                          if "modificationdate" in meta_data else date.today())})

document.add_meta_data({"Date":str(convert_date(meta_data["Date"], date.today()) \
                                          if "Date" in meta_data else date.today())})
```


