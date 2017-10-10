---
layout: content-2-panel
title: Storage and Recommendation Allocation (Coveo Platform)
categories: migrated
toc: ccv2-dev
---

# Storage and Recommendation Allocation (Coveo Platform)

**In this topic:**

-   [Storage](#storage)
-   [Recommendation](#recommendation)

This topic presents index storage and recommendation limits associated with Coveo Platform solutions.  

## Storage

The storage allocation for a Coveo Platform customer is limited to a certain number of items per Coveo Cloud production organization. An *"Item" * means an element of content in the Coveo Cloud index such as a document, an email, an HTML page, or a database record. 

Each customer is allocated items based on the queries per month (QPM) and Authorized Users specified in the order and information in the following table. 

Item allocation
Coveo solution

Item allocation
 
Per 100 K QPM

Per Authorized User

Included
**Website & Portal**

1 M

N/A

**Contact Center**

N/A

20 K
**Intranet**

2.5 K
Additional
Minimum increments
All
1 M  <sup>[1](Storage_and_Recommendation_Allocation__Coveo_Platform_)</sup>

Limit
50 M <sup>[2](Storage_and_Recommendation_Allocation__Coveo_Platform_)</sup>

*Note 1 - Multiple editions or additional billable units (QPM or Authorized User) cumulate up to a maximum of 50 M items.*

*Note 2 - For** greater allocation, c**ontact * *[Coveo Sales](http://www.coveo.com/en/company/contact-us).*

**Example:**

You have two Coveo Platform solution licenses for which item allocations cumulate:

1.  Website & Portal with 1 M QPM Item allocation: 1 M items/100 K QPM x 1 M QPM = 10 M items
2.  Contact Center with 1000 Authorized Users Item allocation: 20 K items/Authorized Users x 1000 Authorized Users = 20 M items

The total item allocation is 30 M items.

## Recommendation

The Coveo Machine Learning Recommendations feature presents a user with most relevant content consulted by other users with a similar navigation history (see [Recommendations Feature](http://www.coveo.com/go?dest=cloudhelp&lcid=9&context=183#Recommendations_Feature)). 

Each Coveo Platform  customer is allocated a limited number of recommendations (expressed in recommendations per month \[RPM\]) per Coveo Cloud production organization based on the order and information in the following table.

 

Item allocation
Coveo Solution

 

Recommendation allocation
Per 100 K QPM

Per Authorized User

Included
**Website & Portal**

300 K RPM

N/A

**Contact Center**

N/A

4 K RPM
**Intranet**

500 RPM
Additional purchase
minimum increments

All
500 K RPM <sup>[3](Storage_and_Recommendation_Allocation__Coveo_Platform_)</sup>

*Note 3 - Additional billable units (QPM or Authorized User) cumulate.*

**Example:**

You have two Coveo Platform licenses for which recommendation allocations cumulate:

1.  Website & Portal with 1 M QPM
    Recommendation allocation: 300 K RPM/100 K QPM x 1 M QPM = 3 M RPM
2.  Contact Center with 1000 Authorized Users
    Recommendation allocation: 4 K RPM/Authorized Users x 1000 Authorized Users = 4 M RPM

The total allocation is 7 M RPM.


