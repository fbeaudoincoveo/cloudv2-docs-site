---
layout: content-2-panel
title: Determining if the Query Pipeline is Coded in the Search Interface
categories: migrated
---

# Determining if the Query Pipeline is Coded in the Search Interface

In your Coveo Cloud organization, you can create several query pipelines to address the needs of your various Coveo-powered search interfaces and panels (see [Creating and Managing Query Pipelines](http://www.coveo.com/go?dest=cloudhelp&lcid=9&context=128)).

Your setup can also use a number of mechanisms to select which query pipeline is used for a specific query (see [Query Pipeline Routing Best Practices and Rules](http://www.coveo.com/go?dest=cloudhelp&lcid=9&context=164)).  

You must use browser developer tools to determine if a query pipeline is coded directly in a search interface.

**To determine if a query pipeline is hardcoded in the Search Interface**

1.   In your preferred browser, access your JavaScript search interface.
2.   Open the developer tools console, select the **Network** tab, and then select the **XHR** filter.
3.  Back to the search interface, perform a query.
4.  In the developers tool console, select the last search event with a `POST` method.
5.  In the **Headers** tab, in the **Form Data** section, look for a `Pipeline` line and its value.
    The  `Pipeline` line is present only when the pipeline is hardcoded in the JavaScript Search interface.  

 

 

 

## Attachments:

![](images/icons/bullet_blue.gif){width="8" height="8"} [ConsolePipeline.png](attachments/36637894/37096157.png) (image/png)

