---
layout: content-2-panel
title: API Key Authentication
categories: migrated
toc: ccv2-dev
slug: "5"
---

# API Key Authentication

The most basic way to authenticate a Coveo Cloud V2 REST Search API call is to directly pass an API key in an HTTP header or in the query string of the call.

If your search page is on a public web site and the index it queries contains no secured content, it can be legitimate to authenticate basic Coveo Search API calls using an API key with extremely limited privileges. For instance, if the API key you expose only has the **Execute queries** privilege, then all one can achieve with this API key is to execute queries on the publicly available content of an index. In such a scenario, all users have the same anonymous identity.

However, if your index contains secured sources and you want to impersonate each user so they can see their own legitimate secured content in search results, you must rather use a secret API key with the Impersonate privilege in server-side code to generate expiring search tokens, which you can then safely expose in client-side code (see Search Token Authentication).

> You should never expose an API key with the **Impersonate** privilege in client-side code.

## Using an API Key for Authentication

You can use an API key to authenticate a Coveo Cloud V2 REST Search API call the same way you would use an OAuth2 token: either in the HTTP header or in the query string.

### Passing the API Key in the Header

You can pass the API key as the value of the `Authorization` field in the HTTP header.

**Example: Passing the API Key as an HTTP Header:**

```
Authorization: Bearer MyApiKey
```

Where `MyApiKey` is your actual API Key.

### Passing the API Key as a Request Parameter

You can pass the API key as the value of the `access_token` HTTP request parameter in the query string.

**Example: Passing the API Key as a Request Parameter:**

```
GET https://platform.cloud.coveo.com/rest/search?access_token=myapikey&q=test
```

Where `myapikey` is your actual API key.
