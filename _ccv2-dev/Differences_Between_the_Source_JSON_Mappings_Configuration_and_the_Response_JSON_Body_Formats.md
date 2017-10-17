---
slug: "63"
layout: content-2-panel
title: Differences Between the Source JSON Mappings Configuration and the Response JSON Body Formats
categories: migrated
---

# Differences Between the Source JSON Mappings Configuration and the Response JSON Body Formats

> The Coveo Cloud V2 indexing pipeline mapping feature is available in beta version (January 7 2017 introduction). To ensure backward compatibility, the source JSON mappings configuration format is still supported (see Mapping - Tab).

The following table shows the differences between the source JSON mappings configuration and the response JSON body formats.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Source JSON mappings configuration format</th>
<th>Response JSON body format - GET mappings configuration</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><div class="code panel pdl" style="border-width: 1px;">
<div class="codeContent panelContent pdl">
<pre style="font-size:12px;"><code> [
  {
    &quot;id&quot;: &quot;rule_ID&quot;,
    &quot;kind&quot;: &quot;COMMON&quot;,
    &quot;fieldName&quot;: &quot;field_name&quot;,
    &quot;extractionMethod&quot;: &quot;METADATA&quot;,
    &quot;content&quot;: &quot;%[metadata_name]&quot;
  },
  {
    &quot;id&quot;: &quot;rule_ID&quot;,
    &quot;kind&quot;: &quot;MAPPING&quot;,
    &quot;type&quot;: &quot;item_type&quot;,
    &quot;fieldName&quot;: &quot;field_name&quot;,
    &quot;extractionMethod&quot;: &quot;METADATA&quot;,
    &quot;content&quot;: &quot;%[metadata_name]&quot;
  }
]</code></pre>
</div>
</div></td>
<td><div class="code panel pdl" style="border-width: 1px;">
<div class="codeContent panelContent pdl">
<pre style="font-size:12px;"><code>{
  &quot;common&quot;: {
    &quot;rules&quot;: [
      {
        &quot;field&quot;: &quot;field_name&quot;,
        &quot;content&quot;: [
          &quot;%[metadata_name]&quot;
        ],
        &quot;id&quot;: &quot;rule_ID&quot;
      }
  },
  &quot;types&quot;: [
    {
      &quot;rules&quot;: [
        {
          &quot;field&quot;: &quot;field_name&quot;,
          &quot;content&quot;: [
            &quot;%[metadata_name]&quot;
          ],
          &quot;id&quot;: &quot;rule_ID&quot;
        }
      ],
      &quot;type&quot;: &quot;item_type&quot;,
      &quot;id&quot;: &quot;item_type&quot;
    }
  ]
}</code></pre>
</div>
</div></td>
</tr>
</tbody>
</table>

Here are the details about the main differences between the two formats:

-   In source JSON mappings configuration format, the mapping rule types are `COMMON` and `MAPPING`.

    > Do not confuse this value with the metadata origin `mapping`.

    In the response JSON body, mapping rules are grouped by type. `types` contains the rules associated with a specific item type.

-   `fieldName` and `field` contain the name of the index field to be populated.

-   In the response JSON body format, the extraction method is omitted.
    A mapping rule can contain one or more metadata name placeholders mixed with some literal text (see [Mapping Rule Syntax Examples](https://developers.coveo.com/x/YwwvAg#IndexingPipelineMappingConcepts-MappingRuleSyntaxExamples)).

