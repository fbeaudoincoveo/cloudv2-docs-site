---
slug: "62"
layout: content-2-panel
title: Determining Which Coveo Cloud Query Pipeline a Search Page Uses
categories: migrated
---

# Determining Which Coveo Cloud Query Pipeline a Search Page Uses

In your Coveo Cloud organization, you can create several query pipelines to address the needs of your various Coveo-powered search interfaces and panels (see [Creating and Managing Query Pipelines](http://www.coveo.com/go?dest=cloudhelp&lcid=9&context=128)).

Your setup can also use a number of mechanisms to select which query pipeline is used for a specific query (see [Query Pipeline Routing Best Practices and Rules](http://www.coveo.com/go?dest=cloudhelp&lcid=9&context=164)).  

You may therefore sometimes not be sure and want to clearly identify which Coveo Cloud query pipeline is used by a specific query in a search interface or panel.

**To determine which query pipeline is used**

1.  Using your favorite browser, access the search interface or panel for which you want to determine the query pipeline that is used. 
2.  Open the browser developer tools. 
3.  Perform a search or your specific search. 
4.  In the browser developer tools, select the **Network** tab: 
    1.  In the list of events (under **Name**), select the latest call to the Coveo Cloud search API.
        The event name varies depending on the query string parameters, but the call is made to one of the following URL
        -   For Coveo Cloud V2: <https://platform.cloud.coveo.com/rest/search/v2/>
        -   For Coveo Cloud V1: <https://cloudplatform.coveo.com/rest/search/v2/>

    2.  In the **Response** tab for the selected event, in the top section of the JSON response, look for the `pipeline` key and then its value. 

        **Example:**

        In the following search JSON response example, the `pipeline` key is the seventh one, and the pipeline name is `default`.

        ```
        {
          "totalCount" : 122452,
          "totalCountFiltered" : 122452,
          "duration" : 271,
          "indexDuration" : 235,
          "requestDuration" : 243,
          "searchUid" : "1852cb7c-2557-424a-af34-ca0a341a9b05",
          "pipeline" : "default",
          "apiVersion" : 2,
          "basicExpression" : null,
          "advancedExpression" : null,
          "largeExpression" : null,
          "constantExpression" : null,
          "disjunctionExpression" : null,
          "mandatoryExpression" : null,
          ...
        ```

 
