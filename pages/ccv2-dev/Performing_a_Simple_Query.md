---
layout: content-2-panel
title: Performing a Simple Query
categories: migrated
toc: ccv2-dev
---

# Performing a Simple Query

Ultimately, the goal of any [Coveo Cloud V2 platform](Glossary_37585054.html#Glossary-CoveoCloudV2Platform) user is to perform [queries](Glossary_37585054.html#Glossary-Query) against a unified, secured [index](Glossary_37585054.html#Glossary-Index) in a specific [Coveo Cloud V2 organization](Glossary_37585054.html#Glossary-CoveoCloudV2Organization), and retrieve the most relevant query result [items](Glossary_37585054.html#Glossary-Item).

You can use the [Search request to the Search API](https://platform.cloud.coveo.com/docs?api=SearchApi#!/Search/post_rest_search) operation to perform a simple query:

```
POST https://platform.cloud.coveo.com/rest/search/v2?organizationId={organizationId}
Content-Type: application/json
Accept: application/json
Authorization: Bearer MyAccessToken
 
{
  "q": "Example"
}
```

Ensure that:

-   You replace `{organizationId}` in the query string by the actual ID of the target Coveo Cloud V2 organization (if the access token you are using to authenticate the call does not implicitly specify the organization it refers to) (see [Getting the organizationId](Getting_the_organizationId)).
-   You replace `MyAccessToken` in the `Authorization` header by an access token that grants the privilege to execute queries in the target organization (see [Getting Your Coveo Cloud V2 Platform Access Token](Getting_Your_Coveo_Cloud_V2_Platform_Access_Token) and [Authentication Methods](Authentication_Methods)).

    Note:

    > You can pass an access token as a query string argument (e.g., `access_token=MyAccessToken`) rather than in an `Authorization` header.

-   You replace the value of the `q` property in the request body by the [basic query expression](Glossary_37585054.html#Glossary-BasicQueryExpression) you want to send to the Search API, such as the keywords an end-user would enter in a search box. 

    **Example:**

    You can pass one or more keywords such as `human resources jobs` to get all source items containing these keywords.

    You can pass an empty request body rather than specifying a `q` value to return all items in the target organization index.

    You can include exact phrase match requests in the `q` value by surrounding groups of keywords with properly escaped double quote characters (e.g., `"q": "Coveo \"Cloud V2\" platform"`).

    Unless you explicitly set the `enableQuerySyntax` property to `false` in the request body, you can also include any valid [Coveo Cloud query syntax](Glossary_37585054.html#Glossary-CoveoCloudQuerySyntax) in the `q` value (e.g., `"q": "Example AND @sourcetype==Web"`).

The body of a successful response contains information about the query itself, such as its `duration` and the `totalCount` of query result items. Most importantly, the response body contains the query `results`.

Note:

> Occasionally, the response body also contains an `executionReport` with detailed debug information.

By default, elements in the `results` array are sorted by *relevancy*: a standard set of ranking rules is applied to compute a `score` value for each query result item; the higher a query result item `score` value is, the lower its 0-based index position in the `results` array will be. There are several ways you can impact the `score` value of query result items. Of course, the Search API also allows you to use other sort criteria than the `score` value, so you should never have to sort query result items client-side.

Each element in the `results` array contains specific information about a single query result item: its `title`, `clickUri`, automatically generated `excerpt`, etc. You can leverage those values to display relevant information when rendering the query results in a graphical search interface. You can also take advantage of the `titleHighlights` and `excerptHighlights` properties to adequately emphasize basic query expression keywords in the title and excerpt.

The `raw` property of each `results` element is also very important, as it holds the [fields](Glossary_37585054.html#Glossary-Field) which were retrieved for this item, and their corresponding values. Each field typically contains specific metadata about an item: its most recent modification `date`, its `size`, the name of its `source`, its `sourceType`, etc. You can explicitly specify which fields to include in (or exclude from) the query result items when performing a query.

**Example:**

**200 OK**

```
{
  "totalCount": 50,
  ...
  "duration": 61,
  ...
  "results": [
    {
      ...
      "title": "Example Domain",
      ...
      "clickUri": "http://www.example.com/",
      ...
      "excerpt": "Example Domain This domain is established to be used for illustrative examples in documents. ...",
      ...
      "score": 4268,
      ...
      "titleHighlights": [
        {
          "length": 7,
          "offset": 0
        }
      ],
      ...
      "excerptHighlights": [
        ...
      ],
      "raw": {
        ...
        "date": 1376092475000,
        "size": 1270,
        "sourcetype": "Web",
        "source": "My web source",
        ...
      }
    },
    ...
  ],
  ...
}
```


