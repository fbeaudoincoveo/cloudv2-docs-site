---
slug: "116"
layout: content-2-panel
title: Source API Mappings Resource Usage Overview
categories: migrated
---

# Source API Mappings Resource Usage Overview

You can take advantage of the Source API Mappings resource to define common and specific mapping rules for your sources.

In the administration console **API Access** page, add an API key for which you select the **View** check box for the **Organization** privilege and the **View** and **Edit** check boxes for the **Sources** privilege (see [API Access - Page](https://onlinehelp.coveo.com/en/cloud/api_access.htm#Add_an_API_Key)).

When no existing field is appropriate for your metadata, add a new index-wide custom field using the administration console **Fields** page (see [Fields - Page](http://www.coveo.com/go?dest=cloudhelp&lcid=9&context=287#Add_a_New_Field)).

> It is recommended to choose a descriptive name for your field so that fields shared across item types can be differentiated (e.g., `video_title`, `video_body`, ...).

Use the Swagger generated documentation to define your mapping rules.

1.  Go to <https://platform.cloud.coveo.com/docs> site.

2.  In the header drop-down list, select **Source**.
3.  Expand Mappings : Mapping Resource, and then click the API call that you want to perform.
               • POST /rest/organizations/{organizationId}/sources/{sourceId}/mappings/common/rules           • PUT /rest/organizations/{organizationId}/sources/{sourceId}/mappings/common/rules/{ruleId}           • POST /rest/organizations/{organizationId}/sources/{sourceId}/mappings/types/{typeId}/rules
               • PUT /rest/organizations/{organizationId}/sources/{sourceId}/mappings/types/{typeId}/rules/{ruleId}

Whether your process adds or updates a mapping rule, enter a rule in a format similar to the following example:

**JSON Body Example**

```
{
  "content": [
    "your_rule"
  ],
  "field": "your_field_name"
}
```

where you replace `your_rule` with the system item metadata or specific value(s) that your `field` should contain (see Mapping Rules Syntax Reference).

When applicable, specify the item type to which you wish to apply your mapping rule.
           • You can use the API to get all item types that are used in your mappings with the following call: GET /rest/organization/{organizationId}/sources/{sourceId}/mappings/types           • If no type is appropriate, you can create one via this call: POST /rest/organization/{organizationId}/sources/{sourceId}/mappings/types

Once you are ready, rebuild the source to apply the mapping changes.

Validate that your mappings work as expected on the content browser (see [Fields Tab](https://onlinehelp.coveo.com/en/cloud/item_properties.htm#fieldstab)).
