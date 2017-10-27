---
slug: "115"
layout: content-2-panel
title: Source API - Mappings Resource
categories: migrated
---

# Source API - Mappings Resource

Each Coveo Cloud V2 organization source comes with a set of standard fields that can be filled with the metadata of your choice when adding mappings for sources.

You can take advantage of the Source API to define how source items, and the fields they use, are included in your Coveo Cloud V2 organization to optimize the global search experience.

Note:

> You can also manage mapping rules from the administration console **Mapping** tab of a source (see [Mapping - Tab](http://www.coveo.com/go?dest=cloudhelp&lcid=9&context=284)).

**To add a mapping rule from the API**

1.  In the administration console [API](https://platform.cloud.coveo.com/admin/#/organization/api-access/)**Access** page, add an API key for which you select the following check boxes:
    1.  **V**i**ew** for the **Organization** privilege
    2.  **View** for the **Sources** privilege
    3.  **Edit** for the **Sources** privilege

2.  Add a new field using the administration console **Fields** page (see [Fields - Page](https://onlinehelp.coveo.com/en/cloud/fields.htm#Add_a_New_Field)).
3.  Add a mapping rule to a source.
    Specify the name of the metadata to map to your newly created field.

4.  When adding a mapping rule for an item type, indicate the type of item to which you wish to apply your mapping rule.

5.  Rebuild the source to make the mapping rule effective.

6.  Validate that your mapping works as expected in the content browser (see [Fields Tab](https://onlinehelp.coveo.com/en/cloud/item_properties.htm#fieldstab)).

#### What's Next

Get familiar with the mapping concepts.
