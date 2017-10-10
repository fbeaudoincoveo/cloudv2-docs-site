---
layout: content-2-panel
title: Understanding Push API Processing Delay
categories: migrated
---

# Understanding Push API Processing Delay

You may notice that items you send to the [Coveo Cloud V2 push API](Using_the_Push_API) are not immediately searchable. This is normal. 

The complete processing time (between the moment items are pushed and the moment they become searchable) typically takes several minutes. You cannot change or reduce this delay. 

The total time is the result of cumulated small delays to go through each Coveo Cloud V2 processing pipeline steps. As they transit through the indexing pipeline, you can see pushed items appear in the Administration Console **Sources** page (and in the **Activity of Source** panel) before they become searchable (such as in the Administration Console **Content Browser** page or in a search interface).  

The Coveo Cloud V2 infrastructure automatically scales following load variations to maintain processing time to a minimum value. The Coveo team constantly monitors the delays and regularly fine-tunes the infrastructure scaling mechanisms to minimize the delays.  

The total push API processing time may vary depending on a number of factor such as:

-   Load variations to the push API queue (multi-tenants)
-   Processing delays (such as typically 300mS for push API calls) 
-   Infrastructure scaling provisioning (such as a few seconds for Lambdas)
-   Management of item processing queues
-   Number and size of pushed items to process 
-   Index commits frequency and thresholds (typically every minute)

 

**Example:**

You send one item to a push type source to test the push API. In the Administration Console **Sources** page, within 2 minutes, you see **1 item processed** appear in the **Status** column for your source. The item becomes searchable a few minutes later.

You send 1000 items to the same source. In the Administration Console **Sources** page, within less than a minute the Status column shows quickly increasing processed items that become searchable apparently faster than the. The delays may be shorter simply because the minimum number of items required to start processing queues was immediately reached.


