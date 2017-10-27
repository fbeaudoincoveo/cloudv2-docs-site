---
title: The Page Title       # Write title "In Title Case". Unique source 
slug: "123"                 # The unique page ID from _data/ids.yml (number as a string)
toc: ccv2-dev               # The table of content to use in the sidebar
audience: Administrator     # Article target audience: User | Administrator | Developer | Anyone
product: Coveo Cloud        # Article relative to which product: List of product to be determined
product_version:            # Article relative to which product version: List of product versions to be determined
tags: [keyword1, keyword2]  # Optional: Article related keywords
layout: content-2-panel     # Optional: Override the _config.yml default for a collection
sitemap: true               # Optional: Set to 'false' to exclude from jekyll-sitemap sitemap.xml file
---

# {{ page.title | escape }}
