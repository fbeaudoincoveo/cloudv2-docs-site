---
slug: "113"
layout: content-2-panel
title: Search Token Authentication
categories: migrated
toc: ccv2-dev
---

# Search Token Authentication

**In this topic:**

-   [Sample Usage Workflow](#sample-usage-workflow)
-   [Requesting a Search Token](#requesting-a-search-token)
    -   [Sample Request](#sample-request)
    -   [Parameters](#parameters)
        -   [userGroups (array of strings, optional)](#usergroups%C2%A0(array-of-strings,-optional))
        -   [userDisplayName (string, optional)](#userdisplayname%C2%A0(string,-optional))
        -   [searchHub (string, optional)](#searchhub%C2%A0(string,-optional))
        -   [pipeline (string, optional)](#pipeline%C2%A0(string,-optional))
        -   [filter (string, optional)](#filter%C2%A0(string,-optional))
        -   [userIds (array of RestUserId, required)](#userids%C2%A0(array-of-restuserid,-required))
            -   [name (string, required)](#name%C2%A0(string,-required))
            -   [provider (string, required)](#provider%C2%A0(string,-required))
            -   [type (string, optional)](#type%C2%A0(string,-optional))
    -   [Response](#response)
-   [Using a Search Token for Authentication](#using-a-search-token-for-authentication)
    -   [Passing the Search Token in the Header](#passing-the-search-token-in-the-header)
    -   [Passing the Search Token as a Request Parameter](#passing-the-search-token-as-a-request-parameter)

*Search tokens* are special JSON web tokens (see <https://jwt.io/>) which you can only use to execute queries on the Coveo Cloud V2 Platform as a specific user. They are intended to be used in JavaScript code running in the browser, typically along with the Coveo JavaScript Search Framework (see [JavaScript Search Framework Home](https://developers.coveo.com/display/JsSearchV1/JavaScript+Search+Framework+Home)).

A search token automatically expires after a certain amount of time (24 hours).

You can generate search tokens in server-side code by using a certain REST call exposed through the Coveo Cloud V2 Platform (see [Requesting a Search Token](Search_Token_Authentication)).

Typically, you will want to use search token authentication when your search page users are authenticated and some -or all- of your indexed content is secured. Each user then transparently gets a unique search token, allowing the search interface to securely return only items which the user has the right to see (see [Sample Usage Workflow](Search_Token_Authentication)).

## Sample Usage Workflow

Here is a typical workflow demonstrating the use of search tokens.

1.  A user requests a search page from a web server.
2.  The web server executes server-side code that eventually renders the HTML response (PHP, ASP.NET, etc.).
3.  Server-side code authenticates the user who is making the request.
4.  Server-side code sends a REST request to the Coveo Cloud V2 Platform to get a search token for the user it has authenticated (see [Requesting a Search Token](Search_Token_Authentication)). 
5.  The resulting token is used to generate the JavaScript code that initializes the Coveo JavaScript Search Framework in the resulting page (see [JavaScript Search Framework Home](https://developers.coveo.com/display/JsSearchV1/JavaScript+Search+Framework+Home)). 
6.  The server sends the generated HTML to the client.
7.  The JavaScript code initializes the search page and executes the first query, using the provided search token.
8.  The Coveo Cloud V2 Platform executes the query as the user that was previously authenticated by server-side code.
9.  Results are displayed to the user.

## Requesting a Search Token

You can get a search token by sending a `POST` request to `https://platform.cloud.coveo.com/rest/search/token`.

The caller must authenticate using an API key with the Impersonate privilege (see API Keys - Page).

Reminder

> You should always request search tokens in secure, server-side code.

### Sample Request

**Example:**

**A search token creation call in which you only specify the required values**

```
POST https://platform.cloud.coveo.com/rest/search/token?access_token=MY_TOKEN&organizationId=MY_ORG
Content-Type: application/json

{
  "userIds": [
    {
      "name": "john_doe@some-domain.com",
      "provider": "Email Security Provider"
    }
  ]
}
```

### Parameters

The body of a `POST` request to `https://platform.cloud.coveo.com/rest/search/token` is a `RestTokenParams` model which has the following attributes.

#### `userGroups` (array of strings, *optional*)

Specifies the groups the user to associate this search token with belongs to.

A group can be any arbitrary string.

**Example:**

**Body of a search token creation call in which you specify user groups**

```
{
  "userGroups" : [
    "Tech Support",
    "Employee"
  ],
  "userIds" : [
    {
      "name" : "john_doe@some-domain.com",
      "provider" : "Email Security Provider"
    }
  ]
}
```

#### `userDisplayName` (string, *optional*)

Specifies the display name of the user to associate this search token with.

**Example:**

**Body of a search token creation call in which you specify the user display name**

```
{
  "userDisplayName" : "John Doe",
  "userIds" : [
    {
      "name" : "john_doe@some-domain.com",
      "provider" : "Email Security Provider"
    }
  ]
}
```

#### `searchHub` (string, *optional*)

Specifies the search hub to enforce on this search token.

The search hub is an important parameter for the analytics service, the Coveo™ Machine Learning service and the query pipeline.

**Example:**

**Body of a search token creation call in which you specify an enforced searchhub**

```
{
  "searchhub" : "Search",
  "userIds" : [
    {
      "name" : "john_doe@some-domain.com",
      "provider" : "Email Security Provider"
    }
  ]
}
```

#### `pipeline` (string, *optional*)

Specifies the query pipeline to use when performing queries using this search token (see [Creating and Managing Query Pipelines](http://www.coveo.com/go?dest=cloudhelp&lcid=9&context=128)).

If you specify a value for this parameter, the query pipeline you specify takes precedence over the possible output of all other query pipeline routing mechanisms when using this search token (see [Query Pipeline Routing Mechanisms and Rules](http://www.coveo.com/go?dest=cloudhelp&lcid=9&context=164)).

**Example:**

**Body of a search token creation call in which you specify an enforced query pipeline**

```
{
  "pipeline" : "Tech Support Query Pipeline",
  "userIds" : [
    {
      "name" : "john_doe@some-domain.com",
      "provider" : "Email Security Provider"
    }
  ]
}
```

#### `filter` (string, *optional*)

Specifies the query expression filter to add to queries when performing queries using the search token (see [Coveo Query Syntax Reference](http://www.coveo.com/go?dest=adminhelp70&lcid=9&context=10005)).

You can use this value to generate tokens that can only query a subset of the items in an index (e.g., `@objecttype=Case`).

**Example:**

**Body of a search token creation call in which you specify a constant query expression**

```
{
  "filter" : "@objecttype=Case",
  "userIds" : [
    {
      "name" : "john_doe@some-domain.com",
      "provider" : "Email Security Provider"
    }
  ]
}
```

#### `userIds` (array of `RestUserId`, *required*)

The list of `RestUserId` to associate to the search token. The RestUserId model exposes the following attributes.

##### `name` (string, *required*)

Specifies the name of the user ID (e.g., `john_doe@some-domain.com`).

##### `provider` (string, *required*)

Specifies the security provider of the user ID (e.g., `Email Security Provider`).

##### `type` (string, *optional*)

Specifies the type of user ID.

**Example:**

**Body of a search token creation call in which you specify the type of a user ID**

```
{
  "userIds" : [
    {
      "name" : "john_doe@some-domain.com",
      "provider" : "Email Security Provider",
      "type" : "User"
    }
  ]
}
```

> Additionally, the `RestTokenParams` model exposes the`salesforceFallbackToAdmin`, `superUserToken`, `scope`, `salesforceUser`, `expiration` and `salesforceCommunityUrl` attributes, while the `RestUserId` model also exposes the `infos`, `authCookie` and `password` attributes.

> Normally, you should not try to manually specify values for these attributes, as they are either intended for internal use by Coveo, or simply exposed for legacy reasons.

### Response

A successful request produces a JSON response containing the search token.

**Example:**

**A successful token creation call response**

```
{ "token": "fzKjcHdjPJKJVaJ2OjK0fzK2CI6dHJ1ZSwiZXhwIjoxNDY4Njk2NzEwLCJpYXQiOjE0lQGN..." }
```

## Using a Search Token for Authentication

You can use a search token to authenticate a Coveo Cloud V2 REST Search API call the same way you would use an OAuth2 token: either in the HTTP header or in the query string.

### Passing the Search Token in the Header

You can pass the search token as the value of the `Authorization` field in the HTTP header.

**Example:**

**Passing a search token in an HTTP Header**

```
Authorization: Bearer fzKjcHdjPJKJVaJ2OjK0fzK2CI6dHJ1ZSwiZXhwIjoxNDY4Njk2NzEwLCJpYXQiOjE0lQGN...
```

### 
Passing the Search Token as a Request Parameter

You can pass the search token as the value of the `access_token` HTTP request parameter in the query string.

**Example: Passing a Search Token as a Request Parameter:**

```
GET https://platform.cloud.coveo.com/rest/search?access_token=fzKjcHdjPJKJVaJ2OjK0fzK2CI6dHJ1ZSwiZXhwIjoxNDY4Njk2NzEwLCJpYXQiOjE0lQGN...&q=test
```


