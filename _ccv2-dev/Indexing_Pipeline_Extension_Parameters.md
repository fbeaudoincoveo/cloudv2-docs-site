---
slug: "79"
layout: content-2-panel
title: Indexing Pipeline Extension Parameters
categories: migrated
---

# Indexing Pipeline Extension Parameters

Indexing pipeline extension parameters are key-value pairs defined in the source extension configuration to get contextual values related to the source and pass them to extension script variables (see [Edit a Source JSON Configuration](http://www.coveo.com/go?dest=cloudhelp&lcid=9&context=286)). When you define extension parameters key-value pairs in the source JSON configuration, they populate the  `parameters` dictionary that is available to your Python script. 

You can use indexing pipeline extension parameters to develop generic extensions that you can reuse with more than one source  (see [Passing Parameters to Indexing Pipeline Extension Scripts](Passing_Parameters_to_Indexing_Pipeline_Extension_Scripts)). The multiple use of an extension is possible when the same code is applicable, but one or more input values vary from one source to another and the script cannot get those values from existing metadata. Maintaining the code of one generic extension is easier than maintaining several slightly different extension script copies. Furthermore, there is a limit to the number of extensions you can define in your Coveo Cloud V2 organization, so reusing one extension for multiple sources minimizes the risk of reaching this limit.

**Example:**

A first source indexes www.myHostNameA.com website and another source indexes www.myHostNameB.com website. Those similar sites are typical transactional website that display products and store information. In the indexing pipeline, there is a script extension that parses the URL and adds a metadata corresponding to the website subsection. Because of the websites similarities, the good practice is to use the same script for both, but unfortunately, URL subsections differ slightly. For instance, www.myHostNameA.com/product and www.myHostNameB.com/item both lead to the products subsection of each site. Furthermore, www.myHostNameA.com/store and www.myHostNameB.com/location both lead to the store information subsection. Therefore, adding the hostname and the subsection keywords directly in the script would make this script static and thus, usable only for one source. In this case, the good practice is to include parameters in the extension to make this script dynamic and reusable for both sources.

While editing the source JSON configuration for myHostNameA website, consider the following configuration:

```
[
  {
    "actionOnError": "SKIP_EXTENSION",
    "extensionId": "myorganization-xc56kss5iazmlq4irhndj52ns4",
    "parameters": {
      "hostname_value": "myHostNameA",
      "website_part_1": "product",
      "website_part_2": "store"
    }
  }
]
```

To reuse the same extension script for `myHostNameB` source, you need to edit the `parameters` dictionary in the source JSON configuration to fit the website keywords:

```
[
  {
    "actionOnError": "SKIP_EXTENSION",
    "extensionId": "myorganization-xc56kss5iazmlq4irhndj52ns4",
    "parameters": {
      "hostname_value": "myHostNameB",
      "website_part_1": "item",
      "website_part_2": "location"
    }
  }
]
```

Consider the following extension script:

```
# importing regex module to parse site url
import re
 
try:
    log('Starting-add-site-subsection-metadata')
    if ('hostname_value' == ''):
        log('hostname_value has not been specified, supply hostname_value with a company name')
        raise Exception('Supply a hostname_value in the extension parameters')
    log('Starting metadata for ' + parameters['hostname_value'])
        
    # assigning 'originaluri' metadata to 'uri' dictionary
    uri = document.get_meta_data_value('originaluri')
    log('Adding localization to site sub_section')
 
    # using regex built-in search method to parse uri[0]
    # this regex detects the site subsection defining word which sits after the '.com/' and before the next '/'
    match = re.search(r'[a-z,0-9]{0,}\.com\/([a-z]{0,})', uri[0])
    if match:
        # the regex built-in method retrieves the website subsection and assign it to 'sitepart' variable
        sitepart = match.group(1)
        if sitepart == parameters['website_part_1']:
            document.add_meta_data({'sub_section': 'product'})
        elif sitepart == parameters['website_part_2']:
            document.add_meta_data({'sub_section': 'store'})
        else:
            document.add_meta_data({'sub_section':parameters['hostname_value']})
except Exception as e:
    log(str(e))
```

From now on, you can create a standardized `subsection` facet to optimize your search page and filter results by `product` or `store` with the use of only one reusable extension script, even if the keywords identifying the website subsections are different from one url to another.

 


