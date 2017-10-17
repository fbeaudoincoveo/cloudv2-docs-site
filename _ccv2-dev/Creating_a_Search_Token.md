---
slug: "54"
layout: content-2-panel
title: Creating a Search Token
categories: migrated
toc: ccv2-dev
---

# Creating a Search Token

Search tokens are used by specific authenticated search page users to perform queries on the Coveo Cloud Platform (see Search Token Authentication).

When your secured content is made searchable, Coveo search results include only items that the user (or the group to which he belongs) is allowed to see.

This topic describes how to create a search token using the Search API.

 

Log into your [Coveo Cloud V2](https://platform.cloud.coveo.com/login) organization.

Create an API key that has the minimal privileges to request a search token (see API Access - Page).
In the administration console, underOrganization, access the API Access page, click Add key, and in the **Privileges** tab, select the **Enable** check box for the **Impersonate** privilege.

Create your search token.

1.  Use the following API call:

    ```
    POST http://platform.cloud.coveo.com/rest/search/token
    ```

2.  Your call must include the following HTTP headers:

    <table>
    <colgroup>
    <col width="50%" />
    <col width="50%" />
    </colgroup>
    <thead>
    <tr class="header">
    <th>Key</th>
    <th>Value</th>
    </tr>
    </thead>
    <tbody>
    <tr class="odd">
    <td><code>Authorization</code></td>
    <td><p><code>Bearer API_key&gt;</code></p></td>
    </tr>
    <tr class="even">
    <td><code>Content-Type</code></td>
    <td><code>application/json</code></td>
    </tr>
    </tbody>
    </table>

3.  Enter a JSON in a format similar to the following example:

    ```
    {
      "userIds": [
        {
          "name": "FirstnameFamilyname@mycompany.com",
          "provider": "Email Security Provider",
          "infos": {
            "key": "value",
            "key": "value"
          }
        }],
      "filter": "filter_name",
      "pipeline": "pipeline_name"
    }
    ```

    where you can add additional information on the user, assign a permission filter, and specify a pipeline (see Creating and Managing Query Pipelines).

4.  Send your request.

    It returns something like this:

    ```
    {
    "token":"fzKjcHdjPJKJVaJ2OjK0.fzK2CI6dHJ1ZSwiZXhwIjoxNDY4Njk2NzEwLCJpYXQiOjE0Njg2MTAzMTAsIm9yZ2FuaXphdGlvbiI6InByb2RkYWlseXJhdGxhYiIsInVzZXJJZHMiOlt7InByb3ZpZGVyIjoiRW1haWwgU2VjdXJpdHkgUHJvdmlkZXIiLCJuYW1lIjoidmxhcm9jcXVlQGN..."
    }
    ```

    The token is valid by default for 24 hours.

5.  Use your search token.

    **Example**

    ```
    Authorization: Bearer <a_valid_search_token>
    ```

 

 
