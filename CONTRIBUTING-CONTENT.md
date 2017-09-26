# Contributing CONTENT

All Coveo employees are encouraged to contribute to the content of this site. This articles provides details on how to contribute.  

## Installation

The best practice is to install and build the site locally and continually validate your changes (see [README.md](README.md)). 

## Content Creation

Instructions on how to create content. 

### Index Pages

Create an `index.md` page in each repo folder to prevent the server from returning a 404 error for URLS ending with a repo (`doc.site.com/path/foldername` or `doc.site.com/path/foldername/`). 

At the minimum the index file should list pages in the folder. 

### Permalinks 

Do not set permalinks in the `_config.yml` file or in the front matter of pages. Rather use the default URL behavior that simply reproduces the repo folder structure and filename. When following the [Links](#links) section instructions, the `.md` extension is automatically switched to `.html`. 

More to come about strategies to create content...

## Links

Instructions to add different types of links. 

### Link to a section in the current article 

Create links to sections in the same page using the standard Markdown link format and as the anchor name, the section title all in lowercase where spaces are replaced by `-`: 

`[The Section Title](#the-section-title)]`

This is possible because for `h1` to `h6` HTML elements, the Kramdown Markdown interpreter automatically creates `id` attributes made of the words of the section title all in lowercase where spaces are replaced by `-` (Kramdown option `auto_ids = true`). 

### Link to another article in this site

As recommended in the Jekyll documentation (see [Linking to pages](https://jekyllrb.com/docs/templates/#links)), use the following syntax to when linking to other articles of this site: 

`[title]({{ site.baseurl }}{% link pathFromRoot/filename.ext %})`

where: 
* `pathFromRoot` is the path relative to the root repo folder
* `filename.ext` is the filename with its original extension

> **Examples**:
> 
>Linking to another page:
>
> `[Creating a Source]({{ site.baseurl }}{% link papes/creating-a-source.md %})`
>
> Linking to a collection item such as a glossary term:
>
> `[indexing pipeline extension]({{ site.baseurl }}{% link _glossary/indexing-pipeline-extension.md %})`

`link` tag advantages:
* Validates links (site fails to build with an error such as `Liquid Exception: Could not find document 'path/filename.md' in tag 'link'. Make sure the document exists and the path is correct. in about.md`)
* Insensitive to permalink changes

Link format disadvantage: 
* The link is not rendered in an HTML preview since the liquid tags are not interpreted. 
> **Tip**: 
>
> You can use a REGEX to find regular Markdown links to the correct format such as for a glossary term reference: 
> 
> Search: `]\(/glossary/(.*?)(\))`
>
> Replace:  ```]({{ site.baseurl }}{% link _glossary/$1.md %})```

### Link to a Section in Another Article in This Site

Append `#` followed byt the anchor name (section title all in lowercase with spaces replaced by `-`) to the syntax when linking to another article of this site: 

`[The Section Title]({{ site.baseurl }}{% link pathFromRoot/the-article-title.md %}#the-section-title)`

### Link to an External Page

Create links to pages outside of this site using the standard Markdown link format: 

`[Page Title](http://www.site.com/path/page.html)]`

> **Example**:
> 
> To refer to the [Coveo Cloud V2](http://www.coveo.com/go?dest=cloudhelp&lcid=9&context=231) online help page: 
> 
> `[Coveo Cloud V2](http://www.coveo.com/go?dest=cloudhelp&lcid=9&context=231)`

## Renaming or Moving Files

There is no content management system (CMS) in Jekyll that automatically manages links between articles. When you rename or move a file, you must find and replace  all links or references to this file. 
