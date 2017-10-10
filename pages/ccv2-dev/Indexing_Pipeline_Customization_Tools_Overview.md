---
layout: content-2-panel
title: Indexing Pipeline Customization Tools Overview
categories: migrated
---

# Indexing Pipeline Customization Tools Overview

This topic provides an overview of Coveo Cloud V2 tools and features that you can use to customize how each source item is indexed through the indexing pipeline (see [Coveo Cloud V2 Indexing Pipeline](http://www.coveo.com/go?dest=cloudhelp&lcid=9&context=336)). You can sometimes use more than one tool to achieve a specific indexing customization goal, but some tools may impact performances or be available only for specific source types.  

**Example:**

As a developer, indexing pipeline extensions Python scripts may appear to you as the first choice because with code you can do what you want. While you can do a lot of things with indexing pipeline extensions, they can impact indexing performances and there is often another tool or feature that can do the same.

 

The following table lists customization tools starting with the ones that are the most appropriate to use either because of their effectiveness, ease of use, or performance optimization.  

<table>
<colgroup>
<col width="20%" />
<col width="20%" />
<col width="20%" />
<col width="20%" />
<col width="20%" />
</colgroup>
<thead>
<tr class="header">
<th>Tool / feature</th>
<th>Indexing goal</th>
<th>How to use</th>
<th>Advantages</th>
<th>Disadvantages</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>URL filters</td>
<td><ul>
<li>Control the indexing scope, choosing which repository pages or sections to include in your source.</li>
</ul></td>
<td><ul>
<li>For Web sources, configuration from the administration console source (see <a href="http://www.coveo.com/go?dest=cloudhelp&amp;lcid=9&amp;context=276">Add/Edit Web Source - Panel</a>).</li>
<li>Other URL based source types:
<ul>
<li>Edit the source JSON configuration (see <a href="http://www.coveo.com/go?dest=cloudhelp&amp;lcid=9&amp;context=349#Add_Source_Filters">Add Source Filters</a>).</li>
<li>Create/update a source from the API (see <a href="https://platformdev.cloud.coveo.com/docs?api=Source#/Sources">Sources : Source Resource</a>)</li>
</ul></li>
</ul></td>
<td><ul>
<li>Efficiently processed by the Crawling stage.</li>
<li>Wildcard or regex flexibility.</li>
<li>For Web sources, easy configuration from the administration console (see <a href="http://www.coveo.com/go?dest=cloudhelp&amp;lcid=9&amp;context=276">Add/Edit a Web Source - Panel</a>).</li>
</ul></td>
<td><ul>
<li>Applicable only to URL based source types (e.g. Web and Sitemap).</li>
<li>For Sitemap sources, less easy configuration from the source JSON.</li>
</ul></td>
</tr>
<tr class="even">
<td><a href="http://www.coveo.com/go?dest=cloudhelp&amp;lcid=9&amp;context=284">Mappings</a></td>
<td><ul>
<li>Extract original document metadata values to populate specific Coveo index fields.</li>
<li>Customize or create an index item body for object based source types such as Salesforce or a database.</li>
</ul></td>
<td><ul>
<li>Configuration from the Coveo Cloud V2 Administration Console (see <a href="http://www.coveo.com/go?dest=cloudhelp&amp;lcid=9&amp;context=284">Mapping - Tab</a>).</li>
<li>Create/update mappings from the API (see <a href="https://platformdev.cloud.coveo.com/docs?api=Source#/Mappings">Mappings : Mapping Resource</a>).<br />
<br />
</li>
</ul></td>
<td><ul>
<li>Efficiently processed by Mapping stage.</li>
<li>Conditional mappings based on item type.</li>
<li>Can concatenate one or more metadata and include personalized text with the Literal option.</li>
<li>Can edit body content (see Add/Edit Body Mapping).</li>
<li>Can get metadata value from a specific stage with the origin suffix (see <a href="http://www.coveo.com/go?dest=cloudhelp&amp;lcid=9&amp;context=338">Mapping Rules Syntax Reference</a>).</li>
</ul></td>
<td><ul>
<li>Cannot programmatically process metadata values.</li>
</ul>
<p> </p></td>
</tr>
<tr class="odd">
<td><a href="http://www.coveo.com/go?dest=cloudhelp&amp;lcid=9&amp;context=277">Web scraping configuration</a></td>
<td><ul>
<li>Exclude specific web page sections.</li>
<li>Extract specific content to create metadata.</li>
<li>Create sub-items.</li>
</ul></td>
<td><ul>
<li>For Web sources, configuration from the Coveo Cloud V2 Administration Console (see Add or Edit a Web Source).</li>
<li>For a Sitemap source, edit the source JSON configuration (see Add a Web Scraping Configuration to a Sitemap Source).</li>
<li>For both source types, create/update source from the API (see <a href="https://platform.cloud.coveo.com/docs?api=Source#!/Sources/rest_organizations_paramId_sources_paramId_put">Update a source from simple configuration</a>).</li>
</ul></td>
<td><ul>
<li>Efficiently processed by the Crawling stage.</li>
<li>Coveo Labs Chrome extension available to easily create web scraping configurations (see <a href="https://github.com/coveo-labs/web-scraper-helper">web-scraper-helper</a>).</li>
<li>Exclusion of repeating web page parts from index (e.g.: header, sidebar, footer) (see <a href="http://www.coveo.com/go?dest=cloudhelp&amp;lcid=9&amp;context=277#Exclusion">Exclusion</a>).</li>
<li>Extraction of content from HTML elements with XPATH and CSS locators to enrich metadata (see <a href="http://www.coveo.com/go?dest=cloudhelp&amp;lcid=9&amp;context=277#Selectors">Selectors</a> ).</li>
<li>Splitting parts of a web page into more than on index items (see <a href="http://www.coveo.com/go?dest=cloudhelp&amp;lcid=9&amp;context=277#subitems">SubItems</a>).</li>
</ul></td>
<td><ul>
<li>Available only for Web and Sitemap sources.</li>
<li>Requires developers skills to create the JSON web scraping configuration and take full advantage of XPATH and CSS expressions.</li>
</ul></td>
</tr>
<tr class="even">
<td><a href="https://developers.coveo.com/x/sAAvAg">Indexing Pipeline Extension</a></td>
<td><ul>
<li>When not possible with the above tools:
<ul>
<li>Add/modify metadata.</li>
<li>Reject items (in pre-conversion scripts).</li>
<li>Exclude specific web page sections.</li>
</ul></li>
</ul>
<ul>
<li>Use external resources and services (e.g. image recognition API to inject metadata).</li>
<li>Add/modify item permissions (e.g. for a Push source for which the crawler does not associate permissions).</li>
</ul></td>
<td><ul>
<li>Modify/create appropriate Python scripts (see <a href="Document_Object_Python_API_Reference">Document Object Python API Reference</a> and <a href="Indexing_Pipeline_Extension_Script_Samples">Indexing Pipeline Extension Script Samples</a>).</li>
<li>Add script to the organization as an extension (see <a href="http://www.coveo.com/go?dest=cloudhelp&amp;lcid=9&amp;context=334">Add/Edit an Extension - Panel</a>).</li>
<li>Apply an extension to a source (see <a href="http://www.coveo.com/go?dest=cloudhelp&amp;lcid=9&amp;context=411">Edit Source Extensions: [SourceName] - Panel</a> ).</li>
</ul></td>
<td><ul>
<li>Coveo Labs Chrome extension available to get samples and test indexing pipeline extensions (see <a href="https://github.com/coveo-labs/pipeline-extension-manager/tree/master/misc/chrome_extension#coveo-extension-manager">Coveo extension manager</a>).</li>
<li>Accessibility to third party services and databases.</li>
<li>Flexibility of Python language and available libraries (see <a href="Python_Modules_Available_to_Indexing_Pipeline_Extensions">Python Modules Available to IPE</a>).</li>
<li>Extension code reuse with conditional execution and extension parameters.</li>
<li>Index item processing to (see <a href="Document_Object_Python_API_Reference">Document Object Python API Reference</a>):<br />

<ul>
<li>Manage metadata.</li>
<li>Manage permissions.</li>
<li>Manage security providers.</li>
<li>Manage data streams.</li>
<li>Retrieve the URI.</li>
<li>Set log messages (see Logging Messages from an Indexing Pipeline Extension).</li>
</ul></li>
</ul></td>
<td><ul>
<li>Requires developer skills to create the Python scripts.</li>
<li>Extension execution for each index item affect indexing performances.</li>
<li>Limit of 10 indexing pipeline extensions per organization.</li>
<li>Extension script execution limited to 5 seconds.</li>
</ul></td>
</tr>
</tbody>
</table>


