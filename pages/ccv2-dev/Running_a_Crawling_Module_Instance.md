---
layout: content-2-panel
title: Running a Crawling Module Instance
categories: migrated
---

# Running a Crawling Module Instance

Crawling Modules instances run with a task scheduling tool of your choice to make your content searchable and maintain its freshness (see What Should Be the Frequency of Source Refresh Schedules?).

You can create schedules for the following source content updates:

-   Initial rebuild
-   Regular refreshes
-   When available for your Crawling Module type, incremental refresh

#### To start an operation on the Crawling Module

Run a command like the following:

**Example**

```
C:\Crawling_module\your_working_folder\bin\crawler.py -start [refresh/rebuild/incremental]
```


