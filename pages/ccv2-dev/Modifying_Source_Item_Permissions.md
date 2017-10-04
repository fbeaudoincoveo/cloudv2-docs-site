---
layout: content-2-panel
title: Modifying Source Item Permissions
categories: migrated
---

# Modifying Source Item Permissions

You can use indexing pipeline extensions to get, clear, add, or set permissions associated with source items (see [Document Object Python API Reference](Document_Object_Python_API_Reference)). 

> While modifying source item permissions with an indexing pipeline extension is legitimate, you must be aware that your code must apply the appropriate permissions in all cases to prevent exposing sensitive information to the wrong people. It is recommended to use permission modification extensions only in simple security model cases that you understand very well and that you can thoroughly test.

**Example:**

You have a source indexing your Salesforce Knowledge articles. The Coveo Cloud Salesforce source does not support index permission for Knowledge content, so by default all articles have the Email Security Provider `*@*`****permission making them searchable by any user, including anonymous users.

Your Knowledge Base (KB) article writing process involves validation stages and only articles that are in the **Public** state should be visible to anonymous users. All others should only be visible to your company employees. Your custom boolean metadata `kav_ispublic` identifies public articles when set to `true`.

In this simple security model, you can use the following indexing pipeline extension script to set restrictive permissions for non public articles.

```
meta = document.get_meta_data_value('kav_ispublic')
isPublic = meta and str(meta[0]).lower() == 'true'
# For non public articles only
if not isPublic:
    # Delete the *@* permission
    document.clear_permissions()
    # Restrict access to users authenticated with an account resolving to an email ending with @mycompany.com 
    document.add_allowed('*@mycompany.com', 'group', 'Email Security Provider')
```

You can now include your Salesforce Knowledge articles source in a public search interface where anonymous users will only see the public articles.


