---
slug: "35"
layout: content-2-panel
title: Claims Authentication
categories: migrated
---

# Claims Authentication

**In this topic:**

-   [Configuring Claims Authentication](#configuring-claims-authentication)
    -   [Creating a SharePoint Authentication with the Search API](#creating-a-sharepoint-authentication-with-the-search-api)
    -   [Configuring SharePoint](#configuring-sharepoint)
    -   [Testing Your Setup](#testing-your-setup)
    -   [Configuring your Coveo JavaScript Search Page](#configuring-your-coveo-javascript-search-page)
-   [Step by Step SharePoint Claims Authentication Process](#step-by-step-sharepoint-claims-authentication-process)

When querying items indexed from a SharePoint server relying on claims authentication, it is necessary to obtain certain special information from the SharePoint server to allow the end users to see the items they are allowed to (see [The Claims-Based Identity Model](https://msdn.microsoft.com/en-ca/library/ee517291.aspx)). There is no way for the Coveo index to obtain this information directly from SharePoint; it can only be computed when the querying user is logged into SharePoint. This means that the web browser must perform a round-trip to SharePoint and back before it is possible to query the content.

The Coveo Search API provides a simple process to automate those steps. The only external requirement is that before performing queries, the end user must be redirected to a special URL. The Coveo JavaScript Search Framework provides a component that fulfills this purpose (see the `AuthenticationProvider` component).

## Configuring Claims Authentication

Configuring claims authentication involves creating a SharePoint authentication with the Coveo Search API and configuring the SharePoint server properly.

#### Creating a SharePoint Authentication with the Search API

To create a new SharePoint authentication in your organization using the Coveo Search API, you need to send a `POST` request to `https://platform.cloud.coveo.com/rest/organizations/{organizationId}/authentication/sharepoint`, where you must replace `{organizationId}` with the actual ID of your Coveo Cloud V2 organization.

**Example:**

**A sample SharePoint authentication creation POST request**

```
POST /rest/organizations/myorganizationid/authentication/sharepoint HTTP/1.1
Host: platform.cloud.coveo.com
Content-Type: application/json
Authorization: Bearer MyOAuth2Token
 
{
  "name" : "mySharePointServer1",
  "uri" : "http://hostname.com/_layouts/CES/SearchApiClaims.aspx",
  "provider" : "My SharePoint Claims Security Provider Name",
  "secret" : "k7dbdcu3HMTtdcRtZzx4uLvKB&T9kG8O12cQ2vOcaWiNmerw3RLQLpcCAnPL8wN",
  "expiration" : 86400000
}
```

Parameters

> `name` (string): Specifies the name of the SharePoint server.

> uri (string): Specifies the full URI of the page that serves the claims information.

> provider (string): Specifies the name of the SharePoint security provider in your index configuration.

> `secret` (string): Specifies the string to use to sign claims information (using HMACSHA1). This should be a random string. The longer the string, the more secure.

> `expiration` (integer): Specifies how much time (in milliseconds) it takes for the browser cookie that stores the claims information to expire. If you set this parameter to `0`, the cookie expires at the end of a browser session.

A successful request returns a Status `201 Created` containing the `id` of the SharePoint authentication.

**Example:**

**A sample successful SharePoint authentication creation POST response**

```
Code: 201
 
{
  "id" : "b5g86444-739i-4945-u9z0-0u0hp37n674b"
}
```

You can create multiple SharePoint authentications if necessary.

#### Configuring SharePoint

> The page that can compute claims information is part of the Coveo SharePoint Integration. You must install this package on your SharePoint server before proceeding (see Installing the Coveo Web Service, Search Box, and Search Interface into SharePoint).

In the `web.config` file of your SharePoint site, locate or create the [`appSettings` ](http://msdn.microsoft.com/en-us/library/aa903313(v=vs.71).aspx)element and add the following configuration value:

```
<appSettings>
  <add key="CoveoClaimsSecret" value="k7dbdcu3HMTtdcRtZzx4uLvKB&T9kG8O12cQ2vOcaWiNmerw3RLQLpcCAnPL8wN"/>
</appSettings>
```

The `value` should be the same as the `secret` value of your SharePoint authentication (see [Creating a SharePoint Authentication with the Search API](Claims_Authentication)).

> Recent versions of SharePoint can contain several `appSettings` tags in the `web.config` file. Be sure to add the key inside `appSettings` tag that is the direct child of the main XML element in the file.

#### Testing Your Setup

Once you have created your SharePoint authentication with the Coveo Search API and configured your SharePoint Server, you can test your setup by directing your web browser to `https://platform.cloud.coveo.com/rest/search/login/{provider}`, where you must replace `{provider}` with the `name` of your SharePoint authentication (see [Creating a SharePoint Authentication with the Search API](Claims_Authentication)). You should also specify your `organizationId` in the query string.

**Example:**

**Testing the setup**

```
https://platform.cloud.coveo.com/rest/search/login/mySharePointServer1?organizationId=myorganizationid
```

If everything is setup properly, the Coveo Search API should return a `statusCode 200` containing a success message, along with the claims information that was obtained.

> The `{provider}` value corresponds to the value you passed as the `name` argument when you created your SharePoint authentication using the Coveo Search API. This value is case sensitive. If you misspell your authentication provider name in your `GET` request, you might get a response such as what follows.

**A possible result when misspelling the authentication provider name in the GET request**

```
{ 
  "statusCode" : 500, 
  "message" : "Invalid authentication provider: mysharepointserver1", 
  "type" : "InvalidAuthenticationProviderException", 
  "executionReport" : [
    {}
  ] 
}
```

#### Configuring your Coveo JavaScript Search Page

If you are using the Coveo JavaScript Search Framework, you should add an `AuthenticationProvider` component in the root element of your search interface for each available SharePoint server. The data-name attribute of an AuthenticationProvider component must match precisely the name value of an existing SharePoint authentication created using the Coveo Search API (see [Creating a SharePoint Authentication with the Search API](Claims_Authentication)).

**Example:**

**Configuring three distinct SharePoint authentication providers**

```
<!-- ... -->
 
<body id='search' class='CoveoSearchInterface'>
 
  <!-- ... -->
 
  <div class="CoveoAuthenticationProvider" data-name="mySharePointServer1"></div>
  <div class="CoveoAuthenticationProvider" data-name="mySharePointServer2"></div>
  <div class="CoveoAuthenticationProvider" data-name="mySharePointServer3"></div>
 
  <!-- ... -->
 
</body>
```

> When a Coveo JavaScript Search Framework search page initially loads, it refreshes once per `AuthenticationProvider` component present in the root element of the search interface. It finishes loading normally unless the end user closes the web browser in the meantime.

> If the end user closes and re-opens the web browser, the search page refreshes again. This is because the claims information is stored in a browser cookie. By default, this cookie expires at the end of a browser session.

> If you want the page to load without having to refresh again for each authentication provider, you should pass a value such as `86400000` (which is equivalent to 24 hours) as an `expiration` when creating your SharePoint claims provider using the Coveo Search API. This makes the cookie expire after a set amount of time rather than at the end of a browser session.

This ensures that end users can authenticate with their SharePoint identity. This identity is sent along the query, allowing the index to return SharePoint results that the end user has access to in SharePoint.

If your search page contains a `Tab` component with a `data-expression` attribute (such as the out-of-the-box `SharePoint.html` file), make sure the value of this attribute is set properly.

**Example:**

**Setting The data-expression attribute for a SharePoint Tab**

```
<div class="CoveoTab" data-id="SharePoint" data-caption="SharePoint" data-expression="@sysconnectortype==SharePoint"></div>
```

-   Use `data-expression="@connectortype==SharePoint" `to show in this only search results indexed with the latest SharePoint connector when the user selects this Tab (see [Microsoft SharePoint Connector](http://www.coveo.com/go?dest=adminhelp70&lcid=9&context=4104)).

-   Use `data-expression="@connectortype==SharePointCrawler"` to show only search results indexed with the deprecated SharePoint legacy connector when the user selects this Tab (see [Microsoft SharePoint Legacy Connector](http://www.coveo.com/go?dest=adminhelp70&lcid=9&context=16)).

## 
Step by Step SharePoint Claims Authentication Process

Here is a typical usage scenario involving SharePoint claims authentication.

1.  **The end user navigates to the search page**
    Since the search page is configured to log into the SharePoint authentication provider, the browser is redirected to the login page implemented by the Coveo Search API (e.g., `https://platform.cloud.coveo.com/rest/search/login/mySharePointServer1`).
2.  **The Coveo Search API redirects the end user to SharePoint**
    When a request comes in the login page, the Coveo Search API looks for an existing valid authentication cookie for this provider. If it finds one, the browser is redirected back to the calling page, and queries can then be performed. Otherwise, the browser is redirected again to the page inside SharePoint that computes the claims information (e.g., `http://http://hostname.com/_layouts/CES/SearchApiClaims.aspx`).
3.  **Claims are computed and sent back to the Coveo Search API**
    When the browser tries to load a SharePoint page, the server first authenticates the user, and then loads the page.
    Before computing the claims information, the page validates a special signature passed through the query string to ensure that the calling page is legitimate. Then, using the login information provided by SharePoint, the needed claims information is generated, signed, and sent back to the Coveo Search API using an auto-submitting browser form.
4.  **The Coveo Search API receives claims information and issues a cookie**
    When the Search API receives the claims information from SharePoint, it first validates the signature to ensure it is genuine, and then issues a signed authentication cookie containing the claims information. The cookie also includes login information from the primary authentication provider, to prevent signed claims from being used by another user. The primary authentication provider used depends on your setup. For example, if you are using Windows authentication, the `Windows login` user will be used.
5.  **REST queries are performed by JavaScript code in the browser**
    Afterward, whenever a REST query is performed by JavaScript code, the browser automatically includes the authentication cookie along with the request. If the request specifies that the SharePoint authentication should be used (through the `authentication` query string parameter), the content of the cookie is sent to the index and the appropriate SharePoint items are made visible to the end user.

