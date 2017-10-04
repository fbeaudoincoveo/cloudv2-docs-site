---
layout: content-2-panel
title: Indexing Pipeline Extension Condition Syntax Reference
categories: migrated
---

# Indexing Pipeline Extension Condition Syntax Reference

In this topic: /\*\*/ Syntax Condition Syntax Examples Pitfalls to Avoid You can optionally add conditions on your extensions to control on which items they must be executed.  The condition is part of the extension configuration when you apply the extension to a source, not in the extension Python script itself.  This way, the Coveo Cloud indexing pipeline loads and executes the extension only for items for which the condition evaluates to True, allowing to optimize crawling performances. 

You can apply an extension to a given source and specify a condition from the Coveo Cloud administration console (see Applying an Extension to a Source). Alternatively, you can also apply an extension to a given source and specify a condition using the Coveo Cloud V2 API (see Applying an Indexing Pipeline Extension to a Source with the API). 

Refer to the information below for extension condition syntax and examples. 

## Syntax

Indexing pipeline extension conditions are essentially build with metadata, metadata values, and operators. 

-   Metadata syntax: `%[metadataName]`
-   Supported operators: `==`, `NOT`, `AND`, `OR`, `()`****

Notes:

-   Operators are case insensitive.
-   Values can be delimited in single or double quotes (`"value"` and *'*`'value'` are equivalent and can be mixed in the same condition).
-   Metadata name can contain special characters (such as `%`, `]`, `[`, `"` etc), but they must be escaped (e.g.: `%[meta1\[test\]]` is valid, `%[meta1[test]]` is not).
-   Extensions without conditions are executed for all items.

## Condition Syntax Examples

The following table presents examples of the different condition syntax features that can help you apply useful indexing pipeline extensions to sources (see [Applying an Indexing Pipeline Extension to a Source](https://developers.coveo.com/x/IQMvAg)).

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Condition syntax example</th>
<th>Evaluate to true if</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><code>%[meta1]</code></td>
<td><p>The metadata <code>meta1</code> exists on the item.</p></td>
</tr>
<tr class="even">
<td><code>NOT %[meta1]</code></td>
<td><p>The metadata <code>meta1</code> does not exist on the item.</p></td>
</tr>
<tr class="odd">
<td><code>%[meta1] == &quot;value&quot;</code></td>
<td>The value of <code>meta1</code> equals <code>value</code>.</td>
</tr>
<tr class="even">
<td><code>NOT %[meta1] == &quot;value&quot;</code></td>
<td><p>The metadata <code>meta1</code> exists but its value does not equal <code>value</code>.</p></td>
</tr>
<tr class="odd">
<td><code>%[meta1] AND %[meta2]</code></td>
<td><p>Both metadata exist on the item.</p></td>
</tr>
<tr class="even">
<td><code>%[meta1] == &quot;value&quot; AND %[meta2] == &quot;value&quot;</code></td>
<td><p>Both metadata values equal <code>value</code>.</p></td>
</tr>
<tr class="odd">
<td><code>%[meta1] OR %[meta2]</code></td>
<td>At least one of the metadata exists on the item.</td>
</tr>
<tr class="even">
<td><code>%[meta1] == &quot;value&quot; OR %[meta2] == &quot;value&quot;</code></td>
<td>At least one of the metadata value equals <code>value</code>.</td>
</tr>
<tr class="odd">
<td><code>(%[meta1] OR %[meta2]) AND %[meta3]</code></td>
<td><p>At least one of the metadata joined by <code>OR</code> exists on the item.</p>
<p>The metadata <code>meta3</code> exists on the item.</p>
<div class="aui-message warning shadowed information-macro">
<div class="message-content">
<blockquote>
When using more than one operator in a condition without parenthesis, the condition is evaluated with the following operator priority: <code>NOT</code> &gt; AND &gt; OR.
</blockquote>
</div>
</div></td>
</tr>
<tr class="even">
<td><code>%[meta1] == [&quot;value1&quot;, &quot;value2&quot;]</code></td>
<td><p>The metadata <code>meta1</code> equals either [&quot;value1&quot;, &quot;value2&quot;] or [&quot;value2&quot;, &quot;value1&quot;].</p></td>
</tr>
</tbody>
</table>

## Pitfalls to Avoid

-   You cannot directly compare one metadata to another (e.g.: `%[meta1] == %[meta2]`).
    Rather use:  `%[meta1] == 'value' AND %[meta2] == 'value'`
-   You cannot use operators between values (e.g.: `%[fruit] == 'apple' OR 'orange'` is not valid).
    Rather use: `%[fruit] == 'apple' OR %[fruit] == 'orange'`
-   You cannot use the inequality operator `!=`.
    Rather use `NOT %[meta1] == 'value'`.
-   Conditions do not support specifying an origin (`crawler`, `converter`, `mapping`). The comparisons are always done using the latest value for the metadata so you must be aware of the indexing pipeline stage at which your extension is executed.  

 
