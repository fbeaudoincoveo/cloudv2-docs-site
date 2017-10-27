---
slug: "44"
layout: content-2-panel
title: Coveo Cloud V2 Indexing Pipeline Extensions
categories: migrated
---

# Coveo Cloud V2 Indexing Pipeline Extensions

Coveo Cloud V2 organization sources can pull content from a variety of systems to make your content searchable for those with the appropriate permissions (see Available Source Types).

The indexing pipeline extension feature provides a way to execute Python conversion scripts in a securely isolated non persistent container, allowing developers to customize how items get indexed. Extension scripts are executed as indexing pipeline stages, which corresponds to the series of actions taken upon the reception of items before they become searchable.  

Note:

>  You can manage your indexing pipeline extensions from the Coveo Cloud V2 administration console **Extensions** page and get more information on indexing pipeline extensions from the administration console documentation (see [Extensions - Page](http://www.coveo.com/go?dest=cloudhelp&lcid=9&context=326) ). 

 

#### Usage Overview

You can execute an indexing pipeline extension for every item of one or more sources of your organization using the Coveo Cloud V2 APIs:

1.  In the administration console **API Keys** page, add an API key for which you select the **Edit** check box for the **Extensions** privilege (see API Keys - Page).

2.  Write your extension script using the `document` object (see [Document Object Python API Reference](https://developers.coveo.com/x/OQMvAg)).
3.  Create your extension (see [Creating an Indexing Pipeline Extension with the API](https://developers.coveo.com/x/uQIvAg)).

4.  Add your script to your extension.
5.  Apply your extension to your source(s) (see [Applying an Indexing Pipeline Extension to a Source with the API](https://developers.coveo.com/x/IQMvAg)).

6.  Rebuild your source(s) to make your extension effective.

7.  Validate that your changes perform as expected.

 
