---
slug: "53"
layout: content-2-panel
title: Creating a Push Type Source
categories: migrated
---

# Creating a Push Type Source

The following procedure describes how to create a Coveo Cloud V2 custom source that can be populated using the Push API (see [Using the Push API](Using_the_Push_API)). 

#### From the Coveo Cloud V2 Administration Console

You can use the Coveo Cloud V2 administration console **Sources** page to easily create a push type source and get an API key with appropriate privileges (see [Add/Edit a Push Source - Panel](http://www.coveo.com/go?dest=ccv2ac&context=53)). 

#### From the API

You can create a push type source using the Coveo Cloud Source API, described below using the Swagger generate site: 

1.  Go to <https://platform.cloud.coveo.com/docs>
2.  In the header drop-down list, select **Source**.
3.  Expand the Sources : Source Resource section, and then click POST /rest/organizations/{organizationId}/sources.
4.  In the POST /rest/organizations/{organizationId}/sources panel upper-right corner, click the OFF switch.
5.  In the Select OAuth2.0 Scopes dialog box that appears, click Authorize. 
6.  If not already logged in to the Coveo Cloud platform with an account that has the privileges to create sources, at the log in dialog, log in to the platform. 
7.  Back in the POST /rest/organizations/{organizationId}/sources panel:
    1.  In the organizationId box, enter the ID of your organization. It is your organization name, without spaces or other special characters, all in lowercase.  
        In the sourceModel box, enter the following JSON in which you only change the name value.

        **Example:**

        When you create a source containing only public items that you want to make available to all search users:

        ```
        {
            "sourceType": "PUSH",
            "name": "MyPushEnabledPublicSource",
            "sourceVisibility": "SHARED",
            "pushEnabled": true
        }
        ```

        Note:

        > You can also make the source content only visible to you by setting `"sourceVisibility": "PRIVATE"`.

        When you also want to push permissions to your secured source, you must also link to the identity provider you created for your source:

        ```
        {
            "sourceType": "PUSH",
            "name": "MyPushEnabledSource",
            "sourceVisibility": "SECURED",
            "pushEnabled": true,
            "securityProviderReferences":["mySecurityProvider"]
        }
        ```

        Note:

        > You can also update the source later using the `PUT/rest/organizations/{organizationId}/sources/{sourceId}` method.

        >  

    2.  Click Try it out!. 

        When you have the appropriate privileges, the Response Body box contains only the ID of your source similar to the following example:

        ```
        {
          "id": "myorgid-someguid"
        }
        ```

8.  In the administration console **Sources** page, validate that your source is created. 

#### What's Next

Add content to your custom source (see Pushing Items to a Source or Batch Pushing Encrypted Files and Permissions to a Source).
