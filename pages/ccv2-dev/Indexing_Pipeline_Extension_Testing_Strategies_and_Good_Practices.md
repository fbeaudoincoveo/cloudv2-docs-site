---
layout: content-2-panel
title: Indexing Pipeline Extension Testing Strategies and Good Practices
categories: migrated
---

# Indexing Pipeline Extension Testing Strategies and Good Practices

This topic compares available strategies to test indexing pipeline extensions. The most obvious method to test an extension is to apply it to a source, rebuild the source and validate if the script did what was expected. This method can quickly be very tedious, particularly for a source with a large number of items, since you have to wait for a rebuild at each test, but goes through the indexing pipeline. 

Simulation alternatives such as the [Test an Extension](https://platform.cloud.coveo.com/docs?api=Extension#!/Indexing32Pipeline32Extensions/rest_organizations_paramId_extensions_paramId_test_post) API call, and the Coveo Labs pipeline-extension-manager (that relies on the  Test an Extension API call) allow to get results much faster, but come with limitations such as simulated metadata from index fields. Metadata that was not mapped to a field will not be available to your extension during the simulation. Similarly, metadata mapped to fields with an unmatching name will not be available with the proper name. 

> As a developer, using the [Test an Extension](https://platform.cloud.coveo.com/docs?api=Extension#!/Indexing32Pipeline32Extensions/rest_organizations_paramId_extensions_paramId_test_post)  API call may appear to you as the first choice. While the implementation of an automated testing process is easier with the API, be aware that only indexed metadata is available with the API call as unmapped metadata is not indexed. Furthermore, indexed metadata is retrievable only with the mapped field name and not with the original metadata name unless they are the same. Before deciding on a testing strategy, you should be aware of the various limitations.

The following table provides and overview of the different indexing pipeline extension test methods.

<table>
<colgroup>
<col width="25%" />
<col width="25%" />
<col width="25%" />
<col width="25%" />
</colgroup>
<thead>
<tr class="header">
<th>Method</th>
<th>Testing goal</th>
<th>Advantages</th>
<th>Disadvantages</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Using the Coveo Labs <a href="https://github.com/coveo-labs/pipeline-extension-manager/tree/master/misc/chrome_extension">pipeline-extension-manager</a></td>
<td>When you want to quickly test one or a few extension scripts without referring to unmapped metadata.</td>
<td><ul>
<li>Easiest and quickest way to test an indexing pipeline extension script on a single item.</li>
<li>Easier to use than the  <a href="https://platform.cloud.coveo.com/docs?api=Extension#!/Indexing32Pipeline32Extensions/rest_organizations_paramId_extensions_paramId_test_post">Test an Extension</a> API call since it does not require developers skills.</li>
<li>Easily find and select an item to test with the use of a search page.</li>
<li>No need to edit the source JSON configuration to test parameters.</li>
</ul></td>
<td><ul>
<li>Only indexed metadata is available. Only metadata mapped to a field are indexed.</li>
<li>Metadata are not retrievable with their original metadata name, but rather with the mapped field name.</li>
<li>The use of metadata origin is worthless since unmapped values are not indexed.</li>
<li>May need to map metadata and re-index a whole source to access metadata.</li>
<li>Unable to test past versionId of an extension. Only current extension can be tested.</li>
<li>Unable to set <code>actionOnError</code> and <code>condition</code> values when testing.</li>
</ul></td>
</tr>
<tr class="even">
<td>Using the <a href="https://platform.cloud.coveo.com/docs?api=Extension#!/Indexing32Pipeline32Extensions/rest_organizations_paramId_extensions_paramId_test_post">Test an Extension</a> API call</td>
<td>When a developer needs to implement automated tests on multiple extension scripts without referring to unmapped metadata.</td>
<td><ul>
<li>Easier to implement an automated testing process with the API call.</li>
<li>Immediate results when testing an indexing pipeline extension script on a single item.</li>
</ul></td>
<td><ul>
<li>Only indexed metadata is available. Only metadata mapped to a field are indexed.</li>
<li>Metadata are not retrievable with their original name, but rather with the mapped field name.</li>
<li>The use of metadata origin is worthless since unmapped values are not indexed.</li>
<li>May need to map metadata and re-index a whole source to access metadata.</li>
<li>Requires developers skills to create or retrieve the document model and feed it to the API.</li>
</ul></td>
</tr>
<tr class="odd">
<td><a href="Logging_Messages_from_an_Indexing_Pipeline_Extension">Logging Messages from an Indexing Pipeline Extension</a></td>
<td><p>When you need to test parts of a single extension script and/or when you need to use unmapped metadata.</p>
<div class="panel" style="border-width: 1px;">
<div class="panelHeader" style="border-bottom-width: 1px;">
<strong>Example:</strong>
</div>
<div class="panelContent">
<p>In this script, the log messages gives detail for each step. Therefore, a developer can validate assigned values and test if-else statements, for instance.</p>
<div class="code panel pdl" style="border-width: 1px;">
<div class="codeContent panelContent pdl">
<pre style="font-size:12px;"><code>itemSize = document.get_meta_data_value(&#39;size&#39;)
log(&quot;1- Size of item: &quot; + str(itemSize[0]), &quot;Detail&quot;)
itemType = document.get_meta_data_value(&#39;filetype&#39;)
log(&quot;2- Type of item: &quot; + str(itemType[0]), &quot;Detail&quot;)

if int(itemSize[0]) &gt; 2000:
    log(&quot;item size is greater than 2000&quot;, &quot;Notification&quot;)
elif str(itemType[0]) == &#39;html&#39;:
    log(&quot;item type is html&quot;, &quot;Notification&quot;)
else:
    log(&quot;both conditions failed to match&quot;, &quot;Warning&quot;)</code></pre>
</div>
</div>
</div>
</div></td>
<td><ul>
<li>Easier to test a single line of code with a log message.</li>
<li>All metadata and metadata origin are available with their original name.</li>
<li>Use of try-except code blocks to manage explicitly specified script errors.</li>
<li>You can use the logging messages method jointly with the other three testing methods.<br />
<br />
</li>
</ul>
<div class="aui-message warning shadowed information-macro">
<div class="message-content">
<blockquote>
Logging messages while indexing a source with a few chosen items is a good practice and it is the best strategy in those situations:
</blockquote>
<ul>
<li>when you need to implement automated tests.</li>
<li>when you do not need to access unmapped metadata.</li>
<li>when you do not have developers skills.</li>
</ul>
</div>
</div></td>
<td><ul>
<li>The log values does not show up immediately in the  <a href="https://platform.cloud.coveo.com/admin/#/logs/browser/">Log Browser</a> page or in the SourceLogs API.</li>
<li>May need to index a whole source to find relevant log results to analyze.</li>
</ul></td>
</tr>
<tr class="even">
<td>Testing with a source containing a small number of items</td>
<td>When you need access to unmapped metadata in your extension script.</td>
<td><ul>
<li>All metadata and metadata origin are available with their original names.<br />
<br />
</li>
</ul></td>
<td><ul>
<li>The rebuild process takes time even with a very few elements.</li>
<li>Can be difficulty to find test relevant items to index.</li>
<li>Not always possible to index only a few items of a particular source.</li>
</ul></td>
</tr>
</tbody>
</table>

> When using a try-except code block in your extension script, you should be aware of good and bad practices.

**Good Practice:**

> The best practice is to catch explicitly specified errors to manage them.

```
myTitle = document.get_meta_data_value('title')
 
# An error is raised when "Coveo" is not part of the title
if "Coveo" not in myTitle:
    raise ValueError('Coveo not in the title')
 
# a try-except code block
try:
    myTitle = myTitle[0]
    myTitle = myTitle.upper()
    document.add_meta_data({'capsTitle':myTitle})
 
# This except block catches and logs the first ValueError that is raised in the script.
# When any other type of error is raised, the extension script fails.
except ValueError as e:
    log(str(e),'Error')
```

> Any error other than `ValueError` still raises a flag and makes this script fail. This practice helps to identify error in your extension script.

> Since catching an error within the code does not raise a flag, and results in a successfully indexed item, another good practice is to raise errors without catching them in the code. This way, you can retrieve the error message with the [Get specified source document logs](https://platform.cloud.coveo.com/docs?api=SourceLogsApi#!/Logs/post_organizations_organizationId) SourceLogs API call or in the administration console [Log Browser](https://platform.cloud.coveo.com/admin/#/logs/browser/) page. Furthermore, when binding the extension to a source in the JSON configuration or with the API call, you can manage the error by editing the `actionOnError` value to `SKIP_EXTENSION` or `REJECT_DOCUMENT` to your convenience.

**Bad Practice:**

> You should never try to catch an exception with a generic `except` code block.

```
myTitle = document.get_meta_data_value('title')
 
# An error is raised when "Coveo" is not part of the title
if "Coveo" not in myTitle:
    raise ValueError('Coveo not in the title')
 
# a try-except code block
try:
    myTitle = myTitle[0]
    myTitle = myTitle.upper()
    document.add_meta_data({'capsTitle':myTitle})
 
# This except block catches the first error that is raised in the script and logs a generic error message.
# Since any type of error is catched, this extension script result is always successful.
except:
    log('An error occurred','Error')
```

> This bad practice has huge consequences:

-   When there is an error, no flag is raised. There is no way to know if there was an error in the script.
-   When there is an error, it is catched without leaving a trace. There is no way to know which type of error occurred since the `except` block does not discriminate.
-   Error or not, the item is successfully indexed. There is no way to know if the extension applied correctly to the item.

> If your indexing pipeline extension script modifies source permissions, ensure your code covers every possible use case to prevent disclosing restricted access items to unauthorized users.

 


