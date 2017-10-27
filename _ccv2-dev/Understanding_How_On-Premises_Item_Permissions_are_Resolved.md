---
slug: "120"
layout: content-2-panel
title: Understanding How On-Premises Item Permissions are Resolved
categories: migrated
---

# Understanding How On-Premises Item Permissions are Resolved

Secured on-premises repositories follow a permission model to control who can access each item they contain. The permission model complexity can range from allowing full anonymous access to requiring the resolution of permissions for several permission levels, each containing one or more permission sets (allowed and denied security identities) (see [Permission Levels and Sets](http://www.coveo.com/go?dest=adminhelp70&lcid=9&context=4203)). Item permissions are expressed as unique security identities (users, groups, and virtual groups) allowed or denied to view secured content in Coveo search results. 

Coveo Cloud internally uses emails to uniquely identify an authenticated user who performs a query. So at some point, allowed or denied users or groups associated with items must be resolved, more precisely, groups members must be expanded to users, and users must be mapped to their corresponding emails. 

**Example:**

You index a Microsoft Windows file repository. Only a few Active Directory (AD) users and one group are allowed to see a given file. This is the information pushed with the item in the source. At this point, we do not know which AD users are members of the group and what are the user emails.

A few components are needed to resolve the permissions for a given on-premises secured repository:

-   In your Coveo Cloud organization:
    -   A Secured Source
    -   An Expanded Security Provider associated with your Secured Source (see [Creating an Identity Provider for a Secured Push Type Source](Creating_an_Identity_Provider_for_a_Secured_Push_Type_Source))

<!-- -->

-   On-premises:
    -   A Crawling Module configured to extract permissions (see [Coveo Cloud V2 On-Premises Crawling Module](https://developers.coveo.com/x/3oYkAg))
        The Crawling Module extracts items and their permissions from on-premises repositories and sends them to your Coveo Cloud. 
    -   A Permission Expansion Tool (comes with Security Providers) (see [Configuring a Permission Expansion Tool for a Secured Source](https://developers.coveo.com/x/5IYkAg))
        The Permission Expansion Tool is an independent module that acts as a proxy and locally simulates the cloud Expanded Security Provider associated with your source and repository type. Its purpose is to relay extracted permissions information between the cloud Expanded Security Provider and the on-premises Security Provider. The Security Provider will be configured to resolve permissions in a format known by the Cloud. 

        **Example:**

        For a Microsoft Windows file repository, the Active Directory Security Provider resolves users in the email format.

## At indexing time

The workflow to resolve the permissions for an on-premises secured repository is described below and illustrated with the simplified schema. 

![](attachments/35949086/36176801.png)

1.  The Crawling Module extracts the items with their permissions and sends them to the Push API. 
2.  The Push API associates the permissions to the Expanded Security Provider associated with your secured source. 
3.  On-premises, asynchronously, the Permission Expansion Tool:
    1.  Starts a local Security Provider of your repository type. 
    2.  Asks the Cloud (though the Push API) for all the permissions associated with the cloud Expanded Security Provider. 
    3.  Sends them to the on-premises Security Provider, which retrieves group members and user mappings from the repository. 
    4.  Sends the resolved users and mappings back to the cloud Expanded Security Provider through the Push API. 

4.  The Security Identities Cache can now ask the Expanded Security Provider the resolution for your push type Secured Source, as it does for other cloud sources. 

## At query time

Once your secured on-premises content is made searchable, search interface end-users can only access the content they are allowed to view (see What happens at Query Time?). 

 

## Attachments:

![](images/icons/bullet_blue.gif){width="8" height="8"} [Untitled drawing.jpg](attachments/35949086/36176792.jpg) (image/jpeg)
![](images/icons/bullet_blue.gif){width="8" height="8"} [CoveoCloudV2PermissionExpansionToolSchema.png](attachments/35949086/36176799.png) (image/png)
![](images/icons/bullet_blue.gif){width="8" height="8"} [CoveoCloudV2PermissionExpansionToolSchema (1).png](attachments/35949086/36176798.png) (image/png)
![](images/icons/bullet_blue.gif){width="8" height="8"} [CoveoCloudV2PermissionExpansionToolSchema (1).png](attachments/35949086/36176797.png) (image/png)
![](images/icons/bullet_blue.gif){width="8" height="8"} [CoveoCloudV2PermissionExpansionToolSchema.png](attachments/35949086/36176793.png) (image/png)
![](images/icons/bullet_blue.gif){width="8" height="8"} [CoveoCloudV2PermissionExpansionToolSchema.jpg](attachments/35949086/36176800.jpg) (image/jpeg)
![](images/icons/bullet_blue.gif){width="8" height="8"} [CoveoCloudV2PermissionExpansionToolSchema (2).png](attachments/35949086/36176801.png) (image/png)

